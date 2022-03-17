import traceback
from PyQt5.QtCore import QObject, QRunnable, pyqtSignal, pyqtSlot
from pycomm3.exceptions import CommError
from utils.coord_filter.data.comm_plc import read_multiple

from utils.coord_filter.functions.serial_ports import get_my_port, set_my_port
from serial import *

sleep_time = 1.0
stop_time = 0.2


class WorkerParent:
    """Class for shared functions of the workers"""
    def __init__(self):
        self.running = True

    def stop(self):
        """Stops thread"""
        self.running = False
        time.sleep(stop_time)


class WorkerSignals(QObject):
    """
    Defines the signals available from a running worker thread.
    Supported signals are:

    error
        tuple (exctype, value, traceback.format_exc() )
    result
        object data returned from processing, anything
    """
    error = pyqtSignal(tuple)
    result = pyqtSignal(object)
    result_multiples = pyqtSignal(object, object, object, object, object, object)
    result_list = pyqtSignal(list)


class Worker_PLC(QRunnable, WorkerParent):
    """
    Worker thread for multiple signals
    """

    def __init__(self, *args):
        super(Worker_PLC, self).__init__()
        self.running = True
        self.signal_worker = WorkerSignals()

    @pyqtSlot()
    def run(self):
        while self.running:
            try:
                tag_list = ['ConfigPontos', 'DataCtrl_A1', 'DataCtrl_A2', 'DataCtrl_B1', 'DataCtrl_B2', 'HMI']

                tags = read_multiple(tag_list)
                config_pontos = tags[0][1]
                data_ctrl_a1 = tags[1][1]
                data_ctrl_a2 = tags[2][1]
                data_ctrl_b1 = tags[3][1]
                data_ctrl_b2 = tags[4][1]
                HMI = tags[5][1]

                if type(config_pontos) == CommError\
                    or type(data_ctrl_a1) == CommError\
                    or type(data_ctrl_a2) == CommError\
                    or type(data_ctrl_b1) == CommError\
                    or type(data_ctrl_b2) == CommError:
                    traceback.print_exc()
                    exctype, value = sys.exc_info()[:2]
                    self.signal_worker.error.emit((exctype, value, traceback.format_exc()))
                    raise Exception("connection failed")
                else:
                    self.signal_worker.result_multiples.emit(config_pontos,
                                                             data_ctrl_a1,
                                                             data_ctrl_a2,
                                                             data_ctrl_b1,
                                                             data_ctrl_b2,
                                                             HMI)
            except Exception as e:
                print(f'{e} Worker - workers.py')
                time.sleep(3)
            time.sleep(sleep_time)


class Worker_Test(QRunnable, WorkerParent):
    """
    Worker thread for multiple signals
    """

    def __init__(self, *args):
        super(Worker_Test, self).__init__()
        self.running = True
        self.signal_worker_test = WorkerSignals()

    @pyqtSlot()
    def run(self):
        while self.running:
            self.signal_worker_test.result.emit(True)
            time.sleep(sleep_time)


class Worker_BarCodeScanner(QRunnable, WorkerParent):
    """
    Worker thread
    """
    def __init__(self, *args):
        super(Worker_BarCodeScanner, self).__init__()
        self.signal = WorkerSignals()
        self.info: str
        self.code: int
        self.running = True
        self.device_connected = False
        self.create_device()
        self.port = get_my_port()
        self.code_read: str = ""
        self.read_a1: bool = False
        self.read_a2: bool = False
        self.read_b1: bool = False
        self.read_b2: bool = False
        self.read_complete: bool = False
        self.list_signal: list = []

    def create_device(self):
        self.port = get_my_port()
        time.sleep(1)
        try:
            if self.port:
                self.device = Serial(self.port, timeout=0.5)
                self.device_connected = True
                print("Dispositivo conectado")
            else:
                raise Exception("Nenhuma ou mais de uma porta serial encontrada")
        except Exception as e:
            print(e)
            time.sleep(2)

    @pyqtSlot()
    def run(self):
        while self.running:
            if self.device_connected:
                try:
                    if not self.device.isOpen():
                        self.device.open()
                    else:
                        self.info = str(self.device.readline())
                        self.code_size = len(self.info)
                        if self.code_size > 4:
                            self.code_read = self.info[2:(self.code_size - 3)]
                            print(f"Código do leitor: {self.code_read}")
                            if self.code_read == "A1":
                                self.read_a1 = True
                                self.read_a2 = False
                                self.read_b1 = False
                                self.read_b2 = False
                            elif self.code_read == "A2":
                                self.read_a1 = False
                                self.read_a2 = True
                                self.read_b1 = False
                                self.read_b2 = False
                            elif self.code_read == "B1":
                                self.read_a1 = False
                                self.read_a2 = False
                                self.read_b1 = True
                                self.read_b2 = False
                            elif self.code_read == "B2":
                                self.read_a1 = False
                                self.read_a2 = False
                                self.read_b1 = False
                                self.read_b2 = True
                            elif self.read_a1:
                                self.list_signal = [self.code_read, "A1"]
                                self.signal.result_list.emit(self.list_signal)
                                self.read_a1 = False
                            elif self.read_a2:
                                self.list_signal = [self.code_read, "A2"]
                                self.signal.result_list.emit(self.list_signal)
                                self.read_a2 = False
                            elif self.read_b1:
                                self.list_signal = [self.code_read, "B1"]
                                self.signal.result_list.emit(self.list_signal)
                                self.read_b1 = False
                            elif self.read_b2:
                                self.list_signal = [self.code_read, "B2"]
                                self.signal.result_list.emit(self.list_signal)
                                self.read_b2 = False

                            self.signal.result.emit({"DataPy": self.code_read, "ReadComplete": True,
                                                     "Connected": self.device_connected})
                            time.sleep(1)
                            self.signal.result.emit({"DataPy": self.code_read, "ReadComplete": False,
                                                     "Connected": self.device_connected})

                except SerialException:
                    print(f"Dispotivo desconectado da porta {self.port}")
                    self.device.close()
                    self.device_connected = False
                    set_my_port("")
                except Exception as e:
                    print(f"{e} - Worker_BarCodeScanner")
                    self.device.close()
                    self.device_connected = False
            else:
                self.create_device()
            try:
                self.signal.result.emit({"Connected": self.device_connected})
            except RuntimeError as e:
                print("Erro de execução no worker do leitor de código de barras: ", e)


class Worker_CreateTable(QRunnable, WorkerParent):
    """
    Worker thread for multiple signals
    """

    def __init__(self, *args):
        super(Worker_CreateTable, self).__init__()
        self.signal = WorkerSignals()

    @pyqtSlot()
    def run(self):
        self.signal.result.emit(True)
        time.sleep(sleep_time)
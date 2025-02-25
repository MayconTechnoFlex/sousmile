"""Runnable Workers para controle do Filtro de Coordenadas"""
#######################################################################################################
# Importações
#######################################################################################################
import traceback
from PyQt5.QtCore import QObject, QRunnable, pyqtSignal, pyqtSlot
from pycomm3.exceptions import CommError
from utils.functions.ctrl_plc import read_multiples, write_tag
from utils.functions.serial_ports import get_my_port, set_my_port
from serial import *

from utils.operator import set_operator
#######################################################################################################
# Definição das variáveis globais
#######################################################################################################
sleep_time = 1.0
stop_time = 0.2
#######################################################################################################
# Workers Base
#######################################################################################################
class WorkerParent:
    """Classe compartilhada entre Workers"""
    def __init__(self):
        self.running = True

    def stop(self):
        """Para o Worker"""
        self.running = False
        time.sleep(stop_time)
#######################################################################################################
class WorkerSignals(QObject):
    """
    Define os sinais disponiveis para um Running Worker.

    Os sinais suportados são:

    error:
        tuple (exctype, value, traceback.format_exc() )
    result:
        object data returned from processing, anything
    result_multiples:
        5 objects returned from processing
    result_list:
        list with results
    """
    error = pyqtSignal(tuple)
    result = pyqtSignal(object)
    result_multiples = pyqtSignal(object, object, object, object, object, object)
    result_list = pyqtSignal(list)
#######################################################################################################
# Workers
#######################################################################################################
class Worker_PLC(QRunnable, WorkerParent):
    """Worker para multiplos sinais"""

    def __init__(self, *args):
        super(Worker_PLC, self).__init__()
        self.running = True
        self.signal_worker = WorkerSignals()

    @pyqtSlot()
    def run(self):
        while self.running:
            try:
                tag_list = ['ConfigPontos', 'DataCtrl_A1', 'DataCtrl_A2', 'DataCtrl_B1', 'DataCtrl_B2', 'HMI']

                tags = read_multiples(tag_list)
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
#######################################################################################################
class Worker_Test(QRunnable, WorkerParent):
    """Worker para Arquivo Teste"""

    def __init__(self, *args):
        super(Worker_Test, self).__init__()
        self.running = True
        self.signal_worker_test = WorkerSignals()

    @pyqtSlot()
    def run(self):
        while self.running:
            self.signal_worker_test.result.emit(True)
            time.sleep(sleep_time)
#######################################################################################################
class Worker_BarCodeScanner(QRunnable, WorkerParent):
    """Worker para leitura do Leitor de Código de Barras"""

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
                            if self.code_read[0] == "#":
                                # the code must be in this format: '#Name_Surname&ID' e.g. "#John_Doe&0001"
                                strIndex1 = self.code_read.index('_')
                                strIndex2 = self.code_read.index('&')

                                name = self.code_read[1:strIndex1]
                                surname = self.code_read[strIndex1 + 1:strIndex2]
                                employee_name = f"{name.capitalize()} {surname.capitalize()}"

                                employee_id = self.code_read[strIndex2 + 1:]

                                print(f"Usuário conectado: {employee_name}")
                                set_operator(employee_name, employee_id)
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
#######################################################################################################
class Worker_CreateTable(QRunnable, WorkerParent):
    """Worker para Criar Tabela"""

    def __init__(self, *args):
        super(Worker_CreateTable, self).__init__()
        self.signal = WorkerSignals()

    @pyqtSlot()
    def run(self):
        self.signal.result.emit(True)
        time.sleep(sleep_time)
#######################################################################################################
class Worker_RunTest(QRunnable, WorkerParent):
    def __init__(self):
        super(Worker_RunTest, self).__init__()
        self.signal = WorkerSignals()

    @pyqtSlot()
    def run(self):
        self.signal.result.emit(True)
        time.sleep(sleep_time)
#######################################################################################################

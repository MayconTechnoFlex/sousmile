"""Workers for actualize GUI with PLC Information"""

import time, traceback, sys

from pycomm3.exceptions import CommError
from PyQt5.QtCore import QObject, QRunnable, pyqtSignal, pyqtSlot
from utils.ctrl_plc import read_tags

sleep_time = 0.75
stop_time = 0.2

class WorkerParent:
    """Class for shared functions of the workers"""
    def __init__(self):
        super(WorkerParent, self).__init__()
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

class Worker(QRunnable, WorkerParent):
    """
    Worker thread for multiple signals
    """

    def __init__(self, *args):
        super(Worker, self).__init__()
        self.signal_barCodeReader = WorkerSignals()
        self.signal_local1In = WorkerSignals()
        self.signal_local1Out = WorkerSignals()
        self.signal_local2In = WorkerSignals()
        self.running = True

    @pyqtSlot()
    def run(self):
        while self.running:
            try:
                bar_code_reader = read_tags("BarCodeReader")
                local_1_in = read_tags("Local:1:I.Data")
                local_1_out = read_tags("Local:1:O.Data")
                local_2_in = read_tags("Local:2:I.Data")

                if type(bar_code_reader) == CommError:
                    traceback.print_exc()
                    exctype, value = sys.exc_info()[:2]
                    self.signal_barCodeReader.error.emit((exctype, value, traceback.format_exc()))
                    self.signal_local1In.error.emit((exctype, value, traceback.format_exc()))
                    self.signal_local1Out.error.emit((exctype, value, traceback.format_exc()))
                    self.signal_local2In.error.emit((exctype, value, traceback.format_exc()))
                    raise Exception("connection failed")
                else:
                    self.signal_barCodeReader.result.emit(bar_code_reader)
                    self.signal_local1In.result.emit(local_1_in)
                    self.signal_local1Out.result.emit(local_1_out)
                    self.signal_local2In.result.emit(local_2_in)

            except Exception as e:
                print(f'{e} - workers.py')
                self.stop()
                break
            time.sleep(sleep_time)

class Worker_Data_Ctrl_A1(QRunnable, WorkerParent):
    """
    Worker thread
    """

    def __init__(self, *args):
        super(Worker_Data_Ctrl_A1, self).__init__()
        self.signal_a1 = WorkerSignals()
        self.running = True

    @pyqtSlot()
    def run(self):
        while self.running:
            try:
                data_ctrl_a1 = read_tags('DataCtrl_A1')

                if type(data_ctrl_a1) == CommError:
                    traceback.print_exc()
                    exctype, value = sys.exc_info()[:2]
                    self.signal_a1.error.emit((exctype, value, traceback.format_exc()))
                    raise Exception("connection failed")
                else:
                    self.signal_a1.result.emit(data_ctrl_a1)
            except Exception as e:
                print(f'{e} - in workers.py')
                self.stop()
                break
            time.sleep(sleep_time)

class Worker_Data_Ctrl_A2(QRunnable, WorkerParent):
    """
    Worker thread
    """

    def __init__(self, *args):
        super(Worker_Data_Ctrl_A2, self).__init__()
        self.signal_a2 = WorkerSignals()
        self.running = True

    @pyqtSlot()
    def run(self):
        while self.running:
            try:
                data_ctrl_a2 = read_tags('DataCtrl_A2')

                if type(data_ctrl_a2) == CommError:
                    traceback.print_exc()
                    exctype, value = sys.exc_info()[:2]
                    self.signal_a2.error.emit((exctype, value, traceback.format_exc()))
                    raise Exception("connection failed")
                else:
                    self.signal_a2.result.emit(data_ctrl_a2)
            except Exception as e:
                print(f'{e} - in workers.py')
                self.stop()
                break
            time.sleep(sleep_time)

class Worker_Data_Ctrl_B1(QRunnable, WorkerParent):
    """
    Worker thread
    """

    def __init__(self, *args):
        super(Worker_Data_Ctrl_B1, self).__init__()
        self.signal_b1 = WorkerSignals()
        self.running = True

    @pyqtSlot()
    def run(self):
        while self.running:
            try:
                data_ctrl_b1 = read_tags('DataCtrl_B1')

                if type(data_ctrl_b1) == CommError:
                    traceback.print_exc()
                    exctype, value = sys.exc_info()[:2]
                    self.signal_b1.error.emit((exctype, value, traceback.format_exc()))
                    raise Exception("connection failed")
                else:
                    self.signal_b1.result.emit(data_ctrl_b1)
            except Exception as e:
                print(f'{e} - in workers.py')
                self.stop()
                break
            time.sleep(sleep_time)

class Worker_Data_Ctrl_B2(QRunnable, WorkerParent):
    """
    Worker thread
    """

    def __init__(self, *args):
        super(Worker_Data_Ctrl_B2, self).__init__()
        self.signal_b2 = WorkerSignals()
        self.running = True

    @pyqtSlot()
    def run(self):
        while self.running:
            try:
                data_ctrl_b2 = read_tags('DataCtrl_B2')

                if type(data_ctrl_b2) == CommError:
                    traceback.print_exc()
                    exctype, value = sys.exc_info()[:2]
                    self.signal_b2.error.emit((exctype, value, traceback.format_exc()))
                    raise Exception("connection failed")
                else:
                    self.signal_b2.result.emit(data_ctrl_b2)
            except Exception as e:
                print(f'{e} - in workers.py')
                self.stop()
                break
            time.sleep(sleep_time)

class Worker_HMI(QRunnable, WorkerParent):
    """
    Worker thread
    """

    def __init__(self, *args):
        super(Worker_HMI, self).__init__()
        self.signal_hmi = WorkerSignals()
        self.running = True

    @pyqtSlot()
    def run(self):
        while self.running:
            try:
                hmi = read_tags('HMI')

                if type(hmi) == CommError:
                    traceback.print_exc()
                    exctype, value = sys.exc_info()[:2]
                    self.signal_hmi.error.emit((exctype, value, traceback.format_exc()))
                    raise Exception("connection failed")
                else:
                    self.signal_hmi.result.emit(hmi)
            except Exception as e:
                print(f'{e} - in workers.py')
                self.stop()
                break
            time.sleep(sleep_time)

class Worker_Config_Pts(QRunnable, WorkerParent):
    """
    Worker thread
    """

    def __init__(self, *args):
        super(Worker_Config_Pts, self).__init__()
        self.signal_configPts = WorkerSignals()
        self.running = True

    @pyqtSlot()
    def run(self):
        while self.running:
            try:
                config_pts = read_tags("ConfigPontos")

                if type(config_pts) == CommError:
                    traceback.print_exc()
                    exctype, value = sys.exc_info()[:2]
                    self.signal_configPts.error.emit((exctype, value, traceback.format_exc()))
                    raise Exception("connection failed")
                else:
                    self.signal_configPts.result.emit(config_pts)
            except Exception as e:
                print(f'{e} - in workers.py')
                self.stop()
                break
            time.sleep(sleep_time)

class Worker_Cyl_Door_A(QRunnable, WorkerParent):
    """
    Worker thread
    """

    def __init__(self, *args):
        super(Worker_Cyl_Door_A, self).__init__()
        self.signal_cylDoorA = WorkerSignals()
        self.running = True

    @pyqtSlot()
    def run(self):
        while self.running:
            try:
                cyl_door_a = read_tags("Cyl_DoorSideA")

                if type(cyl_door_a) == CommError:
                    traceback.print_exc()
                    exctype, value = sys.exc_info()[:2]
                    self.signal_cylDoorA.error.emit((exctype, value, traceback.format_exc()))
                    raise Exception("connection failed")
                else:
                    self.signal_cylDoorA.result.emit(cyl_door_a)
            except Exception as e:
                print(f'{e} - in workers.py')
                self.stop()
                break
            time.sleep(sleep_time)

class Worker_Cyl_Door_B(QRunnable, WorkerParent):
    """
    Worker thread
    """

    def __init__(self, *args):
        super(Worker_Cyl_Door_B, self).__init__()
        self.signal_cylDoorB = WorkerSignals()
        self.running = True

    @pyqtSlot()
    def run(self):
        while self.running:
            try:
                cyl_door_b = read_tags("Cyl_DoorSideB")

                if type(cyl_door_b) == CommError:
                    traceback.print_exc()
                    exctype, value = sys.exc_info()[:2]
                    self.signal_cylDoorB.error.emit((exctype, value, traceback.format_exc()))
                    raise Exception("connection failed")
                else:
                    self.signal_cylDoorB.result.emit(cyl_door_b)
            except Exception as e:
                print(f'{e} - in workers.py')
                self.stop()
                break
            time.sleep(sleep_time)

class Worker_Cyl_Spindle(QRunnable, WorkerParent):
    """
    Worker thread
    """

    def __init__(self, *args):
        super(Worker_Cyl_Spindle, self).__init__()
        self.signal_cylSpindle = WorkerSignals()
        self.running = True

    @pyqtSlot()
    def run(self):
        while self.running:
            try:
                cyl_spindle = read_tags("Cyl_SpindleRobo")

                if type(cyl_spindle) == CommError:
                    traceback.print_exc()
                    exctype, value = sys.exc_info()[:2]
                    self.signal_cylSpindle.error.emit((exctype, value, traceback.format_exc()))
                    raise Exception("connection failed")
                else:
                    self.signal_cylSpindle.result.emit(cyl_spindle)
            except Exception as e:
                print(f'{e} - in workers.py')
                self.stop()
                break
            time.sleep(sleep_time)

class Worker_Robot_Inputs(QRunnable, WorkerParent):
    """
    Worker thread
    """

    def __init__(self, *args):
        super(Worker_Robot_Inputs, self).__init__()
        self.signal_roboInput = WorkerSignals()
        self.running = True

    @pyqtSlot()
    def run(self):
        while self.running:
            try:
                robo_input = read_tags("Robo.Input")

                if type(robo_input) == CommError:
                    traceback.print_exc()
                    exctype, value = sys.exc_info()[:2]
                    self.signal_roboInput.error.emit((exctype, value, traceback.format_exc()))
                    raise Exception("connection failed")
                else:
                    self.signal_roboInput.result.emit(robo_input)
            except Exception as e:
                print(f'{e} - in workers.py')
                self.stop()
                break
            time.sleep(sleep_time)

class Worker_Robot_Outputs(QRunnable, WorkerParent):
    """
    Worker thread
    """

    def __init__(self, *args):
        super(Worker_Robot_Outputs, self).__init__()
        self.signal_robotOutput = WorkerSignals()
        self.running = True

    @pyqtSlot()
    def run(self):
        while self.running:
            try:
                robo_output = read_tags("Robo.Output")

                if type(robo_output) == CommError:
                    traceback.print_exc()
                    exctype, value = sys.exc_info()[:2]
                    self.signal_robotOutput.error.emit((exctype, value, traceback.format_exc()))
                    raise Exception("connection failed")
                else:
                    self.signal_robotOutput.result.emit(robo_output)
            except Exception as e:
                print(f'{e} - in workers.py')
                self.stop()
                break
            time.sleep(sleep_time)

class Worker_IndexRobotPos(QRunnable, WorkerParent):
    """
    Worker thread
    """

    def __init__(self, *args):
        super(Worker_IndexRobotPos, self).__init__()
        self.signal_indexRobotPos = WorkerSignals()
        self.running = True

    @pyqtSlot()
    def run(self):
        """
        Code for this function
        :return:
        """
        while self.running:
            try:
                index_robot_pos = read_tags("IndexRobotPos")

                if type(index_robot_pos) == CommError:
                    traceback.print_exc()
                    exctype, value = sys.exc_info()[:2]
                    self.signal_indexRobotPos.error.emit((exctype, value, traceback.format_exc()))
                    raise Exception("connection failed")
                else:
                    self.signal_indexRobotPos.result.emit(index_robot_pos)
            except Exception as e:
                print(f'{e} - in workers.py')
                self.stop()
                break
            time.sleep(sleep_time)

import time

from PyQt5.QtCore import QObject, QRunnable, pyqtSignal, pyqtSlot, QMutex
from utils.ctrl_plc import read_tags

sleep_time = 0.75


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

class Worker(QRunnable):
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

                self.signal_barCodeReader.result.emit(bar_code_reader)
                self.signal_local1In.result.emit(local_1_in)
                self.signal_local1Out.result.emit(local_1_out)
                self.signal_local2In.result.emit(local_2_in)

            except Exception as e:
                print(f'{e} - Error on the thread')

            time.sleep(sleep_time)

    def stop(self):
        self.running = False

class Worker_Data_Ctrl_A1(QRunnable):
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
                self.signal_a1.result.emit(data_ctrl_a1)
            except Exception as e:
                print(f'{e} - Error on the thread')

            time.sleep(sleep_time)

    def stop(self):
        self.running = False

class Worker_Data_Ctrl_A2(QRunnable):
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
                self.signal_a2.result.emit(data_ctrl_a2)
            except Exception as e:
                print(f'{e} - Error on the thread')

            time.sleep(sleep_time)

    def stop(self):
        self.running = False

class Worker_Data_Ctrl_B1(QRunnable):
    """
    Worker thread
    """

    def __init__(self, *args):
        super(Worker_Data_Ctrl_B1, self).__init__()
        self.signal_b1 = WorkerSignals()
        self.running = True

    @pyqtSlot()
    def run(self):
        while True: #self.running:
            try:
                data_ctrl_b1 = read_tags('DataCtrl_B1')
                self.signal_b1.result.emit(data_ctrl_b1)
            except Exception as e:
                print(f'{e} - Error on the thread')

            time.sleep(sleep_time)

    def stop(self):
        self.running = False

class Worker_Data_Ctrl_B2(QRunnable):
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
                self.signal_b2.result.emit(data_ctrl_b2)
            except Exception as e:
                print(f'{e} - Error on the thread')

            time.sleep(sleep_time)

    def stop(self):
        self.running = False

class Worker_HMI(QRunnable):
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
                self.signal_hmi.result.emit(hmi)
            except Exception as e:
                print(f'{e} - Error on the thread')

            time.sleep(sleep_time)

    def stop(self):
        self.running = False

class Worker_Config_Pts(QRunnable):
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
                self.signal_configPts.result.emit(config_pts)
            except Exception as e:
                print(f'{e} - Error on the thread')

            time.sleep(sleep_time)

    def stop(self):
        self.running = False

class Worker_Cyl_Door_A(QRunnable):
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
                self.signal_cylDoorA.result.emit(cyl_door_a)
            except Exception as e:
                print(f'{e} - Error on the thread')

            time.sleep(sleep_time)

    def stop(self):
        self.running = False

class Worker_Cyl_Door_B(QRunnable):
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
                self.signal_cylDoorB.result.emit(cyl_door_b)
            except Exception as e:
                print(f'{e} - Error on the thread')

            time.sleep(sleep_time)

    def stop(self):
        self.running = False

class Worker_Cyl_Spindle(QRunnable):
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
                self.signal_cylSpindle.result.emit(cyl_spindle)
            except Exception as e:
                print(f'{e} - Error on the thread')

            time.sleep(sleep_time)

    def stop(self):
        self.running = False

class Worker_Robot_Inputs(QRunnable):
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
                self.signal_roboInput.result.emit(robo_input)
            except Exception as e:
                print(f'{e} - Error on the thread')

            time.sleep(sleep_time)

    def stop(self):
        self.running = False

class Worker_Robot_Outputs(QRunnable):
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
                self.signal_robotOutput.result.emit(robo_output)
            except Exception as e:
                print(f'{e} - Error on the thread')

            time.sleep(sleep_time)

    def stop(self):
        self.running = False

class Worker_IndexRobotPos(QRunnable):
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
                self.signal_indexRobotPos.result.emit(index_robot_pos)
            except Exception as e:
                print(f'{e} - Error on the thread')

            time.sleep(sleep_time)

    def stop(self):
        self.running = False

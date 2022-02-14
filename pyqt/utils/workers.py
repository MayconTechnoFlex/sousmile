from PyQt5.QtCore import QObject, QRunnable, pyqtSignal, pyqtSlot
from utils.ctrl_plc import read_tags


class WorkerSignals(QObject):
    """
    Defines the signals available from a running worker thread.

    Supported signals are:

    finished
        No data

    error
        tuple (exctype, value, traceback.format_exc() )

    result
        object data returned from processing, anything

    """
    finished = pyqtSignal()
    error = pyqtSignal(tuple)
    result = pyqtSignal(object)


class Worker(QRunnable):
    """
    Worker thread
    """

    def __init__(self, *args):
        super(Worker, self).__init__()
        #############################################
        ## Add signal
        #############################################
        self.signal_a1 = WorkerSignals()
        self.signal_a2 = WorkerSignals()
        self.signal_b1 = WorkerSignals()
        self.signal_b2 = WorkerSignals()
        self.signal_hmi = WorkerSignals()
        self.signal_configPts = WorkerSignals()
        self.signal_cylDoorA = WorkerSignals()
        self.signal_cylDoorB = WorkerSignals()
        self.signal_indexRobotPos = WorkerSignals()
        self.signal_roboInput = WorkerSignals()
        self.signal_robotOutput = WorkerSignals()
        self.signal_barCodeReader = WorkerSignals()
        self.signal_cylSpindle = WorkerSignals()
        self.signal_local1In = WorkerSignals()
        self.signal_local1Out = WorkerSignals()
        self.signal_local2In = WorkerSignals()

    @pyqtSlot()
    def run(self):
        """
        Code for this function
        :return:
        """

        try:
            data_ctrl_a1 = read_tags('DataCtrl_A1')
            data_ctrl_a2 = read_tags('DataCtrl_A2')
            data_ctrl_b1 = read_tags('DataCtrl_B1')
            data_ctrl_b2 = read_tags('DataCtrl_B2')
            hmi = read_tags('HMI')
            config_pts = read_tags("ConfigPontos")
            cyl_door_a = read_tags("Cyl_DoorSideA")
            cyl_door_b = read_tags("Cyl_DoorSideB")
            cyl_spindle = read_tags("Cyl_SpindleRobo")
            index_robot_pos = read_tags("IndexRobotPos")
            robo_input = read_tags("Robo.Input")
            robo_output = read_tags("Robo.Output")
            bar_code_reader = read_tags("BarCodeReader")
            local_1_in = read_tags("Local:1:I.Data")
            local_1_out = read_tags("Local:1:O.Data")
            local_2_in = read_tags("Local:2:I.Data")

            self.signal_a1.result.emit(data_ctrl_a1)
            self.signal_a2.result.emit(data_ctrl_a2)
            self.signal_b1.result.emit(data_ctrl_b1)
            self.signal_b2.result.emit(data_ctrl_b2)
            self.signal_hmi.result.emit(hmi)
            self.signal_configPts.result.emit(config_pts)
            self.signal_cylDoorA.result.emit(cyl_door_a)
            self.signal_cylDoorB.result.emit(cyl_door_b)
            self.signal_cylSpindle.result.emit(cyl_spindle)
            self.signal_indexRobotPos.result.emit(index_robot_pos)
            self.signal_roboInput.result.emit(robo_input)
            self.signal_robotOutput.result.emit(robo_output)
            self.signal_barCodeReader.result.emit(bar_code_reader)
            self.signal_local1In.result.emit(local_1_in)
            self.signal_local1Out.result.emit(local_1_out)
            self.signal_local2In.result.emit(local_2_in)
        except:
            print('Error on the thread')

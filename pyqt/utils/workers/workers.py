"""Workers para atualização da aplicação com dados do CLP"""
#######################################################################################################
# Importações
#######################################################################################################
import time, traceback, sys

from typing import Union

from pycomm3.exceptions import CommError
from PyQt5.QtCore import QObject, QRunnable, pyqtSignal, pyqtSlot, Qt
from PyQt5.QtWidgets import QWidget, QApplication
from utils.functions.ctrl_plc import read_tags, read_multiples, write_tag
from utils.Tags import *
#######################################################################################################
# Definição das variáveis globais
#######################################################################################################
sleep_time = 0.8
stop_time = 0.2
#######################################################################################################
# Classes Base
#######################################################################################################
class WorkerParent:
    """Classe compartilhada entre Workers"""
    def __init__(self):
        super(WorkerParent, self).__init__()
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
    """
    error = pyqtSignal(tuple)
    result = pyqtSignal(object)
#######################################################################################################
# Classes funcionais
#######################################################################################################
# DataCtrl
#######################################################################################################
class Worker_Data_Ctrl_A1(QRunnable, WorkerParent):
    """Worker para receber dados da tag "DataCtrl_A1" do CLP"""

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
                print(f'{e} Worker_Data_Ctrl_A1 - in workers.py')
                # self.stop()
                # break
            time.sleep(sleep_time)
#######################################################################################################
class Worker_Data_Ctrl_A2(QRunnable, WorkerParent):
    """Worker para receber dados da tag "DataCtrl_A2" do CLP"""

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
                print(f'{e} Worker_Data_Ctrl_A2 - in workers.py')
                # self.stop()
                # break
            time.sleep(sleep_time)
#######################################################################################################
class Worker_Data_Ctrl_B1(QRunnable, WorkerParent):
    """Worker para receber dados da tag "DataCtrl_B1" do CLP"""


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
                print(f'{e} Worker_Data_Ctrl_B1 - in workers.py')
                # self.stop()
                # break
            time.sleep(sleep_time)
#######################################################################################################
class Worker_Data_Ctrl_B2(QRunnable, WorkerParent):
    """Worker para receber dados da tag "DataCtrl_B2" do CLP"""


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
                print(f'{e} Worker_Data_Ctrl_B2 - in workers.py')
                # self.stop()
                # break
            time.sleep(sleep_time)
#######################################################################################################
# HMI
#######################################################################################################
class Worker_HMI(QRunnable, WorkerParent):
    """Worker para receber dados da tag "HMI" do CLP"""

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
                print(f'{e} Worker_HMI - in workers.py')
                # self.stop()
                # break
            time.sleep(sleep_time)
#######################################################################################################
# Config pontos e Cyl
#######################################################################################################
class Worker_Config_Pts(QRunnable, WorkerParent):
    """Worker para receber dados da tag "ConfigPontos" do CLP"""

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
                print(f'{e} Worker_Config_Pts - in workers.py')
                # self.stop()
                # break
            time.sleep(sleep_time)
#######################################################################################################
class Worker_Cyl_Door_A(QRunnable, WorkerParent):
    """Worker para receber dados da tag "Cyl_DoorSideA" do CLP"""

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
                print(f'{e} Worker_Cyl_Door_A - in workers.py')
                # self.stop()
                # break
            time.sleep(sleep_time)
#######################################################################################################
class Worker_Cyl_Door_B(QRunnable, WorkerParent):
    """Worker para receber dados da tag "Cyl_DoorSideB" do CLP"""

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
                print(f'{e} Worker_Cyl_Door_B - in workers.py')
                # self.stop()
                # break
            time.sleep(sleep_time)
#######################################################################################################
class Worker_Cyl_Spindle(QRunnable, WorkerParent):
    """Worker para receber dados da tag "Cyl_SpindleRobo" do CLP"""

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
                print(f'{e} Worker_Cyl_Spindle - in workers.py')
                # self.stop()
                # break
            time.sleep(sleep_time)
#######################################################################################################
# Robô
#######################################################################################################
class Worker_Robot_Inputs(QRunnable, WorkerParent):
    """Worker para receber dados da tag "Robo.Input" do CLP"""

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
                print(f'{e} Worker_Robot_Inputs - in workers.py')
                # self.stop()
                # break
            time.sleep(sleep_time)
#######################################################################################################
class Worker_Robot_Outputs(QRunnable, WorkerParent):
    """Worker para receber dados da tag "Robo.Output" do CLP"""

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
                print(f'{e} Worker_Robot_Outputs - in workers.py')
                # self.stop()
                # break
            time.sleep(sleep_time)
#######################################################################################################
class Worker_IndexRobotPos(QRunnable, WorkerParent):
    """Worker para receber dados da tag "IndexRobotPos" do CLP"""

    def __init__(self, *args):
        super(Worker_IndexRobotPos, self).__init__()
        self.signal_indexRobotPos = WorkerSignals()
        self.running = True

    @pyqtSlot()
    def run(self):
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
                print(f'{e} Worker_IndexRobotPos - in workers.py')
                # self.stop()
                # break
            time.sleep(sleep_time)
#######################################################################################################
# Tags List
#######################################################################################################
class Worker_Alarms(QRunnable, WorkerParent):
    """Worker para receber dados do CLP referentes às tags na TagList de Alarmes"""

    def __init__(self):
        super(Worker_Alarms, self).__init__()
        self.signal_alarm = WorkerSignals()

    @pyqtSlot()
    def run(self):
        while self.running:
            try:
                alarm_list = read_multiples(alarm_tag_list)

                if type(alarm_list) == CommError:
                    traceback.print_exc()
                    exctype, value = sys.exc_info()[:2]
                    self.signal_alarm.error.emit((exctype, value, traceback.format_exc()))
                    raise Exception("connection failed")
                else:
                    self.signal_alarm.result.emit(alarm_list)
            except Exception as e:
                print(f'{e} Worker_Alarms - in workers.py')
                # self.stop()
                # break
            time.sleep(sleep_time)
#######################################################################################################
class Worker_InOut(QRunnable, WorkerParent):
    """Worker para receber dados do CLP referentes às tags na TagList de Entradas e Saídas (InOut)"""

    def __init__(self):
        super(Worker_InOut, self).__init__()
        self.signal_inOut = WorkerSignals()

    @pyqtSlot()
    def run(self):
        while self.running:
            try:
                inOut_list = read_multiples(tags_inOut)

                if type(inOut_list) == CommError:
                    traceback.print_exc()
                    exctype, value = sys.exc_info()[:2]
                    self.signal_inOut.error.emit((exctype, value, traceback.format_exc()))
                    raise Exception("connection failed")
                else:
                    self.signal_inOut.result.emit(inOut_list)
            except Exception as e:
                print(f'{e} Worker_InOut - in workers.py')
                # self.stop()
                # break
            time.sleep(sleep_time)
#######################################################################################################
class Worker_User(QRunnable, WorkerParent):
    """Worker para verificar conexão do usuário"""

    def __init__(self):
        super(Worker_User, self).__init__()
        self.signal_user = WorkerSignals()

    @pyqtSlot()
    def run(self):
        while self.running:
            signal = True
            try:
                self.signal_user.result.emit(signal)
                time.sleep(0.2)
            except Exception as e:
                print(f'{e} - User worker')
#######################################################################################################
class Worker_ReadTags(QRunnable, WorkerParent):
    """Worker para receber dados do CLP referentes às tags na TagList Geral, levando esses dados à diversos locais"""

    def __init__(self):
        super(Worker_ReadTags, self).__init__()
        self.signal_ReadTags = WorkerSignals()
        self.running = True

    @pyqtSlot()
    def run(self):
        while self.running:
            try:
                tag = read_multiples(Tag_List)

                if type(tag) == CommError:
                    traceback.print_exc()
                    exctype, value = sys.exc_info()[:2]
                    self.signal_ReadTags.error.emit((exctype, value, traceback.format_exc()))
                    raise Exception("connection failed")
                else:
                    self.signal_ReadTags.result.emit(tag)
            except Exception as e:
                print(f'{e} - Read Tags Worker')
                # self.stop()
                # break
            time.sleep(sleep_time)
#######################################################################################################
# Escrita de Tags
#######################################################################################################

class Worker_WriteTags(QRunnable, WorkerParent, QObject):
    def __init__(self, tag: str, value, widget: QWidget = None):
        """
        Worker para escrever dados no CLP

        :param tag: String da Tag que será escrita
        :param value: Valor a ser escrito
        :param widget: (opcional) Widget a ser bloqueado enquanto é escrito no CLP
        """
        super(Worker_WriteTags, self).__init__()
        self.tag = tag
        self.value = value
        self.widget = widget

    @pyqtSlot()
    def run(self):
        try:
            if self.widget:
                QApplication.setOverrideCursor(Qt.WaitCursor)
                self.widget.setEnabled(False)
            write_tag(self.tag, self.value)
        except Exception as e:
            print(f'{e} - Write Tags Worker')
        finally:
            if self.widget:
                self.widget.setEnabled(True)
                QApplication.restoreOverrideCursor()

#######################################################################################################
class Worker_Pressed_WriteTags(QRunnable, WorkerParent):
    def __init__(self, tag: str, value):
        """
        Worker para escrever dados no CLP enquanto um botão é pressionado

        :param tag: String da Tag que será escrita
        :param value: Valor a ser escrito
        """
        super(Worker_Pressed_WriteTags, self).__init__()
        self.tag = tag
        self.value = value

    @pyqtSlot()
    def run(self):
        QApplication.setOverrideCursor(Qt.WaitCursor)
        try:
            write_tag(self.tag, self.value)
        except Exception as e:
            print(f'{e} - Write Tags Worker')
        QApplication.restoreOverrideCursor()
#######################################################################################################
class Worker_ToggleBtnValue(QRunnable, WorkerParent):
    def __init__(self, tag: str, actual_value: Union[int, bool], widget: QWidget):
        """
        Worker para escrever 1 em uma tag e escrever 0 logo em seguida

        :param tag: String da Tag que será escrita
        :param actual_value: Valor atual da tag
        :param widget: Widget a ser bloqueado enquanto é escrito no CLP
        """
        super(Worker_ToggleBtnValue, self).__init__()
        self.tag = tag
        self.actual_value = actual_value
        self.widget = widget

    @pyqtSlot()
    def run(self):
        self.widget.setEnabled(False)
        QApplication.setOverrideCursor(Qt.WaitCursor)
        if self.actual_value == 0:
            self.widget.setEnabled(False)
            write_tag(self.tag, 1)
            self.widget.setEnabled(False)
            time.sleep(1)
            write_tag(self.tag, 0)
        else:
            raise ValueError("Valor atual da tag invalido")
        QApplication.restoreOverrideCursor()
        self.widget.setEnabled(True)
#######################################################################################################

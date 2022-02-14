##############################################################
### CR 967 - Sousmile
### RN Robotics
##############################################################
##############################################################
### IMPORTS
##############################################################
import signal
import traceback, sys
import time

from PyQt5.QtCore import *
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QLineEdit

from ui_py.ui_gui_v7 import Ui_MainWindow
from ui_py.ui_cod_dialog_win import Ui_Dialog
from ui_py.ui_alt_val_dialog import Ui_Dialog2
from ui_py.ui_login_dialog import Ui_LoginDialog

from utils.gui_functions import *
from utils.workers import *
from utils.ctrl_plc import *
from utils.alarm_control import *
##############################################################

class RnRobotics_Gui:
    def __init__(self):
        self.main_win = QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.main_win)

        self.cod_dialog_win = QDialog()
        self.ui_cod_dialog_win = Ui_Dialog()
        self.ui_cod_dialog_win.setupUi(self.cod_dialog_win)

        self.alt_val_dialog = QDialog()
        self.ui_alt_val_dialog = Ui_Dialog2()
        self.ui_alt_val_dialog.setupUi(self.alt_val_dialog)

        self.login_dialog = QDialog()
        self.ui_login_dialog = Ui_LoginDialog()
        self.ui_login_dialog.setupUi(self.login_dialog)

        win_icon = QIcon("./assets/images/RN_ico.png")
        self.main_win.setWindowIcon(win_icon)
        self.cod_dialog_win.setWindowIcon(win_icon)
        self.alt_val_dialog.setWindowIcon(win_icon)
        self.login_dialog.setWindowIcon(win_icon)

        self.main_win.setWindowTitle("HMI SouSmile")
        ##################################################################
        self.userName = "Não Conectado"
        self.ui.lbl_username.setText(self.userName)
        ##################################################################
        # thread - to update PLC values
        self.threadpool = QThreadPool()
        ###################################################################
        # timer to execute the update of tags
        self.update_tags()
        # self.timer = QTimer()
        # self.timer.setInterval(1000)
        # self.timer.timeout.connect()
        # self.timer.start()
        ###################################################################
        # main screen of the application
        self.ui.stackedWidget.setCurrentWidget(self.ui.home_screen)
        ###################################################################
        # buttons to navigate between screens
        self.ui.btnHomeScreen.clicked.connect(self.show_home)
        self.ui.btnRobotScreen.clicked.connect(self.show_robot)
        self.ui.btnAlarmScreen.clicked.connect(self.show_alarm)
        self.ui.btnProductionScreen.clicked.connect(self.show_production)
        self.ui.btnMaintenaceScreen.clicked.connect(self.show_maintenance)
        self.ui.btnEngineeringScreen.clicked.connect(self.show_engineering)
        self.ui.btn_in_out_screen.clicked.connect(self.show_in_out)
        self.ui.btnLogin.clicked.connect(self.show_login_dialog)
        self.ui.btn_hist_alarm.clicked.connect(self.show_alarm_history)
        self.ui.btn_atual_alarm.clicked.connect(self.show_alarm)
        ####################################################################
        # button to back screen
        self.ui.btn_volta_manut_screen.clicked.connect(self.show_maintenance)
        ####################################################################
        # adding alarms to list
        # ToDo => ver como receber os alarmes e os tempos
        define_alarm_list(self.ui, "12:35:31", 0)
        define_alarm_list(self.ui, "13:18:57", 11)
        define_alarm_list(self.ui, "15:16:22", 34)
        define_alarm_list(self.ui, "15:34:46", 64)
        ####################################################################
        # button to show pop up to insert code manually
        self.ui.btn_in_cod_man_a1.clicked.connect(lambda: self.show_cod_dialog_win('DataCtrl_A1.ProdCode', "string"))
        self.ui.btn_in_cod_man_a2.clicked.connect(lambda: self.show_cod_dialog_win('DataCtrl_A2.ProdCode', "string"))
        self.ui.btn_in_cod_man_b1.clicked.connect(lambda: self.show_cod_dialog_win('DataCtrl_B1.ProdCode', "string"))
        self.ui.btn_in_cod_man_b2.clicked.connect(lambda: self.show_cod_dialog_win('DataCtrl_B2.ProdCode', "string"))
        ####################################################################
        # button to show pop up to change value
        self.ui.btn_alt_vel_robo_screen.clicked.connect(
            lambda: self.show_alt_val_dialog("Alterar velocidade do robô:", "Robo.Output.Speed", "int")
        )
        set_dialog_buttons_maintenance(self.ui, self.show_alt_val_dialog)
        set_dialog_buttons_engineering(self.ui, self.show_alt_val_dialog)
        ####################################################################
        # button to send code to the PLC tag
        self.ui_cod_dialog_win.btn_insert_code_man.clicked.connect(
            lambda:
            write_QlineEdit(
                self.tag_index,
                self.cod_dialog_win,
                self.ui_cod_dialog_win.txt_code,
                self.tag_type
            )
        )
        self.ui_alt_val_dialog.btn_alt_val.clicked.connect(
            lambda:
            write_QlineEdit(
                self.tag_index,
                self.alt_val_dialog,
                self.ui_alt_val_dialog.new_value,
                self.tag_type
            )
        )
        ####################################################################
        # login button
        self.ui_login_dialog.btn_login.clicked.connect(
            lambda:
            self.login(
                self.login_dialog,
                self.ui_login_dialog.user_login,
                self.ui_login_dialog.user_password
            )
        )
        ####################################################################
        # Side A: man - auto button
        self.ui.btn_man_auto_lado_a.clicked.connect(lambda: self.set_reset_button('HMI.SideA.ModeValue'))
        self.ui.btn_man_auto_lado_b.clicked.connect(lambda: self.set_reset_button('HMI.SideB.ModeValue'))
        ####################################################################
        # Reset Production Count
        self.ui.btn_reset_prod_a1.clicked.connect(lambda: reset_product("HMI.Production.PartsDoneA1"))
        self.ui.btn_reset_prod_a2.clicked.connect(lambda: reset_product("HMI.Production.PartsDoneA2"))
        self.ui.btn_reset_prod_b1.clicked.connect(lambda: reset_product("HMI.Production.PartsDoneB1"))
        self.ui.btn_reset_prod_b2.clicked.connect(lambda: reset_product("HMI.Production.PartsDoneB2"))
        self.ui.btn_reset_prod_total_a.clicked.connect(lambda: reset_product("HMI.Production.PartsDoneA1", "HMI.Production.PartsDoneA2"))
        self.ui.btn_reset_prod_total_b.clicked.connect(lambda: reset_product("HMI.Production.PartsDoneB1", "HMI.Production.PartsDoneB2"))
        ####################################################################
        # button to hold robot
        self.ui.btn_parar_robo.clicked.connect(lambda: self.hold_robot("HMI.HoldRobo"))
        ####################################################################
        # enable pts logs
        self.ui.btn_habilita_logs.clicked.connect(lambda: self.enable_logs("HMI.EnableLog"))
        ####################################################################
        # set maintenance buttons
        # self.ui.btn_DoorSideA_abrir.clicked.connect(lambda: change_button("Cyl_DoorSideA.ManRet"))
        # self.ui.btn_DoorSideA_fechar.clicked.connect(lambda: change_button("Cyl_DoorSideA.ManExt"))
        # self.ui.btn_DoorSideA_manut.clicked.connect(lambda: change_button("Cyl_DoorSideA.MaintTest"))

        # self.ui.btn_DoorSideB_abrir.clicked.connect(lambda: change_button("Cyl_DoorSideB.ManRet"))
        # self.ui.btn_DoorSideB_fechar.clicked.connect(lambda: change_button("Cyl_DoorSideB.ManExt"))
        # self.ui.btn_DoorSideB_manut.clicked.connect(lambda: change_button("Cyl_DoorSideB.MaintTest"))

        # self.ui.btn_SpindleRobo_abrir.clicked.connect(lambda: change_button("Cyl_SpindleRobo.ManRet"))
        # self.ui.btn_SpindleRobo_fechar.clicked.connect(lambda: change_button("Cyl_SpindleRobo.ManExt"))
        # self.ui.btn_SpindleRobo_manut.clicked.connect(lambda: change_button("Cyl_SpindleRobo.MaintTest"))
        ####################################################################
        self.ui.btn_sobe_alarm.clicked.connect(lambda: row_up(self.ui.alarm_list_widget))
        self.ui.btn_desce_alarm.clicked.connect(lambda: row_down(self.ui.alarm_list_widget))
        self.ui.btn_sobe_alarm_hist.clicked.connect(lambda: row_up(self.ui.hist_alarm_list_widget))
        self.ui.btn_desce_alarm_hist.clicked.connect(lambda: row_down(self.ui.hist_alarm_list_widget))

    def show(self):
        self.main_win.show()

    def show_max(self):
        self.main_win.showMaximized()

    ####################################################################
    #### functions to navigate between screens
    ####################################################################
    def show_home(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.home_screen)

    def show_robot(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.robot_screen)

    def show_alarm(self):
        self.ui.alarm_list_widget.horizontalHeader().setVisible(True)
        self.ui.stackedWidget.setCurrentWidget(self.ui.alarms_screen)

    def show_production(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.production_screen)

    def show_maintenance(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.maintenace_screen)

    def show_in_out(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.inOut_screen)

    def show_engineering(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.engineering_screen)

    def show_alarm_history(self):
        self.ui.hist_alarm_list_widget.horizontalHeader().setVisible(True)
        self.ui.stackedWidget.setCurrentWidget(self.ui.alarm_history_screen)
    ####################################################################
    #### function to dialogs
    ####################################################################
    def show_cod_dialog_win(self, tag, type):
        self.tag_index = tag
        self.tag_type = type
        self.cod_dialog_win.exec_()

    def show_alt_val_dialog(self, text, tag, type):
        self.tag_index = tag
        self.tag_type = type
        self.ui_alt_val_dialog.description_text.setText(text)
        self.alt_val_dialog.exec_()

    def show_login_dialog(self):
        self.login_dialog.exec_()
    ####################################################################
    #### others buttons functions (test)
    # ToDo => melhorar botões e estados
    ####################################################################
    def multistate_button(self, tag, value):
        write_tag(tag, value)

    def set_reset_button(self, tag):
        try:
            value = read_tags(tag)
            if value == 0:
                write_tag(tag, 1)
            elif value == 1:
                write_tag(tag, 0)
            else:
                pass
        except:
            pass

    def hold_robot(self, tag):
        try:
            value = read_tags(tag)
            if value == 0:
                write_tag(tag, 1)
            elif value == 1:
                write_tag(tag, 0)
            else:
                pass
        except:
            pass

    def enable_logs(self, tag):
        try:
            value = read_tags(tag)
            if value == 0:
                self.ui.btn_habilita_logs.setText("Desab. log\nde pontos")
                write_tag(tag, 1)
            elif value == 1:
                self.ui.btn_habilita_logs.setText("Habilita log\nde pontos")
                write_tag(tag, 0)
            else:
                pass
        except:
            pass
    #######################################################################
    #### Login
    def login(self, dialog: QDialog, *widgets: QLineEdit):
        for widget in widgets:
            if widget.objectName() == "user_login":
                self.userName = widget.text()
            widget.clear()
        self.ui.lbl_username.setText(self.userName)
        dialog.close()
    #######################################################################
    #### Updating Tags on the PLC
    #######################################################################
    def update_tags(self):

        worker = Worker()

        worker.signal_a1.result.connect(self.update_DataCtrl_A1)
        worker.signal_a2.result.connect(self.update_DataCtrl_A2)
        worker.signal_b1.result.connect(self.update_DataCtrl_B1)
        worker.signal_b2.result.connect(self.update_DataCtrl_B2)
        worker.signal_hmi.result.connect(self.update_hmi)
        worker.signal_configPts.result.connect(self.update_ConfigPontos)
        worker.signal_cylDoorA.result.connect(self.update_CylDoorSideA)
        worker.signal_cylDoorB.result.connect(self.update_CylDoorSideB)
        worker.signal_cylSpindle.result.connect(self.update_CylSpindle)
        worker.signal_indexRobotPos.result.connect(self.update_indexRobotPos)
        worker.signal_roboInput.result.connect(self.update_RoboInput)
        worker.signal_robotOutput.result.connect(self.update_RoboOutput)
        worker.signal_barCodeReader.result.connect(self.update_BarCode)

        self.threadpool.start(worker)
    #######################################################################
    def update_DataCtrl_A1(self, tag):
        if self.ui.stackedWidget.currentIndex() == 0:
            try:
                self.ui.lbl_ProdCode_A1.setText(tag['ProdCode'])
                self.ui.lbl_FileNumPos_A1.setText(str(tag['FileNumPos']))
                self.ui.lbl_NumPos_A1.setText(str(tag['NumPos']))
                self.ui.lbl_IndexPos_A1.setText(str(tag['IndexPos']))
            except:
                pass
    def update_DataCtrl_A2(self, tag):
        if self.ui.stackedWidget.currentIndex() == 0:
            try:
                self.ui.lbl_ProdCode_A2.setText(tag['ProdCode'])
                self.ui.lbl_FileNumPos_A2.setText(str(tag['FileNumPos']))
                self.ui.lbl_NumPos_A2.setText(str(tag['NumPos']))
                self.ui.lbl_IndexPos_A2.setText(str(tag['IndexPos']))
            except:
                pass
    def update_DataCtrl_B1(self, tag):
        if self.ui.stackedWidget.currentIndex() == 0:
            try:
                self.ui.lbl_ProdCode_B1.setText(tag['ProdCode'])
                self.ui.lbl_FileNumPos_B1.setText(str(tag['FileNumPos']))
                self.ui.lbl_NumPos_B1.setText(str(tag['NumPos']))
                self.ui.lbl_IndexPos_B1.setText(str(tag['IndexPos']))
            except:
                pass
    def update_DataCtrl_B2(self, tag):
        if self.ui.stackedWidget.currentIndex() == 0:
            try:
                self.ui.lbl_ProdCode_B2.setText(tag['ProdCode'])
                self.ui.lbl_FileNumPos_B2.setText(str(tag['FileNumPos']))
                self.ui.lbl_NumPos_B2.setText(str(tag['NumPos']))
                self.ui.lbl_IndexPos_B2.setText(str(tag['IndexPos']))
            except:
                pass
    #######################################################################
    def update_hmi(self, tag):
        prodTag = tag["Production"]
        if self.ui.stackedWidget.currentIndex() == 0:
            try:
                self.ui.lbl_production_TimeCutA1.setText(str(round(prodTag['TimeCutA1'], 2)))
                self.ui.lbl_production_TimeCutA2.setText(str(round(prodTag['TimeCutA2'], 2)))
                self.ui.lbl_production_TimeCutB1.setText(str(round(prodTag['TimeCutB1'], 2)))
                self.ui.lbl_production_TimeCutB2.setText(str(round(prodTag['TimeCutB2'], 2)))
                sts_string(tag['Sts']['TransDataSideA'], self.ui.lbl_sts_TransDataSideA)
                sts_string(tag['Sts']['TransDataSideB'], self.ui.lbl_sts_TransDataSideB)

                #### setting alarm status
                if tag["AlarmSideA"]:
                    self.ui.sts_sem_alarm_a.setEnabled(False)
                else:
                    self.ui.sts_sem_alarm_a.setEnabled(True)

                if tag["AlarmSideB"]:
                    self.ui.sts_sem_alarm_b.setEnabled(False)
                else:
                    self.ui.sts_sem_alarm_b.setEnabled(True)

                #### Side A: manual - auto
                if tag['SideA']['ModeValue'] == 0:
                    self.ui.btn_man_auto_lado_a.setChecked(False)
                    self.ui.sts_auto_man_a.setEnabled(False)
                    self.ui.btn_man_auto_lado_a.setText('Automático')
                elif tag['SideA']['ModeValue'] == 1:
                    self.ui.btn_man_auto_lado_a.setChecked(True)
                    self.ui.sts_auto_man_a.setEnabled(True)
                    self.ui.btn_man_auto_lado_a.setText('Manual')
                else:
                    pass

                #### Side B: manual - auto
                if tag['SideB']['ModeValue'] == 0:
                    self.ui.btn_man_auto_lado_b.setChecked(False)
                    self.ui.sts_auto_man_b.setEnabled(False)
                    self.ui.btn_man_auto_lado_b.setText('Automático')
                elif tag['SideB']['ModeValue'] == 1:
                    self.ui.btn_man_auto_lado_b.setChecked(True)
                    self.ui.sts_auto_man_b.setEnabled(True)
                    self.ui.btn_man_auto_lado_b.setText('Manual')
                else:
                    pass
            except:
                pass
        if self.ui.stackedWidget.currentIndex() == 3:
            try:
                ### updating tags
                self.ui.lbl_PartsDoneA1.setText(str(prodTag["PartsDoneA1"]))
                self.ui.lbl_PartsDoneA2.setText(str(prodTag["PartsDoneA2"]))
                self.ui.lbl_PartsDoneSideA.setText(str(prodTag["PartDoneSideA"]))
                self.ui.lbl_PartsDoneB1.setText(str(prodTag["PartsDoneB1"]))
                self.ui.lbl_PartsDoneB2.setText(str(prodTag["PartsDoneB2"]))
                self.ui.lbl_PartsDoneSideB.setText(str(prodTag["PartDoneSideB"]))

                self.ui.lbl_TimeCutA1.setText(str(round(prodTag["TimeCutA1"], 2)))
                self.ui.lbl_TimeCutA2.setText(str(round(prodTag["TimeCutA2"], 2)))
                self.ui.lbl_TimeCutSideA.setText(str(round(prodTag["TimeCutSideA"], 2)))
                self.ui.lbl_TimeCutB1.setText(str(round(prodTag["TimeCutB1"], 2)))
                self.ui.lbl_TimeCutB2.setText(str(round(prodTag["TimeCutB2"], 2)))
                self.ui.lbl_TimeCutSideB.setText(str(round(prodTag["TimeCutSideB"], 2)))
            except:
                pass
        if self.ui.stackedWidget.currentIndex() == 6:
            currentOffset = tag["CurrentOffset"]
            try:
                self.ui.lbl_PosX.setText(str(round(currentOffset["PosX"], 1)))
                self.ui.lbl_PosY.setText(str(round(currentOffset["PosY"], 1)))
                self.ui.lbl_PosZ.setText(str(round(currentOffset["PosZ"], 1)))
                self.ui.lbl_PosC.setText(str(round(currentOffset["PosC"], 1)))
                self.ui.lbl_PosD.setText(str(round(currentOffset["PosD"], 1)))
                self.ui.lbl_MaxPts.setText(str(tag["NumPosMax"]))

                value = tag["EnableLog"]
                if value == 0:
                    self.ui.btn_habilita_logs.setText("Desab. log\nde pontos")
                    write_tag(tag, 1)
                elif value == 1:
                    self.ui.btn_habilita_logs.setText("Habilita log\nde pontos")
                    write_tag(tag, 0)
                else:
                    pass
            except:
                pass
    ########################################################################
    def update_ConfigPontos(self, tag):
        if self.ui.stackedWidget.currentIndex() == 6:
            try:
                self.ui.lbl_dist_xyz.setText(str(round(tag["Dist_XYZ"], 2)))
                self.ui.lbl_diff_c.setText(str(round(tag["Diff_AngleC"], 2)))
                self.ui.lbl_diff_d.setText(str(round(tag["Diff_AngleD"], 2)))
                self.ui.lbl_var_h.setText(str(round(tag["Dist_H"], 2)))
                self.ui.lbl_d_menor_pts.setText(str(round(tag["DistVar"], 2)))

                self.ui.lbl_CutDepth_A1.setText(str(round(tag["CutDepthA1"])))
                self.ui.lbl_CutDepth_A2.setText(str(round(tag["CutDepthA2"])))
                self.ui.lbl_CutDepth_B1.setText(str(round(tag["CutDepthB1"])))
                self.ui.lbl_CutDepth_B2.setText(str(round(tag["CutDepthB2"])))
            except:
                pass
    ########################################################################
    def update_CylDoorSideA(self, tag):
        if self.ui.stackedWidget.currentIndex() == 4:
            try:
                self.ui.lbl_TimeMaint_A.setText(str(tag["TimeMaintTest"]))
                sideA_status_update(tag, self.ui)
            except:
                pass

        if self.ui.stackedWidget.currentIndex() == 6:
            try:
                self.ui.lbl_delay_abre_port_a.setText(str(tag["TimeDelayRet"]))
                self.ui.lbl_delay_fecha_port_a.setText(str(tag["TimeDelayExt"]))
                self.ui.lbl_temp_alarm_sens_a.setText(str(tag["TimeBothSenOnOff"]))
                self.ui.lbl_temp_alarm_pos_port_a.setText(str(tag["TimeOut"]))
            except:
                pass
    def update_CylDoorSideB(self, tag):
        if self.ui.stackedWidget.currentIndex() == 4:
            try:
                self.ui.lbl_TimeMaint_B.setText(str(tag["TimeMaintTest"]))
                sideB_status_update(tag, self.ui)
            except:
                pass

        if self.ui.stackedWidget.currentIndex() == 6:
            try:
                self.ui.lbl_delay_abre_port_b.setText(str(tag["TimeDelayRet"]))
                self.ui.lbl_delay_fecha_port_b.setText(str(tag["TimeDelayExt"]))
                self.ui.lbl_temp_alarm_sens_b.setText(str(tag["TimeBothSenOnOff"]))
                self.ui.lbl_temp_alarm_pos_port_b.setText(str(tag["TimeOut"]))
            except:
                pass
    def update_CylSpindle(self, tag):
        if self.ui.stackedWidget.currentIndex() == 4:
            try:
                self.ui.lbl_TimeMaint_Spindle.setText(str(tag["TimeMaintTest"]))
                spindle_status_update(tag, self.ui)
            except:
                pass
    ########################################################################
    def update_indexRobotPos(self, tag):
        if self.ui.stackedWidget.currentIndex() == 6:
            try:
                self.ui.lbl_RobotPos.setText(str(tag))
            except:
                pass
    ########################################################################
    def update_RoboInput(self, tag):
        if self.ui.stackedWidget.currentIndex() == 1:
            try:
                robot_input_status_update(tag, self.ui)
            except:
                pass
    def update_RoboOutput(self, tag):
        if self.ui.stackedWidget.currentIndex() == 1:
            try:
                self.ui.lbl_RobotSpeed.setText(str(tag["Speed"]))
                robot_output_status_update(tag, self.ui)
            except:
                pass
        if self.ui.stackedWidget.currentIndex() == 6:
            try:
                self.ui.lbl_CutSpeed.setText(str(tag["CutSpeed"]))
            except:
                pass
    ########################################################################
    def update_BarCode(self, tag):
        if self.ui.stackedWidget.currentIndex() == 4:
            try:
                self.ui.lbl_BarCodeReader_data.setText(str(tag["Data"]))
                WStatus = self.ui.sts_BarCodeReader_completed
                change_status(tag["ReadCompete"], WStatus)
            except:
                pass
    ########################################################################


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_win = RnRobotics_Gui()
    main_win.show_max()
    sys.exit(app.exec())

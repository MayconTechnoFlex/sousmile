"""Module with all functions used on the RobotScreen of the application"""

from ui_py.ui_gui_final import Ui_MainWindow
from dialogs.altera_valor import AlteraValorDialog

from PyQt5.QtWidgets import QApplication

from utils.functions.gui_functions import change_status, set_reset_btn_int
from utils.Types import PLCReturn
from utils.btn_style import *

UI: Ui_MainWindow

tag_list: PLCReturn

def define_buttons(receive_ui: Ui_MainWindow, dialog: AlteraValorDialog):
    """
    Define the buttons of the screen

    Params:
        receive_ui = main ui of the application
        dialog = function for pop-up buttons
    """
    global UI
    UI = receive_ui

    UI.btn_parar_robo.clicked.connect(lambda: set_reset_btn_int(2, tag_list, UI.btn_parar_robo))

    UI.btn_alt_vel_robo_screen.clicked.connect(
        lambda: dialog.show_dialog("Alterar velocidade do robô:", "Robo.Output.Speed", "int")
    )


def UpdateHMI(tag):
    global UI
    try:
        if tag["HoldRobo"] == 0:
            UI.btn_parar_robo.setStyleSheet(base_button_style + "*{border-radius: 35}")
            UI.btn_parar_robo.setText("Parar Robô")
            QApplication.restoreOverrideCursor()

        elif tag["HoldRobo"] == 1:
            UI.btn_parar_robo.setStyleSheet(checked_button_style + "*{border-radius: 35}")
            UI.btn_parar_robo.setText("Liberar Robô")
            QApplication.restoreOverrideCursor()
        else:
            pass

    except Exception as e:
        UI.btn_parar_robo.setStyleSheet(btn_error_style)
        UI.btn_parar_robo.setText('Erro')
        UI.btn_parar_robo.setEnabled(False)
        print(f'{e} - robot.UpdateHMI')


def UpdateInput(tag: dict):
    """
    Updates the screen's status with the readed tag values

    Params:
        tag = readed tag from RobotInput
    """
    global UI
    try:
        change_status(tag["Cmd_enabled"], UI.sts_enable)
        change_status(tag["System_ready"], UI.sts_ready)
        change_status(tag["Prg_running"], UI.sts_running)
        change_status(tag["Motion_held"], UI.sts_motion_held)
        change_status(tag["Emergency"], UI.sts_emerg)
        change_status(tag["TP_Enabled"], UI.sts_tp_enabled)
        change_status(tag["Batt_alarm"], UI.sts_battery_alarm)
        change_status(tag["HomePos"], UI.sts_home_pos)
        change_status(tag["RSA"], UI.sts_robo_a)
        change_status(tag["RSB"], UI.sts_robo_b)
    except:
        pass

def UpdateOutput(tag: dict):
    """
    Updates the screen's status with the readed tag values

    Params:
        tag = readed tag from RobotInput
    """
    global UI
    try:
        UI.lbl_RobotSpeed.setText(str(tag["Speed"]))
        change_status(tag["IMSTP"], UI.sts_imstp)
        change_status(tag["Hold"], UI.sts_hold)
        change_status(tag["SFSPD"], UI.sts_sfspd)
        change_status(tag["Start"], UI.sts_start)
        change_status(tag["Enable"], UI.sts_enabled)
        change_status(tag["FP"], UI.sts_finish_part)
        change_status(tag["MSA"], UI.sts_macro_a)
        change_status(tag["MSB"], UI.sts_macro_b)
    except:
        pass

def UpdateTagsList(tags):
    global tag_list
    tag_list = tags

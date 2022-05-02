"""Módulo com todas as funções para a tela Robô"""
#######################################################################################################
# Importações
#######################################################################################################
from PyQt5.Qt import QIntValidator
from PyQt5.QtCore import QThreadPool
from PyQt5.QtWidgets import QApplication

from ui_py.ui_gui_final import Ui_MainWindow

from utils.functions.gui_functions import change_status, set_reset_btn_int
from utils.Types import PLCReturn
from utils.btn_style import *
from utils.workers.workers import Worker_WriteTags
#######################################################################################################
# Definição das variáveis globais
#######################################################################################################
UI: Ui_MainWindow
tag_list: PLCReturn
thread_write_tags = QThreadPool()
#######################################################################################################
# Funções de Definição
#######################################################################################################
def define_buttons(main_ui: Ui_MainWindow):
    """
    Define os botões da tela

    :param main_ui: Ui da aplicação
    """
    global UI
    UI = main_ui
    int_validators_cut_spd = QIntValidator(0, 100)

    UI.btn_parar_robo.clicked.connect(lambda: set_reset_btn_int(2, tag_list, UI.btn_parar_robo))
    UI.btn_alt_vel_robo_screen.clicked.connect(altera_velocidade)

    UI.le_vel_robo.setValidator(int_validators_cut_spd)
#######################################################################################################
def altera_velocidade():
    global UI
    if UI.le_vel_robo.text():
        vel = int(UI.le_vel_robo.text())
        if vel > 100:
            vel = 100
        worker = Worker_WriteTags("Robo.Output.Speed", vel)
        thread_write_tags.start(worker)
        UI.le_vel_robo.clear()
#######################################################################################################
# Funções de Atualização
#######################################################################################################
def UpdateHMI(tag):
    """
    Atualiza os Botões da tela com os valores do CLP

    :param tag: Tag lida do CLP
    """
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
        setErrorButton(UI.btn_parar_robo)
        print(f'{e} - robot.UpdateHMI')
#######################################################################################################
def UpdateInput(tag: dict):
    """
    Atualiza os Status da tela com os valores do CLP

    :param tag: Tag lida do CLP
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
#######################################################################################################
def UpdateOutput(tag: dict):
    """
    Atualiza os Status e Labels da tela com os valores do CLP

    :param tag: Tag lida do CLP
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
#######################################################################################################
def UpdateTagsList(tags):
    global tag_list
    tag_list = tags
#######################################################################################################

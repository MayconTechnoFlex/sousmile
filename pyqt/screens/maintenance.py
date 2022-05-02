"""Módulo com todas as funções para a tela Manutenção"""
#######################################################################################################
# Importações
#######################################################################################################
import time

from PyQt5.Qt import QIntValidator
from PyQt5.QtCore import QThreadPool
from PyQt5.QtWidgets import QPushButton, QLineEdit, QWidget

from ui_py.ui_gui_final import Ui_MainWindow
from dialogs.confirmation import ConfirmationDialog
from dialogs.ajuste_fresa import AjusteFrasaDialog

from security.db_users import get_connected_username

from utils.functions.gui_functions import change_status, set_reset_btn_int
from utils.Types import PLCReturn
from utils.btn_style import setErrorButton, setButton
from utils.workers.workers import Worker_ToggleBtnValue, Worker_Pressed_WriteTags, Worker_WriteTags
from utils.btn_style import base_button_style, checked_button_style

#######################################################################################################
# Definição das variáveis globais
#######################################################################################################
UI: Ui_MainWindow
tag_list: PLCReturn = []
write_thread = QThreadPool()
HomePos: int = 1
not_connected = True


#######################################################################################################
# Funções de Definição
#######################################################################################################
def define_buttons(main_ui: Ui_MainWindow, confirmDialog: ConfirmationDialog, ajustDialog: AjusteFrasaDialog):
    """
    Define os botões da tela

    :param main_ui: Ui da aplicação
    :param altValDialog: Dialog para alterar valor de tag
    :param confirmDialog: Dialog de confirmação de ação
    :param checkUF: Dialog para checar a UserFrame
    """
    global UI, tag_list
    UI = main_ui

    tempo_manut_validators()

    buttons_ConfirmDialogs(confirmDialog)

    UI.btn_check_uf.clicked.connect(lambda: check_uf("Robo.Output.UFCheck", "HMI.btnCheckUF", UI.le_check_user_frame,
                                                     UI.btn_check_uf))

    UI.btn_check_utool.clicked.connect(ajustDialog.show_dialog)

    UI.btn_menos_1_mm.clicked.connect(lambda: set_reset_button(4, UI.btn_menos_1_mm))
    UI.btn_termina_check_uf.clicked.connect(lambda: set_reset_button(5, UI.btn_termina_check_uf))

    UI.btn_DoorSideA_abrir.clicked.connect(lambda: set_reset_button(6, UI.btn_DoorSideA_abrir))
    UI.btn_DoorSideA_fechar.clicked.connect(lambda: set_reset_button(7, UI.btn_DoorSideA_fechar))
    UI.btn_DoorSideA_manut.clicked.connect(lambda: set_reset_btn_int(8, tag_list, UI.btn_DoorSideA_manut))
    UI.btn_DoorSideA_TimeMaint.clicked.connect(
        lambda: change_tempo_manut("Cyl_DoorSideA.TimeMaintTest", UI.le_tempo_manut_a)
    )

    UI.btn_DoorSideB_abrir.clicked.connect(lambda: set_reset_button(9, UI.btn_DoorSideB_abrir))
    UI.btn_DoorSideB_fechar.clicked.connect(lambda: set_reset_button(10, UI.btn_DoorSideB_fechar))
    UI.btn_DoorSideB_manut.clicked.connect(lambda: set_reset_btn_int(11, tag_list, UI.btn_DoorSideB_manut))
    UI.btn_DoorSideB_TimeMaint.clicked.connect(
        lambda: change_tempo_manut("Cyl_DoorSideB.TimeMaintTest", UI.le_tempo_manut_b)
    )

    UI.btn_SpindleRobo_abrir.pressed.connect(spindle_on)
    UI.btn_SpindleRobo_abrir.released.connect(spindle_off)

    UI.btn_SpindleRobo_manut.clicked.connect(lambda: set_reset_btn_int(13, tag_list, UI.btn_SpindleRobo_manut))
    UI.btn_SpindleRobo_TimeMaint.clicked.connect(
        lambda: change_tempo_manut("Cyl_SpindleRobo.TimeMaintTest", UI.le_tempo_manut_spindle)
    )


#######################################################################################################
def tempo_manut_validators():
    global UI
    int_validator = QIntValidator(0, 10000)

    UI.le_tempo_manut_a.setValidator(int_validator)
    UI.le_tempo_manut_b.setValidator(int_validator)
    UI.le_tempo_manut_spindle.setValidator(int_validator)


#######################################################################################################
def change_tempo_manut(tag_name: str, line_edit: QLineEdit):
    if line_edit.text():
        value = int(line_edit.text())
        line_edit.clear()
        worker = Worker_WriteTags(tag_name, value)
        write_thread.start(worker)


#######################################################################################################
def check_uf(tag_robo_uf: str, tag_check_uf: str, line_edit: QLineEdit, widget: QWidget):
    if line_edit.text():
        value = int(line_edit.text())
        line_edit.clear()
        worker = Worker_WriteTags(tag_robo_uf, value)
        write_thread.start(worker)
        time.sleep(1)
        worker = Worker_ToggleBtnValue(tag_check_uf, 0, widget)
        write_thread.start(worker)


#######################################################################################################
def buttons_ConfirmDialogs(dialog: ConfirmationDialog):
    """
    Define os botões que utilizam o Dialog de Confirmação

    :param dialog: Dialog de Confirmação
    """
    global UI
    UI.btn_move_home.clicked.connect(
        lambda: dialog.show_dialog("MoveHome",
                                   "Cuidado! Você vai movimentar o robô para a posição inicial, "
                                   "caso tenha risco de colisão, movimente o robô para a posição inicial manualmente!"))
    UI.btn_change_tool.clicked.connect(
        lambda: dialog.show_dialog("ChangeTool",
                                   "Cuidado! Você vai movimentar o robô para trocar sua ferramenta.")
    )


#######################################################################################################
def setup_buttons_style():
    """Configura os botões para Erro caso hajá problema de conexão"""
    # botões da parte inferior
    setButton(UI.btn_move_home, "Mover\npara Home")
    setButton(UI.btn_check_uf, "Check\nUser Frame")
    setButton(UI.btn_menos_1_mm, "- 1 mm")
    setButton(UI.btn_termina_check_uf, "Termina Check\nUser Frame")
    setButton(UI.btn_check_utool, "Ajustar\nFresa")
    setButton(UI.btn_change_tool, "Trocar de\nFerramenta")

    # botões do lado A
    setButton(UI.btn_DoorSideA_abrir, "ABRIR")
    setButton(UI.btn_DoorSideA_fechar, "FECHAR")
    setButton(UI.btn_DoorSideA_manut, "MANUTENÇÃO")

    # botões do lado B
    setButton(UI.btn_DoorSideB_abrir, "ABRIR")
    setButton(UI.btn_DoorSideB_fechar, "FECHAR")
    setButton(UI.btn_DoorSideB_manut, "MANUTENÇÃO")

    # botões do spindle
    setButton(UI.btn_SpindleRobo_abrir, "LIGAR")
    setButton(UI.btn_SpindleRobo_manut, "MANUTENÇÃO")


#######################################################################################################
def error_buttons():
    """Configura os botões para Erro caso hajá problema de conexão"""
    # botões da parte inferior
    setErrorButton(UI.btn_move_home)
    setErrorButton(UI.btn_check_uf)
    setErrorButton(UI.btn_menos_1_mm)
    setErrorButton(UI.btn_termina_check_uf)
    setErrorButton(UI.btn_check_utool)
    setErrorButton(UI.btn_change_tool)

    # botões do lado A
    setErrorButton(UI.btn_DoorSideA_abrir)
    setErrorButton(UI.btn_DoorSideA_fechar)
    setErrorButton(UI.btn_DoorSideA_manut)

    # botões do lado B
    setErrorButton(UI.btn_DoorSideB_abrir)
    setErrorButton(UI.btn_DoorSideB_fechar)
    setErrorButton(UI.btn_DoorSideB_manut)

    # botões do spindle
    setErrorButton(UI.btn_SpindleRobo_abrir)
    setErrorButton(UI.btn_SpindleRobo_manut)


#######################################################################################################
# Funções de Controles
#######################################################################################################
def spindle_on():
    """Liga o spindle quando o botão é mantido pressionado"""
    global UI, tag_list, write_thread
    tag_name = tag_list[12][0]
    try:
        worker_pressed = Worker_Pressed_WriteTags(tag_name, 1)
        write_thread.start(worker_pressed, priority=0)
        UI.btn_SpindleRobo_abrir.setStyleSheet(checked_button_style)
    except Exception as e:
        print(e, "Erro no ligar spindle")
        UI.btn_SpindleRobo_abrir.setStyleSheet(base_button_style)


#######################################################################################################
def spindle_off():
    """Desliga o spindle quando o botão é solto"""
    global UI, tag_list, write_thread
    tag_name = tag_list[12][0]
    try:
        worker_pressed = Worker_Pressed_WriteTags(tag_name, 0)
        write_thread.start(worker_pressed, priority=0)
        UI.btn_SpindleRobo_abrir.setStyleSheet(base_button_style)
    except Exception as e:
        print(e, "Erro no ligar spindle")
        UI.btn_SpindleRobo_abrir.setStyleSheet(checked_button_style)


#######################################################################################################
def set_reset_button(i: int, button: QPushButton):
    """Muda o valor da tag para 1 e depois para 0"""
    global UI, tag_list, write_thread
    tag_name = tag_list[i][0]
    value = tag_list[i][1]
    try:
        worker_toggle = Worker_ToggleBtnValue(tag_name, value, button)
        write_thread.start(worker_toggle, priority=0)
    except Exception as e:
        print(e, "botão de manutenção falhou")


#######################################################################################################
# Funções de Atualização
#######################################################################################################
def UpdateCylA(tag):
    """
    Atualiza os Labels e Status da tela com os valores do CLP

    :param tag: Tag lida do CLP
    """
    global UI
    try:
        UI.lbl_TimeMaint_A.setText(str(tag["TimeMaintTest"]))
        change_status(tag["InSenExt"], UI.sts_port_fech_a)
        change_status(tag["OutExtCyl"], UI.sts_plc_port_fech_a)
        change_status(tag["OutRetCyl"], UI.sts_plc_port_aber_a)

        if tag["MaintTest"]:
            UI.btn_DoorSideA_manut.setStyleSheet(checked_button_style)
        else:
            UI.btn_DoorSideA_manut.setStyleSheet(base_button_style)
    except:
        pass


#######################################################################################################
def UpdateCylB(tag):
    """
    Atualiza os Labels e Status da tela com os valores do CLP

    :param tag: Tag lida do CLP
    """
    global UI
    try:
        UI.lbl_TimeMaint_B.setText(str(tag["TimeMaintTest"]))
        change_status(tag["InSenExt"], UI.sts_port_fech_b)
        change_status(tag["OutExtCyl"], UI.sts_plc_port_fech_b)
        change_status(tag["OutRetCyl"], UI.sts_plc_port_aber_b)

        if tag["MaintTest"]:
            UI.btn_DoorSideB_manut.setStyleSheet(checked_button_style)
        else:
            UI.btn_DoorSideB_manut.setStyleSheet(base_button_style)
    except:
        pass


#######################################################################################################
def UpdateCylSpindle(tag):
    """
    Atualiza os Labels e Status da tela com os valores do CLP

    :param tag: Tag lida do CLP
    """
    global UI
    try:
        UI.lbl_TimeMaint_Spindle.setText(str(tag["TimeMaintTest"]))
        change_status(tag["OutExtCyl"], UI.sts_plc_liga_spindle)
        change_status(tag["OutRetCyl"], UI.sts_plc_desl_spindle)

        if tag["MaintTest"]:
            UI.btn_SpindleRobo_manut.setStyleSheet(checked_button_style)
        else:
            UI.btn_SpindleRobo_manut.setStyleSheet(base_button_style)
    except:
        pass


#######################################################################################################
def UpdateBarCode(tag):
    """
    Atualiza os Labels e Status da tela com os valores do CLP

    :param tag: Tag lida do CLP
    """
    global UI
    try:
        UI.lbl_BarCodeReader_data.setText(str(tag["DataPy"]))
        WStatus = UI.sts_BarCodeReader_completed
        change_status(tag["ReadComplete"], WStatus)
    except:
        pass


#######################################################################################################
def UpdateHMI(tag):
    """
    Atualiza os botões da tela com os valores do CLP

    :param tag: Tag lida do CLP
    """
    global UI, HomePos, not_connected
    try:
        user = get_connected_username()
        if tag["SideA"]["Manual"] and tag["SideB"]["Manual"]:
            UI.btn_move_home.setEnabled(True)
            if HomePos:
                if user == "rn" or user == "eng":
                    UI.btn_check_uf.setEnabled(True)
                else:
                    UI.btn_check_uf.setEnabled(False)
                UI.btn_check_utool.setEnabled(True)
                UI.btn_change_tool.setEnabled(True)
            else:
                UI.btn_check_uf.setEnabled(False)
                UI.btn_check_utool.setEnabled(False)
                UI.btn_change_tool.setEnabled(False)

            if user == "rn" or user == "eng":
                UI.btn_SpindleRobo_abrir.setEnabled(True)
                UI.btn_SpindleRobo_manut.setEnabled(True)
        else:
            UI.btn_SpindleRobo_abrir.setEnabled(False)
            UI.btn_SpindleRobo_manut.setEnabled(False)
            UI.btn_move_home.setEnabled(False)
            UI.btn_check_uf.setEnabled(False)
            UI.btn_check_utool.setEnabled(False)
            UI.btn_change_tool.setEnabled(False)

        if not_connected:
            setup_buttons_style()
            not_connected = False

        if tag["SideA"]["Manual"]:
            UI.btn_DoorSideA_abrir.setEnabled(True)
            UI.btn_DoorSideA_fechar.setEnabled(True)
            if user == "rn" or user == "eng":
                UI.btn_DoorSideA_manut.setEnabled(True)
            else:
                UI.btn_DoorSideA_manut.setEnabled(False)
        else:
            UI.btn_DoorSideA_abrir.setEnabled(False)
            UI.btn_DoorSideA_fechar.setEnabled(False)
            UI.btn_DoorSideA_manut.setEnabled(False)

        if tag["SideB"]["Manual"]:
            UI.btn_DoorSideB_abrir.setEnabled(True)
            UI.btn_DoorSideB_fechar.setEnabled(True)
            if user == "rn" or user == "eng":
                UI.btn_DoorSideB_manut.setEnabled(True)
            else:
                UI.btn_DoorSideB_manut.setEnabled(False)
        else:
            UI.btn_DoorSideB_abrir.setEnabled(False)
            UI.btn_DoorSideB_fechar.setEnabled(False)
            UI.btn_DoorSideB_manut.setEnabled(False)
    except Exception:
        error_buttons()
        not_connected = True


#######################################################################################################
def UpdateRobotInput(tag):
    """
    Atualiza os botões da tela com os valores do CLP

    :param tag: Tag lida do CLP
    """
    global UI, HomePos
    if tag["CUFOn"] and tag["Prg_running"]:
        UI.btn_menos_1_mm.setEnabled(True)
        UI.btn_termina_check_uf.setEnabled(True)
    else:
        UI.btn_menos_1_mm.setEnabled(False)
        UI.btn_termina_check_uf.setEnabled(False)

    HomePos = tag["HomePos"]

#######################################################################################################
def UpdateRobotOutputs(tag):
    """
    Atualiza os botões da tela com os valores do CLP

    :param tag: Tag lida do CLP
    """
    global UI

    try:
        UI.lbl_check_user_frame.setText(str(tag["UFCheck"]))
    except Exception as e:
        print(e)

#######################################################################################################
def UpdateTagsList(tags):
    global UI, tag_list
    tag_list = tags

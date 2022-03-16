"""Module with all functions used on the MaintenanceScreen of the application"""
from PyQt5.QtCore import QThreadPool
from PyQt5.QtWidgets import QPushButton

from ui_py.ui_gui_final import Ui_MainWindow
from dialogs.confirmation import ConfirmationDialog
from dialogs.altera_valor import AlteraValorDialog
from dialogs.checkUF import CheckUserFrame

from security.db_users import connected_username

from utils.gui_functions import change_status, set_reset_btn_int
from utils.Types import PLCReturn
from utils.btn_style import btn_error_style
from utils.workers import Worker_ToggleBtnValue, Worker_Pressed_WriteTags
from utils.btn_style import base_button_style, checked_button_style

UI: Ui_MainWindow
tag_list: PLCReturn
write_thread = QThreadPool()

def define_buttons(receive_UI: Ui_MainWindow, altValDialog: AlteraValorDialog,
                   confirmDialog: ConfirmationDialog, checkUF: CheckUserFrame):
    """
    Define the buttons of the screen

    Params:
        receive_ui = main ui of the application
        altValDialog = function for pop-up buttons
        confirm_dialog = confirmation dialog object
    """
    global UI, tag_list
    UI = receive_UI

    buttons_ConfirmDialogs(confirmDialog)
    UI.btn_check_uf.clicked.connect(checkUF.show_dialog)
    UI.btn_menos_1_mm.clicked.connect(lambda: set_reset_button(4, UI.btn_menos_1_mm))
    UI.btn_termina_check_uf.clicked.connect(lambda: set_reset_button(5, UI.btn_termina_check_uf))

    UI.btn_DoorSideA_abrir.clicked.connect(lambda: set_reset_button(6, UI.btn_DoorSideA_abrir))
    UI.btn_DoorSideA_fechar.clicked.connect(lambda: set_reset_button(7, UI.btn_DoorSideA_fechar))
    UI.btn_DoorSideA_manut.clicked.connect(lambda: set_reset_btn_int(8, tag_list, UI.btn_DoorSideA_manut))
    UI.btn_DoorSideA_TimeMaint.clicked.connect(
        lambda: altValDialog.show_dialog("Alterar tempo de manutenção do lado A:", "Cyl_DoorSideA.TimeMaintTest", "int")
    )

    UI.btn_DoorSideB_abrir.clicked.connect(lambda: set_reset_button(9, UI.btn_DoorSideB_abrir))
    UI.btn_DoorSideB_fechar.clicked.connect(lambda: set_reset_button(10, UI.btn_DoorSideB_fechar))
    UI.btn_DoorSideB_manut.clicked.connect(lambda: set_reset_btn_int(11, tag_list, UI.btn_DoorSideB_manut))
    UI.btn_DoorSideB_TimeMaint.clicked.connect(
        lambda: altValDialog.show_dialog("Alterar tempo de manutenção do lado B:", "Cyl_DoorSideB.TimeMaintTest", "int")
    )

    UI.btn_SpindleRobo_abrir.pressed.connect(spindle_on)
    UI.btn_SpindleRobo_abrir.released.connect(spindle_off)

    # UI.btn_SpindleRobo_abrir.clicked.connect(lambda: set_reset_button(12, UI.btn_SpindleRobo_abrir))

    UI.btn_SpindleRobo_manut.clicked.connect(lambda: set_reset_btn_int(13, tag_list, UI.btn_SpindleRobo_manut))
    UI.btn_SpindleRobo_TimeMaint.clicked.connect(
        lambda: altValDialog.show_dialog("Alterar tempo de manutenção do spindle:", "Cyl_SpindleRobo.TimeMaintTest", "int")
    )

def spindle_on():
    global UI, tag_list, write_thread
    tag_name = tag_list[12][0]
    try:
        worker_pressed = Worker_Pressed_WriteTags(tag_name, 1)
        write_thread.start(worker_pressed, priority=0)
        UI.btn_SpindleRobo_abrir.setStyleSheet(checked_button_style)
    except Exception as e:
        print(e, "Erro no ligar spindle")
        UI.btn_SpindleRobo_abrir.setStyleSheet(base_button_style)

def spindle_off():
    global UI, tag_list, write_thread
    tag_name = tag_list[12][0]
    try:
        worker_pressed = Worker_Pressed_WriteTags(tag_name, 0)
        write_thread.start(worker_pressed, priority=0)
        UI.btn_SpindleRobo_abrir.setStyleSheet(base_button_style)
    except Exception as e:
        print(e, "Erro no ligar spindle")
        UI.btn_SpindleRobo_abrir.setStyleSheet(checked_button_style)

def set_reset_button(i: int, button: QPushButton):
    global UI, tag_list, write_thread
    tag_name = tag_list[i][0]
    value = tag_list[i][1]
    try:
        worker_toggle = Worker_ToggleBtnValue(tag_name, value, button)
        write_thread.start(worker_toggle, priority=0)
    except Exception as e:
        print(e, "botão de manutenção falhou")

def buttons_ConfirmDialogs(dialog: ConfirmationDialog):
    """
    Define the buttons that open the confirmation dialog

    Params:
        dialog = confirmation dialog itself
    """
    global UI
    UI.btn_move_home.clicked.connect(
        lambda: dialog.show_dialog("MoveHome",
                                   "Cuidado! Você vai movimentar o robô para a posição inicial, "
                                   "caso tenha risco de colisão, movimente o robô para a posição inicial manualmente!"))
    UI.btn_check_utool.clicked.connect(
        lambda: dialog.show_dialog("CheckUTOOL",
                                   "Cuidado! Você vai movimentar o robô para ajustar a User Tool. "
                                   "Para isso, o robô deve estar em Home, caso contrário, não funcionará.")
    )
    UI.btn_change_tool.clicked.connect(
        lambda: dialog.show_dialog("ChangeTool",
                                   "Cuidado! Você vai movimentar o robô para trocar sua ferramenta. "
                                   "Para isso, o robô deve estar em Home, caso contrário, não funcionará.")
    )

def UpdateCylA(tag):
    """
    Updates the screen's labels and status widgets with the readed tag values

    Params:
        tag = readed tag from CYLSideA
    """
    global UI
    try:
        UI.lbl_TimeMaint_A.setText(str(tag["TimeMaintTest"]))
        change_status(tag["InSenExt"], UI.sts_port_fech_a)
        change_status(tag["InSenRet"], UI.sts_port_aber_a)
        change_status(tag["OutExtCyl"], UI.sts_plc_port_fech_a)
        change_status(tag["OutRetCyl"], UI.sts_plc_port_aber_a)

        if tag["MaintTest"]:
            UI.btn_DoorSideA_manut.setStyleSheet(checked_button_style)
        else:
            UI.btn_DoorSideA_manut.setStyleSheet(base_button_style)
    except:
        pass

def UpdateCylB(tag):
    """
    Updates the screen's labels and status widgets with the readed tag values

    Params:
        tag = readed tag from CYLSideB
    """
    global UI
    try:
        UI.lbl_TimeMaint_B.setText(str(tag["TimeMaintTest"]))
        change_status(tag["InSenExt"], UI.sts_port_fech_b)
        change_status(tag["InSenRet"], UI.sts_port_aber_b)
        change_status(tag["OutExtCyl"], UI.sts_plc_port_fech_b)
        change_status(tag["OutRetCyl"], UI.sts_plc_port_aber_b)

        if tag["MaintTest"]:
            UI.btn_DoorSideB_manut.setStyleSheet(checked_button_style)
        else:
            UI.btn_DoorSideB_manut.setStyleSheet(base_button_style)
    except:
        pass

def UpdateCylSpindle(tag):
    """
    Updates the screen's labels and status widgets with the readed tag values

    Params:
        tag = readed tag from CYLSpindle
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

def UpdateBarCode(tag):
    """
    Updates the screen's labels and status widgets with the readed tag values

    Params:
        tag = readed tag from BarCodeReader
    """
    global UI
    try:
        UI.lbl_BarCodeReader_data.setText(str(tag["DataPy"]))
        WStatus = UI.sts_BarCodeReader_completed
        change_status(tag["ReadComplete"], WStatus)
    except:
        pass

def UpdateHMI(tag):
    """
    Updates the screen's buttons with the readed tag values

    Params:
        tag = readed tag from BarCodeReader
    """
    global UI
    try:
        if tag["SideA"]["Manual"] and tag["SideB"]["Manual"]:
            UI.btn_move_home.setEnabled(True)
            if connected_username == "rn" or connected_username == "eng":
                UI.btn_check_uf.setEnabled(True)
                UI.btn_check_utool.setEnabled(True)
                UI.btn_change_tool.setEnabled(True)
                UI.btn_SpindleRobo_abrir.setEnabled(True)
                UI.btn_SpindleRobo_manut.setEnabled(True)
        else:
            UI.btn_move_home.setEnabled(False)
            if connected_username == "rn" or connected_username == "eng":
                UI.btn_check_uf.setEnabled(False)
                UI.btn_check_utool.setEnabled(False)
                UI.btn_change_tool.setEnabled(False)
                UI.btn_SpindleRobo_abrir.setEnabled(False)
                UI.btn_SpindleRobo_manut.setEnabled(False)

        if tag["SideA"]["Manual"]:
            UI.btn_DoorSideA_abrir.setEnabled(True)
            UI.btn_DoorSideA_fechar.setEnabled(True)
            if connected_username == "rn" or connected_username == "eng":
                UI.btn_DoorSideA_manut.setEnabled(True)
        else:
            UI.btn_DoorSideA_abrir.setEnabled(False)
            UI.btn_DoorSideA_fechar.setEnabled(False)
            if connected_username == "rn" or connected_username == "eng":
                UI.btn_DoorSideA_manut.setEnabled(False)

        if tag["SideB"]["Manual"]:
            UI.btn_DoorSideB_abrir.setEnabled(True)
            UI.btn_DoorSideB_fechar.setEnabled(True)
            if connected_username == "rn" or connected_username == "eng":
                UI.btn_DoorSideB_manut.setEnabled(True)
        else:
            UI.btn_DoorSideB_abrir.setEnabled(False)
            UI.btn_DoorSideB_fechar.setEnabled(False)
            if connected_username == "rn" or connected_username == "eng":
                UI.btn_DoorSideB_manut.setEnabled(False)

    except Exception:
        error_buttons()

def error_buttons():
    UI.btn_move_home.setEnabled(False)
    UI.btn_move_home.setText("Erro")
    UI.btn_move_home.setStyleSheet(btn_error_style)
    UI.btn_check_uf.setEnabled(False)
    UI.btn_check_uf.setText("Erro")
    UI.btn_check_uf.setStyleSheet(btn_error_style)
    UI.btn_menos_1_mm.setEnabled(False)
    UI.btn_menos_1_mm.setText("Erro")
    UI.btn_menos_1_mm.setStyleSheet(btn_error_style)
    UI.btn_termina_check_uf.setEnabled(False)
    UI.btn_termina_check_uf.setText("Erro")
    UI.btn_termina_check_uf.setStyleSheet(btn_error_style)
    UI.btn_check_utool.setEnabled(False)
    UI.btn_check_utool.setStyleSheet(btn_error_style)
    UI.btn_check_utool.setText("Erro")

    UI.btn_DoorSideA_abrir.setEnabled(False)
    UI.btn_DoorSideA_abrir.setText("Erro")
    UI.btn_DoorSideA_abrir.setStyleSheet(btn_error_style)
    UI.btn_DoorSideA_fechar.setEnabled(False)
    UI.btn_DoorSideA_fechar.setText("Erro")
    UI.btn_DoorSideA_fechar.setStyleSheet(btn_error_style)
    UI.btn_DoorSideA_manut.setEnabled(False)
    UI.btn_DoorSideA_manut.setText("Erro")
    UI.btn_DoorSideA_manut.setStyleSheet(btn_error_style)

    UI.btn_DoorSideB_abrir.setEnabled(False)
    UI.btn_DoorSideB_abrir.setText("Erro")
    UI.btn_DoorSideB_abrir.setStyleSheet(btn_error_style)
    UI.btn_DoorSideB_fechar.setEnabled(False)
    UI.btn_DoorSideB_fechar.setText("Erro")
    UI.btn_DoorSideB_fechar.setStyleSheet(btn_error_style)
    UI.btn_DoorSideB_manut.setEnabled(False)
    UI.btn_DoorSideB_manut.setText("Erro")
    UI.btn_DoorSideB_manut.setStyleSheet(btn_error_style)

    UI.btn_SpindleRobo_abrir.setEnabled(False)
    UI.btn_SpindleRobo_abrir.setText("Erro")
    UI.btn_SpindleRobo_abrir.setStyleSheet(btn_error_style)
    UI.btn_SpindleRobo_manut.setEnabled(False)
    UI.btn_SpindleRobo_manut.setText("Erro")
    UI.btn_SpindleRobo_manut.setStyleSheet(btn_error_style)

def UpdateRobotInput(tag):
    """
    Updates the screen's buttons with the readed tag values

    Params:
        tag = readed tag from BarCodeReader
    """
    global UI
    if tag["CUFOn"] and tag["Prg_running"]:
        UI.btn_menos_1_mm.setEnabled(True)
        UI.btn_termina_check_uf.setEnabled(True)
    else:
        UI.btn_menos_1_mm.setEnabled(False)
        UI.btn_termina_check_uf.setEnabled(False)

def UpdateTagsList(tags):
    global UI, tag_list
    tag_list = tags
    UI.lbl_return_plc_barcode.setText(tags[14][1])

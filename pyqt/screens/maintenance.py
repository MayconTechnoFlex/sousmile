"""Module with all functions used on the MaintenanceScreen of the application"""

from ui_py.ui_gui_final import Ui_MainWindow
from dialogs.confirmation import ConfirmationDialog
from dialogs.altera_valor import AlteraValorDialog
from dialogs.checkUF import CheckUserFrame

from utils.gui_functions import change_state_button, change_status, set_reset_btn_int
from utils.Types import PLCReturn

UI: Ui_MainWindow
tag_list: PLCReturn

def define_buttons(receive_UI: Ui_MainWindow, altValDialog: AlteraValorDialog,
                   confirmDialog: ConfirmationDialog, checkUF: CheckUserFrame):
    """
    Define the buttons of the screen

    Params:
        receive_ui = main ui of the application
        altValDialog = function for pop-up buttons
        confirm_dialog = confirmation dialog object
    """
    global UI
    UI = receive_UI

    buttons_ConfirmDialogs(confirmDialog)
    UI.btn_check_uf.clicked.connect(checkUF.show_dialog)
    UI.btn_menos_1_mm.clicked.connect(lambda: set_reset_btn_int(4, tag_list, UI.btn_menos_1_mm))
    UI.btn_termina_check_uf.clicked.connect(lambda: set_reset_btn_int(5, tag_list, UI.btn_termina_check_uf))

    UI.btn_DoorSideA_abrir.clicked.connect(lambda: set_reset_btn_int(6, tag_list, UI.btn_DoorSideA_abrir))
    UI.btn_DoorSideA_fechar.clicked.connect(lambda: set_reset_btn_int(7, tag_list, UI.btn_DoorSideA_fechar))
    UI.btn_DoorSideA_manut.clicked.connect(lambda: set_reset_btn_int(8, tag_list, UI.btn_DoorSideA_manut))
    UI.btn_DoorSideA_TimeMaint.clicked.connect(
        lambda: altValDialog.show_dialog("Alterar tempo de manutenção do lado A:", "Cyl_DoorSideA.TimeMaintTest", "int")
    )

    UI.btn_DoorSideB_abrir.clicked.connect(lambda: set_reset_btn_int(9, tag_list, UI.btn_DoorSideB_abrir))
    UI.btn_DoorSideB_fechar.clicked.connect(lambda: set_reset_btn_int(10, tag_list, UI.btn_DoorSideB_fechar))
    UI.btn_DoorSideB_manut.clicked.connect(lambda: set_reset_btn_int(11, tag_list, UI.btn_DoorSideB_manut))
    UI.btn_DoorSideB_TimeMaint.clicked.connect(
        lambda: altValDialog.show_dialog("Alterar tempo de manutenção do lado B:", "Cyl_DoorSideB.TimeMaintTest", "int")
    )

    UI.btn_SpindleRobo_abrir.clicked.connect(lambda: set_reset_btn_int(12, tag_list, UI.btn_SpindleRobo_abrir))
    UI.btn_SpindleRobo_fechar.clicked.connect(lambda: set_reset_btn_int(13, tag_list, UI.btn_SpindleRobo_fechar))
    UI.btn_SpindleRobo_manut.clicked.connect(lambda: set_reset_btn_int(14, tag_list, UI.btn_SpindleRobo_manut))
    UI.btn_SpindleRobo_TimeMaint.clicked.connect(
        lambda: altValDialog.show_dialog("Alterar tempo de manutenção do spindle:", "Cyl_SpindleRobo.TimeMaintTest", "int")
    )

def buttons_ConfirmDialogs(dialog: ConfirmationDialog):
    """
    Define the buttons that open the confirmation dialog

    Params:
        dialog = confirmation dialog itself
    """
    global UI
    UI.btn_move_home.clicked.connect(
        lambda: dialog.show_dialog("MoveHome",
                                   "Cuidado, você vai movimentar o robô para aposição inicial, "
                                   "caso tenha risco de colisão, movimente o robô para a posição inicial manualmente!"))

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
        UI.lbl_BarCodeReader_data.setText(str(tag["Data"]))
        WStatus = UI.sts_BarCodeReader_completed
        change_status(tag["ReadCompete"], WStatus)
    except:
        pass

def UpdateHMI(tag):
    """
    Updates the screen's buttons with the readed tag values

    Params:
        tag = readed tag from BarCodeReader
    """
    global UI
    if tag["SideA"]["Manual"] and tag["SideB"]["Manual"]:
        UI.btn_move_home.setEnabled(True)
        UI.btn_check_uf.setEnabled(True)
    else:
        UI.btn_move_home.setEnabled(False)
        UI.btn_check_uf.setEnabled(False)

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
    global tag_list
    tag_list = tags

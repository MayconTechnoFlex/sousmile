"""Module with all functions used on the MaintenanceScreen of the application"""

from ui_py.ui_gui import Ui_MainWindow
from dialogs.confirmation import ConfirmationDialog
from dialogs.checkUF import CheckUserFrame

from utils.gui_functions import change_state_button, change_status
from utils.Types import AltValShowDialog_WithText
from utils.db_users import get_connected_username

UI: Ui_MainWindow

def define_buttons(receive_UI: Ui_MainWindow, show_dialog: AltValShowDialog_WithText,
                   confirmDialog: ConfirmationDialog, checkUF: CheckUserFrame):
    """
    Define the buttons of the screen

    Params:
        receive_ui = main ui of the application
        show_dialog = function for pop-up buttons
        confirm_dialog = confirmation dialog object
    """
    global UI
    UI = receive_UI
    buttons_ConfirmDialogs(confirmDialog)
    UI.btn_check_uf.clicked.connect(checkUF.show_dialog)

    UI.btn_menos_1_mm.clicked.connect(lambda: change_state_button("HMI.btn_Sub1mm"))
    UI.btn_termina_check_uf.clicked.connect(lambda: change_state_button("HMI.btn_EndCheckUF"))

    UI.btn_DoorSideA_abrir.clicked.connect(lambda: change_state_button("Cyl_DoorSideA.ManRet"))
    UI.btn_DoorSideA_fechar.clicked.connect(lambda: change_state_button("Cyl_DoorSideA.ManExt"))
    UI.btn_DoorSideA_manut.clicked.connect(lambda: change_state_button("Cyl_DoorSideA.MaintTest"))
    UI.btn_DoorSideA_TimeMaint.clicked.connect(
        lambda: show_dialog("Alterar tempo de manutenção do lado A:", "Cyl_DoorSideA.TimeMaintTest", "int")
    )

    UI.btn_DoorSideB_abrir.clicked.connect(lambda: change_state_button("Cyl_DoorSideB.ManRet"))
    UI.btn_DoorSideB_fechar.clicked.connect(lambda: change_state_button("Cyl_DoorSideB.ManExt"))
    UI.btn_DoorSideB_manut.clicked.connect(lambda: change_state_button("Cyl_DoorSideB.MaintTest"))
    UI.btn_DoorSideB_TimeMaint.clicked.connect(
        lambda: show_dialog("Alterar tempo de manutenção do lado B:", "Cyl_DoorSideB.TimeMaintTest", "int")
    )

    UI.btn_SpindleRobo_abrir.clicked.connect(lambda: change_state_button("Cyl_SpindleRobo.ManRet"))
    UI.btn_SpindleRobo_fechar.clicked.connect(lambda: change_state_button("Cyl_SpindleRobo.ManExt"))
    UI.btn_SpindleRobo_manut.clicked.connect(lambda: change_state_button("Cyl_SpindleRobo.MaintTest"))
    UI.btn_SpindleRobo_TimeMaint.clicked.connect(
        lambda: show_dialog("Alterar tempo de manutenção do spindle:", "Cyl_SpindleRobo.TimeMaintTest", "int")
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
                                   "Cuidado, você vai movimentar o robô para aposição inicial, caso tenha risco de colisão, "
                                   "movimente o robô para a posição inicial manualmente!"))

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

from pyqt.ui_py.ui_gui import Ui_MainWindow
from pyqt.dialogs.confirmation import ConfirmationDialog

from pyqt.utils.gui_functions import change_state_button, change_status
from pyqt.utils.Types import AltValShowDialog_WithText

def define_buttons(ui: Ui_MainWindow, show_dialog: AltValShowDialog_WithText, confirmDialog: ConfirmationDialog):
    btns_ConfirmDialogs(ui, confirmDialog)
    ui.btn_DoorSideA_abrir.clicked.connect(lambda: change_state_button("Cyl_DoorSideA.ManRet"))
    ui.btn_DoorSideA_fechar.clicked.connect(lambda: change_state_button("Cyl_DoorSideA.ManExt"))
    ui.btn_DoorSideA_manut.clicked.connect(lambda: change_state_button("Cyl_DoorSideA.MaintTest"))
    ui.btn_DoorSideA_TimeMaint.clicked.connect(
        lambda: show_dialog("Alterar tempo de manutenção do lado A:", "Cyl_DoorSideA.TimeMaintTest", "int")
    )

    ui.btn_DoorSideB_abrir.clicked.connect(lambda: change_state_button("Cyl_DoorSideB.ManRet"))
    ui.btn_DoorSideB_fechar.clicked.connect(lambda: change_state_button("Cyl_DoorSideB.ManExt"))
    ui.btn_DoorSideB_manut.clicked.connect(lambda: change_state_button("Cyl_DoorSideB.MaintTest"))
    ui.btn_DoorSideB_TimeMaint.clicked.connect(
        lambda: show_dialog("Alterar tempo de manutenção do lado B:", "Cyl_DoorSideB.TimeMaintTest", "int")
    )

    ui.btn_SpindleRobo_abrir.clicked.connect(lambda: change_state_button("Cyl_SpindleRobo.ManRet"))
    ui.btn_SpindleRobo_fechar.clicked.connect(lambda: change_state_button("Cyl_SpindleRobo.ManExt"))
    ui.btn_SpindleRobo_manut.clicked.connect(lambda: change_state_button("Cyl_SpindleRobo.MaintTest"))
    ui.btn_SpindleRobo_TimeMaint.clicked.connect(
        lambda: show_dialog("Alterar tempo de manutenção do spindle:", "Cyl_SpindleRobo.TimeMaintTest", "int")
    )

def btns_ConfirmDialogs(ui: Ui_MainWindow, dialog: ConfirmationDialog):
    ui.btn_move_home.clicked.connect(
        lambda: dialog.show(
            "MoveHome",
            "Cuidado, você vai movimentar o robô para aposição inicial, caso tenha risco de colisão, "
            "movimente o robô para a posição inicial manualmente!"))

def UpdateCylA(ui: Ui_MainWindow, tag):
    try:
        ui.lbl_TimeMaint_A.setText(str(tag["TimeMaintTest"]))
        change_status(tag["InSenExt"], ui.sts_port_fech_a)
        change_status(tag["InSenRet"], ui.sts_port_aber_a)
        change_status(tag["OutExtCyl"], ui.sts_plc_port_fech_a)
        change_status(tag["OutRetCyl"], ui.sts_plc_port_aber_a)
    except:
        pass

def UpdateCylB(ui: Ui_MainWindow, tag):
    try:
        ui.lbl_TimeMaint_B.setText(str(tag["TimeMaintTest"]))
        change_status(tag["InSenExt"], ui.sts_port_fech_b)
        change_status(tag["InSenRet"], ui.sts_port_aber_b)
        change_status(tag["OutExtCyl"], ui.sts_plc_port_fech_b)
        change_status(tag["OutRetCyl"], ui.sts_plc_port_aber_b)
    except:
        pass

def UpdateCylSpindle(ui: Ui_MainWindow, tag):
    try:
        ui.lbl_TimeMaint_Spindle.setText(str(tag["TimeMaintTest"]))
        change_status(tag["OutExtCyl"], ui.sts_plc_liga_spindle)
        change_status(tag["OutRetCyl"], ui.sts_plc_desl_spindle)
    except:
        pass

def UpdateBarCode(ui: Ui_MainWindow, tag):
    try:
        ui.lbl_BarCodeReader_data.setText(str(tag["Data"]))
        WStatus = ui.sts_BarCodeReader_completed
        change_status(tag["ReadCompete"], WStatus)
    except:
        pass

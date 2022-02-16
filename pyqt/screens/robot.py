from pyqt.ui_py.ui_gui import Ui_MainWindow
from pyqt.dialogs.altera_valor import AlteraValorDialog
from pyqt.utils.gui_functions import change_status, change_state_button
from pyqt.utils.Types import AltValShowDialog_WithText

def define_buttons(ui: Ui_MainWindow, show_dialog: AltValShowDialog_WithText):
    ui.btn_parar_robo.clicked.connect(lambda: change_state_button("HMI.HoldRobo"))

    ui.btn_alt_vel_robo_screen.clicked.connect(
        lambda: show_dialog("Alterar velocidade do robô:", "Robo.Output.Speed", "int")
    )

def input_update(tag: dict, ui: Ui_MainWindow):
    change_status(tag["Cmd_enabled"], ui.sts_enable)
    change_status(tag["System_ready"], ui.sts_ready)
    change_status(tag["Prg_running"], ui.sts_running)
    change_status(tag["Motion_held"], ui.sts_motion_held)
    change_status(tag["Emergency"], ui.sts_emerg)
    change_status(tag["TP_Enabled"], ui.sts_tp_enabled)
    change_status(tag["Batt_alarm"], ui.sts_battery_alarm)
    change_status(tag["HomePos"], ui.sts_home_pos)
    change_status(tag["RSA"], ui.sts_robo_a)
    change_status(tag["RSB"], ui.sts_robo_b)

def output_update(tag: dict, ui: Ui_MainWindow):
    ui.lbl_RobotSpeed.setText(str(tag["Speed"]))
    change_status(tag["IMSTP"], ui.sts_imstp)
    change_status(tag["Hold"], ui.sts_hold)
    change_status(tag["SFSPD"], ui.sts_sfspd)
    change_status(tag["Start"], ui.sts_start)
    change_status(tag["Enable"], ui.sts_enabled)
    change_status(tag["FP"], ui.sts_finish_part)
    change_status(tag["MSA"], ui.sts_macro_a)
    change_status(tag["MSB"], ui.sts_macro_b)

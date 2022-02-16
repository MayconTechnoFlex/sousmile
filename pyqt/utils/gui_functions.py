#############################################
## Functions to use on the GUI
## Buttons actions
## Label actions
## Line edit actions
#############################################
from PyQt5.QtWidgets import QWidget, QDialog
from pyqt.utils.ctrl_plc import *
from pyqt.ui_py.ui_gui import Ui_MainWindow
from pyqt.utils.Types import *
#############################################
## Edit PLC information with a QLineEdit
#############################################
def write_QlineEdit(tag_name: str, dialog: QDialog, widget: QWidget, dataType: TagTypes = "string"):

    if dataType == "string":
        data = str(widget.text())
    elif dataType == "int":
        data = int(widget.text())
    elif dataType == "float":
        data = float(widget.text())
    else:
        data = None

    write_tag(tag_name, data)
    widget.clear()
    dialog.close()
#############################################
def sts_string(id_num: int, widget: QWidget):
    if id_num == 100:
        widget.setText('Transferencia do codigo da peca habilitado para o lado A1')
    elif id_num == 110:
        widget.setText('Transferencia do lado A1 aguardando python iniciar a transferencia')
    elif id_num == 120:
        widget.setText('Transferencia iniciou A1  python -> CLP')
    elif id_num == 200:
        widget.setText('Transferencia do codigo da peca habilitado para o lado A2')
    elif id_num == 210:
        widget.setText('Transferencia do lado A2 aguardando python iniciar a transferencia')
    elif id_num == 220:
        widget.setText('Transferencia iniciou lado A2  python -> CLP')
    elif id_num == 0:
        widget.setText('Aguardando leitura do código')
    else:
        widget.setText('Erro')
#############################################
def change_state_button(tag: str):
    try:
        value = read_tags(tag)
        if value == 1:
            write_tag(tag, 0)
        elif value == 0:
            write_tag(tag, 1)
        else:
            raise Exception("Valor errado recebido - gui_function/change_state_button")
    except Exception as e:
        print(e)

def set_reset_button(tag: str, widget: QWidget, text_on: str, text_off: str):
    value = read_tags(tag)
    try:
        if value == 0:
            write_tag(tag, 1)
            widget.setText(text_on)
        elif value == 1:
            write_tag(tag, 0)
            widget.setText(text_off)
        else:
            raise Exception("Valor errado recebido - gui_function/set_reset_button")
    except Exception as e:
        print(e)
#############################################
def set_dialog_buttons_engineering(ui: Ui_MainWindow, show_dialog: AltValShowDialog_WithText):
    """Function for setting all the dialogs opened from all the buttons on engineering screen"""
    ui.btn_md_val_dist_xyz.clicked.connect(
        lambda: show_dialog("Alterar a distância entre pontos (XYZ):", "ConfigPontos.Dist_XYZ", "float"))
    ui.btn_md_val_dist_c.clicked.connect(
        lambda: show_dialog("Alterar a distância entre pontos no ângulo C (horizontal):", "ConfigPontos.Diff_AngleC", "float"))
    ui.btn_md_val_dist_d.clicked.connect(
        lambda: show_dialog("Alterar a distância entre pontos no ângulo D (de ataque):", "ConfigPontos.Diff_AngleD", "float"))
    ui.btn_md_val_var_h.clicked.connect(lambda: show_dialog("Alterar a variação entre pontos:", "ConfigPontos.Dist_H", "float"))
    ui.btn_md_val_d0_mnr_pts.clicked.connect(
        lambda: show_dialog("Alterar as vezes que \"D[0]\" tem que ser menor que os outros pontos:", "ConfigPontos.DistVar", "float"))

    ui.btn_md_val_prof_corte_a1.clicked.connect(
        lambda: show_dialog("Alterar a profundidade de corte em A1:", "ConfigPontos.CutDepthA1", "float"))
    ui.btn_md_val_prof_corte_a2.clicked.connect(
        lambda: show_dialog("Alterar a profundidade de corte em A2:", "ConfigPontos.CutDepthA2", "float"))
    ui.btn_md_val_prof_corte_b1.clicked.connect(
        lambda: show_dialog("Alterar a profundidade de corte em B1:", "ConfigPontos.CutDepthB1", "float"))
    ui.btn_md_val_prof_corte_b2.clicked.connect(
        lambda: show_dialog("Alterar a profundidade de corte em B2", "ConfigPontos.CutDepthB2", "float"))

    ui.btn_md_val_max_pts.clicked.connect(lambda: show_dialog("Altera o número máximo de pontos:", "HMI.NumPosMax", "int"))
    ui.btn_md_val_vel_corte.clicked.connect(lambda: show_dialog("Altera a velocidade de corte:", "Robo.Output.CutSpeed", "int"))

    ui.btn_md_val_delay_abre_porta_a.clicked.connect(
        lambda: show_dialog("Altera delay para abrir porta A:", "Cyl_DoorSideA.TimeDelayRet", "int"))
    ui.btn_md_val_delay_abre_porta_b.clicked.connect(
        lambda: show_dialog("Altera delay para abrir porta B:", "Cyl_DoorSideB.TimeDelayRet", "int"))
    ui.btn_md_val_delay_fecha_porta_a.clicked.connect(
        lambda: show_dialog("Altera delay para fechar porta A:", "Cyl_DoorSideA.TimeDelayExt", "int"))
    ui.btn_md_val_delay_fecha_porta_b.clicked.connect(
        lambda: show_dialog("Altera delay para fechar porta B:", "Cyl_DoorSideB.TimeDelayExt", "int"))
    ui.btn_md_val_temp_alarm_sens_a.clicked.connect(
        lambda: show_dialog("Altera tempo do alarme de sensores A:", "Cyl_DoorSideA.TimeBothSenOnOff", "int"))
    ui.btn_md_val_temp_alarm_sens_b.clicked.connect(
        lambda: show_dialog("Altera tempo do alarme de sensores B:", "Cyl_DoorSideB.TimeBothSenOnOff", "int"))
    ui.btn_md_val_temp_alarm_pos_port_a.clicked.connect(
        lambda: show_dialog("Altera tempo do alarme de posição da porta A:", "Cyl_DoorSideA.TimeOut", "int"))
    ui.btn_md_val_temp_alarm_pos_port_b.clicked.connect(
        lambda: show_dialog("Altera tempo do alarme de posição da porta B:", "Cyl_DoorSideB.TimeOut", "int"))
#############################################
def set_dialog_buttons_maintenance(ui: Ui_MainWindow, show_dialog: AltValShowDialog_WithText):
    """Function for setting all the dialogs opened from all the buttons on maintenance screen"""
    ui.btn_DoorSideA_TimeMaint.clicked.connect(
        lambda: show_dialog("Alterar tempo de manutenção do lado A:","Cyl_DoorSideA.TimeMaintTest", "int")
    )
    ui.btn_DoorSideB_TimeMaint.clicked.connect(
        lambda: show_dialog("Alterar tempo de manutenção do lado B:","Cyl_DoorSideB.TimeMaintTest", "int")
    )
    ui.btn_SpindleRobo_TimeMaint.clicked.connect(
        lambda: show_dialog("Alterar tempo de manutenção do spindle:","Cyl_SpindleRobo.TimeMaintTest", "int")
    )
#############################################
def change_status(tag: str, stsWidget: QWidget):
    """Change the red/green circles of status"""
    if tag:
        stsWidget.setEnabled(True)
    else:
        stsWidget.setEnabled(False)
#############################################
def reset_product(*tags: str):
    for tag in tags:
        write_tag(tag, 0)
#############################################
def sideA_status_update(tag: dict, ui: Ui_MainWindow):
    change_status(tag["InSenExt"], ui.sts_port_fech_a)
    change_status(tag["InSenRet"], ui.sts_port_aber_a)
    change_status(tag["OutExtCyl"], ui.sts_plc_port_fech_a)
    change_status(tag["OutRetCyl"], ui.sts_plc_port_aber_a)

def sideB_status_update(tag: dict, ui: Ui_MainWindow):
    change_status(tag["InSenExt"], ui.sts_port_fech_b)
    change_status(tag["InSenRet"], ui.sts_port_aber_b)
    change_status(tag["OutExtCyl"], ui.sts_plc_port_fech_b)
    change_status(tag["OutRetCyl"], ui.sts_plc_port_aber_b)

def spindle_status_update(tag: dict, ui: Ui_MainWindow):
    change_status(tag["OutExtCyl"], ui.sts_plc_liga_spindle)
    change_status(tag["OutRetCyl"], ui.sts_plc_desl_spindle)
#############################################

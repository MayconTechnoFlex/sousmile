"""Functions to use in multiple screens and widgets"""
#############################################
from PyQt5.QtWidgets import QWidget, QDialog
from pyqt.utils.ctrl_plc import *
from pyqt.ui_py.ui_gui import Ui_MainWindow
from pyqt.utils.Types import *
#############################################
def write_LineEdit(tag_name: str, dialog: QDialog, widget: QWidget, dataType: TagTypes = "string"):
    """
    This function takes the input from a dialog and writes it in a tag
    """
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
def change_state_button(tag: str):
    """
    This function reads the tag and change its value for the opposite
    WARNING: the read tag needs to return a BOOL or INT
    """
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
#############################################
def set_reset_button(tag: str, widget: QWidget, text_on: str, text_off: str):
    """
    This function reads the tag and change its value for the opposite,
    writing the texts on the button
    WARNING: the read tag needs to return a BOOL or INT
    """
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
def change_status(tag: Union[int, bool], stsWidget: QWidget):
    """
    This function change the red/green status circles based on the tag received
    """
    if tag:
        stsWidget.setEnabled(True)
    else:
        stsWidget.setEnabled(False)
#############################################

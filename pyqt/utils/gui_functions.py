#############################################
## Functions to use on the GUI
## Buttons actions
## Label actions
## Line edit actions
#############################################
from PyQt5.QtWidgets import QWidget, QDialog
from utils.ctrl_plc import *
#############################################
## Edit PLC information with a QLineEdit
#############################################
def write_QlineEdit(tag_name: str, dialog: QDialog, widget: QWidget, dataType="string"):

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
def change_button(tag):
    value = read_tags(tag)
    if value:
        write_tag(tag, 0)
    else:
        write_tag(tag, 1)

#############################################
def set_dialog_buttons_engineering(ui, show_dialog):
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
def set_dialog_buttons_maintenance(ui, show_dialog):
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
def change_status(tag, stsWidget):
    if tag:
        stsWidget.setEnabled(True)
    else:
        stsWidget.setEnabled(False)
#############################################
def robot_input_status_update(tag, ui):
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

def robot_output_status_update(tag, ui):
    change_status(tag["IMSTP"], ui.sts_imstp)
    change_status(tag["Hold"], ui.sts_hold)
    change_status(tag["SFSPD"], ui.sts_sfspd)
    change_status(tag["Start"], ui.sts_start)
    change_status(tag["Enable"], ui.sts_enabled)
    change_status(tag["FP"], ui.sts_finish_part)
    change_status(tag["MSA"], ui.sts_macro_a)
    change_status(tag["MSB"], ui.sts_macro_b)
#############################################
def reset_product(*tags):
    for tag in tags:
        write_tag(tag, 0)
#############################################
def sideA_status_update(tag, ui):
    change_status(tag["InSenExt"], ui.sts_port_fech_a)
    change_status(tag["InSenRet"], ui.sts_port_aber_a)
    change_status(tag["OutExtCyl"], ui.sts_plc_port_fech_a)
    change_status(tag["OutRetCyl"], ui.sts_plc_port_aber_a)

def sideB_status_update(tag, ui):
    change_status(tag["InSenExt"], ui.sts_port_fech_b)
    change_status(tag["InSenRet"], ui.sts_port_aber_b)
    change_status(tag["OutExtCyl"], ui.sts_plc_port_fech_b)
    change_status(tag["OutRetCyl"], ui.sts_plc_port_aber_b)

def spindle_status_update(tag, ui):
    change_status(tag["OutExtCyl"], ui.sts_plc_liga_spindle)
    change_status(tag["OutRetCyl"], ui.sts_plc_desl_spindle)
#############################################
#############################################

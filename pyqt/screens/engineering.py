from pyqt.ui_py.ui_gui import Ui_MainWindow

from pyqt.utils.gui_functions import set_reset_button
from pyqt.utils.Types import AltValShowDialog_WithText

def define_buttons(ui: Ui_MainWindow, show_dialog: AltValShowDialog_WithText):
    # Todo => botão on/off
    def_coordinate_buttons(ui, show_dialog)
    def_prof_cort(ui, show_dialog)
    def_pts(ui, show_dialog)
    def_delayA(ui, show_dialog)
    def_delayB(ui, show_dialog)
    ui.btn_habilita_logs.clicked.connect(
        lambda: set_reset_button("HMI.EnableLog", ui.btn_habilita_logs,
                                 "Desab. Log\nde Pontos", "Habilita Log\nde Pontos"))

### Defining Dialogs
def def_coordinate_buttons(ui: Ui_MainWindow, show_dialog: AltValShowDialog_WithText):
    ui.btn_md_val_dist_xyz.clicked.connect(
        lambda: show_dialog("Alterar a distância entre pontos (XYZ):", "ConfigPontos.Dist_XYZ", "float"))
    ui.btn_md_val_dist_c.clicked.connect(
        lambda: show_dialog("Alterar a distância entre pontos no ângulo C (horizontal):", "ConfigPontos.Diff_AngleC",
                            "float"))
    ui.btn_md_val_dist_d.clicked.connect(
        lambda: show_dialog("Alterar a distância entre pontos no ângulo D (de ataque):", "ConfigPontos.Diff_AngleD",
                            "float"))
    ui.btn_md_val_var_h.clicked.connect(
        lambda: show_dialog("Alterar a variação entre pontos:", "ConfigPontos.Dist_H", "float"))
    ui.btn_md_val_d0_mnr_pts.clicked.connect(
        lambda: show_dialog("Alterar as vezes que \"D[0]\" tem que ser menor que os outros pontos:",
                            "ConfigPontos.DistVar", "float"))

def def_prof_cort(ui: Ui_MainWindow, show_dialog: AltValShowDialog_WithText):
    ui.btn_md_val_prof_corte_a1.clicked.connect(
        lambda: show_dialog("Alterar a profundidade de corte em A1:", "ConfigPontos.CutDepthA1", "float"))
    ui.btn_md_val_prof_corte_a2.clicked.connect(
        lambda: show_dialog("Alterar a profundidade de corte em A2:", "ConfigPontos.CutDepthA2", "float"))
    ui.btn_md_val_prof_corte_b1.clicked.connect(
        lambda: show_dialog("Alterar a profundidade de corte em B1:", "ConfigPontos.CutDepthB1", "float"))
    ui.btn_md_val_prof_corte_b2.clicked.connect(
        lambda: show_dialog("Alterar a profundidade de corte em B2", "ConfigPontos.CutDepthB2", "float"))

def def_pts(ui: Ui_MainWindow, show_dialog: AltValShowDialog_WithText):
    ui.btn_md_val_max_pts.clicked.connect(
        lambda: show_dialog("Altera o número máximo de pontos:", "HMI.NumPosMax", "int"))
    ui.btn_md_val_vel_corte.clicked.connect(
        lambda: show_dialog("Altera a velocidade de corte:", "Robo.Output.CutSpeed", "int"))

def def_delayA(ui: Ui_MainWindow, show_dialog: AltValShowDialog_WithText):
    ui.btn_md_val_delay_abre_porta_a.clicked.connect(
        lambda: show_dialog("Altera delay para abrir porta A:", "Cyl_DoorSideA.TimeDelayRet", "int"))
    ui.btn_md_val_delay_fecha_porta_a.clicked.connect(
        lambda: show_dialog("Altera delay para fechar porta A:", "Cyl_DoorSideA.TimeDelayExt", "int"))
    ui.btn_md_val_temp_alarm_sens_a.clicked.connect(
        lambda: show_dialog("Altera tempo do alarme de sensores A:", "Cyl_DoorSideA.TimeBothSenOnOff", "int"))
    ui.btn_md_val_temp_alarm_pos_port_a.clicked.connect(
        lambda: show_dialog("Altera tempo do alarme de posição da porta A:", "Cyl_DoorSideA.TimeOut", "int"))

def def_delayB(ui: Ui_MainWindow, show_dialog: AltValShowDialog_WithText):
    ui.btn_md_val_delay_abre_porta_b.clicked.connect(
        lambda: show_dialog("Altera delay para abrir porta B:", "Cyl_DoorSideB.TimeDelayRet", "int"))
    ui.btn_md_val_delay_fecha_porta_b.clicked.connect(
        lambda: show_dialog("Altera delay para fechar porta B:", "Cyl_DoorSideB.TimeDelayExt", "int"))
    ui.btn_md_val_temp_alarm_sens_b.clicked.connect(
        lambda: show_dialog("Altera tempo do alarme de sensores B:", "Cyl_DoorSideB.TimeBothSenOnOff", "int"))
    ui.btn_md_val_temp_alarm_pos_port_b.clicked.connect(
        lambda: show_dialog("Altera tempo do alarme de posição da porta B:", "Cyl_DoorSideB.TimeOut", "int"))

### Updating widgets
def UpdateHMI(ui: Ui_MainWindow, tag):
    try:
        currentOffset = tag["CurrentOffset"]
        ui.lbl_PosX.setText(str(round(currentOffset["PosX"], 1)))
        ui.lbl_PosY.setText(str(round(currentOffset["PosY"], 1)))
        ui.lbl_PosZ.setText(str(round(currentOffset["PosZ"], 1)))
        ui.lbl_PosC.setText(str(round(currentOffset["PosC"], 1)))
        ui.lbl_PosD.setText(str(round(currentOffset["PosD"], 1)))
        ui.lbl_MaxPts.setText(str(tag["NumPosMax"]))

        value = tag["EnableLog"]
        if value == 0:
            ui.btn_habilita_logs.setText("Desab. log\nde pontos")
        elif value == 1:
            ui.btn_habilita_logs.setText("Habilita log\nde pontos")
        else:
            pass
    except:
        pass

def UpdateConfigPts(ui: Ui_MainWindow, tag):
    try:
        ui.lbl_dist_xyz.setText(str(round(tag["Dist_XYZ"], 2)))
        ui.lbl_diff_c.setText(str(round(tag["Diff_AngleC"], 2)))
        ui.lbl_diff_d.setText(str(round(tag["Diff_AngleD"], 2)))
        ui.lbl_var_h.setText(str(round(tag["Dist_H"], 2)))
        ui.lbl_d_menor_pts.setText(str(round(tag["DistVar"], 2)))

        ui.lbl_CutDepth_A1.setText(str(round(tag["CutDepthA1"])))
        ui.lbl_CutDepth_A2.setText(str(round(tag["CutDepthA2"])))
        ui.lbl_CutDepth_B1.setText(str(round(tag["CutDepthB1"])))
        ui.lbl_CutDepth_B2.setText(str(round(tag["CutDepthB2"])))
    except:
        pass

def UpdateCylA(ui: Ui_MainWindow, tag):
    try:
        ui.lbl_delay_abre_port_a.setText(str(tag["TimeDelayRet"]))
        ui.lbl_delay_fecha_port_a.setText(str(tag["TimeDelayExt"]))
        ui.lbl_temp_alarm_sens_a.setText(str(tag["TimeBothSenOnOff"]))
        ui.lbl_temp_alarm_pos_port_a.setText(str(tag["TimeOut"]))
    except:
        pass

def UpdateCylB(ui: Ui_MainWindow, tag):
    try:
        ui.lbl_delay_abre_port_b.setText(str(tag["TimeDelayRet"]))
        ui.lbl_delay_fecha_port_b.setText(str(tag["TimeDelayExt"]))
        ui.lbl_temp_alarm_sens_b.setText(str(tag["TimeBothSenOnOff"]))
        ui.lbl_temp_alarm_pos_port_b.setText(str(tag["TimeOut"]))
    except:
        pass

def UpdateRobotPos(ui: Ui_MainWindow, tag):
    try:
        ui.lbl_RobotPos.setText(str(tag))
    except:
        pass

def UpdateRobotOutput(ui: Ui_MainWindow, tag):
    try:
        ui.lbl_CutSpeed.setText(str(tag["CutSpeed"]))
    except:
        pass

"""Module with all functions used on the EngineeringScreen of the application"""

from ui_py.ui_gui import Ui_MainWindow

from utils.gui_functions import set_reset_button
from utils.Types import AltValShowDialog_WithText

UI: Ui_MainWindow
SHOW_DIALOG: AltValShowDialog_WithText

def define_buttons(receive_ui: Ui_MainWindow, receive_show_dialog: AltValShowDialog_WithText):
    """
    Define the buttons of the screen

    Params:
        receive_ui = main ui of the application
        receive_show_dialog = function for pop-up buttons
    """
    # Todo => botão on/off
    global UI, SHOW_DIALOG
    UI = receive_ui
    SHOW_DIALOG = receive_show_dialog
    def_coordinate_buttons()
    def_prof_cort()
    def_pts()
    def_delayA()
    def_delayB()
    UI.btn_habilita_logs.clicked.connect(
        lambda: set_reset_button("HMI.EnableLog", UI.btn_habilita_logs,
                                 "Desab. Log\nde Pontos", "Habilita Log\nde Pontos"))

### Defining Dialogs
def def_coordinate_buttons():
    """
    Define the coordinate buttons of the screen
    """
    global UI, SHOW_DIALOG
    UI.btn_md_val_dist_xyz.clicked.connect(
        lambda: SHOW_DIALOG("Alterar a distância entre pontos (XYZ):", "ConfigPontos.Dist_XYZ", "float"))
    UI.btn_md_val_dist_c.clicked.connect(
        lambda: SHOW_DIALOG("Alterar a distância entre pontos no ângulo C (horizontal):", "ConfigPontos.Diff_AngleC",
                            "float"))
    UI.btn_md_val_dist_d.clicked.connect(
        lambda: SHOW_DIALOG("Alterar a distância entre pontos no ângulo D (de ataque):", "ConfigPontos.Diff_AngleD",
                            "float"))
    UI.btn_md_val_var_h.clicked.connect(
        lambda: SHOW_DIALOG("Alterar a variação entre pontos:", "ConfigPontos.Dist_H", "float"))
    UI.btn_md_val_d0_mnr_pts.clicked.connect(
        lambda: SHOW_DIALOG("Alterar as vezes que \"D[0]\" tem que ser menor que os outros pontos:",
                            "ConfigPontos.DistVar", "float"))

def def_prof_cort():
    """
    Define the depth cut buttons of the screen
    """
    global UI, SHOW_DIALOG
    UI.btn_md_val_prof_corte_a1.clicked.connect(
        lambda: SHOW_DIALOG("Alterar a profundidade de corte em A1:", "ConfigPontos.CutDepthA1", "float"))
    UI.btn_md_val_prof_corte_a2.clicked.connect(
        lambda: SHOW_DIALOG("Alterar a profundidade de corte em A2:", "ConfigPontos.CutDepthA2", "float"))
    UI.btn_md_val_prof_corte_b1.clicked.connect(
        lambda: SHOW_DIALOG("Alterar a profundidade de corte em B1:", "ConfigPontos.CutDepthB1", "float"))
    UI.btn_md_val_prof_corte_b2.clicked.connect(
        lambda: SHOW_DIALOG("Alterar a profundidade de corte em B2", "ConfigPontos.CutDepthB2", "float"))

def def_pts():
    """
    Define the point buttons of the screen
    """
    global UI, SHOW_DIALOG
    UI.btn_md_val_max_pts.clicked.connect(
        lambda: SHOW_DIALOG("Altera o número máximo de pontos:", "HMI.NumPosMax", "int"))
    UI.btn_md_val_vel_corte.clicked.connect(
        lambda: SHOW_DIALOG("Altera a velocidade de corte:", "Robo.Output.CutSpeed", "int"))

def def_delayA():
    """
    Define the Side A buttons of the screen
    """
    global UI, SHOW_DIALOG
    UI.btn_md_val_delay_abre_porta_a.clicked.connect(
        lambda: SHOW_DIALOG("Altera delay para abrir porta A:", "Cyl_DoorSideA.TimeDelayRet", "int"))
    UI.btn_md_val_delay_fecha_porta_a.clicked.connect(
        lambda: SHOW_DIALOG("Altera delay para fechar porta A:", "Cyl_DoorSideA.TimeDelayExt", "int"))
    UI.btn_md_val_temp_alarm_sens_a.clicked.connect(
        lambda: SHOW_DIALOG("Altera tempo do alarme de sensores A:", "Cyl_DoorSideA.TimeBothSenOnOff", "int"))
    UI.btn_md_val_temp_alarm_pos_port_a.clicked.connect(
        lambda: SHOW_DIALOG("Altera tempo do alarme de posição da porta A:", "Cyl_DoorSideA.TimeOut", "int"))

def def_delayB():
    """
    Define the Side B buttons of the screen
    """
    global UI, SHOW_DIALOG
    UI.btn_md_val_delay_abre_porta_b.clicked.connect(
        lambda: SHOW_DIALOG("Altera delay para abrir porta B:", "Cyl_DoorSideB.TimeDelayRet", "int"))
    UI.btn_md_val_delay_fecha_porta_b.clicked.connect(
        lambda: SHOW_DIALOG("Altera delay para fechar porta B:", "Cyl_DoorSideB.TimeDelayExt", "int"))
    UI.btn_md_val_temp_alarm_sens_b.clicked.connect(
        lambda: SHOW_DIALOG("Altera tempo do alarme de sensores B:", "Cyl_DoorSideB.TimeBothSenOnOff", "int"))
    UI.btn_md_val_temp_alarm_pos_port_b.clicked.connect(
        lambda: SHOW_DIALOG("Altera tempo do alarme de posição da porta B:", "Cyl_DoorSideB.TimeOut", "int"))

### Updating widgets
def UpdateHMI(tag):
    """
    Updates the screen's labels and buttons with the readed tag values

    Params:
        tag = readed tag from HMI
    """
    global UI
    try:
        currentOffset = tag["CurrentOffset"]
        UI.lbl_PosX.setText(str(round(currentOffset["PosX"], 1)))
        UI.lbl_PosY.setText(str(round(currentOffset["PosY"], 1)))
        UI.lbl_PosZ.setText(str(round(currentOffset["PosZ"], 1)))
        UI.lbl_PosC.setText(str(round(currentOffset["PosC"], 1)))
        UI.lbl_PosD.setText(str(round(currentOffset["PosD"], 1)))
        UI.lbl_MaxPts.setText(str(tag["NumPosMax"]))

        value = tag["EnableLog"]
        if value == 0:
            UI.btn_habilita_logs.setText("Desab. log\nde pontos")
        elif value == 1:
            UI.btn_habilita_logs.setText("Habilita log\nde pontos")
        else:
            pass
    except:
        pass

def UpdateConfigPts(tag):
    """
    Updates the screen's labels with the readed tag values

    Params:
        tag = readed tag from ConfigPts
    """
    global UI
    try:
        UI.lbl_dist_xyz.setText(str(round(tag["Dist_XYZ"], 2)))
        UI.lbl_diff_c.setText(str(round(tag["Diff_AngleC"], 2)))
        UI.lbl_diff_d.setText(str(round(tag["Diff_AngleD"], 2)))
        UI.lbl_var_h.setText(str(round(tag["Dist_H"], 2)))
        UI.lbl_d_menor_pts.setText(str(round(tag["DistVar"], 2)))

        UI.lbl_CutDepth_A1.setText(str(round(tag["CutDepthA1"])))
        UI.lbl_CutDepth_A2.setText(str(round(tag["CutDepthA2"])))
        UI.lbl_CutDepth_B1.setText(str(round(tag["CutDepthB1"])))
        UI.lbl_CutDepth_B2.setText(str(round(tag["CutDepthB2"])))
    except:
        pass

def UpdateCylA(tag):
    """
    Updates the screen's labels with the readed tag values

    Params:
        tag = readed tag from CYLSideA
    """
    global UI
    try:
        UI.lbl_delay_abre_port_a.setText(str(tag["TimeDelayRet"]))
        UI.lbl_delay_fecha_port_a.setText(str(tag["TimeDelayExt"]))
        UI.lbl_temp_alarm_sens_a.setText(str(tag["TimeBothSenOnOff"]))
        UI.lbl_temp_alarm_pos_port_a.setText(str(tag["TimeOut"]))
    except:
        pass

def UpdateCylB(tag):
    """
    Updates the screen's labels with the readed tag values

    Params:
        tag = readed tag from CYLSideB
    """
    global UI
    try:
        UI.lbl_delay_abre_port_b.setText(str(tag["TimeDelayRet"]))
        UI.lbl_delay_fecha_port_b.setText(str(tag["TimeDelayExt"]))
        UI.lbl_temp_alarm_sens_b.setText(str(tag["TimeBothSenOnOff"]))
        UI.lbl_temp_alarm_pos_port_b.setText(str(tag["TimeOut"]))
    except:
        pass

def UpdateRobotPos(tag):
    """
    Updates the screen's labels with the readed tag values

    Params:
        tag = readed tag from RobotPos
    """
    global UI
    try:
        UI.lbl_RobotPos.setText(str(tag))
    except:
        pass

def UpdateRobotOutput(tag):
    """
    Updates the screen's labels with the readed tag values

    Params:
        tag = readed tag from RobotOutput
    """
    global UI
    try:
        UI.lbl_CutSpeed.setText(str(tag["CutSpeed"]))
    except:
        pass

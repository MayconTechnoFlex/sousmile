"""Módulo com todas as funções para a tela Engenharia"""
#######################################################################################################
# Importações
#######################################################################################################
from ui_py.ui_gui_final import Ui_MainWindow
from dialogs.barcode_config import BarCodeDialog

from PyQt5.QtWidgets import QApplication, QLineEdit
from PyQt5.QtCore import QRegExp, Qt
from PyQt5.QtGui import QRegExpValidator, QIntValidator, QDoubleValidator
from PyQt5.QtCore import QThreadPool

from utils.functions.gui_functions import set_reset_btn_int
from utils.Types import PLCReturn
from utils.btn_style import *
from utils.workers.workers import *

#######################################################################################################
# Definição das variáveis globais
#######################################################################################################
UI: Ui_MainWindow
BARCODE_DIALOG: BarCodeDialog

tag_list: PLCReturn

thread_write_tags = QThreadPool()

#######################################################################################################
# Funções de Definição
#######################################################################################################
def define_buttons(main_ui: Ui_MainWindow, configBarCodeDialog: BarCodeDialog):
    """
    Define os botões da tela

    :param main_ui: Ui da aplicação
    :param configBarCodeDialog: Dialog para configurar porta do Leitor de Código de Barras
    """
    # define as variáveis globais
    global UI, BARCODE_DIALOG
    UI = main_ui
    BARCODE_DIALOG = configBarCodeDialog

    # chama função configuração de botões e labels
    def_coordinate_buttons()
    def_prof_cort()
    def_pts()
    def_delayA()
    def_delayB()
    def_set_validators()

    # botões da lateral direita
    UI.btn_habilita_logs.clicked.connect(lambda: set_reset_btn_int(3, tag_list, UI.btn_habilita_logs))
    UI.btn_config_barcode.clicked.connect(lambda: BARCODE_DIALOG.show_dialog())


#######################################################################################################
def def_coordinate_buttons():
    """Define os botões de Seleção de Pontos"""
    global UI
    UI.btn_md_val_dist_xyz.clicked.connect(lambda: change_float("ConfigPontos.Dist_XYZ", UI.le_dist_xyz))
    UI.btn_md_val_dist_c.clicked.connect(lambda: change_float("ConfigPontos.Diff_AngleC", UI.le_dist_ang_c))
    UI.btn_md_val_dist_d.clicked.connect(lambda: change_float("ConfigPontos.Diff_AngleD", UI.le_dist_ang_d))
    UI.btn_md_val_var_h.clicked.connect(lambda: change_float("ConfigPontos.Dist_H", UI.le_dist_h))
    UI.btn_md_val_d0_mnr_pts.clicked.connect(lambda: change_float("ConfigPontos.DistVar", UI.le_dist_d0))


#######################################################################################################
def def_prof_cort():
    """Define os botões de Profundidade de Corte"""
    global UI
    UI.btn_md_val_prof_corte_a1.clicked.connect(lambda: change_float("ConfigPontos.CutDepthA1", UI.le_prof_corte_a1))
    UI.btn_md_val_prof_corte_a2.clicked.connect(lambda: change_float("ConfigPontos.CutDepthA2", UI.le_prof_corte_a2))
    UI.btn_md_val_prof_corte_b1.clicked.connect(lambda: change_float("ConfigPontos.CutDepthB1", UI.le_prof_corte_b1))
    UI.btn_md_val_prof_corte_b2.clicked.connect(lambda: change_float("ConfigPontos.CutDepthB2", UI.le_prof_corte_b2))


#######################################################################################################
def def_pts():
    """Define os botões dos Offsets Atuais do Robô"""
    global UI
    UI.btn_md_val_max_pts.clicked.connect(lambda: change_int("HMI.NumPosMax", UI.le_num_max_pts))
    UI.btn_md_val_vel_corte.clicked.connect(lambda: change_int("Robo.Output.CutSpeed", UI.le_cut_spd))

#######################################################################################################
def def_delayA():
    """Define os botões do Ajuste de Tempo do lado A"""
    global UI
    UI.btn_md_val_delay_abre_porta_a.clicked.connect(
        lambda: change_int("Cyl_DoorSideA.TimeDelayRet", UI.le_open_door_a))
    UI.btn_md_val_delay_fecha_porta_a.clicked.connect(
        lambda: change_int("Cyl_DoorSideA.TimeDelayExt", UI.le_close_door_a))
    UI.btn_md_val_temp_alarm_sens_a.clicked.connect(
        lambda: change_int("Cyl_DoorSideA.TimeBothSenOnOff", UI.le_alarm_sens_a))
    UI.btn_md_val_temp_alarm_pos_port_a.clicked.connect(
        lambda: change_int("Cyl_DoorSideA.TimeOut", UI.le_alarm_door_a))

#######################################################################################################
def def_delayB():
    """Define os botões do Ajuste de Tempo do lado B"""
    global UI
    UI.btn_md_val_delay_abre_porta_b.clicked.connect(
        lambda: change_int("Cyl_DoorSideB.TimeDelayRet", UI.le_open_door_b))
    UI.btn_md_val_delay_fecha_porta_b.clicked.connect(
        lambda: change_int("Cyl_DoorSideB.TimeDelayExt", UI.le_close_door_b))
    UI.btn_md_val_temp_alarm_sens_b.clicked.connect(
        lambda: change_int("Cyl_DoorSideB.TimeBothSenOnOff", UI.le_alarm_sens_b))
    UI.btn_md_val_temp_alarm_pos_port_b.clicked.connect(
        lambda: change_int("Cyl_DoorSideB.TimeOut", UI.le_alarm_door_b))

#######################################################################################################
def def_set_validators():
    # Validators
    float_validator = QDoubleValidator(0.0, 5.0, 2)
    int_validators_max_pts = QIntValidator(0, 250)
    int_validators_cut_spd = QIntValidator(0, 100)
    int_validators_delay = QIntValidator(0, 10000)

    UI.le_prof_corte_a1.setValidator(float_validator)
    UI.le_prof_corte_a2.setValidator(float_validator)
    UI.le_prof_corte_b1.setValidator(float_validator)
    UI.le_prof_corte_b2.setValidator(float_validator)

    UI.le_dist_xyz.setValidator(float_validator)
    UI.le_dist_ang_c.setValidator(float_validator)
    UI.le_dist_ang_d.setValidator(float_validator)
    UI.le_dist_h.setValidator(float_validator)
    UI.le_dist_d0.setValidator(float_validator)

    UI.le_num_max_pts.setValidator(int_validators_max_pts)
    UI.le_cut_spd.setValidator(int_validators_cut_spd)

    UI.le_close_door_a.setValidator(int_validators_delay)
    UI.le_close_door_b.setValidator(int_validators_delay)
    UI.le_open_door_a.setValidator(int_validators_delay)
    UI.le_open_door_b.setValidator(int_validators_delay)
    UI.le_alarm_door_a.setValidator(int_validators_delay)
    UI.le_alarm_door_b.setValidator(int_validators_delay)
    UI.le_alarm_sens_a.setValidator(int_validators_delay)
    UI.le_alarm_sens_b.setValidator(int_validators_delay)

#######################################################################################################
def change_int(tag_name: str, line_edit: QLineEdit):
    if line_edit.text():
        value = int(line_edit.text())
        line_edit.clear()
        worker = Worker_WriteTags(tag_name, value)
        thread_write_tags.start(worker)

#######################################################################################################
def change_float(tag_name: str, line_edit: QLineEdit):
    if line_edit.text():
        value = float(line_edit.text())
        line_edit.clear()
        worker = Worker_WriteTags(tag_name, value)
        thread_write_tags.start(worker)
#######################################################################################################
# Funções de Atualização
#######################################################################################################
def UpdateHMI(tag):
    """
    Atualiza os Labels e os Botões da tela com os valores do CLP

    :param tag: Tag lida do CLP
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

        if tag["EnableLog"] == 1:
            UI.btn_habilita_logs.setStyleSheet(checked_button_style)
            UI.btn_habilita_logs.setText("Desab. log\nde pontos")
        elif tag["EnableLog"] == 0:
            UI.btn_habilita_logs.setStyleSheet(base_button_style)
            UI.btn_habilita_logs.setText("Habilitar log\nde pontos")
        else:
            pass

        QApplication.restoreOverrideCursor()

    except Exception as e:
        setErrorButton(UI.btn_habilita_logs)
        print(f'{e} - engineering.UpdateHMI')


#######################################################################################################
def UpdateConfigPts(tag):
    """
    Atualiza os Labels da tela com os valores do CLP

    :param tag: Tag lida do CLP
    """
    global UI
    try:
        UI.lbl_dist_xyz.setText(str(round(tag["Dist_XYZ"], 2)))
        UI.lbl_diff_c.setText(str(round(tag["Diff_AngleC"], 2)))
        UI.lbl_diff_d.setText(str(round(tag["Diff_AngleD"], 2)))
        UI.lbl_var_h.setText(str(round(tag["Dist_H"], 2)))
        UI.lbl_d_menor_pts.setText(str(round(tag["DistVar"], 2)))

        UI.lbl_CutDepth_A1.setText(str(round(tag["CutDepthA1"], 1)))
        UI.lbl_CutDepth_A2.setText(str(round(tag["CutDepthA2"], 1)))
        UI.lbl_CutDepth_B1.setText(str(round(tag["CutDepthB1"], 1)))
        UI.lbl_CutDepth_B2.setText(str(round(tag["CutDepthB2"], 1)))
    except:
        pass


#######################################################################################################
def UpdateCylA(tag):
    """
    Atualiza os Labels da tela com os valores do CLP

    :param tag: Tag lida do CLP
    """
    global UI
    try:
        UI.lbl_delay_abre_port_a.setText(str(tag["TimeDelayRet"]))
        UI.lbl_delay_fecha_port_a.setText(str(tag["TimeDelayExt"]))
        UI.lbl_temp_alarm_sens_a.setText(str(tag["TimeBothSenOnOff"]))
        UI.lbl_temp_alarm_pos_port_a.setText(str(tag["TimeOut"]))
    except:
        pass


#######################################################################################################
def UpdateCylB(tag):
    """
    Atualiza os Labels da tela com os valores do CLP

    :param tag: Tag lida do CLP
    """
    global UI
    try:
        UI.lbl_delay_abre_port_b.setText(str(tag["TimeDelayRet"]))
        UI.lbl_delay_fecha_port_b.setText(str(tag["TimeDelayExt"]))
        UI.lbl_temp_alarm_sens_b.setText(str(tag["TimeBothSenOnOff"]))
        UI.lbl_temp_alarm_pos_port_b.setText(str(tag["TimeOut"]))
    except:
        pass


#######################################################################################################
def UpdateRobotPos(tag):
    """
    Atualiza o Label da tela com os valores do CLP

    :param tag: Tag lida do CLP
    """
    global UI
    try:
        UI.lbl_RobotPos.setText(str(tag))
    except:
        pass


#######################################################################################################
def UpdateRobotOutput(tag):
    """
    Atualiza o Label da tela com os valores do CLP

    :param tag: Tag lida do CLP
    """
    global UI
    try:
        UI.lbl_CutSpeed.setText(str(tag["CutSpeed"]))
    except:
        pass


#######################################################################################################
def UpdateTagsList(tags):
    global tag_list
    tag_list = tags

#######################################################################################################

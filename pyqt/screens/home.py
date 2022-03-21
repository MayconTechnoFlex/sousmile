"""Módulo com todas as funções para a tela Home"""
#######################################################################################################
# Importações
#######################################################################################################
from utils.Types import PLCReturn
from typing import Literal

from PyQt5.QtCore import QThreadPool
from PyQt5.QtWidgets import QLabel, QApplication, QPushButton
from ui_py.ui_gui_final import Ui_MainWindow
from dialogs.insert_code import InsertCodeDialog

from utils.functions.gui_functions import set_reset_btn_int
from utils.btn_style import *
from utils.functions.gui_functions import change_status

from utils.workers.workers import Worker_ToggleBtnValue
#######################################################################################################
# Definição das Variáveis Globais
#######################################################################################################
UI: Ui_MainWindow
tag_list: PLCReturn
write_thread = QThreadPool()
#######################################################################################################
# Funçoes de Controle
#######################################################################################################
def sts_string(id_num: int, widget: QLabel, side: Literal["A", "B"]):
    """
    Set the label with the code reader status

    Params:
        id_num = code of the status
        widget = label for status text
    """
    if side == "A":
        if id_num == 100:
            widget.setText('Transferência do código da peça habilitado para o lado A1')
        elif id_num == 110:
            widget.setText('Transferência do lado A1 aguardando python iniciar a transferência')
        elif id_num == 120:
            widget.setText('Transferência iniciou lado A1: python -> CLP')
        elif id_num == 200:
            widget.setText('Transferência do código da peça habilitado para o lado A2')
        elif id_num == 210:
            widget.setText('Transferência do lado A2 aguardando python iniciar a transferência')
        elif id_num == 220:
            widget.setText('Transferência iniciou lado A2: python -> CLP')
        elif id_num == 0:
            widget.setText('Aguardando leitura do código')
        else:
            widget.setText('Erro')
    elif side == "B":
        if id_num == 100:
            widget.setText('Transferência do código da peça habilitado para o lado B1')
        elif id_num == 110:
            widget.setText('Transferência do lado B1 aguardando python iniciar a transferência')
        elif id_num == 120:
            widget.setText('Transferência iniciou lado B1: python -> CLP')
        elif id_num == 200:
            widget.setText('Transferência do código da peça habilitado para o lado B2')
        elif id_num == 210:
            widget.setText('Transferência do lado B2 aguardando python iniciar a transferência')
        elif id_num == 220:
            widget.setText('Transferência iniciou lado B2: python -> CLP')
        elif id_num == 0:
            widget.setText('Aguardando leitura do código')
        else:
            widget.setText('Erro')
#######################################################################################################
def transfer_data(side: Literal["A1", "A2", "B1", "B2"], button: QPushButton):
    global UI, write_thread
    if side == "A1"\
            or side == "A2"\
            or side == "B1"\
            or side == "B2":
        worker_toggle = Worker_ToggleBtnValue(f"HMI.ManTransData{side}", 0, button)
        write_thread.start(worker_toggle, priority=0)
    else:
        raise ValueError('Nome incorreto do lado, deve ser "A1", "A2", "B1", "B2"')
#######################################################################################################
# Funções de Definição
#######################################################################################################
def define_buttons(receive_ui: Ui_MainWindow, dialog: InsertCodeDialog):
    """
    Define the buttons of the screen

    Params:
        receive_ui = main ui of the application
        dialog = function for pop-up buttons
    """
    global UI, tag_list
    UI = receive_ui
    UI.btn_in_cod_man_a1.clicked.connect(lambda: dialog.show_dialog('DataCtrl_A1.ProdCode', "string", UI, "A1"))
    UI.btn_in_cod_man_a2.clicked.connect(lambda: dialog.show_dialog('DataCtrl_A2.ProdCode', "string", UI, "A2"))
    UI.btn_in_cod_man_b1.clicked.connect(lambda: dialog.show_dialog('DataCtrl_B1.ProdCode', "string", UI, "B1"))
    UI.btn_in_cod_man_b2.clicked.connect(lambda: dialog.show_dialog('DataCtrl_B2.ProdCode', "string", UI, "B2"))

    UI.btn_trans_dados_man_a1.clicked.connect(lambda: transfer_data("A1", UI.btn_trans_dados_man_a1))
    UI.btn_trans_dados_man_a2.clicked.connect(lambda: transfer_data("A2", UI.btn_trans_dados_man_a2))
    UI.btn_trans_dados_man_b1.clicked.connect(lambda: transfer_data("B1", UI.btn_trans_dados_man_b1))
    UI.btn_trans_dados_man_b2.clicked.connect(lambda: transfer_data("B2", UI.btn_trans_dados_man_b2))

    UI.btn_man_auto_lado_a.clicked.connect(lambda: set_reset_btn_int(0, tag_list, UI.btn_man_auto_lado_a))
    UI.btn_man_auto_lado_b.clicked.connect(lambda: set_reset_btn_int(1, tag_list, UI.btn_man_auto_lado_b))
#######################################################################################################
# Funções de Atualização
#######################################################################################################
def UpdateDataCtrl_A1(tag):
    """
    Updates the screen's labels with the readed tag values

    Params:
        tag = readed tag from DataCtrl_A1
    """
    global UI
    try:
        # UI.lbl_ProdCode_A1.setText(tag['ProdCode'])
        UI.lbl_FileNumPos_A1.setText(str(tag['FileNumPos']))
        UI.lbl_NumPos_A1.setText(str(tag['NumPos']))
        UI.lbl_IndexPos_A1.setText(str(tag['IndexPos']))
        change_status(tag["Complete"], UI.sts_Complete_A1)
    except:
        pass
#######################################################################################################
def UpdateDataCtrl_A2(tag):
    """
    Updates the screen's labels with the readed tag values

    Params:
        tag = readed tag from DataCtrl_A2
    """
    global UI
    try:
        # UI.lbl_ProdCode_A2.setText(tag['ProdCode'])
        UI.lbl_FileNumPos_A2.setText(str(tag['FileNumPos']))
        UI.lbl_NumPos_A2.setText(str(tag['NumPos']))
        UI.lbl_IndexPos_A2.setText(str(tag['IndexPos']))
        change_status(tag["Complete"], UI.sts_Complete_A2)
    except:
        pass
#######################################################################################################
def UpdateDataCtrl_B1(tag):
    """
    Updates the screen's labels with the readed tag values

    Params:
        tag = readed tag from DataCtrl_B1
    """
    global UI
    try:
        # UI.lbl_ProdCode_B1.setText(tag['ProdCode'])
        UI.lbl_FileNumPos_B1.setText(str(tag['FileNumPos']))
        UI.lbl_NumPos_B1.setText(str(tag['NumPos']))
        UI.lbl_IndexPos_B1.setText(str(tag['IndexPos']))
        change_status(tag["Complete"], UI.sts_Complete_B1)
    except:
        pass
#######################################################################################################
def UpdateDataCtrl_B2(tag):
    """
    Updates the screen's labels with the readed tag values

    Params:
        tag = readed tag from DataCtrl_B2
    """
    global UI
    try:
        # UI.lbl_ProdCode_B2.setText(tag['ProdCode'])
        UI.lbl_FileNumPos_B2.setText(str(tag['FileNumPos']))
        UI.lbl_NumPos_B2.setText(str(tag['NumPos']))
        UI.lbl_IndexPos_B2.setText(str(tag['IndexPos']))
        change_status(tag["Complete"], UI.sts_Complete_B2)
    except:
        pass
#######################################################################################################
def UpdateHMI(tag):
    """
    Updates the screen's labels and status widgets with the readed tag values

    Params:
        tag = readed tag from HMI
    """

    global UI
    try:
        prodTag = tag["Production"]
        UI.lbl_production_TimeCutA1.setText(str(round(prodTag['TimeCutA1'], 2)))
        UI.lbl_production_TimeCutA2.setText(str(round(prodTag['TimeCutA2'], 2)))
        UI.lbl_production_TimeCutB1.setText(str(round(prodTag['TimeCutB1'], 2)))
        UI.lbl_production_TimeCutB2.setText(str(round(prodTag['TimeCutB2'], 2)))
        sts_string(tag['Sts']['TransDataSideA'], UI.lbl_sts_TransDataSideA, "A")
        sts_string(tag['Sts']['TransDataSideB'], UI.lbl_sts_TransDataSideB, "B")

        ### buttons manual <-> auto
        if tag['SideA']['ModeValue'] == 0:
            hmi_side_a_mode_value = 0
            UI.btn_man_auto_lado_a.setStyleSheet(base_button_style)
            UI.btn_man_auto_lado_a.setText('Manual')
        elif tag['SideA']['ModeValue'] == 1:
            hmi_side_a_mode_value = 1
            UI.btn_man_auto_lado_a.setStyleSheet(checked_button_style)
            UI.btn_man_auto_lado_a.setText('Automático')

        if tag['SideB']['ModeValue'] == 0:
            hmi_side_b_mode_value = 0
            UI.btn_man_auto_lado_b.setStyleSheet(base_button_style)
            UI.btn_man_auto_lado_b.setText('Manual')
        elif tag['SideB']['ModeValue'] == 1:
            hmi_side_b_mode_value = 1
            UI.btn_man_auto_lado_b.setStyleSheet(checked_button_style)
            UI.btn_man_auto_lado_b.setText('Automático')

        QApplication.restoreOverrideCursor()

        #### setting alarm status
        if tag["AlarmSideA"]:
            UI.sts_sem_alarm_a.setEnabled(False)
        else:
            UI.sts_sem_alarm_a.setEnabled(True)

        if tag["AlarmSideB"]:
            UI.sts_sem_alarm_b.setEnabled(False)
        else:
            UI.sts_sem_alarm_b.setEnabled(True)

        if tag["Sts"]["TransDataSideA"] == 0:
            UI.btn_trans_dados_man_a1.setEnabled(True)
            UI.btn_trans_dados_man_a2.setEnabled(True)
        else:
            UI.btn_trans_dados_man_a1.setEnabled(False)
            UI.btn_trans_dados_man_a2.setEnabled(False)

        if tag["Sts"]["TransDataSideB"] == 0:
            UI.btn_trans_dados_man_b1.setEnabled(True)
            UI.btn_trans_dados_man_b2.setEnabled(True)
        else:
            UI.btn_trans_dados_man_b1.setEnabled(False)
            UI.btn_trans_dados_man_b2.setEnabled(False)

        QApplication.restoreOverrideCursor()


    except Exception as e:
        hmi_side_a_mode_value = None
        hmi_side_b_mode_value = None
        UI.btn_man_auto_lado_a.setStyleSheet(btn_error_style)
        UI.btn_man_auto_lado_b.setStyleSheet(btn_error_style)
        UI.btn_man_auto_lado_a.setText('Erro')
        UI.btn_man_auto_lado_b.setText('Erro')
        UI.btn_man_auto_lado_a.setEnabled(False)
        UI.btn_man_auto_lado_b.setEnabled(False)
        print(f'{e} - home.UpdateHMI')

    return hmi_side_a_mode_value, hmi_side_b_mode_value
#######################################################################################################
def UpdateRobotInput(tag):
    """
    Updates the screen's labels and status widgets with the readed tag values

    Params:
        tag = readed tag from HMI
    """
    global UI

    try:
        if tag["Prg_running"] and tag["RSA"]:
            UI.btn_man_auto_lado_a.setEnabled(False)
            UI.btn_man_auto_lado_b.setEnabled(False)
        else:
            UI.btn_man_auto_lado_a.setEnabled(True)
            UI.btn_man_auto_lado_b.setEnabled(True)
    except Exception as e:
        print(f"{e} - UpdateRobotInput - home")
#######################################################################################################
def UpdateTagsList(tags):
    global tag_list
    tag_list = tags
#######################################################################################################

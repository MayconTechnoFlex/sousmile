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
tag_list: PLCReturn = None
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
            widget.setText('Transferência do cód. habilitado')
        elif id_num == 110:
            widget.setText('Aguardando Python iniciar a transf.')
        elif id_num == 120:
            widget.setText('Transferência iniciou')
        elif id_num == 200:
            widget.setText('Transferência do cód. habilitado')
        elif id_num == 210:
            widget.setText('Aguardando Python iniciar a transf.')
        elif id_num == 220:
            widget.setText('Transferência iniciou')
        elif id_num == 0:
            widget.setText('Aguardando leitura do código')
        else:
            widget.setText('Erro')
    elif side == "B":
        if id_num == 100:
            widget.setText('Transferência do cód. habilitado')
        elif id_num == 110:
            widget.setText('Aguardando Python iniciar a transf.')
        elif id_num == 120:
            widget.setText('Transferência iniciou')
        elif id_num == 200:
            widget.setText('Transferência do cód. habilitado')
        elif id_num == 210:
            widget.setText('Aguardando Python iniciar a transf.')
        elif id_num == 220:
            widget.setText('Transferência iniciou')
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

    global UI, tag_list
    try:
        prodTag = tag["Production"]
        UI.lbl_production_TimeCutA1.setText(str(round(prodTag['TimeCutA1'], 2)))
        UI.lbl_production_TimeCutA2.setText(str(round(prodTag['TimeCutA2'], 2)))
        UI.lbl_production_TimeCutB1.setText(str(round(prodTag['TimeCutB1'], 2)))
        UI.lbl_production_TimeCutB2.setText(str(round(prodTag['TimeCutB2'], 2)))
        sts_string(tag['Sts']['TransDataSideA1'], UI.lbl_sts_TransDataSideA1, "A")
        sts_string(tag['Sts']['TransDataSideA2'], UI.lbl_sts_TransDataSideA2, "A")
        sts_string(tag['Sts']['TransDataSideB1'], UI.lbl_sts_TransDataSideB1, "B")
        sts_string(tag['Sts']['TransDataSideB2'], UI.lbl_sts_TransDataSideB2, "B")

        setButton(UI.btn_trans_dados_man_a1, "Transferir dados\n manualmente A1")
        setButton(UI.btn_trans_dados_man_a2, "Transferir dados\n manualmente A2")
        setButton(UI.btn_trans_dados_man_b1, "Transferir dados\n manualmente B1")
        setButton(UI.btn_trans_dados_man_b2, "Transferir dados\n manualmente B2")

        ### buttons manual <-> auto
        if tag['SideA']['Manual']:
            hmi_side_a_mode_value = 0
            UI.btn_man_auto_lado_a.setStyleSheet(base_button_style)
            UI.btn_man_auto_lado_a.setText('Manual')
        elif tag['SideA']['Auto']:
            hmi_side_a_mode_value = 1
            UI.btn_man_auto_lado_a.setStyleSheet(checked_button_style)
            UI.btn_man_auto_lado_a.setText('Automático')

        if tag['SideB']['Manual']:
            hmi_side_b_mode_value = 0
            UI.btn_man_auto_lado_b.setStyleSheet(base_button_style)
            UI.btn_man_auto_lado_b.setText('Manual')
        elif tag['SideB']['Auto']:
            hmi_side_b_mode_value = 1
            UI.btn_man_auto_lado_b.setStyleSheet(checked_button_style)
            UI.btn_man_auto_lado_b.setText('Automático')

        QApplication.restoreOverrideCursor()

        # setting status
        change_status(tag["SideA"]["Manual"], UI.sts_auto_man_a)
        change_status(tag["SideB"]["Manual"], UI.sts_auto_man_b)
        change_status(tag["RobotCuttingSideA"], UI.sts_robo_cort_a)
        change_status(tag["RobotCuttingSideB"], UI.sts_robo_cort_b)
        if tag_list:
            change_status(tag_list[15], UI.sts_seg_cort_a)
            change_status(tag_list[16], UI.sts_seg_cort_b)

        if tag["AlarmSideA"]:
            change_status(0, UI.sts_sem_alarm_a)
        else:
            change_status(1, UI.sts_sem_alarm_a)

        if tag["AlarmSideB"]:
            change_status(0, UI.sts_sem_alarm_b)
        else:
            change_status(1, UI.sts_sem_alarm_b)

        # enable/disable buttons
        # if (not tag["Sts"]["TransDataSideA1"] and not tag["Sts"]["TransDataSideA2"]
        #     and not tag["Sts"]["TransDataSideB1"] and not tag["Sts"]["TransDataSideB2"]) and \
        #         not tag["AlarmSideA"] and tag["SideA"]["Auto"]:
        #     UI.btn_trans_dados_man_a1.setEnabled(True)
        #     UI.btn_trans_dados_man_a2.setEnabled(True)
        # else:
        #     UI.btn_trans_dados_man_a1.setEnabled(False)
        #     UI.btn_trans_dados_man_a2.setEnabled(False)
        #
        # if (not tag["Sts"]["TransDataSideA1"] and not tag["Sts"]["TransDataSideA2"]
        #     and not tag["Sts"]["TransDataSideB1"] and not tag["Sts"]["TransDataSideB2"])  and \
        #         not tag["AlarmSideB"] and tag["SideB"]["Auto"]:
        #     UI.btn_trans_dados_man_b1.setEnabled(True)
        #     UI.btn_trans_dados_man_b2.setEnabled(True)
        # else:
        #     UI.btn_trans_dados_man_b1.setEnabled(False)
        #     UI.btn_trans_dados_man_b2.setEnabled(False)

        if not tag["AlarmSideA"] and not tag["Sts"]["TransDataSideA1"] and tag["SideA"]["Auto"]:
            UI.btn_trans_dados_man_a1.setEnabled(True)
        else:
            UI.btn_trans_dados_man_a1.setEnabled(False)

        if not tag["AlarmSideA"] and not tag["Sts"]["TransDataSideA2"] and tag["SideA"]["Auto"]:
            UI.btn_trans_dados_man_a2.setEnabled(True)
        else:
            UI.btn_trans_dados_man_a2.setEnabled(False)

        if not tag["AlarmSideB"] and not tag["Sts"]["TransDataSideB1"] and tag["SideB"]["Auto"]:
            UI.btn_trans_dados_man_b1.setEnabled(True)
        else:
            UI.btn_trans_dados_man_b1.setEnabled(False)

        if not tag["AlarmSideB"] and not tag["Sts"]["TransDataSideB2"] and tag["SideB"]["Auto"]:
            UI.btn_trans_dados_man_b2.setEnabled(True)
        else:
            UI.btn_trans_dados_man_b2.setEnabled(False)


        QApplication.restoreOverrideCursor()


    except Exception as e:
        hmi_side_a_mode_value = None
        hmi_side_b_mode_value = None
        setErrorButton(UI.btn_man_auto_lado_a)
        setErrorButton(UI.btn_man_auto_lado_b)
        setErrorButton(UI.btn_trans_dados_man_a1)
        setErrorButton(UI.btn_trans_dados_man_a2)
        setErrorButton(UI.btn_trans_dados_man_b1)
        setErrorButton(UI.btn_trans_dados_man_b2)
        print(f'{e} - home.UpdateHMI')

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

"""Module with all functions used on the HomeScreen of the application"""
from utils.Types import PLCReturn

from PyQt5.QtWidgets import QLabel
from ui_py.ui_gui import Ui_MainWindow
from dialogs.insert_code import InsertCodeDialog

from utils.gui_functions import set_reset_button, set_reset_btn_int
from utils.Types import AltValShowDialog_WithoutText

UI: Ui_MainWindow

tag_list = PLCReturn

def sts_string(id_num: int, widget: QLabel):
    """
    Set the label with the code reader status

    Params:
        id_num = code of the status
        widget = label for status text
    """
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

def define_buttons(receive_ui: Ui_MainWindow, dialog: InsertCodeDialog):
    """
    Define the buttons of the screen

    Params:
        receive_ui = main ui of the application
        dialog = function for pop-up buttons
    """
    global UI
    UI = receive_ui
    UI.btn_in_cod_man_a1.clicked.connect(lambda: dialog.show_dialog('DataCtrl_A1.ProdCode', "string"))
    UI.btn_in_cod_man_a2.clicked.connect(lambda: dialog.show_dialog('DataCtrl_A2.ProdCode', "string"))
    UI.btn_in_cod_man_b1.clicked.connect(lambda: dialog.show_dialog('DataCtrl_B1.ProdCode', "string"))
    UI.btn_in_cod_man_b2.clicked.connect(lambda: dialog.show_dialog('DataCtrl_B2.ProdCode', "string"))

    UI.btn_man_auto_lado_a.clicked.connect(lambda: set_reset_btn_int(0, tag_list))
    UI.btn_man_auto_lado_b.clicked.connect(lambda: set_reset_btn_int(1, tag_list))

def UpdateDataCtrl_A1(tag):
    """
    Updates the screen's labels with the readed tag values

    Params:
        tag = readed tag from DataCtrl_A1
    """
    global UI
    try:
        UI.lbl_ProdCode_A1.setText(tag['ProdCode'])
        UI.lbl_FileNumPos_A1.setText(str(tag['FileNumPos']))
        UI.lbl_NumPos_A1.setText(str(tag['NumPos']))
        UI.lbl_IndexPos_A1.setText(str(tag['IndexPos']))
    except:
        pass

def UpdateDataCtrl_A2(tag):
    """
    Updates the screen's labels with the readed tag values

    Params:
        tag = readed tag from DataCtrl_A2
    """
    global UI
    try:
        UI.lbl_ProdCode_A2.setText(tag['ProdCode'])
        UI.lbl_FileNumPos_A2.setText(str(tag['FileNumPos']))
        UI.lbl_NumPos_A2.setText(str(tag['NumPos']))
        UI.lbl_IndexPos_A2.setText(str(tag['IndexPos']))
    except:
        pass

def UpdateDataCtrl_B1(tag):
    """
    Updates the screen's labels with the readed tag values

    Params:
        tag = readed tag from DataCtrl_B1
    """
    global UI
    try:
        UI.lbl_ProdCode_B1.setText(tag['ProdCode'])
        UI.lbl_FileNumPos_B1.setText(str(tag['FileNumPos']))
        UI.lbl_NumPos_B1.setText(str(tag['NumPos']))
        UI.lbl_IndexPos_B1.setText(str(tag['IndexPos']))
    except:
        pass

def UpdateDataCtrl_B2(tag):
    """
    Updates the screen's labels with the readed tag values

    Params:
        tag = readed tag from DataCtrl_B2
    """
    global UI
    try:
        UI.lbl_ProdCode_B2.setText(tag['ProdCode'])
        UI.lbl_FileNumPos_B2.setText(str(tag['FileNumPos']))
        UI.lbl_NumPos_B2.setText(str(tag['NumPos']))
        UI.lbl_IndexPos_B2.setText(str(tag['IndexPos']))
    except:
        pass

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
        sts_string(tag['Sts']['TransDataSideA'], UI.lbl_sts_TransDataSideA)
        sts_string(tag['Sts']['TransDataSideB'], UI.lbl_sts_TransDataSideB)

        ### buttons manual <-> auto
        if tag['SideA']['ModeValue'] == 0:
            hmi_side_a_mode_value = 0
            # UI.btn_man_auto_lado_a.setStyleSheet("background-color : #ffdf00; color : #565656")
            UI.btn_man_auto_lado_a.setChecked(True)
            UI.sts_auto_man_a.setEnabled(True)
            UI.btn_man_auto_lado_a.setText('Manual')
        elif tag['SideA']['ModeValue'] == 1:
            hmi_side_a_mode_value = 1
            # UI.btn_man_auto_lado_a.setStyleSheet("background-color : #565656; color : #ffdf00")
            UI.btn_man_auto_lado_a.setChecked(False)
            UI.sts_auto_man_a.setEnabled(False)
            UI.btn_man_auto_lado_a.setText('Automático')

        if tag['SideB']['ModeValue'] == 0:
            hmi_side_b_mode_value = 0
            # UI.btn_man_auto_lado_b.setStyleSheet("background-color : #ffdf00; color : #565656")
            UI.btn_man_auto_lado_b.setChecked(True)
            UI.sts_auto_man_b.setEnabled(True)
            UI.btn_man_auto_lado_b.setText('Manual')
        elif tag['SideB']['ModeValue'] == 1:
            hmi_side_b_mode_value = 1
            # UI.btn_man_auto_lado_b.setStyleSheet("background-color : #565656; color : #ffdf00")
            UI.btn_man_auto_lado_b.setChecked(False)
            UI.sts_auto_man_b.setEnabled(False)
            UI.btn_man_auto_lado_b.setText('Automático')

        #### setting alarm status
        if tag["AlarmSideA"]:
            UI.sts_sem_alarm_a.setEnabled(False)
        else:
            UI.sts_sem_alarm_a.setEnabled(True)

        if tag["AlarmSideB"]:
            UI.sts_sem_alarm_b.setEnabled(False)
        else:
            UI.sts_sem_alarm_b.setEnabled(True)

    except Exception as e:
        hmi_side_a_mode_value = None
        hmi_side_b_mode_value = None
        UI.btn_man_auto_lado_a.setStyleSheet("background-color : #dc1f1f; color : black")
        UI.btn_man_auto_lado_b.setStyleSheet("background-color : #dc1f1f; color : black")
        UI.btn_man_auto_lado_a.setText('Erro')
        UI.btn_man_auto_lado_b.setText('Erro')
        print(f'{e} - home.UpdateHMI')

    return hmi_side_a_mode_value, hmi_side_b_mode_value

def UpdateTagsList(tags):
    global tag_list
    tag_list = tags
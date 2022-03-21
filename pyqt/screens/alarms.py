"""Módulo com todas as funções para a tela Alarmes"""
#######################################################################################################
# Importações
#######################################################################################################
from datetime import datetime

from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem
from PyQt5.QtCore import Qt

from ui_py.ui_gui_final import Ui_MainWindow
from dialogs.alarm import AlarmDialog
from utils.functions.alarm_control import *
#######################################################################################################
# Definição das variáveis globais
#######################################################################################################
UI: Ui_MainWindow
DIALOG: AlarmDialog
SHOW_ALARM_SCREEN = None
CURRENT_ROW = 0

hasAlarm: List[bool] = []
for i in range(0, 97):
    hasAlarm.append(False)
#######################################################################################################
# Funções de Definição
#######################################################################################################
def define_buttons(main_ui: Ui_MainWindow, AlarmDialog: AlarmDialog, show_alarm_screen):
    """
    Define os botões da tela

    :param main_ui: Ui principal da aplicação
    :param AlarmDialog: Dialog de novo alarme
    :param show_alarm_screen: Função que mostra o Dialog de novo alarme
    """
    global UI, DIALOG, SHOW_ALARM_SCREEN
    # define as variaveis globais
    UI = main_ui
    DIALOG = AlarmDialog
    SHOW_ALARM_SCREEN = show_alarm_screen

    # define os botões de cima/baixo
    UI.btn_sobe_alarm.clicked.connect(lambda: row_up(UI.alarm_list_widget))
    UI.btn_desce_alarm.clicked.connect(lambda: row_down(UI.alarm_list_widget))
    UI.btn_sobe_alarm_hist.clicked.connect(lambda: row_up(UI.hist_alarm_list_widget))
    UI.btn_desce_alarm_hist.clicked.connect(lambda: row_down(UI.hist_alarm_list_widget))
#######################################################################################################
# Funções de Controle
#######################################################################################################
def verify_alarms(alarm_time: str, alarm_id: int, alarm_active: bool):
    """
    Verifica se o alarme está ativo e habilita/desabilita ele na tela

    :param alarm_time: String do momento que o alarme aparece
    :param alarm_id: Número do alarme
    :param alarm_active: O sinal que vem do CLP
    """
    if alarm_active and not hasAlarm[alarm_id]:
        hasAlarm[alarm_id] = True
        define_new_alarm(alarm_time, alarm_id)
    elif not alarm_active and hasAlarm[alarm_id]:
        hasAlarm[alarm_id] = False
        delete_alarm_row(alarm_id)
#######################################################################################################
def define_new_alarm(alarm_time: str, alarm_id: int):
    """
    Adiciona um novo alarme na tela e na variável interna do módulo

    :param alarm_time: String do momento que o alarme aparece
    :param alarm_id: Número do alarme
    """
    listWidget = UI.alarm_list_widget
    histWidget = UI.hist_alarm_list_widget
    dialogsListWidget = DIALOG.ui.alarm_list_widget

    row_num = 0
    hist_row_num = 0
    alarm_msg: str = get_alarm_message(alarm_id)

    set_alarm_list(alarm_id, alarm_time, alarm_msg)

    time_item = QTableWidgetItem()
    msg_item = QTableWidgetItem()
    time_item.setText(str(alarm_time))
    msg_item.setText(alarm_msg)

    hist_time = QTableWidgetItem()
    hist_msg = QTableWidgetItem()
    hist_time.setText(str(alarm_time))
    hist_msg.setText(alarm_msg)

    dialog_time = QTableWidgetItem()
    dialog_msg = QTableWidgetItem()
    dialog_time.setText(str(alarm_time))
    dialog_msg.setText(alarm_msg)

    listWidget.insertRow(row_num)
    listWidget.setItem(row_num, 0, time_item)
    listWidget.setItem(row_num, 1, msg_item)

    histWidget.insertRow(hist_row_num)
    histWidget.setItem(hist_row_num, 0, hist_time)
    histWidget.setItem(hist_row_num, 1, hist_msg)

    dialogsListWidget.insertRow(0)
    dialogsListWidget.setItem(0, 0, dialog_time)
    dialogsListWidget.setItem(0, 1, dialog_msg)
    DIALOG.show_dialog(SHOW_ALARM_SCREEN)
#######################################################################################################
def delete_alarm_row(alarm_id: int):
    """
    Deleta um alarme da tela de Alarmes, mas não da tela Histórico de Alarmes

    :param alarm_id: Número do alarme
    """
    listWidget: QTableWidget = UI.alarm_list_widget

    itemFound = listWidget.findItems(f"Alarme {alarm_id}:", Qt.MatchContains)
    listWidget.setCurrentItem(itemFound[0])

    row_num = itemFound[0].row()

    listWidget.removeRow(row_num)
    delete_alarm_from_list(alarm_id)
#######################################################################################################
def row_down(listWidget: QTableWidget):
    """
    Chamado quando o botão para descer é pressionado

    :param listWidget: Widget da lista de alarmes
    """
    global CURRENT_ROW

    CURRENT_ROW = listWidget.currentRow()
    CURRENT_ROW += 1

    listWidget.setCurrentCell(CURRENT_ROW, 0)
#######################################################################################################
def row_up(listWidget: QTableWidget):
    """
    Chamado quando o botão para subir é pressionado

    :param listWidget: Widget da lista de alarmes
    """
    global CURRENT_ROW

    CURRENT_ROW = listWidget.currentRow()
    CURRENT_ROW -= 1

    listWidget.setCurrentCell(CURRENT_ROW, 0)
#######################################################################################################
# Funções de Atualização
#######################################################################################################
def UpdateAlarms(tag):
    """Recebe a tag do worker e manda para verificação"""
    try:
        alarms_count = 0
        for alarm in tag:
            time_now = str(datetime.now())
            verify_alarms(time_now[0:19], alarms_count, alarm[1])
            alarms_count += 1
    except Exception as e:
        print(f"{e} - dialogs/alarms.py - UpdateAlarms")
#######################################################################################################

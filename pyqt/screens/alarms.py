"""Module with all functions used on the AlarmScreen of the application"""

from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem
from PyQt5.QtCore import Qt

from ui_py.ui_gui import Ui_MainWindow
from utils.alarm_control import *

UI: Ui_MainWindow
CURRENT_ROW = 0

def define_buttons(receive_ui: Ui_MainWindow):
    """
    Define the buttons of the screen

    Params:
        receive_ui = main ui of the application
    """
    global UI
    UI = receive_ui
    UI.btn_sobe_alarm.clicked.connect(lambda: row_up(UI.alarm_list_widget))
    UI.btn_desce_alarm.clicked.connect(lambda: row_down(UI.alarm_list_widget))
    UI.btn_sobe_alarm_hist.clicked.connect(lambda: row_up(UI.hist_alarm_list_widget))
    UI.btn_desce_alarm_hist.clicked.connect(lambda: row_down(UI.hist_alarm_list_widget))

def define_new_alarm(alarm_time: str, alarm_id: int):
    """
    Set up a new alarm in screen and in the alarm_control module

    Params:
        alarm_time = string of when the alarm appears
        alarm_id = number of the alarm
    """
    listWidget = UI.alarm_list_widget
    histWidget = UI.hist_alarm_list_widget
    """
    da pra adicionar de duas formas:
    1ª adicionar no final da lista
    row_num = listWidget.rowCount()
    hist_row_num = histWidget.rowCount()
    ToDo => 2ª adicionar ao início da lista
    """
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

    listWidget.insertRow(row_num)
    listWidget.setItem(row_num, 0, time_item)
    listWidget.setItem(row_num, 1, msg_item)

    histWidget.insertRow(hist_row_num)
    histWidget.setItem(hist_row_num, 0, hist_time)
    histWidget.setItem(hist_row_num, 1, hist_msg)

def delete_alarm_row(alarm_id: int):
    """
    Deletes an alarm from the Actual Alarms Screen, but keeps in the historic

    Params:
        alarm_id = number of the alarm
    """
    listWidget: QTableWidget = UI.alarm_list_widget

    itemFound = listWidget.findItems(f"Alarme {alarm_id}:", Qt.MatchContains)
    listWidget.setCurrentItem(itemFound[0])

    row_num = itemFound[0].row()

    listWidget.removeRow(row_num)
    delete_alarm_from_list(alarm_id)

def row_down(listWidget: QTableWidget):
    """
    Called when the button down is pressed, show in the screen what row is selected

    Params:
        listWidget = list widget of alarms
    """
    global CURRENT_ROW

    CURRENT_ROW = listWidget.currentRow()
    CURRENT_ROW += 1

    listWidget.setCurrentCell(CURRENT_ROW, 0)

def row_up(listWidget: QTableWidget):
    """
    Called when the button up is pressed, show in the screen what row is selected

    Params:
        listWidget = list widget of alarms
    """
    global CURRENT_ROW

    CURRENT_ROW = listWidget.currentRow()
    CURRENT_ROW -= 1

    listWidget.setCurrentCell(CURRENT_ROW, 0)

def UpdateAlarms(tag):
    print(tag)

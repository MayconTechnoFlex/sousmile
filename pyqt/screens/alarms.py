from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem
from PyQt5.QtCore import Qt
from pyqt.ui_py.ui_gui import Ui_MainWindow

from pyqt.utils.alarm_control import *

def define_buttons(ui: Ui_MainWindow):
    ui.btn_sobe_alarm.clicked.connect(lambda: row_up(ui.alarm_list_widget))
    ui.btn_desce_alarm.clicked.connect(lambda: row_down(ui.alarm_list_widget))
    ui.btn_sobe_alarm_hist.clicked.connect(lambda: row_up(ui.hist_alarm_list_widget))
    ui.btn_desce_alarm_hist.clicked.connect(lambda: row_down(ui.hist_alarm_list_widget))

def define_new_alarm(ui: Ui_MainWindow, alarm_time: str, alarm_id: int):
    listWidget = ui.alarm_list_widget
    histWidget = ui.hist_alarm_list_widget
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

def delete_alarm_row(ui: Ui_MainWindow, alarm_id: int):
    listWidget: QTableWidget = ui.alarm_list_widget

    itemFound = listWidget.findItems(f"Alarme {alarm_id}:", Qt.MatchContains)
    listWidget.setCurrentItem(itemFound[0])

    row_num = itemFound[0].row()

    listWidget.removeRow(row_num)
    delete_alarm_from_list(alarm_id)

CURRENT_ROW = 0
def row_down(listWidget: QTableWidget):
    global CURRENT_ROW

    CURRENT_ROW = listWidget.currentRow()
    CURRENT_ROW += 1

    listWidget.setCurrentCell(CURRENT_ROW, 0)

def row_up(listWidget: QTableWidget):
    global CURRENT_ROW

    CURRENT_ROW = listWidget.currentRow()
    CURRENT_ROW -= 1

    listWidget.setCurrentCell(CURRENT_ROW, 0)

"""Functions to use in multiple screens and widgets"""
#############################################
import time
import ctypes
from typing import Union
from PyQt5.QtCore import QObject, QThreadPool, QThread, pyqtSignal, pyqtSlot
from PyQt5.QtWidgets import QLineEdit, QDialog, QWidget
from utils.ctrl_plc import read_tags, write_tag
from utils.Types import TagTypes
from utils.Tags import *
from utils.workers import Worker_WriteTags
#############################################
# Workers and trheads
#############################################
write_thread = QThreadPool()
#############################################
def write_LineEdit(tag_name: str, dialog: QDialog, widget: QLineEdit, data_type: TagTypes = "string"):
    """
    Takes the input from a dialog and writes it in a tag

    Params:
        tag_name = the Tag that will be changed with the widget text
        dialog = the dialog itself
        widget = the QLineEdit widget
        data_type = the value's type that will be sent to the PLC
    """
    if data_type == "string":
        data = str(widget.text())
    elif data_type == "int":
        data = int(widget.text())
    elif data_type == "float":
        data = float(widget.text())
    else:
        data = None

    try:
        write_tag(tag_name, data)
    except Exception as e:
        print(f"{e} - write_LineEdit")
    widget.clear()
    dialog.close()
#############################################
def change_state_button(tag: str, tag_indicator: int = None):
    """
    Reads the tag and change its value for the opposite
    WARNING: the read tag needs to return a BOOL or INT

    Params:
        tag = the Tag of the PLC
    """
    try:
        if not tag_indicator:
            value = read_tags(tag)
        else:
            value = tag_indicator

        if value == 1:
            write_tag(tag, 0)
        elif value == 0:
            write_tag(tag, 1)
        else:
            raise Exception("Valor errado recebido - gui_function/change_state_button")
    except Exception as e:
        print(f"{e} - gui_function.py - change_state_button")
#############################################
def set_reset_button(tag_to_write: str, widget: QWidget, text_on: str, text_off: str, tag_indicator: bool = None):

    """
    Reads the tag and change its value for the opposite,
    writing the texts on the button
    WARNING: the read tag needs to return a BOOL or INT

    Params:
        tag_to_write = the Tag of the PLC that we write the value
        tag_indicator = the Tag of the PLC used to show the status of the button
        widget = the button or label that was interacted
        text_on = text if the value is True
        text_off = text if the value is False
    """

    try:
        widget.setStyleSheet(":disabled{background-color:#cbcbcb; color: #cbcccc}")
        widget.setEnabled(False)

        value = read_tags(tag_indicator)

        if value == 0:
            write_tag(tag_to_write, 1)
            widget.setText(text_on)
        elif value == 1:
            write_tag(tag_to_write, 0)
            widget.setText(text_off)
        else:
            raise Exception("Valor errado recebido - gui_function/set_reset_button")
        time.sleep(0.5)
        widget.setEnabled(True)
    except Exception as e:
        print(f"{e} - gui_function.py - set_reset_button")
        widget.setEnabled(True)


def set_reset_btn_int(i: int, tag_list, widget):
    global write_thread
    #widget.setEnabled(False)
    try:
        tag_name = tag_list[i][0]
        value = tag_list[i][1]
        if value == 0:
            write_value = 1
            worker_write_tags = Worker_WriteTags(tag_name, write_value)
            write_thread.start(worker_write_tags, priority=0)
        elif value == 1:
            write_value = 0
            worker_write_tags = Worker_WriteTags(tag_name, write_value)
            write_thread.start(worker_write_tags, priority=0)
    except Exception as e:
        print(e)
    #time.sleep(4)
    #widget.setEnabled(True)


#############################################
def change_status(tag: Union[int, bool], stsWidget: QWidget):
    """
    Change the red/green status circles based on the tag received

    Params:
        tag = the result of a read Tag
        stsWidget = widget that will be activated/deactivated
    """
    if tag:
        stsWidget.setEnabled(True)
    else:
        stsWidget.setEnabled(False)











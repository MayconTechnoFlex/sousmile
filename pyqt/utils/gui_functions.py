"""Functions to use in multiple screens and widgets"""
#############################################
from typing import Union
from PyQt5.QtWidgets import QLineEdit, QDialog, QWidget
from utils.ctrl_plc import read_tags, write_tag
from utils.Types import TagTypes
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

    write_tag(tag_name, data)
    widget.clear()
    dialog.close()
#############################################
def change_state_button(tag: str, tag_indicator: int = 0):
    """
    Reads the tag and change its value for the opposite
    WARNING: the read tag needs to return a BOOL or INT

    Params:
        tag = the Tag of the PLC
    """
    value = read_tags(tag)
    try:
        if value == 1:
            write_tag(tag, 0)
        elif value == 0:
            write_tag(tag, 1)
        else:
            raise Exception("Valor errado recebido - gui_function/change_state_button")
    except Exception as e:
        print(e)
#############################################
def set_reset_button(tag_to_write: str, tag_indicator: bool, widget: QWidget, text_on: str, text_off: str):
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
        if tag_indicator == 0:
            write_tag(tag_to_write, 1)
            widget.setText(text_on)
        elif tag_indicator == 1:
            write_tag(tag_to_write, 0)
            widget.setText(text_off)
        else:
            raise Exception("Valor errado recebido - gui_function/set_reset_button")
    except Exception as e:
        print(e)
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

"""Functions to use in multiple screens and widgets"""
#############################################
from PyQt5.QtWidgets import QLineEdit, QDialog, QWidget
from pyqt.utils.ctrl_plc import *
from pyqt.ui_py.ui_gui import Ui_MainWindow
from pyqt.utils.Types import *
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
def change_state_button(tag: str):
    """
    Reads the tag and change its value for the opposite
    WARNING: the read tag needs to return a BOOL or INT

    Params:
        tag = the Tag of the PLC
    """
    try:
        value = read_tags(tag)
        if value == 1:
            write_tag(tag, 0)
        elif value == 0:
            write_tag(tag, 1)
        else:
            raise Exception("Valor errado recebido - gui_function/change_state_button")
    except Exception as e:
        print(e)
#############################################
def set_reset_button(tag: str, widget: QWidget, text_on: str, text_off: str):
    """
    Reads the tag and change its value for the opposite,
    writing the texts on the button
    WARNING: the read tag needs to return a BOOL or INT

    params:
        tag = the Tag of the PLC
        widget = the button or label that was interacted
        text_on = text if the value is True
        text_off = text if the value is False
    """
    try:
        value = read_tags(tag)
        if value == 0:
            write_tag(tag, 1)
            widget.setText(text_on)
        elif value == 1:
            write_tag(tag, 0)
            widget.setText(text_off)
        else:
            raise Exception("Valor errado recebido - gui_function/set_reset_button")
    except Exception as e:
        print(e)
#############################################
def change_status(tag: Union[int, bool], stsWidget: QWidget):
    """
    Change the red/green status circles based on the tag received

    params:
        tag = the result of a read Tag
        stsWidget = widget that will be activated/deactivated
    """
    if tag:
        stsWidget.setEnabled(True)
    else:
        stsWidget.setEnabled(False)

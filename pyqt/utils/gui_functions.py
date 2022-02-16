"""Functions to use in multiple screens and widgets"""
#############################################
from PyQt5.QtWidgets import QWidget, QDialog
from pyqt.utils.ctrl_plc import *
from pyqt.ui_py.ui_gui import Ui_MainWindow
from pyqt.utils.Types import *
#############################################
def write_LineEdit(tag_name: str, dialog: QDialog, widget: QWidget, dataType: TagTypes = "string"):
    """
    This function takes the input from a dialog and writes it in a tag
    """
    if dataType == "string":
        data = str(widget.text())
    elif dataType == "int":
        data = int(widget.text())
    elif dataType == "float":
        data = float(widget.text())
    else:
        data = None

    write_tag(tag_name, data)
    widget.clear()
    dialog.close()
#############################################
def change_state_button(tag: str):
    """
    This function reads the tag and change its value for the opposite
    WARNING: the read tag needs to return a BOOL or INT
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
    This function reads the tag and change its value for the opposite,
    writing the texts on the button
    WARNING: the read tag needs to return a BOOL or INT
    """
    value = read_tags(tag)
    try:
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
    This function change the red/green status circles based on the tag received
    """
    if tag:
        stsWidget.setEnabled(True)
    else:
        stsWidget.setEnabled(False)
#############################################

"""Functions to use in multiple screens and widgets"""
#############################################
from typing import Union
from PyQt5.QtCore import QThreadPool
from PyQt5.QtWidgets import QWidget, QLabel
from utils.workers import Worker_WriteTags, Worker_ReadTags
#############################################
# Workers and trheads
#############################################
write_thread = QThreadPool()
read_thread = QThreadPool()
#############################################
def set_reset_btn_int(i: int, tag_list, widget: QWidget) -> None:
    """
    Change the value of the button with the tag_list

    Params:
        i = the tag of tag_list
        tag_list = list of tags from utils.Tags
        widget = button or widget that must be disabled
    """
    global write_thread
    try:
        tag_name = tag_list[i][0]
        value = tag_list[i][1]
        if value == 0:
            write_value = 1
            worker_write_tags = Worker_WriteTags(tag_name, write_value, widget)
            write_thread.start(worker_write_tags, priority=0)
        elif value == 1:
            write_value = 0
            worker_write_tags = Worker_WriteTags(tag_name, write_value, widget)
            write_thread.start(worker_write_tags, priority=0)
    except Exception as e:
        print(e)
#############################################
def change_status(tag: Union[int, bool], stsWidget: QWidget) -> None:
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

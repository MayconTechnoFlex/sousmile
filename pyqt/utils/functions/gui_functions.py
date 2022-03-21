"""Funções para usar em multiplas telas e módulos"""
#######################################################################################################
# Importações
#######################################################################################################
from typing import Union
from PyQt5.QtCore import QThreadPool
from PyQt5.QtWidgets import QWidget
from utils.workers.workers import Worker_WriteTags
#######################################################################################################
# Definindo Threads
#######################################################################################################
write_thread = QThreadPool()
read_thread = QThreadPool()
#######################################################################################################
# Funções
#######################################################################################################
def set_reset_btn_int(i: int, tag_list, widget: QWidget) -> None:
    """
    Muda o valor de um botão utilizando a Tag List Geral

    :param i: Index da TagList que contenha a tag desejada
    :param tag_list: A lista das tags
    :param widget: Botão ou Widget que será desabilitado
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
#######################################################################################################
def change_status(tag_value: Union[int, bool], stsWidget: QWidget) -> None:
    """
    Muda os Status Vermelho/Verde baseado no valor recebido

    :param tag_value: Valor da Tag para a verificação
    :param stsWidget: Widget que será habilitado/desabilitado
    """
    if tag_value:
        stsWidget.setEnabled(True)
    else:
        stsWidget.setEnabled(False)
#######################################################################################################

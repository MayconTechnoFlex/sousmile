"""Module with all functions used on the InOutScreen of the application"""

from typing import Callable
from ui_py.ui_gui import Ui_MainWindow

from utils.gui_functions import change_status

UI: Ui_MainWindow

def define_buttons(receive_ui: Ui_MainWindow, change_screen_func: Callable[[], None]):
    """
    Define the buttons of the screen

    Params:
        receive_ui = main ui of the application
        change_screen_func = function to back the screen to maintenance
    """
    global UI
    UI = receive_ui
    UI.btn_volta_manut_screen.clicked.connect(change_screen_func)

def atualize_widgets():
    """
    Updates the screen's status widgets with the readed tag values
    """
    # Todo => criar função para atualizar as entradas e saídas
    global UI
    pass

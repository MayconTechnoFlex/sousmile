from typing import Callable
from ui_py.ui_gui import Ui_MainWindow

from utils.gui_functions import change_status

ui: Ui_MainWindow

def define_buttons(receive_ui: Ui_MainWindow, change_screen_func: Callable[[], None]):
    global ui
    ui = receive_ui
    ui.btn_volta_manut_screen.clicked.connect(change_screen_func)

def atualize_widgets():
    # Todo => criar função para atualizar as entradas e saídas
    global ui
    pass

from typing import Callable
from pyqt.ui_py.ui_gui import Ui_MainWindow

from pyqt.utils.gui_functions import change_status

def define_buttons(ui: Ui_MainWindow, change_screen_func: Callable[[], None]):
    ui.btn_volta_manut_screen.clicked.connect(change_screen_func)

def atualize_widgets(ui: Ui_MainWindow):
    # Todo => criar função para atualizar as entradas e saídas
    pass

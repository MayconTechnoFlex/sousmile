"""Permission functions of security module"""

from ui_py.ui_gui_v1 import Ui_MainWindow

def noneUserConnected(ui: Ui_MainWindow):
    if ui.stackedWidget.currentIndex() == 1:
        ui.stackedWidget.setCurrentIndex(0)
    ui.btnRobotScreen.setEnabled(False)

def operConnected(ui: Ui_MainWindow):
    ui.btnRobotScreen.setEnabled(True)

def engConnected(ui: Ui_MainWindow):
    ui.btnRobotScreen.setEnabled(True)

def rnConnected(ui: Ui_MainWindow):
    ui.btnRobotScreen.setEnabled(True)

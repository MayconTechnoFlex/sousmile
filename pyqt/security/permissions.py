"""Permission functions of security module"""

from ui_py.ui_gui_final import Ui_MainWindow

def noneUserConnected(ui: Ui_MainWindow):
    if ui.stackedWidget.currentIndex() == 6:
        ui.stackedWidget.setCurrentIndex(0)
    ui.btnEngineeringScreen.setEnabled(False)

def operConnected(ui: Ui_MainWindow):
    ui.btnEngineeringScreen.setEnabled(False)

def engConnected(ui: Ui_MainWindow):
    ui.btnEngineeringScreen.setEnabled(True)

def rnConnected(ui: Ui_MainWindow):
    ui.btnEngineeringScreen.setEnabled(False)

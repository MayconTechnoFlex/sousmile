"""Permission functions of security module"""

from ui_py.ui_gui_final import Ui_MainWindow

def noneUserConnected(ui: Ui_MainWindow):
    if ui.stackedWidget.currentIndex() == 6:
        ui.stackedWidget.setCurrentIndex(0)
    ui.btnEngineeringScreen.setEnabled(False)
    ui.btn_change_tool.setEnabled(False)
    ui.btn_check_uf.setEnabled(False)
    ui.btn_check_utool.setEnabled(False)
    ui.btn_DoorSideA_manut.setEnabled(False)
    ui.btn_DoorSideB_manut.setEnabled(False)
    ui.btn_SpindleRobo_manut.setEnabled(False)
    ui.btn_SpindleRobo_abrir.setEnabled(False)

def operConnected(ui: Ui_MainWindow):
    ui.btnEngineeringScreen.setEnabled(False)
    ui.btn_change_tool.setEnabled(False)
    ui.btn_check_uf.setEnabled(False)
    ui.btn_check_utool.setEnabled(False)
    ui.btn_DoorSideA_manut.setEnabled(False)
    ui.btn_DoorSideB_manut.setEnabled(False)
    ui.btn_SpindleRobo_manut.setEnabled(False)
    ui.btn_SpindleRobo_abrir.setEnabled(False)

def engConnected(ui: Ui_MainWindow):
    ui.btnEngineeringScreen.setEnabled(True)
    ui.btn_change_tool.setEnabled(True)
    ui.btn_check_uf.setEnabled(True)
    ui.btn_check_utool.setEnabled(True)
    ui.btn_DoorSideA_manut.setEnabled(True)
    ui.btn_DoorSideB_manut.setEnabled(True)
    ui.btn_SpindleRobo_manut.setEnabled(True)
    ui.btn_SpindleRobo_abrir.setEnabled(True)

def rnConnected(ui: Ui_MainWindow):
    ui.btnEngineeringScreen.setEnabled(True)
    ui.btn_change_tool.setEnabled(True)
    ui.btn_check_uf.setEnabled(True)
    ui.btn_check_utool.setEnabled(True)
    ui.btn_DoorSideA_manut.setEnabled(True)
    ui.btn_DoorSideB_manut.setEnabled(True)
    ui.btn_SpindleRobo_manut.setEnabled(True)
    ui.btn_SpindleRobo_abrir.setEnabled(True)

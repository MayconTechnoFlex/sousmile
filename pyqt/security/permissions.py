"""Permissões do módulo de segurança"""
#######################################################################################################
# Importações
#######################################################################################################
from ui_py.ui_gui_final import Ui_MainWindow
#######################################################################################################
# Funções que definem o acesso
#######################################################################################################
def noneUserConnected(ui: Ui_MainWindow):
    """Para caso de nenhum usuário conectado"""
    if ui.stackedWidget.currentWidget() == ui.engineering_screen:
        ui.stackedWidget.setCurrentWidget(ui.home_screen)
    ui.btnEngineeringScreen.setEnabled(False)
    ui.btn_change_tool.setEnabled(False)
    ui.btn_check_uf.setEnabled(False)
    ui.btn_check_utool.setEnabled(False)
    ui.btn_DoorSideA_manut.setEnabled(False)
    ui.btn_DoorSideB_manut.setEnabled(False)
    ui.btn_SpindleRobo_manut.setEnabled(False)
    ui.btn_SpindleRobo_abrir.setEnabled(False)
#######################################################################################################
def operConnected(ui: Ui_MainWindow):
    """Para caso de um Operador conectado"""
    if ui.stackedWidget.currentWidget() == ui.engineering_screen:
        ui.stackedWidget.setCurrentWidget(ui.home_screen)
    ui.btnEngineeringScreen.setEnabled(False)
    ui.btn_change_tool.setEnabled(False)
    ui.btn_check_uf.setEnabled(False)
    ui.btn_check_utool.setEnabled(False)
    ui.btn_DoorSideA_manut.setEnabled(False)
    ui.btn_DoorSideB_manut.setEnabled(False)
    ui.btn_SpindleRobo_manut.setEnabled(False)
    ui.btn_SpindleRobo_abrir.setEnabled(False)
#######################################################################################################
def engConnected(ui: Ui_MainWindow):
    """Para caso de um Engenheiro conectado"""
    ui.btnEngineeringScreen.setEnabled(True)
    ui.btn_change_tool.setEnabled(True)
    ui.btn_check_uf.setEnabled(True)
    ui.btn_check_utool.setEnabled(True)
    ui.btn_DoorSideA_manut.setEnabled(True)
    ui.btn_DoorSideB_manut.setEnabled(True)
    ui.btn_SpindleRobo_manut.setEnabled(True)
    ui.btn_SpindleRobo_abrir.setEnabled(True)
#######################################################################################################
def rnConnected(ui: Ui_MainWindow):
    """Para caso de um Programador (RNRobotics) conectado"""
    ui.btnEngineeringScreen.setEnabled(True)
    ui.btn_change_tool.setEnabled(True)
    ui.btn_check_uf.setEnabled(True)
    ui.btn_check_utool.setEnabled(True)
    ui.btn_DoorSideA_manut.setEnabled(True)
    ui.btn_DoorSideB_manut.setEnabled(True)
    ui.btn_SpindleRobo_manut.setEnabled(True)
    ui.btn_SpindleRobo_abrir.setEnabled(True)
#######################################################################################################

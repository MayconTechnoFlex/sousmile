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
#######################################################################################################
def operConnected(ui: Ui_MainWindow):
    """Para caso de um Operador conectado"""
    if ui.stackedWidget.currentWidget() == ui.engineering_screen:
        ui.stackedWidget.setCurrentWidget(ui.home_screen)
    ui.btnEngineeringScreen.setEnabled(False)
#######################################################################################################
def engConnected(ui: Ui_MainWindow):
    """Para caso de um Engenheiro conectado"""
    ui.btnEngineeringScreen.setEnabled(True)
#######################################################################################################
def rnConnected(ui: Ui_MainWindow):
    """Para caso de um Programador (RNRobotics) conectado"""
    ui.btnEngineeringScreen.setEnabled(True)
#######################################################################################################

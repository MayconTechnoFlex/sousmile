"""Dialog que mostra quando novos alarmes chegam"""
#######################################################################################################
# Importações
#######################################################################################################
from PyQt5.QtWidgets import QDialog
from PyQt5.QtCore import Qt
from ui_py.ui_alarm_dialog import Ui_Dialog
#######################################################################################################

class AlarmDialog(QDialog):
    """Dialog que mostra quando novos alarmes chegam"""

    def __init__(self, parents=None):
        super(AlarmDialog, self).__init__(parents)
        self.setWindowFlag(Qt.WindowContextHelpButtonHint, False)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.define_buttons()
    ###################################################################################################
    def show_dialog(self, show_alarm_screen):
        """
        Função que mostra o dialogo na tela

        :param show_alarm_screen: Função para mostra a tela de alarmes
        """
        self.show_alarm_screen = show_alarm_screen
        self.exec_()
    ###################################################################################################
    def closeEvent(self, event):
        """Após a tela ser fechada, essa função é executada, limpando todos os alarmes"""
        while self.ui.alarm_list_widget.rowCount() != 0:
            self.ui.alarm_list_widget.removeRow(0)
    ###################################################################################################
    def go_to_alarms(self):
        """Envia o usuário para a tela de alarmes"""
        self.close()
        self.show_alarm_screen()
    ###################################################################################################
    def define_buttons(self):
        """Define os botões do dialog"""
        self.ui.btn_go_alarm_screen.clicked.connect(self.go_to_alarms)
        self.ui.btn_cancel.clicked.connect(self.close)
#######################################################################################################

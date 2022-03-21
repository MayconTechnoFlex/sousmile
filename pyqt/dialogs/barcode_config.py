"""Dialog para configurar a porta do Leitor de Código de Barras"""
#######################################################################################################
# Importações
#######################################################################################################
from PyQt5.QtWidgets import QDialog
from PyQt5.QtCore import Qt
from ui_py.ui_barCode_dialog import Ui_Dialog

from utils.functions.serial_ports import get_serial_ports, set_my_port
#######################################################################################################

class BarCodeDialog(QDialog):
    """Dialog para configurar da porta do Leitor de Código de Barras"""

    def __init__(self, parents=None):
        super(BarCodeDialog, self).__init__(parents)
        self.setWindowFlag(Qt.WindowContextHelpButtonHint, False)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        # configura a porta inicialmente, se houver
        self.serial_ports = get_serial_ports()
    ###################################################################################################
    def show_dialog(self):
        """Mostra o dialog na tela"""
        self.serial_ports = get_serial_ports()
        if len(self.serial_ports) != 1:
            for port in self.serial_ports:
                self.ui.comboBox.addItem(port)
            self.define_buttons()
            self.exec_()
        else:
            print(f"Somente uma porta serial conectada ({self.serial_ports[0]}), aguarde a conexão automática...")
    ###################################################################################################
    def closeEvent(self, event):
        """Ativado quando o dialog é fechado, limpa a caixa de seleção"""
        self.ui.comboBox.clear()
    ###################################################################################################
    def confirm_action(self):
        """Função chamada quando o botão Confirmar é clicado"""
        port = self.ui.comboBox.currentText()
        set_my_port(port)
        self.close()
    ###################################################################################################
    def define_buttons(self):
        self.ui.btn_confirm.clicked.connect(self.confirm_action)
        self.ui.btn_cancel.clicked.connect(self.close)
#######################################################################################################

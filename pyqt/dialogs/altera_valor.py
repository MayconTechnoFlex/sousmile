"""Dialog para mudar o valor de alguma tag"""
#######################################################################################################
# Importações
#######################################################################################################
from PyQt5.QtWidgets import QDialog
from PyQt5.QtCore import QRegExp, Qt
from PyQt5.QtGui import QRegExpValidator

from ui_py.ui_alt_val_dialog import Ui_Dialog2
from utils.Types import TagTypes
from utils.workers.write_thread import Thread_LineEdit
#######################################################################################################

class AlteraValorDialog(QDialog):
    """Dialog para mudar o valor de alguma tag"""

    def __init__(self, parents=None):
        super(AlteraValorDialog, self).__init__(parents)
        self.setWindowFlag(Qt.WindowContextHelpButtonHint, False)
        self.ui = Ui_Dialog2()
        self.ui.setupUi(self)

        # setup de variáveis
        self.TAG_INDEX: str = ""
        self.TAG_TYPE: TagTypes = ""
        self.thread: Thread_LineEdit
    ###################################################################################################
    def closeEvent(self, event):
        """Essa função é executada quando o dialog é fechado"""
        self.ui.new_value.clear()
    ###################################################################################################
    def show_dialog(self, text: str, tag: str, tag_type: TagTypes = "string"):
        """
        Mostra o dialog na tela

        :param text: O que será escrito no dialog
        :param tag: Tag do CLP que o LineEdit vai mudar
        :param tag_type: O tipo de valor que será enviado ao CLP
        """
        self.TAG_INDEX = tag
        self.TAG_TYPE = tag_type
        validator: QValidator

        # configura a validação do QLineEdit
        try:
            if tag_type == "int":
                if text.__contains__("velocidade do robô"):
                    regex = QRegExp(r"^[0-9][0-9]?$|^100$")
                else:
                    regex = QRegExp(r"\d{5}")
            elif tag_type == "float":
                regex = QRegExp(r"[0-9][0-9]?[0-9]?[0-9]?\.?[0-9][0-9]?")
            elif tag_type == "string":
                regex = QRegExp(r"[\w\S]*")
            else:
                raise Exception("Nenhum tipo definido - dialogs/altera_valor.py show()")
            validator = QRegExpValidator(regex)
            self.ui.new_value.setValidator(validator)
        except Exception as e:
            print(e)
        # mostra o texto no dialog
        self.ui.description_text.setText(text)
        # define a thread que será executada
        self.thread = Thread_LineEdit(self.TAG_INDEX, self, self.ui.new_value, self.TAG_TYPE)

        self.set_button()
        self.exec_()
    ###################################################################################################
    def change_value(self):
        """Executada quando o botão é clicado, essa função inicia a thread caso haja texto escrito no QLineEdit"""
        try:
            if self.ui.new_value.text():
                self.thread.start()
            else:
                raise Exception("Campo vazio")
        except Exception as e:
            print(f"{e} - change_value - AlteraValorDialog")
    ###################################################################################################
    def set_button(self):
        """Define os botões do dialog"""
        self.ui.btn_alt_val.clicked.connect(self.change_value)
#######################################################################################################

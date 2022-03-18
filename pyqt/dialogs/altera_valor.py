"""Dialog for change the value of some tags"""

from PyQt5.QtWidgets import QDialog
from PyQt5.QtCore import QRegExp, Qt
from PyQt5.QtGui import QRegExpValidator

from ui_py.ui_alt_val_dialog import Ui_Dialog2
from utils.Types import TagTypes
from utils.workers.write_thread import Thread_LineEdit


class AlteraValorDialog(QDialog):
    """
    Dialog to change a value of some tag
    """
    def __init__(self, parents=None):
        super(AlteraValorDialog, self).__init__(parents)
        self.setWindowFlag(Qt.WindowContextHelpButtonHint, False)
        self.ui = Ui_Dialog2()
        self.ui.setupUi(self)

        self.TAG_INDEX: str = ""
        self.TAG_TYPE: TagTypes = ""

        self.thread: Thread_LineEdit

    def closeEvent(self, event):
        """Activated when the Dialog is closed"""
        self.ui.new_value.clear()

    def show_dialog(self, text: str, tag: str, tag_type: TagTypes = "string"):
        """
        Pop up the dialog in the screen

        Params:
            text = what will be showed in the dialog
            tag = the PLC tag that the value of LineEdit will change
            tag_type = the value's type that will be sent to the PLC
        """
        self.TAG_INDEX = tag
        self.TAG_TYPE = tag_type
        validator: QValidator
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
        self.ui.description_text.setText(text)

        self.thread = Thread_LineEdit(self.TAG_INDEX, self, self.ui.new_value, self.TAG_TYPE)
        self.set_button()
        self.exec_()

    def change_value(self):
        try:
            if self.ui.new_value.text():
                self.thread.start()
            else:
                raise Exception("Campo vazio")
        except Exception as e:
            print(f"{e} - change_value - AlteraValorDialog")

    def set_button(self):
        """Set the button of the dialog"""
        self.ui.btn_alt_val.clicked.connect(self.change_value)

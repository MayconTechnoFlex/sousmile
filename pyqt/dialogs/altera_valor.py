from PyQt5.QtWidgets import QDialog
from PyQt5.QtCore import QRegExp
from PyQt5.QtGui import QRegExpValidator
from pyqt.ui_py.ui_alt_val_dialog import Ui_Dialog2

from pyqt.utils.Types import TagTypes
from pyqt.utils.gui_functions import write_LineEdit


class AlteraValorDialog:
    def __init__(self):
        super(AlteraValorDialog, self).__init__()

        self.dialog = QDialog()
        self.ui = Ui_Dialog2()
        self.ui.setupUi(self.dialog)

        self.TAG_INDEX: str = ""
        self.TAG_TYPE: TagTypes = ""

        self.set_button()

    def show(self, text: str, tag: str, tag_type: TagTypes = "string"):
        self.TAG_INDEX = tag
        self.TAG_TYPE = tag_type
        validator: QValidator
        try:
            if tag_type == "int":
                if text.__contains__("velocidade do robô"):
                    regex = QRegExp(r"^[0-9][0-9]?$|^100$")
                else:
                    regex = QRegExp(r"\d{5}")
                validator = QRegExpValidator(regex)
            elif tag_type == "float":
                regex = QRegExp(r"[0-9][0-9]?[0-9]?[0-9]?\.?[0-9][0-9]?")
                validator = QRegExpValidator(regex)
            elif tag_type == "string":
                regex = QRegExp(r"[\w\S]*")
                validator = QRegExpValidator(regex)
            else:
                raise Exception("Nenhum tipo definido - dialogs/altera_valor.py show()")
            self.ui.new_value.setValidator(validator)
        except Exception as e:
            print(e)
        self.ui.description_text.setText(text)
        self.dialog.exec_()

    def setWindowIcon(self, Icon):
        self.dialog.setWindowIcon(Icon)

    def set_button(self):
        self.ui.btn_alt_val.clicked.connect(
            lambda: write_LineEdit(self.TAG_INDEX, self.dialog,
                                   self.ui.new_value, self.TAG_TYPE)
        )

from PyQt5.QtCore import QRegExp, Qt
from PyQt5.QtGui import QRegExpValidator
from PyQt5.QtWidgets import QDialog
from pyqt.ui_py.ui_cod_dialog_win import Ui_Dialog

from pyqt.utils.gui_functions import write_LineEdit
from pyqt.utils.Types import TagTypes

class InsertCodeDialog(QDialog):
    def __init__(self, parents=None):
        super(InsertCodeDialog, self).__init__(parents)
        self.setWindowFlag(Qt.WindowContextHelpButtonHint, False)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.TAG_INDEX: str = ""
        self.TAG_TYPE: TagTypes = ""

        regex = QRegExp(r"[\w\S]*")
        self.validator = QRegExpValidator(regex)

        self.insert_button()

    def closeEvent(self, event) -> None:
        self.ui.txt_code.clear()

    def show_dialog(self, tag: str, tag_type: TagTypes):
        self.TAG_INDEX = tag
        self.TAG_TYPE = tag_type
        self.ui.txt_code.setValidator(self.validator)
        self.exec_()

    def insert_button(self):
        self.ui.btn_insert_code_man.clicked.connect(
            lambda: write_LineEdit(self.TAG_INDEX, self,
                                   self.ui.txt_code, self.TAG_TYPE)
        )

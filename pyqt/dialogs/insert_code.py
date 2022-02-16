from PyQt5.QtWidgets import QDialog
from ui_py.ui_cod_dialog_win import Ui_Dialog

from utils.gui_functions import write_QlineEdit
from utils.Types import TagTypes


class InsertCodeDialog:
    def __init__(self):
        super(InsertCodeDialog, self).__init__()

        self.dialog = QDialog()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self.dialog)

        self.TAG_INDEX: str = ""
        self.TAG_TYPE: TagTypes = ""

        self.insert_button()

    def setWindowIcon(self, Icon):
        self.dialog.setWindowIcon(Icon)

    def show(self, tag: str, tag_type: TagTypes):
        self.TAG_INDEX = tag
        self.TAG_TYPE = tag_type
        self.dialog.exec_()

    def insert_button(self):
        self.ui.btn_insert_code_man.clicked.connect(
            lambda: write_QlineEdit(self.TAG_INDEX, self.dialog,
                                    self.ui.txt_code, self.TAG_TYPE)
        )

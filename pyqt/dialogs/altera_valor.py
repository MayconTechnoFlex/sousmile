from PyQt5.QtWidgets import QDialog
from pyqt.ui_py.ui_alt_val_dialog import Ui_Dialog2

from pyqt.utils.Types import TagTypes
from pyqt.utils.gui_functions import write_QlineEdit

class AlteraValorDialog:
    def __init__(self):
        super(AlteraValorDialog, self).__init__()

        self.dialog = QDialog()
        self.ui = Ui_Dialog2()
        self.ui.setupUi(self.dialog)

        self.TAG_INDEX: str = ""
        self.TAG_TYPE: TagTypes = ""

        self.set_button()

    def show(self, text: str, tag: str, tag_type: TagTypes):
        self.TAG_INDEX = tag
        self.TAG_TYPE = tag_type
        self.ui.description_text.setText(text)
        self.dialog.exec_()

    def setWindowIcon(self, Icon):
        self.dialog.setWindowIcon(Icon)

    def set_button(self):
        self.ui.btn_alt_val.clicked.connect(
            lambda: write_QlineEdit(self.TAG_INDEX, self.dialog,
                                    self.ui.new_value, self.TAG_TYPE)
        )

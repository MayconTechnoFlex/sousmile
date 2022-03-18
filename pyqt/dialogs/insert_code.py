"""Dialog for insert code manually in the HomeScreen"""

from PyQt5.QtCore import QRegExp, Qt
from PyQt5.QtGui import QRegExpValidator
from PyQt5.QtWidgets import QDialog

from ui_py.ui_gui_final import Ui_MainWindow

from ui_py.ui_cod_dialog_win import Ui_Dialog
from utils.write_thread import Thread_LineEdit
from utils.Types import TagTypes


class InsertCodeDialog(QDialog):
    """
    Dialog for insert code manually in the HomeScreen
    """
    def __init__(self, parents=None):
        super(InsertCodeDialog, self).__init__(parents)
        self.setWindowFlag(Qt.WindowContextHelpButtonHint, False)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.TAG_INDEX: str = ""
        self.TAG_TYPE: TagTypes = ""

        regex = QRegExp(r"[\w\S]*")
        self.validator = QRegExpValidator(regex)

        self.thread: Thread_LineEdit

    def closeEvent(self, event) -> None:
        """Activated when the Dialog is closed"""
        self.ui.txt_code.clear()

    def show_dialog(self, tag: str, tag_type: TagTypes, ui_main: Ui_MainWindow, side):
        """
        Pop up the dialog in the screen

        Params:
            tag: the PLC tag that the value of LineEdit will change
            tag_type = the value's type that will be sent to the PLC
        """
        self.TAG_INDEX = tag
        self.TAG_TYPE = tag_type
        self.ui.txt_code.setValidator(self.validator)
        self.thread = Thread_LineEdit(self.TAG_INDEX, self, self.ui.txt_code, self.TAG_TYPE)
        self.ui_main = ui_main
        self.side = side
        self.set_button()
        self.exec_()

    def insert_code(self):
        try:
            if self.ui.txt_code.text():
                # self.thread.start()
                if self.side == "A1":
                    self.ui_main.lbl_ProdCode_A1.setText(self.ui.txt_code.text())
                elif self.side == "A2":
                    self.ui_main.lbl_ProdCode_A2.setText(self.ui.txt_code.text())
                elif self.side == "B1":
                    self.ui_main.lbl_ProdCode_B1.setText(self.ui.txt_code.text())
                elif self.side == "B2":
                    self.ui_main.lbl_ProdCode_B2.setText(self.ui.txt_code.text())

                self.close()
            else:
                raise Exception("Campo vazio")
        except Exception as e:
            print(f"{e} - insert_code - InsertCodeDialog")

    def set_button(self):
        """Set the button of the dialog"""
        self.ui.btn_insert_code_man.clicked.connect(self.insert_code)

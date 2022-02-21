from PyQt5.QtWidgets import QDialog
from PyQt5.QtCore import QRegExp, Qt
from PyQt5.QtGui import QRegExpValidator

from ui_py.ui_check_uf import Ui_Dialog
from utils.Types import TagTypes
from utils.gui_functions import write_LineEdit
from utils.ctrl_plc import write_tag

class CheckUserFrame(QDialog):
    def __init__(self, parents=None):
        super(CheckUserFrame, self).__init__(parents)
        self.setWindowFlag(Qt.WindowContextHelpButtonHint, False)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.set_button()

    def closeEvent(self, event):
        """Activated when the Dialog is closed"""
        self.ui.lineEdit.clear()
        self.ui.lineEdit.setFocus()

    def show_dialog(self):
        """
        Pop up the dialog in the screen
        """
        validator: QValidator
        try:
            regex = QRegExp(r"\d{2}")
            validator = QRegExpValidator(regex)
            self.ui.lineEdit.setValidator(validator)
        except Exception as e:
            print(e)
        self.exec_()

    def confirm_action(self):
        """Called when the "Confirmar" button is pressed"""
        try:
            write_tag("HMI.btnCheckUF", 1)
            write_LineEdit("Robo.Output.UFCheck", self, self.ui.lineEdit, "int")
        except Exception as e:
            print(e)

    def cancel_action(self):
        """Called when the "Cancelar" button is pressed"""
        self.close()
        print("Action canceled")

    def set_button(self):
        """Set the button of the dialog"""
        self.ui.btn_confirm.clicked.connect(self.confirm_action)
        self.ui.btn_cancel.clicked.connect(self.cancel_action)

from PyQt5.QtWidgets import QDialog
from PyQt5.QtCore import QRegExp, Qt, QThreadPool
from PyQt5.QtGui import QRegExpValidator

from ui_py.ui_check_uf import Ui_Dialog
from utils.write_thread import Thread_LineEdit
from utils.workers import Worker_ToggleBtnValue

class CheckUserFrame(QDialog):
    def __init__(self, parents=None):
        super(CheckUserFrame, self).__init__(parents)
        self.setWindowFlag(Qt.WindowContextHelpButtonHint, False)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.thread: Thread_LineEdit
        self.worker_check: Worker_ToggleBtnValue
        self.worker_thread = QThreadPool()

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

        self.thread = Thread_LineEdit("Robo.Output.UFCheck", self, self.ui.lineEdit, "int")
        self.worker_check = Worker_ToggleBtnValue("HMI.btnCheckUF", 0, self.ui.btn_confirm)
        self.set_button()
        self.exec_()

    def confirm_action(self):
        """Called when the "Confirmar" button is pressed"""
        try:
            if self.ui.lineEdit.text():
                self.thread.start()
                self.worker_thread.start(self.worker_check)
            else:
                raise Exception("Campo vazio")
        except Exception as e:
            print(f"{e} - confirm_action - CheckUF")
        finally:
            self.close()

    def cancel_action(self):
        """Called when the "Cancelar" button is pressed"""
        self.close()

    def set_button(self):
        """Set the button of the dialog"""
        self.ui.btn_confirm.clicked.connect(self.confirm_action)
        self.ui.btn_cancel.clicked.connect(self.cancel_action)

"""Dialog para chegar a UserFrame"""
#######################################################################################################
# Importações
#######################################################################################################
from PyQt5.QtWidgets import QDialog
from PyQt5.QtCore import QRegExp, Qt, QThreadPool
from PyQt5.QtGui import QRegExpValidator

from ui_py.ui_check_uf_dialog import Ui_Dialog
from utils.workers.write_thread import Thread_LineEdit
from utils.workers.workers import Worker_ToggleBtnValue, Worker_WriteTags
#######################################################################################################

class CheckUF(QDialog):
    """Dialog para chegar a UserFrame"""

    def __init__(self, parents=None):
        super(CheckUF, self).__init__(parents)
        self.setWindowFlag(Qt.WindowContextHelpButtonHint, False)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.set_button()

        # definições iniciais
        self.thread: Thread_LineEdit
        self.worker: Worker_WriteTags
        self.worker_check: Worker_ToggleBtnValue
        self.worker_thread1 = QThreadPool()
        self.worker_thread2 = QThreadPool()
    ###################################################################################################
    def closeEvent(self, event):
        """Ativado quando o dialog é fechado, apaga os QLineEdit"""
        self.ui.uf_num.clear()
        self.ui.uf_num.clear()
        self.ui.offset_num.setFocus()
        self.ui.offset_num.setFocus()
    ###################################################################################################
    def show_dialog(self):
        """Mostra o dialog na tela"""
        validator: QValidator
        try:
            uf_num_regex = QRegExp(r"^[1-4]$")
            uf_num_validator = QRegExpValidator(uf_num_regex)
            self.ui.uf_num.setValidator(uf_num_validator)

            offset_num_regex = QRegExp(r"^\d{1,5}$")
            offset_num_validator = QRegExpValidator(offset_num_regex)
            self.ui.offset_num.setValidator(offset_num_validator)
        except Exception as e:
            print(e)

        self.thread = Thread_LineEdit("Robo.Output.UFCheck", self, self.ui.uf_num, "int")
        # self.worker_check = Worker_ToggleBtnValue("HMI.btnCheckUF", 0, self.ui.btn_confirm)
        self.exec_()
    ###################################################################################################
    def confirm_action(self):
        """Chamado quando o botão Confirmar é clicado"""
        try:
            if self.ui.uf_num.text() and self.ui.offset_num.text():
                self.worker = Worker_WriteTags("Robo.Output.UFCheckOffset", int(self.ui.offset_num.text()))
                self.thread.start()
                self.worker_thread1.start(self.worker)
                # self.worker_thread2.start(self.worker_check)
            else:
                raise Exception("Campo vazio")
        except Exception as e:
            print(f"{e} - confirm_action - CheckUF")
        finally:
            self.close()
    ###################################################################################################
    def set_button(self):
        """Define os botões do dialog"""
        self.ui.btn_confirm.clicked.connect(self.confirm_action)
        self.ui.btn_cancel.clicked.connect(self.close)
#######################################################################################################

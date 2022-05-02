"""Dialog para inserir o código manualmente na tela Home"""
#######################################################################################################
# Importações
#######################################################################################################
from typing import Literal

from PyQt5.Qt import QValidator
from PyQt5.QtCore import QRegExp, Qt, QThreadPool
from PyQt5.QtGui import QRegExpValidator
from PyQt5.QtWidgets import QDialog

from ui_py.ui_gui_final import Ui_MainWindow

from ui_py.ajuste_fresa_ui import Ui_Dialog
from utils.workers.workers import Worker_WriteTags, Worker_ToggleBtnValue
from utils.functions.ctrl_plc import read_tags

from threading import Thread
#######################################################################################################

class AjusteFrasaDialog(QDialog):
    """Dialog para inserir o código manualmente na tela Home"""

    def __init__(self, parents=None):
        super(AjusteFrasaDialog, self).__init__(parents)
        self.setWindowFlag(Qt.WindowContextHelpButtonHint, False)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.thread = QThreadPool()
        self.thread2 = QThreadPool()

        self.ui.btn_confirm.clicked.connect(self.insert_code)
        self.ui.btn_cancel.clicked.connect(self.close)

        self.set_validators()
    ###################################################################################################
    def closeEvent(self, event) -> None:
        """Ativado quando o dialog é fechado"""
        self.ui.le_code.clear()
    ###################################################################################################
    def set_validators(self):
        regex = QRegExp(r"[0-9]\.?[0-9]")
        validator = QRegExpValidator(regex)
        self.ui.le_code.setValidator(validator)
    ###################################################################################################
    def actual_value(self):
        value = read_tags("Robo.Output.MillingCutSize")
        self.ui.valor_atual.setText(str(value))
    ###################################################################################################
    def show_dialog(self):
        """
        Mostra o dialog na tela

        :param ui_main: Ui da tela principal
        :param side: Lado que receberá o código
        """
        self.py_thread = Thread(target=self.actual_value)
        self.py_thread.start()
        self.ui.le_code.setFocus()
        self.exec_()
    ###################################################################################################
    def insert_code(self):
        try:
            if self.ui.le_code.text():
                code = self.change_float()
                worker = Worker_WriteTags("Robo.Output.MillingCutSize", code)
                self.thread.start(worker)
                worker2 = Worker_ToggleBtnValue("HMI.btn_AdjustUTOOL", 0, self.ui.btn_confirm)
                self.thread2.start(worker2)

                self.close()
            else:
                raise Exception("Campo vazio")
        except Exception as e:
            print(f"{e} - insert_code - InsertCodeDialog")
    def change_float(self):
        if self.ui.le_code.text():
            txt = self.ui.le_code.text()
            if txt.find(",") == -1:
                value = float(txt)
            else:
                new_txt = txt.replace(",", ".")
                value = float(new_txt)
            return value
#######################################################################################################

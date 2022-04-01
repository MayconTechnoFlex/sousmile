"""Dialog para inserir o código manualmente na tela Home"""
#######################################################################################################
# Importações
#######################################################################################################
from typing import Literal

from PyQt5.Qt import QValidator
from PyQt5.QtCore import QRegExp, Qt
from PyQt5.QtGui import QRegExpValidator
from PyQt5.QtWidgets import QDialog

from ui_py.ui_gui_final import Ui_MainWindow

from ui_py.ui_cod_dialog_win import Ui_Dialog
from utils.Types import TagTypes
#######################################################################################################

class InsertCodeDialog(QDialog):
    """Dialog para inserir o código manualmente na tela Home"""

    def __init__(self, parents=None):
        super(InsertCodeDialog, self).__init__(parents)
        self.setWindowFlag(Qt.WindowContextHelpButtonHint, False)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.ui.btn_insert_code_man.clicked.connect(self.insert_code)

        self.set_validators()
    ###################################################################################################
    def closeEvent(self, event) -> None:
        """Ativado quando o dialog é fechado"""
        self.ui.le_etapa.clear()
        self.ui.le_code.clear()
        self.ui.le_pos.clear()
        self.ui.lbl_info.clear()
    ###################################################################################################
    def set_validators(self):
        regex_etapa = QRegExp(r"^(c?)$|^([1-99]?[0-99]?)$")
        regex_code = QRegExp(r"^[A-Z]{0,4}$|^[a-z]{0,4}$")
        regex_pos = QRegExp(r"^[A-Z]{0,1}$|^[a-z]{0,1}$")
        etapa_validator = QRegExpValidator(regex_etapa)
        code_validator = QRegExpValidator(regex_code)
        pos_validator = QRegExpValidator(regex_pos)

        self.ui.le_etapa.setValidator(etapa_validator)
        self.ui.le_code.setValidator(code_validator)
        self.ui.le_pos.setValidator(pos_validator)
    ###################################################################################################
    def show_dialog(self, ui_main: Ui_MainWindow, side: Literal["A1", "A2", "B1", "B2"]):
        """
        Mostra o dialog na tela

        :param ui_main: Ui da tela principal
        :param side: Lado que receberá o código
        """
        self.ui_main = ui_main
        self.side = side
        self.ui.le_etapa.setFocus()
        self.exec_()
    ###################################################################################################
    def insert_code(self):
        try:
            codigo = self.ui.le_code.text()
            etapa = self.ui.le_etapa.text()
            pos = self.ui.le_pos.text()
            if etapa and codigo and pos:
                code = f"{etapa}_{codigo}_{pos}"
                if self.side == "A1":
                    self.ui_main.lbl_ProdCode_A1.setText(code)
                elif self.side == "A2":
                    self.ui_main.lbl_ProdCode_A2.setText(code)
                elif self.side == "B1":
                    self.ui_main.lbl_ProdCode_B1.setText(code)
                elif self.side == "B2":
                    self.ui_main.lbl_ProdCode_B2.setText(code)
                self.close()
            else:
                self.ui.lbl_info.setText("Estão faltando informações para formar o código completo!")
        except Exception as e:
            print(f"{e} - insert_code - InsertCodeDialog")
#######################################################################################################

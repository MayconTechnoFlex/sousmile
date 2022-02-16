from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QDialog
from pyqt.ui_py.confirm_dialog_ui import Ui_ConfirmDialog

from pyqt.utils.Types import *

class ConfirmationDialog(QDialog):
    def __init__(self, parents=None):
        super(ConfirmationDialog, self).__init__(parents)
        self.setWindowFlag(Qt.WindowContextHelpButtonHint, False)
        self.ui = Ui_ConfirmDialog()
        self.ui.setupUi(self)

        self.ACTION_TO_CONFIRM: ActionsToConfirm = ""

        self.buttons_of_dialog()

    def show_dialog(self, action_to_confirm: ActionsToConfirm, text: str = ""):
        self.ACTION_TO_CONFIRM = action_to_confirm
        if text:
            self.ui.description_text.setText(text)
        self.exec_()

    def closeEvent(self, event):
        self.cancel_action()

    def confirm_action(self):
        action = self.ACTION_TO_CONFIRM
        try:
            if action == "MoveHome":
                # escreve a tag referente para cada ação
                # write_tag("", 1)
                print(f"{action} realized")
            elif action == "":
                raise Exception("Nenhuma ação foi passada")
        except Exception as e:
            print(f"{e} - Erro na ação")
        finally:
            self.close()

    def cancel_action(self):
        self.ACTION_TO_CONFIRM = ""
        self.close()
        print("Action canceled")

    def buttons_of_dialog(self):
        self.ui.btn_confirm.clicked.connect(self.confirm_action)
        self.ui.btn_cancel.clicked.connect(self.cancel_action)

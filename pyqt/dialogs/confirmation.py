from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QDialog
from pyqt.main import Ui_ConfirmDialog

from pyqt.utils.Types import *

class ConfirmationDialog:
    def __init__(self):
        super(ConfirmationDialog, self).__init__()

        self.dialog = QDialog()
        self.ui = Ui_ConfirmDialog()
        self.ui.setupUi(self.dialog)

        self.ACTION_TO_CONFIRM: ActionsToConfirm = ""

        self.buttons_of_dialog()

    def setWindowIcon(self, Icon):
        self.dialog.setWindowIcon(Icon)

    def show_confirm_dialog(self, action_to_confirm: ActionsToConfirm, text: str = ""):
        self.ACTION_TO_CONFIRM = action_to_confirm
        if text:
            self.ui.description_text.setText(text)
        self.dialog.exec_()

    def confirm_action(self):
        action = self.ACTION_TO_CONFIRM
        try:
            if action == "MoveHome":
                # escreve a tag referente para cada ação
                # write_tag("", 1)
                pass
            elif action == "":
                raise Exception("Nenhuma ação foi passada")
        except Exception as e:
            print(f"{e} - Erro na ação")
        finally:
            self.dialog.close()

    def cancel_action(self):
        self.ACTION_TO_CONFIRM = ""
        self.dialog.close()

    def buttons_of_dialog(self):
        self.ui.btn_confirm.clicked.connect(self.confirm_action)
        self.ui.btn_cancel.clicked.connect(self.cancel_action)

"""Dialog for confirm or cancel an action"""

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QDialog

from ui_py.confirm_dialog_ui import Ui_ConfirmDialog
from utils.Types import ActionsToConfirm
from utils.write_thread import Thread_Dialogs_NoLineEdit
from utils.ctrl_plc import write_tag

class ConfirmationDialog(QDialog):
    """
    Dialog for confirme or cancel a determined action
    """
    def __init__(self, parents=None):
        super(ConfirmationDialog, self).__init__(parents)
        self.setWindowFlag(Qt.WindowContextHelpButtonHint, False)
        self.ui = Ui_ConfirmDialog()
        self.ui.setupUi(self)

        self.ACTION_TO_CONFIRM: ActionsToConfirm = ""

        self.thread: Thread_Dialogs_NoLineEdit

    def show_dialog(self, action_to_confirm: ActionsToConfirm, text: str = ""):
        """
        Pop up the Dialog in the screen

        Params:
            action_to_confirm = the action that is waiting to confirm
            text = what will be showed in the dialog
        """
        self.ACTION_TO_CONFIRM = action_to_confirm
        if text:
            self.ui.description_text.setText(text)
        self.buttons_of_dialog()
        self.exec_()

    def closeEvent(self, event):
        """Activated when the Dialog is closed"""
        self.cancel_action()

    def confirm_action(self):
        """Called when the "Confirmar" button is pressed"""
        action = self.ACTION_TO_CONFIRM
        try:
            if action == "MoveHome":
                self.thread = Thread_Dialogs_NoLineEdit(self, "HMI.btnGoHome")
                self.thread.start()
            elif action == "":
                raise Exception("Nenhuma ação foi passada")
        except Exception as e:
            print(f"{e} - Erro na ação")
            self.dialog.cancel_action()

    def cancel_action(self):
        """Called when the "Cancelar" button is pressed"""
        self.ACTION_TO_CONFIRM = ""
        self.close()

    def buttons_of_dialog(self):
        """Set the buttons of the dialog"""
        self.ui.btn_confirm.clicked.connect(self.confirm_action)
        self.ui.btn_cancel.clicked.connect(self.cancel_action)

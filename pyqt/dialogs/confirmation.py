"""Dialog para confirmar ou negar determinada ação"""
#######################################################################################################
# Importações
#######################################################################################################
from PyQt5.QtCore import Qt, QThreadPool
from PyQt5.QtWidgets import QDialog

from ui_py.confirm_dialog_ui import Ui_ConfirmDialog
from utils.Types import ActionsToConfirm
from utils.workers.write_thread import Thread_Dialogs_NoLineEdit
from utils.workers.workers import Worker_ToggleBtnValue
#######################################################################################################

class ConfirmationDialog(QDialog):
    """Dialog para confirmar ou negar determinada ação"""

    def __init__(self, parents=None):
        super(ConfirmationDialog, self).__init__(parents)
        self.setWindowFlag(Qt.WindowContextHelpButtonHint, False)
        self.ui = Ui_ConfirmDialog()
        self.ui.setupUi(self)

        self.ACTION_TO_CONFIRM: ActionsToConfirm = ""

        self.thread = QThreadPool()
        self.worker: Worker_ToggleBtnValue
        self.thread_dialog: Thread_Dialogs_NoLineEdit
    ###################################################################################################
    def show_dialog(self, action_to_confirm: ActionsToConfirm, text: str = ""):
        """
        Mostra o dialog na tela

        :param action_to_confirm: A ação que é para ser confirmada
        :param text: Texto que será mostrado no dialog
        """
        self.ACTION_TO_CONFIRM = action_to_confirm
        if text:
            self.ui.description_text.setText(text)
        self.buttons_of_dialog()
        if action_to_confirm == "MoveHome":
            self.worker = Worker_ToggleBtnValue("HMI.btnGoHome", 0, self.ui.btn_confirm)
        elif action_to_confirm == "CheckUTOOL":
            self.worker = Worker_ToggleBtnValue("HMI.btn_AdjustUTOOL", 0, self.ui.btn_confirm)
        elif action_to_confirm == "ChangeTool":
            self.worker = Worker_ToggleBtnValue("HMI.btn_ChangeTool", 0, self.ui.btn_confirm)
        elif action_to_confirm == "":
            raise Exception("Nenhuma ação foi passada para confirmação")
        self.exec_()
    ###################################################################################################
    def closeEvent(self, event):
        """Activado quando o dialog é fechado"""
        self.cancel_action()
    ###################################################################################################
    def confirm_action(self):
        """Chamado quando o botão Confirmar for clicado"""
        action = self.ACTION_TO_CONFIRM
        try:
            if action:
                self.thread.start(self.worker)
            else:
                raise Exception("Nenhuma ação foi passada")
        except Exception as e:
            print(f"{e} - Erro na ação")
        finally:
            self.close()
    ###################################################################################################
    def cancel_action(self):
        """Chamado quando o botão Cancelar for clicado"""
        self.ACTION_TO_CONFIRM = ""
        self.close()
    ###################################################################################################
    def buttons_of_dialog(self):
        """Define os botões da tela"""
        self.ui.btn_confirm.clicked.connect(self.confirm_action)
        self.ui.btn_cancel.clicked.connect(self.cancel_action)
#######################################################################################################

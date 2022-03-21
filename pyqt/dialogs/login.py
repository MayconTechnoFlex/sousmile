"""Dialog para LogIn na aplicação"""
#######################################################################################################
# Importações
#######################################################################################################
import time

from PyQt5.QtCore import QRegExp, Qt
from PyQt5.QtGui import QRegExpValidator
from PyQt5.QtWidgets import QDialog, QLabel

from ui_py.ui_login_dialog import Ui_LoginDialog

from security.db_users import users_accounts as users
from security.db_users import set_connected_username, disconnect_user
#######################################################################################################

class LoginDialog(QDialog):
    """Dialog para LogIn na aplicação"""

    def __init__(self, parents=None):
        super(LoginDialog, self).__init__(parents)
        self.setWindowFlag(Qt.WindowContextHelpButtonHint, False)
        self.ui = Ui_LoginDialog()
        self.ui.setupUi(self)

        self.set_button()
        self.lbl_username: QLabel = QLabel()

        regex = QRegExp(r"[\w\S]*")
        self.validator = QRegExpValidator(regex)
    ###################################################################################################
    def closeEvent(self, event):
        """Ativado quando o dialog é fechado"""
        self.clear_labels()
    ###################################################################################################
    def show_dialog(self, lbl_username: QLabel):
        """
        Mostra o dialog na tela

        :param lbl_username: Label do Nome do Usuário na barra lateral
        """
        self.lbl_username = lbl_username
        self.ui.lbl_login_staus.setText('Insira o usuário e a senha para o login')
        self.ui.user_login.setValidator(self.validator)
        self.ui.user_password.setValidator(self.validator)
        self.exec_()
    ###################################################################################################
    def set_button(self):
        """Define os botões do dialog"""
        self.ui.btn_login.clicked.connect(self.login_user)
    ###################################################################################################
    def clear_labels(self):
        """Limpa todos os Labels e define o foco para o primeiro"""
        self.ui.user_login.clear()
        self.ui.user_login.setFocus()
        self.ui.user_password.clear()
    ###################################################################################################
    def login_user(self):
        """Chamado quando o botão de login é pressionado"""
        user = self.ui.user_login.text()
        password = self.ui.user_password.text()
        login_successful = False
        items = users.items()
        # verifica se o Usuário e a Senha combinam e loga o usuário
        for key, value in items:
            if key == user and value == password:
                self.ui.lbl_login_staus.setText('Login efetuado com sucesso')
                set_connected_username(user)
                self.lbl_username.setText(user)
                login_successful = True
                self.close()
                break
        if not login_successful:
            self.ui.lbl_login_staus.setText('Usuário ou senha incorreto')
        self.clear_labels()
    ###################################################################################################
    def logout_user(self):
        """Desconecta o usuário da aplicação"""
        disconnect_user()
        self.lbl_username.setText('Nenhum usuário logado')
#######################################################################################################

from PyQt5.QtCore import QRegExp
from PyQt5.QtGui import QRegExpValidator, QCloseEvent
from PyQt5.QtWidgets import QDialog, QLabel
from pyqt.ui_py.ui_login_dialog import Ui_LoginDialog

from pyqt.utils.db_users import users_accounts as users
from pyqt.utils.db_users import set_connected_username, disconnect_user

class LoginDialog:
    def __init__(self):
        super(LoginDialog, self).__init__()

        self.dialog = QDialog()
        self.ui = Ui_LoginDialog()
        self.ui.setupUi(self.dialog)

        self.set_button()
        self.lbl_username: QLabel = QLabel()

        regex = QRegExp(r"[\w\S]*")
        self.validator = QRegExpValidator(regex)

    def setWindowIcon(self, Icon):
        self.dialog.setWindowIcon(Icon)

    def closeEvent(self):
        self.clear_labels()

    def show(self, lbl_username: QLabel):
        self.lbl_username = lbl_username
        self.ui.lbl_login_staus.setText('Insira o usuário e a senha para o login')
        self.ui.user_login.setValidator(self.validator)
        self.ui.user_password.setValidator(self.validator)
        self.dialog.exec_()

    def set_button(self):
        self.ui.btn_login.clicked.connect(self.login_user)

    def clear_labels(self):
        self.ui.user_login.setText("")
        self.ui.user_login.setFocus()
        self.ui.user_password.setText("")

    def login_user(self):
        user = self.ui.user_login.text()
        password = self.ui.user_password.text()
        login_successful = False
        items = users.items()
        for key, value in items:
            if key == user and value == password:
                self.ui.lbl_login_staus.setText('Login efetuado com sucesso')
                set_connected_username(user)
                self.lbl_username.setText(user)
                login_successful = True
                self.dialog.close()
                break
        if not login_successful:
            self.ui.lbl_login_staus.setText('Usuário ou senha incorreto')
        self.clear_labels()

    def logout_user(self):
        disconnect_user()
        self.lbl_username.setText('Nenhum usuário logado')

"""Dialog for log-in a user"""

from PyQt5.QtCore import QRegExp, Qt, QThread
from PyQt5.QtGui import QRegExpValidator
from PyQt5.QtWidgets import QDialog, QLabel

from ui_py.ui_login_dialog import Ui_LoginDialog

from utils.db_users import users_accounts as users
from utils.db_users import set_connected_username, disconnect_user

class LoginDialog(QDialog):
    """
    Dialog for log in the application and enable some features depending of the user
    """
    def __init__(self, parents=None):
        super(LoginDialog, self).__init__(parents)
        self.setWindowFlag(Qt.WindowContextHelpButtonHint, False)
        self.ui = Ui_LoginDialog()
        self.ui.setupUi(self)

        self.set_button()
        self.lbl_username: QLabel = QLabel()

        regex = QRegExp(r"[\w\S]*")
        self.validator = QRegExpValidator(regex)

    def closeEvent(self, event):
        """Activated when the Dialog is closed"""
        self.clear_labels()

    def show_dialog(self, lbl_username: QLabel):
        """
        Pop up the dialog in the screen

        Params:
            lbl_username = the username label in the left tab bar in application
        """
        self.lbl_username = lbl_username
        self.ui.lbl_login_staus.setText('Insira o usuário e a senha para o login')
        self.ui.user_login.setValidator(self.validator)
        self.ui.user_password.setValidator(self.validator)
        self.exec_()

    def set_button(self):
        """Set the button of the dialog"""
        self.ui.btn_login.clicked.connect(self.login_user)

    def clear_labels(self):
        """Clear all labels and set focus on first one"""
        self.ui.user_login.clear()
        self.ui.user_login.setFocus()
        self.ui.user_password.clear()

    def login_user(self):
        """Called when the button is pressed, verify if the user and password
        is right and log-in it"""
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
                self.close()
                break
        if not login_successful:
            self.ui.lbl_login_staus.setText('Usuário ou senha incorreto')
        self.clear_labels()

    def logout_user(self):
        """Log-out the user when the button is pressed"""
        disconnect_user()
        self.lbl_username.setText('Nenhum usuário logado')



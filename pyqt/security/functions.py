"""Main functions of the security moduel"""

from ui_py.ui_gui_final import Ui_MainWindow
from security.db_users import users_list, get_connected_username

from security.permissions import *

def UpdateUserAccess(signal: bool, ui: Ui_MainWindow):
    try:
        user = get_connected_username()
        if user not in users_list:
            noneUserConnected(ui)
        elif user == "oper":
            operConnected(ui)
        elif user == "eng":
            engConnected(ui)
        elif user == "rn":
            rnConnected(ui)
    except Exception as e:
        print(f"{e} - security.functions")


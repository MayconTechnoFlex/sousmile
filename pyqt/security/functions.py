"""Principal função do módulo de segurança"""
#######################################################################################################
# Importações
#######################################################################################################
from ui_py.ui_gui_final import Ui_MainWindow
from security.db_users import users_list, get_connected_username

from security.permissions import *
#######################################################################################################
# Funções de Controle
#######################################################################################################
def UpdateUserAccess(signal: bool, main_ui: Ui_MainWindow):
    """
    Atualiza os locais em que o usuário pode logar, dependendo do seu nível de acesso

    :param signal: Sinal vindo do CLP (não utilizado)
    :param main_ui: Ui principal da aplicação
    """
    try:
        user = get_connected_username()
        if user not in users_list:
            noneUserConnected(main_ui)
        elif user == "oper":
            operConnected(main_ui)
        elif user == "eng":
            engConnected(main_ui)
        elif user == "rn":
            rnConnected(main_ui)
    except Exception as e:
        print(f"{e} - security.functions")
#######################################################################################################

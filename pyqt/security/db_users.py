"""Control of the user connected in the application"""

from typing import Union, List, Dict
from security.types import UsersName

users_accounts: Dict[UsersName, str] = {
    'oper': '12345',
    'eng': 'engenharia',
    'rn': 'rnrobotics'
}

users_list = list(users_accounts.keys())

connected_username: UsersName = "Nenhum usuário logado"


def set_connected_username(username: UsersName) -> None:
    """Writes the username in a module variable"""
    global connected_username
    connected_username = username


def disconnect_user() -> None:
    """Deletes the username in the module variable"""
    global connected_username
    connected_username = "Nenhum usuário logado"


def get_connected_username() -> UsersName:
    """Returns the username from the modules variable"""
    global connected_username
    if connected_username:
        return connected_username
    else:
        return "Nenhum usuário logado"

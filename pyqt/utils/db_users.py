"""Control of the user connected in the application"""

from utils.Types import UsersName, UsersAccounts

users_accounts: UsersAccounts = {
    'oper': '12345',
    'eng': 'engenharia',
    'rn': 'rnrobotics'
}

connected_username: UsersName = ""

def set_connected_username(username: UsersName) -> None:
    """Writes the username in a module variable"""
    global connected_username
    connected_username = username

def disconnect_user() -> None:
    """Deletes the username in a module variable"""
    global connected_username
    connected_username = ""

def get_connected_username() -> str:
    """Returns the username from the modules variable"""
    return connected_username

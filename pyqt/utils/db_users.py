from pyqt.utils.Types import UsersName
users_accounts: dict[UsersName, str] = {
    'oper': '12345',
    'eng': 'engenharia',
    'rn': 'rnrobotics'
}

connected_username: UsersName = ""

def set_connected_username(username: UsersName):
    global connected_username
    connected_username = username

def disconnect_user():
    global connected_username
    connected_username = ""

def get_connected_username():
    return connected_username

users_accounts = {
    'oper': '12345',
    'eng': 'engenharia',
    'rn': 'rnrobotics'
}

connected_username: str = ""

def set_connected_username(username: str):
    global connected_username
    connected_username = username

def get_connected_username():
    return connected_username

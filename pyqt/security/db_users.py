"""Controla o Usuário conectado na aplicação"""
#######################################################################################################
# Importações
#######################################################################################################
from typing import Dict
from security.types import UsersName
#######################################################################################################
# Definição das variáveis globais
#######################################################################################################
users_accounts: Dict[UsersName, str] = {
    'oper': '12345',
    'eng': 'engenharia',
    'rn': 'rnrobotics'
}
users_list = list(users_accounts.keys())
connected_username: UsersName = "Nenhum usuário logado"
#######################################################################################################
# Funções de Controle
#######################################################################################################
def set_connected_username(username: UsersName) -> None:
    """Escreve o Nome do Usuário na variável do módulo"""
    global connected_username
    connected_username = username
#######################################################################################################
def disconnect_user() -> None:
    """Deleta o Nome do Usuário na variável do módulo"""
    global connected_username
    connected_username = "Nenhum usuário logado"
#######################################################################################################
def get_connected_username() -> UsersName:
    """Retorna o Nome do Usuário na variável do módulo

    :return: Nome do usuário conectado
    """
    global connected_username
    if connected_username:
        return connected_username
    else:
        return "Nenhum usuário logado"
#######################################################################################################

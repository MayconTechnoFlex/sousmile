"""Módulo para controle da Porta do Leitor de Código de Barras"""
#######################################################################################################
# Importações
#######################################################################################################
import serial
from typing import List
#######################################################################################################
# Definição das variáveis globais
#######################################################################################################
PORT = ""
#######################################################################################################
# Funções de Controle
#######################################################################################################
def get_serial_ports() -> List[str]:
    """
    Lista de portas seriais

    :return: Lista das portas seriais disponíveis
    """
    ports = ['COM%s' % (i + 1) for i in range(256)]

    result = []
    for port in ports:
        try:
            s = serial.Serial(port)
            s.close()
            result.append(port)
            print(f"{port} é uma porta serial válida!")
        except Exception as e:
            pass
    return result
#######################################################################################################
def set_my_port(port: str):
    """
    Define a porta na variável do módulo

    :param port: String da Porta
    """
    global PORT
    PORT = port
#######################################################################################################
def get_my_port() -> str:
    """
    Retorna a porta da variável do módulo

    :return: String da Porta
    """
    global PORT
    return PORT
#######################################################################################################
# Verifica se há apenas uma porta e já configura ela
#######################################################################################################
if len(get_serial_ports()) == 1:
    set_my_port(get_serial_ports()[0])
#######################################################################################################

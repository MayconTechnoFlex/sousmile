"""Controle das funções de Escrita e Leitura do CLP"""
#######################################################################################################
# Importações
#######################################################################################################
from pycomm3 import LogixDriver, Tag
from typing import Union, List, Tuple
from utils.Types import PLCReturn
#######################################################################################################
# Define o IP
#######################################################################################################
IP = '192.168.1.10'
#######################################################################################################
# Tags de Escrita
#######################################################################################################
def read_tags(tag_name: str) -> PLCReturn:
    """
    Lê a tag do CLP e retorna o seu valor

    Se algo da errado, retorna e printa o erro

    :param tag_name: Tag a ser lida
    :return: Valor da tag lida OU erro
    """
    try:
        with LogixDriver(IP) as plc:
            return plc.read(tag_name).value
    except Exception as e:
        print(f"{e} - Error on plc communication")
        return e
#######################################################################################################
def read_multiples(tag_list: List[str]) -> Union[List[Tag], Exception]:
    """
    Lê várias tags do CLP e retorna elas

    Se algo da errado, retorna e printa o erro

    :param tag_list: Lista de Tags a serem lidas
    :return: Tags lidas OU erro
    """
    try:
        with LogixDriver(IP) as plc:
            return plc.read(*tag_list)
    except Exception as e:
        print(f"{e} - Error on plc communication")
        return e
#######################################################################################################
# Tags de Escrita
#######################################################################################################
def write_tag(tag_name: str, value: Union[str, int, float]) -> Union[None, Exception]:
    """
    Escreve um valor na tag do CLP

    Se algo da errado, retorna e printa o erro

    :param tag_name: Tag a ser mudada
    :param value: Valor a ser escrito na tag
    :return: Erro ou Nada
    """
    try:
        with LogixDriver(IP) as plc:
            plc.write((tag_name, value))
    except Exception as e:
        print(f"{e} - Error on plc communication")
        return e
#######################################################################################################
def write_multiples(*tags: Tuple[str, Union[str, float, int, bool]]) -> Union[None, Exception]:
    """
    Escreve valores em várias tags do CLP

    Se algo da errado, retorna e printa o erro

    :param tags: Tupla com o Nome da Tag e seu Valor a ser escrito
    :return: Erro ou Nada
    """
    try:
        with LogixDriver(IP) as plc:
            plc.write(*tags)
    except Exception as e:
        print(f"{e} - Error on plc communication")
        return e
#######################################################################################################

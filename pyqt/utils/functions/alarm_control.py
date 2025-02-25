"""Controle da Lista de Alarmes"""
#######################################################################################################
# Importações
#######################################################################################################
from typing import List

from utils.Types import AlarmDict
#######################################################################################################
# Definição das variáveis globais
#######################################################################################################
alarm_message_list = ["Alarme 00: Botão de Emergência Pressionado", "Alarme 01:", "Alarme 02:", "Alarme 03:",
                      "Alarme 04:", "Alarme 05:", "Alarme 06: Porta da Célula Aberta", "Alarme 07:", "Alarme 08:",
                      "Alarme 09: Pressão do ar comprimido baixa", "Alarme 10: Emergência do Lado Esquerdo Acionado",
                      "Alarme 11:  Emergência do Lado Direito Acionado", "Alarme 12:", "Alarme 13:",
                      "Alarme 14: Botão de Emergência Pressionado no Robô", "Alarme 15: Robô em falha",
                      "Alarme 16: Transferência de Dados com o Robô excedeu o tempo",
                      "Alarme 17: Mais de um sinal de Transferência de Dados ligado, verifique os sinais do robô",
                      "Alarme 18: Segurança da WebCam ativada - mão detectada", "Alarme 19:", "Alarme 20:", "Alarme 21:", "Alarme 22:", "Alarme 23:", "Alarme 24:",
                      "Alarme 25:", "Alarme 26:", "Alarme 27:", "Alarme 28:", "Alarme 29:", "Alarme 30:", "Alarme 31:",
                      "Alarme 32: Transferência de dados do lado A1 com erro (Python para CLP)",
                      "Alarme 33: Tempo para o cilindro da porta do lado A fechar foi excedido",
                      "Alarme 34: Tempo para o cilindro da porta do lado A abrir foi excedido",
                      "Alarme 35: Os dois sensores do cilindro da porta do lado A estão ligados",
                      "Alarme 36: Os dois sensores do cilindro da porta do lado A estão desligados",
                      "Alarme 37: Coordenada recebida com risco de colisão no lado A1",
                      "Alarme 38: Transferência de dados lado A2 com erro (Python para CLP)",
                      "Alarme 39: Coordenada recebida com risco de colisão no lado A2",
                      "Alarme 40: Proteção da porta do lado A foi acionada",
                      "Alarme 41: Robô no lado A e sensor de segurança da porta lado A não esta acionado",
                      "Alarme 42: Falha de comunicação do robô", "Alarme 43:", "Alarme 44:", "Alarme 45:", "Alarme 46:", "Alarme 47:", "Alarme 48:",
                      "Alarme 49:", "Alarme 50:", "Alarme 51:",
                      "Alarme 52:", "Alarme 53:", "Alarme 54:", "Alarme 55:",
                      "Alarme 56:", "Alarme 57:", "Alarme 58:", "Alarme 59:",
                      "Alarme 60:", "Alarme 61:", "Alarme 62:", "Alarme 63:",
                      "Alarme 64: Transferência de dados do lado B1 com erro (Python para CLP)",
                      "Alarme 65: Tempo para o cilindro da porta do lado B fechar foi excedido",
                      "Alarme 66: Tempo para o cilindro da porta do lado B abrir foi excedido",
                      "Alarme 67: Os dois sensores do cilindro da porta do lado B estão ligados",
                      "Alarme 68: Os dois sensores do cilindro da porta do lado B estão desligados",
                      "Alarme 69: Coordenada recebida com risco de colisão no lado B1",
                      "Alarme 70: Transferência de dados lado B2 com erro (Python para CLP)",
                      "Alarme 71: Coordenada recebida com risco de colisão lado B2",
                      "Alarme 72: Proteção da porta do lado B foi acionada",
                      "Alarme 73: Robô no lado B e sensor de segurança da porta lado B não esta acionado", "Alarme 74:",
                      "Alarme 75:", "Alarme 76:", "Alarme 77:", "Alarme 78:", "Alarme 79:", "Alarme 80:", "Alarme 81:",
                      "Alarme 82:", "Alarme 83:", "Alarme 84:", "Alarme 85:", "Alarme 86:", "Alarme 87:", "Alarme 88:",
                      "Alarme 89:", "Alarme 90:", "Alarme 91:", "Alarme 92:", "Alarme 93:", "Alarme 94:", "Alarme 95:",
                      "Alarme 96: Falha na verificação de User Tool", "Alarme 97:", "Alarme 98:", "Alarme 99:",
                      "Alarme 100:", "Alarme 101:", "Alarme 102:", "Alarme 103:", "Alarme 104:", "Alarme 105:",
                      "Alarme 106:", "Alarme 107:", "Alarme 108:", "Alarme 109:", "Alarme 110:", "Alarme 111:",
                      "Alarme 112:", "Alarme 113:", "Alarme 114:", "Alarme 115:", "Alarme 116:", "Alarme 117:",
                      "Alarme 118:", "Alarme 119:", "Alarme 120:", "Alarme 121:", "Alarme 122:", "Alarme 123:",
                      "Alarme 124:", "Alarme 125:", "Alarme 126:", "Alarme 127:", "Alarme 128:"]
#######################################################################################################
alarm_list: List[AlarmDict] = []
alarm_history: List[AlarmDict] = []
#######################################################################################################
# Funções de Controle
#######################################################################################################
def set_alarm_list(alarm_id: int, alarm_time: str, alarm_msg: str) -> None:
    """
    Adiciona o alarme nas listas do módulo

    Formato do alarme:
        { "id": int, "time": str, "message": str }

    :param alarm_id: Id do alarme
    :param alarm_time: Momento em que o alarme apareceu
    :param alarm_msg: Mensagem do respectivo alarme
    """
    actual_alarm: AlarmDict = {"id": alarm_id, "time": alarm_time, "message": alarm_msg}
    alarm_list.append(actual_alarm)
    alarm_history.append(actual_alarm)
#######################################################################################################
def delete_alarm_from_list(alarm_id: int) -> None:
    """
    Encontra o alarme usando o Id passado e deleta da lista do módulo

    :param alarm_id: Id do alarme
    """
    count_index = 0
    for item in alarm_list:
        if item["id"] == alarm_id:
            del alarm_list[count_index]
        count_index += 1
#######################################################################################################
def get_alarm_message(alarm_id: int) -> str:
    """
    Retorna a mensagem do alarme

    :param alarm_id: Id do alarme
    :return: Mensagem do Alarme
    """
    return alarm_message_list[alarm_id]
#######################################################################################################
def get_alarm_history() -> list:
    """
    Retorna o histórico de alarmes salvo na lista do módulo

    :return: Lista de todos os alarmes que já ocorreram
    """
    return alarm_history
#######################################################################################################

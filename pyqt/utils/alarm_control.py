from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem
from PyQt5.QtCore import Qt

alarm_message_list = ["Alarme 0: Botão de Emergência Pressionado", "Alarme 1:", "Alarme 2:", "Alarme 3:", "Alarme 4:",
                      "Alarme 5:", "Alarme 6: Porta da Célula Aberta", "Alarme 7:", "Alarme 8:",
                      "Alarme 9: Pressão do ar comprimido baixa", "Alarme 10:",
                      "Alarme 11: Emergência Interior da Célula Pressionada", "Alarme 12:", "Alarme 13:",
                      "Alarme 14: Botão de Emergência Pressionado no Robô", "Alarme 15: Robô em falha",
                      "Alarme 16: Transferência de Dados com o Robô excedeu o tempo",
                      "Alarme 17: Mais de um sinal de Transferência de Dados ligado, verifique os sinais do robô",
                      "Alarme 18:", "Alarme 19:", "Alarme 20:", "Alarme 21:", "Alarme 22:", "Alarme 23:", "Alarme 24:",
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
                      "Alarme 42:", "Alarme 43:", "Alarme 44:", "Alarme 45:", "Alarme 46:", "Alarme 47:", "Alarme 48:",
                      "Alarme 49:", "Alarme 50:", "Alarme 51:", "Alarme 52:", "Alarme 53:", "Alarme 54:", "Alarme 55:",
                      "Alarme 56:", "Alarme 57:", "Alarme 58:", "Alarme 59:", "Alarme 60:", "Alarme 61:", "Alarme 62:",
                      "Alarme 63:", "Alarme 64: Transferência de dados do lado B1 com erro (Python para CLP)",
                      "Alarme 65: Tempo para o cilindro da porta do lado B fechar foi excedido",
                      "Alarme 66: Tempo para o cilindro da porta do lado B abrir foi excedido",
                      "Alarme 67: Os dois sensores do cilindro da porta do lado B estão ligados",
                      "Alarme 68: Os dois sensores do cilindro da porta do lado B estão desligados",
                      "Alarme 69: Coordenada recebida com risco de colisão no lado B1",
                      "Alarme 70: Transferência de dados lado B2 com erro (Python para CLP)",
                      "Alarme 71: Coordenada recebida com risco de colisão lado B2",
                      "Alarme 72: Proteção da porta do lado B foi acionada",
                      "Alarme 73: Robô no lado B e sensor de segurança da porta lado B não esta acionado", "Alarme 74:"]

alarm_list = []
alarm_history = []

def set_alarm_list(alarm_id: int, alarm_time: str, alarm_msg: str):
    actual_alarm = {"id": alarm_id, "time": alarm_time, "message": alarm_msg}
    alarm_list.append(actual_alarm)
    alarm_history.append(actual_alarm)


def delete_alarm_from_list(alarm_id: int):
    count_index = 0
    for item in alarm_list:
        if item["id"] == alarm_id:
            alarm_list.pop(count_index)
        count_index += 1


def get_alarm_message(alarm_id: int) -> str:
    return alarm_message_list[alarm_id]


def get_alarm_history() -> list:
    return alarm_history

def define_alarm_list(ui, alarm_time: str, alarm_id: int):
    listWidget = ui.alarm_list_widget
    histWidget = ui.hist_alarm_list_widget
    # ToDo => da pra adicionar de duas formas:
    # ToDo => 1ª adicionar no final da lista
    row_num = listWidget.rowCount()
    hist_row_num = histWidget.rowCount()
    # ToDo => 2ª adicionar ao início da lista
    # row_num = 0
    # hist_row_num = 0
    alarm_msg: str = get_alarm_message(alarm_id)

    set_alarm_list(alarm_id, alarm_time, alarm_msg)

    time_item = QTableWidgetItem()
    msg_item = QTableWidgetItem()
    time_item.setText(str(alarm_time))
    msg_item.setText(alarm_msg)

    hist_time = QTableWidgetItem()
    hist_msg = QTableWidgetItem()
    hist_time.setText(str(alarm_time))
    hist_msg.setText(alarm_msg)

    listWidget.insertRow(row_num)
    listWidget.setItem(row_num, 0, time_item)
    listWidget.setItem(row_num, 1, msg_item)

    histWidget.insertRow(hist_row_num)
    histWidget.setItem(hist_row_num, 0, hist_time)
    histWidget.setItem(hist_row_num, 1, hist_msg)

def delete_alarm_row(ui, alarm_id: int):
    listWidget: QTableWidget = ui.alarm_list_widget

    itemFound = listWidget.findItems(f"Alarme {alarm_id}:", Qt.MatchContains)
    listWidget.setCurrentItem(itemFound[0])

    row_num = itemFound[0].row()

    listWidget.removeRow(row_num)
    delete_alarm_from_list(alarm_id)


current_row = 0
def row_down(listWidget: QTableWidget):
    global current_row

    current_row = listWidget.currentRow()
    current_row += 1

    listWidget.setCurrentCell(current_row, 0)

def row_up(listWidget):
    global current_row

    current_row = listWidget.currentRow()
    current_row -= 1

    listWidget.setCurrentCell(current_row, 0)



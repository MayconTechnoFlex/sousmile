"""Funções para facilitar a criação e configuração de tabela"""
#######################################################################################################
# Importações
#######################################################################################################
from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem
#######################################################################################################
# Função
#######################################################################################################
def qt_create_table(widget: QTableWidget, num_col: int, num_row: int):
    """
    Função para criar e configurar tabela de pontos

    :param widget: QTableWidget usado no tela de Filtro de Coordenadas
    :param num_col: Número de colunas que deseja na tabela
    :param num_row: Número de linhas que deseja na tabela
    """
    ###################################################################################################
    # Create a table
    ###################################################################################################
    widget.setColumnCount(num_col)
    widget.setRowCount(num_row)
    widget.setHorizontalHeaderItem(0, QTableWidgetItem("Posições"))
    widget.setHorizontalHeaderItem(1, QTableWidgetItem("X"))
    widget.setHorizontalHeaderItem(2, QTableWidgetItem("Y"))
    widget.setHorizontalHeaderItem(3, QTableWidgetItem("Z"))
    widget.setHorizontalHeaderItem(4, QTableWidgetItem("C"))
    widget.setHorizontalHeaderItem(5, QTableWidgetItem("D"))
    widget.setHorizontalHeaderItem(6, QTableWidgetItem("Info"))
    widget.horizontalHeader().setVisible(True)
    widget.verticalHeader().setVisible(True)
#######################################################################################################

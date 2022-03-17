from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem

from typing import List


def qt_create_table(widget: QTableWidget,
                    num_col: int,
                    num_row: int):
    """
    Function to create a table

    :param widget: QTableWidget used on the program
    :param num_col: Number of column that you want on the table
    :param num_row: Number of rows that you want on the table
    :return: Nothing
    """

    ##################################################
    # Create a table
    ##################################################
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
    ##################################################

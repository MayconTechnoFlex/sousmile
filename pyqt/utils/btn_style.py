#######################################################################################################
# Importações
#######################################################################################################
from PyQt5.QtWidgets import QPushButton
#######################################################################################################
# Estilos
#######################################################################################################
base_button_style = """
QPushButton{ background-color: #ffdf00; color: #000000 }
QPushButton:hover{ background-color: #f1d100 }
QPushButton:pressed{ background-color: #dfc200 }
QPushButton::disabled{ background-color: #cbcbcb; color: gray }
"""
#######################################################################################################
checked_button_style = """
QPushButton{ background-color: #565656; color: #ffdf00 }
QPushButton:hover{ background-color: #434343 }
QPushButton:pressed{ background-color: #232323 }
QPushButton::disabled{ background-color: #cbcbcb; color: gray }
"""
#######################################################################################################
btn_error_style = """
* { background-color : #dc1f1f; color : black; }
"""
#######################################################################################################
# Funções
#######################################################################################################
def setErrorButton(button: QPushButton):
    button.setStyleSheet(btn_error_style)
    button.setText("Erro")
    button.setEnabled(False)
#######################################################################################################

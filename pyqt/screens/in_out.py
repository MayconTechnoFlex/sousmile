"""Módulo com todas as funções para a tela Entradas e Saídas"""
#######################################################################################################
# Importações
#######################################################################################################
from typing import Callable
from ui_py.ui_gui_final import Ui_MainWindow

from utils.functions.gui_functions import change_status
#######################################################################################################
# Definição das variáveis globais
#######################################################################################################
UI: Ui_MainWindow
#######################################################################################################
# Funções de Definição
#######################################################################################################
def define_buttons(ui_main: Ui_MainWindow, change_screen_func: Callable[[], None]):
    """
    Define os botões da tela

    :param main_ui: Ui da aplicação
    :param change_screen_func: Função para retornar à tela anterior (Manutenção)
    """
    global UI
    UI = ui_main
    UI.btn_volta_manut_screen.clicked.connect(change_screen_func)
#######################################################################################################
# Funções de Atualização
#######################################################################################################
def UpdateInOut(tag):
    """
    Atualiza os Status da tela com os valores do CLP

    :param tag: Tag lida do CLP
    """
    global UI
    try:
        change_status(tag[0][1], UI.sts_start_a)
        change_status(tag[1][1], UI.sts_start_b)
        change_status(tag[2][1], UI.sts_btn_solic_ent_cel)
        change_status(tag[3][1], UI.sts_btn_reset)
        change_status(tag[4][1], UI.sts_sinal_emerg)
        change_status(tag[5][1], UI.sts_sinal_port)
        change_status(tag[6][1], UI.sts_btn_emerg_ehm)
        change_status(tag[7][1], UI.sts_btn_emerg_int)
        change_status(tag[8][1], UI.sts_btn_emerg_port)
        change_status(tag[9][1], UI.sts_sens_port_fec_a)
        change_status(tag[10][1], UI.sts_sens_port_abr_a)
        change_status(tag[11][1], UI.sts_sens_port_fec_b)
        change_status(tag[12][1], UI.sts_sens_port_abr_b)
        change_status(tag[13][1], UI.sts_sinal_seg_port_a)
        change_status(tag[14][1], UI.sts_sinal_seg_port_b)
        change_status(tag[15][1], UI.sts_pressostato)

        change_status(tag[16][1], UI.sts_saida_reserv_00)
        change_status(tag[17][1], UI.sts_saida_reserv_01)
        change_status(tag[18][1], UI.sts_saida_reserv_02)
        change_status(tag[19][1], UI.sts_saida_reserv_03)
        change_status(tag[20][1], UI.sts_saida_reserv_04)
        change_status(tag[21][1], UI.sts_lamp_verd_a)
        change_status(tag[22][1], UI.sts_lamp_verm_a)
        change_status(tag[23][1], UI.sts_lamp_amar_a)
        change_status(tag[24][1], UI.sts_lamp_verd_b)
        change_status(tag[25][1], UI.sts_lamp_verm_b)
        change_status(tag[26][1], UI.sts_lamp_amar_b)
        change_status(tag[27][1], UI.sts_sinal_sono)
        change_status(tag[28][1], UI.sts_lamp_btn_reset)
        change_status(tag[29][1], UI.sts_lamp_btn_solic_ent)
        change_status(tag[30][1], UI.sts_ent_libe)
        change_status(tag[31][1], UI.sts_saida_reserv_05)

        change_status(tag[32][1], UI.sts_seg_port_a)
        change_status(tag[33][1], UI.sts_seg_port_b)
        change_status(tag[34][1], UI.sts_ent_reserv_02)
        change_status(tag[35][1], UI.sts_ent_reserv_03)
        change_status(tag[36][1], UI.sts_ent_reserv_04)
        change_status(tag[37][1], UI.sts_ent_reserv_05)
        change_status(tag[38][1], UI.sts_ent_reserv_06)
        change_status(tag[39][1], UI.sts_ent_reserv_07)
    except Exception as e:
        print(e)
#######################################################################################################

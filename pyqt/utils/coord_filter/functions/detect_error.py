"""Função para detecção e filtro de erros"""
#######################################################################################################
# Importações
#######################################################################################################
import pandas as pd
from pandas.io.parsers.readers import TextFileReader
from utils.coord_filter.functions.calc_functions import *
#######################################################################################################
# Funções
#######################################################################################################
def find_error_filter(data: TextFileReader):
    """
    Calcula a distancia entre um ponto e os seus próximos 25 pontos para ver se a distancia entre o
    primeiro e o segundo ponto são realmente as menores, caso não esse ponto é excluido e o ponto
    com o que o primeiro ponto teve a menor distancia entra para a lista de posições

    :param data: Lista de posições vindas de um arquivo csv
    :return:
    """
    new_data = list()
    d = list()
    i = 0
    points_ahead = 25
    while i < len(data):
        if i > 0:
            for j in range(1, points_ahead):
                if i + j >= len(data):
                    break
                d.append(dist_between_points(data, i + j, i))
        if (i == 0) or (len(d) < 2) or ((d[0]) <= min(d[1:points_ahead])):
            new_data.append(data.values[i])
            i = i + 1
        else:
            i = i + d.index(min(d[1:points_ahead]))
        d.clear()

    new_df = pd.DataFrame(new_data)

    print('Foram removidas', len(data) - len(new_data), 'linhas')

    return new_df
#######################################################################################################

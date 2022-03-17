from utils.coord_filter.functions.detect_error import *
from utils.coord_filter.functions import position_filter_test
import matplotlib.pyplot as plt
from datetime import date, datetime
from typing import List


def test_file(file_path: str,
              lx: List[float],
              ly: List[float],
              lz: List[float],
              lc: List[float],
              ld: List[float],
              l_pos: List[int],
              l_info: List[str],
              var_limit_d: float,
              var_limit_c: float,
              var_limit_xyz: float,
              var_limit_h: float,
              var_p: float) -> int:
    """
    Função para teste do filtro de pontos

    :param file_path:
    :param lx: Lista para as posições de X
    :param ly: Lista para as posições de Y
    :param lz: Lista para as posições de Z
    :param lc: Lista para as posições de c
    :param ld: Lista para as posições de d
    :param l_pos: Lista do numero das posições
    :param l_info: Lista de informações
    :param var_limit_d: variavél para o limite de d
    :param var_limit_c: variavél para o limite de c
    :param var_limit_xyz: variavél para o limite da distância entre os pontos
    :param var_limit_h: variavél para o limite da altura do ponto
    :param var_p: variavél para a profundidade do corte
    :return: O número de posições do arquivo original
    """

    data = pd.read_csv(file_path, sep=',', header=None)  # Copia o arquivo csv do caminho  -filepath
    num_pos_orig_file = len(data)
    new_data = find_error_filter(data)
    position_filter_test.pos_filter(new_data, lx, ly, lz, lc, ld, l_pos, l_info, var_limit_d, var_limit_c,
                                    var_limit_xyz, var_limit_h, var_p)

    return num_pos_orig_file


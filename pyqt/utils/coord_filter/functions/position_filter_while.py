"""Modulo para Filtrar Pontos de arquivo da nuvem"""
#######################################################################################################
# Importações
#######################################################################################################
from utils.coord_filter.functions.calc_functions import *
from pandas.io.parsers.readers import DataFrame
from typing import List
#######################################################################################################
# Função
#######################################################################################################
def pos_filter(in_data: DataFrame, lx: List[float], ly: List[float], lz: List[float],
               lc: List[float], ld: List[float], l_pos: List[int], l_info: List[str],
               tag_cut_depth: str, config_pontos: dict):
    """
    Função para filtrar pontos e salvar em listas individuais

    :param in_data:
    :param lx: Lista para valores de posição em X
    :param ly: Lista para valores de posição em Y
    :param lz: Lista para valores de posição em Z
    :param lc: Lista para valores de posição em C
    :param ld: Lista para valores de posição em D
    :param l_pos: Lista para valores o numero da posição
    :param l_info: Lista de informações
    :param tag_cut_depth: Tag de profundidade de corte
    :param config_pontos: Tag de ConfigPontos
    """

    print('- Lendo tag do clp para a configuração dos filtros de pontos')
    ######################################################################################
    limit_D = config_pontos['Diff_AngleD']
    limit_C = config_pontos['Diff_AngleC']
    limit_XYZ = config_pontos['Dist_XYZ']
    limit_h = config_pontos['Dist_H']
    p = config_pontos[tag_cut_depth]
    ######################################################################################
    print(f'''
    - Ajustes para filtro de posição:
    - Diferença do ângulo D: {limit_D};
    - Diferença do ângulo C: {limit_C};
    - Distância entre pontos: {limit_XYZ};
    - Profundidade entre os 3 pontos: {round(limit_h, 3)};
    - Profundidade de corte: {round(p, 3)};''')
    #####################################################################################
    # Clear the lists
    #####################################################################################
    print('- Limpando as listas de posições e de informações')
    lx.clear()
    ly.clear()
    lz.clear()
    lc.clear()
    ld.clear()
    l_pos.clear()
    l_info.clear()
    #####################################################################################
    # Set positions variables
    #####################################################################################
    pos_1 = 0
    pos_2 = 1
    pos_3 = 2
    #####################################################################################
    # Add the first point to the list
    #####################################################################################
    print('- Adicionando primeiro ponto na lista de posições')
    if pos_1 == 0:
        ##################################################################
        # Save the data of the first position to the list
        ##################################################################
        lx.append(round(cut_depth_x(in_data, pos_1, p), 1))
        ly.append(round(cut_depth_y(in_data, pos_1, p), 1))
        lz.append(round(cut_depth_z(in_data, pos_1, p), 1))
        ld.append(round(calc_attack_angle(in_data, pos_1), 1))
        ##################################################################
        # Check if the limits of "C" are between 180 and -180
        ##################################################################
        if round(float(in_data.values[pos_1][5].replace('C=', ''))) > 180:
            lc.append(180)
        elif round(float(in_data.values[pos_1][5].replace('C=', ''))) < -180:
            lc.append(-180)
        else:
            lc.append(round(float(in_data.values[pos_1][5].replace('C=', ''))))
        ###################################################################
        # Add the number of the point to the list
        ###################################################################
        l_pos.append(pos_1)
        ###################################################################
        l_info.append(f'Ponto adicionado por ser o primeiro da lista')
        ###################################################################
    #####################################################################################
    # Start while loop
    #####################################################################################
    print('- Entrando no loop while para filtrar os pontos')
    while pos_1 <= len(in_data.index):

        if (pos_1 + 4) < len(in_data.index):
            while True:
                #################################################################################################
                dist_XYZ = dist_between_points(in_data, pos_1, pos_2)  # Calc distance between points
                D1 = calc_attack_angle(in_data, pos_1)  # Calculates attack angle
                D2 = calc_attack_angle(in_data, pos_2)  # Calculates attack angle of the next point
                difference_D = D2 - D1  # Calculates the attack angle difference between the points
                difference_C = calc_diff_c_angle(in_data, pos_1, pos_2)  # Calc the difference between two angles C
                a = dist_between_points(in_data, pos_1, pos_2)  # Side "a" of the triangle
                b = dist_between_points(in_data, pos_1, pos_3)  # Side "b" of the triangle
                c = dist_between_points(in_data, pos_2, pos_3)  # Side "c" of the triangle
                ####################################################################################################
                #  Triangle height - Triângulo criado por três pontos para criar um filtro da profundidade do corte
                h = triangle_height(a, b, c)
                ###################################################################################################
                # Check the differences betwen points
                ###################################################################################################
                if abs(difference_D) <= limit_D and abs(difference_C) <= limit_C and h <= limit_h and dist_XYZ <= limit_XYZ:
                    ######################################################################
                    # If the differences are in the limits change the value
                    # of pos_2 and pos_3
                    ######################################################################
                    pos_2 += 1
                    pos_3 += 1
                    ######################################################################
                # Difference filter
                else:
                    ########################################################################################################
                    # Add to the list why we added the position
                    ########################################################################################################
                    if abs(difference_D) > limit_D and abs(difference_C) < limit_C and h < limit_h and dist_XYZ < limit_XYZ:
                        l_info.append(f'Limite D: {round(difference_D, 1)}')
                    elif abs(difference_D) < limit_D and abs(
                            difference_C) > limit_C and h < limit_h and dist_XYZ < limit_XYZ:
                        l_info.append(f'Limite C: {round(difference_C, 1)}')
                    elif abs(difference_D) < limit_D and abs(
                            difference_C) < limit_C and h > limit_h and dist_XYZ < limit_XYZ:
                        l_info.append(f'Limite H: {round(h, 3)}')
                    elif abs(difference_D) < limit_D and abs(
                            difference_C) > limit_C and h > limit_h and dist_XYZ < limit_XYZ:
                        l_info.append(
                            f'Limite H e C: {round(h, 3)}/ {round(difference_C, 1)})')
                    elif abs(difference_D) > limit_D and abs(
                            difference_C) < limit_C and h > limit_h and dist_XYZ < limit_XYZ:
                        l_info.append(
                            f'Limite H e D: {round(h, 3)}/ {round(difference_D, 1)}')
                    elif abs(difference_D) > limit_D and abs(
                            difference_C) > limit_C and h < limit_h and dist_XYZ < limit_XYZ:
                        l_info.append(
                            f'Limite C e D: {round(difference_C, 1)}/ {round(difference_D, 1)}')
                    elif abs(difference_D) > limit_D and abs(
                            difference_C) > limit_C and h < limit_h and dist_XYZ < limit_XYZ:
                        l_info.append(
                            f'Limite C e D: {round(difference_C, 1)}/ {round(difference_D, 1)}')
                    elif abs(difference_D) < limit_D and abs(
                            difference_C) < limit_C and h < limit_h and dist_XYZ > limit_XYZ:
                        l_info.append(
                            f'Limite XYZ: {round(dist_XYZ, 1)}')
                    elif abs(difference_D) > limit_D and abs(
                            difference_C) < limit_C and h < limit_h and dist_XYZ > limit_XYZ:
                        l_info.append(
                            f'Limite XYZ e D: {round(dist_XYZ, 1)}/ {round(difference_D, 1)}')
                    elif abs(difference_D) < limit_D and abs(
                            difference_C) > limit_C and h < limit_h and dist_XYZ > limit_XYZ:
                        l_info.append(
                            f'Limite XYZ e C: {round(dist_XYZ, 1)}/ {round(difference_C, 1)}')
                    elif abs(difference_D) < limit_D and abs(
                            difference_C) < limit_C and h > limit_h and dist_XYZ > limit_XYZ:
                        l_info.append(
                            f'Limite XYZ e C: {round(dist_XYZ, 1)}/ {round(h, 3)}')
                    else:
                        l_info.append(
                            f'Todos os limites: H:{round(h, 3)}/ C:{round(difference_C, 1)}/ '
                            f'D:{round(difference_D, 1)}/ XYZ:{round(dist_XYZ, 1)}')
                    ##########################################################
                    # Add the position to the list
                    ##########################################################
                    lx.append(round(cut_depth_x(in_data, pos_2, p), 1))
                    ly.append(round(cut_depth_y(in_data, pos_2, p), 1))
                    lz.append(round(cut_depth_z(in_data, pos_2, p), 1))
                    ld.append(round(calc_attack_angle(in_data, pos_2), 1))
                    ##################################################################
                    # Check if the limits of "C" are between 180 and -180
                    ##################################################################
                    if round(float(in_data.values[pos_2][5].replace('C=', '')), 1) > 180:
                        lc.append(180)
                    elif round(float(in_data.values[pos_2][5].replace('C=', '')), 1) < -180:
                        lc.append(-180)
                    else:
                        lc.append(round(float(in_data.values[pos_2][5].replace('C=', '')), 1))
                    ##################################################################
                    # Change the variables value
                    ##################################################################
                    pos_1 = pos_2
                    pos_2 += 1
                    pos_3 += 1
                    ###################################################################
                    # Add the number of the point to the list
                    ###################################################################
                    l_pos.append(pos_2)
                    break
        else:
            print('- Terminando de filtrar posições')

            """for _ in range(5):
                lx.append(round(cut_depth_x(in_data, l_pos[_], p), 1))
                ly.append(round(cut_depth_y(in_data, l_pos[_], p), 1))
                lz.append(round(cut_depth_z(in_data, l_pos[_], p), 1))
                ld.append(round(calc_attack_angle(in_data, l_pos[_]), 1))

                # Check if the limits of "C" are between 180 and -180
                if round(float(in_data.values[l_pos[_]][5].replace('C=', '')), 1) > 180:
                    lc.append(180)
                elif round(float(in_data.values[l_pos[_]][5].replace('C=', '')), 1) < -180:
                    lc.append(-180)
                else:
                    lc.append(round(float(in_data.values[l_pos[_]][5].replace('C=', '')), 1))

                l_pos.append(l_pos[_])
                l_info.append(f'Ponto adicionado para terminar o ciclo')"""
            break
#######################################################################################################

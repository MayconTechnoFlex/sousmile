"""Modulo de fórmula para diferentes cálculos com coordenadas"""
#######################################################################################################
# Importações
#######################################################################################################
import math
#######################################################################################################
# Funções
#######################################################################################################
import traceback


def calc_diff_c_angle(data, pos1, pos2):
    C1 = float(data.values[pos1][5].replace('C=', ''))
    C2 = float(data.values[pos2][5].replace('C=', ''))
    return abs((abs(C2) - 180)) - abs((abs(C1) - 180))
#######################################################################################################
def calc_attack_angle(data, pos):
    A1 = float(data.values[pos][3].replace('A=', ''))
    B1 = float(data.values[pos][4].replace('B=', ''))
    return abs(max(abs(A1), abs(B1)) - 90)
#######################################################################################################
def dist_between_points(data, p1, p2):
    # Calc distance between points
    X1 = float(data.values[p1][0].replace('X=', ''))
    X2 = float(data.values[p2][0].replace('X=', ''))
    Y1 = float(data.values[p1][1].replace('Y=', ''))
    Y2 = float(data.values[p2][1].replace('Y=', ''))
    Z1 = float(data.values[p1][2].replace('Z=', ''))
    Z2 = float(data.values[p2][2].replace('Z=', ''))
    return math.sqrt(math.pow((X2 - X1), 2) + math.pow((Y2 - Y1), 2) + math.pow((Z2 - Z1), 2))
#######################################################################################################
def triangle_height(a, b, c):
    if abs(b) < 0.01:
        b = 0.01

    h = math.sqrt(abs(math.pow(a, 2) - math.pow(((math.pow(a, 2) + math.pow(b, 2) - math.pow(c, 2)) / (2 * b)), 2)))
    return h
#######################################################################################################
def cut_depth_x(in_data, i, p):
    x = float(in_data.values[i][0].replace('X=', ''))
    b = float(in_data.values[i][4].replace('B=', ''))
    c = float(in_data.values[i][5].replace('C=', ''))

    if -90 <= c <= 90:
        return x - math.sin(math.radians(abs(b))) * p
    else:
        return x + math.sin(math.radians(abs(b))) * p
#######################################################################################################
def cut_depth_y(in_data, i, p):
    y = float(in_data.values[i][1].replace('Y=', ''))
    a = float(in_data.values[i][3].replace('A=', ''))
    c = float(in_data.values[i][5].replace('C=', ''))

    # Verifica se o valor de "C" não ultrapassou os limites de 180 e -180
    if c > 180:
        c = 180
    elif c <= -180:
        c = -180

    if -180 <= c <= 0:
        return y - math.sin(math.radians(abs(a))) * p
    else:
        return y + math.sin(math.radians(abs(a))) * p
#######################################################################################################
def cut_depth_z(in_data, i, p):
    z = float(in_data.values[i][2].replace('Z=', ''))
    d = calc_attack_angle(in_data, i)
    return z - math.sin(math.radians(d)) * p
#######################################################################################################

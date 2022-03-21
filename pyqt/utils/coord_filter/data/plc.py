"""Filtro de Coordenadas via CLP"""
#######################################################################################################
# Importações
#######################################################################################################
from PyQt5.QtCore import pyqtSignal, QRunnable, QObject
from datetime import date, datetime
from typing import List

import matplotlib.pyplot as plt
import pandas as pd
from pycomm3 import LogixDriver

from ui_py.ui_gui_final import Ui_MainWindow
from utils.coord_filter.functions import position_filter_while
from utils.coord_filter.functions.detect_error import find_error_filter
from utils.coord_filter.workers_coord_filter import *

from utils.coord_filter.workers_coord_filter import WorkerSignals
#######################################################################################################
# Definição das Variáveis Globais
#######################################################################################################
data_list_X: List[float] = []
data_list_Y: List[float] = []
data_list_Z: List[float] = []
data_list_C: List[float] = []
data_list_D: List[float] = []
data_list_pos: List[int] = []
data_list_info: List[str] = []
#######################################################################################################
class Worker_Data_to_PLC(QRunnable):
    def __init__(self,
                 data_ctrl: dict,
                 tag_cut_depth: str,
                 tag_enable_log: bool,
                 tag_max_num_points: int,
                 config_pontos: dict,
                 data_ctrl_str: str,
                 cloud_signal: bool,
                 local_signal: bool,
                 local_file: str,
                 ui: Ui_MainWindow,
                 scene,
                 code: str):
        super(Worker_Data_to_PLC, self).__init__()
        self.signal = WorkerSignals()
        self.data_ctrl = data_ctrl
        self.tag_cut_depth = tag_cut_depth
        self.tag_enable_log = tag_enable_log
        self.tag_max_num_points = tag_max_num_points
        self.config_pontos = config_pontos
        self.data_ctrl_str = data_ctrl_str
        self.cloud_signal = cloud_signal
        self.local_signal = local_signal
        self.local_file = local_file
        self.ui = ui
        self.scene = scene
        self.code = code

    def data_to_plc(self,
                    data_ctrl: dict,
                    tag_cut_depth: str,
                    tag_enable_log: bool,
                    tag_max_num_points: int,
                    config_pontos: dict,
                    data_ctrl_str: str,
                    cloud_signal: bool,
                    local_signal: bool,
                    local_file: str,
                    ui: Ui_MainWindow,
                    scene,
                    code: str):
        """
        :param data_ctrl: DataCtrl_(Lado do corte (A1, A2, B1, B2))
        :param tag_cut_depth: Tag com a profundidade do corte
        :param tag_enable_log: Tag para habilitar o log dos arquivos filtrados
        :param tag_max_num_points: Tag da IHM que limita o numero de pontos
        :param config_pontos: Tag config pontos
        :param data_ctrl_str:
        :param cloud_signal: Sinal para pegar os pontos do servidor da nuvem
        :param local_signal: Sinal para pegar os pontos de um arquivo local
        :param local_file: Caminho do aquivo local
        :param ui:
        :param scene:
        :param code:
        :return:
        """
        #######################################
        # set url
        #######################################
        print("Entrou na rotina")
        if cloud_signal:
            print('- Coletando dados da nuvem')
            url = 'https://sousmile-ed-integration.herokuapp.com/manage-files/download'
        elif local_signal and not cloud_signal:
            print('- Coletando dados de um arquivo local')
            url = local_file
        #######################################
        print('- Iniciando transferência de dados para o CLP Rockwell')
        # filepath = f'{url}/{data_ctrl["ProdCode"]}.csv'
        filepath = f'{url}/{code}.csv'
        print(filepath)
        print('-Inicia tempo de tranferência')
        start = time.time()  # Inicio da contagem de tempo para a transferência de dados

        write_tag(f'{data_ctrl_str}.Started', True)
        try:
            ##############################################################################################
            print("- Lendo arquivo...")
            data = pd.read_csv(filepath, sep=',', header=None)  # Copia o arquivo csv do caminho  -filepath
            write_tag(f'{data_ctrl_str}.FileNumPos', len(data.index))  # Number of positions in the original file
            ##############################################################################################
            print('- Iniciou filtro para verificar se há erros na linha de corte')
            new_data = find_error_filter(data)
            ##############################################################################################
            position_filter_while.pos_filter(new_data, data_list_X, data_list_Y, data_list_Z, data_list_C, data_list_D,
                                             data_list_pos, data_list_info, tag_cut_depth, config_pontos)
            ##############################################################################################
            print('- Finalizou a seleção de pontos')
            ##############################################################################################
            num_rows = len(data_list_X)
            num_values_to_pass = len(data_list_X)
            ##############################################################################################
            with LogixDriver('192.168.1.10') as plc:
                plc.write((f'{data_ctrl_str}.NumPos', num_rows),
                          (f'{data_ctrl_str}.Status', 'Transferencia de Dados Iniciou'))
            ##############################################################################################
            #  Check the number of points
            ##############################################################################################
            print(f'- Check do número de pontos após o filtro, número máximo de pontos: {tag_max_num_points}')
            if num_rows > tag_max_num_points:
                print('- Erro no arquivo número de pontos maior do que o limite colocado')
                raise Exception
            ##############################################################################################
            for i in range(0, num_rows, num_values_to_pass):
                print(f'- Transferindo {num_values_to_pass} dados para o CLP')
                try:
                    with LogixDriver('192.168.1.10') as plc:
                        plc.write(
                            (f'{data_ctrl_str}.PosX[{i}]{{{num_values_to_pass}}}', data_list_X[i:i + num_values_to_pass]),
                            (f'{data_ctrl_str}.PosY[{i}]{{{num_values_to_pass}}}', data_list_Y[i:i + num_values_to_pass]),
                            (f'{data_ctrl_str}.PosZ[{i}]{{{num_values_to_pass}}}', data_list_Z[i:i + num_values_to_pass]),
                            (f'{data_ctrl_str}.PosD[{i}]{{{num_values_to_pass}}}', data_list_D[i:i + num_values_to_pass]),
                            (f'{data_ctrl_str}.PosC[{i}]{{{num_values_to_pass}}}', data_list_C[i:i + num_values_to_pass])
                        )
                except Exception as e:
                    print(f"{e} - falha ne escrita de valores para o CLP")
            print(f'- Terminou a transferência dos pontos para o CLP')
            ##############################################################################################
            # Check if the signal to create a log is on
            ##############################################################################################
            if tag_enable_log:

                print('- Log de pontos habilitado')

                # date and time
                today = date.today()
                now_Hour = datetime.now().hour
                now_Minute = datetime.now().minute
                now_Second = datetime.now().second

                if not os.path.exists('log'):
                    os.makedirs('log')

                save_path = f'{os.getcwd()}\\log'
                file_name = f'{data_ctrl["ProdCode"]}_{today} {now_Hour}_{now_Minute}_{now_Second}.txt'
                completeName = os.path.join(save_path, file_name)

                # create a log file of the filtered positions, that the PLC received

                log_file = open(completeName, 'w')

                for i in range(len(data_list_pos)):
                    log_file.write(f'Pos:{data_list_pos[i]} X:{round(data_list_X[i], 1)} Y:{round(data_list_Y[i], 1)} '
                                   f'Z:{round(data_list_Z[i], 1)} C:{round(data_list_C[i], 1)} '
                                   f'D: {round(data_list_D[i], 1)} {data_list_info[i]}\n')
                log_file.close()

                filename = f'{os.getcwd()}\\log\\{data_ctrl["ProdCode"]}_{today} {now_Hour}_{now_Minute}_{now_Second}.png'

                fig1, ax1 = plt.subplots()
                lines, = ax1.plot(data_list_X, data_list_Y)
                fig1.savefig(filename, dpi=300)
                plt.close(fig1)

                print(f'- Os arquivos de log foram salvos em: {os.getcwd()}\\log')
            # ---------------------------------------------------------------------------------------------------------
            stop = time.time()  # Stop time to transfer data
            duration = stop - start

            with LogixDriver('192.168.1.10') as plc:
                plc.write((f'{data_ctrl_str}.Started', False), (f'{data_ctrl_str}.Status', 'Transferencia de dados acabou'))

            print(f'- Transferencia acabou, duração de {duration}')
            ########################################################################################
            # Create table to show data and a scene to 'create' a graphic that was passed to the robot
            ########################################################################################
            # Create a table
            ########################################################################################
            self.signal.result_list.emit([data_list_pos, data_list_X, data_list_Y,
                             data_list_Z, data_list_C, data_list_D, data_list_info])
        except Exception as e:
            # print python error
            print(e)

            with LogixDriver('192.168.1.10') as plc:
                plc.write((f'{data_ctrl_str}.Error', True), (f'{data_ctrl_str}.Status', 'Erro na Transferencia de Dados'))

    def run(self):
        self.data_to_plc(self.data_ctrl,
                         self.tag_cut_depth,
                         self.tag_enable_log,
                         self.tag_max_num_points,
                         self.config_pontos,
                         self.data_ctrl_str,
                         self.cloud_signal,
                         self.local_signal,
                         self.local_file,
                         self.ui,
                         self.scene,
                         self.code)
#######################################################################################################

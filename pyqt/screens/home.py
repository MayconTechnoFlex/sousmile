########################################################################################
# Contorl of widgets home screen
########################################################################################
from pyqt.main import *
from pyqt.utils.Types import *

def home_screen_func(ui: Ui_MainWindow, show_dialog: AltValShowDialog_WithoutText):
    ####################################################################
    # button to show pop up to insert code manually
    ####################################################################
    ui.btn_in_cod_man_a1.clicked.connect(lambda: show_dialog('DataCtrl_A1.ProdCode', "string"))
    ui.btn_in_cod_man_a2.clicked.connect(lambda: show_dialog('DataCtrl_A2.ProdCode', "string"))
    ui.btn_in_cod_man_b1.clicked.connect(lambda: show_dialog('DataCtrl_B1.ProdCode', "string"))
    ui.btn_in_cod_man_b2.clicked.connect(lambda: show_dialog('DataCtrl_B2.ProdCode', "string"))

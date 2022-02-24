"""Module with all functions used on the ProductionScreen of the application"""
from PyQt5.QtCore import QThread, Qt
from PyQt5.QtWidgets import QApplication

from ui_py.ui_gui_final import Ui_MainWindow

from utils.ctrl_plc import write_tag
from utils.btn_style import btn_error_style

UI: Ui_MainWindow

class ThreadResetProduct(QThread):
    def __init__(self, button, *tags: str):
        super(ThreadResetProduct, self).__init__()
        self.button = button
        self.tags = tags

    def run(self):
        QApplication.setOverrideCursor(Qt.WaitCursor)
        self.button.setEnabled(False)
        try:
            for tag in self.tags:
                write_tag(tag, 0)
        except Exception as e:
            print(e)
        self.button.setEnabled(True)


resetA1: ThreadResetProduct
resetA2: ThreadResetProduct
resetA: ThreadResetProduct
resetB1: ThreadResetProduct
resetB2: ThreadResetProduct
resetB: ThreadResetProduct

def define_buttons(receive_ui: Ui_MainWindow):
    """
    Define the buttons of the screen

    Params:
        receive_ui = main ui of the application
    """
    global UI, resetA1, resetA2, resetA, resetB1, resetB2, resetB
    UI = receive_ui

    resetA1 = ThreadResetProduct(UI.btn_reset_prod_a1, "HMI.Production.PartsDoneA1")
    resetA2 = ThreadResetProduct(UI.btn_reset_prod_a2, "HMI.Production.PartsDoneA2")
    resetA = ThreadResetProduct(UI.btn_reset_prod_total_a, "HMI.Production.PartsDoneA1", "HMI.Production.PartsDoneA2")
    resetB1 = ThreadResetProduct(UI.btn_reset_prod_b1, "HMI.Production.PartsDoneB1")
    resetB2 = ThreadResetProduct(UI.btn_reset_prod_b2, "HMI.Production.PartsDoneB2")
    resetB = ThreadResetProduct(UI.btn_reset_prod_total_b, "HMI.Production.PartsDoneB1", "HMI.Production.PartsDoneB2")

    UI.btn_reset_prod_a1.clicked.connect(resetA1.start)
    UI.btn_reset_prod_a2.clicked.connect(resetA2.start)
    UI.btn_reset_prod_b1.clicked.connect(resetB1.start)
    UI.btn_reset_prod_b2.clicked.connect(resetB2.start)
    UI.btn_reset_prod_total_a.clicked.connect(resetA.start)
    UI.btn_reset_prod_total_b.clicked.connect(resetB.start)

def UpdateHMI(tag):
    """
    Updates the screen's labels with the readed tag values

    Params:
        tag = readed tag from HMI
    """
    global UI
    try:
        prodTag = tag["Production"]
        UI.lbl_PartsDoneA1.setText(str(prodTag["PartsDoneA1"]))
        UI.lbl_PartsDoneA2.setText(str(prodTag["PartsDoneA2"]))
        UI.lbl_PartsDoneSideA.setText(str(prodTag["PartDoneSideA"]))
        UI.lbl_TimeCutA1.setText(str(round(prodTag["TimeCutA1"], 2)))
        UI.lbl_TimeCutA2.setText(str(round(prodTag["TimeCutA2"], 2)))
        UI.lbl_TimeCutSideA.setText(str(round(prodTag["TimeCutSideA"], 2)))

        UI.lbl_PartsDoneB1.setText(str(prodTag["PartsDoneB1"]))
        UI.lbl_PartsDoneB2.setText(str(prodTag["PartsDoneB2"]))
        UI.lbl_PartsDoneSideB.setText(str(prodTag["PartDoneSideB"]))
        UI.lbl_TimeCutB1.setText(str(round(prodTag["TimeCutB1"], 2)))
        UI.lbl_TimeCutB2.setText(str(round(prodTag["TimeCutB2"], 2)))
        UI.lbl_TimeCutSideB.setText(str(round(prodTag["TimeCutSideB"], 2)))

        QApplication.restoreOverrideCursor()
    except:
        UI.btn_reset_prod_a1.setStyleSheet(btn_error_style)
        UI.btn_reset_prod_a2.setStyleSheet(btn_error_style)
        UI.btn_reset_prod_total_a.setStyleSheet(btn_error_style)
        UI.btn_reset_prod_b1.setStyleSheet(btn_error_style)
        UI.btn_reset_prod_b2.setStyleSheet(btn_error_style)
        UI.btn_reset_prod_total_b.setStyleSheet(btn_error_style)
        UI.btn_reset_prod_a1.setText('Erro')
        UI.btn_reset_prod_a2.setText('Erro')
        UI.btn_reset_prod_total_a.setText('Erro')
        UI.btn_reset_prod_b1.setText('Erro')
        UI.btn_reset_prod_b2.setText('Erro')
        UI.btn_reset_prod_total_b.setText('Erro')
        UI.btn_reset_prod_a1.setEnabled(False)
        UI.btn_reset_prod_a2.setEnabled(False)
        UI.btn_reset_prod_total_a.setEnabled(False)
        UI.btn_reset_prod_b1.setEnabled(False)
        UI.btn_reset_prod_b2.setEnabled(False)
        UI.btn_reset_prod_total_b.setEnabled(False)

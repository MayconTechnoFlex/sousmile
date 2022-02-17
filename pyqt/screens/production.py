"""Module with all functions used on the ProductionScreen of the application"""

from ui_py.ui_gui import Ui_MainWindow

from utils.ctrl_plc import write_tag

UI: Ui_MainWindow

def define_buttons(receive_ui: Ui_MainWindow):
    """
    Define the buttons of the screen

    Params:
        receive_ui = main ui of the application
    """
    global UI
    UI = receive_ui
    UI.btn_reset_prod_a1.clicked.connect(lambda: reset_product("HMI.Production.PartsDoneA1"))
    UI.btn_reset_prod_a2.clicked.connect(lambda: reset_product("HMI.Production.PartsDoneA2"))
    UI.btn_reset_prod_b1.clicked.connect(lambda: reset_product("HMI.Production.PartsDoneB1"))
    UI.btn_reset_prod_b2.clicked.connect(lambda: reset_product("HMI.Production.PartsDoneB2"))
    UI.btn_reset_prod_total_a.clicked.connect(lambda: reset_product("HMI.Production.PartsDoneA1",
                                                                    "HMI.Production.PartsDoneA2"))
    UI.btn_reset_prod_total_b.clicked.connect(lambda: reset_product("HMI.Production.PartsDoneB1",
                                                                    "HMI.Production.PartsDoneB2"))

def reset_product(*tags: str):
    """
    Set 0 for all the tags passed

    Params:
        tags = one or more tags to be write with 0
    """
    for tag in tags:
        write_tag(tag, 0)

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
    except:
        pass


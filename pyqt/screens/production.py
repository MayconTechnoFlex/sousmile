from ui_py.ui_gui import Ui_MainWindow

from utils.ctrl_plc import write_tag

ui: Ui_MainWindow

def define_buttons(receive_ui: Ui_MainWindow):
    global ui
    ui = receive_ui
    ui.btn_reset_prod_a1.clicked.connect(lambda: reset_product("HMI.Production.PartsDoneA1"))
    ui.btn_reset_prod_a2.clicked.connect(lambda: reset_product("HMI.Production.PartsDoneA2"))
    ui.btn_reset_prod_b1.clicked.connect(lambda: reset_product("HMI.Production.PartsDoneB1"))
    ui.btn_reset_prod_b2.clicked.connect(lambda: reset_product("HMI.Production.PartsDoneB2"))
    ui.btn_reset_prod_total_a.clicked.connect(lambda: reset_product("HMI.Production.PartsDoneA1",
                                                                    "HMI.Production.PartsDoneA2"))
    ui.btn_reset_prod_total_b.clicked.connect(lambda: reset_product("HMI.Production.PartsDoneB1",
                                                                    "HMI.Production.PartsDoneB2"))

def reset_product(*tags: str):
    for tag in tags:
        write_tag(tag, 0)

def UpdateHMI(tag):
    global ui
    try:
        prodTag = tag["Production"]
        ui.lbl_PartsDoneA1.setText(str(prodTag["PartsDoneA1"]))
        ui.lbl_PartsDoneA2.setText(str(prodTag["PartsDoneA2"]))
        ui.lbl_PartsDoneSideA.setText(str(prodTag["PartDoneSideA"]))
        ui.lbl_TimeCutA1.setText(str(round(prodTag["TimeCutA1"], 2)))
        ui.lbl_TimeCutA2.setText(str(round(prodTag["TimeCutA2"], 2)))
        ui.lbl_TimeCutSideA.setText(str(round(prodTag["TimeCutSideA"], 2)))

        ui.lbl_PartsDoneB1.setText(str(prodTag["PartsDoneB1"]))
        ui.lbl_PartsDoneB2.setText(str(prodTag["PartsDoneB2"]))
        ui.lbl_PartsDoneSideB.setText(str(prodTag["PartDoneSideB"]))
        ui.lbl_TimeCutB1.setText(str(round(prodTag["TimeCutB1"], 2)))
        ui.lbl_TimeCutB2.setText(str(round(prodTag["TimeCutB2"], 2)))
        ui.lbl_TimeCutSideB.setText(str(round(prodTag["TimeCutSideB"], 2)))
    except:
        pass


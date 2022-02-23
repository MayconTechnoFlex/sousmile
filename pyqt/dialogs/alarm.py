from PyQt5.QtWidgets import QDialog
from PyQt5.QtCore import Qt
from ui_py.ui_alarm_dialog import Ui_Dialog


class AlarmDialog(QDialog):
    """
    Dialog that appears when a new alarm comes in
    """
    def __init__(self, parents=None):
        super(AlarmDialog, self).__init__(parents)
        self.setWindowFlag(Qt.WindowContextHelpButtonHint, False)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

    def show_dialog(self, show_alarm_screen):
        # fazer validações para adicionar alarme aqui
        self.show_alarm_screen = show_alarm_screen
        self.define_buttons()
        self.exec_()

    def closeEvent(self, event):
        # limpar lista de alarmes
        self.ui.alarm_list_widget.clear()

    def go_to_alarms(self):
        self.close()
        self.show_alarm_screen()

    def cancel(self):
        self.close()

    def define_buttons(self):
        self.ui.btn_go_alarm_screen.clicked.connect(self.go_to_alarms)
        self.ui.btn_cancel.clicked.connect(self.cancel)

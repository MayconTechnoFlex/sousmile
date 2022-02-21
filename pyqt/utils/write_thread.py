from PyQt5.QtCore import QObject, pyqtSignal, QThread, Qt
from PyQt5.QtWidgets import QApplication, QDialog, QLineEdit, QPushButton

from utils.ctrl_plc import write_tag, read_tags
from utils.Types import TagTypes


class ThreadSetResetButton(QThread):
    def __init__(self, button: QPushButton, tag_name: str):
        super(ThreadSetResetButton, self).__init__()
        self.button = button
        self.tag_name = tag_name

    def run(self):
        QApplication.setOverrideCursor(Qt.WaitCursor)
        self.button.setEnabled(False)
        try:
            value = read_tags(self.tag_name)
            if value:
                write_tag(self.tag_name, 0)
            else:
                write_tag(self.tag_name, 1)
        except Exception as e:
            print(e)
        QApplication.restoreOverrideCursor()
        self.button.setEnabled(True)

class Thread_LineEdit(QThread):
    def __init__(self, tag_name: str, dialog: QDialog, widget: QLineEdit, data_type: TagTypes = "string"):
        super(Thread_LineEdit, self).__init__()
        self.tag_name = tag_name
        self.dialog = dialog
        self.widget = widget
        self.data_type = data_type

    def run(self):
        QApplication.setOverrideCursor(Qt.WaitCursor)
        self.dialog.setEnabled(False)

        if self.data_type == "string":
            data = str(self.widget.text())
        elif self.data_type == "int":
            data = int(self.widget.text())
        elif self.data_type == "float":
            data = float(self.widget.text())
        else:
            data = None

        try:
            write_tag(self.tag_name, data)
        except Exception as e:
            print(f"{e} - write_LineEdit")
        self.widget.clear()
        self.dialog.close()

        QApplication.restoreOverrideCursor()

        self.dialog.setEnabled(True)
        self.finished.emit()

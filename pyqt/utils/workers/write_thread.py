"""Threads para escrever no CLP através de dialog"""
#######################################################################################################
# Importações
#######################################################################################################
from pycomm3 import CommError
from PyQt5.QtCore import QThread, Qt
from PyQt5.QtWidgets import QApplication, QDialog, QLineEdit

from utils.functions.ctrl_plc import write_tag, read_tags
from utils.Types import TagTypes
#######################################################################################################
# Threads
#######################################################################################################
class Thread_Dialogs_NoLineEdit(QThread):
    def __init__(self, dialog: QDialog, tag_name: str):
        """
        Escreve no CLP 1 caso esteja escrito 0 e vice-versa

        :param dialog: Dialog que executou a thread
        :param tag_name: String com o nome da tag
        """
        super(Thread_Dialogs_NoLineEdit, self).__init__()
        self.dialog = dialog
        self.tag_name = tag_name

    def run(self):
        QApplication.setOverrideCursor(Qt.WaitCursor)
        self.dialog.setEnabled(False)
        try:
            value = read_tags(self.tag_name)
            if type(value) is CommError:
                raise Exception("Erro de Conexão")
            if value:
                write_tag(self.tag_name, 0)
            else:
                write_tag(self.tag_name, 1)

        except Exception as e:
            print(e)
        finally:
            QApplication.restoreOverrideCursor()
            self.dialog.setEnabled(True)
            self.dialog.close()
#######################################################################################################
class Thread_LineEdit(QThread):
    def __init__(self, tag_name: str, dialog: QDialog, lineEdit: QLineEdit, data_type: TagTypes = "string"):
        """
        Escreve o valor do LineEdit no CLP

        :param tag_name: String com o nome da tag
        :param dialog: Dialog que executou a thread
        :param lineEdit: LineEdit do dialog
        :param data_type: Tipo de dado que será enviado para o CLP
        """
        super(Thread_LineEdit, self).__init__()
        self.tag_name = tag_name
        self.dialog = dialog
        self.lineEdit = lineEdit
        self.data_type = data_type

    def run(self):
        QApplication.setOverrideCursor(Qt.WaitCursor)
        self.dialog.setEnabled(False)

        try:
            if self.data_type == "string":
                data = str(self.lineEdit.text())
            elif self.data_type == "int":
                data = int(self.lineEdit.text())
            elif self.data_type == "float":
                data = float(self.lineEdit.text())
            else:
                raise Exception("Tipo incorreto foi passado")
        except Exception as e:
            print(f"{e} - Thread_LineEdit")
            data = None

        try:
            if not data or data == '':
                raise Exception("Campo vazio")
            else:
                ret = write_tag(self.tag_name, data)
                if type(ret) is CommError:
                    raise Exception("Erro de Conexão")
        except Exception as e:
            print(f"{e} - Thread_LineEdit")
        finally:
            self.lineEdit.clear()
            self.dialog.close()

            QApplication.restoreOverrideCursor()

            self.dialog.setEnabled(True)
            self.finished.emit()
#######################################################################################################

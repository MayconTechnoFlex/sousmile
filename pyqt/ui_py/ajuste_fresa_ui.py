# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\pyqt\ui\ajuste_frase_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(412, 340)
        Dialog.setMinimumSize(QtCore.QSize(412, 340))
        Dialog.setMaximumSize(QtCore.QSize(412, 340))
        Dialog.setStyleSheet("* {margin:0; padding:0; border: 0}\n"
"\n"
"QDialog{background-color:#efefef}\n"
"\n"
"QPushButton{\n"
"    background-color: #ffdf00;\n"
"    border: 0;\n"
"border-radius:25; padding:0; margin:0\n"
"}\n"
"QPushButton::disabled{background-color:#cbcbcb}\n"
"QPushButton:hover{ background-color: #f1d100}\n"
"QPushButton:pressed{background-color:#dfc200 }\n"
"\n"
"QLineEdit{\n"
"background-color: white;\n"
"border: 2px solid #b0b0b0;\n"
"border-radius: 18\n"
"}\n"
"QLineEdit {\\ncolor: black; \\nbackground-color: white;\\nborder-width: 1px;\\nborder-radius: 25px;\\n}\n"
"")
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(Dialog)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Equinox Bold")
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.verticalLayout.addWidget(self.frame)
        self.frame_5 = QtWidgets.QFrame(Dialog)
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_5)
        self.horizontalLayout_4.setContentsMargins(15, 0, 15, 0)
        self.horizontalLayout_4.setSpacing(5)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)
        self.label_4 = QtWidgets.QLabel(self.frame_5)
        font = QtGui.QFont()
        font.setFamily("Equinox Bold")
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_4.addWidget(self.label_4)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem1)
        self.valor_atual = QtWidgets.QLabel(self.frame_5)
        font = QtGui.QFont()
        font.setFamily("Equinox Bold")
        font.setPointSize(12)
        self.valor_atual.setFont(font)
        self.valor_atual.setAlignment(QtCore.Qt.AlignCenter)
        self.valor_atual.setObjectName("valor_atual")
        self.horizontalLayout_4.addWidget(self.valor_atual)
        self.label_5 = QtWidgets.QLabel(self.frame_5)
        font = QtGui.QFont()
        font.setFamily("Equinox Bold")
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_4.addWidget(self.label_5)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem2)
        self.verticalLayout.addWidget(self.frame_5)
        self.frame_2 = QtWidgets.QFrame(Dialog)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(5)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.le_code = QtWidgets.QLineEdit(self.frame_2)
        self.le_code.setMinimumSize(QtCore.QSize(90, 50))
        self.le_code.setMaximumSize(QtCore.QSize(90, 50))
        font = QtGui.QFont()
        font.setFamily("Equinox Bold")
        font.setPointSize(14)
        self.le_code.setFont(font)
        self.le_code.setText("")
        self.le_code.setAlignment(QtCore.Qt.AlignCenter)
        self.le_code.setObjectName("le_code")
        self.horizontalLayout_2.addWidget(self.le_code)
        self.label = QtWidgets.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setFamily("Equinox Bold")
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem4)
        self.verticalLayout.addWidget(self.frame_2)
        self.frame_4 = QtWidgets.QFrame(Dialog)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_4)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.frame_4)
        font = QtGui.QFont()
        font.setFamily("Equinox Bold")
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.verticalLayout.addWidget(self.frame_4)
        self.frame_3 = QtWidgets.QFrame(Dialog)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout.setContentsMargins(15, 0, 15, 0)
        self.horizontalLayout.setSpacing(15)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btn_confirm = QtWidgets.QPushButton(self.frame_3)
        self.btn_confirm.setMinimumSize(QtCore.QSize(0, 50))
        self.btn_confirm.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setFamily("Equinox Bold")
        font.setPointSize(14)
        self.btn_confirm.setFont(font)
        self.btn_confirm.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/assets/icons/sharp_check_black_48dp.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_confirm.setIcon(icon)
        self.btn_confirm.setIconSize(QtCore.QSize(25, 25))
        self.btn_confirm.setAutoDefault(False)
        self.btn_confirm.setDefault(True)
        self.btn_confirm.setObjectName("btn_confirm")
        self.horizontalLayout.addWidget(self.btn_confirm)
        self.btn_cancel = QtWidgets.QPushButton(self.frame_3)
        self.btn_cancel.setMinimumSize(QtCore.QSize(0, 50))
        self.btn_cancel.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setFamily("Equinox Bold")
        font.setPointSize(14)
        self.btn_cancel.setFont(font)
        self.btn_cancel.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_cancel.setFocusPolicy(QtCore.Qt.TabFocus)
        self.btn_cancel.setStyleSheet("* {\n"
"background-color: #eece00\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: #ddbd00\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color: #ccac00\n"
"}\n"
"QPushButton::disabled{background-color:#cbcbcb}")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/assets/icons/sharp_close_black_48dp.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_cancel.setIcon(icon1)
        self.btn_cancel.setIconSize(QtCore.QSize(25, 25))
        self.btn_cancel.setAutoDefault(False)
        self.btn_cancel.setObjectName("btn_cancel")
        self.horizontalLayout.addWidget(self.btn_cancel)
        self.verticalLayout.addWidget(self.frame_3)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Ajuste da fresa"))
        self.label_2.setText(_translate("Dialog", "Digite abaixo um tamanho\n"
"para a fresa:"))
        self.label_4.setText(_translate("Dialog", "Valor atual:"))
        self.valor_atual.setText(_translate("Dialog", "0.0"))
        self.label_5.setText(_translate("Dialog", "mm"))
        self.le_code.setPlaceholderText(_translate("Dialog", "00000"))
        self.label.setText(_translate("Dialog", "mm"))
        self.label_3.setText(_translate("Dialog", "Cuidado! O robô se moverá\n"
"para ajustar a fresa!"))
        self.btn_confirm.setText(_translate("Dialog", "Confirmar"))
        self.btn_cancel.setText(_translate("Dialog", "Cancelar"))
import ui_py.icons_rc

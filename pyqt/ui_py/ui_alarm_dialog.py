# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\pyqt\ui\alarm_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1134, 652)
        Dialog.setStyleSheet("#frame, #frame_3 { background-color: white}\n"
"#line, #line_2 {border: 3px solid #b0b0b0; margin:0; padding:0}\n"
"QPushButton{\n"
"background-color:#ffdf00;\n"
"border-radius: 30;\n"
"}\n"
"QPushButton:hover{ background-color: #f1d100}\n"
"QPushButton:pressed{background-color:#dfc200 }\n"
"QPushButton:disabled{background-color:#cbcbcb }")
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(Dialog)
        self.frame.setMinimumSize(QtCore.QSize(0, 80))
        self.frame.setMaximumSize(QtCore.QSize(16777215, 80))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Equinox Bold")
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.verticalLayout.addWidget(self.frame)
        self.line = QtWidgets.QFrame(Dialog)
        self.line.setMinimumSize(QtCore.QSize(0, 2))
        self.line.setMaximumSize(QtCore.QSize(16777215, 2))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.frame_2 = QtWidgets.QFrame(Dialog)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setContentsMargins(25, 10, 25, 10)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame_138 = QtWidgets.QFrame(self.frame_2)
        self.frame_138.setStyleSheet("#frame_138{\n"
"background-color: #989898; border-radius: 50;\n"
"padding:0; margin:0; border: 2px solid #888888\n"
"}")
        self.frame_138.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_138.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_138.setObjectName("frame_138")
        self.verticalLayout_21 = QtWidgets.QVBoxLayout(self.frame_138)
        self.verticalLayout_21.setContentsMargins(35, 35, 35, 35)
        self.verticalLayout_21.setSpacing(35)
        self.verticalLayout_21.setObjectName("verticalLayout_21")
        self.frame_139 = QtWidgets.QFrame(self.frame_138)
        self.frame_139.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.frame_139.setStyleSheet("#frame_139{\n"
"background-color: lightgray; padding:20; margin:0; border:0;\n"
"border-radius: 15;\n"
"border: 5px solid #888888\n"
"}\n"
"\n"
"QFrame{\n"
"padding:0; margin:0; border: 4px solid #ffdf00\n"
"}\n"
"")
        self.frame_139.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_139.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_139.setObjectName("frame_139")
        self.verticalLayout_22 = QtWidgets.QVBoxLayout(self.frame_139)
        self.verticalLayout_22.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_22.setSpacing(0)
        self.verticalLayout_22.setObjectName("verticalLayout_22")
        self.frame_141 = QtWidgets.QFrame(self.frame_139)
        self.frame_141.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_141.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_141.setObjectName("frame_141")
        self.verticalLayout_23 = QtWidgets.QVBoxLayout(self.frame_141)
        self.verticalLayout_23.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_23.setSpacing(0)
        self.verticalLayout_23.setObjectName("verticalLayout_23")
        self.alarm_list_widget = QtWidgets.QTableWidget(self.frame_141)
        font = QtGui.QFont()
        font.setFamily("Equinox Bold")
        font.setPointSize(12)
        self.alarm_list_widget.setFont(font)
        self.alarm_list_widget.setFocusPolicy(QtCore.Qt.NoFocus)
        self.alarm_list_widget.setStyleSheet(" * { border:0; margin: 0; padding:0}\n"
"\n"
"QHeaderView::section {\n"
"    padding: 5 20;\n"
"    border: 1px solid #ffdf00;\n"
"    border-bottom: 2px solid #ffdf00;\n"
"    border-top: 0;\n"
"    background-color: white\n"
"}\n"
"\n"
"QHeaderView::up-arrow, QHeaderView::down-arrow {\n"
"    color: black;\n"
"    width: 25; height: 25;\n"
"    subcontrol-position: left;\n"
"    \n"
"}\n"
"\n"
"QTableWidget {\n"
"    gridline-color: #ffdf00;\n"
"}\n"
"\n"
"QTableWidget::item {\n"
"    border: 1px solid #ffdf00;\n"
"    border-right: 0; border-left: 0;\n"
"    padding: 0 20;\n"
"}\n"
"\n"
"QTableWidget::item:selected{\n"
"    background-color: #ababab\n"
"}")
        self.alarm_list_widget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.alarm_list_widget.setAlternatingRowColors(False)
        self.alarm_list_widget.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.alarm_list_widget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.alarm_list_widget.setRowCount(0)
        self.alarm_list_widget.setColumnCount(2)
        self.alarm_list_widget.setObjectName("alarm_list_widget")
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignVCenter)
        font = QtGui.QFont()
        font.setFamily("Equinox Bold")
        font.setPointSize(16)
        item.setFont(font)
        self.alarm_list_widget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignVCenter)
        font = QtGui.QFont()
        font.setFamily("Equinox Bold")
        font.setPointSize(16)
        item.setFont(font)
        self.alarm_list_widget.setHorizontalHeaderItem(1, item)
        self.alarm_list_widget.horizontalHeader().setCascadingSectionResizes(False)
        self.alarm_list_widget.horizontalHeader().setDefaultSectionSize(300)
        self.alarm_list_widget.horizontalHeader().setHighlightSections(False)
        self.alarm_list_widget.horizontalHeader().setSortIndicatorShown(True)
        self.alarm_list_widget.horizontalHeader().setStretchLastSection(True)
        self.alarm_list_widget.verticalHeader().setVisible(False)
        self.alarm_list_widget.verticalHeader().setHighlightSections(False)
        self.alarm_list_widget.verticalHeader().setSortIndicatorShown(True)
        self.verticalLayout_23.addWidget(self.alarm_list_widget)
        self.verticalLayout_22.addWidget(self.frame_141)
        self.verticalLayout_21.addWidget(self.frame_139)
        self.verticalLayout_2.addWidget(self.frame_138)
        self.verticalLayout.addWidget(self.frame_2)
        self.line_2 = QtWidgets.QFrame(Dialog)
        self.line_2.setMinimumSize(QtCore.QSize(0, 2))
        self.line_2.setMaximumSize(QtCore.QSize(16777215, 2))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout.addWidget(self.line_2)
        self.frame_3 = QtWidgets.QFrame(Dialog)
        self.frame_3.setMinimumSize(QtCore.QSize(0, 80))
        self.frame_3.setMaximumSize(QtCore.QSize(16777215, 100))
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout_2.setContentsMargins(0, 10, 0, 20)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(224, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.btn_go_alarm_screen = QtWidgets.QPushButton(self.frame_3)
        self.btn_go_alarm_screen.setMinimumSize(QtCore.QSize(225, 65))
        self.btn_go_alarm_screen.setMaximumSize(QtCore.QSize(225, 65))
        font = QtGui.QFont()
        font.setFamily("Equinox Bold")
        font.setPointSize(14)
        self.btn_go_alarm_screen.setFont(font)
        self.btn_go_alarm_screen.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_go_alarm_screen.setObjectName("btn_go_alarm_screen")
        self.horizontalLayout_2.addWidget(self.btn_go_alarm_screen)
        spacerItem1 = QtWidgets.QSpacerItem(225, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.btn_cancel = QtWidgets.QPushButton(self.frame_3)
        self.btn_cancel.setMinimumSize(QtCore.QSize(225, 65))
        self.btn_cancel.setMaximumSize(QtCore.QSize(225, 65))
        font = QtGui.QFont()
        font.setFamily("Equinox Bold")
        font.setPointSize(14)
        self.btn_cancel.setFont(font)
        self.btn_cancel.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
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
        self.btn_cancel.setObjectName("btn_cancel")
        self.horizontalLayout_2.addWidget(self.btn_cancel)
        spacerItem2 = QtWidgets.QSpacerItem(224, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.verticalLayout.addWidget(self.frame_3)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Alarme Novo!"))
        self.alarm_list_widget.setSortingEnabled(True)
        item = self.alarm_list_widget.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "TIME MESSAGE"))
        item = self.alarm_list_widget.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "MESSAGE"))
        self.btn_go_alarm_screen.setText(_translate("Dialog", "Ir para tela\n"
"de alarmes"))
        self.btn_cancel.setText(_translate("Dialog", "Fechar"))
import ui_py.icons_rc

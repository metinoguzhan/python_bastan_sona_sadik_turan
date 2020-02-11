# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '24_Masaustu_Uygulamasi_PyQt5/_comboboxForm.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(643, 391)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.cbSehirler = QtWidgets.QComboBox(self.centralwidget)
        self.cbSehirler.setGeometry(QtCore.QRect(40, 60, 271, 41))
        self.cbSehirler.setObjectName("cbSehirler")
        self.lblResult = QtWidgets.QLabel(self.centralwidget)
        self.lblResult.setGeometry(QtCore.QRect(340, 67, 181, 31))
        self.lblResult.setText("")
        self.lblResult.setObjectName("lblResult")
        self.btnGetItem = QtWidgets.QPushButton(self.centralwidget)
        self.btnGetItem.setGeometry(QtCore.QRect(40, 140, 271, 41))
        self.btnGetItem.setObjectName("btnGetItem")
        self.btnLoadItem = QtWidgets.QPushButton(self.centralwidget)
        self.btnLoadItem.setGeometry(QtCore.QRect(340, 140, 271, 41))
        self.btnLoadItem.setObjectName("btnLoadItem")
        self.btnClearItem = QtWidgets.QPushButton(self.centralwidget)
        self.btnClearItem.setGeometry(QtCore.QRect(40, 200, 271, 41))
        self.btnClearItem.setObjectName("btnClearItem")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 643, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btnGetItem.setText(_translate("MainWindow", "Get Item"))
        self.btnLoadItem.setText(_translate("MainWindow", "Load Items"))
        self.btnClearItem.setText(_translate("MainWindow", "Clear Item"))

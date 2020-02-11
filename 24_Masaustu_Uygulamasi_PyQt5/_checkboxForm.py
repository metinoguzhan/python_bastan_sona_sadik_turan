# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '24_Masaustu_Uygulamasi_PyQt5/_checkbox.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.btnHobilerSecilenleriAl = QtWidgets.QPushButton(self.centralwidget)
        self.btnHobilerSecilenleriAl.setGeometry(QtCore.QRect(190, 310, 191, 71))
        self.btnHobilerSecilenleriAl.setObjectName("btnHobilerSecilenleriAl")
        self.lblHobiler = QtWidgets.QLabel(self.centralwidget)
        self.lblHobiler.setGeometry(QtCore.QRect(200, 400, 161, 141))
        self.lblHobiler.setText("")
        self.lblHobiler.setObjectName("lblHobiler")
        self.groupHobiler = QtWidgets.QGroupBox(self.centralwidget)
        self.groupHobiler.setGeometry(QtCore.QRect(180, 50, 201, 261))
        self.groupHobiler.setObjectName("groupHobiler")
        self.widget = QtWidgets.QWidget(self.groupHobiler)
        self.widget.setGeometry(QtCore.QRect(6, 20, 191, 201))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.cbSinema = QtWidgets.QCheckBox(self.widget)
        self.cbSinema.setObjectName("cbSinema")
        self.verticalLayout.addWidget(self.cbSinema)
        self.cbKitapOkumak = QtWidgets.QCheckBox(self.widget)
        self.cbKitapOkumak.setObjectName("cbKitapOkumak")
        self.verticalLayout.addWidget(self.cbKitapOkumak)
        self.cbSpor = QtWidgets.QCheckBox(self.widget)
        self.cbSpor.setObjectName("cbSpor")
        self.verticalLayout.addWidget(self.cbSpor)
        self.groupDersler = QtWidgets.QGroupBox(self.centralwidget)
        self.groupDersler.setGeometry(QtCore.QRect(400, 50, 201, 261))
        self.groupDersler.setObjectName("groupDersler")
        self.layoutWidget = QtWidgets.QWidget(self.groupDersler)
        self.layoutWidget.setGeometry(QtCore.QRect(6, 20, 191, 201))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.cbWebTasarim = QtWidgets.QCheckBox(self.layoutWidget)
        self.cbWebTasarim.setObjectName("cbWebTasarim")
        self.verticalLayout_2.addWidget(self.cbWebTasarim)
        self.cbProgramlama = QtWidgets.QCheckBox(self.layoutWidget)
        self.cbProgramlama.setObjectName("cbProgramlama")
        self.verticalLayout_2.addWidget(self.cbProgramlama)
        self.cbMatematik = QtWidgets.QCheckBox(self.layoutWidget)
        self.cbMatematik.setObjectName("cbMatematik")
        self.verticalLayout_2.addWidget(self.cbMatematik)
        self.btnDerslerSecilenleriAl = QtWidgets.QPushButton(self.centralwidget)
        self.btnDerslerSecilenleriAl.setGeometry(QtCore.QRect(400, 310, 191, 71))
        self.btnDerslerSecilenleriAl.setObjectName("btnDerslerSecilenleriAl")
        self.lblDersler = QtWidgets.QLabel(self.centralwidget)
        self.lblDersler.setGeometry(QtCore.QRect(420, 400, 161, 141))
        self.lblDersler.setText("")
        self.lblDersler.setObjectName("lblDersler")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
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
        self.btnHobilerSecilenleriAl.setText(_translate("MainWindow", "Seçilenleri Al"))
        self.groupHobiler.setTitle(_translate("MainWindow", "GroupBox"))
        self.cbSinema.setText(_translate("MainWindow", "Sinema"))
        self.cbKitapOkumak.setText(_translate("MainWindow", "Kitap okumak"))
        self.cbSpor.setText(_translate("MainWindow", "Spor"))
        self.groupDersler.setTitle(_translate("MainWindow", "GroupBox"))
        self.cbWebTasarim.setText(_translate("MainWindow", "Web Tasarım"))
        self.cbProgramlama.setText(_translate("MainWindow", "Programlama"))
        self.cbMatematik.setText(_translate("MainWindow", "Matematik"))
        self.btnDerslerSecilenleriAl.setText(_translate("MainWindow", "Seçilenleri Al"))

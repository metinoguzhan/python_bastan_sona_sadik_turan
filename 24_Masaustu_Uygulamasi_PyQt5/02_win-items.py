import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication,QMainWindow,QToolTip
from PyQt5.QtGui import QIcon

'''
    QLabel
    QComboBox
    QCheckBox
    QRadioButton
    QPushButton
    QTableWidget
    QLineEdit
    QSlider
    QProgressBar
'''



def window():
    app = QApplication(sys.argv)
    win = QMainWindow()

    win.setGeometry(200,200,500,500)
    win.setWindowTitle("First Application")
    win.setWindowIcon(QIcon("24_Masaustu_Uygulamasi_PyQt5/icon.png"))
    win.setToolTip("This is a <b>QPushButton</b> widget")

    lbl_name = QtWidgets.QLabel(win)
    lbl_name.move(50,30)
    lbl_name.setText("Adınız : ")

    lbl_surname = QtWidgets.QLabel(win)
    lbl_surname.move(50,70)
    lbl_surname.setText("Soyadınız : ")

    txt_name = QtWidgets.QLineEdit(win)
    txt_name.move(150,30)

    txt_surname = QtWidgets.QLineEdit(win)
    txt_surname.move(150,70)
    
    def clicked(self):
        print("Butona tıklandı. Name : " + txt_name.text() + "  Surname : " + txt_surname.text())

    btn_save = QtWidgets.QPushButton(win)
    btn_save.setText("Kaydet")
    btn_save.move(150,110)
    btn_save.clicked.connect(clicked)

    win.show()
    sys.exit(app.exec_())

window()
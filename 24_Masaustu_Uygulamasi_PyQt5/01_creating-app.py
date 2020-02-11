import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication,QMainWindow,QToolTip
from PyQt5.QtGui import QIcon


def window():
    app = QApplication(sys.argv)
    win = QMainWindow()

    win.setWindowTitle("First Application")
    win.setGeometry(200,200,700,700)
    win.setWindowIcon(QIcon("24_Masaustu_Uygulamasi_PyQt5/icon.png"))
    win.setToolTip("This is a <b>QPushButton</b> widget")

    
    win.show()
    sys.exit(app.exec_())

window()
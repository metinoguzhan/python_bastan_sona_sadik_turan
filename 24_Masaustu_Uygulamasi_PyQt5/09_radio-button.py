from PyQt5 import QtWidgets
import sys
from _radioButtonForm import Ui_MainWindow

class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super(Window,self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.radioTurkiye.setChecked(True)
        self.ui.radioIlkokul.setChecked(True)
        
        self.ui.radioTurkiye.toggled.connect(self.onClickedUlke)
        self.ui.radioAzerbeycan.toggled.connect(self.onClickedUlke)
        self.ui.radioAlmanya.toggled.connect(self.onClickedUlke)
        self.ui.radioYunanistan.toggled.connect(self.onClickedUlke)

        self.ui.radioIlkokul.toggled.connect(self.onClickedEgitim)
        self.ui.radioLise.toggled.connect(self.onClickedEgitim)
        self.ui.radioUniversite.toggled.connect(self.onClickedEgitim)
        self.ui.radioYuksekLisans.toggled.connect(self.onClickedEgitim)

        self.ui.btnUlke.clicked.connect(self.getSelectedUlke)
        self.ui.btnEgitim.clicked.connect(self.getSelectedEgitim)
    def onClickedUlke(self):
        rb = self.sender()
        if rb.isChecked():
            print('Seçilen ülke: ' + rb.text())
    
    def onClickedEgitim(self):
        rb = self.sender()
        if rb.isChecked():
            print("Seçilen eğitim: " + rb.text())

    def getSelectedUlke(self):
        items = self.ui.groupBoxUlke.findChildren(QtWidgets.QRadioButton)
        for item in items:
            if item.isChecked():
                self.ui.lblUlke.setText(item.text())
    
    def getSelectedEgitim(self):
        items = self.ui.groupBoxEgitim.findChildren(QtWidgets.QRadioButton)
        for item in items:
            if item.isChecked():
                self.ui.lblEgitim.setText(item.text())

app = QtWidgets.QApplication(sys.argv)
win = Window()
win.show()
sys.exit(app.exec_())
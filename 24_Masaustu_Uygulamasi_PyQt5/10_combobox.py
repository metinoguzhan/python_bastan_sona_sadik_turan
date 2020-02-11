from PyQt5 import QtWidgets
import sys
from _comboboxForm import Ui_MainWindow

class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super(Window,self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # self.ui.cbSehirler.addItem('Ankara')
        # self.ui.cbSehirler.addItem('İstanbul')
        # self.ui.cbSehirler.addItem('Kocaeli')

        combo = self.ui.cbSehirler
        combo.addItem('Ankara')
        combo.addItem('İstanbul')
        combo.addItem('Kocaeli')
        
        self.ui.btnLoadItem.clicked.connect(self.loadItems)
        self.ui.btnGetItem.clicked.connect(self.getItem)
        self.ui.cbSehirler.currentIndexChanged.connect(self.selectedChangedIndex)
        self.ui.cbSehirler.currentIndexChanged[str].connect(self.selectedChangedText)
        self.ui.btnClearItem.clicked.connect(self.clearItems)

    def clearItems(self):
        self.ui.cbSehirler.clear()
        
    def loadItems(self):
        sehirler = ['Adana','İzmir','Rize']
        self.ui.cbSehirler.addItems(sehirler)
    
    def getItem(self):
        secilen = self.ui.cbSehirler.currentText()
        index = self.ui.cbSehirler.currentIndex()
        count = self.ui.cbSehirler.count()
        
        for index in range(count):
            print(self.ui.cbSehirler.itemText(index))
            
        # print(index,secilen)
        # print(count)
        self.ui.lblResult.setText("Seçilen şehir : " + secilen)

    def selectedChangedIndex(self,index):
        print(index)

    def selectedChangedText(self,text):
        print(text)



app = QtWidgets.QApplication(sys.argv)
win = Window()
win.show()
sys.exit(app.exec_())
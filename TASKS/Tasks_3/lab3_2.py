import sys

import PySide6.QtWidgets as psqw
import PySide6.QtCore as psqc

class Mak(psqw.QWidget):

    def __init__(self, widget):
        super(Mak, self).__init__()

class MainWindow(psqw.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle('Window1')

        self.setFixedSize(psqc.QSize(900, 600))

        tabs = psqw.QTabWidget()
        tabs.setTabPosition(psqw.QTabWidget.West)
        tabs.setMovable(True)

        # task 1
        self.n = 1
        wid = psqw.QWidget()
        hbox = psqw.QHBoxLayout()

        self.label = psqw.QLabel("Hello")
        font = self.label.font()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setAlignment(psqc.Qt.AlignLeft | psqc.Qt.AlignVCenter)

        self.check = psqw.QCheckBox('lock_sign_change')
        self.check.setCheckState(psqc.Qt.Checked)

        hbox.addWidget(self.label)
        hbox.addWidget(self.check)

        wid.setLayout(hbox)
        tabs.addTab(wid, "one")

        # task 2

        wid2 = psqw.QWidget()
        hbox2 = psqw.QGridLayout()

        for i in range(30):
            for j in range(30):
                button = psqw.QPushButton()
                hbox2.addWidget(button, i, j)

        wid2.setLayout(hbox2)
        tabs.addTab(wid2, "two")

        # task 3

        self.wid3 = psqw.QWidget()
        self.hbox3 = psqw.QVBoxLayout()

        button3 = psqw.QPushButton()
        button3.clicked.connect(self.hlayout)
        

        self.wid3.setLayout(self.hbox3)
        tabs.addTab(self.wid3, "three")

        self.setCentralWidget(tabs)
        self.hbox3.addWidget(button3)

    def hlayout(self):
        hbox = psqw.QHBoxLayout()
        self.wid3.layout().addLayout(hbox)

        button3 = self.sender()
        button3.setEnabled(False)

        self.n += 1
      
        for i in range(self.n):
            button3 = psqw.QPushButton()
            button3.clicked.connect(self.hlayout)
            button3.clicked.connect(self.btn_click)
            hbox.addWidget(button3)
        
            
           
           


    def btn_click(self):
        button3 = self.sender()
        button3.setEnabled(False)
        

app = psqw.QApplication(sys.argv)
window = MainWindow()
window.show()

app.exec_()
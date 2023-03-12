import sys

import PySide6.QtWidgets as psqw
import PySide6.QtCore as psqc

class Mak(psqw.QWidget):

    def __init__(self, widget):
        super(Mak, self).__init__()

class MainWindow(psqw.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle('Я окно')

        self.setFixedSize(psqc.QSize(900, 600))

        tabs = psqw.QTabWidget()
        tabs.setTabPosition(psqw.QTabWidget.West)
        tabs.setMovable(True)

        wid = psqw.QWidget()
        hbox = psqw.QHBoxLayout()

        self.label = psqw.QLabel("Привет")
        font = self.label.font()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setAlignment(psqc.Qt.AlignLeft | psqc.Qt.AlignVCenter)

        self.check = psqw.QCheckBox('Заблокировать')
        self.check.setCheckState(psqc.Qt.Checked)

        hbox.addWidget(self.label)
        hbox.addWidget(self.check)

        wid.setLayout(hbox)

        tabs.addTab(wid, "one")

        self.setCentralWidget(tabs)

app = psqw.QApplication(sys.argv)
window = MainWindow()
window.show()

app.exec_()
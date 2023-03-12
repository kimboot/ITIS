import PySide6.QtWidgets as psqw
import PySide6.QtCore as psqc

class MainWindow(psqw.QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Window1')

        self.setFixedSize(psqc.QSize(900, 600))

        self.button1 = psqw.QPushButton('Button1')
        self.button2 = psqw.QPushButton('Button2')
        self.button3 = psqw.QPushButton('Button3')


        layout = psqw.QVBoxLayout()
        layout.addWidget(self.button1)
        layout.addWidget(self.button2)
        layout.addWidget(self.button3)

        container = psqw.QWidget()
        container.setLayout(layout)

        self.setCentralWidget(container)

class NewWindow(psqw.QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Window2')

        self.setFixedSize(psqc.QSize(400, 200))


app = psqw.QApplication()

window1 = MainWindow()
window1.show()

window2 = NewWindow()
window2.show()


app.exec_()
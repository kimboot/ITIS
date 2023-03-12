import PySide6.QtWidgets as psqw
import PySide6.QtCore as psqc

class MainWindow(psqw.QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Window3')

        self.setFixedSize(psqc.QSize(900, 600))

        self.button = psqw.QPushButton('Button1')
        self.button.setFixedSize(psqc.QSize(900,100))
        self.button.clicked.connect(self.the_button_was_clicked)

        self.setCentralWidget(self.button)
    
    def the_button_was_clicked(self):
        self.button.setText('Hello world')
        self.button.setEnabled(False)
        


app = psqw.QApplication()

window = MainWindow()
window.show()


app.exec_()
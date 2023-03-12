import PySide6.QtWidgets as psqw
import PySide6.QtCore as psqc

class MainWindow(psqw.QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Я окно')

        self.setMinimumSize(psqc.QSize(400, 200))
        self.setMaximumSize(psqc.QSize(800, 600))

        button = psqw.QPushButton('Не нажимай на эту кнопку.')
        
        button.setFixedSize(psqc.QSize(400,100))

        self.setCentralWidget(button)


app = psqw.QApplication()

window = MainWindow()
window.show()

app.exec_()
import PySide6.QtWidgets as psqw
import PySide6.QtCore as psqc
import random

class MainWindow(psqw.QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Я окно')

        self.titles = ['Что?', 'Не нажмай', 'Ты окно?', 'Отстань']

        self.setFixedSize(psqc.QSize(900, 600))

        self.button1 = psqw.QPushButton('Поменять заголовок')
        self.button2 = psqw.QPushButton('Ошибка')
        self.button3 = psqw.QPushButton('Закрыть')

        layout = psqw.QVBoxLayout()
        layout.addWidget(self.button1)
        layout.addWidget(self.button2)
        layout.addWidget(self.button3)

        container = psqw.QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        self.button1.clicked.connect(self.change_title1)
        self.button2.clicked.connect(self.error2)
        self.button3.clicked.connect(self.close3)

        
    def change_title1(self):
        self.setWindowTitle(random.choice(self.titles))

    def error2(self):
        if self.button1.isEnabled() and self.button3.isEnabled():
            self.setWindowTitle('Что-то пошло не так')
            self.button1.setEnabled(False)
            self.button3.setEnabled(False)
        else:
            self.setWindowTitle('Я окно')
            self.button1.setEnabled(True)
            self.button3.setEnabled(True)

    def close3(self):
        self.close()


app = psqw.QApplication()

window = MainWindow()
window.show()

app.exec_()
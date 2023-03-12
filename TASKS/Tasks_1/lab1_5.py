import PySide6.QtWidgets as psqw
import PySide6.QtCore as psqc
import PySide6.QtGui as psqv

class MainWindow(psqw.QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Window1')

        self.setFixedSize(psqc.QSize(900, 600))

        self.label1 = psqw.QLabel('left')
        self.label2 = psqw.QLabel('mid')
        self.label3 = psqw.QLabel('right')

        layout = psqw.QVBoxLayout()
        layout.addWidget(self.label1)
        layout.addWidget(self.label2)
        layout.addWidget(self.label3)

        container = psqw.QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def mousePressEvent(self, e):
        if e.button() == psqc.Qt.LeftButton:
            self.label1.setText('Pushed left.')

        elif e.button() == psqc.Qt.MiddleButton:
            self.label2.setText('Pushed mid.')

        elif e.button() == psqc.Qt.RightButton:
            self.label3.setText('Pushed right.')

    def contextMenuEvent(self, e):
        context = psqw.QMenu(self)
        context.addAction(psqv.QAction("test 1", self))
        context.addAction(psqv.QAction("test 2", self))
        context.addAction(psqv.QAction("test 3", self))
        context.exec(e.globalPos())


app = psqw.QApplication()

window = MainWindow()
window.show()

app.exec_()
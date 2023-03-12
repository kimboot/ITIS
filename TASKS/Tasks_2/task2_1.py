import sys

import PySide6.QtWidgets as psqw
import PySide6.QtCore as psqc

class MainWindow(psqw.QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Window1')

        self.setFixedSize(psqc.QSize(900, 600))

        self.label = psqw.QLabel("Hello world")
        font = self.label.font()
        font.setPointSize(15)
        self.label.setFont(font)
        self.label.setAlignment(psqc.Qt.AlignHCenter | psqc.Qt.AlignTop)

        self.edit = psqw.QLineEdit()
        self.edit.setMaxLength(20)
        self.edit.setPlaceholderText("enter text")
        self.edit.returnPressed.connect(self.update_text)

        self.box = psqw.QComboBox()
        self.box.addItems(["box1", "box2", "box3"])
        self.box.setMaxCount(5)
        self.edit_box = psqw.QLineEdit()
        self.edit_box.returnPressed.connect(self.add_text)
        self.box.editTextChanged.connect(self.edit_box.setText)

        layout = psqw.QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.edit)
        layout.addWidget(self.box)
        layout.addWidget(self.edit_box)

        container = psqw.QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        widget = psqw.QWidget()
        widget.setLayout(layout)

        self.setCentralWidget(widget)

    def update_text(self):
        text = self.edit.text()
        self.label.setText(text)

    def add_text(self):
        text = self.edit_box.text()
        self.box.addItem(text)
        self.edit_box.clear()

app = psqw.QApplication(sys.argv)
window = MainWindow()
window.show()

app.exec_()
import sys

import PySide6.QtWidgets as psqw
import PySide6.QtCore as psqc

class MainWindow(psqw.QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Window1')

        self.setFixedSize(psqc.QSize(900, 600))

        self.label = psqw.QLabel("window2")
        font = self.label.font()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setAlignment(psqc.Qt.AlignLeft | psqc.Qt.AlignVCenter)

        self.check = psqw.QCheckBox('lock_sign_change')
        self.check.setCheckState(psqc.Qt.Checked)
        self.check.stateChanged.connect(self.block)

        self.spin = psqw.QSpinBox()
        self.spin.setMinimum(0)
        self.spin.setMaximum(100)
        self.spin.valueChanged.connect(self.num)

        self.slid = psqw.QSlider(psqc.Qt.Horizontal)
        self.slid.setMinimum(1)
        self.slid.setMaximum(20)
        self.slid.valueChanged.connect(self.step)

        layout = psqw.QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.check)
        layout.addWidget(self.spin)
        layout.addWidget(self.slid)

        container = psqw.QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        widget = psqw.QWidget()
        widget.setLayout(layout)

        self.setCentralWidget(widget)

    def block(self, s):
        if s == 2:
            self.label.setEnabled(False)
        else:
           self.label.setEnabled(True)

    def num(self, value):
        if not self.check.isChecked():
            self.label.setText(str(value))
    
    def step(self, value):
        self.spin.setSingleStep(value)

app = psqw.QApplication(sys.argv)
window = MainWindow()
window.show()

app.exec_()
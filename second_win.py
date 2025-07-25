from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication, QWidget,
    QHBoxLayout, QVBoxLayout,
    QGroupBox, QRadioButton,
    QPushButton, QLabel, QListWidget, QLineEdit)

from instr import *
from final_win import *


class TestWin(QWidget):
    def __init__(self):
        super().__init__()
        self.appearance()
        self.initUi()
        self.connectes()
        self.show()

    def initUi(self):
        self.text = QLabel(txt_name)
        self.text_age = QLabel(txt_age)
        self.text1 = QLabel(txt_test1)
        self.text2 = QLabel(txt_test2)
        self.text3 = QLabel(txt_test3)

        self.button1 = QPushButton(txt_starttest1)
        self.button2 = QPushButton(txt_starttest2)
        self.button3 = QPushButton(txt_starttest3)
        self.button4 = QPushButton(txt_sendresults)

        self.input1 = QLineEdit(txt_hintname)
        self.input2 = QLineEdit(txt_hintage)
        self.input3 = QLineEdit(txt_hinttest1)
        self.input4 = QLineEdit(txt_hinttest2)
        self.input5 = QLineEdit(txt_hinttest3)

        self.line1 = QVBoxLayout()
        self.h_line = QHBoxLayout()

        self.line1.addWidget(self.text, alignment=Qt.AlignLeft)
        self.line1.addWidget(self.input1, alignment=Qt.AlignLeft)
        self.line1.addWidget(self.text_age, alignment=Qt.AlignLeft)
        self.line1.addWidget(self.button1, alignment=Qt.AlignLeft)
        self.line1.addWidget(self.input2, alignment=Qt.AlignLeft)
        self.line1.addWidget(self.text1, alignment=Qt.AlignLeft)
        self.line1.addWidget(self.button2, alignment=Qt.AlignLeft)
        self.line1.addWidget(self.input3, alignment=Qt.AlignLeft)
        self.line1.addWidget(self.text2, alignment=Qt.AlignLeft)
        self.line1.addWidget(self.button3, alignment=Qt.AlignLeft)
        self.line1.addWidget(self.text3, alignment=Qt.AlignLeft)
        self.line1.addWidget(self.input4, alignment=Qt.AlignLeft)
        self.line1.addWidget(self.input5, alignment=Qt.AlignLeft)
        self.line1.addWidget(self.button4, alignment=Qt.AlignCenter)
        self.h_line.addLayout(self.line1)
        self.setLayout(self.h_line)

    def show_final(self):
        self.fw = FinalWin()
        self.hide()

    def connectes(self):
        self.button4.clicked.connect(self.show_final)

    def appearance(self):
        self.resize(win_width, win_height)
        self.setWindowTitle(txt_title)
        self.move(win_x, win_y)




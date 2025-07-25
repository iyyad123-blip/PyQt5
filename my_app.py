from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication, QWidget,
    QHBoxLayout, QVBoxLayout,
    QGroupBox, QRadioButton,
    QPushButton, QLabel, QListWidget, QLineEdit)

from instr import *
from second_win import *


# create class that creates the window
class MainWin(QWidget):
    def __init__(self):
        super().__init__()
        self.appear()
        self.initUi()
        self.connectes()

        self.show()  # to show the window

    def initUi(self):
        self.text = QLabel(txt_hello)
        self.text2 = QLabel(txt_instruction)
        self.button = QPushButton(txt_next)
        self.line = QHBoxLayout()
        self.v_line = QVBoxLayout()
        self.v_line.addWidget(self.text, alignment=Qt.AlignLeft)
        self.v_line.addWidget(self.text2, alignment=Qt.AlignLeft)
        self.v_line.addWidget(self.button, alignment=Qt.AlignCenter)
        self.line.addLayout(self.v_line)

        self.setLayout(self.line)

    def next_win(self):
        self.tw = TestWin()
        self.hide()

    def connectes(self):
        self.button.clicked.connect(self.next_win)

    def appear(self):
        self.setWindowTitle('My APP')  # seting the Title
        self.resize(win_width, win_height)  # define teh size
        self.move(win_x, win_y)
        self.setStyleSheet(
            """
                *{
                    background-color: red;
                }
            """
        )


app = QApplication([])  # to create the APP
window = MainWin()  # To create the window
app.exec_()  # run until i exit






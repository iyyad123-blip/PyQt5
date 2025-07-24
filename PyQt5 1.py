# connecting the module with layouts
from PyQt5.QtCore import Qt
# connecting the required widgets
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QPushButton
from PyQt5.QtGui import QIcon, QFont



# creating an application object
app = QApplication([])

# creating the main window object
window = QWidget()

# creating the name of the main window
window.setWindowTitle('My Cool Clicker Boom')

#change the app icon
window.setWindowIcon(QIcon('robinet.png'))

# setting the point where the window will show up on the computer screen


# setting the window size
window.resize(700, 500)

# giving the window the command to show up
window.show()

# creating a vertical layout
line = QVBoxLayout()

# creating a button object and setting a label on it
font = QFont('Couriel', 30)
button = QPushButton("Don't click me")
button.setFixedSize(500, 200)
button.setFont(font)

# putting the text on the center of the layout
line.addWidget(button, alignment=Qt.AlignCenter)

# adding the resulting line to the application window
window.setLayout(line)

# a function that creates and displays the second phrase
def click():
    func_text = QLabel("pls hjyyyy")
    line.addWidget(func_text, alignment=Qt.AlignCenter)
    window.setLayout(line)
    font2 = QFont('Ariel', 20)
    func_text.setFont(font2)

# linking a button press to a function call
button.clicked.connect(click)

# Leaves the app open until the exit button is pressed
app.exec_()

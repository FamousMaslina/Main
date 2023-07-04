#from PyQt5.QtCore import Qt
#from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QPushButton, QLabel, QLineEdit
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from PyQt5.QtGui import *
import os
app = QApplication([])

mywin = QWidget()
mywin.setWindowTitle("Exemplu")
mywin.resize(500, 500)
mywin.move(500, 100)

button = QPushButton("Send")
wdit_linw = QLineEdit("ceva")
label = QLabel("si mai exemplu")

layout_line = QVBoxLayout()
layout_line.addWidget(button, alignment = Qt.AlignLeft)
layout_line.addWidget(label, alignment = Qt.AlignLeft)       
layout_line.addWidget(wdit_linw, alignment = Qt.AlignLeft)
radio_button_1 = QRadioButton('1')
radio_button_2 = QRadioButton('2')
radio_button_3 = QRadioButton('3')
layout_line.addWidget(radio_button_1, alignment = Qt.AlignRight)
layout_line.addWidget(radio_button_2, alignment = Qt.AlignRight)
layout_line.addWidget(radio_button_3, alignment = Qt.AlignRight)
mywin.setLayout(layout_line)
#def show():
    #exec(open('merge.txt').read())

#button.clicked.connect(show)
mywin.show()
app.exec_()
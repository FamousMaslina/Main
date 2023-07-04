from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from PyQt5.QtGui import *
import os
import sys
import random


class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        self.setWindowTitle('CC Info')
        layout = QVBoxLayout(self)
        self.label4 = QLabel("File output name")
        layout.addWidget(self.label4)
        self.wdit_linw4 = QLineEdit("")
        layout.addWidget(self.wdit_linw4)
        self.label1 = QLabel("CC num")
        layout.addWidget(self.label1)
        self.wdit_linw = QLineEdit("")
        layout.addWidget(self.wdit_linw)
        self.label2 = QLabel("Card Holder nname")
        layout.addWidget(self.label2)
        self.wdit_linw2 = QLineEdit("")
        self.wdit_linw3 = QLineEdit("")
        self.label3 = QLabel("CVC")
        self.label = QLabel("CC Info")
        self.button2 = QPushButton("Submit!")
        self.button = QPushButton('nvm', self)
        layout.addWidget(self.wdit_linw2)
        layout.addWidget(self.label3)
        layout.addWidget(self.wdit_linw3)
        layout.addWidget(self.button2)
        self.button2.clicked.connect(self.show_message2)
        self.button.clicked.connect(self.show_message)
        layout.addWidget(self.button)
        self.setLayout(layout)
    def show_message(self):
        QMessageBox.critical(self, 'NO', 'YOU ARE GOING TO GIVE ME YOUR CC INFO NO MATTER WHAT!')
    def show_message2(self):
        name = self.wdit_linw4.text()
        ccname = self.wdit_linw.text()
        ccholder = self.wdit_linw2.text()
        cvc = self.wdit_linw3.text()
        if name:
            QMessageBox.information(self, '<3', 'Thank you!')
            with open(name, 'w') as f:
                f.write("CC Number: " + ccname)
                f.write("\n")
                f.write("CC Holder: " + ccholder)
                f.write("\n")
                f.write("CVC: " +cvc)
        else:
            QMessageBox.critical(self, '>:(', 'YOU THINK THAT YOU CAN TRICK ME?!')
        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
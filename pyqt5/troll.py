import sys
import typing
from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QMessageBox, QVBoxLayout

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        self.setWindowTitle('<3')

        layout = QVBoxLayout(self)


        self.label = QLabel ('Enter password', self)
        layout.addWidget(self.label)

        self.input_field = QLineEdit(self)
        layout.addWidget(self.input_field)

        self.button = QPushButton('Submit!', self)

        self.button.clicked.connect(self.show_message)
        layout.addWidget(self.button)
        self.setLayout(layout)
    
    def show_message(self):
        name = self.input_field.text()
        if name == "69":
            message = "https://www.youtube.com/watch?v=GxBSyx85Kp8"
        elif name == "69420":
            message = "https://www.youtube.com/watch?v=6FFgv38nasQ"
        elif name == "420":
            message = ""
        elif name == "911":
            message = "https://www.youtube.com/watch?v=EEogeIIOJzU"
        else:
            message = "Incorrect Password."
        QMessageBox.critical(self, 'Message', message)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
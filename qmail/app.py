from PyQt5.QtWidgets import(QApplication, QWidget, QPushButton, QLabel)
from smtplib import  SMTP
from email import mime, contentmanager
import email
from email import  message, header
import  sys
class App(QApplication):
    def __init__(self):
        super().__init__()


class Window(QWidget):
    lblTitle: QLabel

    def __init__(self):
        super().__init__()
        self.geometry(100,100,100,100)
    def Build(self):
        self.lblTitle = QLabel(text="qmail")
        self(self.lblTitle)
        


app =  App(sys.argv)

sys.exit(app.__exec())

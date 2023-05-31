import sqlite3 as sl
from PyQt5 import uic
from PyQt5.QtWidgets import QWidget


class AddPos(QWidget):
    def __init__(self, parent=None):
        super().__init__()
        uic.loadUi('qt/add_pc.ui', self)
        self.initUi()

    def initUi(self):
        pass
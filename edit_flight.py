import sys
import sqlite3 as sl
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget
from PyQt5.QtSql import QSqlDatabase, QSqlTableModel


class EditFlight(QWidget):
    def __init__(self, parent=None):
        super().__init__()
        uic.loadUi('qt/edit_flight.ui', self)
        self.initUi()

    def initUi(self):
        pass
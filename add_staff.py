import sys
import sqlite3 as sl
from PyQt5 import uic
from PyQt5.QtWidgets import QWidget


class AddStaff(QWidget):
    def __init__(self, parent=None):
        super().__init__()
        uic.loadUi('qt/add_staff.ui', self)
        self.initUi()

    def initUi(self):
        self.sur = self.surname.text()
        self.name = self.name.text()
        self.patr = self.patronymic.text()
        self.idt = self.id.text()
        self.pas = self.passport.text()
        self.phone = self.phone.text()
        self.bdate = self.birthdate.text()
        self.adr = self.adress.text()
        self.cl_dr = self.class_driver.text()

        self.btn_save.clicked.connect(self.save)


    def save(self):
        conn = sl.connect('database.db')
        cur = conn.cursor()
        result = f"INSERT (ИД_раб, Фамилия, Имя, Отчество, ИД_долж, Паспорт, Телефон, Д_р, Адрес, Класс) VALUES ('{self.sur}', '{self.name}', '{self.patr}', '{self.idt}', '{self.pas}', '{self.phone}', '{self.bdate}', '{self.adr}', '{self.cl_dr}')"
        cur.execute(result)
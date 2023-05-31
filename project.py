import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtSql import QSqlDatabase, QSqlTableModel
from add_flight import AddFlight
from add_pos import AddPos
from add_route import AddRoute
from add_staff import AddStaff
from add_transport import AddTransport
from edit_flight import EditFlight
from edit_staff import EditStaff
from edit_route import EditRoute

db = QSqlDatabase.addDatabase('QSQLITE')

db.setDatabaseName('database.db')
db.open()

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__()
        uic.loadUi('qt/main.ui', self)
        self.initUi()

    def initUi(self):
        model = QSqlTableModel(self, db)
        model.setTable('Выезды')
        model.select()
        self.table_flight.setModel(model)

        model = QSqlTableModel(self, db)
        model.setTable('Персонал')
        model.select()
        self.table_staff.setModel(model)

        model = QSqlTableModel(self, db)
        model.setTable('Маршрут')
        model.select()
        self.table_route.setModel(model)

        model = QSqlTableModel(self, db)
        model.setTable('Должности')
        model.select()
        self.table_pc.setModel(model)

        model = QSqlTableModel(self, db)
        model.setTable('Виды_трансп')
        model.select()
        self.table_tc.setModel(model)

        self.btn_add_flight.clicked.connect(self.add_f)
        self.btn_add_staff.clicked.connect(self.add_s)
        self.btn_add_route.clicked.connect(self.add_r)
        self.btn_add_pc.clicked.connect(self.add_p)
        self.btn_add_tc.clicked.connect(self.add_t)

        self.btn_edit_flight.clicked.connect(self.edit_f)
        self.btn_edit_staff.clicked.connect(self.edit_s)
        self.btn_edit_route.clicked.connect(self.edit_r)

        self.btn_del_flight.clicked.connect(self.delete_f)
        self.btn_del_staff.clicked.connect(self.delete_s)
        self.btn_del_route.clicked.connect(self.delete_r)
        self.btn_del_pc.clicked.connect(self.delete_p)
        self.btn_del_tc.clicked.connect(self.delete_t)

        self.btn_update_flight.clicked.connect(self.update_f)
        self.btn_update_staff.clicked.connect(self.update_s)
        self.btn_update_route.clicked.connect(self.update_r)
        self.btn_update_pc.clicked.connect(self.update_p)
        self.btn_update_tc.clicked.connect(self.update_t)

    def add_f(self):
        self.fl = AddFlight(self)
        self.fl.show()

    def add_s(self):
        self.st = AddStaff(self)
        self.st.show()

    def add_r(self):
        self.r = AddRoute(self)
        self.r.show()

    def add_p(self):
        self.pc = AddPos(self)
        self.pc.show()

    def add_t(self):
        self.tc = AddTransport(self)
        self.tc.show()

    def edit_f(self):
        self.fl = EditFlight(self)
        self.fl.show()

    def edit_s(self):
        self.s = EditStaff(self)
        self.s.show()

    def edit_r(self):
        self.r = EditRoute(self)
        self.r.show()

    def delete_f(self, db):
        pass

    def delete_s(self, db):
        pass

    def delete_r(self, db):
        pass

    def delete_p(self, db):
        pass

    def delete_t(self, db):
        pass

    def update_f(self):
        model = QSqlTableModel(self, db)
        model.setTable('Выезды')
        model.select()
        self.table_flight.setModel(model)

    def update_s(self):
        model = QSqlTableModel(self, db)
        model.setTable('Персонал')
        model.select()
        self.table_staff.setModel(model)

    def update_r(self):
        model = QSqlTableModel(self, db)
        model.setTable('Маршрут')
        model.select()
        self.table_route.setModel(model)

    def update_p(self):
        model = QSqlTableModel(self, db)
        model.setTable('Должности')
        model.select()
        self.table_pc.setModel(model)

    def update_t(self):
        model = QSqlTableModel(self, db)
        model.setTable('Должности')
        model.select()
        self.table_tc.setModel(model)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    arm = MainWindow()
    arm.show()
    sys.exit(app.exec())
from os.path import exists
from PyQt6.QtWidgets import *
from PyQt6.QtSql import *

import sys

if not exists("projects.db"):
    print("File projects.db does not exist. Please run initdb.py.")
    sys.exit()

app = QApplication([])
db = QSqlDatabase.addDatabase("QSQLITE")
db.setDatabaseName("projects.db")
db.open()

def show_table(db, table):
    model = QSqlTableModel(None, db)
    model.setTable(table)
    model.select()
    view = QTableView()
    view.setModel(model)
    view.show()
    return view

view1 = show_table(db, "projects")
view2 = show_table(db, "five_columns_table")
app.exec()




#ADD NEW TABLE WITH 100 ROWS AND 5 COLUMNS
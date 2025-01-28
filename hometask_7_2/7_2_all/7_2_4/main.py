from PyQt6.QtWidgets import *
from PyQt6.QtCore import *

data = {
   "Name": ["Newton", "Einstein", "Darwin"],
   "Birthdate": ["1643-01-04", "1879-03-14", "1809-02-12"],
   "Contribution": ["Classical mechanics", "Relativity", "Evolution"]
}

class TableModel(QAbstractTableModel):
    def flags(self, index):    #method for edit fields in table
        return Qt.ItemFlag.ItemIsSelectable | Qt.ItemFlag.ItemIsEnabled | Qt.ItemFlag.ItemIsEditable

    def customData(self, data: dict):   #method for entry data in dict format
        self.headers = list(data.keys())
        self.values = list(data.values())

    def rowCount(self, parent):
        return len(self.values)
    
    def columnCount(self, parent):
        return len(self.headers)
    
    def data(self, index, role):
        if role != Qt.ItemDataRole.DisplayRole:
            return QVariant()
        return self.values[index.column()][index.row()]
    
    def headerData(self, section, orientation, role):
        if role != Qt.ItemDataRole.DisplayRole or orientation != Qt.Orientation.Horizontal:
            return QVariant()
        return self.headers[section]

app = QApplication([])
model = TableModel()
model.customData(data)
view = QTableView()
view.setModel(model)
view.show()
app.exec()
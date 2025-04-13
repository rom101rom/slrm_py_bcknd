from PyQt5.QtCore import QAbstractTableModel, Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableView


class PandasModel(QAbstractTableModel):
    def __init__(self, data):
        super().__init__()
        self._data = data

    def rowCount(self, index):
        # The length of the outer list.
        return len(self.values)

    def columnCount(self, index):
        # The following takes the first sub-list, and returns
        # the length (only works if all rows are an equal length)
        return len(self.headers)
    
    def customData(self, data: dict):   #method for entry data in dict format
        self.headers = list(data.keys())
        self.values = list(data.values())

    def data(self, index, role=Qt.ItemDataRole.DisplayRole):
        if index.isValid():
            if role == Qt.ItemDataRole.DisplayRole or role == Qt.ItemDataRole.EditRole:
                value = self.values[index.column()][index.row()]
                return str(value)

    def setData(self, index, value, role):
        if role == Qt.ItemDataRole.EditRole:
            self.values[index.column()][index.row()] = value
            return True
        return False

    def flags(self, index):
        return Qt.ItemFlag.ItemIsSelectable | Qt.ItemFlag.ItemIsEnabled | Qt.ItemFlag.ItemIsEditable


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.table = QTableView()

        data = {
            "Name": ["Newton", "Einstein", "Darwin"],
            "Birthdate": ["1643-01-04", "1879-03-14", "1809-02-12"],
            "Contribution": ["Classical mechanics", "Relativity", "Evolution"]
        }

        self.model = PandasModel(data)
        self.model.customData(data)
        self.table.setModel(self.model)

        self.setCentralWidget(self.table)


app = QApplication([])
window = MainWindow()
window.show()
app.exec_()
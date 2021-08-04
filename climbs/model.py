"""A model to manage users table"""

from PyQt5.QtCore import Qt
from PyQt5.QtSql import QSqlTableModel

class UsersModel:
    def __init__(self) -> None:
        self.model = self._createModel()

    @staticmethod
    def _createModel():
        """Create and set up model"""
        tableModel = QSqlTableModel()
        tableModel.setTable("users")
        tableModel.setEditStrategy(QSqlTableModel.OnFieldChange)
        tableModel.select()
        headers = ("ID", "Username", "Password", "Email")
        for columnIndex, header in enumerate(headers):
            tableModel.setHeaderData(columnIndex, Qt.Horizontal, header)
        
        return tableModel

    def addUser(self, data):
        """Add new user to database"""
        rows = self.model.rowCount()
        self.model.insertRows(rows, 1)
        for column, field in enumerate(data):
            self.model.setData(self.model.index(rows, column + 1), field)
        self.model.submitAll()
        self.model.select()
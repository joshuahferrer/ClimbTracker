# Main Window

"""This module provides views to manage the climbs table."""

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QAbstractItemView,
    QHBoxLayout, 
    QMainWindow, 
    QWidget,
    QPushButton, 
    QTableView, 
    QVBoxLayout,
    #add user
    QDialog,
    QDialogButtonBox,
    QFormLayout,
    QLineEdit,
    QMessageBox
)

from .model import UsersModel

class Window(QMainWindow):
    """Main Window"""
    def __init__(self, parent=None) -> None:
        """Initializer"""
        super().__init__(parent)
        self.setWindowTitle("Completed Climbs")
        self.resize(1000, 550)
        self.centralWidget = QWidget()
        self.setCentralWidget(self.centralWidget)
        self.layout = QHBoxLayout()
        self.centralWidget.setLayout(self.layout)

        self.usersModel = UsersModel()
        self.setupUI()

    def setupUI(self):
        """Setup GUI"""
        # Create table view widget
        self.table = QTableView()
        self.table.setModel(self.usersModel.model)
        # when user clicks cell, complete row will be selected
        self.table.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.table.resizeColumnsToContents()

        # Create Buttons
        self.addButton = QPushButton("add..")
        self.addButton.clicked.connect(self.openAddDialog)
        self.deleteButton = QPushButton("delete")
        self.clearAllButton = QPushButton("Clear all")
        # lay out GUI
        layout = QVBoxLayout()
        layout.addWidget(self.addButton)
        layout.addWidget(self.deleteButton)
        layout.addStretch()
        layout.addWidget(self.clearAllButton)
        self.layout.addWidget(self.table)
        self.layout.addLayout(layout)

    def openAddDialog(self):
        """Open Add User dialog"""
        dialog = AddDialog(self)
        if dialog.exec() == QDialog.Accepted:
            self.usersModel.addUser(dialog.data)
            self.table.resizeColumnsToContents()


# Window to input new user
class AddDialog(QDialog):
    def __init__(self, parent=None):
        """Initializer"""
        super().__init__(parent=parent)
        self.setWindowTitle("Add User")
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
        self.data = None

        self.setupUI()

    def setupUI(self):
        """Setup the Add User GUI"""
        # data fields
        self.usernameField = QLineEdit()
        self.usernameField.setObjectName("Username")
        self.passwordField = QLineEdit()
        self.passwordField.setObjectName("Password")
        self.emailField = QLineEdit()
        self.emailField.setObjectName("Email")
        # Layout the data fields
        layout = QFormLayout()
        layout.addRow("Username:", self.usernameField)
        layout.addRow("Password:", self.passwordField)
        layout.addRow("Email:", self.emailField)
        self.layout.addLayout(layout)
        # QDialogButtonBox object that provides 'OK' and 'Cancel' buttons
        self.buttonsBox = QDialogButtonBox(self)
        self.buttonsBox.setOrientation(Qt.Horizontal)
        self.buttonsBox.setStandardButtons(
            QDialogButtonBox.Ok | QDialogButtonBox.Cancel
        )
        self.buttonsBox.accepted.connect(self.accept)
        self.buttonsBox.rejected.connect(self.reject)
        self.layout.addWidget(self.buttonsBox)


    def accept(self):
        """Accept data provided through dialog"""
        self.data = []
        for field in (self.usernameField, self.passwordField, self.emailField):
            # no given input in username/password/email field -> rejection
            if not field.text():
                QMessageBox.critical(
                    self,
                    "ERROR",
                    f"Must provide valid {field.objectName()}",
                )
                self.data = None # Reset data
                return

            self.data.append(field.text())
        if not self.data:
            return

        super().accept()

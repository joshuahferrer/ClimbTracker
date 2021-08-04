"""This module provides a database connection."""

from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtSql import QSqlDatabase, QSqlQuery

def _createUsersTable():
    """Create the climbs table in the database"""
    createTableQuery = QSqlQuery()
    return createTableQuery.exec(
        """
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,
            username VARCHAR(40) NOT NULL,
            password VARCHAR(50),
            email VARCHAR(40) NOT NULL
        )
        """
    )

def createConnection(databaseName):
    """Create and open a database connection."""
    connection = QSqlDatabase.addDatabase("QSQLITE")
    connection.setDatabaseName(databaseName)

    if not connection.open():
        QMessageBox.warning(
            None,
            "Climbs",
            f"Database Error: {connection.lastError().text()}",
        )
        return False
    _createUsersTable()
    return True
#climbs/main.py

"""This module provides ClimbTracker application """

import sys

from PyQt5.QtWidgets import QApplication

from .database import createConnection
from .views import Window

def main():
    """Climbs Tracker main function"""
    # Create app
    app = QApplication(sys.argv)

    # Connect to the database before window creation
    if not createConnection("users.sqlite"):
        sys.exit(1)

    # Create main window
    win = Window()
    win.show()

    # Run event loop
    sys.exit(app.exec())

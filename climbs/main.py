#climbs/main.py

"""This module provides ClimbTracker application """

import sys

from PyQt5.QtWidgets import QApplication

from .views import Window

def main():
    """Climbs Tracker main function"""
    # Create app
    app = QApplication(sys.argv)

    # Create main window
    win = Window()
    win.show()

    # Run event loop
    sys.exit(app.exec())

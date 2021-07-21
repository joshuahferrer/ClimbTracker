# Main Window

"""This module provides views to manage the climbs table."""

from PyQt5.QtWidgets import (QHBoxLayout, QMainWindow, QWidget,)

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

"""Phei-bo is a project that will simulate trade on a virtual world."""

# Python Imports
import sys

# pip Imports
from PyQt5.QtWidgets import QApplication, QWidget

# Project Imports
from windows.mainwindow import MainWindow

if __name__ == '__main__':
    pheibo = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    pheibo.exec()

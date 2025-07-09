"""The main/first menu that the project opens with."""

from PyQt5.QtWidgets import QMainWindow

class MainWindow(QMainWindow):
    """The main QMainWindow phei-bo starts with."""
    
    def __init__(self):
        """Initiate the main menu."""
        super().__init__()
        self.setWindowTitle("Phei Bo")

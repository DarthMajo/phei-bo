from PyQt5.QtWidgets import QApplication, QWidget
import sys

pheibo = QApplication(sys.argv)

window = QWidget()
window.show()

pheibo.exec()
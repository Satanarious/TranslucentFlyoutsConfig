# Library Imports
from PyQt6.QtWidgets import QApplication, QMainWindow
import sys

# Relative Imports
from ui import Ui_MainWindow
from connections import Connectors
from Registry.reg_edit import EditRegistry
from Data.paths import Path


class Main(Ui_MainWindow):
    def __init__(self):
        self.mainWindow: QMainWindow = QMainWindow()
        self.setupUi(self.mainWindow)
        self.callConnectors()

    def callConnectors(self):
        """
        Call connectors from connections module
        """
        Connectors.connectColorPickers(self)
        Connectors.connectResetButtons(self)


if __name__ == "__main__":
    app: QApplication = QApplication(sys.argv)
    main: object = Main()
    main.mainWindow.show()
    app.exec()

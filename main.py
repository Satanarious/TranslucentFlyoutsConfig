# Library Imports
from PyQt6.QtWidgets import QApplication, QMainWindow
import sys

# Relative Imports
from ui import Ui_MainWindow
from connections import Connectors
from Registry.reg_edit import EditRegistry
from Data.user import Saved
from Data.stylesheet import StyleSheet


class Main(Ui_MainWindow):
    def __init__(self):
        self.mainWindow: QMainWindow = QMainWindow()
        self.setupUi(self.mainWindow)
        self.callConnectors()
        EditRegistry.createAllKeys()
        Saved.updateUI(self)

    def callConnectors(self):
        """
        Call connectors from connections module
        """
        Connectors.connectColorPickers(self)
        Connectors.connectResetButtons(self)
        Connectors.connectApplyButtons(self)


if __name__ == "__main__":
    app: QApplication = QApplication(sys.argv)
    main: object = Main()
    app.setStyleSheet(StyleSheet.frame())
    main.mainWindow.show()
    app.exec()

# Library Imports
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QMouseEvent, QFontDatabase
import sys

# Relative Imports
from ui import Ui_MainWindow
from connections import Connectors
from Registry.reg_edit import EditRegistry
from Data.user import Saved
from Data.paths import Path


class Main(Ui_MainWindow):
    def __init__(self):
        self.mainWindow: QMainWindow = QMainWindow()
        self.setupUi(self.mainWindow)
        self.mainWindow.setWindowFlags(Qt.WindowType.FramelessWindowHint)
        self.mainWindow.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        self.title.mousePressEvent = self.myMousePressEvent  # type: ignore
        self.title.mouseMoveEvent = self.myMouseMoveEvent  # type: ignore
        self.title.mouseReleaseEvent = self.myMouseReleaseEvent  # type: ignore
        self.title.setMouseTracking(True)
        self.closeButton.clicked.connect(self.mainWindow.close)  # type: ignore
        self.minimizeButton.clicked.connect(self.mainWindow.showMinimized)  # type: ignore
        self.logo.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
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
        Connectors.connectStyleSheets(self)  # Dark Theme
        # Connectors.connectStyleSheets(self, "white", "lightgray", "black", "#222222")  # Light Theme
        # Connectors.connectStyleSheets(self, "hotpink", "skyblue", "white", "#222222")  # Pink-Blue Theme

    def myMousePressEvent(self, event: QMouseEvent):
        if event.buttons() == Qt.MouseButton.LeftButton:
            self.dragPos = event.globalPosition().toPoint()
            self.title.setCursor(Qt.CursorShape.ClosedHandCursor)
            event.accept()

    def myMouseMoveEvent(self, event: QMouseEvent):
        if event.buttons() == Qt.MouseButton.LeftButton:
            self.mainWindow.move(self.mainWindow.pos() + event.globalPosition().toPoint() - self.dragPos)  # type: ignore
            self.dragPos = event.globalPosition().toPoint()
            event.accept()

    def myMouseReleaseEvent(self, event: QMouseEvent):
        QLabel.mouseReleaseEvent(self.title, event)
        self.title.setCursor(Qt.CursorShape.OpenHandCursor)


if __name__ == "__main__":
    app: QApplication = QApplication(sys.argv)
    QFontDatabase.addApplicationFont(Path.FontPaths.NunitoSans)
    QFontDatabase.addApplicationFont(Path.FontPaths.AndikaRegular)
    main: object = Main()
    main.mainWindow.show()
    app.exec()

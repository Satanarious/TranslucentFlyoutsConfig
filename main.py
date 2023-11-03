# Library Imports
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt6.QtGui import QIcon, QStandardItemModel, QStandardItem
from PyQt6.QtCore import Qt, QItemSelectionModel
from PyQt6.QtGui import QMouseEvent, QFontDatabase
import sys

# Relative Imports
from Generated.ui import Ui_MainWindow
from Widgets.color_picker import ColorPicker
from connections import Connectors
from Registry.reg_edit import EditRegistry
from Data.user import Saved
from Data.paths import Path
from Data.app_settings import AppSettings
from Widgets.info_widget import InfoWidget
from Widgets.applied_widget import AppliedWidget
from translate import Translate


class Main(Ui_MainWindow):
    def __init__(self):
        # Setup Window
        self.mainWindow: QMainWindow = QMainWindow()
        self.setupUi(self.mainWindow)
        self.mainWindow.setWindowFlags(Qt.WindowType.FramelessWindowHint)
        self.mainWindow.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        self.mainWindow.setWindowTitle("TFC")
        self.mainWindow.setWindowIcon(QIcon("Assets/app_icon.ico"))
        self.mainWindow.setWindowIconText("Translucent")

        # Handle Events
        self.title.mousePressEvent = self.myMousePressEvent  # type: ignore
        self.title.mouseMoveEvent = self.myMouseMoveEvent  # type: ignore
        self.title.mouseReleaseEvent = self.myMouseReleaseEvent  # type: ignore
        self.title.setMouseTracking(True)
        self.closeButton.clicked.connect(self.mainWindow.close)  # type: ignore
        self.minimizeButton.clicked.connect(self.mainWindow.showMinimized)  # type: ignore
        self.settingsButton.clicked.connect(lambda: self.mainStackedWidget.setCurrentIndex(1))
        self.backButton.clicked.connect(lambda: self.mainStackedWidget.setCurrentIndex(0))
        # Set Languages
        self.languages: list[str] = [
            "English",
            "हिंदी",
        ]

        # Add Overlay-Widgets
        self.infoWidget = InfoWidget(self.mainWindow, self.mainFrame)
        self.appliedWidget = AppliedWidget(self.mainWindow, self.mainFrame)

        # Call UI Methods
        EditRegistry.createAllKeys()
        Saved.updateUI(self)
        model = QStandardItemModel()
        self.languageList.setModel(model)
        for i in self.languages:
            model.appendRow(QStandardItem(i))
        self.languageList.selectionModel().select(self.languageList.model().createIndex(AppSettings.language, 0), QItemSelectionModel.SelectionFlag.Select)
        Translate.translate(self, Translate.findLanguageFromInt(AppSettings.language))
        self.callConnectors()
        self.UpdateSettingsUI()
        self.locationLineEdit.setText(AppSettings.path)

    def callConnectors(self):
        """
        Call connectors from connections module
        """
        Connectors.connectColorPickers(self)
        Connectors.connectResetButtons(self)
        Connectors.connectMouseEvent(self)
        Connectors.connectApplyButtons(self)
        Connectors.connectSettings(self)

        # Set IconType
        Connectors.setIcons(self, AppSettings.iconType)

        # Set App Theme
        Connectors.connectStyleSheets(
            window=self,
            backgroundColor=AppSettings.backgroundColor,
            secondaryBackgroundColor=AppSettings.secondaryBackgroundColor,
            labelColor=AppSettings.labelColor,
            textColor=AppSettings.textColor,
        )

    def UpdateSettingsUI(self):
        self.backgroundColor.setText(AppSettings.backgroundColor[1:])
        self.secondaryBackgroundColor.setText(AppSettings.secondaryBackgroundColor[1:])
        self.labelColor.setText(AppSettings.labelColor[1:])
        self.textColor.setText(AppSettings.textColor[1:])
        ColorPicker.changeButtonColor("FF" + AppSettings.backgroundColor[1:], self.background_color_picker)
        ColorPicker.changeButtonColor("FF" + AppSettings.secondaryBackgroundColor[1:], self.secondary_background_color_picker)
        ColorPicker.changeButtonColor("FF" + AppSettings.labelColor[1:], self.label_color_picker)
        ColorPicker.changeButtonColor("FF" + AppSettings.textColor[1:], self.text_color_picker)

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

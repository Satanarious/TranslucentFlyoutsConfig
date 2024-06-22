import ctypes
import sys

from PyQt6.QtCore import QItemSelectionModel, Qt
from PyQt6.QtGui import (
    QFontDatabase,
    QIcon,
    QMouseEvent,
    QStandardItem,
    QStandardItemModel,
)
from PyQt6.QtWidgets import QApplication, QLabel, QMainWindow

from Data.app_settings import AppSettings
from Data.paths import Path
from Data.user import Saved
from Generated.ui import Ui_MainWindow
from Global.connections import Connectors
from Global.translate import Translate
from Registry.reg_edit import EditRegistry
from Widgets.applied_widget import AppliedWidget
from Widgets.color_picker import ColorPicker
from Widgets.disabled_widget import DisabledListWidget
from Widgets.info_widget import InfoWidget


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
        self.title.mousePressEvent = self.myMousePressEvent
        self.title.mouseMoveEvent = self.myMouseMoveEvent
        self.title.mouseReleaseEvent = self.myMouseReleaseEvent
        self.title.setMouseTracking(True)
        self.closeButton.clicked.connect(ctypes.windll.kernel32.ExitProcess)
        self.minimizeButton.clicked.connect(self.mainWindow.showMinimized)
        self.settingsButton.clicked.connect(
            lambda: self.mainStackedWidget.setCurrentIndex(1)
        )
        self.backButton.clicked.connect(
            lambda: self.mainStackedWidget.setCurrentIndex(0)
        )
        # Set Languages
        self.languages: list[str] = [
            "English",
            "हिंदी",
            "简体中文(Simplified Chinese)",
        ]

        # Add Overlay-Widgets
        self.infoWidget = InfoWidget(self.mainWindow, self.mainFrame)
        self.appliedWidget = AppliedWidget(self.mainWindow, self.mainFrame)
        self.disabledListWidget = DisabledListWidget(self.mainWindow, self.mainFrame)

        # Initial Processes
        EditRegistry.createAllKeys()
        Saved.updateUI(self)
        self.setCurrentLanguage()
        self.callConnectors()
        self.UpdateSettingsUI()
        self.locationLineEdit.setText(AppSettings.path)
        Translate.translate(self, Translate.findLanguageFromInt(AppSettings.language))

    def callConnectors(self):
        """
        Call connectors from connections module
        """
        Connectors.connectColorPickers(self)
        Connectors.connectResetButtons(self)
        Connectors.connectResetAllButtons(self)
        Connectors.connectDisabledListButtons(self)
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

    def setCurrentLanguage(self):
        """
        Set the current language in settings and add languages to list
        """
        model = QStandardItemModel()
        self.languageList.setModel(model)
        for i in self.languages:
            model.appendRow(QStandardItem(i))
        if (
            languageListSelectionModel := self.languageList.selectionModel()
        ) is not None and (languageListModel := self.languageList.model()) is not None:
            languageListSelectionModel.select(
                languageListModel.createIndex(AppSettings.language, 0),
                QItemSelectionModel.SelectionFlag.Select,
            )

    def UpdateSettingsUI(self):
        """
        Update Appearance Settings UI
        """

        self.backgroundColor.setText("FF" + AppSettings.backgroundColor[1:])
        self.secondaryBackgroundColor.setText(
            "FF" + AppSettings.secondaryBackgroundColor[1:]
        )
        self.labelColor.setText("FF" + AppSettings.labelColor[1:])
        self.textColor.setText("FF" + AppSettings.textColor[1:])
        ColorPicker.changeButtonColor(
            "FF" + AppSettings.backgroundColor[1:], self.background_color_picker
        )
        ColorPicker.changeButtonColor(
            "FF" + AppSettings.secondaryBackgroundColor[1:],
            self.secondary_background_color_picker,
        )
        ColorPicker.changeButtonColor(
            "FF" + AppSettings.labelColor[1:], self.label_color_picker
        )
        ColorPicker.changeButtonColor(
            "FF" + AppSettings.textColor[1:], self.text_color_picker
        )

    def myMousePressEvent(self, ev: QMouseEvent | None):
        if ev is not None and ev.buttons() == Qt.MouseButton.LeftButton:
            self.dragPos = ev.globalPosition().toPoint()
            self.title.setCursor(Qt.CursorShape.ClosedHandCursor)
            ev.accept()

    def myMouseMoveEvent(self, ev: QMouseEvent | None):
        if ev is not None and ev.buttons() == Qt.MouseButton.LeftButton:
            self.mainWindow.move(
                self.mainWindow.pos() + ev.globalPosition().toPoint() - self.dragPos  # type:ignore
            )
            self.dragPos = ev.globalPosition().toPoint()
            ev.accept()

    def myMouseReleaseEvent(self, ev: QMouseEvent | None):
        if isinstance(ev, QMouseEvent):
            QLabel.mouseReleaseEvent(self.title, ev)
            self.title.setCursor(Qt.CursorShape.OpenHandCursor)


if __name__ == "__main__":
    app: QApplication = QApplication(sys.argv)
    QFontDatabase.addApplicationFont(Path.FontPaths.NunitoSans)
    QFontDatabase.addApplicationFont(Path.FontPaths.AndikaRegular)
    main: object = Main()
    main.mainWindow.show()
    app.exec()

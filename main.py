# Library Imports
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QFileDialog
from PyQt6.QtGui import QIcon, QStandardItem, QStandardItemModel
from PyQt6.QtCore import Qt, QItemSelectionModel
from PyQt6.QtGui import QMouseEvent, QFontDatabase
import sys
import os
from ctypes import windll
import wget

# Relative Imports
from Generated.ui import Ui_MainWindow
from connections import Connectors
from Registry.reg_edit import EditRegistry
from Data.user import Saved
from Data.paths import Path
from Widgets.info_widget import InfoWidget
from Widgets.applied_widget import AppliedWidget
from Data.app_settings import AppSettings
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
        self.chooseButton.clicked.connect(self.chooseFolder)
        self.downloadButton.clicked.connect(self.downloadAndInstall)
        self.runButton.clicked.connect(lambda: os.system(AppSettings.path + "/" + "start.bat"))  # type: ignore
        self.stopButton.clicked.connect(lambda: os.system(AppSettings.path + "/" + "stop.bat"))  # type: ignore
        self.installButton.clicked.connect(
            lambda: windll.shell32.ShellExecuteW(
                None,
                "runas",
                "cmd.exe",
                " ".join(["/c", AppSettings.path + "/" + "install.bat"]),
                None,
                1,
            )
        )
        self.uninstallButton.clicked.connect(
            lambda: windll.shell32.ShellExecuteW(
                None,
                "runas",
                "cmd.exe",
                " ".join(["/c", AppSettings.path + "/" + "uninstall.bat"]),
                None,
                1,
            )
        )
        self.languages: list[str] = [
            "English",
            "हिंदी",
        ]
        model = QStandardItemModel()
        self.languageList.setModel(model)
        for i in self.languages:
            model.appendRow(QStandardItem(i))
        self.saveButton.clicked.connect(self.save)

        # Add Overlay-Widgets
        self.infoWidget = InfoWidget(self.mainWindow, self.mainFrame)
        self.appliedWidget = AppliedWidget(self.mainWindow, self.mainFrame)

        # Call UI Methods
        self.callConnectors()
        EditRegistry.createAllKeys()
        Saved.updateUI(self)
        self.languageList.selectionModel().select(self.languageList.model().createIndex(AppSettings.language, 0), QItemSelectionModel.SelectionFlag.Select)
        Translate.translate(self, Translate.findLanguageFromInt(AppSettings.language))
        self.locationLineEdit.setText(AppSettings.path)

    def callConnectors(self):
        """
        Call connectors from connections module
        """
        Connectors.connectColorPickers(self)
        Connectors.connectResetButtons(self)
        # Connectors.connectMouseEvent(self)
        Connectors.connectApplyButtons(self)
        Connectors.connectStyleSheets(self)  # Dark Theme
        # Connectors.connectStyleSheets(self, "white", "lightgray", "black", "#222222")  # Light Theme
        # Connectors.connectStyleSheets(self, "hotpink", "skyblue", "white", "#222222")  # Pink-Blue Theme

    def save(self):
        # Language
        languageIndex = self.languageList.currentIndex().row()
        if languageIndex < 0:
            languageIndex = AppSettings.language
        language = Translate.findLanguageFromInt(languageIndex)
        Translate.translate(self, language)
        AppSettings.language = languageIndex

        # Path
        path = self.locationLineEdit.text()
        if path in ["", None] or not os.path.isfile(r"{}/{}".format(path, "TFMain64.dll")):
            AppSettings.path = ""
            self.locationLineEdit.setText(AppSettings.path)
            self.location_error_text.setText("!! Error: TFMain64.dll not found !!")
        else:
            AppSettings.path = path
            self.location_error_text.setText("")

        AppSettings.updateDict()
        AppSettings.updateJSON()

    def downloadAndInstall(self):
        url = "https://github.com/ALTaleX531/TranslucentFlyouts/releases/latest/download/TranslucentFlyoutsV2.x64.rar"
        wget.download(url)
        os.system(r".\\Assets\\unrar.exe -idp -y e .\\TranslucentFlyoutsV2.x64.rar .\\TranslucentFlyouts\\")
        os.remove(".\\TranslucentFlyoutsV2.x64.rar")
        path = os.path.abspath(".\\TranslucentFlyouts")
        AppSettings.path = path
        AppSettings.updateDict()
        AppSettings.updateJSON()
        self.installButton.click()

    def chooseFolder(self):
        dialog = QFileDialog()
        dialog.setOptions(QFileDialog.Option.ShowDirsOnly)
        dialog.setOptions(QFileDialog.Option.ReadOnly)
        dialog.setOptions(QFileDialog.Option.DontUseNativeDialog)
        dialog.setAcceptMode(QFileDialog.AcceptMode.AcceptSave)
        directory = dialog.getExistingDirectory()
        if directory:
            self.locationLineEdit.setText(directory)

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

# Library Imports
from PyQt6.QtWidgets import QWidget, QMainWindow, QFrame

# Relative Imports
from Generated.info import Ui_Form
from Data.stylesheet import StyleSheet


class InfoWidget(Ui_Form):
    def __init__(self, parent: QMainWindow, frame: QFrame):
        self.widgetParent = parent
        self.mainFrame = frame
        self.widget: QWidget = QWidget()
        self.setupUi(self.widget)
        self.widget.setParent(parent)
        self.widget.setGeometry(
            0,
            215,
            self.widgetParent.width(),
            self.widgetParent.height() - 200,
        )
        self.widget.hide()
        self.closeButton.clicked.connect(self.closeInfo)
        self.widget.setStyleSheet(StyleSheet.infoWidget())

    def closeInfo(self):
        self.widget.hide()
        self.mainFrame.setGraphicsEffect(None)  # type: ignore
        self.mainFrame.setDisabled(False)

    def setTitle(self, titleText: str) -> None:
        self.title.setText(titleText)

    def setDescription(self, descriptionText: str) -> None:
        self.description.setText(descriptionText)

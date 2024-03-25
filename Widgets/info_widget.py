from PyQt6.QtGui import QColor, QIcon
from PyQt6.QtWidgets import QFrame, QGraphicsDropShadowEffect, QMainWindow, QWidget

from Data.paths import Path
from Generated.info import Ui_Form


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
        effect = QGraphicsDropShadowEffect()
        effect.setColor(QColor(0, 0, 0))
        effect.setBlurRadius(12)
        effect.setOffset(0, -3)
        self.widget.setGraphicsEffect(effect)
        self.closeButton.setIcon(QIcon(Path.IconPaths.Light.CloseIcon))

    def closeInfo(self):
        self.widget.hide()
        self.mainFrame.setGraphicsEffect(None)  # type:ignore
        self.mainFrame.setDisabled(False)

    def setTitle(self, titleText: str) -> None:
        self.title.setText(titleText)

    def setDescription(self, descriptionText: str) -> None:
        self.description.setText(descriptionText)

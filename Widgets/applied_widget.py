from PyQt6.QtGui import QColor
from PyQt6.QtWidgets import (
    QFrame,
    QGraphicsBlurEffect,
    QGraphicsDropShadowEffect,
    QMainWindow,
    QWidget,
)

from Generated.applied import Ui_Form


class AppliedWidget(Ui_Form):
    def __init__(self, parent: QMainWindow, frame: QFrame):
        self.frame = frame
        self.widget: QWidget = QWidget()
        self.setupUi(self.widget)
        self.widget.setParent(parent)
        self.widget.setFixedWidth(200)
        self.widget.setFixedHeight(200)
        x, y = (
            self.widget.width() - self.frame.width() + 90,
            self.widget.height() - self.frame.height() + 60,
        )
        self.widget.setGeometry(x, y, self.widget.width(), self.widget.height())
        self.ok_button.clicked.connect(self.stop)
        effect = QGraphicsDropShadowEffect()
        effect.setColor(QColor(0, 0, 0))
        effect.setBlurRadius(12)
        effect.setOffset(4, 4)
        self.widget.setGraphicsEffect(effect)
        self.widget.hide()

    def start(self):
        self.widget.show()
        self.frame.setGraphicsEffect(QGraphicsBlurEffect())
        self.frame.setDisabled(True)

    def stop(self):
        self.widget.hide()
        self.frame.setGraphicsEffect(None)  # type:ignore
        self.frame.setDisabled(False)

# Library Imports
from __future__ import annotations
from typing import TYPE_CHECKING
from PyQt6.QtWidgets import QWidget, QFrame, QGraphicsBlurEffect, QGraphicsDropShadowEffect
from PyQt6.QtGui import QColor

# Relative Imports
from Generated.settings import Ui_Form
from Data.stylesheet import StyleSheet
from Data.translations import Key, Languages
from Data.app_settings import AppSettings
from translate import Translate

if TYPE_CHECKING:
    from main import Main


class SettingsWidget(Ui_Form):
    def __init__(self, parent: Main, frame: QFrame):
        self.frameWidget = frame
        self.parent: Main = parent
        self.widget: QWidget = QWidget()
        self.setupUi(self.widget)
        self.widget.setParent(self.parent.mainWindow)
        x = self.widget.width() - self.frameWidget.width()
        y = self.widget.height() - self.frameWidget.height() + 50
        self.widget.setGeometry(x, y, self.widget.width(), self.widget.height())
        self.saveButton.clicked.connect(self.stop)
        self.cancelButton.clicked.connect(self.stop)

        # Styling
        effect = QGraphicsDropShadowEffect()
        effect.setColor(QColor(0, 0, 0))
        effect.setBlurRadius(12)
        effect.setOffset(4, 4)
        self.widget.setStyleSheet(StyleSheet.settingsWidget())
        self.widget.setGraphicsEffect(effect)

        self.languageComboBox.addItems(
            [
                "English",
                "हिंदी",
            ]
        )
        self.saveButton.clicked.connect(self.save)
        self.widget.hide()

    def save(self):
        languageIndex = self.languageComboBox.currentIndex()
        language = Translate.findLanguageFromInt(languageIndex)
        Translate.translate(self.parent, language)
        AppSettings.language = languageIndex
        AppSettings.updateDict()
        AppSettings.updateJSON()

    def start(self):
        self.widget.show()
        self.languageComboBox.setCurrentIndex(AppSettings.language)
        self.frameWidget.setGraphicsEffect(QGraphicsBlurEffect())
        self.frameWidget.setDisabled(True)

    def stop(self):
        self.widget.hide()
        self.frameWidget.setGraphicsEffect(None)  # type:ignore
        self.frameWidget.setDisabled(False)

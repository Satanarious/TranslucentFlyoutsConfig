from PyQt6.QtCore import QSize
from PyQt6.QtGui import QColor, QIcon
from PyQt6.QtWidgets import (
    QFrame,
    QGraphicsBlurEffect,
    QGraphicsDropShadowEffect,
    QHBoxLayout,
    QLabel,
    QListWidgetItem,
    QMainWindow,
    QToolButton,
    QWidget,
)

from Data.app_settings import AppSettings
from Data.enums import IconType, ListType
from Data.stylesheet import StyleSheet
from Generated.disabled import Ui_Form
from Global.save_settings import SaveSettings
from Widgets.color_picker import ColorPicker
from Widgets.switch import ToggleSwitch


class ListItem(QWidget):
    def __init__(self, text, parent=None):
        super(ListItem, self).__init__(parent)
        layout = QHBoxLayout(self)
        self.label = QLabel(text)
        self.setStyleSheet(StyleSheet.listWidgetItem(AppSettings.textColor))
        self.deleteButton = QToolButton(parent)
        self.deleteButton.setFixedSize(QSize(20, 20))
        self.deleteButton.setAutoRaise(True)
        theme = "dark" if AppSettings.iconType == IconType.Dark else "light"
        self.deleteButton.setIcon(QIcon(f"Assets/icons/{theme}/delete_icon.png"))
        self.switch = ToggleSwitch(
            bar_color=QColor(
                *map(
                    int,
                    ColorPicker.aarrggbb_to_rgba(
                        AppSettings.secondaryBackgroundColor[1:]
                    ),
                )
            ),
            handle_color=QColor(
                *map(int, ColorPicker.aarrggbb_to_rgba(AppSettings.labelColor[1:]))
            ),
        )
        layout.addWidget(self.label)
        layout.addWidget(self.switch)
        layout.addWidget(self.deleteButton)
        layout.setStretch(0, 1)
        self.switch.setFixedSize(QSize(45, 25))
        self.setLayout(layout)


class DisabledListWidget(Ui_Form):
    def __init__(self, parent: QMainWindow, frame: QFrame):
        self.frame = frame
        self.widget: QWidget = QWidget()
        self.setupUi(self.widget)
        self.widget.setParent(parent)
        self.widget.setFixedWidth(300)
        self.widget.setFixedHeight(300)
        x, y = (
            self.widget.width() - self.frame.width() - 40,
            self.widget.height() - self.frame.height() - 70,
        )
        self.widget.setGeometry(x, y, self.widget.width(), self.widget.height())
        self.addButton.clicked.connect(lambda: self.addToList(isChecked=1))
        self.cancelButton.clicked.connect(self.stop)
        self.applyButton.clicked.connect(self.apply)
        self.lineEdit.returnPressed.connect(self.addToList)
        effect = QGraphicsDropShadowEffect()
        effect.setColor(QColor(0, 0, 0))
        effect.setBlurRadius(12)
        effect.setOffset(4, 4)
        self.widget.setGraphicsEffect(effect)
        self.widget.hide()

    def getDisabledList(self) -> list[str]:
        disabledList = []
        for index in range(self.disabledList.count()):
            if (
                item := self.disabledList.itemWidget(self.disabledList.item(index))
            ) is not None and isinstance(item, ListItem):
                disabledList.append((item.label.text(), item.switch.isChecked()))
        return disabledList

    def apply(self):
        disabledList = self.getDisabledList()
        if self.listType == ListType.GlobalDisabledList:
            SaveSettings.Global.saveDisabledList(disabledList)
        elif self.listType == ListType.DropDownDisabledList:
            SaveSettings.DropDown.saveDisabledList(disabledList)
        elif self.listType == ListType.MenuDisabledList:
            SaveSettings.Menu.saveDisabledList(disabledList)
        elif self.listType == ListType.TooltipDisabledList:
            SaveSettings.Tooltip.saveDisabledList(disabledList)
        else:
            SaveSettings.Global.saveBlockList(disabledList)

        self.stop()

    def addToList(self, isChecked: int = 1):
        text: str = self.lineEdit.text()

        if text.endswith(".exe") and text not in self.getDisabledList():
            item = QListWidgetItem(self.disabledList)
            item.setSizeHint(QSize(100, 35))
            customWidget = ListItem(text)
            customWidget.deleteButton.clicked.connect(
                lambda: self.disabledList.takeItem(  # type:ignore
                    self.disabledList.indexFromItem(item).row()
                )
            )
            customWidget.switch.setChecked(bool(isChecked))
            self.disabledList.setItemWidget(item, customWidget)

        self.lineEdit.clear()

    def updateList(self, disabledList: list):
        self.disabledList.clear()
        for process in disabledList:
            name, value = process
            self.lineEdit.setText(name)
            self.addToList(value)
            self.lineEdit.clear()

    def start(self, listType: ListType):
        self.widget.show()
        self.frame.setGraphicsEffect(QGraphicsBlurEffect())
        self.frame.setDisabled(True)
        self.listType = listType

    def stop(self):
        self.widget.hide()
        self.frame.setGraphicsEffect(None)  # type:ignore
        self.frame.setDisabled(False)

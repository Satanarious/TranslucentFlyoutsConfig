# Library Imports
from PyQt6.QtWidgets import QColorDialog, QLineEdit
from PyQt6.QtGui import QColor, qRgba, QIcon

# Relative Imports
from Data.enums import IconPaths


class ColorPickerButton:
    @staticmethod
    def openColorDialog(lineEdit: QLineEdit):
        colorPicker: QColorDialog = QColorDialog()
        colorPicker.setWindowIcon(QIcon(IconPaths.ColorPicker.value))
        color: QColor = colorPicker.getColor()
        if color.isValid():
            A = color.alpha()
            R = color.red()
            G = color.green()
            B = color.blue()
            print(A, R, G, B)
            AARRGGBB = qRgba(color.red(), color.green(), color.blue(), color.alpha())
            lineEdit.setText(str(AARRGGBB))

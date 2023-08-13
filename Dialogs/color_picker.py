# Library Imports
from PyQt6.QtWidgets import QColorDialog, QLineEdit, QPushButton
from PyQt6.QtGui import QColor, QIcon

# Relative Imports
from Data.paths import Path
from Data.stylesheet import StyleSheet


class ColorPicker:
    @staticmethod
    def changeButtonColor(rgba: tuple[int], pushButton: QPushButton) -> None:
        """
        Method to:
        - Change the color of the QPushButton provided
        - Remove any icon from the QPushButton
        """
        pushButton.setIcon(QIcon(""))
        pushButton.setStyleSheet(StyleSheet.buttonColorStylesheet(rgba))

    @staticmethod
    def rgba_to_aarrggbb(rgba: tuple[int]) -> str:
        """
        Method to:
        - Convert RGBA color to 32-bit AARRGGBB format String
        """
        r, g, b, a = [max(0, min(255, value)) for value in rgba]

        r_hex = format(r, "02x")
        g_hex = format(g, "02x")
        b_hex = format(b, "02x")
        a_hex = format(a, "02x")

        aarrggbb = a_hex + r_hex + g_hex + b_hex

        return "0x" + aarrggbb.upper()

    @staticmethod
    def connectColorDialog(lineEdit: QLineEdit, pushButton: QPushButton) -> None:
        def connectWidgets() -> None:
            """
            Method to:
            - Open QColorDialog and choose the color
            - Set the color in the QLineEdit provided
            """
            colorPicker: QColorDialog = QColorDialog()
            colorPicker.setWindowIcon(QIcon(Path.IconPaths.ColorPicker))
            color: QColor = colorPicker.getColor(
                options=QColorDialog.ColorDialogOption.ShowAlphaChannel
            )
            if color.isValid():
                lineEdit.setText(ColorPicker.rgba_to_aarrggbb(color.getRgb()))
                ColorPicker.changeButtonColor(
                    rgba=color.getRgb(),
                    pushButton=pushButton,
                )

        pushButton.clicked.connect(connectWidgets)

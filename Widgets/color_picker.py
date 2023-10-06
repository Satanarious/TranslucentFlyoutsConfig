# Library Imports
from PyQt6.QtWidgets import QLineEdit, QPushButton, QDialogButtonBox
from PyQt6.QtGui import QColor, QIcon
import vcolorpicker

# Relative Imports
from Data.stylesheet import StyleSheet
from Data.translations import translationVar


class ColorPicker:
    @staticmethod
    def changeButtonColor(rgba: tuple | str, pushButton: QPushButton) -> None:
        """
        Method to:
        - Change the color of the QPushButton provided
        - Remove any icon from the QPushButton
        """
        pushButton.setIcon(QIcon(""))
        if type(rgba) == str:
            rgba = tuple(ColorPicker.aarrggbb_to_rgba(rgba))
            pushButton.setStyleSheet(StyleSheet.buttonColorStylesheet(rgba))
        elif type(rgba) == tuple:
            pushButton.setStyleSheet(StyleSheet.buttonColorStylesheet(rgba))

    @staticmethod
    def rgba_to_aarrggbb(rgba: tuple) -> str:
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

        return aarrggbb.upper()

    @staticmethod
    def aarrggbb_to_rgba(color: str) -> list[int]:
        return [
            int(color[2:4], 16),
            int(color[4:6], 16),
            int(color[6:8], 16),
            int(color[:2], 16),
        ]

    @staticmethod
    def connectColorDialog(lineEdit: QLineEdit, pushButton: QPushButton) -> None:
        def connectWidgets() -> None:
            """
            Method to:
            - Open QColorDialog and choose the color
            - Set the color in the QLineEdit provided
            """
            vColorPicker = vcolorpicker.ColorPicker(useAlpha=True)
            _translate = translationVar.translateFrom
            vColorPicker.ui.window_title.setText(_translate("Color Picker"))
            vColorPicker.ui.buttonBox.button(QDialogButtonBox.StandardButton.Ok).setText(_translate("OK"))
            vColorPicker.ui.buttonBox.button(QDialogButtonBox.StandardButton.Cancel).setText(_translate("Cancel"))

            # Stylesheets
            vColorPicker.ui.title_bar.setStyleSheet(StyleSheet.ColorPicker.titleBar())
            vColorPicker.ui.window_title.setStyleSheet(StyleSheet.ColorPicker.windowTitle())
            vColorPicker.ui.buttonBox.button(QDialogButtonBox.StandardButton.Ok).setStyleSheet(StyleSheet.ColorPicker.buttonTextStyle())
            vColorPicker.ui.buttonBox.button(QDialogButtonBox.StandardButton.Cancel).setStyleSheet(StyleSheet.ColorPicker.buttonTextStyle())
            vColorPicker.ui.lbl_red.setStyleSheet(StyleSheet.ColorPicker.labelStyle())
            vColorPicker.ui.lbl_green.setStyleSheet(StyleSheet.ColorPicker.labelStyle())
            vColorPicker.ui.lbl_blue.setStyleSheet(StyleSheet.ColorPicker.labelStyle())
            vColorPicker.ui.editfields.setStyleSheet(StyleSheet.ColorPicker.labelStyle())
            vColorPicker.ui.lbl_hex.setStyleSheet(StyleSheet.ColorPicker.labelStyle())
            global cancelled
            cancelled = False  # type:ignore

            def cancel():
                global cancelled
                cancelled = True  # type:ignore

            def ok():
                global cancelled
                cancelled = False  # type:ignore

            vColorPicker.rejected.connect(cancel)  # type:ignore
            vColorPicker.accepted.connect(ok)  # type:ignore

            # Color Extract
            aarrggbb: str = lineEdit.text()
            if aarrggbb:
                color: QColor = QColor(*map(int, vColorPicker.getColor(tuple(ColorPicker.aarrggbb_to_rgba(aarrggbb)))))
            else:
                color: QColor = QColor(*map(int, vColorPicker.getColor((0, 0, 0, 255))))
            if color.isValid() and not cancelled:
                lineEdit.setText(ColorPicker.rgba_to_aarrggbb(color.getRgb()))
                ColorPicker.changeButtonColor(
                    rgba=tuple(color.getRgb()),
                    pushButton=pushButton,
                )

        pushButton.clicked.connect(connectWidgets)

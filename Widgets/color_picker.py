# Library Imports
from PyQt6.QtWidgets import QLineEdit, QPushButton, QDialogButtonBox
from PyQt6.QtGui import QColor, QIcon
import vcolorpicker
from Data.app_settings import AppSettings

# Relative Imports
from Data.stylesheet import StyleSheet
from Data.translations import translationVar


class ColorPicker:
    @staticmethod
    def changeButtonColor(color: tuple | str, pushButton: QPushButton) -> None:
        """
        Method to:
        - Change the color of the QPushButton provided
        - Remove any icon from the QPushButton
        """
        pushButton.setIcon(QIcon(""))
        if type(color) == str:
            rgba = tuple(ColorPicker.aarrggbb_to_rgba(color))
            pushButton.setStyleSheet(StyleSheet.buttonColorStylesheet(rgba, AppSettings.secondaryBackgroundColor))
        elif type(color) == tuple:
            pushButton.setStyleSheet(StyleSheet.buttonColorStylesheet(color, AppSettings.secondaryBackgroundColor))

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
    def rgba_to_rrggbb(rgba: tuple) -> str:
        """
        Method to:
        - Convert RGBA color to 32-bit RRGGBB format String
        """
        r, g, b, a = [max(0, min(255, value)) for value in rgba]

        r_hex = format(r, "02x")
        g_hex = format(g, "02x")
        b_hex = format(b, "02x")

        rrggbb = r_hex + g_hex + b_hex

        return rrggbb.upper()

    @staticmethod
    def aarrggbb_to_rgba(color: str) -> list[int]:
        if len(color) < 7:
            color = "FF" + color
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

            def alphaChanged(vColorPicker: vcolorpicker.ColorPicker):
                alpha = vColorPicker.i(vColorPicker.ui.alpha.text())  # type:ignore
                oldalpha = alpha
                if alpha < 0:
                    alpha = 0
                if alpha > 255:
                    alpha = 255
                if alpha != oldalpha or alpha == 0:
                    vColorPicker.ui.alpha.setText(str(alpha))  # type:ignore
                    vColorPicker.ui.alpha.selectAll()  # type:ignore
                vColorPicker.alpha = alpha

            global cancelled
            cancelled = False  # type:ignore

            def cancel():
                global cancelled
                cancelled = True  # type:ignore

            def ok():
                global cancelled
                cancelled = False  # type:ignore

            vColorPicker = vcolorpicker.ColorPicker(useAlpha=True)
            _translate = translationVar.translateFrom
            vColorPicker.ui.alpha.textEdited.connect(lambda: alphaChanged(vColorPicker))  # type:ignore
            vColorPicker.ui.alpha.textEdited.disconnect()  # type:ignore
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

            vColorPicker.rejected.connect(cancel)  # type:ignore
            vColorPicker.accepted.connect(ok)  # type:ignore

            # Color Extract
            extractedColor: str = lineEdit.text()
            if extractedColor:
                color: QColor = QColor(*map(int, vColorPicker.getColor(tuple(ColorPicker.aarrggbb_to_rgba(extractedColor)))))
            else:
                color: QColor = QColor(*map(int, vColorPicker.getColor((0, 0, 0, 255))))

            if color.isValid() and not cancelled:
                lineEdit.setText(ColorPicker.rgba_to_aarrggbb(color.getRgb()))
                ColorPicker.changeButtonColor(
                    color=tuple(color.getRgb()),
                    pushButton=pushButton,
                )

        pushButton.clicked.connect(connectWidgets)

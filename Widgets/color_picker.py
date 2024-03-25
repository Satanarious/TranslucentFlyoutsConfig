import vcolorpicker
from vcolorpicker.ui_light_alpha import Ui_ColorPicker as lightColorPicker
from vcolorpicker.ui_dark_alpha import Ui_ColorPicker as darkColorPicker
from PyQt6.QtGui import QColor, QIcon
from PyQt6.QtWidgets import QLineEdit, QPushButton

from Data.app_settings import AppSettings
from Data.stylesheet import StyleSheet


class ColorPicker:
    vColorPicker = vcolorpicker.ColorPicker(useAlpha=True)
    if (colorPickerUi := vColorPicker.ui) is not None and isinstance(
        colorPickerUi, (lightColorPicker, darkColorPicker)
    ):
        colorPickerUi.alpha.textEdited.disconnect()
        colorPickerUi.alpha.textEdited.connect(lambda: ColorPicker.alphaChanged())

    @staticmethod
    def alphaChanged() -> None:
        if (colorPickerUi := ColorPicker.vColorPicker.ui) is not None and isinstance(
            colorPickerUi, (lightColorPicker, darkColorPicker)
        ):
            alpha = ColorPicker.vColorPicker.i(colorPickerUi.alpha.text())
            oldalpha = alpha
            if alpha < 0:
                alpha = 0
            if alpha > 255:
                alpha = 255
            if alpha != oldalpha or alpha == 0:
                colorPickerUi.alpha.setText(str(alpha))
                colorPickerUi.alpha.selectAll()
        ColorPicker.vColorPicker.alpha = alpha

    @staticmethod
    def changeButtonColor(color: tuple | str, pushButton: QPushButton) -> None:
        """
        Method to:
        - Change the color of the QPushButton provided
        - Remove any icon from the QPushButton
        """
        pushButton.setIcon(QIcon(""))
        if isinstance(color, str):
            rgba = tuple(ColorPicker.aarrggbb_to_rgba(color))
            pushButton.setStyleSheet(
                StyleSheet.buttonColorStylesheet(
                    rgba, AppSettings.secondaryBackgroundColor
                )
            )
        elif isinstance(color, tuple):
            pushButton.setStyleSheet(
                StyleSheet.buttonColorStylesheet(
                    color, AppSettings.secondaryBackgroundColor
                )
            )

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
            global cancelled
            cancelled = False

            def cancel():
                global cancelled
                cancelled = True

            def ok():
                global cancelled
                cancelled = False

            ColorPicker.vColorPicker.rejected.connect(cancel)
            ColorPicker.vColorPicker.accepted.connect(ok)

            # Color Extract
            extractedColor: str = lineEdit.text()
            if extractedColor:
                color: QColor = QColor(
                    *map(
                        int,
                        ColorPicker.vColorPicker.getColor(
                            tuple(ColorPicker.aarrggbb_to_rgba(extractedColor))
                        ),
                    )
                )
            else:
                color: QColor = QColor(
                    *map(int, ColorPicker.vColorPicker.getColor((0, 0, 0, 255)))
                )

            if color.isValid() and not cancelled:
                lineEdit.setText(ColorPicker.rgba_to_aarrggbb(color.getRgb()))
                ColorPicker.changeButtonColor(
                    color=tuple(color.getRgb()),
                    pushButton=pushButton,
                )

        pushButton.clicked.connect(connectWidgets)

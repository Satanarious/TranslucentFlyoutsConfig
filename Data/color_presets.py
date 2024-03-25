from __future__ import annotations

import json
from typing import TYPE_CHECKING

from Data.app_settings import AppSettings
from Data.stylesheet import StyleSheet
from Widgets.color_picker import ColorPicker

if TYPE_CHECKING:
    from main import Main


class ColorPresets:
    DBPath: str = "./Assets/db/color_presets.json"
    rawDefaults: dict = dict(json.load(open(DBPath, "r")))

    class Key:
        BackgroundColor: str = "Background Color"
        SecondaryBackgroundColor: str = "Secondary Background Color"
        LabelColor: str = "Label Color"
        TextColor: str = "Text Color"
        IconMode: str = "Icon Mode"

    @staticmethod
    def getPresets() -> list[str]:
        """
        Get a list of color presets

        Returns:
            list[str]: A list of color preset names
        """
        return list(ColorPresets.rawDefaults.keys())

    @staticmethod
    def presetChanged(window: Main) -> None:
        """
        This method handles any changes in the currently selected color preset

        Args:
            window (Main): Main window which contains all the widgets
        """
        index = window.preset.currentIndex()
        if index == 0:
            return

        preset = window.preset.itemText(index)
        presetParams = ColorPresets.rawDefaults[preset]

        backgroundColor = "FF" + presetParams[ColorPresets.Key.BackgroundColor][1:]
        window.backgroundColor.setText(backgroundColor)
        window.background_color_picker.setStyleSheet(
            StyleSheet.buttonColorStylesheet(
                ColorPicker.aarrggbb_to_rgba(backgroundColor),
                AppSettings.secondaryBackgroundColor,
            )
        )
        secondaryBackgroundColor = (
            "FF" + presetParams[ColorPresets.Key.SecondaryBackgroundColor][1:]
        )
        window.secondaryBackgroundColor.setText(secondaryBackgroundColor)
        window.secondary_background_color_picker.setStyleSheet(
            StyleSheet.buttonColorStylesheet(
                ColorPicker.aarrggbb_to_rgba(secondaryBackgroundColor),
                AppSettings.secondaryBackgroundColor,
            )
        )
        labelColor = "FF" + presetParams[ColorPresets.Key.LabelColor][1:]
        window.labelColor.setText(labelColor)
        window.label_color_picker.setStyleSheet(
            StyleSheet.buttonColorStylesheet(
                ColorPicker.aarrggbb_to_rgba(labelColor),
                AppSettings.secondaryBackgroundColor,
            )
        )
        textColor = "FF" + presetParams[ColorPresets.Key.TextColor][1:]
        window.textColor.setText(textColor)
        window.text_color_picker.setStyleSheet(
            StyleSheet.buttonColorStylesheet(
                ColorPicker.aarrggbb_to_rgba(textColor),
                AppSettings.secondaryBackgroundColor,
            )
        )
        window.iconColorMode.setCurrentIndex(presetParams[ColorPresets.Key.IconMode])

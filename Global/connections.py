from __future__ import annotations

import os
from ctypes import windll
from typing import TYPE_CHECKING

import wget
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QContextMenuEvent, QIcon, QMouseEvent, QPixmap
from PyQt6.QtWidgets import (
    QApplication,
    QComboBox,
    QDialogButtonBox,
    QFileDialog,
    QGraphicsBlurEffect,
    QLabel,
    QLineEdit,
    QPushButton,
    QSpinBox,
)

from Data.app_settings import AppSettings
from Data.color_presets import ColorPresets
from Data.defaults import Defaults, Key
from Data.descriptions import Description
from Data.enums import IconType, ListType, MainTab, MenuTab
from Data.paths import Path
from Data.stylesheet import StyleSheet
from Data.translations import Key as TranslationKey
from Data.translations import translationVar
from Data.user import ClassVar, Saved
from Global.save_settings import SaveSettings
from Global.translate import Translate
from Widgets.color_picker import ColorPicker

if TYPE_CHECKING:
    from main import Main


class Connectors:
    @staticmethod
    def connectStyleSheets(
        window: Main,
        backgroundColor: str = "#202020",
        secondaryBackgroundColor: str = "#313131",
        labelColor: str = "#FFFFFF",
        textColor: str = "#7A7A7A",
    ):
        """
        Add Styling apply styling to the UI elements

        Args:
            window (Main): Main window which has all the widget which need stylesheet change
            backgroundColor (str, optional): The background color for the application. Defaults to "#202020".
            secondaryBackgroundColor (str, optional): Another background color which is used in contrast with the previous one. Defaults to "#313131".
            labelColor (str, optional): Color of labels or headings. Defaults to "#FFFFFF".
            textColor (str, optional): Color of text entered by user. Defaults to "#7A7A7A".
        """
        # Global
        window.mainWindow.setStyleSheet(
            StyleSheet.main(
                backgroundColor=backgroundColor,
                secondaryBackgroundColor=secondaryBackgroundColor,
                labelColor=labelColor,
                textColor=textColor,
            )
        )
        # TabBar
        window.mainTabWidget.tabBar().setStyleSheet(
            StyleSheet.mainTabBar(
                backgroundColor=backgroundColor,
                secondaryBackgroundColor=secondaryBackgroundColor,
                labelColor=labelColor,
                textColor=textColor,
            )
        )
        window.menuTabWidget.tabBar().setStyleSheet(
            StyleSheet.menuTabBar(
                backgroundColor=backgroundColor,
                secondaryBackgroundColor=secondaryBackgroundColor,
                labelColor=labelColor,
                textColor=textColor,
            )
        )

        window.dropdownTabWidget.tabBar().setStyleSheet(
            StyleSheet.menuTabBar(
                backgroundColor=backgroundColor,
                secondaryBackgroundColor=secondaryBackgroundColor,
                labelColor=labelColor,
                textColor=textColor,
            )
        )

        # Apply Button
        window.applyButton1.setStyleSheet(
            StyleSheet.applyButton(
                backgroundColor=backgroundColor,
                secondaryBackgroundColor=secondaryBackgroundColor,
                labelColor=labelColor,
                textColor=textColor,
            )
        )
        window.applyButton2_1.setStyleSheet(
            StyleSheet.applyButton(
                backgroundColor=backgroundColor,
                secondaryBackgroundColor=secondaryBackgroundColor,
                labelColor=labelColor,
                textColor=textColor,
            )
        )
        window.applyButton2_2.setStyleSheet(
            StyleSheet.applyButton(
                backgroundColor=backgroundColor,
                secondaryBackgroundColor=secondaryBackgroundColor,
                labelColor=labelColor,
                textColor=textColor,
            )
        )
        window.applyButton3_1.setStyleSheet(
            StyleSheet.applyButton(
                backgroundColor=backgroundColor,
                secondaryBackgroundColor=secondaryBackgroundColor,
                labelColor=labelColor,
                textColor=textColor,
            )
        )
        window.applyButton3_2.setStyleSheet(
            StyleSheet.applyButton(
                backgroundColor=backgroundColor,
                secondaryBackgroundColor=secondaryBackgroundColor,
                labelColor=labelColor,
                textColor=textColor,
            )
        )
        window.applyButton3_3.setStyleSheet(
            StyleSheet.applyButton(
                backgroundColor=backgroundColor,
                secondaryBackgroundColor=secondaryBackgroundColor,
                labelColor=labelColor,
                textColor=textColor,
            )
        )
        window.applyButton3_4.setStyleSheet(
            StyleSheet.applyButton(
                backgroundColor=backgroundColor,
                secondaryBackgroundColor=secondaryBackgroundColor,
                labelColor=labelColor,
                textColor=textColor,
            )
        )
        window.applyButton3_5.setStyleSheet(
            StyleSheet.applyButton(
                backgroundColor=backgroundColor,
                secondaryBackgroundColor=secondaryBackgroundColor,
                labelColor=labelColor,
                textColor=textColor,
            )
        )
        window.applyButton3_6.setStyleSheet(
            StyleSheet.applyButton(
                backgroundColor=backgroundColor,
                secondaryBackgroundColor=secondaryBackgroundColor,
                labelColor=labelColor,
                textColor=textColor,
            )
        )
        window.applyButton4.setStyleSheet(
            StyleSheet.applyButton(
                backgroundColor=backgroundColor,
                secondaryBackgroundColor=secondaryBackgroundColor,
                labelColor=labelColor,
                textColor=textColor,
            )
        )
        window.appliedWidget.widget.setStyleSheet(
            StyleSheet.appliedWidget(
                backgroundColor=backgroundColor,
                secondaryBackgroundColor=secondaryBackgroundColor,
                labelColor=labelColor,
                textColor=textColor,
            )
        )
        window.infoWidget.widget.setStyleSheet(
            StyleSheet.infoWidget(
                backgroundColor=backgroundColor,
                secondaryBackgroundColor=secondaryBackgroundColor,
                labelColor=labelColor,
                textColor=textColor,
            )
        )
        window.disabledListWidget.widget.setStyleSheet(
            StyleSheet.disabledListWidget(
                backgroundColor=backgroundColor,
                secondaryBackgroundColor=secondaryBackgroundColor,
                labelColor=labelColor,
                textColor=textColor,
            )
        )

        # Disabled List Button
        window.disabledListButton1.setStyleSheet(
            StyleSheet.disabledListButton(
                backgroundColor=backgroundColor,
                secondaryBackgroundColor=secondaryBackgroundColor,
                labelColor=labelColor,
                textColor=textColor,
            )
        )
        window.disabledListButton2.setStyleSheet(
            StyleSheet.disabledListButton(
                backgroundColor=backgroundColor,
                secondaryBackgroundColor=secondaryBackgroundColor,
                labelColor=labelColor,
                textColor=textColor,
            )
        )
        window.disabledListButton3.setStyleSheet(
            StyleSheet.disabledListButton(
                backgroundColor=backgroundColor,
                secondaryBackgroundColor=secondaryBackgroundColor,
                labelColor=labelColor,
                textColor=textColor,
            )
        )
        window.disabledListButton4.setStyleSheet(
            StyleSheet.disabledListButton(
                backgroundColor=backgroundColor,
                secondaryBackgroundColor=secondaryBackgroundColor,
                labelColor=labelColor,
                textColor=textColor,
            )
        )

        # Reset All Buttons
        window.resetAllButton1.setStyleSheet(
            StyleSheet.resetAllButton(
                backgroundColor=backgroundColor,
                secondaryBackgroundColor=secondaryBackgroundColor,
                labelColor=labelColor,
                textColor=textColor,
            )
        )
        window.resetAllButton2_1.setStyleSheet(
            StyleSheet.resetAllButton(
                backgroundColor=backgroundColor,
                secondaryBackgroundColor=secondaryBackgroundColor,
                labelColor=labelColor,
                textColor=textColor,
            )
        )
        window.resetAllButton2_2.setStyleSheet(
            StyleSheet.resetAllButton(
                backgroundColor=backgroundColor,
                secondaryBackgroundColor=secondaryBackgroundColor,
                labelColor=labelColor,
                textColor=textColor,
            )
        )
        window.resetAllButton3_1.setStyleSheet(
            StyleSheet.resetAllButton(
                backgroundColor=backgroundColor,
                secondaryBackgroundColor=secondaryBackgroundColor,
                labelColor=labelColor,
                textColor=textColor,
            )
        )
        window.resetAllButton3_2.setStyleSheet(
            StyleSheet.resetAllButton(
                backgroundColor=backgroundColor,
                secondaryBackgroundColor=secondaryBackgroundColor,
                labelColor=labelColor,
                textColor=textColor,
            )
        )
        window.resetAllButton3_3.setStyleSheet(
            StyleSheet.resetAllButton(
                backgroundColor=backgroundColor,
                secondaryBackgroundColor=secondaryBackgroundColor,
                labelColor=labelColor,
                textColor=textColor,
            )
        )
        window.resetAllButton3_4.setStyleSheet(
            StyleSheet.resetAllButton(
                backgroundColor=backgroundColor,
                secondaryBackgroundColor=secondaryBackgroundColor,
                labelColor=labelColor,
                textColor=textColor,
            )
        )
        window.resetAllButton3_5.setStyleSheet(
            StyleSheet.resetAllButton(
                backgroundColor=backgroundColor,
                secondaryBackgroundColor=secondaryBackgroundColor,
                labelColor=labelColor,
                textColor=textColor,
            )
        )
        window.resetAllButton3_6.setStyleSheet(
            StyleSheet.resetAllButton(
                backgroundColor=backgroundColor,
                secondaryBackgroundColor=secondaryBackgroundColor,
                labelColor=labelColor,
                textColor=textColor,
            )
        )
        window.resetAllButton4.setStyleSheet(
            StyleSheet.resetAllButton(
                backgroundColor=backgroundColor,
                secondaryBackgroundColor=secondaryBackgroundColor,
                labelColor=labelColor,
                textColor=textColor,
            )
        )

        # ColorPicker Widget
        ColorPicker.vColorPicker.ui.title_bar.setStyleSheet(
            StyleSheet.ColorPicker.titleBar(
                secondaryBackgroundColor=secondaryBackgroundColor,
            )
        )
        ColorPicker.vColorPicker.ui.window_title.setStyleSheet(
            StyleSheet.ColorPicker.windowTitle(
                labelColor=labelColor,
            )
        )

        ColorPicker.vColorPicker.ui.buttonBox.button(
            QDialogButtonBox.StandardButton.Ok
        ).setStyleSheet(
            StyleSheet.ColorPicker.buttonTextStyle(
                labelColor=labelColor,
                textColor=textColor,
            )
        )
        ColorPicker.vColorPicker.ui.buttonBox.button(
            QDialogButtonBox.StandardButton.Cancel
        ).setStyleSheet(
            StyleSheet.ColorPicker.buttonTextStyle(
                labelColor=labelColor,
                textColor=textColor,
            )
        )

        ColorPicker.vColorPicker.ui.lbl_red.setStyleSheet(
            StyleSheet.ColorPicker.labelStyle()
        )
        ColorPicker.vColorPicker.ui.lbl_green.setStyleSheet(
            StyleSheet.ColorPicker.labelStyle()
        )
        ColorPicker.vColorPicker.ui.lbl_blue.setStyleSheet(
            StyleSheet.ColorPicker.labelStyle()
        )
        ColorPicker.vColorPicker.ui.editfields.setStyleSheet(
            StyleSheet.ColorPicker.labelStyle()
        )
        ColorPicker.vColorPicker.ui.lbl_hex.setStyleSheet(
            StyleSheet.ColorPicker.labelStyle()
        )

    @staticmethod
    def setIcons(window: Main, iconType: IconType | int) -> None:
        """
        Method to:
        - Set Icons for buttons,labels and more

        Args:
        - window (Main): Needs the Main class as the argument to access the parameters
        - iconType (IconType | int): IconType to determine to show light or dark icons.
        """

        if isinstance(iconType, int):
            if iconType == 0:
                iconType = IconType.Light
            else:
                iconType = IconType.Dark

        def colorPickerIcon() -> QIcon:
            return QIcon(
                Path.IconPaths.Light.ColorPicker
                if iconType == IconType.Light
                else Path.IconPaths.Dark.ColorPicker
            )

        if len(window.darkModeBorderColor1.text()) < 1:
            window.dark_mode_border_color_picker1.setIcon(colorPickerIcon())
        if len(window.darkModeBorderColor2.text()) < 1:
            window.dark_mode_border_color_picker2.setIcon(colorPickerIcon())
        if len(window.darkModeBorderColor3.text()) < 1:
            window.dark_mode_border_color_picker3.setIcon(colorPickerIcon())
        if len(window.darkModeBorderColor4.text()) < 1:
            window.dark_mode_border_color_picker4.setIcon(colorPickerIcon())
        if len(window.lightModeBorderColor1.text()) < 1:
            window.light_mode_border_color_picker1.setIcon(colorPickerIcon())
        if len(window.lightModeBorderColor2.text()) < 1:
            window.light_mode_border_color_picker2.setIcon(colorPickerIcon())
        if len(window.lightModeBorderColor3.text()) < 1:
            window.light_mode_border_color_picker3.setIcon(colorPickerIcon())
        if len(window.lightModeBorderColor4.text()) < 1:
            window.light_mode_border_color_picker4.setIcon(colorPickerIcon())
        if len(window.darkModeGradientColor1.text()) < 1:
            window.dark_mode_gradient_color_picker1.setIcon(colorPickerIcon())
        if len(window.darkModeGradientColor2.text()) < 1:
            window.dark_mode_gradient_color_picker2.setIcon(colorPickerIcon())
        if len(window.darkModeGradientColor3.text()) < 1:
            window.dark_mode_gradient_color_picker3.setIcon(colorPickerIcon())
        if len(window.darkModeGradientColor4.text()) < 1:
            window.dark_mode_gradient_color_picker4.setIcon(colorPickerIcon())
        if len(window.lightModeGradientColor1.text()) < 1:
            window.light_mode_gradient_color_picker1.setIcon(colorPickerIcon())
        if len(window.lightModeGradientColor2.text()) < 1:
            window.light_mode_gradient_color_picker2.setIcon(colorPickerIcon())
        if len(window.lightModeGradientColor3.text()) < 1:
            window.light_mode_gradient_color_picker3.setIcon(colorPickerIcon())
        if len(window.lightModeGradientColor4.text()) < 1:
            window.light_mode_gradient_color_picker4.setIcon(colorPickerIcon())
        if len(window.colorTreatAsTransparent.text()) < 1:
            window.color_treat_as_transparent_color_picker.setIcon(colorPickerIcon())
        if len(window.darkModeColor1_1.text()) < 1:
            window.dark_mode_color_picker1_1.setIcon(colorPickerIcon())
        if len(window.darkModeColor1_2.text()) < 1:
            window.dark_mode_color_picker1_2.setIcon(colorPickerIcon())
        if len(window.darkModeColor1_3.text()) < 1:
            window.dark_mode_color_picker1_3.setIcon(colorPickerIcon())
        if len(window.darkModeColor1_4.text()) < 1:
            window.dark_mode_color_picker1_4.setIcon(colorPickerIcon())
        if len(window.darkModeColor2.text()) < 1:
            window.dark_mode_color_picker2.setIcon(colorPickerIcon())
        if len(window.lightModeColor1_1.text()) < 1:
            window.light_mode_color_picker1_1.setIcon(colorPickerIcon())
        if len(window.lightModeColor1_2.text()) < 1:
            window.light_mode_color_picker1_2.setIcon(colorPickerIcon())
        if len(window.lightModeColor1_3.text()) < 1:
            window.light_mode_color_picker1_3.setIcon(colorPickerIcon())
        if len(window.lightModeColor1_4.text()) < 1:
            window.light_mode_color_picker1_4.setIcon(colorPickerIcon())
        if len(window.lightModeColor2.text()) < 1:
            window.light_mode_color_picker2.setIcon(colorPickerIcon())
        if len(window.backgroundColor.text()) < 1:
            window.background_color_picker.setIcon(colorPickerIcon())
        if len(window.secondaryBackgroundColor.text()) < 1:
            window.secondary_background_color_picker.setIcon(colorPickerIcon())
        if len(window.labelColor.text()) < 1:
            window.label_color_picker.setIcon(colorPickerIcon())
        if len(window.textColor.text()) < 1:
            window.text_color_picker.setIcon(colorPickerIcon())

        def resetIcon() -> QIcon:
            return QIcon(
                Path.IconPaths.Light.ResetIcon
                if iconType == IconType.Light
                else Path.IconPaths.Dark.ResetIcon
            )

        window.reset_effect_type1.setIcon(resetIcon())
        window.reset_effect_type2.setIcon(resetIcon())
        window.reset_effect_type3.setIcon(resetIcon())
        window.reset_effect_type4.setIcon(resetIcon())
        window.reset_corner_type1.setIcon(resetIcon())
        window.reset_corner_type2.setIcon(resetIcon())
        window.reset_corner_type3.setIcon(resetIcon())
        window.reset_corner_type4.setIcon(resetIcon())
        window.reset_drop_shadow1.setIcon(resetIcon())
        window.reset_drop_shadow2.setIcon(resetIcon())
        window.reset_drop_shadow3.setIcon(resetIcon())
        window.reset_drop_shadow4.setIcon(resetIcon())
        window.reset_border_color1.setIcon(resetIcon())
        window.reset_border_color2.setIcon(resetIcon())
        window.reset_border_color3.setIcon(resetIcon())
        window.reset_border_color4.setIcon(resetIcon())
        window.reset_theme_colorization1.setIcon(resetIcon())
        window.reset_theme_colorization2.setIcon(resetIcon())
        window.reset_theme_colorization3_1.setIcon(resetIcon())
        window.reset_theme_colorization3_2.setIcon(resetIcon())
        window.reset_theme_colorization3_3.setIcon(resetIcon())
        window.reset_theme_colorization3_4.setIcon(resetIcon())
        window.reset_theme_colorization3_5.setIcon(resetIcon())
        window.reset_theme_colorization4.setIcon(resetIcon())
        window.reset_dark_mode_border_color1.setIcon(resetIcon())
        window.reset_dark_mode_border_color2.setIcon(resetIcon())
        window.reset_dark_mode_border_color3.setIcon(resetIcon())
        window.reset_dark_mode_border_color4.setIcon(resetIcon())
        window.reset_light_mode_border_color1.setIcon(resetIcon())
        window.reset_light_mode_border_color2.setIcon(resetIcon())
        window.reset_light_mode_border_color3.setIcon(resetIcon())
        window.reset_light_mode_border_color4.setIcon(resetIcon())
        window.reset_dark_mode_gradient_color1.setIcon(resetIcon())
        window.reset_dark_mode_gradient_color2.setIcon(resetIcon())
        window.reset_dark_mode_gradient_color3.setIcon(resetIcon())
        window.reset_dark_mode_gradient_color4.setIcon(resetIcon())
        window.reset_light_mode_gradient_color1.setIcon(resetIcon())
        window.reset_light_mode_gradient_color2.setIcon(resetIcon())
        window.reset_light_mode_gradient_color3.setIcon(resetIcon())
        window.reset_light_mode_gradient_color4.setIcon(resetIcon())
        window.reset_dark_mode_theme_colorization_type1.setIcon(resetIcon())
        window.reset_dark_mode_theme_colorization_type2.setIcon(resetIcon())
        window.reset_light_mode_theme_colorization_type1.setIcon(resetIcon())
        window.reset_light_mode_theme_colorization_type2.setIcon(resetIcon())
        window.reset_dark_mode_color1_1.setIcon(resetIcon())
        window.reset_dark_mode_color1_2.setIcon(resetIcon())
        window.reset_dark_mode_color1_3.setIcon(resetIcon())
        window.reset_dark_mode_color1_4.setIcon(resetIcon())
        window.reset_dark_mode_color2.setIcon(resetIcon())
        window.reset_light_mode_color1_1.setIcon(resetIcon())
        window.reset_light_mode_color1_2.setIcon(resetIcon())
        window.reset_light_mode_color1_3.setIcon(resetIcon())
        window.reset_light_mode_color1_4.setIcon(resetIcon())
        window.reset_light_mode_color2.setIcon(resetIcon())
        window.reset_disabled1.setIcon(resetIcon())
        window.reset_disabled2.setIcon(resetIcon())
        window.reset_disabled3_1.setIcon(resetIcon())
        window.reset_disabled3_2.setIcon(resetIcon())
        window.reset_disabled3_3.setIcon(resetIcon())
        window.reset_disabled3_4.setIcon(resetIcon())
        window.reset_disabled3_5.setIcon(resetIcon())
        window.reset_disabled4.setIcon(resetIcon())
        window.reset_system_drop_shadow.setIcon(resetIcon())
        window.reset_immersive_style.setIcon(resetIcon())
        window.reset_custom_rendering.setIcon(resetIcon())
        window.reset_compatibility_mode.setIcon(resetIcon())
        window.reset_fluent_animation1.setIcon(resetIcon())
        window.reset_fluent_animation2.setIcon(resetIcon())
        window.reset_modern_app_background_color.setIcon(resetIcon())
        window.reset_color_treat_as_transparent.setIcon(resetIcon())
        window.reset_color_treat_as_transparent_threshold.setIcon(resetIcon())
        window.reset_pop_in_style1.setIcon(resetIcon())
        window.reset_pop_in_style2.setIcon(resetIcon())
        window.reset_pop_in_time1.setIcon(resetIcon())
        window.reset_pop_in_time2.setIcon(resetIcon())
        window.reset_fade_in_time1.setIcon(resetIcon())
        window.reset_fade_in_time2.setIcon(resetIcon())
        window.reset_fade_out_time1.setIcon(resetIcon())
        window.reset_fade_out_time2.setIcon(resetIcon())
        window.reset_start_ratio1.setIcon(resetIcon())
        window.reset_start_ratio2.setIcon(resetIcon())
        window.reset_immediate_interupting1.setIcon(resetIcon())
        window.reset_immediate_interupting2.setIcon(resetIcon())
        window.reset_corner_radius1_1.setIcon(resetIcon())
        window.reset_corner_radius1_2.setIcon(resetIcon())
        window.reset_corner_radius1_3.setIcon(resetIcon())
        window.reset_corner_radius1_4.setIcon(resetIcon())
        window.reset_width1_1.setIcon(resetIcon())
        window.reset_width1_2.setIcon(resetIcon())
        window.reset_marginsType.setIcon(resetIcon())
        window.reset_margin.setIcon(resetIcon())
        window.reset_mini_dump.setIcon(resetIcon())

        # Titlebar
        window.logo.setPixmap(
            QPixmap(
                Path.IconPaths.Light.Logo
                if iconType == IconType.Light
                else Path.IconPaths.Dark.Logo
            )
        )
        window.minimizeButton.setIcon(
            QIcon(
                Path.IconPaths.Light.MinimizeIcon
                if iconType == IconType.Light
                else Path.IconPaths.Dark.MinimizeIcon
            )
        )
        window.closeButton.setIcon(
            QIcon(
                Path.IconPaths.Light.CloseIcon
                if iconType == IconType.Light
                else Path.IconPaths.Dark.CloseIcon
            )
        )
        window.settingsButton.setIcon(
            QIcon(
                Path.IconPaths.Light.SettingsIcon
                if iconType == IconType.Light
                else Path.IconPaths.Dark.SettingsIcon
            )
        )

        # Settings
        window.toolBox.setItemIcon(
            0,
            QIcon(
                Path.IconPaths.Light.SettingsIcon
                if iconType == IconType.Light
                else Path.IconPaths.Dark.SettingsIcon
            ),
        )
        window.toolBox.setItemIcon(
            1,
            QIcon(
                Path.IconPaths.Light.ColorPicker
                if iconType == IconType.Light
                else Path.IconPaths.Dark.ColorPicker
            ),
        )
        window.toolBox.setItemIcon(
            2,
            QIcon(
                Path.IconPaths.Light.InternalIcon
                if iconType == IconType.Light
                else Path.IconPaths.Dark.InternalIcon
            ),
        )
        window.toolBox.setItemIcon(
            3,
            QIcon(
                Path.IconPaths.Light.ExternalIcon
                if iconType == IconType.Light
                else Path.IconPaths.Dark.ExternalIcon
            ),
        )
        window.toolBox.setItemIcon(
            4,
            QIcon(
                Path.IconPaths.Light.AdvancedIcon
                if iconType == IconType.Light
                else Path.IconPaths.Dark.AdvancedIcon
            ),
        )
        window.chooseButton.setIcon(
            QIcon(
                Path.IconPaths.Light.FolderIcon
                if iconType == IconType.Light
                else Path.IconPaths.Dark.FolderIcon
            )
        )
        window.installButton.setIcon(
            QIcon(
                Path.IconPaths.Light.InstallIcon
                if iconType == IconType.Light
                else Path.IconPaths.Dark.InstallIcon
            )
        )
        window.uninstallButton.setIcon(
            QIcon(
                Path.IconPaths.Light.UninstallIcon
                if iconType == IconType.Light
                else Path.IconPaths.Dark.UninstallIcon
            )
        )
        window.runButton.setIcon(
            QIcon(
                Path.IconPaths.Light.RunIcon
                if iconType == IconType.Light
                else Path.IconPaths.Dark.RunIcon
            )
        )
        window.stopButton.setIcon(
            QIcon(
                Path.IconPaths.Light.StopIcon
                if iconType == IconType.Light
                else Path.IconPaths.Dark.StopIcon
            )
        )
        window.download_icon_label.setPixmap(
            QPixmap(
                Path.IconPaths.Light.DownloadIcon
                if iconType == IconType.Light
                else Path.IconPaths.Dark.DownloadIcon
            )
        )
        window.backButton.setIcon(
            QIcon(
                Path.IconPaths.Light.BackIcon
                if iconType == IconType.Light
                else Path.IconPaths.Dark.BackIcon
            )
        )
        window.blockListButton.setIcon(
            QIcon(
                Path.IconPaths.Light.CloseIcon
                if iconType == IconType.Light
                else Path.IconPaths.Dark.CloseIcon
            )
        )

        window.disabledListWidget.addButton.setIcon(
            QIcon(
                Path.IconPaths.Light.CheckIcon
                if iconType == IconType.Light
                else Path.IconPaths.Dark.CheckIcon
            )
        )

        # Stylesheet
        if iconType == IconType.Light:
            window.mainFrame.setStyleSheet(
                """
                QComboBox::down-arrow {
                    image: url("Assets/icons/light/down-arrow.png");
                }
                QSpinBox::up-button{
                    image: url("Assets/icons/light/up-arrow.png");
                }
                QSpinBox::down-button{
                    image: url("Assets/icons/light/down-arrow.png");
                }
            """
            )
        else:
            window.mainFrame.setStyleSheet(
                """
                QComboBox::down-arrow {
                    image: url("Assets/icons/dark/down-arrow.png");
                }
                QSpinBox::up-button{
                    image: url("Assets/icons/dark/up-arrow.png");
                }
                QSpinBox::down-button{
                    image: url("Assets/icons/dark/down-arrow.png");
                }
            """
            )

    @staticmethod
    def connectApplyButtons(window: Main) -> None:
        """
        Connect Apply Button to its respective functions
        Args:
            window (Main): Main window which has all the widgets
        """
        window.applyButton1.clicked.connect(lambda a: SaveSettings.Global.save(window))
        window.applyButton1.clicked.connect(lambda a: window.appliedWidget.start())
        window.applyButton2_1.clicked.connect(
            lambda a: SaveSettings.DropDown.save(window)
        )
        window.applyButton2_1.clicked.connect(lambda a: window.appliedWidget.start())
        window.applyButton2_2.clicked.connect(
            lambda a: SaveSettings.DropDown.Animation.save(window)
        )
        window.applyButton2_2.clicked.connect(lambda a: window.appliedWidget.start())
        window.applyButton3_1.clicked.connect(lambda a: SaveSettings.Menu.save(window))
        window.applyButton3_1.clicked.connect(lambda a: window.appliedWidget.start())
        window.applyButton3_2.clicked.connect(
            lambda a: SaveSettings.Menu.Animation.save(window)
        )
        window.applyButton3_2.clicked.connect(lambda a: window.appliedWidget.start())
        window.applyButton3_3.clicked.connect(
            lambda a: SaveSettings.Menu.Hot.save(window)
        )
        window.applyButton3_3.clicked.connect(lambda a: window.appliedWidget.start())
        window.applyButton3_4.clicked.connect(
            lambda a: SaveSettings.Menu.DisabledHot.save(window)
        )
        window.applyButton3_4.clicked.connect(lambda a: window.appliedWidget.start())
        window.applyButton3_5.clicked.connect(
            lambda a: SaveSettings.Menu.Focusing.save(window)
        )
        window.applyButton3_5.clicked.connect(lambda a: window.appliedWidget.start())
        window.applyButton3_6.clicked.connect(
            lambda a: SaveSettings.Menu.Separator.save(window)
        )
        window.applyButton3_6.clicked.connect(lambda a: window.appliedWidget.start())
        window.applyButton4.clicked.connect(lambda a: SaveSettings.Tooltip.save(window))
        window.applyButton4.clicked.connect(lambda a: window.appliedWidget.start())

    @staticmethod
    def connectResetButtons(window: Main) -> None:
        """
        Connect Reset Buttons to their respective methods:
        - Left Click to reset to default
        - Right Click to reset to last saved value
        Args:
            window (Main): Main window which has all the widgets
        """

        def configureResetButton(
            resetButton: QPushButton,
            valueWidget: QLineEdit | QComboBox | QSpinBox,
            defaultValue: str | int,
            savedValueName: str,
            colorPickerButton: QPushButton | None,
        ) -> None:
            def getSavedValue(valueVarAsString: str):
                """
                This methods retrieves the current value of the provided variable
                as a string
                Args:
                    valueVarAsString (str): Variable name as string
                """
                exec(f"val={valueVarAsString}")
                return locals()["val"]

            resetButton.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)

            if isinstance(valueWidget, QLineEdit):
                if colorPickerButton and isinstance(defaultValue, str):
                    resetButton.clicked.connect(
                        lambda a: valueWidget.setText(defaultValue)
                    )
                    resetButton.clicked.connect(
                        lambda a: colorPickerButton.setStyleSheet(
                            StyleSheet.buttoResetStyleSheet()
                        )
                    )
                    resetButton.clicked.connect(
                        lambda a: colorPickerButton.setIcon(
                            QIcon(Path.IconPaths.Light.ColorPicker)
                        )
                    )

                    resetButton.customContextMenuRequested.connect(
                        lambda a: valueWidget.setText(getSavedValue(savedValueName))
                    )
                    resetButton.customContextMenuRequested.connect(
                        lambda a: (
                            colorPickerButton.setStyleSheet(
                                StyleSheet.buttoResetStyleSheet()
                            )
                            if (getSavedValue(savedValueName) == "")
                            else ColorPicker.changeButtonColor(
                                getSavedValue(savedValueName), colorPickerButton
                            )
                        )
                    )
                    resetButton.customContextMenuRequested.connect(
                        lambda a: colorPickerButton.setIcon(
                            QIcon(Path.IconPaths.Light.ColorPicker)
                            if (getSavedValue(savedValueName) == "")
                            else QIcon("")
                        )
                    )
            elif isinstance(valueWidget, QComboBox):
                if isinstance(defaultValue, int):
                    resetButton.clicked.connect(
                        lambda a: valueWidget.setCurrentIndex(defaultValue)
                    )
                    resetButton.customContextMenuRequested.connect(
                        lambda a: valueWidget.setCurrentIndex(
                            getSavedValue(savedValueName)
                        )
                    )
            elif isinstance(valueWidget, QSpinBox):
                if isinstance(defaultValue, int):
                    resetButton.clicked.connect(
                        lambda a: valueWidget.setValue(defaultValue)
                    )
                    resetButton.customContextMenuRequested.connect(
                        lambda a: valueWidget.setValue(getSavedValue(savedValueName))
                    )

        # Global
        configureResetButton(
            resetButton=window.reset_effect_type1,
            valueWidget=window.effectType1,
            defaultValue=Defaults.Global.effectType,
            savedValueName=ClassVar.joinVars(ClassVar._global, ClassVar.effectType),
            colorPickerButton=None,
        )
        configureResetButton(
            resetButton=window.reset_corner_type1,
            valueWidget=window.cornerType1,
            defaultValue=Defaults.Global.cornerType,
            savedValueName=ClassVar.joinVars(ClassVar._global, ClassVar.cornerType),
            colorPickerButton=None,
        )
        configureResetButton(
            resetButton=window.reset_drop_shadow1,
            valueWidget=window.enableDropShadow1,
            defaultValue=Defaults.Global.enableDropShadow,
            savedValueName=ClassVar.joinVars(
                ClassVar._global, ClassVar.enableDropShadow
            ),
            colorPickerButton=None,
        )
        configureResetButton(
            resetButton=window.reset_theme_colorization1,
            valueWidget=window.enableThemeColorization1,
            defaultValue=Defaults.Global.enableThemeColorization,
            savedValueName=ClassVar.joinVars(
                ClassVar._global, ClassVar.enableThemeColorization
            ),
            colorPickerButton=None,
        )
        configureResetButton(
            resetButton=window.reset_dark_mode_theme_colorization_type1,
            valueWidget=window.darkModeThemeColorizationType1,
            defaultValue=Defaults.Global.darkModeThemeColorizationType,
            savedValueName=ClassVar.joinVars(
                ClassVar._global, ClassVar.darkModeThemeColorizationType
            ),
            colorPickerButton=None,
        )
        configureResetButton(
            resetButton=window.reset_light_mode_theme_colorization_type1,
            valueWidget=window.lightModeThemeColorizationType1,
            defaultValue=Defaults.Global.lightModeThemeColorizationType,
            savedValueName=ClassVar.joinVars(
                ClassVar._global, ClassVar.lightModeThemeColorizationType
            ),
            colorPickerButton=None,
        )
        configureResetButton(
            resetButton=window.reset_mini_dump,
            valueWidget=window.enableMiniDump,
            defaultValue=Defaults.Global.enableMiniDump,
            savedValueName=ClassVar.joinVars(ClassVar._global, ClassVar.enableMiniDump),
            colorPickerButton=None,
        )
        configureResetButton(
            resetButton=window.reset_border_color1,
            valueWidget=window.noBorderColor1,
            defaultValue=Defaults.Global.noBorderColor,
            savedValueName=ClassVar.joinVars(ClassVar._global, ClassVar.noBorderColor),
            colorPickerButton=None,
        )
        configureResetButton(
            resetButton=window.reset_dark_mode_border_color1,
            valueWidget=window.darkModeBorderColor1,
            defaultValue=Defaults.Global.darkModeBorderColor,
            savedValueName=ClassVar.joinVars(
                ClassVar._global, ClassVar.darkModeBorderColor
            ),
            colorPickerButton=window.dark_mode_border_color_picker1,
        )
        configureResetButton(
            resetButton=window.reset_light_mode_border_color1,
            valueWidget=window.lightModeBorderColor1,
            defaultValue=Defaults.Global.lightModeBorderColor,
            savedValueName=ClassVar.joinVars(
                ClassVar._global, ClassVar.lightModeBorderColor
            ),
            colorPickerButton=window.light_mode_border_color_picker1,
        )
        configureResetButton(
            resetButton=window.reset_dark_mode_gradient_color1,
            valueWidget=window.darkModeGradientColor1,
            defaultValue=Defaults.Global.darkModeGradientColor,
            savedValueName=ClassVar.joinVars(
                ClassVar._global, ClassVar.darkModeGradientColor
            ),
            colorPickerButton=window.dark_mode_gradient_color_picker1,
        )
        configureResetButton(
            resetButton=window.reset_light_mode_gradient_color1,
            valueWidget=window.lightModeGradientColor1,
            defaultValue=Defaults.Global.lightModeGradientColor,
            savedValueName=ClassVar.joinVars(
                ClassVar._global, ClassVar.lightModeGradientColor
            ),
            colorPickerButton=window.light_mode_gradient_color_picker1,
        )
        configureResetButton(
            resetButton=window.reset_disabled1,
            valueWidget=window.disabledEffect1,
            defaultValue=Defaults.Global.disabled,
            savedValueName=ClassVar.joinVars(ClassVar._global, ClassVar.disabled),
            colorPickerButton=None,
        )

        # DropDown-General
        configureResetButton(
            resetButton=window.reset_effect_type2,
            valueWidget=window.effectType2,
            defaultValue=Defaults.DropDown.effectType,
            savedValueName=ClassVar.joinVars(ClassVar.dropdown, ClassVar.effectType),
            colorPickerButton=None,
        )
        configureResetButton(
            resetButton=window.reset_corner_type2,
            valueWidget=window.cornerType2,
            defaultValue=Defaults.DropDown.cornerType,
            savedValueName=ClassVar.joinVars(ClassVar.dropdown, ClassVar.cornerType),
            colorPickerButton=None,
        )
        configureResetButton(
            resetButton=window.reset_drop_shadow2,
            valueWidget=window.enableDropShadow2,
            defaultValue=Defaults.DropDown.enableDropShadow,
            savedValueName=ClassVar.joinVars(
                ClassVar.dropdown, ClassVar.enableDropShadow
            ),
            colorPickerButton=None,
        )
        configureResetButton(
            resetButton=window.reset_fluent_animation1,
            valueWidget=window.enableFluentAnimation1,
            defaultValue=Defaults.DropDown.enableFluentAnimation,
            savedValueName=ClassVar.joinVars(
                ClassVar.dropdown, ClassVar.enableFluentAnimation
            ),
            colorPickerButton=None,
        )
        configureResetButton(
            resetButton=window.reset_theme_colorization2,
            valueWidget=window.enableThemeColorization2,
            defaultValue=Defaults.DropDown.enableThemeColorization,
            savedValueName=ClassVar.joinVars(
                ClassVar.dropdown, ClassVar.enableThemeColorization
            ),
            colorPickerButton=None,
        )
        configureResetButton(
            resetButton=window.reset_border_color2,
            valueWidget=window.noBorderColor2,
            defaultValue=Defaults.DropDown.noBorderColor,
            savedValueName=ClassVar.joinVars(ClassVar.dropdown, ClassVar.noBorderColor),
            colorPickerButton=None,
        )
        configureResetButton(
            resetButton=window.reset_dark_mode_border_color2,
            valueWidget=window.darkModeBorderColor2,
            defaultValue=Defaults.DropDown.darkModeBorderColor,
            savedValueName=ClassVar.joinVars(
                ClassVar.dropdown, ClassVar.darkModeBorderColor
            ),
            colorPickerButton=window.dark_mode_border_color_picker2,
        )
        configureResetButton(
            resetButton=window.reset_light_mode_border_color2,
            valueWidget=window.lightModeBorderColor2,
            defaultValue=Defaults.DropDown.lightModeBorderColor,
            savedValueName=ClassVar.joinVars(
                ClassVar.dropdown, ClassVar.lightModeBorderColor
            ),
            colorPickerButton=window.light_mode_border_color_picker2,
        )
        configureResetButton(
            resetButton=window.reset_dark_mode_gradient_color2,
            valueWidget=window.darkModeGradientColor2,
            defaultValue=Defaults.DropDown.darkModeGradientColor,
            savedValueName=ClassVar.joinVars(
                ClassVar.dropdown, ClassVar.darkModeGradientColor
            ),
            colorPickerButton=window.dark_mode_gradient_color_picker2,
        )
        configureResetButton(
            resetButton=window.reset_light_mode_gradient_color2,
            valueWidget=window.lightModeGradientColor2,
            defaultValue=Defaults.DropDown.lightModeGradientColor,
            savedValueName=ClassVar.joinVars(
                ClassVar.dropdown, ClassVar.lightModeGradientColor
            ),
            colorPickerButton=window.light_mode_gradient_color_picker2,
        )
        configureResetButton(
            resetButton=window.reset_disabled2,
            valueWidget=window.disabledEffect2,
            defaultValue=Defaults.DropDown.disabled,
            savedValueName=ClassVar.joinVars(ClassVar.dropdown, ClassVar.disabled),
            colorPickerButton=None,
        )

        # DropDown-Animation
        configureResetButton(
            resetButton=window.reset_fade_out_time1,
            valueWidget=window.fadeOutTime1,
            defaultValue=Defaults.DropDown.Animation.fadeOutTime,
            savedValueName=ClassVar.joinVars(
                ClassVar.dropdown, ClassVar.animation, ClassVar.fadeOutTime
            ),
            colorPickerButton=None,
        )
        configureResetButton(
            resetButton=window.reset_pop_in_time1,
            valueWidget=window.popInTime1,
            defaultValue=Defaults.DropDown.Animation.popInTime,
            savedValueName=ClassVar.joinVars(
                ClassVar.dropdown, ClassVar.animation, ClassVar.popInTime
            ),
            colorPickerButton=None,
        )
        configureResetButton(
            resetButton=window.reset_fade_in_time1,
            valueWidget=window.fadeInTime1,
            defaultValue=Defaults.DropDown.Animation.fadeInTime,
            savedValueName=ClassVar.joinVars(
                ClassVar.dropdown, ClassVar.animation, ClassVar.fadeInTime
            ),
            colorPickerButton=None,
        )
        configureResetButton(
            resetButton=window.reset_pop_in_style1,
            valueWidget=window.popInStyle1,
            defaultValue=Defaults.DropDown.Animation.popInStyle,
            savedValueName=ClassVar.joinVars(
                ClassVar.dropdown, ClassVar.animation, ClassVar.popInStyle
            ),
            colorPickerButton=None,
        )
        configureResetButton(
            resetButton=window.reset_start_ratio1,
            valueWidget=window.startRatio1,
            defaultValue=Defaults.DropDown.Animation.startRatio,
            savedValueName=ClassVar.joinVars(
                ClassVar.dropdown, ClassVar.animation, ClassVar.startRatio
            ),
            colorPickerButton=None,
        )
        configureResetButton(
            resetButton=window.reset_immediate_interupting1,
            valueWidget=window.enableImmediateInterupting1,
            defaultValue=Defaults.DropDown.Animation.enableImmediateInterupting,
            savedValueName=ClassVar.joinVars(
                ClassVar.dropdown,
                ClassVar.animation,
                ClassVar.enableImmediateInterupting,
            ),
            colorPickerButton=None,
        )

        # Menu-General
        configureResetButton(
            resetButton=window.reset_system_drop_shadow,
            valueWidget=window.noSystemDropShadow,
            defaultValue=Defaults.Menu.noSystemDropShadow,
            savedValueName=ClassVar.joinVars(
                ClassVar.menu, ClassVar.noSystemDropShadow
            ),
            colorPickerButton=None,
        )
        configureResetButton(
            resetButton=window.reset_immersive_style,
            valueWidget=window.enableImmersiveStyle,
            defaultValue=Defaults.Menu.enableImmersiveStyle,
            savedValueName=ClassVar.joinVars(
                ClassVar.menu, ClassVar.enableImmersiveStyle
            ),
            colorPickerButton=None,
        )
        configureResetButton(
            resetButton=window.reset_custom_rendering,
            valueWidget=window.enableCustomRendering,
            defaultValue=Defaults.Menu.enableCustomRendering,
            savedValueName=ClassVar.joinVars(
                ClassVar.menu, ClassVar.enableCustomRendering
            ),
            colorPickerButton=None,
        )
        configureResetButton(
            resetButton=window.reset_fluent_animation2,
            valueWidget=window.enableFluentAnimation2,
            defaultValue=Defaults.Menu.enableFluentAnimation,
            savedValueName=ClassVar.joinVars(
                ClassVar.menu, ClassVar.enableFluentAnimation
            ),
            colorPickerButton=None,
        )
        configureResetButton(
            resetButton=window.reset_modern_app_background_color,
            valueWidget=window.noModernAppBackgroundColor,
            defaultValue=Defaults.Menu.noModernAppBackgroundColor,
            savedValueName=ClassVar.joinVars(
                ClassVar.menu, ClassVar.noModernAppBackgroundColor
            ),
            colorPickerButton=None,
        )
        configureResetButton(
            resetButton=window.reset_color_treat_as_transparent,
            valueWidget=window.colorTreatAsTransparent,
            defaultValue=Defaults.Menu.colorTreatAsTransparent,
            savedValueName=ClassVar.joinVars(
                ClassVar.menu, ClassVar.colorTreatAsTransparent
            ),
            colorPickerButton=window.color_treat_as_transparent_color_picker,
        )
        configureResetButton(
            resetButton=window.reset_color_treat_as_transparent_threshold,
            valueWidget=window.colorTreatAsTransparentThreshold,
            defaultValue=Defaults.Menu.colorTreatAsTransparentThreshold,
            savedValueName=ClassVar.joinVars(
                ClassVar.menu, ClassVar.colorTreatAsTransparentThreshold
            ),
            colorPickerButton=None,
        )
        configureResetButton(
            resetButton=window.reset_effect_type3,
            valueWidget=window.effectType3,
            defaultValue=Defaults.Menu.effectType,
            savedValueName=ClassVar.joinVars(ClassVar.menu, ClassVar.effectType),
            colorPickerButton=None,
        )
        configureResetButton(
            resetButton=window.reset_corner_type3,
            valueWidget=window.cornerType3,
            defaultValue=Defaults.Menu.cornerType,
            savedValueName=ClassVar.joinVars(ClassVar.menu, ClassVar.cornerType),
            colorPickerButton=None,
        )

        configureResetButton(
            resetButton=window.reset_drop_shadow3,
            valueWidget=window.enableDropShadow3,
            defaultValue=Defaults.Menu.enableDropShadow,
            savedValueName=ClassVar.joinVars(ClassVar.menu, ClassVar.enableDropShadow),
            colorPickerButton=None,
        )
        configureResetButton(
            resetButton=window.reset_compatibility_mode,
            valueWidget=window.enableCompatibilityMode,
            defaultValue=Defaults.Menu.enableCompatibilityMode,
            savedValueName=ClassVar.joinVars(
                ClassVar.menu, ClassVar.enableCompatibilityMode
            ),
            colorPickerButton=None,
        )
        configureResetButton(
            resetButton=window.reset_theme_colorization3_1,
            valueWidget=window.enableThemeColorization3_1,
            defaultValue=Defaults.Menu.enableThemeColorization,
            savedValueName=ClassVar.joinVars(
                ClassVar.menu, ClassVar.enableThemeColorization
            ),
            colorPickerButton=None,
        )
        configureResetButton(
            resetButton=window.reset_dark_mode_theme_colorization_type2,
            valueWidget=window.darkModeThemeColorizationType2,
            defaultValue=Defaults.Menu.darkModeThemeColorizationType,
            savedValueName=ClassVar.joinVars(
                ClassVar.menu, ClassVar.darkModeThemeColorizationType
            ),
            colorPickerButton=None,
        )
        configureResetButton(
            resetButton=window.reset_light_mode_theme_colorization_type2,
            valueWidget=window.lightModeThemeColorizationType2,
            defaultValue=Defaults.Menu.lightModeThemeColorizationType,
            savedValueName=ClassVar.joinVars(
                ClassVar.menu, ClassVar.lightModeThemeColorizationType
            ),
            colorPickerButton=None,
        )
        configureResetButton(
            resetButton=window.reset_border_color3,
            valueWidget=window.noBorderColor3,
            defaultValue=Defaults.Menu.noBorderColor,
            savedValueName=ClassVar.joinVars(ClassVar.menu, ClassVar.noBorderColor),
            colorPickerButton=None,
        )
        configureResetButton(
            resetButton=window.reset_dark_mode_border_color3,
            valueWidget=window.darkModeBorderColor3,
            defaultValue=Defaults.Menu.darkModeBorderColor,
            savedValueName=ClassVar.joinVars(
                ClassVar.menu, ClassVar.darkModeBorderColor
            ),
            colorPickerButton=window.dark_mode_border_color_picker3,
        )

        configureResetButton(
            resetButton=window.reset_light_mode_border_color3,
            valueWidget=window.lightModeBorderColor3,
            defaultValue=Defaults.Menu.lightModeBorderColor,
            savedValueName=ClassVar.joinVars(
                ClassVar.menu, ClassVar.lightModeBorderColor
            ),
            colorPickerButton=window.light_mode_border_color_picker3,
        )
        configureResetButton(
            resetButton=window.reset_dark_mode_gradient_color3,
            valueWidget=window.darkModeGradientColor3,
            defaultValue=Defaults.Menu.darkModeGradientColor,
            savedValueName=ClassVar.joinVars(
                ClassVar.menu, ClassVar.darkModeGradientColor
            ),
            colorPickerButton=window.dark_mode_gradient_color_picker3,
        )
        configureResetButton(
            resetButton=window.reset_light_mode_gradient_color3,
            valueWidget=window.lightModeGradientColor3,
            defaultValue=Defaults.Menu.lightModeGradientColor,
            savedValueName=ClassVar.joinVars(
                ClassVar.menu, ClassVar.lightModeGradientColor
            ),
            colorPickerButton=window.light_mode_gradient_color_picker3,
        )
        configureResetButton(
            resetButton=window.reset_disabled3_1,
            valueWidget=window.disabledEffect3_1,
            defaultValue=Defaults.Menu.disabled,
            savedValueName=ClassVar.joinVars(ClassVar.menu, ClassVar.disabled),
            colorPickerButton=None,
        )

        # Menu-Animation
        configureResetButton(
            resetButton=window.reset_fade_out_time2,
            valueWidget=window.fadeOutTime2,
            defaultValue=Defaults.Menu.Animation.fadeOutTime,
            savedValueName=ClassVar.joinVars(
                ClassVar.menu, ClassVar.animation, ClassVar.fadeOutTime
            ),
            colorPickerButton=None,
        )
        configureResetButton(
            resetButton=window.reset_pop_in_time2,
            valueWidget=window.popInTime2,
            defaultValue=Defaults.Menu.Animation.popInTime,
            savedValueName=ClassVar.joinVars(
                ClassVar.menu, ClassVar.animation, ClassVar.popInTime
            ),
            colorPickerButton=None,
        )
        configureResetButton(
            resetButton=window.reset_fade_in_time2,
            valueWidget=window.fadeInTime2,
            defaultValue=Defaults.Menu.Animation.fadeInTime,
            savedValueName=ClassVar.joinVars(
                ClassVar.menu, ClassVar.animation, ClassVar.fadeInTime
            ),
            colorPickerButton=None,
        )
        configureResetButton(
            resetButton=window.reset_pop_in_style2,
            valueWidget=window.popInStyle2,
            defaultValue=Defaults.Menu.Animation.popInStyle,
            savedValueName=ClassVar.joinVars(
                ClassVar.menu, ClassVar.animation, ClassVar.popInStyle
            ),
            colorPickerButton=None,
        )
        configureResetButton(
            resetButton=window.reset_start_ratio2,
            valueWidget=window.startRatio2,
            defaultValue=Defaults.Menu.Animation.startRatio,
            savedValueName=ClassVar.joinVars(
                ClassVar.menu, ClassVar.animation, ClassVar.startRatio
            ),
            colorPickerButton=None,
        )
        configureResetButton(
            resetButton=window.reset_immediate_interupting2,
            valueWidget=window.enableImmediateInterupting2,
            defaultValue=Defaults.Menu.Animation.enableImmediateInterupting,
            savedValueName=ClassVar.joinVars(
                ClassVar.menu, ClassVar.animation, ClassVar.enableImmediateInterupting
            ),
            colorPickerButton=None,
        )
        # Menu-Hot
        configureResetButton(
            resetButton=window.reset_dark_mode_color1_1,
            valueWidget=window.darkModeColor1_1,
            defaultValue=Defaults.Menu.Hot.darkModeColor,
            savedValueName=ClassVar.joinVars(
                ClassVar.menu, ClassVar.hot, ClassVar.darkModeColor
            ),
            colorPickerButton=window.dark_mode_color_picker1_1,
        )
        configureResetButton(
            resetButton=window.reset_light_mode_color1_1,
            valueWidget=window.lightModeColor1_1,
            defaultValue=Defaults.Menu.Hot.lightModeColor,
            savedValueName=ClassVar.joinVars(
                ClassVar.menu, ClassVar.hot, ClassVar.lightModeColor
            ),
            colorPickerButton=window.light_mode_color_picker1_1,
        )
        configureResetButton(
            resetButton=window.reset_disabled3_2,
            valueWidget=window.disabledEffect3_2,
            defaultValue=Defaults.Menu.Hot.disabled,
            savedValueName=ClassVar.joinVars(
                ClassVar.menu, ClassVar.hot, ClassVar.disabled
            ),
            colorPickerButton=None,
        )
        configureResetButton(
            resetButton=window.reset_corner_radius1_1,
            valueWidget=window.cornerRadius1_1,
            defaultValue=Defaults.Menu.Hot.cornerRadius,
            savedValueName=ClassVar.joinVars(
                ClassVar.menu, ClassVar.hot, ClassVar.cornerRadius
            ),
            colorPickerButton=None,
        )
        configureResetButton(
            resetButton=window.reset_theme_colorization3_2,
            valueWidget=window.enableThemeColorization3_2,
            defaultValue=Defaults.Menu.Hot.enableThemeColorization,
            savedValueName=ClassVar.joinVars(
                ClassVar.menu, ClassVar.hot, ClassVar.enableThemeColorization
            ),
            colorPickerButton=None,
        )
        # Menu-Disabled Hot
        configureResetButton(
            resetButton=window.reset_dark_mode_color1_2,
            valueWidget=window.darkModeColor1_2,
            defaultValue=Defaults.Menu.DisabledHot.darkModeColor,
            savedValueName=ClassVar.joinVars(
                ClassVar.menu, ClassVar.disabledHot, ClassVar.darkModeColor
            ),
            colorPickerButton=window.dark_mode_color_picker1_2,
        )
        configureResetButton(
            resetButton=window.reset_light_mode_color1_2,
            valueWidget=window.lightModeColor1_2,
            defaultValue=Defaults.Menu.DisabledHot.lightModeColor,
            savedValueName=ClassVar.joinVars(
                ClassVar.menu, ClassVar.disabledHot, ClassVar.lightModeColor
            ),
            colorPickerButton=window.light_mode_color_picker1_2,
        )
        configureResetButton(
            resetButton=window.reset_disabled3_3,
            valueWidget=window.disabledEffect3_3,
            defaultValue=Defaults.Menu.DisabledHot.disabled,
            savedValueName=ClassVar.joinVars(
                ClassVar.menu, ClassVar.disabledHot, ClassVar.disabled
            ),
            colorPickerButton=None,
        )
        configureResetButton(
            resetButton=window.reset_corner_radius1_2,
            valueWidget=window.cornerRadius1_2,
            defaultValue=Defaults.Menu.DisabledHot.cornerRadius,
            savedValueName=ClassVar.joinVars(
                ClassVar.menu, ClassVar.disabledHot, ClassVar.cornerRadius
            ),
            colorPickerButton=None,
        )
        configureResetButton(
            resetButton=window.reset_theme_colorization3_3,
            valueWidget=window.enableThemeColorization3_3,
            defaultValue=Defaults.Menu.Hot.enableThemeColorization,
            savedValueName=ClassVar.joinVars(
                ClassVar.menu, ClassVar.disabledHot, ClassVar.enableThemeColorization
            ),
            colorPickerButton=None,
        )

        # Menu-Focusing
        configureResetButton(
            resetButton=window.reset_width1_1,
            valueWidget=window.width1_1,
            defaultValue=Defaults.Menu.Focusing.width,
            savedValueName=ClassVar.joinVars(
                ClassVar.menu, ClassVar.focusing, ClassVar.width
            ),
            colorPickerButton=None,
        )
        configureResetButton(
            resetButton=window.reset_dark_mode_color1_3,
            valueWidget=window.darkModeColor1_3,
            defaultValue=Defaults.Menu.Focusing.darkModeColor,
            savedValueName=ClassVar.joinVars(
                ClassVar.menu, ClassVar.focusing, ClassVar.darkModeColor
            ),
            colorPickerButton=window.dark_mode_color_picker1_3,
        )
        configureResetButton(
            resetButton=window.reset_light_mode_color1_3,
            valueWidget=window.lightModeColor1_3,
            defaultValue=Defaults.Menu.Focusing.lightModeColor,
            savedValueName=ClassVar.joinVars(
                ClassVar.menu, ClassVar.focusing, ClassVar.lightModeColor
            ),
            colorPickerButton=window.light_mode_color_picker1_3,
        )
        configureResetButton(
            resetButton=window.reset_disabled3_4,
            valueWidget=window.disabledEffect3_4,
            defaultValue=Defaults.Menu.Focusing.disabled,
            savedValueName=ClassVar.joinVars(
                ClassVar.menu, ClassVar.focusing, ClassVar.disabled
            ),
            colorPickerButton=None,
        )
        configureResetButton(
            resetButton=window.reset_corner_radius1_3,
            valueWidget=window.cornerRadius1_3,
            defaultValue=Defaults.Menu.Focusing.cornerRadius,
            savedValueName=ClassVar.joinVars(
                ClassVar.menu, ClassVar.focusing, ClassVar.cornerRadius
            ),
            colorPickerButton=None,
        )
        configureResetButton(
            resetButton=window.reset_theme_colorization3_4,
            valueWidget=window.enableThemeColorization3_4,
            defaultValue=Defaults.Menu.Focusing.enableThemeColorization,
            savedValueName=ClassVar.joinVars(
                ClassVar.menu, ClassVar.focusing, ClassVar.enableThemeColorization
            ),
            colorPickerButton=None,
        )

        # Menu-Separator
        configureResetButton(
            resetButton=window.reset_width1_2,
            valueWidget=window.width1_2,
            defaultValue=Defaults.Menu.Separator.width,
            savedValueName=ClassVar.joinVars(
                ClassVar.menu, ClassVar.separator, ClassVar.width
            ),
            colorPickerButton=None,
        )
        configureResetButton(
            resetButton=window.reset_dark_mode_color1_4,
            valueWidget=window.darkModeColor1_4,
            defaultValue=Defaults.Menu.Separator.darkModeColor,
            savedValueName=ClassVar.joinVars(
                ClassVar.menu, ClassVar.separator, ClassVar.darkModeColor
            ),
            colorPickerButton=window.dark_mode_color_picker1_4,
        )
        configureResetButton(
            resetButton=window.reset_light_mode_color1_4,
            valueWidget=window.lightModeColor1_4,
            defaultValue=Defaults.Menu.Separator.lightModeColor,
            savedValueName=ClassVar.joinVars(
                ClassVar.menu, ClassVar.separator, ClassVar.lightModeColor
            ),
            colorPickerButton=window.light_mode_color_picker1_4,
        )
        configureResetButton(
            resetButton=window.reset_disabled3_5,
            valueWidget=window.disabledEffect3_5,
            defaultValue=Defaults.Menu.Separator.disabled,
            savedValueName=ClassVar.joinVars(
                ClassVar.menu, ClassVar.separator, ClassVar.disabled
            ),
            colorPickerButton=None,
        )
        configureResetButton(
            resetButton=window.reset_corner_radius1_4,
            valueWidget=window.cornerRadius1_4,
            defaultValue=Defaults.Menu.Separator.cornerRadius,
            savedValueName=ClassVar.joinVars(
                ClassVar.menu, ClassVar.separator, ClassVar.cornerRadius
            ),
            colorPickerButton=None,
        )
        configureResetButton(
            resetButton=window.reset_theme_colorization3_5,
            valueWidget=window.enableThemeColorization3_5,
            defaultValue=Defaults.Menu.Separator.enableThemeColorization,
            savedValueName=ClassVar.joinVars(
                ClassVar.menu, ClassVar.separator, ClassVar.enableThemeColorization
            ),
            colorPickerButton=None,
        )

        # Tooltip
        configureResetButton(
            resetButton=window.reset_effect_type4,
            valueWidget=window.effectType4,
            defaultValue=Defaults.Tooltip.effectType,
            savedValueName=ClassVar.joinVars(ClassVar.tooltip, ClassVar.effectType),
            colorPickerButton=None,
        )
        configureResetButton(
            resetButton=window.reset_corner_type4,
            valueWidget=window.cornerType4,
            defaultValue=Defaults.Tooltip.cornerType,
            savedValueName=ClassVar.joinVars(ClassVar.tooltip, ClassVar.cornerType),
            colorPickerButton=None,
        )
        configureResetButton(
            resetButton=window.reset_drop_shadow4,
            valueWidget=window.enableDropShadow4,
            defaultValue=Defaults.Tooltip.enableDropShadow,
            savedValueName=ClassVar.joinVars(
                ClassVar.tooltip, ClassVar.enableDropShadow
            ),
            colorPickerButton=None,
        )
        configureResetButton(
            resetButton=window.reset_marginsType,
            valueWidget=window.marginsType,
            defaultValue=Defaults.Tooltip.marginsType,
            savedValueName=ClassVar.joinVars(ClassVar.tooltip, ClassVar.marginsType),
            colorPickerButton=None,
        )
        configureResetButton(
            resetButton=window.reset_margin,
            valueWidget=window.marginLeft,
            defaultValue=Defaults.Tooltip.marginLeft,
            savedValueName=ClassVar.joinVars(ClassVar.tooltip, ClassVar.marginLeft),
            colorPickerButton=None,
        )
        configureResetButton(
            resetButton=window.reset_margin,
            valueWidget=window.marginRight,
            defaultValue=Defaults.Tooltip.marginRight,
            savedValueName=ClassVar.joinVars(ClassVar.tooltip, ClassVar.marginRight),
            colorPickerButton=None,
        )
        configureResetButton(
            resetButton=window.reset_margin,
            valueWidget=window.marginTop,
            defaultValue=Defaults.Tooltip.marginTop,
            savedValueName=ClassVar.joinVars(ClassVar.tooltip, ClassVar.marginTop),
            colorPickerButton=None,
        )
        configureResetButton(
            resetButton=window.reset_margin,
            valueWidget=window.marginBottom,
            defaultValue=Defaults.Tooltip.marginBottom,
            savedValueName=ClassVar.joinVars(ClassVar.tooltip, ClassVar.marginBottom),
            colorPickerButton=None,
        )
        configureResetButton(
            resetButton=window.reset_theme_colorization4,
            valueWidget=window.enableThemeColorization4,
            defaultValue=Defaults.Tooltip.enableThemeColorization,
            savedValueName=ClassVar.joinVars(
                ClassVar.tooltip, ClassVar.enableThemeColorization
            ),
            colorPickerButton=None,
        )
        configureResetButton(
            resetButton=window.reset_border_color4,
            valueWidget=window.noBorderColor4,
            defaultValue=Defaults.Tooltip.noBorderColor,
            savedValueName=ClassVar.joinVars(ClassVar.tooltip, ClassVar.noBorderColor),
            colorPickerButton=None,
        )
        configureResetButton(
            resetButton=window.reset_dark_mode_color2,
            valueWidget=window.darkModeColor2,
            defaultValue=Defaults.Tooltip.darkModeColor,
            savedValueName=ClassVar.joinVars(ClassVar.tooltip, ClassVar.darkModeColor),
            colorPickerButton=window.dark_mode_color_picker2,
        )
        configureResetButton(
            resetButton=window.reset_light_mode_color2,
            valueWidget=window.lightModeColor2,
            defaultValue=Defaults.Tooltip.lightModeColor,
            savedValueName=ClassVar.joinVars(ClassVar.tooltip, ClassVar.lightModeColor),
            colorPickerButton=window.light_mode_color_picker2,
        )
        configureResetButton(
            resetButton=window.reset_dark_mode_border_color4,
            valueWidget=window.darkModeBorderColor4,
            defaultValue=Defaults.Tooltip.darkModeBorderColor,
            savedValueName=ClassVar.joinVars(
                ClassVar.tooltip, ClassVar.darkModeBorderColor
            ),
            colorPickerButton=window.dark_mode_border_color_picker4,
        )
        configureResetButton(
            resetButton=window.reset_light_mode_border_color4,
            valueWidget=window.lightModeBorderColor4,
            defaultValue=Defaults.Tooltip.lightModeBorderColor,
            savedValueName=ClassVar.joinVars(
                ClassVar.tooltip, ClassVar.lightModeBorderColor
            ),
            colorPickerButton=window.light_mode_border_color_picker4,
        )
        configureResetButton(
            resetButton=window.reset_dark_mode_gradient_color4,
            valueWidget=window.darkModeGradientColor4,
            defaultValue=Defaults.Tooltip.darkModeGradientColor,
            savedValueName=ClassVar.joinVars(
                ClassVar.tooltip, ClassVar.darkModeGradientColor
            ),
            colorPickerButton=window.dark_mode_gradient_color_picker4,
        )
        configureResetButton(
            resetButton=window.reset_light_mode_gradient_color4,
            valueWidget=window.lightModeGradientColor4,
            defaultValue=Defaults.Tooltip.lightModeGradientColor,
            savedValueName=ClassVar.joinVars(
                ClassVar.tooltip, ClassVar.lightModeGradientColor
            ),
            colorPickerButton=window.light_mode_gradient_color_picker4,
        )
        configureResetButton(
            resetButton=window.reset_disabled4,
            valueWidget=window.disabledEffect4,
            defaultValue=Defaults.Tooltip.disabled,
            savedValueName=ClassVar.joinVars(ClassVar.tooltip, ClassVar.disabled),
            colorPickerButton=None,
        )

    @staticmethod
    def connectDisabledListButtons(window: Main) -> None:
        """
        Connect Disabled List Buttons to:
        - Disabled List Dialog
        Args:
            window (Main): Main window which has all the widgets
        """
        window.disabledListButton1.clicked.connect(
            lambda: window.disabledListWidget.updateList(Saved.Global.disabledList)
        )
        window.disabledListButton1.clicked.connect(
            lambda: window.disabledListWidget.start(ListType.GlobalDisabledList)
        )
        window.disabledListButton2.clicked.connect(
            lambda: window.disabledListWidget.updateList(Saved.DropDown.disabledList)
        )
        window.disabledListButton2.clicked.connect(
            lambda: window.disabledListWidget.start(ListType.DropDownDisabledList)
        )
        window.disabledListButton3.clicked.connect(
            lambda: window.disabledListWidget.updateList(Saved.Menu.disabledList)
        )
        window.disabledListButton3.clicked.connect(
            lambda: window.disabledListWidget.start(ListType.MenuDisabledList)
        )
        window.disabledListButton4.clicked.connect(
            lambda: window.disabledListWidget.updateList(Saved.Tooltip.disabledList)
        )
        window.disabledListButton4.clicked.connect(
            lambda: window.disabledListWidget.start(ListType.TooltipDisabledList)
        )
        window.blockListButton.clicked.connect(
            lambda: window.disabledListWidget.updateList(Saved.Global.blockList)
        )
        window.blockListButton.clicked.connect(
            lambda: window.disabledListWidget.start(ListType.GlobalBlockList)
        )

    @staticmethod
    def connectColorPickers(window: Main) -> None:
        """
        Connect Color Picker Buttons to:
        - Color Picker Dialog
        Connect Color Picker Dialog to:
        - Color Output lineEdit
        Args:
            window (Main): Main window which has all the widgets
        """
        # Global
        ColorPicker.connectColorDialog(
            lineEdit=window.darkModeBorderColor1,
            pushButton=window.dark_mode_border_color_picker1,
        )
        ColorPicker.connectColorDialog(
            lineEdit=window.lightModeBorderColor1,
            pushButton=window.light_mode_border_color_picker1,
        )

        ColorPicker.connectColorDialog(
            lineEdit=window.darkModeGradientColor1,
            pushButton=window.dark_mode_gradient_color_picker1,
        )
        ColorPicker.connectColorDialog(
            lineEdit=window.lightModeGradientColor1,
            pushButton=window.light_mode_gradient_color_picker1,
        )

        # DropDown
        ColorPicker.connectColorDialog(
            lineEdit=window.darkModeBorderColor2,
            pushButton=window.dark_mode_border_color_picker2,
        )
        ColorPicker.connectColorDialog(
            lineEdit=window.lightModeBorderColor2,
            pushButton=window.light_mode_border_color_picker2,
        )

        ColorPicker.connectColorDialog(
            lineEdit=window.darkModeGradientColor2,
            pushButton=window.dark_mode_gradient_color_picker2,
        )
        ColorPicker.connectColorDialog(
            lineEdit=window.lightModeGradientColor2,
            pushButton=window.light_mode_gradient_color_picker2,
        )
        # Menu-General
        ColorPicker.connectColorDialog(
            lineEdit=window.colorTreatAsTransparent,
            pushButton=window.color_treat_as_transparent_color_picker,
        )
        ColorPicker.connectColorDialog(
            lineEdit=window.darkModeBorderColor3,
            pushButton=window.dark_mode_border_color_picker3,
        )
        ColorPicker.connectColorDialog(
            lineEdit=window.lightModeBorderColor3,
            pushButton=window.light_mode_border_color_picker3,
        )

        ColorPicker.connectColorDialog(
            lineEdit=window.darkModeGradientColor3,
            pushButton=window.dark_mode_gradient_color_picker3,
        )
        ColorPicker.connectColorDialog(
            lineEdit=window.lightModeGradientColor3,
            pushButton=window.light_mode_gradient_color_picker3,
        )

        # Menu Items-Hot
        ColorPicker.connectColorDialog(
            lineEdit=window.darkModeColor1_1,
            pushButton=window.dark_mode_color_picker1_1,
        )
        ColorPicker.connectColorDialog(
            lineEdit=window.lightModeColor1_1,
            pushButton=window.light_mode_color_picker1_1,
        )

        # Menu Items-Disabled Hot
        ColorPicker.connectColorDialog(
            lineEdit=window.darkModeColor1_2,
            pushButton=window.dark_mode_color_picker1_2,
        )
        ColorPicker.connectColorDialog(
            lineEdit=window.lightModeColor1_2,
            pushButton=window.light_mode_color_picker1_2,
        )

        # Menu Items-Focusing
        ColorPicker.connectColorDialog(
            lineEdit=window.darkModeColor1_3,
            pushButton=window.dark_mode_color_picker1_3,
        )
        ColorPicker.connectColorDialog(
            lineEdit=window.lightModeColor1_3,
            pushButton=window.light_mode_color_picker1_3,
        )

        # Menu Items-Separator
        ColorPicker.connectColorDialog(
            lineEdit=window.darkModeColor1_4,
            pushButton=window.dark_mode_color_picker1_4,
        )
        ColorPicker.connectColorDialog(
            lineEdit=window.lightModeColor1_4,
            pushButton=window.light_mode_color_picker1_4,
        )
        # Tooltip
        ColorPicker.connectColorDialog(
            lineEdit=window.darkModeColor2,
            pushButton=window.dark_mode_color_picker2,
        )
        ColorPicker.connectColorDialog(
            lineEdit=window.lightModeColor2,
            pushButton=window.light_mode_color_picker2,
        )
        ColorPicker.connectColorDialog(
            lineEdit=window.darkModeBorderColor4,
            pushButton=window.dark_mode_border_color_picker4,
        )
        ColorPicker.connectColorDialog(
            lineEdit=window.lightModeBorderColor4,
            pushButton=window.light_mode_border_color_picker4,
        )

        ColorPicker.connectColorDialog(
            lineEdit=window.darkModeGradientColor4,
            pushButton=window.dark_mode_gradient_color_picker4,
        )
        ColorPicker.connectColorDialog(
            lineEdit=window.lightModeGradientColor4,
            pushButton=window.light_mode_gradient_color_picker4,
        )

        # Appearance Settings
        ColorPicker.connectColorDialog(
            lineEdit=window.backgroundColor,
            pushButton=window.background_color_picker,
        )
        ColorPicker.connectColorDialog(
            lineEdit=window.secondaryBackgroundColor,
            pushButton=window.secondary_background_color_picker,
        )
        ColorPicker.connectColorDialog(
            lineEdit=window.labelColor,
            pushButton=window.label_color_picker,
        )
        ColorPicker.connectColorDialog(
            lineEdit=window.textColor,
            pushButton=window.text_color_picker,
        )

    @staticmethod
    def connectResetAllButtons(window: Main):
        """
        Method to handle left/right clicks on the Reset All Buttons
        Args:
        - window (Main): Main window of the whole application.
        """

        def simulateRightClick(widget: QPushButton):
            event = QContextMenuEvent(QContextMenuEvent.Reason.Mouse, widget.pos())
            QApplication.postEvent(widget, event)

        # Global
        window.resetAllButton1.setContextMenuPolicy(
            Qt.ContextMenuPolicy.CustomContextMenu
        )

        window.resetAllButton1.clicked.connect(window.reset_effect_type1.click)
        window.resetAllButton1.clicked.connect(window.reset_corner_type1.click)
        window.resetAllButton1.clicked.connect(window.reset_drop_shadow1.click)
        window.resetAllButton1.clicked.connect(window.reset_border_color1.click)
        window.resetAllButton1.clicked.connect(window.reset_theme_colorization1.click)
        window.resetAllButton1.clicked.connect(
            window.reset_dark_mode_theme_colorization_type1.click
        )
        window.resetAllButton1.clicked.connect(
            window.reset_light_mode_theme_colorization_type1.click
        )
        window.resetAllButton1.clicked.connect(
            window.reset_dark_mode_border_color1.click
        )
        window.resetAllButton1.clicked.connect(
            window.reset_light_mode_border_color1.click
        )
        window.resetAllButton1.clicked.connect(
            window.reset_dark_mode_gradient_color1.click
        )
        window.resetAllButton1.clicked.connect(
            window.reset_light_mode_gradient_color1.click
        )
        window.resetAllButton1.clicked.connect(window.reset_mini_dump.click)
        window.resetAllButton1.clicked.connect(window.reset_disabled1.click)

        window.resetAllButton1.customContextMenuRequested.connect(
            lambda: simulateRightClick(window.reset_effect_type1)
        )
        window.resetAllButton1.customContextMenuRequested.connect(
            lambda: simulateRightClick(window.reset_corner_type1)
        )
        window.resetAllButton1.customContextMenuRequested.connect(
            lambda: simulateRightClick(window.reset_drop_shadow1)
        )
        window.resetAllButton1.customContextMenuRequested.connect(
            lambda: simulateRightClick(window.reset_border_color1)
        )
        window.resetAllButton1.customContextMenuRequested.connect(
            lambda: simulateRightClick(window.reset_theme_colorization1)
        )
        window.resetAllButton1.customContextMenuRequested.connect(
            lambda: simulateRightClick(window.reset_dark_mode_theme_colorization_type1)
        )
        window.resetAllButton1.customContextMenuRequested.connect(
            lambda: simulateRightClick(window.reset_light_mode_theme_colorization_type1)
        )
        window.resetAllButton1.customContextMenuRequested.connect(
            lambda: simulateRightClick(window.reset_dark_mode_border_color1)
        )
        window.resetAllButton1.customContextMenuRequested.connect(
            lambda: simulateRightClick(window.reset_light_mode_border_color1)
        )
        window.resetAllButton1.customContextMenuRequested.connect(
            lambda: simulateRightClick(window.reset_dark_mode_gradient_color1)
        )
        window.resetAllButton1.customContextMenuRequested.connect(
            lambda: simulateRightClick(window.reset_light_mode_gradient_color1)
        )
        window.resetAllButton1.customContextMenuRequested.connect(
            lambda: simulateRightClick(window.reset_mini_dump)
        )
        window.resetAllButton1.customContextMenuRequested.connect(
            lambda: simulateRightClick(window.reset_disabled1)
        )

        # DropDown-General
        window.resetAllButton2_1.setContextMenuPolicy(
            Qt.ContextMenuPolicy.CustomContextMenu
        )

        window.resetAllButton2_1.clicked.connect(window.reset_effect_type2.click)
        window.resetAllButton2_1.clicked.connect(window.reset_corner_type2.click)
        window.resetAllButton2_1.clicked.connect(window.reset_drop_shadow2.click)
        window.resetAllButton2_1.clicked.connect(window.reset_fluent_animation1.click)
        window.resetAllButton2_1.clicked.connect(window.reset_border_color2.click)
        window.resetAllButton2_1.clicked.connect(window.reset_theme_colorization2.click)
        window.resetAllButton2_1.clicked.connect(
            window.reset_dark_mode_border_color2.click
        )
        window.resetAllButton2_1.clicked.connect(
            window.reset_light_mode_border_color2.click
        )
        window.resetAllButton2_1.clicked.connect(
            window.reset_dark_mode_gradient_color2.click
        )
        window.resetAllButton2_1.clicked.connect(
            window.reset_light_mode_gradient_color2.click
        )
        window.resetAllButton2_1.clicked.connect(window.reset_disabled2.click)

        window.resetAllButton2_1.customContextMenuRequested.connect(
            lambda: simulateRightClick(window.reset_effect_type2)
        )
        window.resetAllButton2_1.customContextMenuRequested.connect(
            lambda: simulateRightClick(window.reset_corner_type2)
        )
        window.resetAllButton2_1.customContextMenuRequested.connect(
            lambda: simulateRightClick(window.reset_drop_shadow2)
        )
        window.resetAllButton2_1.customContextMenuRequested.connect(
            lambda: simulateRightClick(window.reset_fluent_animation1)
        )
        window.resetAllButton2_1.customContextMenuRequested.connect(
            lambda: simulateRightClick(window.reset_border_color2)
        )
        window.resetAllButton2_1.customContextMenuRequested.connect(
            lambda: simulateRightClick(window.reset_theme_colorization2)
        )
        window.resetAllButton2_1.customContextMenuRequested.connect(
            lambda: simulateRightClick(window.reset_dark_mode_border_color2)
        )
        window.resetAllButton2_1.customContextMenuRequested.connect(
            lambda: simulateRightClick(window.reset_light_mode_border_color2)
        )
        window.resetAllButton2_1.customContextMenuRequested.connect(
            lambda: simulateRightClick(window.reset_dark_mode_gradient_color2)
        )
        window.resetAllButton2_1.customContextMenuRequested.connect(
            lambda: simulateRightClick(window.reset_light_mode_gradient_color2)
        )
        window.resetAllButton2_1.customContextMenuRequested.connect(
            lambda: simulateRightClick(window.reset_disabled2)
        )

        # DropDown-Animation
        window.resetAllButton2_2.setContextMenuPolicy(
            Qt.ContextMenuPolicy.CustomContextMenu
        )

        window.resetAllButton2_2.clicked.connect(window.reset_fade_out_time1.click)
        window.resetAllButton2_2.clicked.connect(window.reset_pop_in_time1.click)
        window.resetAllButton2_2.clicked.connect(window.reset_fade_in_time1.click)
        window.resetAllButton2_2.clicked.connect(window.reset_pop_in_style1.click)
        window.resetAllButton2_2.clicked.connect(window.reset_start_ratio1.click)
        window.resetAllButton2_2.clicked.connect(
            window.reset_immediate_interupting1.click
        )

        window.resetAllButton2_2.customContextMenuRequested.connect(
            lambda: simulateRightClick(window.reset_fade_out_time1)
        )
        window.resetAllButton2_2.customContextMenuRequested.connect(
            lambda: simulateRightClick(window.reset_pop_in_time1)
        )
        window.resetAllButton2_2.customContextMenuRequested.connect(
            lambda: simulateRightClick(window.reset_fade_in_time1)
        )
        window.resetAllButton2_2.customContextMenuRequested.connect(
            lambda: simulateRightClick(window.reset_pop_in_style1)
        )
        window.resetAllButton2_2.customContextMenuRequested.connect(
            lambda: simulateRightClick(window.reset_start_ratio1)
        )
        window.resetAllButton2_2.customContextMenuRequested.connect(
            lambda: simulateRightClick(window.reset_immediate_interupting1)
        )

        # Menu-General
        window.resetAllButton3_1.setContextMenuPolicy(
            Qt.ContextMenuPolicy.CustomContextMenu
        )

        window.resetAllButton3_1.clicked.connect(window.reset_system_drop_shadow.click)
        window.resetAllButton3_1.clicked.connect(window.reset_immersive_style.click)
        window.resetAllButton3_1.clicked.connect(window.reset_custom_rendering.click)
        window.resetAllButton3_1.clicked.connect(window.reset_fluent_animation2.click)
        window.resetAllButton3_1.clicked.connect(window.reset_compatibility_mode.click)
        window.resetAllButton3_1.clicked.connect(
            window.reset_modern_app_background_color.click
        )
        window.resetAllButton3_1.clicked.connect(
            window.reset_color_treat_as_transparent.click
        )
        window.resetAllButton3_1.clicked.connect(
            window.reset_color_treat_as_transparent_threshold.click
        )
        window.resetAllButton3_1.clicked.connect(window.reset_effect_type3.click)
        window.resetAllButton3_1.clicked.connect(window.reset_corner_type3.click)
        window.resetAllButton3_1.clicked.connect(window.reset_drop_shadow3.click)
        window.resetAllButton3_1.clicked.connect(window.reset_border_color3.click)
        window.resetAllButton3_1.clicked.connect(
            window.reset_theme_colorization3_1.click
        )
        window.resetAllButton3_1.clicked.connect(
            window.reset_dark_mode_theme_colorization_type1.click
        )
        window.resetAllButton3_1.clicked.connect(
            window.reset_light_mode_theme_colorization_type2.click
        )
        window.resetAllButton3_1.clicked.connect(
            window.reset_dark_mode_border_color3.click
        )
        window.resetAllButton3_1.clicked.connect(
            window.reset_light_mode_border_color3.click
        )
        window.resetAllButton3_1.clicked.connect(
            window.reset_dark_mode_gradient_color3.click
        )
        window.resetAllButton3_1.clicked.connect(
            window.reset_light_mode_gradient_color3.click
        )
        window.resetAllButton3_1.clicked.connect(window.reset_disabled3_1.click)

        window.resetAllButton3_1.customContextMenuRequested.connect(
            lambda: simulateRightClick(window.reset_system_drop_shadow)
        )
        window.resetAllButton3_1.customContextMenuRequested.connect(
            lambda: simulateRightClick(window.reset_immersive_style)
        )
        window.resetAllButton3_1.customContextMenuRequested.connect(
            lambda: simulateRightClick(window.reset_custom_rendering)
        )
        window.resetAllButton3_1.customContextMenuRequested.connect(
            lambda: simulateRightClick(window.reset_fluent_animation2)
        )
        window.resetAllButton3_1.customContextMenuRequested.connect(
            lambda: simulateRightClick(window.reset_compatibility_mode)
        )
        window.resetAllButton3_1.customContextMenuRequested.connect(
            lambda: simulateRightClick(window.reset_modern_app_background_color)
        )
        window.resetAllButton3_1.customContextMenuRequested.connect(
            lambda: simulateRightClick(window.reset_color_treat_as_transparent)
        )
        window.resetAllButton3_1.customContextMenuRequested.connect(
            lambda: simulateRightClick(
                window.reset_color_treat_as_transparent_threshold
            )
        )
        window.resetAllButton3_1.customContextMenuRequested.connect(
            lambda: simulateRightClick(window.reset_effect_type3)
        )
        window.resetAllButton3_1.customContextMenuRequested.connect(
            lambda: simulateRightClick(window.reset_corner_type3)
        )
        window.resetAllButton3_1.customContextMenuRequested.connect(
            lambda: simulateRightClick(window.reset_drop_shadow3)
        )
        window.resetAllButton3_1.customContextMenuRequested.connect(
            lambda: simulateRightClick(window.reset_border_color3)
        )
        window.resetAllButton3_1.customContextMenuRequested.connect(
            lambda: simulateRightClick(window.reset_theme_colorization3_1)
        )
        window.resetAllButton3_1.customContextMenuRequested.connect(
            lambda: simulateRightClick(window.reset_dark_mode_theme_colorization_type1)
        )
        window.resetAllButton3_1.customContextMenuRequested.connect(
            lambda: simulateRightClick(window.reset_light_mode_theme_colorization_type2)
        )
        window.resetAllButton3_1.customContextMenuRequested.connect(
            lambda: simulateRightClick(window.reset_dark_mode_border_color3)
        )
        window.resetAllButton3_1.customContextMenuRequested.connect(
            lambda: simulateRightClick(window.reset_light_mode_border_color3)
        )
        window.resetAllButton3_1.customContextMenuRequested.connect(
            lambda: simulateRightClick(window.reset_dark_mode_gradient_color3)
        )
        window.resetAllButton3_1.customContextMenuRequested.connect(
            lambda: simulateRightClick(window.reset_light_mode_gradient_color3)
        )
        window.resetAllButton3_1.customContextMenuRequested.connect(
            lambda: simulateRightClick(window.reset_disabled3_1)
        )

        # Menu-Animation
        window.resetAllButton3_2.setContextMenuPolicy(
            Qt.ContextMenuPolicy.CustomContextMenu
        )

        window.resetAllButton3_2.clicked.connect(window.reset_fade_out_time2.click)
        window.resetAllButton3_2.clicked.connect(window.reset_pop_in_time2.click)
        window.resetAllButton3_2.clicked.connect(window.reset_fade_in_time2.click)
        window.resetAllButton3_2.clicked.connect(window.reset_pop_in_style2.click)
        window.resetAllButton3_2.clicked.connect(window.reset_start_ratio2.click)
        window.resetAllButton3_2.clicked.connect(
            window.reset_immediate_interupting2.click
        )

        window.resetAllButton3_2.customContextMenuRequested.connect(
            lambda: simulateRightClick(window.reset_fade_out_time2)
        )
        window.resetAllButton3_2.customContextMenuRequested.connect(
            lambda: simulateRightClick(window.reset_pop_in_time2)
        )
        window.resetAllButton3_2.customContextMenuRequested.connect(
            lambda: simulateRightClick(window.reset_fade_in_time2)
        )
        window.resetAllButton3_2.customContextMenuRequested.connect(
            lambda: simulateRightClick(window.reset_pop_in_style2)
        )
        window.resetAllButton3_2.customContextMenuRequested.connect(
            lambda: simulateRightClick(window.reset_start_ratio2)
        )
        window.resetAllButton3_2.customContextMenuRequested.connect(
            lambda: simulateRightClick(window.reset_immediate_interupting2)
        )

        # Menu-Hot
        window.resetAllButton3_3.setContextMenuPolicy(
            Qt.ContextMenuPolicy.CustomContextMenu
        )

        window.resetAllButton3_3.clicked.connect(window.reset_dark_mode_color1_1.click)
        window.resetAllButton3_3.clicked.connect(window.reset_light_mode_color1_1.click)
        window.resetAllButton3_3.clicked.connect(window.reset_disabled3_2.click)
        window.resetAllButton3_3.clicked.connect(window.reset_corner_radius1_1.click)
        window.resetAllButton3_3.clicked.connect(
            window.reset_theme_colorization3_2.click
        )

        window.resetAllButton3_3.customContextMenuRequested.connect(
            lambda: simulateRightClick(window.reset_dark_mode_color1_1)
        )
        window.resetAllButton3_3.customContextMenuRequested.connect(
            lambda: simulateRightClick(window.reset_light_mode_color1_1)
        )
        window.resetAllButton3_3.customContextMenuRequested.connect(
            lambda: simulateRightClick(window.reset_disabled3_2)
        )
        window.resetAllButton3_3.customContextMenuRequested.connect(
            lambda: simulateRightClick(window.reset_corner_radius1_1)
        )
        window.resetAllButton3_3.customContextMenuRequested.connect(
            lambda: simulateRightClick(window.reset_theme_colorization3_2)
        )

        # Menu-DisabledHot
        window.resetAllButton3_4.setContextMenuPolicy(
            Qt.ContextMenuPolicy.CustomContextMenu
        )

        window.resetAllButton3_4.clicked.connect(window.reset_dark_mode_color1_2.click)
        window.resetAllButton3_4.clicked.connect(window.reset_light_mode_color1_2.click)
        window.resetAllButton3_4.clicked.connect(window.reset_disabled3_3.click)
        window.resetAllButton3_4.clicked.connect(window.reset_corner_radius1_2.click)
        window.resetAllButton3_4.clicked.connect(
            window.reset_theme_colorization3_3.click
        )

        window.resetAllButton3_4.customContextMenuRequested.connect(
            lambda: simulateRightClick(window.reset_dark_mode_color1_2)
        )
        window.resetAllButton3_4.customContextMenuRequested.connect(
            lambda: simulateRightClick(window.reset_light_mode_color1_2)
        )
        window.resetAllButton3_4.customContextMenuRequested.connect(
            lambda: simulateRightClick(window.reset_disabled3_3)
        )
        window.resetAllButton3_4.customContextMenuRequested.connect(
            lambda: simulateRightClick(window.reset_corner_radius1_2)
        )
        window.resetAllButton3_4.customContextMenuRequested.connect(
            lambda: simulateRightClick(window.reset_theme_colorization3_3)
        )

        # Menu-Focusing
        window.resetAllButton3_5.setContextMenuPolicy(
            Qt.ContextMenuPolicy.CustomContextMenu
        )

        window.resetAllButton3_5.clicked.connect(window.reset_width1_1.click)
        window.resetAllButton3_5.clicked.connect(window.reset_dark_mode_color1_3.click)
        window.resetAllButton3_5.clicked.connect(window.reset_light_mode_color1_3.click)
        window.resetAllButton3_5.clicked.connect(window.reset_disabled3_4.click)
        window.resetAllButton3_5.clicked.connect(window.reset_corner_radius1_3.click)
        window.resetAllButton3_5.clicked.connect(
            window.reset_theme_colorization3_4.click
        )

        window.resetAllButton3_5.customContextMenuRequested.connect(
            lambda: simulateRightClick(window.reset_width1_1)
        )
        window.resetAllButton3_5.customContextMenuRequested.connect(
            lambda: simulateRightClick(window.reset_dark_mode_color1_3)
        )
        window.resetAllButton3_5.customContextMenuRequested.connect(
            lambda: simulateRightClick(window.reset_light_mode_color1_3)
        )
        window.resetAllButton3_5.customContextMenuRequested.connect(
            lambda: simulateRightClick(window.reset_disabled3_4)
        )
        window.resetAllButton3_5.customContextMenuRequested.connect(
            lambda: simulateRightClick(window.reset_corner_radius1_3)
        )
        window.resetAllButton3_5.customContextMenuRequested.connect(
            lambda: simulateRightClick(window.reset_theme_colorization3_4)
        )

        # Menu-Separator
        window.resetAllButton3_6.setContextMenuPolicy(
            Qt.ContextMenuPolicy.CustomContextMenu
        )

        window.resetAllButton3_6.clicked.connect(window.reset_width1_2.click)
        window.resetAllButton3_6.clicked.connect(window.reset_dark_mode_color1_4.click)
        window.resetAllButton3_6.clicked.connect(window.reset_light_mode_color1_4.click)
        window.resetAllButton3_6.clicked.connect(window.reset_disabled3_5.click)
        window.resetAllButton3_6.clicked.connect(window.reset_corner_radius1_4.click)
        window.resetAllButton3_6.clicked.connect(
            window.reset_theme_colorization3_5.click
        )

        window.resetAllButton3_6.customContextMenuRequested.connect(
            lambda: simulateRightClick(window.reset_width1_2)
        )
        window.resetAllButton3_6.customContextMenuRequested.connect(
            lambda: simulateRightClick(window.reset_dark_mode_color1_4)
        )
        window.resetAllButton3_6.customContextMenuRequested.connect(
            lambda: simulateRightClick(window.reset_light_mode_color1_4)
        )
        window.resetAllButton3_6.customContextMenuRequested.connect(
            lambda: simulateRightClick(window.reset_disabled3_5)
        )
        window.resetAllButton3_6.customContextMenuRequested.connect(
            lambda: simulateRightClick(window.reset_corner_radius1_4)
        )
        window.resetAllButton3_6.customContextMenuRequested.connect(
            lambda: simulateRightClick(window.reset_theme_colorization3_5)
        )

        # Tooltip
        window.resetAllButton4.setContextMenuPolicy(
            Qt.ContextMenuPolicy.CustomContextMenu
        )

        window.resetAllButton4.clicked.connect(window.reset_effect_type4.click)
        window.resetAllButton4.clicked.connect(window.reset_corner_type4.click)
        window.resetAllButton4.clicked.connect(window.reset_drop_shadow4.click)
        window.resetAllButton4.clicked.connect(window.reset_border_color4.click)
        window.resetAllButton4.clicked.connect(window.reset_theme_colorization4.click)
        window.resetAllButton4.clicked.connect(window.reset_marginsType.click)
        window.resetAllButton4.clicked.connect(window.reset_margin.click)
        window.resetAllButton4.clicked.connect(window.reset_dark_mode_color2.click)
        window.resetAllButton4.clicked.connect(window.reset_light_mode_color2.click)
        window.resetAllButton4.clicked.connect(
            window.reset_dark_mode_border_color4.click
        )
        window.resetAllButton4.clicked.connect(
            window.reset_light_mode_border_color4.click
        )
        window.resetAllButton4.clicked.connect(
            window.reset_dark_mode_gradient_color4.click
        )
        window.resetAllButton4.clicked.connect(
            window.reset_light_mode_gradient_color4.click
        )
        window.resetAllButton4.clicked.connect(window.reset_disabled4.click)

        window.resetAllButton4.customContextMenuRequested.connect(
            lambda: simulateRightClick(window.reset_effect_type4)
        )
        window.resetAllButton4.customContextMenuRequested.connect(
            lambda: simulateRightClick(window.reset_corner_type4)
        )
        window.resetAllButton4.customContextMenuRequested.connect(
            lambda: simulateRightClick(window.reset_drop_shadow4)
        )
        window.resetAllButton4.customContextMenuRequested.connect(
            lambda: simulateRightClick(window.reset_border_color4)
        )
        window.resetAllButton4.customContextMenuRequested.connect(
            lambda: simulateRightClick(window.reset_theme_colorization4)
        )
        window.resetAllButton4.customContextMenuRequested.connect(
            lambda: simulateRightClick(window.reset_marginsType)
        )
        window.resetAllButton4.customContextMenuRequested.connect(
            lambda: simulateRightClick(window.reset_margin)
        )
        window.resetAllButton4.customContextMenuRequested.connect(
            lambda: simulateRightClick(window.reset_dark_mode_color2)
        )
        window.resetAllButton4.customContextMenuRequested.connect(
            lambda: simulateRightClick(window.reset_light_mode_color2)
        )
        window.resetAllButton4.customContextMenuRequested.connect(
            lambda: simulateRightClick(window.reset_dark_mode_border_color4)
        )
        window.resetAllButton4.customContextMenuRequested.connect(
            lambda: simulateRightClick(window.reset_light_mode_border_color4)
        )
        window.resetAllButton4.customContextMenuRequested.connect(
            lambda: simulateRightClick(window.reset_dark_mode_gradient_color4)
        )
        window.resetAllButton4.customContextMenuRequested.connect(
            lambda: simulateRightClick(window.reset_light_mode_gradient_color4)
        )
        window.resetAllButton4.customContextMenuRequested.connect(
            lambda: simulateRightClick(window.reset_disabled4)
        )

    @staticmethod
    def connectMouseEvent(window: Main) -> None:
        """
        Method to handle mouse hover and clicks on parameters
        - Handles mouse enter event
        - Handles mouse leave event
        - Handles mouse press event
        Args:
            window (Main): Main window which has all the widgets
        """

        def labelEnterEvent(label: QLabel) -> None:
            font = label.font()
            font.setUnderline(True)
            label.setFont(font)

        def labelLeaveEvent(label: QLabel) -> None:
            font = label.font()
            font.setUnderline(False)
            label.setFont(font)

        def labelMousePressEvent(
            event: QMouseEvent | None, parameterType: str, height: int
        ) -> None:
            _translate = translationVar.translateFrom
            if event is not None and event.buttons() == Qt.MouseButton.LeftButton:
                window.infoWidget.title.setText(_translate(parameterType))
                if parameterType == Key.effectType:
                    if window.mainTabWidget.currentIndex() == MainTab.Global:
                        window.infoWidget.description.setText(Description.effectType())
                        window.infoWidget.widget.setGeometry(
                            0,
                            window.mainFrame.height() - height + 50,
                            window.mainFrame.width(),
                            height,
                        )
                    else:
                        window.infoWidget.description.setText(
                            Description.effectType(True)
                        )
                        window.infoWidget.widget.setGeometry(
                            0,
                            window.mainFrame.height() - height + 40,
                            window.mainFrame.width(),
                            height + 10,
                        )

                elif parameterType == Key.cornerType:
                    if window.mainTabWidget.currentIndex() == MainTab.Global:
                        window.infoWidget.description.setText(Description.cornerType())
                        window.infoWidget.widget.setGeometry(
                            0,
                            window.mainFrame.height() - height + 50,
                            window.mainFrame.width(),
                            height,
                        )
                    else:
                        window.infoWidget.description.setText(
                            Description.cornerType(True)
                        )
                        window.infoWidget.widget.setGeometry(
                            0,
                            window.mainFrame.height() - height + 40,
                            window.mainFrame.width(),
                            height + 10,
                        )

                elif parameterType == Key.enableDropShadow:
                    if window.mainTabWidget.currentIndex() == MainTab.Global:
                        window.infoWidget.widget.setGeometry(
                            0,
                            window.mainFrame.height() - height + 50,
                            window.mainFrame.width(),
                            height,
                        )
                        window.infoWidget.description.setText(
                            Description.enableDropShadow()
                        )
                        window.infoWidget.widget.setGeometry(
                            0,
                            window.mainFrame.height() - height + 50,
                            window.mainFrame.width(),
                            height,
                        )
                    else:
                        window.infoWidget.description.setText(
                            Description.enableDropShadow(True)
                        )
                        window.infoWidget.widget.setGeometry(
                            0,
                            window.mainFrame.height() - height + 40,
                            window.mainFrame.width(),
                            height + 10,
                        )

                elif parameterType == Key.noBorderColor:
                    if window.mainTabWidget.currentIndex() == MainTab.Global:
                        window.infoWidget.widget.setGeometry(
                            0,
                            window.mainFrame.height() - height + 50,
                            window.mainFrame.width(),
                            height,
                        )
                        window.infoWidget.description.setText(
                            Description.noBorderColor()
                        )
                        window.infoWidget.widget.setGeometry(
                            0,
                            window.mainFrame.height() - height + 50,
                            window.mainFrame.width(),
                            height,
                        )
                    else:
                        window.infoWidget.description.setText(
                            Description.noBorderColor(True)
                        )
                        window.infoWidget.widget.setGeometry(
                            0,
                            window.mainFrame.height() - height + 40,
                            window.mainFrame.width(),
                            height + 10,
                        )

                elif parameterType == Key.enableThemeColorization:
                    if window.mainTabWidget.currentIndex() == MainTab.Global:
                        window.infoWidget.widget.setGeometry(
                            0,
                            window.mainFrame.height() - height + 50,
                            window.mainFrame.width(),
                            height,
                        )
                        window.infoWidget.description.setText(
                            Description.enableThemeColorization()
                        )
                        window.infoWidget.widget.setGeometry(
                            0,
                            window.mainFrame.height() - height + 50,
                            window.mainFrame.width(),
                            height,
                        )
                    else:
                        window.infoWidget.description.setText(
                            Description.enableThemeColorization(True)
                        )
                        window.infoWidget.widget.setGeometry(
                            0,
                            window.mainFrame.height() - height + 40,
                            window.mainFrame.width(),
                            height + 10,
                        )

                elif parameterType == Key.darkModeThemeColorizationType:
                    window.infoWidget.description.setText(
                        Description.darkModeThemeColorizationType()
                    )
                    window.infoWidget.widget.setGeometry(
                        0,
                        window.mainFrame.height() - height + 40,
                        window.mainFrame.width(),
                        height,
                    )

                elif parameterType == Key.lightModeThemeColorizationType:
                    window.infoWidget.description.setText(
                        Description.lightModeThemeColorizationType()
                    )
                    window.infoWidget.widget.setGeometry(
                        0,
                        window.mainFrame.height() - height + 40,
                        window.mainFrame.width(),
                        height,
                    )

                elif parameterType == Key.enableMiniDump:
                    window.infoWidget.description.setText(Description.enableMiniDump())
                    window.infoWidget.widget.setGeometry(
                        0,
                        window.mainFrame.height() - height + 40,
                        window.mainFrame.width(),
                        height,
                    )

                elif parameterType == Key.enableCompatibilityMode:
                    window.infoWidget.description.setText(
                        Description.enableCompatibilityMode()
                    )
                    window.infoWidget.widget.setGeometry(
                        0,
                        window.mainFrame.height() - height + 50,
                        window.mainFrame.width(),
                        height,
                    )

                elif parameterType == Key.marginsType:
                    window.infoWidget.description.setText(Description.marginsType())
                    window.infoWidget.widget.setGeometry(
                        0,
                        window.mainFrame.height() - height + 40,
                        window.mainFrame.width(),
                        height,
                    )

                elif parameterType == Key.margin:
                    window.infoWidget.description.setText(Description.margin())
                    window.infoWidget.widget.setGeometry(
                        0,
                        window.mainFrame.height() - height + 40,
                        window.mainFrame.width(),
                        height,
                    )

                elif parameterType == Key.textColor:
                    window.infoWidget.description.setText(Description.textColor())
                    window.infoWidget.widget.setGeometry(
                        0,
                        window.mainFrame.height() - height + 50,
                        window.mainFrame.width(),
                        height,
                    )

                elif parameterType == Key.borderColor:
                    window.infoWidget.description.setText(Description.borderColor())
                    window.infoWidget.widget.setGeometry(
                        0,
                        window.mainFrame.height() - height + 50,
                        window.mainFrame.width(),
                        height,
                    )

                elif parameterType == Key.textColor:
                    window.infoWidget.description.setText(Description.gradientColor())
                    window.infoWidget.widget.setGeometry(
                        0,
                        window.mainFrame.height() - height + 50,
                        window.mainFrame.width(),
                        height,
                    )

                elif parameterType == Key.darkModeBorderColor:
                    window.infoWidget.description.setText(
                        Description.darkModeBorderColor()
                    )
                    window.infoWidget.widget.setGeometry(
                        0,
                        window.mainFrame.height() - height + 50,
                        window.mainFrame.width(),
                        height,
                    )

                elif parameterType == Key.lightModeBorderColor:
                    window.infoWidget.description.setText(
                        Description.lightModeBorderColor()
                    )
                    window.infoWidget.widget.setGeometry(
                        0,
                        window.mainFrame.height() - height + 50,
                        window.mainFrame.width(),
                        height,
                    )

                elif parameterType == Key.darkModeGradientColor:
                    window.infoWidget.description.setText(
                        Description.darkModeGradientColor()
                    )
                    window.infoWidget.widget.setGeometry(
                        0,
                        window.mainFrame.height() - height + 50,
                        window.mainFrame.width(),
                        height,
                    )

                elif parameterType == Key.lightModeGradientColor:
                    window.infoWidget.description.setText(
                        Description.lightModeGradientColor()
                    )
                    window.infoWidget.widget.setGeometry(
                        0,
                        window.mainFrame.height() - height + 50,
                        window.mainFrame.width(),
                        height,
                    )

                elif parameterType == Key.disabled:
                    if window.mainTabWidget.currentIndex() == MainTab.Global:
                        window.infoWidget.widget.setGeometry(
                            0,
                            window.mainFrame.height() - height + 50,
                            window.mainFrame.width(),
                            height,
                        )
                        window.infoWidget.description.setText(Description.disabled())
                        window.infoWidget.widget.setGeometry(
                            0,
                            window.mainFrame.height() - height + 50,
                            window.mainFrame.width(),
                            height,
                        )
                    else:
                        window.infoWidget.description.setText(
                            Description.disabled(True)
                        )
                        window.infoWidget.widget.setGeometry(
                            0,
                            window.mainFrame.height() - height + 40,
                            window.mainFrame.width(),
                            height + 10,
                        )

                elif parameterType == Key.noSystemDropShadow:
                    window.infoWidget.description.setText(
                        Description.noSystemDropShadow()
                    )
                    window.infoWidget.widget.setGeometry(
                        0,
                        window.mainFrame.height() - height + 50,
                        window.mainFrame.width(),
                        height,
                    )

                elif parameterType == Key.enableImmersiveStyle:
                    window.infoWidget.description.setText(
                        Description.enableImmersiveStyle()
                    )
                    window.infoWidget.widget.setGeometry(
                        0,
                        window.mainFrame.height() - height + 50,
                        window.mainFrame.width(),
                        height,
                    )

                elif parameterType == Key.enableCustomRendering:
                    window.infoWidget.description.setText(
                        Description.enableCustomRendering()
                    )
                    window.infoWidget.widget.setGeometry(
                        0,
                        window.mainFrame.height() - height + 50,
                        window.mainFrame.width(),
                        height,
                    )

                elif parameterType == Key.enableFluentAnimation:
                    window.infoWidget.description.setText(
                        Description.enableFluentAnimation()
                    )
                    window.infoWidget.widget.setGeometry(
                        0,
                        window.mainFrame.height() - height + 50,
                        window.mainFrame.width(),
                        height,
                    )

                elif parameterType == Key.noModernAppBackgroundColor:
                    window.infoWidget.description.setText(
                        Description.noModernAppBackgroundColor()
                    )
                    window.infoWidget.widget.setGeometry(
                        0,
                        window.mainFrame.height() - height + 50,
                        window.mainFrame.width(),
                        height,
                    )

                elif parameterType == Key.colorTreatAsTransparent:
                    window.infoWidget.description.setText(
                        Description.colorTreatAsTransparent()
                    )
                    window.infoWidget.widget.setGeometry(
                        0,
                        window.mainFrame.height() - height + 50,
                        window.mainFrame.width(),
                        height,
                    )

                elif parameterType == Key.colorTreatAsTransparentThreshold:
                    window.infoWidget.description.setText(
                        Description.colorTreatAsTransparentThreshold()
                    )
                    window.infoWidget.widget.setGeometry(
                        0,
                        window.mainFrame.height() - height + 50,
                        window.mainFrame.width(),
                        height,
                    )

                elif parameterType == Key.fadeOutTime:
                    window.infoWidget.description.setText(Description.fadeOutTime())
                    window.infoWidget.widget.setGeometry(
                        0,
                        window.mainFrame.height() - height + 50,
                        window.mainFrame.width(),
                        height,
                    )

                elif parameterType == Key.fadeInTime:
                    window.infoWidget.description.setText(Description.fadeInTime())
                    window.infoWidget.widget.setGeometry(
                        0,
                        window.mainFrame.height() - height + 50,
                        window.mainFrame.width(),
                        height,
                    )

                elif parameterType == Key.popInTime:
                    window.infoWidget.description.setText(Description.popInTime())
                    window.infoWidget.widget.setGeometry(
                        0,
                        window.mainFrame.height() - height + 50,
                        window.mainFrame.width(),
                        height,
                    )

                elif parameterType == Key.startRatio:
                    window.infoWidget.description.setText(Description.startRatio())
                    window.infoWidget.widget.setGeometry(
                        0,
                        window.mainFrame.height() - height + 50,
                        window.mainFrame.width(),
                        height,
                    )

                elif parameterType == Key.enableImmediateInterupting:
                    window.infoWidget.description.setText(
                        Description.enableImmediateInterupting()
                    )
                    window.infoWidget.widget.setGeometry(
                        0,
                        window.mainFrame.height() - height + 50,
                        window.mainFrame.width(),
                        height,
                    )

                elif parameterType == Key.popInStyle:
                    window.infoWidget.description.setText(Description.popInStyle())
                    window.infoWidget.widget.setGeometry(
                        0,
                        window.mainFrame.height() - height + 50,
                        window.mainFrame.width(),
                        height,
                    )

                elif parameterType == Key.width:
                    isFocusing = window.menuTabWidget.currentIndex() == MenuTab.Focusing
                    window.infoWidget.widget.setGeometry(
                        0,
                        window.mainFrame.height() - height + 50,
                        window.mainFrame.width(),
                        height,
                    )
                    window.infoWidget.description.setText(Description.width(isFocusing))

                elif parameterType == Key.cornerRadius:
                    window.infoWidget.description.setText(Description.cornerRadius())
                    window.infoWidget.widget.setGeometry(
                        0,
                        window.mainFrame.height() - height + 50,
                        window.mainFrame.width(),
                        height,
                    )

                elif parameterType == Key.darkModeColor:
                    window.infoWidget.description.setText(Description.darkModeColor())
                    window.infoWidget.widget.setGeometry(
                        0,
                        window.mainFrame.height() - height + 50,
                        window.mainFrame.width(),
                        height,
                    )

                elif parameterType == Key.lightModeColor:
                    window.infoWidget.description.setText(Description.lightModeColor())
                    window.infoWidget.widget.setGeometry(
                        0,
                        window.mainFrame.height() - height + 50,
                        window.mainFrame.width(),
                        height,
                    )

                window.infoWidget.widget.show()
                window.mainFrame.setGraphicsEffect(QGraphicsBlurEffect())
                window.mainFrame.setDisabled(True)
                window.infoWidget.scrollArea.verticalScrollBar().setValue(0)

        def setMouseEvents(label: QLabel, parameterType: str, height: int):
            label.enterEvent = lambda event: labelEnterEvent(label)
            label.leaveEvent = lambda a0: labelLeaveEvent(label)
            label.mousePressEvent = lambda ev: labelMousePressEvent(
                ev,
                parameterType,
                height,
            )
            label.setCursor(Qt.CursorShape.PointingHandCursor)

        # Global
        setMouseEvents(window.lbl_effectType1, Key.effectType, 400)
        setMouseEvents(window.lbl_cornerType1, Key.cornerType, 250)
        setMouseEvents(window.lbl_enableDropShadow1, Key.enableDropShadow, 280)
        setMouseEvents(window.lbl_noBorderColor1, Key.noBorderColor, 220)
        setMouseEvents(window.lbl_enableMiniDump, Key.enableMiniDump, 180)
        setMouseEvents(
            window.lbl_enableThemeColorization1, Key.enableThemeColorization, 240
        )
        setMouseEvents(
            window.lbl_darkModeThemeColorizationType1,
            Key.darkModeThemeColorizationType,
            140,
        )
        setMouseEvents(
            window.lbl_lightModeThemeColorizationType1,
            Key.lightModeThemeColorizationType,
            140,
        )
        setMouseEvents(window.lbl_darkModeBorderColor1, Key.darkModeBorderColor, 140)
        setMouseEvents(window.lbl_lightModeBorderColor1, Key.lightModeBorderColor, 140)
        setMouseEvents(
            window.lbl_darkModeGradientColor1, Key.darkModeGradientColor, 140
        )
        setMouseEvents(
            window.lbl_lightModeGradientColor1, Key.lightModeGradientColor, 140
        )
        setMouseEvents(window.lbl_disabledEffect1, Key.disabled, 200)

        # DropDown-General
        setMouseEvents(window.lbl_effectType2, Key.effectType, 400)
        setMouseEvents(window.lbl_cornerType2, Key.cornerType, 270)
        setMouseEvents(window.lbl_enableDropShadow2, Key.enableDropShadow, 350)
        setMouseEvents(
            window.lbl_enableFluentAnimation1, Key.enableFluentAnimation, 170
        )
        setMouseEvents(window.lbl_noBorderColor2, Key.noBorderColor, 300)
        setMouseEvents(
            window.lbl_enableThemeColorization2, Key.enableThemeColorization, 330
        )
        setMouseEvents(window.lbl_darkModeBorderColor2, Key.darkModeBorderColor, 140)
        setMouseEvents(window.lbl_lightModeBorderColor2, Key.lightModeBorderColor, 140)
        setMouseEvents(
            window.lbl_darkModeGradientColor2, Key.darkModeGradientColor, 140
        )
        setMouseEvents(
            window.lbl_lightModeGradientColor2, Key.lightModeGradientColor, 140
        )
        setMouseEvents(window.lbl_disabledEffect2, Key.disabled, 250)

        # DropDown-Animation
        setMouseEvents(window.lbl_fadeOutTime1, Key.fadeOutTime, 150)
        setMouseEvents(window.lbl_fadeInTime1, Key.fadeInTime, 150)
        setMouseEvents(window.lbl_popInTime1, Key.popInTime, 150)
        setMouseEvents(window.lbl_popInStyle1, Key.popInStyle, 300)
        setMouseEvents(window.lbl_startRatio1, Key.startRatio, 200)
        setMouseEvents(
            window.lbl_enableImmediateInterupting1, Key.enableImmediateInterupting, 300
        )

        # Menu-General
        setMouseEvents(window.lbl_noSystemDropShadow, Key.noSystemDropShadow, 240)
        setMouseEvents(window.lbl_enableImmersiveStyle, Key.enableImmersiveStyle, 210)
        setMouseEvents(window.lbl_enableCustomRendering, Key.enableCustomRendering, 240)
        setMouseEvents(
            window.lbl_enableFluentAnimation2, Key.enableFluentAnimation, 170
        )
        setMouseEvents(
            window.lbl_enableCompatibiliyMode, Key.enableCompatibilityMode, 270
        )
        setMouseEvents(
            window.lbl_noModernAppBackgroundColor, Key.noModernAppBackgroundColor, 250
        )
        setMouseEvents(
            window.lbl_colorTreatAsTransparent, Key.colorTreatAsTransparent, 140
        )
        setMouseEvents(
            window.lbl_colorTreatAsTransparentThreshold,
            Key.colorTreatAsTransparentThreshold,
            150,
        )
        setMouseEvents(window.lbl_effectType3, Key.effectType, 400)
        setMouseEvents(window.lbl_cornerType3, Key.cornerType, 280)
        setMouseEvents(window.lbl_enableDropShadow3, Key.enableDropShadow, 350)
        setMouseEvents(window.lbl_noBorderColor3, Key.noBorderColor, 300)
        setMouseEvents(
            window.lbl_enableThemeColorization3_1, Key.enableThemeColorization, 330
        )
        setMouseEvents(
            window.lbl_darkModeThemeColorizationType2,
            Key.darkModeThemeColorizationType,
            140,
        )
        setMouseEvents(
            window.lbl_lightModeThemeColorizationType2,
            Key.lightModeThemeColorizationType,
            140,
        )
        setMouseEvents(window.lbl_darkModeBorderColor3, Key.darkModeBorderColor, 140)
        setMouseEvents(window.lbl_lightModeBorderColor3, Key.lightModeBorderColor, 140)
        setMouseEvents(
            window.lbl_darkModeGradientColor3, Key.darkModeGradientColor, 140
        )
        setMouseEvents(
            window.lbl_lightModeGradientColor3, Key.lightModeGradientColor, 140
        )
        setMouseEvents(window.lbl_disabledEffect3_1, Key.disabled, 240)

        # Menu-Animation
        setMouseEvents(window.lbl_fadeOutTime2, Key.fadeOutTime, 150)
        setMouseEvents(window.lbl_fadeInTime2, Key.fadeInTime, 150)
        setMouseEvents(window.lbl_popInTime2, Key.popInTime, 150)
        setMouseEvents(window.lbl_popInStyle2, Key.popInStyle, 300)
        setMouseEvents(window.lbl_startRatio2, Key.startRatio, 200)
        setMouseEvents(
            window.lbl_enableImmediateInterupting2, Key.enableImmediateInterupting, 300
        )

        # Menu-Hot
        setMouseEvents(window.lbl_darkModeColor1_1, Key.darkModeColor, 180)
        setMouseEvents(window.lbl_lightModeColor1_1, Key.lightModeColor, 180)
        setMouseEvents(window.lbl_disabledEffect3_2, Key.disabled, 240)
        setMouseEvents(window.lbl_cornerRadius1_1, Key.cornerRadius, 140)
        setMouseEvents(
            window.lbl_enableThemeColorization3_2, Key.enableThemeColorization, 320
        )

        # Menu-DisabledHot
        setMouseEvents(window.lbl_darkModeColor1_2, Key.darkModeColor, 180)
        setMouseEvents(window.lbl_lightModeColor1_2, Key.lightModeColor, 180)
        setMouseEvents(window.lbl_disabledEffect3_3, Key.disabled, 240)
        setMouseEvents(window.lbl_cornerRadius1_2, Key.cornerRadius, 140)
        setMouseEvents(
            window.lbl_enableThemeColorization3_3, Key.enableThemeColorization, 320
        )

        # Menu-Focusing
        setMouseEvents(window.lbl_width1_1, Key.width, 240)
        setMouseEvents(window.lbl_darkModeColor1_3, Key.darkModeColor, 180)
        setMouseEvents(window.lbl_lightModeColor1_3, Key.lightModeColor, 180)
        setMouseEvents(window.lbl_disabledEffect3_4, Key.disabled, 240)
        setMouseEvents(window.lbl_cornerRadius1_3, Key.cornerRadius, 140)
        setMouseEvents(
            window.lbl_enableThemeColorization3_4, Key.enableThemeColorization, 320
        )

        # Menu-Separator
        setMouseEvents(window.lbl_width1_2, Key.width, 240)
        setMouseEvents(window.lbl_darkModeColor1_4, Key.darkModeColor, 180)
        setMouseEvents(window.lbl_lightModeColor1_4, Key.lightModeColor, 180)
        setMouseEvents(window.lbl_disabledEffect3_5, Key.disabled, 240)
        setMouseEvents(window.lbl_cornerRadius1_4, Key.cornerRadius, 140)
        setMouseEvents(
            window.lbl_enableThemeColorization3_5, Key.enableThemeColorization, 320
        )

        # Tooltip
        setMouseEvents(window.lbl_effectType4, Key.effectType, 400)
        setMouseEvents(window.lbl_cornerType4, Key.cornerType, 270)
        setMouseEvents(window.lbl_enableDropShadow4, Key.enableDropShadow, 340)
        setMouseEvents(window.lbl_noBorderColor4, Key.noBorderColor, 300)
        setMouseEvents(window.lbl_textColor, Key.textColor, 100)
        setMouseEvents(window.lbl_borderColor, Key.borderColor, 120)
        setMouseEvents(window.lbl_gradientColor, Key.gradientColor, 120)
        setMouseEvents(window.lbl_marginsType, Key.marginsType, 180)
        setMouseEvents(window.lbl_margin, Key.margin, 100)
        setMouseEvents(
            window.lbl_enableThemeColorization4, Key.enableThemeColorization, 320
        )
        setMouseEvents(window.lbl_disabledEffect4, Key.disabled, 240)

    @staticmethod
    def connectSettings(window: Main):
        """
        Method to connect various Buttons in Settings

        Args:
            window (Main): Main window which has all the widgets
        """
        _translate = translationVar.translateFrom

        def run():
            if not AppSettings.isValidTFPath():
                window.toolBox.setCurrentIndex(0)
                window.location_error_text.setText(
                    _translate(TranslationKey.Settings.locationError)
                )
                return

            path: str = rf'start Rundll32 "{AppSettings.path}\TFMain64.dll",Main /start'
            os.system(path)

        def stop():
            if not AppSettings.isValidTFPath():
                window.toolBox.setCurrentIndex(0)
                window.location_error_text.setText(
                    _translate(TranslationKey.Settings.locationError)
                )
                return

            path: str = rf'start Rundll32 "{AppSettings.path}\TFMain64.dll",Main /stop'
            os.system(path)

        def install():
            if not AppSettings.isValidTFPath():
                window.toolBox.setCurrentIndex(0)
                window.location_error_text.setText(
                    _translate(TranslationKey.Settings.locationError)
                )
                return

            path: str = (
                rf'/c start Rundll32 "{AppSettings.path}\TFMain64.dll",Main /install'
            )
            windll.shell32.ShellExecuteW(
                None,
                "runas",
                "cmd.exe",
                path,
                None,
                1,
            )

        def uninstall():
            if not AppSettings.isValidTFPath():
                window.toolBox.setCurrentIndex(0)
                window.location_error_text.setText(
                    _translate(TranslationKey.Settings.locationError)
                )
                return

            path: str = (
                rf'/c start Rundll32 "{AppSettings.path}\TFMain64.dll",Main /uninstall'
            )
            windll.shell32.ShellExecuteW(
                None,
                "runas",
                "cmd.exe",
                path,
                None,
                1,
            )

        def downloadAndInstall():
            url = "https://github.com/ALTaleX531/TranslucentFlyouts/releases/latest/download/TranslucentFlyouts.Win32.V3.x64.rar"
            wget.download(url)
            os.system(
                r".\\Assets\\unrar.exe -idp -y e .\\TranslucentFlyouts.Win32.V3.x64.rar .\\TranslucentFlyouts\\"
            )
            os.remove(".\\TranslucentFlyouts.Win32.V3.x64.rar")
            path = os.path.abspath(".\\TranslucentFlyouts")
            window.locationLineEdit.setText(path)
            window.saveButton.click()
            window.installButton.click()
            window.toolBox.setCurrentIndex(0)

        def chooseFolder():
            dialog = QFileDialog()
            dialog.setOptions(QFileDialog.Option.ShowDirsOnly)
            dialog.setOptions(QFileDialog.Option.ReadOnly)
            dialog.setOptions(QFileDialog.Option.DontUseNativeDialog)
            dialog.setAcceptMode(QFileDialog.AcceptMode.AcceptSave)
            directory = dialog.getExistingDirectory(
                caption="Choose Installation Folder"
            )
            if directory:
                window.locationLineEdit.setText(directory)

        def saveGeneral():
            # Language
            languageIndex = window.languageList.currentIndex().row()
            if languageIndex < 0:
                languageIndex = AppSettings.language
            language = Translate.findLanguageFromInt(languageIndex)
            Translate.translate(window, language)
            AppSettings.language = languageIndex

            # Path
            path = window.locationLineEdit.text()
            if path in ["", None] or not os.path.isfile(
                r"{}/{}".format(path, "TFMain64.dll")
            ):
                AppSettings.path = ""
                window.locationLineEdit.setText(AppSettings.path)
                window.location_error_text.setText(
                    _translate(TranslationKey.Settings.locationError)
                )
            else:
                AppSettings.path = path
                window.location_error_text.setText("")

            AppSettings.updateDict()
            AppSettings.updateJSON()

        def saveAppearance():
            backgroundColor: str = window.backgroundColor.text()
            secondaryBackgroundColor: str = window.secondaryBackgroundColor.text()
            labelColor: str = window.labelColor.text()
            textColor: str = window.textColor.text()
            iconType: int = window.iconColorMode.currentIndex()

            if not all(
                (backgroundColor, secondaryBackgroundColor, labelColor, textColor)
            ):
                return

            backgroundColor = "#" + backgroundColor[2:]
            secondaryBackgroundColor = "#" + secondaryBackgroundColor[2:]
            labelColor = "#" + labelColor[2:]
            textColor = "#" + textColor[2:]
            AppSettings.iconType = iconType

            Connectors.connectStyleSheets(
                window=window,
                backgroundColor=backgroundColor,
                secondaryBackgroundColor=secondaryBackgroundColor,
                labelColor=labelColor,
                textColor=textColor,
            )
            Connectors.setIcons(window, iconType)
            AppSettings.updateDict()
            AppSettings.updateJSON()

        window.chooseButton.clicked.connect(chooseFolder)
        window.downloadButton.clicked.connect(downloadAndInstall)
        window.runButton.clicked.connect(run)
        window.stopButton.clicked.connect(stop)
        window.installButton.clicked.connect(install)
        window.uninstallButton.clicked.connect(uninstall)
        window.saveButton.clicked.connect(saveGeneral)
        window.saveButton_2.clicked.connect(saveAppearance)
        window.preset.addItems(ColorPresets.getPresets())
        window.preset.currentIndexChanged.connect(
            lambda: ColorPresets.presetChanged(window)
        )

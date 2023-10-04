# Library Imports
from __future__ import annotations
from typing import TYPE_CHECKING, Callable
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QPushButton, QLineEdit, QComboBox, QSpinBox, QLabel, QGraphicsBlurEffect
from PyQt6.QtGui import QIcon, QMouseEvent


# Relative Imports
from Widgets.color_picker import ColorPicker
from Data.defaults import Defaults, Key
from Data.stylesheet import StyleSheet
from Data.paths import Path
from Data.user import ClassVar
from Data.descriptions import Description
from Data.enums import MainTab, MenuTab, InfoWidgetHeight
from save_settings import SaveSettings

if TYPE_CHECKING:
    from main import Main


class Connectors:
    @staticmethod
    def connectStyleSheets(
        window: Main,
        backgroundColor: str = "#202020",
        secondaryBackgroundColor: str = "#313131",
        labelColor: str = "white",
        textColor: str = "#7A7A7A",
    ):
        """
        Method to:
        - Add Styling apply styling to the UI elements
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

        # Apply Button
        window.applyButton1.setStyleSheet(
            StyleSheet.applyButton(
                secondaryBackgroundColor=secondaryBackgroundColor,
                labelColor=labelColor,
                textColor=textColor,
            )
        )
        window.applyButton2.setStyleSheet(
            StyleSheet.applyButton(
                secondaryBackgroundColor=secondaryBackgroundColor,
                labelColor=labelColor,
                textColor=textColor,
            )
        )
        window.applyButton3_1.setStyleSheet(
            StyleSheet.applyButton(
                secondaryBackgroundColor=secondaryBackgroundColor,
                labelColor=labelColor,
                textColor=textColor,
            )
        )
        window.applyButton3_2.setStyleSheet(
            StyleSheet.applyButton(
                secondaryBackgroundColor=secondaryBackgroundColor,
                labelColor=labelColor,
                textColor=textColor,
            )
        )
        window.applyButton3_3.setStyleSheet(
            StyleSheet.applyButton(
                secondaryBackgroundColor=secondaryBackgroundColor,
                labelColor=labelColor,
                textColor=textColor,
            )
        )
        window.applyButton3_4.setStyleSheet(
            StyleSheet.applyButton(
                secondaryBackgroundColor=secondaryBackgroundColor,
                labelColor=labelColor,
                textColor=textColor,
            )
        )
        window.applyButton3_5.setStyleSheet(
            StyleSheet.applyButton(
                secondaryBackgroundColor=secondaryBackgroundColor,
                labelColor=labelColor,
                textColor=textColor,
            )
        )
        window.applyButton3_6.setStyleSheet(
            StyleSheet.applyButton(
                secondaryBackgroundColor=secondaryBackgroundColor,
                labelColor=labelColor,
                textColor=textColor,
            )
        )
        window.applyButton4.setStyleSheet(
            StyleSheet.applyButton(
                secondaryBackgroundColor=secondaryBackgroundColor,
                labelColor=labelColor,
                textColor=textColor,
            )
        )
        window.appliedWidget.widget.setStyleSheet(StyleSheet.appliedWidget())

    @staticmethod
    def connectApplyButtons(window: Main) -> None:
        """
        Method to:
        - Connect Apply Button to its respective functions
        """
        window.applyButton1.clicked.connect(lambda a: SaveSettings.Global.save(window))
        window.applyButton1.clicked.connect(lambda a: window.appliedWidget.start())
        window.applyButton2.clicked.connect(lambda a: SaveSettings.DropDown.save(window))
        window.applyButton2.clicked.connect(lambda a: window.appliedWidget.start())
        window.applyButton3_1.clicked.connect(lambda a: SaveSettings.Menu.save(window))
        window.applyButton3_1.clicked.connect(lambda a: window.appliedWidget.start())
        window.applyButton3_2.clicked.connect(lambda a: SaveSettings.Menu.Animation.save(window))
        window.applyButton3_2.clicked.connect(lambda a: window.appliedWidget.start())
        window.applyButton3_3.clicked.connect(lambda a: SaveSettings.Menu.Hot.save(window))
        window.applyButton3_3.clicked.connect(lambda a: window.appliedWidget.start())
        window.applyButton3_4.clicked.connect(lambda a: SaveSettings.Menu.DisabledHot.save(window))
        window.applyButton3_4.clicked.connect(lambda a: window.appliedWidget.start())
        window.applyButton3_5.clicked.connect(lambda a: SaveSettings.Menu.Focusing.save(window))
        window.applyButton3_5.clicked.connect(lambda a: window.appliedWidget.start())
        window.applyButton3_6.clicked.connect(lambda a: SaveSettings.Menu.Separator.save(window))
        window.applyButton3_6.clicked.connect(lambda a: window.appliedWidget.start())
        window.applyButton4.clicked.connect(lambda a: SaveSettings.Tooltip.save(window))
        window.applyButton4.clicked.connect(lambda a: window.appliedWidget.start())

    @staticmethod
    def connectResetButtons(window: Main) -> None:
        """
        Connect Reset Buttons to their respective methods:
        - Left Click to reset to default
        - Right Click to reset to last saved value
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
                """
                exec(f"val={valueVarAsString}")
                return locals()["val"]

            resetButton.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)

            if isinstance(valueWidget, QLineEdit):
                if colorPickerButton and type(defaultValue) == str:
                    resetButton.clicked.connect(lambda a: valueWidget.setText(defaultValue))
                    resetButton.clicked.connect(lambda a: colorPickerButton.setStyleSheet(StyleSheet.buttoResetStyleSheet()))
                    resetButton.clicked.connect(lambda a: colorPickerButton.setIcon(QIcon(Path.IconPaths.ColorPicker)))

                    resetButton.customContextMenuRequested.connect(lambda a: valueWidget.setText(getSavedValue(savedValueName)))
                    resetButton.customContextMenuRequested.connect(
                        lambda a: colorPickerButton.setStyleSheet(StyleSheet.buttoResetStyleSheet())
                        if (getSavedValue(savedValueName) == "")
                        else ColorPicker.changeButtonColor(getSavedValue(savedValueName), colorPickerButton)
                    )
                    resetButton.customContextMenuRequested.connect(
                        lambda a: colorPickerButton.setIcon(QIcon(Path.IconPaths.ColorPicker) if (getSavedValue(savedValueName) == "") else QIcon(""))
                    )
            elif isinstance(valueWidget, QComboBox):
                if type(defaultValue) == int:
                    resetButton.clicked.connect(lambda a: valueWidget.setCurrentIndex(defaultValue))
                    resetButton.customContextMenuRequested.connect(lambda a: valueWidget.setCurrentIndex(getSavedValue(savedValueName)))
            elif isinstance(valueWidget, QSpinBox):
                if type(defaultValue) == int:
                    resetButton.clicked.connect(lambda a: valueWidget.setValue(defaultValue))
                    resetButton.customContextMenuRequested.connect(lambda a: valueWidget.setValue(getSavedValue(savedValueName)))

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
            savedValueName=ClassVar.joinVars(ClassVar._global, ClassVar.enableDropShadow),
            colorPickerButton=None,
        )
        configureResetButton(
            resetButton=window.reset_theme_colorization1,
            valueWidget=window.enableThemeColorization1,
            defaultValue=Defaults.Global.enableThemeColorization,
            savedValueName=ClassVar.joinVars(ClassVar._global, ClassVar.enableThemeColorization),
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
            savedValueName=ClassVar.joinVars(ClassVar._global, ClassVar.darkModeBorderColor),
            colorPickerButton=window.dark_mode_border_color_picker1,
        )
        configureResetButton(
            resetButton=window.reset_light_mode_border_color1,
            valueWidget=window.lightModeBorderColor1,
            defaultValue=Defaults.Global.lightModeBorderColor,
            savedValueName=ClassVar.joinVars(ClassVar._global, ClassVar.lightModeBorderColor),
            colorPickerButton=window.light_mode_border_color_picker1,
        )
        configureResetButton(
            resetButton=window.reset_dark_mode_gradient_color1,
            valueWidget=window.darkModeGradientColor1,
            defaultValue=Defaults.Global.darkModeGradientColor,
            savedValueName=ClassVar.joinVars(ClassVar._global, ClassVar.darkModeGradientColor),
            colorPickerButton=window.dark_mode_gradient_color_picker1,
        )
        configureResetButton(
            resetButton=window.reset_light_mode_gradient_color1,
            valueWidget=window.lightModeGradientColor1,
            defaultValue=Defaults.Global.lightModeGradientColor,
            savedValueName=ClassVar.joinVars(ClassVar._global, ClassVar.lightModeGradientColor),
            colorPickerButton=window.light_mode_gradient_color_picker1,
        )
        configureResetButton(
            resetButton=window.reset_disabled1,
            valueWidget=window.disabledEffect1,
            defaultValue=Defaults.Global.disabled,
            savedValueName=ClassVar.joinVars(ClassVar._global, ClassVar.disabled),
            colorPickerButton=None,
        )

        # DropDown
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
            savedValueName=ClassVar.joinVars(ClassVar.dropdown, ClassVar.enableDropShadow),
            colorPickerButton=None,
        )
        configureResetButton(
            resetButton=window.reset_theme_colorization2,
            valueWidget=window.enableThemeColorization2,
            defaultValue=Defaults.DropDown.enableThemeColorization,
            savedValueName=ClassVar.joinVars(ClassVar.dropdown, ClassVar.enableThemeColorization),
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
            savedValueName=ClassVar.joinVars(ClassVar.dropdown, ClassVar.darkModeBorderColor),
            colorPickerButton=window.dark_mode_border_color_picker2,
        )
        configureResetButton(
            resetButton=window.reset_light_mode_border_color2,
            valueWidget=window.lightModeBorderColor2,
            defaultValue=Defaults.DropDown.lightModeBorderColor,
            savedValueName=ClassVar.joinVars(ClassVar.dropdown, ClassVar.lightModeBorderColor),
            colorPickerButton=window.light_mode_border_color_picker2,
        )
        configureResetButton(
            resetButton=window.reset_dark_mode_gradient_color2,
            valueWidget=window.darkModeGradientColor2,
            defaultValue=Defaults.DropDown.darkModeGradientColor,
            savedValueName=ClassVar.joinVars(ClassVar.dropdown, ClassVar.darkModeGradientColor),
            colorPickerButton=window.dark_mode_gradient_color_picker2,
        )
        configureResetButton(
            resetButton=window.reset_light_mode_gradient_color2,
            valueWidget=window.lightModeGradientColor2,
            defaultValue=Defaults.DropDown.lightModeGradientColor,
            savedValueName=ClassVar.joinVars(ClassVar.dropdown, ClassVar.lightModeGradientColor),
            colorPickerButton=window.light_mode_gradient_color_picker2,
        )
        configureResetButton(
            resetButton=window.reset_disabled2,
            valueWidget=window.disabledEffect2,
            defaultValue=Defaults.DropDown.disabled,
            savedValueName=ClassVar.joinVars(ClassVar.dropdown, ClassVar.disabled),
            colorPickerButton=None,
        )

        # Menu-General
        configureResetButton(
            resetButton=window.reset_system_drop_shadow,
            valueWidget=window.noSystemDropShadow,
            defaultValue=Defaults.Menu.noSystemDropShadow,
            savedValueName=ClassVar.joinVars(ClassVar.menu, ClassVar.noSystemDropShadow),
            colorPickerButton=None,
        )
        configureResetButton(
            resetButton=window.reset_immersive_style,
            valueWidget=window.enableImmersiveStyle,
            defaultValue=Defaults.Menu.enableImmersiveStyle,
            savedValueName=ClassVar.joinVars(ClassVar.menu, ClassVar.enableImmersiveStyle),
            colorPickerButton=None,
        )
        configureResetButton(
            resetButton=window.reset_custom_rendering,
            valueWidget=window.enableCustomRendering,
            defaultValue=Defaults.Menu.enableCustomRendering,
            savedValueName=ClassVar.joinVars(ClassVar.menu, ClassVar.enableCustomRendering),
            colorPickerButton=None,
        )
        configureResetButton(
            resetButton=window.reset_fluent_animation,
            valueWidget=window.enableFluentAnimation,
            defaultValue=Defaults.Menu.enableFluentAnimation,
            savedValueName=ClassVar.joinVars(ClassVar.menu, ClassVar.enableFluentAnimation),
            colorPickerButton=None,
        )
        configureResetButton(
            resetButton=window.reset_modern_app_background_color,
            valueWidget=window.noModernAppBackgroundColor,
            defaultValue=Defaults.Menu.noModernAppBackgroundColor,
            savedValueName=ClassVar.joinVars(ClassVar.menu, ClassVar.noModernAppBackgroundColor),
            colorPickerButton=None,
        )
        configureResetButton(
            resetButton=window.reset_color_treat_as_transparent,
            valueWidget=window.colorTreatAsTransparent,
            defaultValue=Defaults.Menu.colorTreatAsTransparent,
            savedValueName=ClassVar.joinVars(ClassVar.menu, ClassVar.colorTreatAsTransparent),
            colorPickerButton=window.color_treat_as_transparent_color_picker,
        )
        configureResetButton(
            resetButton=window.reset_color_treat_as_transparent_threshold,
            valueWidget=window.colorTreatAsTransparentThreshold,
            defaultValue=Defaults.Menu.colorTreatAsTransparentThreshold,
            savedValueName=ClassVar.joinVars(ClassVar.menu, ClassVar.colorTreatAsTransparentThreshold),
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
            resetButton=window.reset_theme_colorization3_1,
            valueWidget=window.enableThemeColorization3_1,
            defaultValue=Defaults.Menu.enableThemeColorization,
            savedValueName=ClassVar.joinVars(ClassVar.menu, ClassVar.enableThemeColorization),
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
            savedValueName=ClassVar.joinVars(ClassVar.menu, ClassVar.darkModeBorderColor),
            colorPickerButton=window.dark_mode_border_color_picker3,
        )

        configureResetButton(
            resetButton=window.reset_light_mode_border_color3,
            valueWidget=window.lightModeBorderColor3,
            defaultValue=Defaults.Menu.lightModeBorderColor,
            savedValueName=ClassVar.joinVars(ClassVar.menu, ClassVar.lightModeBorderColor),
            colorPickerButton=window.light_mode_border_color_picker3,
        )
        configureResetButton(
            resetButton=window.reset_dark_mode_gradient_color3,
            valueWidget=window.darkModeGradientColor3,
            defaultValue=Defaults.Menu.darkModeGradientColor,
            savedValueName=ClassVar.joinVars(ClassVar.menu, ClassVar.darkModeGradientColor),
            colorPickerButton=window.dark_mode_gradient_color_picker3,
        )
        configureResetButton(
            resetButton=window.reset_light_mode_gradient_color3,
            valueWidget=window.lightModeGradientColor3,
            defaultValue=Defaults.Menu.lightModeGradientColor,
            savedValueName=ClassVar.joinVars(ClassVar.menu, ClassVar.lightModeGradientColor),
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
            resetButton=window.reset_fade_out_time,
            valueWidget=window.fadeOutTime,
            defaultValue=Defaults.Menu.Animation.fadeOutTime,
            savedValueName=ClassVar.joinVars(ClassVar.menu, ClassVar.animation, ClassVar.fadeOutTime),
            colorPickerButton=None,
        )
        configureResetButton(
            resetButton=window.reset_pop_in_time,
            valueWidget=window.popInTime,
            defaultValue=Defaults.Menu.Animation.popInTime,
            savedValueName=ClassVar.joinVars(ClassVar.menu, ClassVar.animation, ClassVar.popInTime),
            colorPickerButton=None,
        )
        configureResetButton(
            resetButton=window.reset_fade_in_time,
            valueWidget=window.fadeInTime,
            defaultValue=Defaults.Menu.Animation.fadeInTime,
            savedValueName=ClassVar.joinVars(ClassVar.menu, ClassVar.animation, ClassVar.fadeInTime),
            colorPickerButton=None,
        )
        configureResetButton(
            resetButton=window.reset_pop_in_style,
            valueWidget=window.popInStyle,
            defaultValue=Defaults.Menu.Animation.popInStyle,
            savedValueName=ClassVar.joinVars(ClassVar.menu, ClassVar.animation, ClassVar.popInStyle),
            colorPickerButton=None,
        )
        configureResetButton(
            resetButton=window.reset_start_ratio,
            valueWidget=window.startRatio,
            defaultValue=Defaults.Menu.Animation.startRatio,
            savedValueName=ClassVar.joinVars(ClassVar.menu, ClassVar.animation, ClassVar.startRatio),
            colorPickerButton=None,
        )
        configureResetButton(
            resetButton=window.reset_immediate_interupting,
            valueWidget=window.enableImmediateInterupting,
            defaultValue=Defaults.Menu.Animation.enableImmediateInterupting,
            savedValueName=ClassVar.joinVars(ClassVar.menu, ClassVar.animation, ClassVar.enableImmediateInterupting),
            colorPickerButton=None,
        )
        # Menu-Hot
        configureResetButton(
            resetButton=window.reset_dark_mode_color1_1,
            valueWidget=window.darkModeColor1_1,
            defaultValue=Defaults.Menu.Hot.darkModeColor,
            savedValueName=ClassVar.joinVars(ClassVar.menu, ClassVar.hot, ClassVar.darkModeColor),
            colorPickerButton=window.dark_mode_color_picker1_1,
        )
        configureResetButton(
            resetButton=window.reset_light_mode_color1_1,
            valueWidget=window.lightModeColor1_1,
            defaultValue=Defaults.Menu.Hot.lightModeColor,
            savedValueName=ClassVar.joinVars(ClassVar.menu, ClassVar.hot, ClassVar.lightModeColor),
            colorPickerButton=window.light_mode_color_picker1_1,
        )
        configureResetButton(
            resetButton=window.reset_disabled3_2,
            valueWidget=window.disabledEffect3_2,
            defaultValue=Defaults.Menu.Hot.disabled,
            savedValueName=ClassVar.joinVars(ClassVar.menu, ClassVar.hot, ClassVar.disabled),
            colorPickerButton=None,
        )
        configureResetButton(
            resetButton=window.reset_corner_radius1_1,
            valueWidget=window.cornerRadius1_1,
            defaultValue=Defaults.Menu.Hot.cornerRadius,
            savedValueName=ClassVar.joinVars(ClassVar.menu, ClassVar.hot, ClassVar.cornerRadius),
            colorPickerButton=None,
        )
        configureResetButton(
            resetButton=window.reset_theme_colorization3_2,
            valueWidget=window.enableThemeColorization3_2,
            defaultValue=Defaults.Menu.Hot.enableThemeColorization,
            savedValueName=ClassVar.joinVars(ClassVar.menu, ClassVar.hot, ClassVar.enableThemeColorization),
            colorPickerButton=None,
        )
        # Menu-Disabled Hot
        configureResetButton(
            resetButton=window.reset_dark_mode_color1_2,
            valueWidget=window.darkModeColor1_2,
            defaultValue=Defaults.Menu.DisabledHot.darkModeColor,
            savedValueName=ClassVar.joinVars(ClassVar.menu, ClassVar.disabledHot, ClassVar.darkModeColor),
            colorPickerButton=window.dark_mode_color_picker1_2,
        )
        configureResetButton(
            resetButton=window.reset_light_mode_color1_2,
            valueWidget=window.lightModeColor1_2,
            defaultValue=Defaults.Menu.DisabledHot.lightModeColor,
            savedValueName=ClassVar.joinVars(ClassVar.menu, ClassVar.disabledHot, ClassVar.lightModeColor),
            colorPickerButton=window.light_mode_color_picker1_2,
        )
        configureResetButton(
            resetButton=window.reset_disabled3_3,
            valueWidget=window.disabledEffect3_3,
            defaultValue=Defaults.Menu.DisabledHot.disabled,
            savedValueName=ClassVar.joinVars(ClassVar.menu, ClassVar.disabledHot, ClassVar.disabled),
            colorPickerButton=None,
        )
        configureResetButton(
            resetButton=window.reset_corner_radius1_2,
            valueWidget=window.cornerRadius1_2,
            defaultValue=Defaults.Menu.DisabledHot.cornerRadius,
            savedValueName=ClassVar.joinVars(ClassVar.menu, ClassVar.disabledHot, ClassVar.cornerRadius),
            colorPickerButton=None,
        )
        configureResetButton(
            resetButton=window.reset_theme_colorization3_3,
            valueWidget=window.enableThemeColorization3_3,
            defaultValue=Defaults.Menu.Hot.enableThemeColorization,
            savedValueName=ClassVar.joinVars(ClassVar.menu, ClassVar.disabledHot, ClassVar.enableThemeColorization),
            colorPickerButton=None,
        )

        # Menu-Focusing
        configureResetButton(
            resetButton=window.reset_width1_1,
            valueWidget=window.width1_1,
            defaultValue=Defaults.Menu.Focusing.width,
            savedValueName=ClassVar.joinVars(ClassVar.menu, ClassVar.focusing, ClassVar.width),
            colorPickerButton=None,
        )
        configureResetButton(
            resetButton=window.reset_dark_mode_color1_3,
            valueWidget=window.darkModeColor1_3,
            defaultValue=Defaults.Menu.Focusing.darkModeColor,
            savedValueName=ClassVar.joinVars(ClassVar.menu, ClassVar.focusing, ClassVar.darkModeColor),
            colorPickerButton=window.dark_mode_color_picker1_3,
        )
        configureResetButton(
            resetButton=window.reset_light_mode_color1_3,
            valueWidget=window.lightModeColor1_3,
            defaultValue=Defaults.Menu.Focusing.lightModeColor,
            savedValueName=ClassVar.joinVars(ClassVar.menu, ClassVar.focusing, ClassVar.lightModeColor),
            colorPickerButton=window.light_mode_color_picker1_3,
        )
        configureResetButton(
            resetButton=window.reset_disabled3_4,
            valueWidget=window.disabledEffect3_4,
            defaultValue=Defaults.Menu.Focusing.disabled,
            savedValueName=ClassVar.joinVars(ClassVar.menu, ClassVar.focusing, ClassVar.disabled),
            colorPickerButton=None,
        )
        configureResetButton(
            resetButton=window.reset_corner_radius1_3,
            valueWidget=window.cornerRadius1_3,
            defaultValue=Defaults.Menu.Focusing.cornerRadius,
            savedValueName=ClassVar.joinVars(ClassVar.menu, ClassVar.focusing, ClassVar.cornerRadius),
            colorPickerButton=None,
        )
        configureResetButton(
            resetButton=window.reset_theme_colorization3_4,
            valueWidget=window.enableThemeColorization3_4,
            defaultValue=Defaults.Menu.Focusing.enableThemeColorization,
            savedValueName=ClassVar.joinVars(ClassVar.menu, ClassVar.focusing, ClassVar.enableThemeColorization),
            colorPickerButton=None,
        )

        # Menu-Separator
        configureResetButton(
            resetButton=window.reset_width1_2,
            valueWidget=window.width1_2,
            defaultValue=Defaults.Menu.Separator.width,
            savedValueName=ClassVar.joinVars(ClassVar.menu, ClassVar.separator, ClassVar.width),
            colorPickerButton=None,
        )
        configureResetButton(
            resetButton=window.reset_dark_mode_color1_4,
            valueWidget=window.darkModeColor1_4,
            defaultValue=Defaults.Menu.Separator.darkModeColor,
            savedValueName=ClassVar.joinVars(ClassVar.menu, ClassVar.separator, ClassVar.darkModeColor),
            colorPickerButton=window.dark_mode_color_picker1_4,
        )
        configureResetButton(
            resetButton=window.reset_light_mode_color1_4,
            valueWidget=window.lightModeColor1_4,
            defaultValue=Defaults.Menu.Separator.lightModeColor,
            savedValueName=ClassVar.joinVars(ClassVar.menu, ClassVar.separator, ClassVar.lightModeColor),
            colorPickerButton=window.light_mode_color_picker1_4,
        )
        configureResetButton(
            resetButton=window.reset_disabled3_5,
            valueWidget=window.disabledEffect3_5,
            defaultValue=Defaults.Menu.Separator.disabled,
            savedValueName=ClassVar.joinVars(ClassVar.menu, ClassVar.separator, ClassVar.disabled),
            colorPickerButton=None,
        )
        configureResetButton(
            resetButton=window.reset_corner_radius1_4,
            valueWidget=window.cornerRadius1_4,
            defaultValue=Defaults.Menu.Separator.cornerRadius,
            savedValueName=ClassVar.joinVars(ClassVar.menu, ClassVar.separator, ClassVar.cornerRadius),
            colorPickerButton=None,
        )
        configureResetButton(
            resetButton=window.reset_theme_colorization3_5,
            valueWidget=window.enableThemeColorization3_5,
            defaultValue=Defaults.Menu.Separator.enableThemeColorization,
            savedValueName=ClassVar.joinVars(ClassVar.menu, ClassVar.separator, ClassVar.enableThemeColorization),
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
            savedValueName=ClassVar.joinVars(ClassVar.tooltip, ClassVar.enableDropShadow),
            colorPickerButton=None,
        )
        configureResetButton(
            resetButton=window.reset_theme_colorization4,
            valueWidget=window.enableThemeColorization4,
            defaultValue=Defaults.Tooltip.enableThemeColorization,
            savedValueName=ClassVar.joinVars(ClassVar.tooltip, ClassVar.enableThemeColorization),
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
            resetButton=window.reset_dark_mode_border_color4,
            valueWidget=window.darkModeBorderColor4,
            defaultValue=Defaults.Tooltip.darkModeBorderColor,
            savedValueName=ClassVar.joinVars(ClassVar.tooltip, ClassVar.darkModeBorderColor),
            colorPickerButton=window.dark_mode_border_color_picker4,
        )
        configureResetButton(
            resetButton=window.reset_light_mode_border_color4,
            valueWidget=window.lightModeBorderColor4,
            defaultValue=Defaults.Tooltip.lightModeBorderColor,
            savedValueName=ClassVar.joinVars(ClassVar.tooltip, ClassVar.lightModeBorderColor),
            colorPickerButton=window.light_mode_border_color_picker4,
        )
        configureResetButton(
            resetButton=window.reset_dark_mode_gradient_color4,
            valueWidget=window.darkModeGradientColor4,
            defaultValue=Defaults.Tooltip.darkModeGradientColor,
            savedValueName=ClassVar.joinVars(ClassVar.tooltip, ClassVar.darkModeGradientColor),
            colorPickerButton=window.dark_mode_gradient_color_picker4,
        )
        configureResetButton(
            resetButton=window.reset_light_mode_gradient_color4,
            valueWidget=window.lightModeGradientColor4,
            defaultValue=Defaults.Tooltip.lightModeGradientColor,
            savedValueName=ClassVar.joinVars(ClassVar.tooltip, ClassVar.lightModeGradientColor),
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
    def connectColorPickers(window: Main) -> None:
        """
        Connect Color Picker Buttons to:
        - Color Picker Dialog
        Connect Color Picker Dialog to:
        - Color Output lineEdit
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

    @staticmethod
    def connectMouseEvent(window: Main, _translate: Callable[[str], str]) -> None:
        """
        Method to handle mouse hover and clicks on parameters
        - Handles mouse enter event
        - Handles mouse leave event
        - Handles mouse press event
        Arguments:
        - window: Main window of the whole application.
        """

        def labelEnterEvent(label: QLabel) -> None:
            font = label.font()
            font.setUnderline(True)
            label.setFont(font)

        def labelLeaveEvent(label: QLabel) -> None:
            font = label.font()
            font.setUnderline(False)
            label.setFont(font)

        def labelMousePressEvent(event: QMouseEvent, parameterType: str, height: int) -> None:
            if event.buttons() == Qt.MouseButton.LeftButton:
                window.infoWidget.title.setText(_translate(parameterType))
                if parameterType == Key.effectType:
                    if window.mainTabWidget.currentIndex() == MainTab.Global:
                        window.infoWidget.description.setText(Description.effectType())
                        window.infoWidget.widget.setGeometry(0, window.mainFrame.height() - height + 50, window.mainFrame.width(), height)
                    else:
                        window.infoWidget.description.setText(Description.effectType(True))
                        window.infoWidget.widget.setGeometry(0, window.mainFrame.height() - height + 40, window.mainFrame.width(), height + 10)

                elif parameterType == Key.cornerType:
                    if window.mainTabWidget.currentIndex() == MainTab.Global:
                        window.infoWidget.description.setText(Description.cornerType())
                        window.infoWidget.widget.setGeometry(0, window.mainFrame.height() - height + 50, window.mainFrame.width(), height)
                    else:
                        window.infoWidget.description.setText(Description.cornerType(True))
                        window.infoWidget.widget.setGeometry(0, window.mainFrame.height() - height + 40, window.mainFrame.width(), height + 10)

                elif parameterType == Key.enableDropShadow:
                    if window.mainTabWidget.currentIndex() == MainTab.Global:
                        window.infoWidget.widget.setGeometry(0, window.mainFrame.height() - height + 50, window.mainFrame.width(), height)
                        window.infoWidget.description.setText(Description.enableDropShadow())
                        window.infoWidget.widget.setGeometry(0, window.mainFrame.height() - height + 50, window.mainFrame.width(), height)
                    else:
                        window.infoWidget.description.setText(Description.enableDropShadow(True))
                        window.infoWidget.widget.setGeometry(0, window.mainFrame.height() - height + 40, window.mainFrame.width(), height + 10)

                elif parameterType == Key.noBorderColor:
                    if window.mainTabWidget.currentIndex() == MainTab.Global:
                        window.infoWidget.widget.setGeometry(0, window.mainFrame.height() - height + 50, window.mainFrame.width(), height)
                        window.infoWidget.description.setText(Description.noBorderColor())
                        window.infoWidget.widget.setGeometry(0, window.mainFrame.height() - height + 50, window.mainFrame.width(), height)
                    else:
                        window.infoWidget.description.setText(Description.noBorderColor(True))
                        window.infoWidget.widget.setGeometry(0, window.mainFrame.height() - height + 40, window.mainFrame.width(), height + 10)

                elif parameterType == Key.enableThemeColorization:
                    if window.mainTabWidget.currentIndex() == MainTab.Global:
                        window.infoWidget.widget.setGeometry(0, window.mainFrame.height() - height + 50, window.mainFrame.width(), height)
                        window.infoWidget.description.setText(Description.enableThemeColorization())
                        window.infoWidget.widget.setGeometry(0, window.mainFrame.height() - height + 50, window.mainFrame.width(), height)
                    else:
                        window.infoWidget.description.setText(Description.enableThemeColorization(True))
                        window.infoWidget.widget.setGeometry(0, window.mainFrame.height() - height + 40, window.mainFrame.width(), height + 10)

                elif parameterType == Key.darkModeBorderColor:
                    window.infoWidget.description.setText(Description.darkModeBorderColor())
                    window.infoWidget.widget.setGeometry(0, window.mainFrame.height() - height + 50, window.mainFrame.width(), height)

                elif parameterType == Key.lightModeBorderColor:
                    window.infoWidget.description.setText(Description.lightModeBorderColor())
                    window.infoWidget.widget.setGeometry(0, window.mainFrame.height() - height + 50, window.mainFrame.width(), height)

                elif parameterType == Key.darkModeGradientColor:
                    window.infoWidget.description.setText(Description.darkModeGradientColor())
                    window.infoWidget.widget.setGeometry(0, window.mainFrame.height() - height + 50, window.mainFrame.width(), height)

                elif parameterType == Key.lightModeGradientColor:
                    window.infoWidget.description.setText(Description.lightModeGradientColor())
                    window.infoWidget.widget.setGeometry(0, window.mainFrame.height() - height + 50, window.mainFrame.width(), height)

                elif parameterType == Key.disabled:
                    if window.mainTabWidget.currentIndex() == MainTab.Global:
                        window.infoWidget.widget.setGeometry(0, window.mainFrame.height() - height + 50, window.mainFrame.width(), height)
                        window.infoWidget.description.setText(Description.disabled())
                        window.infoWidget.widget.setGeometry(0, window.mainFrame.height() - height + 50, window.mainFrame.width(), height)
                    else:
                        window.infoWidget.description.setText(Description.disabled(True))
                        window.infoWidget.widget.setGeometry(0, window.mainFrame.height() - height + 40, window.mainFrame.width(), height + 10)

                elif parameterType == Key.noSystemDropShadow:
                    window.infoWidget.description.setText(Description.noSystemDropShadow())
                    window.infoWidget.widget.setGeometry(0, window.mainFrame.height() - height + 50, window.mainFrame.width(), height)

                elif parameterType == Key.enableImmersiveStyle:
                    window.infoWidget.description.setText(Description.enableImmersiveStyle())
                    window.infoWidget.widget.setGeometry(0, window.mainFrame.height() - height + 50, window.mainFrame.width(), height)

                elif parameterType == Key.enableCustomRendering:
                    window.infoWidget.description.setText(Description.enableCustomRendering())
                    window.infoWidget.widget.setGeometry(0, window.mainFrame.height() - height + 50, window.mainFrame.width(), height)

                elif parameterType == Key.enableFluentAnimation:
                    window.infoWidget.description.setText(Description.enableFluentAnimation())
                    window.infoWidget.widget.setGeometry(0, window.mainFrame.height() - height + 50, window.mainFrame.width(), height)

                elif parameterType == Key.noModernAppBackgroundColor:
                    window.infoWidget.description.setText(Description.noModernAppBackgroundColor())
                    window.infoWidget.widget.setGeometry(0, window.mainFrame.height() - height + 50, window.mainFrame.width(), height)

                elif parameterType == Key.colorTreatAsTransparent:
                    window.infoWidget.description.setText(Description.colorTreatAsTransparent())
                    window.infoWidget.widget.setGeometry(0, window.mainFrame.height() - height + 50, window.mainFrame.width(), height)

                elif parameterType == Key.colorTreatAsTransparentThreshold:
                    window.infoWidget.description.setText(Description.colorTreatAsTransparentThreshold())
                    window.infoWidget.widget.setGeometry(0, window.mainFrame.height() - height + 50, window.mainFrame.width(), height)

                elif parameterType == Key.fadeOutTime:
                    window.infoWidget.description.setText(Description.fadeOutTime())
                    window.infoWidget.widget.setGeometry(0, window.mainFrame.height() - height + 50, window.mainFrame.width(), height)

                elif parameterType == Key.fadeInTime:
                    window.infoWidget.description.setText(Description.fadeInTime())
                    window.infoWidget.widget.setGeometry(0, window.mainFrame.height() - height + 50, window.mainFrame.width(), height)

                elif parameterType == Key.startRatio:
                    window.infoWidget.description.setText(Description.startRatio())
                    window.infoWidget.widget.setGeometry(0, window.mainFrame.height() - height + 50, window.mainFrame.width(), height)

                elif parameterType == Key.enableImmediateInterupting:
                    window.infoWidget.description.setText(Description.enableImmediateInterupting())
                    window.infoWidget.widget.setGeometry(0, window.mainFrame.height() - height + 50, window.mainFrame.width(), height)

                elif parameterType == Key.popInStyle:
                    window.infoWidget.description.setText(Description.popInStyle())
                    window.infoWidget.widget.setGeometry(0, window.mainFrame.height() - height + 50, window.mainFrame.width(), height)

                elif parameterType == Key.width:
                    isFocusing = window.menuTabWidget.currentIndex() == MenuTab.Focusing
                    window.infoWidget.widget.setGeometry(0, window.mainFrame.height() - height + 50, window.mainFrame.width(), height)
                    window.infoWidget.description.setText(Description.width(isFocusing))

                elif parameterType == Key.cornerRadius:
                    window.infoWidget.description.setText(Description.cornerRadius())
                    window.infoWidget.widget.setGeometry(0, window.mainFrame.height() - height + 50, window.mainFrame.width(), height)

                elif parameterType == Key.darkModeColor:
                    window.infoWidget.description.setText(Description.darkModeColor())
                    window.infoWidget.widget.setGeometry(0, window.mainFrame.height() - height + 50, window.mainFrame.width(), height)

                elif parameterType == Key.lightModeColor:
                    window.infoWidget.description.setText(Description.lightModeColor())
                    window.infoWidget.widget.setGeometry(0, window.mainFrame.height() - height + 50, window.mainFrame.width(), height)

                window.infoWidget.widget.show()
                window.mainFrame.setGraphicsEffect(QGraphicsBlurEffect())
                window.mainFrame.setDisabled(True)
                window.infoWidget.scrollArea.verticalScrollBar().setValue(0)

        def setMouseEvents(label: QLabel, parameterType: str, height: int):
            label.enterEvent = lambda event: labelEnterEvent(label)  # type: ignore
            label.leaveEvent = lambda event: labelLeaveEvent(label)  # type: ignore
            label.mousePressEvent = lambda event: labelMousePressEvent(event, parameterType, height)  # type: ignore
            label.setCursor(Qt.CursorShape.PointingHandCursor)

        # Global
        setMouseEvents(window.lbl_effectType1, Key.effectType, InfoWidgetHeight.FiveItems)
        setMouseEvents(window.lbl_cornerType1, Key.cornerType, InfoWidgetHeight.FourItems)
        setMouseEvents(window.lbl_enableDropShadow1, Key.enableDropShadow, InfoWidgetHeight.TwoItems)
        setMouseEvents(window.lbl_noBorderColor1, Key.noBorderColor, InfoWidgetHeight.TwoItems)
        setMouseEvents(window.lbl_enableThemeColorization1, Key.enableThemeColorization, InfoWidgetHeight.TwoItems)
        setMouseEvents(window.lbl_darkModeBorderColor1, Key.darkModeBorderColor, InfoWidgetHeight.TextShort)
        setMouseEvents(window.lbl_lightModeBorderColor1, Key.lightModeBorderColor, InfoWidgetHeight.TextShort)
        setMouseEvents(window.lbl_darkModeGradientColor1, Key.darkModeGradientColor, InfoWidgetHeight.TextShort)
        setMouseEvents(window.lbl_lightModeGradientColor1, Key.lightModeGradientColor, InfoWidgetHeight.TextShort)
        setMouseEvents(window.lbl_disabledEffect1, Key.disabled, InfoWidgetHeight.TwoItems)

        # DropDown
        setMouseEvents(window.lbl_effectType2, Key.effectType, InfoWidgetHeight.FiveItems)
        setMouseEvents(window.lbl_cornerType2, Key.cornerType, InfoWidgetHeight.FourItems)
        setMouseEvents(window.lbl_enableDropShadow2, Key.enableDropShadow, InfoWidgetHeight.TwoItems)
        setMouseEvents(window.lbl_noBorderColor2, Key.noBorderColor, InfoWidgetHeight.TwoItems)
        setMouseEvents(window.lbl_enableThemeColorization2, Key.enableThemeColorization, InfoWidgetHeight.TwoItems)
        setMouseEvents(window.lbl_darkModeBorderColor2, Key.darkModeBorderColor, InfoWidgetHeight.TextShort)
        setMouseEvents(window.lbl_lightModeBorderColor2, Key.lightModeBorderColor, InfoWidgetHeight.TextShort)
        setMouseEvents(window.lbl_darkModeGradientColor2, Key.darkModeGradientColor, InfoWidgetHeight.TextShort)
        setMouseEvents(window.lbl_lightModeGradientColor2, Key.lightModeGradientColor, InfoWidgetHeight.TextShort)
        setMouseEvents(window.lbl_disabledEffect2, Key.disabled, InfoWidgetHeight.TwoItems)

        # Menu-General
        setMouseEvents(window.lbl_noSystemDropShadow, Key.noSystemDropShadow, InfoWidgetHeight.TwoItems)
        setMouseEvents(window.lbl_enableImmersiveStyle, Key.enableImmersiveStyle, InfoWidgetHeight.TwoItems)
        setMouseEvents(window.lbl_enableCustomRendering, Key.enableCustomRendering, InfoWidgetHeight.TwoItems)
        setMouseEvents(window.lbl_enableFluentAnimation, Key.enableFluentAnimation, InfoWidgetHeight.TwoItems)
        setMouseEvents(window.lbl_noModernAppBackgroundColor, Key.noModernAppBackgroundColor, InfoWidgetHeight.TwoItems)
        setMouseEvents(window.lbl_colorTreatAsTransparent, Key.colorTreatAsTransparent, InfoWidgetHeight.TextShort)
        setMouseEvents(window.lbl_colorTreatAsTransparentThreshold, Key.colorTreatAsTransparentThreshold, InfoWidgetHeight.TextShort)
        setMouseEvents(window.lbl_effectType3, Key.effectType, InfoWidgetHeight.FiveItems)
        setMouseEvents(window.lbl_cornerType3, Key.cornerType, InfoWidgetHeight.FourItems)
        setMouseEvents(window.lbl_enableDropShadow3, Key.enableDropShadow, InfoWidgetHeight.TwoItems)
        setMouseEvents(window.lbl_noBorderColor3, Key.noBorderColor, InfoWidgetHeight.TwoItems)
        setMouseEvents(window.lbl_enableThemeColorization3_1, Key.enableThemeColorization, InfoWidgetHeight.TwoItems)
        setMouseEvents(window.lbl_darkModeBorderColor3, Key.darkModeBorderColor, InfoWidgetHeight.TextShort)
        setMouseEvents(window.lbl_lightModeBorderColor3, Key.lightModeBorderColor, InfoWidgetHeight.TextShort)
        setMouseEvents(window.lbl_darkModeGradientColor3, Key.darkModeGradientColor, InfoWidgetHeight.TextShort)
        setMouseEvents(window.lbl_lightModeGradientColor3, Key.lightModeGradientColor, InfoWidgetHeight.TextShort)
        setMouseEvents(window.lbl_disabledEffect3_1, Key.disabled, InfoWidgetHeight.TwoItems)

        # Menu-Animation
        setMouseEvents(window.lbl_fadeOutTime, Key.fadeOutTime, InfoWidgetHeight.TextShort)
        setMouseEvents(window.lbl_fadeInTime, Key.fadeInTime, InfoWidgetHeight.TextShort)
        setMouseEvents(window.lbl_popInTime, Key.popInTime, InfoWidgetHeight.TextShort)
        setMouseEvents(window.lbl_popInStyle, Key.popInStyle, InfoWidgetHeight.FourItems)
        setMouseEvents(window.lbl_startRatio, Key.startRatio, InfoWidgetHeight.TextShort)
        setMouseEvents(window.lbl_enableImmediateInterupting, Key.enableImmediateInterupting, InfoWidgetHeight.TwoItems)

        # Menu-Hot
        setMouseEvents(window.lbl_darkModeColor1_1, Key.darkModeColor, InfoWidgetHeight.TextShort)
        setMouseEvents(window.lbl_lightModeColor1_1, Key.lightModeColor, InfoWidgetHeight.TextShort)
        setMouseEvents(window.lbl_disabledEffect3_2, Key.disabled, InfoWidgetHeight.TwoItems)
        setMouseEvents(window.lbl_cornerRadius1_1, Key.cornerRadius, InfoWidgetHeight.TextShort)
        setMouseEvents(window.lbl_enableThemeColorization3_2, Key.enableThemeColorization, InfoWidgetHeight.TwoItems)

        # Menu-DisabledHot
        setMouseEvents(window.lbl_darkModeColor1_2, Key.darkModeColor, InfoWidgetHeight.TextShort)
        setMouseEvents(window.lbl_lightModeColor1_2, Key.lightModeColor, InfoWidgetHeight.TextShort)
        setMouseEvents(window.lbl_disabledEffect3_3, Key.disabled, InfoWidgetHeight.TwoItems)
        setMouseEvents(window.lbl_cornerRadius1_2, Key.cornerRadius, InfoWidgetHeight.TextShort)
        setMouseEvents(window.lbl_enableThemeColorization3_3, Key.enableThemeColorization, InfoWidgetHeight.TwoItems)

        # Menu-Focusing
        setMouseEvents(window.lbl_width1_1, Key.width, InfoWidgetHeight.TextShort)
        setMouseEvents(window.lbl_darkModeColor1_3, Key.darkModeColor, InfoWidgetHeight.TextShort)
        setMouseEvents(window.lbl_lightModeColor1_3, Key.lightModeColor, InfoWidgetHeight.TextShort)
        setMouseEvents(window.lbl_disabledEffect3_4, Key.disabled, InfoWidgetHeight.TwoItems)
        setMouseEvents(window.lbl_cornerRadius1_3, Key.cornerRadius, InfoWidgetHeight.TextShort)
        setMouseEvents(window.lbl_enableThemeColorization3_4, Key.enableThemeColorization, InfoWidgetHeight.TwoItems)

        # Menu-Separator
        setMouseEvents(window.lbl_width1_2, Key.width, InfoWidgetHeight.TextShort)
        setMouseEvents(window.lbl_darkModeColor1_3, Key.darkModeColor, InfoWidgetHeight.TextShort)
        setMouseEvents(window.lbl_lightModeColor1_3, Key.lightModeColor, InfoWidgetHeight.TextShort)
        setMouseEvents(window.lbl_disabledEffect3_4, Key.disabled, InfoWidgetHeight.TwoItems)
        setMouseEvents(window.lbl_cornerRadius1_3, Key.cornerRadius, InfoWidgetHeight.TextShort)
        setMouseEvents(window.lbl_enableThemeColorization3_4, Key.enableThemeColorization, InfoWidgetHeight.TwoItems)

        # Tooltip
        setMouseEvents(window.lbl_effectType4, Key.effectType, InfoWidgetHeight.FiveItems)
        setMouseEvents(window.lbl_cornerType4, Key.cornerType, InfoWidgetHeight.FourItems)
        setMouseEvents(window.lbl_enableDropShadow4, Key.enableDropShadow, InfoWidgetHeight.TwoItems)
        setMouseEvents(window.lbl_noBorderColor4, Key.noBorderColor, InfoWidgetHeight.TwoItems)
        setMouseEvents(window.lbl_enableThemeColorization4, Key.enableThemeColorization, InfoWidgetHeight.TwoItems)
        setMouseEvents(window.lbl_darkModeBorderColor4, Key.darkModeBorderColor, InfoWidgetHeight.TextShort)
        setMouseEvents(window.lbl_lightModeBorderColor4, Key.lightModeBorderColor, InfoWidgetHeight.TextShort)
        setMouseEvents(window.lbl_darkModeGradientColor4, Key.darkModeGradientColor, InfoWidgetHeight.TextShort)
        setMouseEvents(window.lbl_lightModeGradientColor4, Key.lightModeGradientColor, InfoWidgetHeight.TextShort)
        setMouseEvents(window.lbl_disabledEffect4, Key.disabled, InfoWidgetHeight.TwoItems)

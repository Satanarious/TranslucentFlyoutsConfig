# Library Imports
from __future__ import annotations
from typing import TYPE_CHECKING
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QPushButton, QLineEdit, QComboBox, QSpinBox
from PyQt6.QtGui import QIcon


# Relative Imports
from Dialogs.color_picker import ColorPicker
from Data.defaults import Defaults
from Data.stylesheet import StyleSheet
from Data.paths import Path
from Data.user import ClassVar, Saved
from save_settings import SaveSettings

if TYPE_CHECKING:
    from main import Main


class Connectors:
    @staticmethod
    def connectApplyButtons(window: Main) -> None:
        """
        Method to:
        - Connect Apply Button to its respective functions
        """
        window.applyButton1.clicked.connect(lambda a: SaveSettings.Global.save(window))
        window.applyButton2.clicked.connect(lambda a: SaveSettings.DropDown.save(window))
        window.applyButton3_1.clicked.connect(lambda a: SaveSettings.Menu.save(window))
        window.applyButton3_2.clicked.connect(lambda a: SaveSettings.Menu.Animation.save(window))
        window.applyButton3_3.clicked.connect(lambda a: SaveSettings.Menu.Hot.save(window))
        window.applyButton3_4.clicked.connect(lambda a: SaveSettings.Menu.DisabledHot.save(window))
        window.applyButton3_5.clicked.connect(lambda a: SaveSettings.Menu.Focusing.save(window))
        window.applyButton3_6.clicked.connect(lambda a: SaveSettings.Menu.Separator.save(window))
        window.applyButton4.clicked.connect(lambda a: SaveSettings.Tooltip.save(window))

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

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
from Data.user import ClassVar
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
        window.applyButton1.clicked.connect(SaveSettings.General.save)
        window.applyButton2.clicked.connect(SaveSettings.DropDown.save)
        window.applyButton3_1.clicked.connect(SaveSettings.Menu.save)
        window.applyButton3_2.clicked.connect(SaveSettings.Menu.Animation.save)
        window.applyButton3_3.clicked.connect(SaveSettings.Menu.Hot.save)
        window.applyButton3_4.clicked.connect(SaveSettings.Menu.DisabledHot.save)
        window.applyButton3_5.clicked.connect(SaveSettings.Menu.Focusing.save)
        window.applyButton3_6.clicked.connect(SaveSettings.Menu.Separator.save)

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
            savedValue: str,
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
                    resetButton.clicked.connect(
                        lambda a: colorPickerButton.setStyleSheet(
                            StyleSheet.buttoResetStyleSheet() if (defaultValue == "") else StyleSheet.buttonColorStylesheet(str(defaultValue))
                        )
                    )
                    resetButton.clicked.connect(lambda a: colorPickerButton.setIcon(QIcon(Path.IconPaths.ColorPicker)))

                    resetButton.customContextMenuRequested.connect(lambda a: valueWidget.setText(getSavedValue(savedValue)))
            elif isinstance(valueWidget, QComboBox):
                if type(defaultValue) == int:
                    resetButton.clicked.connect(lambda a: valueWidget.setCurrentIndex(defaultValue))
                    resetButton.customContextMenuRequested.connect(lambda a: valueWidget.setCurrentIndex(getSavedValue(savedValue)))
            elif isinstance(valueWidget, QSpinBox):
                if type(defaultValue) == int:
                    resetButton.clicked.connect(lambda a: valueWidget.setValue(defaultValue))
                    resetButton.customContextMenuRequested.connect(lambda a: valueWidget.setValue(getSavedValue(savedValue)))

        # General
        configureResetButton(
            resetButton=window.reset_effect_type1,
            valueWidget=window.effectType1,
            defaultValue=Defaults.General.effectType,
            savedValue=ClassVar.joinVars(ClassVar.general, ClassVar.effectType),
            colorPickerButton=None,
        )
        configureResetButton(
            resetButton=window.reset_corner_type1,
            valueWidget=window.cornerType1,
            defaultValue=Defaults.General.cornerType,
            savedValue=ClassVar.joinVars(ClassVar.general, ClassVar.cornerType),
            colorPickerButton=None,
        )
        configureResetButton(
            resetButton=window.reset_drop_shadow1,
            valueWidget=window.enableDropShadow1,
            defaultValue=Defaults.General.enableDropShadow,
            savedValue=ClassVar.joinVars(ClassVar.general, ClassVar.enableDropShadow),
            colorPickerButton=None,
        )
        configureResetButton(
            resetButton=window.reset_theme_colorization1,
            valueWidget=window.enableThemeColorization1,
            defaultValue=Defaults.General.enableThemeColorization,
            savedValue=ClassVar.joinVars(ClassVar.general, ClassVar.enableThemeColorization),
            colorPickerButton=None,
        )
        configureResetButton(
            resetButton=window.reset_border_color1,
            valueWidget=window.noBorderColor1,
            defaultValue=Defaults.General.noBorderColor,
            savedValue=ClassVar.joinVars(ClassVar.general, ClassVar.noBorderColor),
            colorPickerButton=None,
        )
        configureResetButton(
            resetButton=window.reset_dark_mode_border_color1,
            valueWidget=window.darkModeBorderColor1,
            defaultValue=Defaults.General.darkModeBorderColor,
            savedValue=ClassVar.joinVars(ClassVar.general, ClassVar.darkModeBorderColor),
            colorPickerButton=window.dark_mode_border_color_picker1,
        )
        configureResetButton(
            resetButton=window.reset_light_mode_border_color1,
            valueWidget=window.lightModeBorderColor1,
            defaultValue=Defaults.General.lightModeBorderColor,
            savedValue=ClassVar.joinVars(ClassVar.general, ClassVar.lightModeBorderColor),
            colorPickerButton=window.light_mode_border_color_picker1,
        )
        configureResetButton(
            resetButton=window.reset_dark_mode_gradient_color1,
            valueWidget=window.darkModeGradientColor1,
            defaultValue=Defaults.General.darkModeGradientColor,
            savedValue=ClassVar.joinVars(ClassVar.general, ClassVar.darkModeGradientColor),
            colorPickerButton=window.dark_mode_gradient_color_picker1,
        )
        configureResetButton(
            resetButton=window.reset_light_mode_gradient_color1,
            valueWidget=window.lightModeGradientColor1,
            defaultValue=Defaults.General.lightModeGradientColor,
            savedValue=ClassVar.joinVars(ClassVar.general, ClassVar.lightModeGradientColor),
            colorPickerButton=window.light_mode_gradient_color_picker1,
        )
        configureResetButton(
            resetButton=window.reset_disabled1,
            valueWidget=window.disabledEffect1,
            defaultValue=Defaults.General.disabled,
            savedValue=ClassVar.joinVars(ClassVar.general, ClassVar.disabled),
            colorPickerButton=None,
        )

        # DropDown
        configureResetButton(
            resetButton=window.reset_effect_type2,
            valueWidget=window.effectType2,
            defaultValue=Defaults.DropDown.effectType,
            savedValue=ClassVar.joinVars(ClassVar.dropdown, ClassVar.effectType),
            colorPickerButton=None,
        )
        configureResetButton(
            resetButton=window.reset_corner_type2,
            valueWidget=window.cornerType2,
            defaultValue=Defaults.DropDown.cornerType,
            savedValue=ClassVar.joinVars(ClassVar.dropdown, ClassVar.cornerType),
            colorPickerButton=None,
        )
        configureResetButton(
            resetButton=window.reset_drop_shadow2,
            valueWidget=window.enableDropShadow2,
            defaultValue=Defaults.DropDown.enableDropShadow,
            savedValue=ClassVar.joinVars(ClassVar.dropdown, ClassVar.enableDropShadow),
            colorPickerButton=None,
        )
        configureResetButton(
            resetButton=window.reset_theme_colorization2,
            valueWidget=window.enableThemeColorization2,
            defaultValue=Defaults.DropDown.enableThemeColorization,
            savedValue=ClassVar.joinVars(ClassVar.dropdown, ClassVar.enableThemeColorization),
            colorPickerButton=None,
        )
        configureResetButton(
            resetButton=window.reset_border_color2,
            valueWidget=window.noBorderColor2,
            defaultValue=Defaults.DropDown.noBorderColor,
            savedValue=ClassVar.joinVars(ClassVar.dropdown, ClassVar.noBorderColor),
            colorPickerButton=None,
        )
        configureResetButton(
            resetButton=window.reset_dark_mode_border_color2,
            valueWidget=window.darkModeBorderColor2,
            defaultValue=Defaults.DropDown.darkModeBorderColor,
            savedValue=ClassVar.joinVars(ClassVar.dropdown, ClassVar.darkModeBorderColor),
            colorPickerButton=window.dark_mode_border_color_picker2,
        )
        configureResetButton(
            resetButton=window.reset_light_mode_border_color2,
            valueWidget=window.lightModeBorderColor2,
            defaultValue=Defaults.DropDown.lightModeBorderColor,
            savedValue=ClassVar.joinVars(ClassVar.dropdown, ClassVar.lightModeBorderColor),
            colorPickerButton=window.light_mode_border_color_picker2,
        )
        configureResetButton(
            resetButton=window.reset_dark_mode_gradient_color2,
            valueWidget=window.darkModeGradientColor2,
            defaultValue=Defaults.DropDown.darkModeGradientColor,
            savedValue=ClassVar.joinVars(ClassVar.dropdown, ClassVar.darkModeGradientColor),
            colorPickerButton=window.dark_mode_gradient_color_picker2,
        )
        configureResetButton(
            resetButton=window.reset_light_mode_gradient_color2,
            valueWidget=window.lightModeGradientColor2,
            defaultValue=Defaults.DropDown.lightModeGradientColor,
            savedValue=ClassVar.joinVars(ClassVar.dropdown, ClassVar.lightModeGradientColor),
            colorPickerButton=window.light_mode_gradient_color_picker2,
        )
        configureResetButton(
            resetButton=window.reset_disabled2,
            valueWidget=window.disabledEffect2,
            defaultValue=Defaults.DropDown.disabled,
            savedValue=ClassVar.joinVars(ClassVar.dropdown, ClassVar.disabled),
            colorPickerButton=None,
        )

        # Menu-General
        configureResetButton(
            resetButton=window.reset_system_drop_shadow,
            valueWidget=window.noSystemDropShadow,
            defaultValue=Defaults.Menu.noSystemDropShadow,
            savedValue=ClassVar.joinVars(ClassVar.menu, ClassVar.noSystemDropShadow),
            colorPickerButton=None,
        )
        configureResetButton(
            resetButton=window.reset_immersive_style,
            valueWidget=window.enableImmersiveStyle,
            defaultValue=Defaults.Menu.enableImmersiveStyle,
            savedValue=ClassVar.joinVars(ClassVar.menu, ClassVar.enableImmersiveStyle),
            colorPickerButton=None,
        )
        configureResetButton(
            resetButton=window.reset_custom_rendering,
            valueWidget=window.enableCustomRendering,
            defaultValue=Defaults.Menu.enableCustomRendering,
            savedValue=ClassVar.joinVars(ClassVar.menu, ClassVar.enableCustomRendering),
            colorPickerButton=None,
        )
        configureResetButton(
            resetButton=window.reset_fluent_animation,
            valueWidget=window.enableFluentAnimation,
            defaultValue=Defaults.Menu.enableFluentAnimation,
            savedValue=ClassVar.joinVars(ClassVar.menu, ClassVar.enableFluentAnimation),
            colorPickerButton=None,
        )
        configureResetButton(
            resetButton=window.reset_effect_type3,
            valueWidget=window.effectType3,
            defaultValue=Defaults.Menu.effectType,
            savedValue=ClassVar.joinVars(ClassVar.menu, ClassVar.effectType),
            colorPickerButton=None,
        )
        configureResetButton(
            resetButton=window.reset_corner_type3,
            valueWidget=window.cornerType3,
            defaultValue=Defaults.Menu.cornerType,
            savedValue=ClassVar.joinVars(ClassVar.menu, ClassVar.cornerType),
            colorPickerButton=None,
        )

        configureResetButton(
            resetButton=window.reset_drop_shadow3,
            valueWidget=window.enableDropShadow3,
            defaultValue=Defaults.Menu.enableDropShadow,
            savedValue=ClassVar.joinVars(ClassVar.menu, ClassVar.enableDropShadow),
            colorPickerButton=None,
        )
        configureResetButton(
            resetButton=window.reset_theme_colorization3_1,
            valueWidget=window.enableThemeColorization3_1,
            defaultValue=Defaults.Menu.enableThemeColorization,
            savedValue=ClassVar.joinVars(ClassVar.menu, ClassVar.enableThemeColorization),
            colorPickerButton=None,
        )
        configureResetButton(
            resetButton=window.reset_border_color3,
            valueWidget=window.noBorderColor3,
            defaultValue=Defaults.Menu.noBorderColor,
            savedValue=ClassVar.joinVars(ClassVar.menu, ClassVar.noBorderColor),
            colorPickerButton=None,
        )
        configureResetButton(
            resetButton=window.reset_dark_mode_border_color3,
            valueWidget=window.darkModeBorderColor3,
            defaultValue=Defaults.Menu.darkModeBorderColor,
            savedValue=ClassVar.joinVars(ClassVar.menu, ClassVar.darkModeBorderColor),
            colorPickerButton=window.dark_mode_border_color_picker3,
        )

        configureResetButton(
            resetButton=window.reset_light_mode_border_color3,
            valueWidget=window.lightModeBorderColor3,
            defaultValue=Defaults.Menu.lightModeBorderColor,
            savedValue=ClassVar.joinVars(ClassVar.menu, ClassVar.lightModeBorderColor),
            colorPickerButton=window.light_mode_border_color_picker3,
        )
        configureResetButton(
            resetButton=window.reset_dark_mode_gradient_color3,
            valueWidget=window.darkModeGradientColor3,
            defaultValue=Defaults.Menu.darkModeGradientColor,
            savedValue=ClassVar.joinVars(ClassVar.menu, ClassVar.darkModeGradientColor),
            colorPickerButton=window.dark_mode_gradient_color_picker3,
        )
        configureResetButton(
            resetButton=window.reset_light_mode_gradient_color3,
            valueWidget=window.lightModeGradientColor3,
            defaultValue=Defaults.Menu.lightModeGradientColor,
            savedValue=ClassVar.joinVars(ClassVar.menu, ClassVar.lightModeGradientColor),
            colorPickerButton=window.light_mode_gradient_color_picker3,
        )
        configureResetButton(
            resetButton=window.reset_disabled3_1,
            valueWidget=window.disabledEffect3_1,
            defaultValue=Defaults.Menu.disabled,
            savedValue=ClassVar.joinVars(ClassVar.menu, ClassVar.disabled),
            colorPickerButton=None,
        )
        # Menu-Animation
        configureResetButton(
            resetButton=window.reset_fade_out_time,
            valueWidget=window.fadeOutTime,
            defaultValue=Defaults.Menu.Animation.fadeOutTime,
            savedValue=ClassVar.joinVars(ClassVar.menu, ClassVar.animation, ClassVar.fadeOutTime),
            colorPickerButton=None,
        )
        configureResetButton(
            resetButton=window.reset_pop_in_time,
            valueWidget=window.popInTime,
            defaultValue=Defaults.Menu.Animation.popInTime,
            savedValue=ClassVar.joinVars(ClassVar.menu, ClassVar.animation, ClassVar.popInTime),
            colorPickerButton=None,
        )
        configureResetButton(
            resetButton=window.reset_fade_in_time,
            valueWidget=window.fadeInTime,
            defaultValue=Defaults.Menu.Animation.fadeInTime,
            savedValue=ClassVar.joinVars(ClassVar.menu, ClassVar.animation, ClassVar.fadeInTime),
            colorPickerButton=None,
        )
        configureResetButton(
            resetButton=window.reset_pop_in_style,
            valueWidget=window.popInStyle,
            defaultValue=Defaults.Menu.Animation.popInStyle,
            savedValue=ClassVar.joinVars(ClassVar.menu, ClassVar.animation, ClassVar.popInStyle),
            colorPickerButton=None,
        )
        configureResetButton(
            resetButton=window.reset_start_ratio,
            valueWidget=window.startRatio,
            defaultValue=Defaults.Menu.Animation.startRatio,
            savedValue=ClassVar.joinVars(ClassVar.menu, ClassVar.animation, ClassVar.startRatio),
            colorPickerButton=None,
        )
        configureResetButton(
            resetButton=window.reset_immediate_interupting,
            valueWidget=window.enableImmediateInterupting,
            defaultValue=Defaults.Menu.Animation.enableImmediateInterupting,
            savedValue=ClassVar.joinVars(ClassVar.menu, ClassVar.animation, ClassVar.enableImmediateInterupting),
            colorPickerButton=None,
        )
        # Menu-Hot
        configureResetButton(
            resetButton=window.reset_dark_mode_color1_1,
            valueWidget=window.darkModeColor1_1,
            defaultValue=Defaults.Menu.Hot.darkModeColor,
            savedValue=ClassVar.joinVars(ClassVar.menu, ClassVar.hot, ClassVar.darkModeColor),
            colorPickerButton=window.dark_mode_color_picker1_1,
        )
        configureResetButton(
            resetButton=window.reset_light_mode_color1_1,
            valueWidget=window.lightModeColor1_1,
            defaultValue=Defaults.Menu.Hot.lightModeColor,
            savedValue=ClassVar.joinVars(ClassVar.menu, ClassVar.hot, ClassVar.lightModeColor),
            colorPickerButton=window.light_mode_color_picker1_1,
        )
        configureResetButton(
            resetButton=window.reset_disabled3_2,
            valueWidget=window.disabledEffect3_2,
            defaultValue=Defaults.Menu.Hot.disabled,
            savedValue=ClassVar.joinVars(ClassVar.menu, ClassVar.hot, ClassVar.disabled),
            colorPickerButton=None,
        )
        configureResetButton(
            resetButton=window.reset_corner_radius1_1,
            valueWidget=window.cornerRadius1_1,
            defaultValue=Defaults.Menu.Hot.cornerRadius,
            savedValue=ClassVar.joinVars(ClassVar.menu, ClassVar.hot, ClassVar.cornerRadius),
            colorPickerButton=None,
        )
        configureResetButton(
            resetButton=window.reset_theme_colorization3_2,
            valueWidget=window.enableThemeColorization3_2,
            defaultValue=Defaults.Menu.Hot.enableThemeColorization,
            savedValue=ClassVar.joinVars(ClassVar.menu, ClassVar.hot, ClassVar.enableThemeColorization),
            colorPickerButton=None,
        )
        # Menu-Disabled Hot
        configureResetButton(
            resetButton=window.reset_dark_mode_color1_2,
            valueWidget=window.darkModeColor1_2,
            defaultValue=Defaults.Menu.DisabledHot.darkModeColor,
            savedValue=ClassVar.joinVars(ClassVar.menu, ClassVar.disabledHot, ClassVar.darkModeColor),
            colorPickerButton=window.dark_mode_color_picker1_2,
        )
        configureResetButton(
            resetButton=window.reset_light_mode_color1_2,
            valueWidget=window.lightModeColor1_2,
            defaultValue=Defaults.Menu.DisabledHot.lightModeColor,
            savedValue=ClassVar.joinVars(ClassVar.menu, ClassVar.disabledHot, ClassVar.lightModeColor),
            colorPickerButton=window.light_mode_color_picker1_2,
        )
        configureResetButton(
            resetButton=window.reset_disabled3_3,
            valueWidget=window.disabledEffect3_3,
            defaultValue=Defaults.Menu.DisabledHot.disabled,
            savedValue=ClassVar.joinVars(ClassVar.menu, ClassVar.disabledHot, ClassVar.disabled),
            colorPickerButton=None,
        )
        configureResetButton(
            resetButton=window.reset_corner_radius1_2,
            valueWidget=window.cornerRadius1_2,
            defaultValue=Defaults.Menu.DisabledHot.cornerRadius,
            savedValue=ClassVar.joinVars(ClassVar.menu, ClassVar.disabledHot, ClassVar.cornerRadius),
            colorPickerButton=None,
        )
        configureResetButton(
            resetButton=window.reset_theme_colorization3_3,
            valueWidget=window.enableThemeColorization3_3,
            defaultValue=Defaults.Menu.Hot.enableThemeColorization,
            savedValue=ClassVar.joinVars(ClassVar.menu, ClassVar.disabledHot, ClassVar.enableThemeColorization),
            colorPickerButton=None,
        )

        # Menu-Focusing
        configureResetButton(
            resetButton=window.reset_width1_1,
            valueWidget=window.width1_1,
            defaultValue=Defaults.Menu.Focusing.width,
            savedValue=ClassVar.joinVars(ClassVar.menu, ClassVar.focusing, ClassVar.width),
            colorPickerButton=None,
        )
        configureResetButton(
            resetButton=window.reset_dark_mode_color1_3,
            valueWidget=window.darkModeColor1_3,
            defaultValue=Defaults.Menu.Focusing.darkModeColor,
            savedValue=ClassVar.joinVars(ClassVar.menu, ClassVar.focusing, ClassVar.darkModeColor),
            colorPickerButton=window.dark_mode_color_picker1_3,
        )
        configureResetButton(
            resetButton=window.reset_light_mode_color1_3,
            valueWidget=window.lightModeColor1_3,
            defaultValue=Defaults.Menu.Focusing.lightModeColor,
            savedValue=ClassVar.joinVars(ClassVar.menu, ClassVar.focusing, ClassVar.lightModeColor),
            colorPickerButton=window.light_mode_color_picker1_3,
        )
        configureResetButton(
            resetButton=window.reset_disabled3_4,
            valueWidget=window.disabledEffect3_4,
            defaultValue=Defaults.Menu.Focusing.disabled,
            savedValue=ClassVar.joinVars(ClassVar.menu, ClassVar.focusing, ClassVar.disabled),
            colorPickerButton=None,
        )
        configureResetButton(
            resetButton=window.reset_corner_radius1_3,
            valueWidget=window.cornerRadius1_3,
            defaultValue=Defaults.Menu.Focusing.cornerRadius,
            savedValue=ClassVar.joinVars(ClassVar.menu, ClassVar.focusing, ClassVar.cornerRadius),
            colorPickerButton=None,
        )
        configureResetButton(
            resetButton=window.reset_theme_colorization3_4,
            valueWidget=window.enableThemeColorization3_4,
            defaultValue=Defaults.Menu.Focusing.enableThemeColorization,
            savedValue=ClassVar.joinVars(ClassVar.menu, ClassVar.focusing, ClassVar.enableThemeColorization),
            colorPickerButton=None,
        )

        # Menu-Separator
        configureResetButton(
            resetButton=window.reset_width1_2,
            valueWidget=window.width1_2,
            defaultValue=Defaults.Menu.Separator.width,
            savedValue=ClassVar.joinVars(ClassVar.menu, ClassVar.separator, ClassVar.width),
            colorPickerButton=None,
        )
        configureResetButton(
            resetButton=window.reset_dark_mode_color1_4,
            valueWidget=window.darkModeColor1_4,
            defaultValue=Defaults.Menu.Separator.darkModeColor,
            savedValue=ClassVar.joinVars(ClassVar.menu, ClassVar.separator, ClassVar.darkModeColor),
            colorPickerButton=window.dark_mode_color_picker1_4,
        )
        configureResetButton(
            resetButton=window.reset_light_mode_color1_4,
            valueWidget=window.lightModeColor1_4,
            defaultValue=Defaults.Menu.Separator.lightModeColor,
            savedValue=ClassVar.joinVars(ClassVar.menu, ClassVar.separator, ClassVar.lightModeColor),
            colorPickerButton=window.light_mode_color_picker1_4,
        )
        configureResetButton(
            resetButton=window.reset_disabled3_5,
            valueWidget=window.disabledEffect3_5,
            defaultValue=Defaults.Menu.Separator.disabled,
            savedValue=ClassVar.joinVars(ClassVar.menu, ClassVar.separator, ClassVar.disabled),
            colorPickerButton=None,
        )
        configureResetButton(
            resetButton=window.reset_corner_radius1_4,
            valueWidget=window.cornerRadius1_4,
            defaultValue=Defaults.Menu.Separator.cornerRadius,
            savedValue=ClassVar.joinVars(ClassVar.menu, ClassVar.separator, ClassVar.cornerRadius),
            colorPickerButton=None,
        )
        configureResetButton(
            resetButton=window.reset_theme_colorization3_5,
            valueWidget=window.enableThemeColorization3_5,
            defaultValue=Defaults.Menu.Separator.enableThemeColorization,
            savedValue=ClassVar.joinVars(ClassVar.menu, ClassVar.separator, ClassVar.enableThemeColorization),
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
        # General
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

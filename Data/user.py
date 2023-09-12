# Library Imports
from __future__ import annotations
from typing import TYPE_CHECKING
import json

# Relative Imports
from Registry.reg_edit import EditRegistry
from Data.defaults import Defaults
from color_picker import ColorPicker
from Data.paths import Path

if TYPE_CHECKING:
    from main import Main

# Dump Residue or Previously Present Parameters
with open(Path.DBPaths.UserSettings, "w") as json_file:
    json.dump(EditRegistry.fetchAllValues(), json_file)

rawDefaults: dict = dict(json.load(open(Path.DBPaths.UserSettings, "r")))


class ClassVar:
    @staticmethod
    def joinVars(*vars: str) -> str:
        return "Saved." + ".".join(vars)

    _global: str = "Global"
    dropdown: str = "DropDown"
    menu: str = "Menu"
    animation: str = "Animation"
    disabledHot: str = "DisabledHot"
    focusing: str = "Focusing"
    hot: str = "Hot"
    separator: str = "Separator"
    tooltip: str = "Tooltip"
    effectType: str = "effectType"
    cornerType: str = "cornerType"
    enableDropShadow: str = "enableDropShadow"
    noBorderColor: str = "noBorderColor"
    darkModeBorderColor: str = "darkModeBorderColor"
    lightModeBorderColor: str = "lightModeBorderColor"
    darkModeGradientColor: str = "darkModeGradientColor"
    lightModeGradientColor: str = "lightModeGradientColor"
    disabled: str = "disabled"
    noSystemDropShadow: str = "noSystemDropShadow"
    enableImmersiveStyle: str = "enableImmersiveStyle"
    enableCustomRendering: str = "enableCustomRendering"
    enableFluentAnimation: str = "enableFluentAnimation"
    noModernAppBackgroundColor: str = "noModernAppBackgroundColor"
    colorTreatAsTransparent: str = "colorTreatAsTransparent"
    colorTreatAsTransparentThreshold: str = "colorTreatAsTransparentThreshold"
    fadeOutTime: str = "fadeOutTime"
    popInTime: str = "popInTime"
    fadeInTime: str = "fadeInTime"
    popInStyle: str = "popInStyle"
    startRatio: str = "startRatio"
    enableImmediateInterupting: str = "enableImmediateInterupting"
    cornerRadius: str = "cornerRadius"
    darkModeColor: str = "darkModeColor"
    lightModeColor: str = "lightModeColor"
    enableThemeColorization: str = "enableThemeColorization"
    width: str = "width"


# Keys from JSON file
class Key:
    _global: str = "Global"
    dropdown: str = "DropDown"
    menu: str = "Menu"
    animation: str = "Animation"
    disabledHot: str = "Disabled Hot"
    focusing: str = "Focusing"
    hot: str = "Hot"
    separator: str = "Separator"
    tooltip: str = "Tooltip"
    effectType: str = "Effect Type"
    cornerType: str = "Corner Type"
    enableDropShadow: str = "Enable Drop Shadow"
    noBorderColor: str = "No Border Color"
    darkModeBorderColor: str = "Dark Mode Border Color"
    lightModeBorderColor: str = "Light Mode Border Color"
    darkModeGradientColor: str = "Dark Mode Gradient Color"
    lightModeGradientColor: str = "Light Mode Gradient Color"
    disabled: str = "Disabled"
    noSystemDropShadow: str = "No System Drop Shadow"
    enableImmersiveStyle: str = "Enable Immersive Style"
    enableCustomRendering: str = "Enable Custom Rendering"
    enableFluentAnimation: str = "Enable Fluent Animation"
    noModernAppBackgroundColor: str = "No Modern App Background Color"
    colorTreatAsTransparent: str = "Color Treat As Transparent"
    colorTreatAsTransparentThreshold: str = "Color Treat As Transparent Threshold"
    fadeOutTime: str = "Fade Out Time"
    popInTime: str = "Pop In Time"
    fadeInTime: str = "Fade In Time"
    popInStyle: str = "Pop In Style"
    startRatio: str = "Start Ratio"
    enableImmediateInterupting: str = "Enable Immediate Interupting"
    cornerRadius: str = "Corner Radius"
    darkModeColor: str = "Dark Mode Color"
    lightModeColor: str = "Light Mode Color"
    enableThemeColorization: str = "Enable Theme Colorization"
    width: str = "Width"


# Getter Classes
class Saved:
    @staticmethod
    def updateJSON():
        with open(Path.DBPaths.UserSettings, "w") as json_file:
            json.dump(rawDefaults, json_file)

    @staticmethod
    def updateUI(window: Main):
        # Global
        window.effectType1.setCurrentIndex(Saved.Global.effectType)
        window.cornerType1.setCurrentIndex(Saved.Global.cornerType)
        window.enableDropShadow1.setCurrentIndex(Saved.Global.enableDropShadow)
        window.noBorderColor1.setCurrentIndex(Saved.Global.noBorderColor)
        window.enableThemeColorization1.setCurrentIndex(Saved.Global.enableThemeColorization)
        window.darkModeBorderColor1.setText(Saved.Global.darkModeBorderColor)
        if Saved.Global.darkModeBorderColor != Defaults.Global.darkModeBorderColor:
            ColorPicker.changeButtonColor(Saved.Global.darkModeBorderColor, window.dark_mode_border_color_picker1)
        window.lightModeBorderColor1.setText(Saved.Global.lightModeBorderColor)
        if Saved.Global.lightModeBorderColor != Defaults.Global.lightModeBorderColor:
            ColorPicker.changeButtonColor(Saved.Global.lightModeBorderColor, window.light_mode_border_color_picker1)
        window.darkModeGradientColor1.setText(Saved.Global.darkModeGradientColor)
        if Saved.Global.darkModeGradientColor != Defaults.Global.darkModeGradientColor:
            ColorPicker.changeButtonColor(Saved.Global.darkModeGradientColor, window.dark_mode_gradient_color_picker1)
        window.lightModeGradientColor1.setText(Saved.Global.lightModeGradientColor)
        if Saved.Global.lightModeGradientColor != Defaults.Global.lightModeGradientColor:
            ColorPicker.changeButtonColor(Saved.Global.lightModeGradientColor, window.light_mode_gradient_color_picker1)
        window.disabledEffect1.setCurrentIndex(Saved.Global.disabled)

        # DropDown
        window.effectType2.setCurrentIndex(Saved.DropDown.effectType)
        window.cornerType2.setCurrentIndex(Saved.DropDown.cornerType)
        window.enableDropShadow2.setCurrentIndex(Saved.DropDown.enableDropShadow)
        window.noBorderColor2.setCurrentIndex(Saved.DropDown.noBorderColor)
        window.enableThemeColorization2.setCurrentIndex(Saved.DropDown.enableThemeColorization)
        window.darkModeBorderColor2.setText(Saved.DropDown.darkModeBorderColor)
        if Saved.DropDown.darkModeBorderColor != Defaults.DropDown.darkModeBorderColor:
            ColorPicker.changeButtonColor(Saved.DropDown.darkModeBorderColor, window.dark_mode_border_color_picker2)
        window.lightModeBorderColor2.setText(Saved.DropDown.lightModeBorderColor)
        if Saved.DropDown.lightModeBorderColor != Defaults.DropDown.lightModeBorderColor:
            ColorPicker.changeButtonColor(Saved.DropDown.lightModeBorderColor, window.light_mode_border_color_picker2)
        window.darkModeGradientColor2.setText(Saved.DropDown.darkModeGradientColor)
        if Saved.DropDown.darkModeGradientColor != Defaults.DropDown.darkModeGradientColor:
            ColorPicker.changeButtonColor(Saved.DropDown.darkModeGradientColor, window.dark_mode_gradient_color_picker2)
        window.lightModeGradientColor2.setText(Saved.DropDown.lightModeGradientColor)
        if Saved.DropDown.lightModeGradientColor != Defaults.DropDown.lightModeGradientColor:
            ColorPicker.changeButtonColor(Saved.DropDown.lightModeGradientColor, window.light_mode_gradient_color_picker2)
        window.disabledEffect2.setCurrentIndex(Saved.DropDown.disabled)

        # Menu-General
        window.noSystemDropShadow.setCurrentIndex(Saved.Menu.noSystemDropShadow)
        window.enableImmersiveStyle.setCurrentIndex(Saved.Menu.enableImmersiveStyle)
        window.enableCustomRendering.setCurrentIndex(Saved.Menu.enableCustomRendering)
        window.enableFluentAnimation.setCurrentIndex(Saved.Menu.enableFluentAnimation)
        window.noModernAppBackgroundColor.setCurrentIndex(Saved.Menu.noModernAppBackgroundColor)
        window.colorTreatAsTransparent.setText(Saved.Menu.colorTreatAsTransparent)
        if Saved.Menu.colorTreatAsTransparent != Defaults.Menu.colorTreatAsTransparent:
            ColorPicker.changeButtonColor(Saved.Menu.colorTreatAsTransparent, window.color_treat_as_transparent_color_picker)
        window.colorTreatAsTransparentThreshold.setValue(Saved.Menu.colorTreatAsTransparentThreshold)
        window.effectType3.setCurrentIndex(Saved.Menu.effectType)
        window.cornerType3.setCurrentIndex(Saved.Menu.cornerType)
        window.enableDropShadow3.setCurrentIndex(Saved.Menu.enableDropShadow)
        window.noBorderColor3.setCurrentIndex(Saved.Menu.noBorderColor)
        window.enableThemeColorization3_1.setCurrentIndex(Saved.Menu.enableThemeColorization)
        window.darkModeBorderColor3.setText(Saved.Menu.darkModeBorderColor)
        if Saved.Menu.darkModeBorderColor != Defaults.Menu.darkModeBorderColor:
            ColorPicker.changeButtonColor(Saved.Menu.darkModeBorderColor, window.dark_mode_border_color_picker3)
        window.lightModeBorderColor3.setText(Saved.Menu.lightModeBorderColor)
        if Saved.Menu.lightModeBorderColor != Defaults.Menu.lightModeBorderColor:
            ColorPicker.changeButtonColor(Saved.Menu.lightModeBorderColor, window.light_mode_border_color_picker3)
        window.darkModeGradientColor3.setText(Saved.Menu.darkModeGradientColor)
        if Saved.Menu.darkModeGradientColor != Defaults.Menu.darkModeGradientColor:
            ColorPicker.changeButtonColor(Saved.Menu.darkModeGradientColor, window.dark_mode_gradient_color_picker3)
        window.lightModeGradientColor3.setText(Saved.Menu.lightModeGradientColor)
        if Saved.Menu.lightModeGradientColor != Defaults.Menu.lightModeGradientColor:
            ColorPicker.changeButtonColor(Saved.Menu.lightModeGradientColor, window.light_mode_gradient_color_picker3)
        window.disabledEffect3_1.setCurrentIndex(Saved.Menu.disabled)

        # Menu-Animation
        window.fadeOutTime.setValue(Saved.Menu.Animation.fadeOutTime)
        window.popInTime.setValue(Saved.Menu.Animation.popInTime)
        window.fadeInTime.setValue(Saved.Menu.Animation.fadeInTime)
        window.popInStyle.setCurrentIndex(Saved.Menu.Animation.popInStyle)
        window.startRatio.setValue(Saved.Menu.Animation.startRatio)
        window.enableImmediateInterupting.setCurrentIndex(Saved.Menu.Animation.enableImmediateInterupting)

        # Menu-Hot
        window.darkModeColor1_1.setText(Saved.Menu.Hot.darkModeColor)
        if Saved.Menu.Hot.darkModeColor != Defaults.Menu.Hot.darkModeColor:
            ColorPicker.changeButtonColor(Saved.Menu.Hot.darkModeColor, window.dark_mode_color_picker1_1)
        window.lightModeColor1_1.setText(Saved.Menu.Hot.lightModeColor)
        if Saved.Menu.Hot.lightModeColor != Defaults.Menu.Hot.lightModeColor:
            ColorPicker.changeButtonColor(Saved.Menu.Hot.lightModeColor, window.light_mode_color_picker1_1)
        window.disabledEffect3_2.setCurrentIndex(Saved.Menu.Hot.disabled)
        window.cornerRadius1_1.setValue(Saved.Menu.Hot.cornerRadius)
        window.enableThemeColorization3_2.setCurrentIndex(Saved.Menu.Hot.enableThemeColorization)

        # Menu-Disabled Hot
        window.darkModeColor1_2.setText(Saved.Menu.DisabledHot.darkModeColor)
        if Saved.Menu.DisabledHot.darkModeColor != Defaults.Menu.DisabledHot.darkModeColor:
            ColorPicker.changeButtonColor(Saved.Menu.DisabledHot.darkModeColor, window.dark_mode_color_picker1_2)
        window.lightModeColor1_2.setText(Saved.Menu.DisabledHot.lightModeColor)
        if Saved.Menu.DisabledHot.lightModeColor != Defaults.Menu.DisabledHot.lightModeColor:
            ColorPicker.changeButtonColor(Saved.Menu.DisabledHot.lightModeColor, window.light_mode_color_picker1_2)
        window.disabledEffect3_3.setCurrentIndex(Saved.Menu.DisabledHot.disabled)
        window.cornerRadius1_2.setValue(Saved.Menu.DisabledHot.cornerRadius)
        window.enableThemeColorization3_3.setCurrentIndex(Saved.Menu.DisabledHot.enableThemeColorization)

        # Menu-Focusing
        window.width1_1.setValue(Saved.Menu.Focusing.width)
        window.darkModeColor1_3.setText(Saved.Menu.Focusing.darkModeColor)
        if Saved.Menu.Focusing.darkModeColor != Defaults.Menu.Focusing.darkModeColor:
            ColorPicker.changeButtonColor(Saved.Menu.Focusing.darkModeColor, window.dark_mode_color_picker1_3)
        window.lightModeColor1_3.setText(Saved.Menu.Focusing.lightModeColor)
        if Saved.Menu.Focusing.lightModeColor != Defaults.Menu.Focusing.lightModeColor:
            ColorPicker.changeButtonColor(Saved.Menu.Focusing.lightModeColor, window.light_mode_color_picker1_3)
        window.disabledEffect3_4.setCurrentIndex(Saved.Menu.Focusing.disabled)
        window.cornerRadius1_3.setValue(Saved.Menu.Focusing.cornerRadius)
        window.enableThemeColorization3_4.setCurrentIndex(Saved.Menu.Focusing.enableThemeColorization)

        # Menu-Separator
        window.width1_2.setValue(Saved.Menu.Separator.width)
        window.darkModeColor1_4.setText(Saved.Menu.Separator.darkModeColor)
        if Saved.Menu.Separator.darkModeColor != Defaults.Menu.Separator.darkModeColor:
            ColorPicker.changeButtonColor(Saved.Menu.Separator.darkModeColor, window.dark_mode_color_picker1_4)
        window.lightModeColor1_4.setText(Saved.Menu.Separator.lightModeColor)
        if Saved.Menu.Separator.lightModeColor != Defaults.Menu.Separator.lightModeColor:
            ColorPicker.changeButtonColor(Saved.Menu.Separator.lightModeColor, window.light_mode_color_picker1_4)
        window.disabledEffect3_5.setCurrentIndex(Saved.Menu.Separator.disabled)
        window.cornerRadius1_4.setValue(Saved.Menu.Separator.cornerRadius)
        window.enableThemeColorization3_5.setCurrentIndex(Saved.Menu.Separator.enableThemeColorization)

        # Tooltip
        window.effectType4.setCurrentIndex(Saved.Tooltip.effectType)
        window.cornerType4.setCurrentIndex(Saved.Tooltip.cornerType)
        window.enableDropShadow4.setCurrentIndex(Saved.Tooltip.enableDropShadow)
        window.noBorderColor4.setCurrentIndex(Saved.Tooltip.noBorderColor)
        window.enableThemeColorization4.setCurrentIndex(Saved.Tooltip.enableThemeColorization)
        window.darkModeBorderColor4.setText(Saved.Tooltip.darkModeBorderColor)
        if Saved.Tooltip.darkModeBorderColor != Defaults.Tooltip.darkModeBorderColor:
            ColorPicker.changeButtonColor(Saved.Tooltip.darkModeBorderColor, window.dark_mode_border_color_picker4)
        window.lightModeBorderColor4.setText(Saved.Tooltip.lightModeBorderColor)
        if Saved.Tooltip.lightModeBorderColor != Defaults.Tooltip.lightModeBorderColor:
            ColorPicker.changeButtonColor(Saved.Tooltip.lightModeBorderColor, window.light_mode_border_color_picker4)
        window.darkModeGradientColor4.setText(Saved.Tooltip.darkModeGradientColor)
        if Saved.Tooltip.darkModeGradientColor != Defaults.Tooltip.darkModeGradientColor:
            ColorPicker.changeButtonColor(Saved.Tooltip.darkModeGradientColor, window.dark_mode_gradient_color_picker4)
        window.lightModeGradientColor4.setText(Saved.Tooltip.lightModeGradientColor)
        if Saved.Tooltip.lightModeGradientColor != Defaults.Tooltip.lightModeGradientColor:
            ColorPicker.changeButtonColor(Saved.Tooltip.lightModeGradientColor, window.light_mode_gradient_color_picker4)
        window.disabledEffect4.setCurrentIndex(Saved.Tooltip.disabled)

    class Global:
        effectType: int = rawDefaults[Key._global][Key.effectType]
        cornerType: int = rawDefaults[Key._global][Key.cornerType]
        enableDropShadow: int = rawDefaults[Key._global][Key.enableDropShadow]
        noBorderColor: int = rawDefaults[Key._global][Key.noBorderColor]
        enableThemeColorization: int = rawDefaults[Key._global][Key.enableThemeColorization]
        darkModeBorderColor: str = rawDefaults[Key._global][Key.darkModeBorderColor]
        lightModeBorderColor: str = rawDefaults[Key._global][Key.lightModeBorderColor]
        darkModeGradientColor: str = rawDefaults[Key._global][Key.darkModeGradientColor]
        lightModeGradientColor: str = rawDefaults[Key._global][Key.lightModeGradientColor]
        disabled: int = rawDefaults[Key._global][Key.disabled]

        @staticmethod
        def updateDict():
            rawDefaults[Key._global][Key.effectType] = Saved.Global.effectType
            rawDefaults[Key._global][Key.cornerType] = Saved.Global.cornerType
            rawDefaults[Key._global][Key.enableDropShadow] = Saved.Global.enableDropShadow
            rawDefaults[Key._global][Key.noBorderColor] = Saved.Global.noBorderColor
            rawDefaults[Key._global][Key.enableThemeColorization] = Saved.Global.enableThemeColorization
            rawDefaults[Key._global][Key.darkModeBorderColor] = Saved.Global.darkModeBorderColor
            rawDefaults[Key._global][Key.lightModeBorderColor] = Saved.Global.lightModeBorderColor
            rawDefaults[Key._global][Key.darkModeGradientColor] = Saved.Global.darkModeGradientColor
            rawDefaults[Key._global][Key.lightModeGradientColor] = Saved.Global.lightModeGradientColor
            rawDefaults[Key._global][Key.disabled] = Saved.Global.disabled

    class DropDown:
        effectType: int = rawDefaults[Key.dropdown][Key.effectType]
        cornerType: int = rawDefaults[Key.dropdown][Key.cornerType]
        enableDropShadow: int = rawDefaults[Key.dropdown][Key.enableDropShadow]
        noBorderColor: int = rawDefaults[Key.dropdown][Key.noBorderColor]
        enableThemeColorization: int = rawDefaults[Key.dropdown][Key.enableThemeColorization]
        darkModeBorderColor: str = rawDefaults[Key.dropdown][Key.darkModeBorderColor]
        lightModeBorderColor: str = rawDefaults[Key.dropdown][Key.lightModeBorderColor]
        darkModeGradientColor: str = rawDefaults[Key.dropdown][Key.darkModeGradientColor]
        lightModeGradientColor: str = rawDefaults[Key.dropdown][Key.lightModeGradientColor]
        disabled: int = rawDefaults[Key.dropdown][Key.disabled]

        @staticmethod
        def updateDict():
            rawDefaults[Key.dropdown][Key.effectType] = Saved.DropDown.effectType
            rawDefaults[Key.dropdown][Key.cornerType] = Saved.DropDown.cornerType
            rawDefaults[Key.dropdown][Key.enableDropShadow] = Saved.DropDown.enableDropShadow
            rawDefaults[Key.dropdown][Key.noBorderColor] = Saved.DropDown.noBorderColor
            rawDefaults[Key.dropdown][Key.enableThemeColorization] = Saved.DropDown.enableThemeColorization
            rawDefaults[Key.dropdown][Key.darkModeBorderColor] = Saved.DropDown.darkModeBorderColor
            rawDefaults[Key.dropdown][Key.lightModeBorderColor] = Saved.DropDown.lightModeBorderColor
            rawDefaults[Key.dropdown][Key.darkModeGradientColor] = Saved.DropDown.darkModeGradientColor
            rawDefaults[Key.dropdown][Key.lightModeGradientColor] = Saved.DropDown.lightModeGradientColor
            rawDefaults[Key.dropdown][Key.disabled] = Saved.DropDown.disabled

    class Menu:
        noSystemDropShadow: int = rawDefaults[Key.menu][Key.noSystemDropShadow]
        enableImmersiveStyle: int = rawDefaults[Key.menu][Key.enableImmersiveStyle]
        enableCustomRendering: int = rawDefaults[Key.menu][Key.enableCustomRendering]
        enableFluentAnimation: int = rawDefaults[Key.menu][Key.enableFluentAnimation]
        noModernAppBackgroundColor: int = rawDefaults[Key.menu][Key.noModernAppBackgroundColor]
        colorTreatAsTransparent: str = rawDefaults[Key.menu][Key.colorTreatAsTransparent]
        colorTreatAsTransparentThreshold: int = rawDefaults[Key.menu][Key.colorTreatAsTransparentThreshold]
        effectType: int = rawDefaults[Key.menu][Key.effectType]
        cornerType: int = rawDefaults[Key.menu][Key.cornerType]
        enableDropShadow: int = rawDefaults[Key.menu][Key.enableDropShadow]
        noBorderColor: int = rawDefaults[Key.menu][Key.noBorderColor]
        enableThemeColorization: int = rawDefaults[Key.menu][Key.enableThemeColorization]
        darkModeBorderColor: str = rawDefaults[Key.menu][Key.darkModeBorderColor]
        lightModeBorderColor: str = rawDefaults[Key.menu][Key.lightModeBorderColor]
        darkModeGradientColor: str = rawDefaults[Key.menu][Key.darkModeGradientColor]
        lightModeGradientColor: str = rawDefaults[Key.menu][Key.lightModeGradientColor]
        disabled: int = rawDefaults[Key.menu][Key.disabled]

        @staticmethod
        def updateDict():
            rawDefaults[Key.menu][Key.noSystemDropShadow] = Saved.Menu.noSystemDropShadow
            rawDefaults[Key.menu][Key.enableImmersiveStyle] = Saved.Menu.enableImmersiveStyle
            rawDefaults[Key.menu][Key.enableCustomRendering] = Saved.Menu.enableCustomRendering
            rawDefaults[Key.menu][Key.enableFluentAnimation] = Saved.Menu.enableFluentAnimation
            rawDefaults[Key.menu][Key.noModernAppBackgroundColor] = Saved.Menu.noModernAppBackgroundColor
            rawDefaults[Key.menu][Key.colorTreatAsTransparent] = Saved.Menu.colorTreatAsTransparent
            rawDefaults[Key.menu][Key.colorTreatAsTransparentThreshold] = Saved.Menu.colorTreatAsTransparentThreshold
            rawDefaults[Key.menu][Key.effectType] = Saved.Menu.effectType
            rawDefaults[Key.menu][Key.cornerType] = Saved.Menu.cornerType
            rawDefaults[Key.menu][Key.enableDropShadow] = Saved.Menu.enableDropShadow
            rawDefaults[Key.menu][Key.noBorderColor] = Saved.Menu.noBorderColor
            rawDefaults[Key.menu][Key.enableThemeColorization] = Saved.Menu.enableThemeColorization
            rawDefaults[Key.menu][Key.darkModeBorderColor] = Saved.Menu.darkModeBorderColor
            rawDefaults[Key.menu][Key.lightModeBorderColor] = Saved.Menu.lightModeBorderColor
            rawDefaults[Key.menu][Key.darkModeGradientColor] = Saved.Menu.darkModeGradientColor
            rawDefaults[Key.menu][Key.lightModeGradientColor] = Saved.Menu.lightModeGradientColor
            rawDefaults[Key.menu][Key.disabled] = Saved.Menu.disabled

        class Animation:
            fadeOutTime: int = rawDefaults[Key.menu][Key.animation][Key.fadeOutTime]
            popInTime: int = rawDefaults[Key.menu][Key.animation][Key.popInTime]
            fadeInTime: int = rawDefaults[Key.menu][Key.animation][Key.fadeInTime]
            popInStyle: int = rawDefaults[Key.menu][Key.animation][Key.popInStyle]
            startRatio: int = rawDefaults[Key.menu][Key.animation][Key.startRatio]
            enableImmediateInterupting: int = rawDefaults[Key.menu][Key.animation][Key.enableImmediateInterupting]

            @staticmethod
            def updateDict():
                rawDefaults[Key.menu][Key.animation][Key.fadeOutTime] = Saved.Menu.Animation.fadeOutTime
                rawDefaults[Key.menu][Key.animation][Key.popInTime] = Saved.Menu.Animation.popInTime
                rawDefaults[Key.menu][Key.animation][Key.fadeInTime] = Saved.Menu.Animation.fadeInTime
                rawDefaults[Key.menu][Key.animation][Key.popInStyle] = Saved.Menu.Animation.popInStyle
                rawDefaults[Key.menu][Key.animation][Key.startRatio] = Saved.Menu.Animation.startRatio
                rawDefaults[Key.menu][Key.animation][Key.enableImmediateInterupting] = Saved.Menu.Animation.enableImmediateInterupting

        class DisabledHot:
            cornerRadius: int = rawDefaults[Key.menu][Key.disabledHot][Key.cornerRadius]
            darkModeColor: str = rawDefaults[Key.menu][Key.disabledHot][Key.darkModeColor]
            lightModeColor: str = rawDefaults[Key.menu][Key.disabledHot][Key.lightModeColor]
            enableThemeColorization: int = rawDefaults[Key.menu][Key.disabledHot][Key.enableThemeColorization]
            disabled: int = rawDefaults[Key.menu][Key.disabledHot][Key.disabled]

            @staticmethod
            def updateDict():
                rawDefaults[Key.menu][Key.disabledHot][Key.cornerRadius] = Saved.Menu.DisabledHot.cornerRadius
                rawDefaults[Key.menu][Key.disabledHot][Key.darkModeColor] = Saved.Menu.DisabledHot.darkModeColor
                rawDefaults[Key.menu][Key.disabledHot][Key.lightModeColor] = Saved.Menu.DisabledHot.lightModeColor
                rawDefaults[Key.menu][Key.disabledHot][Key.enableThemeColorization] = Saved.Menu.DisabledHot.enableThemeColorization
                rawDefaults[Key.menu][Key.disabledHot][Key.disabled] = Saved.Menu.DisabledHot.disabled

        class Focusing:
            width: int = rawDefaults[Key.menu][Key.focusing][Key.width]
            cornerRadius: int = rawDefaults[Key.menu][Key.focusing][Key.cornerRadius]
            darkModeColor: str = rawDefaults[Key.menu][Key.focusing][Key.darkModeColor]
            lightModeColor: str = rawDefaults[Key.menu][Key.focusing][Key.lightModeColor]
            enableThemeColorization: int = rawDefaults[Key.menu][Key.focusing][Key.enableThemeColorization]
            disabled: int = rawDefaults[Key.menu][Key.focusing][Key.disabled]

            @staticmethod
            def updateDict():
                rawDefaults[Key.menu][Key.focusing][Key.width] = Saved.Menu.Focusing.width
                rawDefaults[Key.menu][Key.focusing][Key.cornerRadius] = Saved.Menu.Focusing.cornerRadius
                rawDefaults[Key.menu][Key.focusing][Key.darkModeColor] = Saved.Menu.Focusing.darkModeColor
                rawDefaults[Key.menu][Key.focusing][Key.lightModeColor] = Saved.Menu.Focusing.lightModeColor
                rawDefaults[Key.menu][Key.focusing][Key.enableThemeColorization] = Saved.Menu.Focusing.enableThemeColorization
                rawDefaults[Key.menu][Key.focusing][Key.disabled] = Saved.Menu.Focusing.disabled

        class Hot:
            cornerRadius: int = rawDefaults[Key.menu][Key.hot][Key.cornerRadius]
            darkModeColor: str = rawDefaults[Key.menu][Key.hot][Key.darkModeColor]
            lightModeColor: str = rawDefaults[Key.menu][Key.hot][Key.lightModeColor]
            enableThemeColorization: int = rawDefaults[Key.menu][Key.hot][Key.enableThemeColorization]
            disabled: int = rawDefaults[Key.menu][Key.hot][Key.disabled]

            @staticmethod
            def updateDict():
                rawDefaults[Key.menu][Key.hot][Key.cornerRadius] = Saved.Menu.Hot.cornerRadius
                rawDefaults[Key.menu][Key.hot][Key.darkModeColor] = Saved.Menu.Hot.darkModeColor
                rawDefaults[Key.menu][Key.hot][Key.lightModeColor] = Saved.Menu.Hot.lightModeColor
                rawDefaults[Key.menu][Key.hot][Key.enableThemeColorization] = Saved.Menu.Hot.enableThemeColorization
                rawDefaults[Key.menu][Key.hot][Key.disabled] = Saved.Menu.Hot.disabled

        class Separator:
            width: int = rawDefaults[Key.menu][Key.separator][Key.width]
            cornerRadius: int = rawDefaults[Key.menu][Key.separator][Key.cornerRadius]
            darkModeColor: str = rawDefaults[Key.menu][Key.separator][Key.darkModeColor]
            lightModeColor: str = rawDefaults[Key.menu][Key.separator][Key.lightModeColor]
            enableThemeColorization: int = rawDefaults[Key.menu][Key.separator][Key.enableThemeColorization]
            disabled: int = rawDefaults[Key.menu][Key.separator][Key.disabled]

            @staticmethod
            def updateDict():
                rawDefaults[Key.menu][Key.separator][Key.width] = Saved.Menu.Separator.width
                rawDefaults[Key.menu][Key.separator][Key.cornerRadius] = Saved.Menu.Separator.cornerRadius
                rawDefaults[Key.menu][Key.separator][Key.darkModeColor] = Saved.Menu.Separator.darkModeColor
                rawDefaults[Key.menu][Key.separator][Key.lightModeColor] = Saved.Menu.Separator.lightModeColor
                rawDefaults[Key.menu][Key.separator][Key.enableThemeColorization] = Saved.Menu.Separator.enableThemeColorization
                rawDefaults[Key.menu][Key.separator][Key.disabled] = Saved.Menu.Separator.disabled

    class Tooltip:
        effectType: int = rawDefaults[Key.tooltip][Key.effectType]
        cornerType: int = rawDefaults[Key.tooltip][Key.cornerType]
        enableDropShadow: int = rawDefaults[Key.tooltip][Key.enableDropShadow]
        noBorderColor: int = rawDefaults[Key.tooltip][Key.noBorderColor]
        enableThemeColorization: int = rawDefaults[Key.tooltip][Key.enableThemeColorization]
        darkModeBorderColor: str = rawDefaults[Key.tooltip][Key.darkModeBorderColor]
        lightModeBorderColor: str = rawDefaults[Key.tooltip][Key.lightModeBorderColor]
        darkModeGradientColor: str = rawDefaults[Key.tooltip][Key.darkModeGradientColor]
        lightModeGradientColor: str = rawDefaults[Key.tooltip][Key.lightModeGradientColor]
        disabled: int = rawDefaults[Key.tooltip][Key.disabled]

        @staticmethod
        def updateDict():
            rawDefaults[Key.tooltip][Key.effectType] = Saved.Tooltip.effectType
            rawDefaults[Key.tooltip][Key.cornerType] = Saved.Tooltip.cornerType
            rawDefaults[Key.tooltip][Key.enableDropShadow] = Saved.Tooltip.enableDropShadow
            rawDefaults[Key.tooltip][Key.noBorderColor] = Saved.Tooltip.noBorderColor
            rawDefaults[Key.tooltip][Key.enableThemeColorization] = Saved.Tooltip.enableThemeColorization
            rawDefaults[Key.tooltip][Key.darkModeBorderColor] = Saved.Tooltip.darkModeBorderColor
            rawDefaults[Key.tooltip][Key.lightModeBorderColor] = Saved.Tooltip.lightModeBorderColor
            rawDefaults[Key.tooltip][Key.darkModeGradientColor] = Saved.Tooltip.darkModeGradientColor
            rawDefaults[Key.tooltip][Key.lightModeGradientColor] = Saved.Tooltip.lightModeGradientColor
            rawDefaults[Key.tooltip][Key.disabled] = Saved.Tooltip.disabled

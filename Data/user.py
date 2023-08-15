# Library Imports
from __future__ import annotations
from typing import TYPE_CHECKING
import json

if TYPE_CHECKING:
    from main import Main


rawDefaults: dict = dict(json.load(open("user_settings.json", "r")))


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
        with open("user_Settings.json", "w") as json_file:
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
        window.lightModeBorderColor1.setText(Saved.Global.lightModeBorderColor)
        window.darkModeGradientColor1.setText(Saved.Global.darkModeGradientColor)
        window.lightModeGradientColor1.setText(Saved.Global.lightModeGradientColor)
        window.disabledEffect1.setCurrentIndex(Saved.Global.disabled)

        # DropDown
        window.effectType2.setCurrentIndex(Saved.DropDown.effectType)
        window.cornerType2.setCurrentIndex(Saved.DropDown.cornerType)
        window.enableDropShadow2.setCurrentIndex(Saved.DropDown.enableDropShadow)
        window.noBorderColor2.setCurrentIndex(Saved.DropDown.noBorderColor)
        window.enableThemeColorization2.setCurrentIndex(Saved.DropDown.enableThemeColorization)
        window.darkModeBorderColor2.setText(Saved.DropDown.darkModeBorderColor)
        window.lightModeBorderColor2.setText(Saved.DropDown.lightModeBorderColor)
        window.darkModeGradientColor2.setText(Saved.DropDown.darkModeGradientColor)
        window.lightModeGradientColor2.setText(Saved.DropDown.lightModeGradientColor)
        window.disabledEffect2.setCurrentIndex(Saved.DropDown.disabled)

        # Menu-General
        window.noSystemDropShadow.setCurrentIndex(Saved.Menu.noSystemDropShadow)
        window.enableImmersiveStyle.setCurrentIndex(Saved.Menu.enableImmersiveStyle)
        window.enableCustomRendering.setCurrentIndex(Saved.Menu.enableCustomRendering)
        window.enableFluentAnimation.setCurrentIndex(Saved.Menu.enableFluentAnimation)
        window.effectType3.setCurrentIndex(Saved.Menu.effectType)
        window.cornerType3.setCurrentIndex(Saved.Menu.cornerType)
        window.enableDropShadow3.setCurrentIndex(Saved.Menu.enableDropShadow)
        window.noBorderColor3.setCurrentIndex(Saved.Menu.noBorderColor)
        window.enableThemeColorization3_1.setCurrentIndex(Saved.Menu.enableThemeColorization)
        window.darkModeBorderColor3.setText(Saved.Menu.darkModeBorderColor)
        window.lightModeBorderColor3.setText(Saved.Menu.lightModeBorderColor)
        window.darkModeGradientColor3.setText(Saved.Menu.darkModeGradientColor)
        window.lightModeGradientColor3.setText(Saved.Menu.lightModeGradientColor)
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
        window.lightModeColor1_1.setText(Saved.Menu.Hot.lightModeColor)
        window.disabledEffect3_2.setCurrentIndex(Saved.Menu.Hot.disabled)
        window.cornerRadius1_1.setValue(Saved.Menu.Hot.cornerRadius)
        window.enableThemeColorization3_2.setCurrentIndex(Saved.Menu.Hot.enableThemeColorization)

        # Menu-Disabled Hot
        window.darkModeColor1_2.setText(Saved.Menu.DisabledHot.darkModeColor)
        window.lightModeColor1_2.setText(Saved.Menu.DisabledHot.lightModeColor)
        window.disabledEffect3_3.setCurrentIndex(Saved.Menu.DisabledHot.disabled)
        window.cornerRadius1_2.setValue(Saved.Menu.DisabledHot.cornerRadius)
        window.enableThemeColorization3_3.setCurrentIndex(Saved.Menu.DisabledHot.enableThemeColorization)

        # Menu-Focusing
        window.width1_1.setValue(Saved.Menu.Focusing.width)
        window.darkModeColor1_3.setText(Saved.Menu.Focusing.darkModeColor)
        window.lightModeColor1_3.setText(Saved.Menu.Focusing.lightModeColor)
        window.disabledEffect3_4.setCurrentIndex(Saved.Menu.Focusing.disabled)
        window.cornerRadius1_3.setValue(Saved.Menu.Focusing.cornerRadius)
        window.enableThemeColorization3_4.setCurrentIndex(Saved.Menu.Focusing.enableThemeColorization)

        # Menu-Separator
        window.width1_2.setValue(Saved.Menu.Separator.width)
        window.darkModeColor1_4.setText(Saved.Menu.Separator.darkModeColor)
        window.lightModeColor1_4.setText(Saved.Menu.Separator.lightModeColor)
        window.disabledEffect3_5.setCurrentIndex(Saved.Menu.Separator.disabled)
        window.cornerRadius1_4.setValue(Saved.Menu.Separator.cornerRadius)
        window.enableThemeColorization3_5.setCurrentIndex(Saved.Menu.Separator.enableThemeColorization)

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

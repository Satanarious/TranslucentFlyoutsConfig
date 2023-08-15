# Library Imports
import json

rawDefaults: dict = dict(json.load(open("defaults.json", "r")))


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
class Defaults:
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

        class Animation:
            fadeOutTime: int = rawDefaults[Key.menu][Key.animation][Key.fadeOutTime]
            popInTime: int = rawDefaults[Key.menu][Key.animation][Key.popInTime]
            fadeInTime: int = rawDefaults[Key.menu][Key.animation][Key.fadeInTime]
            popInStyle: int = rawDefaults[Key.menu][Key.animation][Key.popInStyle]
            startRatio: int = rawDefaults[Key.menu][Key.animation][Key.startRatio]
            enableImmediateInterupting: int = rawDefaults[Key.menu][Key.animation][Key.enableImmediateInterupting]

        class DisabledHot:
            cornerRadius: int = rawDefaults[Key.menu][Key.disabledHot][Key.cornerRadius]
            darkModeColor: str = rawDefaults[Key.menu][Key.disabledHot][Key.darkModeColor]
            lightModeColor: str = rawDefaults[Key.menu][Key.disabledHot][Key.lightModeColor]
            enableThemeColorization: int = rawDefaults[Key.menu][Key.disabledHot][Key.enableThemeColorization]
            disabled: int = rawDefaults[Key.menu][Key.disabledHot][Key.disabled]

        class Focusing:
            width: int = rawDefaults[Key.menu][Key.focusing][Key.width]
            cornerRadius: int = rawDefaults[Key.menu][Key.focusing][Key.cornerRadius]
            darkModeColor: str = rawDefaults[Key.menu][Key.focusing][Key.darkModeColor]
            lightModeColor: str = rawDefaults[Key.menu][Key.focusing][Key.lightModeColor]
            enableThemeColorization: int = rawDefaults[Key.menu][Key.focusing][Key.enableThemeColorization]
            disabled: int = rawDefaults[Key.menu][Key.focusing][Key.disabled]

        class Hot:
            cornerRadius: int = rawDefaults[Key.menu][Key.hot][Key.cornerRadius]
            darkModeColor: str = rawDefaults[Key.menu][Key.hot][Key.darkModeColor]
            lightModeColor: str = rawDefaults[Key.menu][Key.hot][Key.lightModeColor]
            enableThemeColorization: int = rawDefaults[Key.menu][Key.hot][Key.enableThemeColorization]
            disabled: int = rawDefaults[Key.menu][Key.hot][Key.disabled]

        class Separator:
            width: int = rawDefaults[Key.menu][Key.separator][Key.width]
            cornerRadius: int = rawDefaults[Key.menu][Key.separator][Key.cornerRadius]
            darkModeColor: str = rawDefaults[Key.menu][Key.separator][Key.darkModeColor]
            lightModeColor: str = rawDefaults[Key.menu][Key.separator][Key.lightModeColor]
            enableThemeColorization: int = rawDefaults[Key.menu][Key.separator][Key.enableThemeColorization]
            disabled: int = rawDefaults[Key.menu][Key.separator][Key.disabled]

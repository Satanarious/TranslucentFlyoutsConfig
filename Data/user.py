# Library Imports
import json


rawDefaults: dict = dict(json.load(open("user_settings.json", "r")))


class ClassVar:
    @staticmethod
    def joinVars(*vars: str) -> str:
        return "Saved." + ".".join(vars)

    general: str = "General"
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
    general: str = "General"
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

    class General:
        effectType: int = rawDefaults[Key.general][Key.effectType]
        cornerType: int = rawDefaults[Key.general][Key.cornerType]
        enableDropShadow: int = rawDefaults[Key.general][Key.enableDropShadow]
        noBorderColor: int = rawDefaults[Key.general][Key.noBorderColor]
        enableThemeColorization: int = rawDefaults[Key.general][Key.enableThemeColorization]
        darkModeBorderColor: str = rawDefaults[Key.general][Key.darkModeBorderColor]
        lightModeBorderColor: str = rawDefaults[Key.general][Key.lightModeBorderColor]
        darkModeGradientColor: str = rawDefaults[Key.general][Key.darkModeGradientColor]
        lightModeGradientColor: str = rawDefaults[Key.general][Key.lightModeGradientColor]
        disabled: int = rawDefaults[Key.general][Key.disabled]

        @staticmethod
        def updateDict():
            rawDefaults[Key.general][Key.effectType] = Saved.General.effectType
            rawDefaults[Key.general][Key.cornerType] = Saved.General.cornerType
            rawDefaults[Key.general][Key.enableDropShadow] = Saved.General.enableDropShadow
            rawDefaults[Key.general][Key.noBorderColor] = Saved.General.noBorderColor
            rawDefaults[Key.general][Key.enableThemeColorization] = Saved.General.enableThemeColorization
            rawDefaults[Key.general][Key.darkModeBorderColor] = Saved.General.darkModeBorderColor
            rawDefaults[Key.general][Key.lightModeBorderColor] = Saved.General.lightModeBorderColor
            rawDefaults[Key.general][Key.darkModeGradientColor] = Saved.General.darkModeGradientColor
            rawDefaults[Key.general][Key.lightModeGradientColor] = Saved.General.lightModeGradientColor
            rawDefaults[Key.general][Key.disabled] = Saved.General.disabled

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

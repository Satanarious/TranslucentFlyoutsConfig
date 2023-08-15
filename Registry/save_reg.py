# Relative Imports
from Data.user import Saved
from Data.paths import Path
from Data.defaults import Defaults
from Data.enums import Settings
from Registry.edit_settings import EditSettings
from Registry.reg_edit import EditRegistry


class Apply:
    class Global:
        @staticmethod
        def apply() -> bool:
            """
            Method to:
            - Remove a value if it is being set to its default value
            - Update the value
            """
            keyPath = Path.RegPaths.Global
            try:
                if Saved.Global.effectType == Defaults.Global.effectType:
                    EditRegistry.removeValue(
                        keyPath=keyPath,
                        valueName=Path.RegKeys.EffectType,
                    )
                else:
                    EditSettings.changeEffectType(
                        keyPath=keyPath,
                        effectType=Saved.Global.effectType,
                    )
                if Saved.Global.cornerType == Defaults.Global.cornerType:
                    EditRegistry.removeValue(
                        keyPath=keyPath,
                        valueName=Path.RegKeys.CornerType,
                    )
                else:
                    EditSettings.changeCornerType(
                        keyPath=keyPath,
                        cornerType=Saved.Global.cornerType,
                    )
                if Saved.Global.enableDropShadow == Defaults.Global.enableDropShadow:
                    EditRegistry.removeValue(
                        keyPath=keyPath,
                        valueName=Path.RegKeys.EnableDropShadow,
                    )
                else:
                    EditSettings.changeEnableDropShadow(
                        keyPath=keyPath,
                        isEnabled=Saved.Global.enableDropShadow,
                    )
                if Saved.Global.noBorderColor == Defaults.Global.noBorderColor:
                    EditRegistry.removeValue(
                        keyPath=keyPath,
                        valueName=Path.RegKeys.NoBorderColor,
                    )
                else:
                    EditSettings.changeNoBorderColor(
                        keyPath=keyPath,
                        isEnabled=Saved.Global.noBorderColor,
                    )
                if Saved.Global.enableThemeColorization == Defaults.Global.enableThemeColorization:
                    EditRegistry.removeValue(
                        keyPath=keyPath,
                        valueName=Path.RegKeys.EnableThemeColorization,
                    )
                else:
                    EditSettings.changeEnableThemeColorization(
                        keyPath=keyPath,
                        isEnabled=Saved.Global.enableThemeColorization,
                    )
                if Saved.Global.darkModeBorderColor == Defaults.Global.darkModeBorderColor:
                    EditRegistry.removeValue(
                        keyPath=keyPath,
                        valueName=Path.RegKeys.DarkModeBorderColor,
                    )
                else:
                    EditSettings.changeDarkModeBorderColor(
                        keyPath=keyPath,
                        color=Saved.Global.darkModeBorderColor,
                    )
                if Saved.Global.lightModeBorderColor == Defaults.Global.lightModeBorderColor:
                    EditRegistry.removeValue(
                        keyPath=keyPath,
                        valueName=Path.RegKeys.LightModeBorderColor,
                    )
                else:
                    EditSettings.changeLightModeBorderColor(
                        keyPath=keyPath,
                        color=Saved.Global.lightModeBorderColor,
                    )
                if Saved.Global.darkModeGradientColor == Defaults.Global.darkModeGradientColor:
                    EditRegistry.removeValue(
                        keyPath=keyPath,
                        valueName=Path.RegKeys.DarkModeGradientColor,
                    )
                else:
                    EditSettings.changeDarkModeGradientColor(
                        keyPath=keyPath,
                        color=Saved.Global.darkModeGradientColor,
                    )
                if Saved.Global.lightModeGradientColor == Defaults.Global.lightModeGradientColor:
                    EditRegistry.removeValue(
                        keyPath=keyPath,
                        valueName=Path.RegKeys.LightModeGradientColor,
                    )
                else:
                    EditSettings.changeLightModeGradientColor(
                        keyPath=keyPath,
                        color=Saved.Global.lightModeGradientColor,
                    )
                if Saved.Global.disabled == Defaults.Global.disabled:
                    EditRegistry.removeValue(
                        keyPath=keyPath,
                        valueName=Path.RegKeys.Disabled,
                    )
                else:
                    EditSettings.changeDisabled(
                        keyPath=keyPath,
                        isDisabled=Saved.Global.disabled,
                    )
            except:
                return False
            else:
                return True

    class DropDown:
        @staticmethod
        def apply() -> bool:
            """
            Method to:
            - Remove a value if it is being set to its default value
            - Update the value
            """
            keyPath = Path.RegPaths.DropDown
            try:
                if Saved.DropDown.effectType == Settings.EffectType.UseGlobalSetting:
                    EditRegistry.removeValue(
                        keyPath=keyPath,
                        valueName=Path.RegKeys.EffectType,
                    )
                else:
                    EditSettings.changeEffectType(
                        keyPath=keyPath,
                        effectType=Saved.DropDown.effectType,
                    )
                if Saved.DropDown.cornerType == Defaults.DropDown.cornerType:
                    EditRegistry.removeValue(
                        keyPath=keyPath,
                        valueName=Path.RegKeys.CornerType,
                    )
                else:
                    EditSettings.changeCornerType(
                        keyPath=keyPath,
                        cornerType=Saved.DropDown.cornerType,
                    )
                if Saved.DropDown.enableDropShadow == Settings.EnableDropShadow.UseGlobalSetting:
                    EditRegistry.removeValue(
                        keyPath=keyPath,
                        valueName=Path.RegKeys.EnableDropShadow,
                    )
                else:
                    EditSettings.changeEnableDropShadow(
                        keyPath=keyPath,
                        isEnabled=Saved.DropDown.enableDropShadow,
                    )
                if Saved.DropDown.noBorderColor == Settings.NoBorderColor.UseGlobalSetting:
                    EditRegistry.removeValue(
                        keyPath=keyPath,
                        valueName=Path.RegKeys.NoBorderColor,
                    )
                else:
                    EditSettings.changeNoBorderColor(
                        keyPath=keyPath,
                        isEnabled=Saved.DropDown.noBorderColor,
                    )
                if Saved.DropDown.enableThemeColorization == Settings.EnableThemeColorization.UseGlobalSetting:
                    EditRegistry.removeValue(
                        keyPath=keyPath,
                        valueName=Path.RegKeys.EnableThemeColorization,
                    )
                else:
                    EditSettings.changeEnableThemeColorization(
                        keyPath=keyPath,
                        isEnabled=Saved.DropDown.enableThemeColorization,
                    )
                if Saved.DropDown.darkModeBorderColor == Defaults.DropDown.darkModeBorderColor:
                    EditRegistry.removeValue(
                        keyPath=keyPath,
                        valueName=Path.RegKeys.DarkModeBorderColor,
                    )
                else:
                    EditSettings.changeDarkModeBorderColor(
                        keyPath=keyPath,
                        color=Saved.DropDown.darkModeBorderColor,
                    )
                if Saved.DropDown.lightModeBorderColor == Defaults.DropDown.lightModeBorderColor:
                    EditRegistry.removeValue(
                        keyPath=keyPath,
                        valueName=Path.RegKeys.LightModeBorderColor,
                    )
                else:
                    EditSettings.changeLightModeBorderColor(
                        keyPath=keyPath,
                        color=Saved.DropDown.lightModeBorderColor,
                    )
                if Saved.DropDown.darkModeGradientColor == Defaults.DropDown.darkModeGradientColor:
                    EditRegistry.removeValue(
                        keyPath=keyPath,
                        valueName=Path.RegKeys.DarkModeGradientColor,
                    )
                else:
                    EditSettings.changeDarkModeGradientColor(
                        keyPath=keyPath,
                        color=Saved.DropDown.darkModeGradientColor,
                    )
                if Saved.DropDown.lightModeGradientColor == Defaults.DropDown.lightModeGradientColor:
                    EditRegistry.removeValue(
                        keyPath=keyPath,
                        valueName=Path.RegKeys.LightModeGradientColor,
                    )
                else:
                    EditSettings.changeLightModeGradientColor(
                        keyPath=keyPath,
                        color=Saved.DropDown.lightModeGradientColor,
                    )
                if Saved.DropDown.disabled == Settings.Disabled.UseGlobalSetting:
                    EditRegistry.removeValue(
                        keyPath=keyPath,
                        valueName=Path.RegKeys.Disabled,
                    )
                else:
                    EditSettings.changeDisabled(
                        keyPath=keyPath,
                        isDisabled=Saved.DropDown.disabled,
                    )
            except:
                return False
            else:
                return True

    class Menu:
        @staticmethod
        def apply() -> bool:
            """
            Method to:
            - Remove a value if it is being set to its default value
            - Update the value
            """
            keyPath = Path.RegPaths.Menu
            try:
                if Saved.Menu.noSystemDropShadow == Defaults.Menu.noSystemDropShadow:
                    EditRegistry.removeValue(
                        keyPath=keyPath,
                        valueName=Path.RegKeys.NoSystemDropShadow,
                    )
                else:
                    EditSettings.changeEffectType(
                        keyPath=keyPath,
                        effectType=Saved.Menu.noSystemDropShadow,
                    )
                if Saved.Menu.enableImmersiveStyle == Defaults.Menu.enableImmersiveStyle:
                    EditRegistry.removeValue(
                        keyPath=keyPath,
                        valueName=Path.RegKeys.EnableImmersiveStyle,
                    )
                else:
                    EditSettings.changeEffectType(
                        keyPath=keyPath,
                        effectType=Saved.Menu.enableImmersiveStyle,
                    )
                if Saved.Menu.enableCustomRendering == Defaults.Menu.enableCustomRendering:
                    EditRegistry.removeValue(
                        keyPath=keyPath,
                        valueName=Path.RegKeys.EnableCustomRendering,
                    )
                else:
                    EditSettings.changeEffectType(
                        keyPath=keyPath,
                        effectType=Saved.Menu.enableCustomRendering,
                    )
                if Saved.Menu.enableFluentAnimation == Defaults.Menu.enableFluentAnimation:
                    EditRegistry.removeValue(
                        keyPath=keyPath,
                        valueName=Path.RegKeys.EnableFluentAnimation,
                    )
                else:
                    EditSettings.changeEffectType(
                        keyPath=keyPath,
                        effectType=Saved.Menu.enableFluentAnimation,
                    )
                if Saved.Menu.effectType == Settings.EffectType.UseGlobalSetting:
                    EditRegistry.removeValue(
                        keyPath=keyPath,
                        valueName=Path.RegKeys.EffectType,
                    )
                else:
                    EditSettings.changeEffectType(
                        keyPath=keyPath,
                        effectType=Saved.Menu.effectType,
                    )
                if Saved.Menu.cornerType == Settings.CornerType.UseGlobalSetting:
                    EditRegistry.removeValue(
                        keyPath=keyPath,
                        valueName=Path.RegKeys.CornerType,
                    )
                else:
                    EditSettings.changeCornerType(
                        keyPath=keyPath,
                        cornerType=Saved.Menu.cornerType,
                    )
                if Saved.Menu.enableDropShadow == Settings.EnableDropShadow.UseGlobalSetting:
                    EditRegistry.removeValue(
                        keyPath=keyPath,
                        valueName=Path.RegKeys.EnableDropShadow,
                    )
                else:
                    EditSettings.changeEnableDropShadow(
                        keyPath=keyPath,
                        isEnabled=Saved.Menu.enableDropShadow,
                    )
                if Saved.Menu.noBorderColor == Settings.NoBorderColor.UseGlobalSetting:
                    EditRegistry.removeValue(
                        keyPath=keyPath,
                        valueName=Path.RegKeys.NoBorderColor,
                    )
                else:
                    EditSettings.changeNoBorderColor(
                        keyPath=keyPath,
                        isEnabled=Saved.Menu.noBorderColor,
                    )
                if Saved.Menu.enableThemeColorization == Settings.EnableThemeColorization.UseGlobalSetting:
                    EditRegistry.removeValue(
                        keyPath=keyPath,
                        valueName=Path.RegKeys.EnableThemeColorization,
                    )
                else:
                    EditSettings.changeEnableThemeColorization(
                        keyPath=keyPath,
                        isEnabled=Saved.Menu.enableThemeColorization,
                    )
                if Saved.Menu.darkModeBorderColor == Defaults.Menu.darkModeBorderColor:
                    EditRegistry.removeValue(
                        keyPath=keyPath,
                        valueName=Path.RegKeys.DarkModeBorderColor,
                    )
                else:
                    EditSettings.changeDarkModeBorderColor(
                        keyPath=keyPath,
                        color=Saved.Menu.darkModeBorderColor,
                    )
                if Saved.Menu.lightModeBorderColor == Defaults.Menu.lightModeBorderColor:
                    EditRegistry.removeValue(
                        keyPath=keyPath,
                        valueName=Path.RegKeys.LightModeBorderColor,
                    )
                else:
                    EditSettings.changeLightModeBorderColor(
                        keyPath=keyPath,
                        color=Saved.Menu.lightModeBorderColor,
                    )
                if Saved.Menu.darkModeGradientColor == Defaults.Menu.darkModeGradientColor:
                    EditRegistry.removeValue(keyPath=keyPath, valueName=Path.RegKeys.DarkModeGradientColor)
                else:
                    EditSettings.changeDarkModeGradientColor(
                        keyPath=keyPath,
                        color=Saved.Menu.darkModeGradientColor,
                    )
                if Saved.Menu.lightModeGradientColor == Defaults.Menu.lightModeGradientColor:
                    EditRegistry.removeValue(
                        keyPath=keyPath,
                        valueName=Path.RegKeys.LightModeGradientColor,
                    )
                else:
                    EditSettings.changeLightModeGradientColor(
                        keyPath=keyPath,
                        color=Saved.Menu.lightModeGradientColor,
                    )
                if Saved.Menu.disabled == Settings.Disabled.UseGlobalSetting:
                    EditRegistry.removeValue(
                        keyPath=keyPath,
                        valueName=Path.RegKeys.Disabled,
                    )
                else:
                    EditSettings.changeDisabled(
                        keyPath=keyPath,
                        isDisabled=Saved.Menu.disabled,
                    )
            except:
                return False
            else:
                return True

        class Animation:
            @staticmethod
            def apply() -> bool:
                """
                Method to:
                - Remove a value if it is being set to its default value
                - Update the value
                """
                keyPath = Path.RegPaths.Menu + Path.RegPaths.Animation
                try:
                    if Saved.Menu.Animation.fadeOutTime == Defaults.Menu.Animation.fadeOutTime:
                        EditRegistry.removeValue(
                            keyPath=keyPath,
                            valueName=Path.RegKeys.FadeOutTime,
                        )
                    else:
                        EditSettings.changeFadeOutTime(
                            keyPath=keyPath,
                            time=Saved.Menu.Animation.fadeOutTime,
                        )
                    if Saved.Menu.Animation.popInTime == Defaults.Menu.Animation.popInTime:
                        EditRegistry.removeValue(
                            keyPath=keyPath,
                            valueName=Path.RegKeys.PopInTime,
                        )
                    else:
                        EditSettings.changeFadeOutTime(
                            keyPath=keyPath,
                            time=Saved.Menu.Animation.popInTime,
                        )
                    if Saved.Menu.Animation.fadeInTime == Defaults.Menu.Animation.fadeInTime:
                        EditRegistry.removeValue(
                            keyPath=keyPath,
                            valueName=Path.RegKeys.FadeInTime,
                        )
                    else:
                        EditSettings.changeFadeOutTime(
                            keyPath=keyPath,
                            time=Saved.Menu.Animation.fadeInTime,
                        )
                    if Saved.Menu.Animation.popInStyle == Defaults.Menu.Animation.popInStyle:
                        EditRegistry.removeValue(
                            keyPath=keyPath,
                            valueName=Path.RegKeys.PopInStyle,
                        )
                    else:
                        EditSettings.changeFadeOutTime(
                            keyPath=keyPath,
                            time=Saved.Menu.Animation.popInStyle,
                        )
                    if Saved.Menu.Animation.startRatio == Defaults.Menu.Animation.startRatio:
                        EditRegistry.removeValue(
                            keyPath=keyPath,
                            valueName=Path.RegKeys.StartRatio,
                        )
                    else:
                        EditSettings.changeFadeOutTime(
                            keyPath=keyPath,
                            time=Saved.Menu.Animation.startRatio,
                        )
                    if Saved.Menu.Animation.enableImmediateInterupting == Defaults.Menu.Animation.enableImmediateInterupting:
                        EditRegistry.removeValue(
                            keyPath=keyPath,
                            valueName=Path.RegKeys.EnableImmediateInterupting,
                        )
                    else:
                        EditSettings.changeFadeOutTime(
                            keyPath=keyPath,
                            time=Saved.Menu.Animation.enableImmediateInterupting,
                        )
                except:
                    return False
                else:
                    return True

        class Hot:
            @staticmethod
            def apply() -> bool:
                """
                Method to:
                - Remove a value if it is being set to its default value
                - Update the value
                """
                keyPath = Path.RegPaths.Menu + Path.RegPaths.Hot
                try:
                    if Saved.Menu.Hot.darkModeColor == Defaults.Menu.Hot.darkModeColor:
                        EditRegistry.removeValue(
                            keyPath=keyPath,
                            valueName=Path.RegKeys.DarkModeColor,
                        )
                    else:
                        EditSettings.changeDarkModeColor(
                            keyPath=keyPath,
                            color=Saved.Menu.Hot.darkModeColor,
                        )
                    if Saved.Menu.Hot.lightModeColor == Defaults.Menu.Hot.lightModeColor:
                        EditRegistry.removeValue(
                            keyPath=keyPath,
                            valueName=Path.RegKeys.LightModeColor,
                        )
                    else:
                        EditSettings.changeDarkModeColor(
                            keyPath=keyPath,
                            color=Saved.Menu.Hot.lightModeColor,
                        )
                    if Saved.Menu.Hot.disabled == Defaults.Menu.Hot.disabled:
                        EditRegistry.removeValue(
                            keyPath=keyPath,
                            valueName=Path.RegKeys.Disabled,
                        )
                    else:
                        EditSettings.changeDisabled(
                            keyPath=keyPath,
                            isDisabled=Saved.Menu.Hot.disabled,
                        )

                except:
                    return False
                else:
                    return True

        class DisabledHot:
            @staticmethod
            def apply() -> bool:
                """
                Method to:
                - Remove a value if it is being set to its default value
                - Update the value
                """
                keyPath = Path.RegPaths.Menu + Path.RegPaths.DisabledHot
                try:
                    if Saved.Menu.DisabledHot.darkModeColor == Defaults.Menu.DisabledHot.darkModeColor:
                        EditRegistry.removeValue(
                            keyPath=keyPath,
                            valueName=Path.RegKeys.DarkModeColor,
                        )
                    else:
                        EditSettings.changeDarkModeColor(
                            keyPath=keyPath,
                            color=Saved.Menu.DisabledHot.darkModeColor,
                        )
                    if Saved.Menu.DisabledHot.lightModeColor == Defaults.Menu.DisabledHot.lightModeColor:
                        EditRegistry.removeValue(
                            keyPath=keyPath,
                            valueName=Path.RegKeys.LightModeColor,
                        )
                    else:
                        EditSettings.changeDarkModeColor(
                            keyPath=keyPath,
                            color=Saved.Menu.DisabledHot.lightModeColor,
                        )
                    if Saved.Menu.DisabledHot.disabled == Defaults.Menu.DisabledHot.disabled:
                        EditRegistry.removeValue(
                            keyPath=keyPath,
                            valueName=Path.RegKeys.Disabled,
                        )
                    else:
                        EditSettings.changeDisabled(
                            keyPath=keyPath,
                            isDisabled=Saved.Menu.DisabledHot.disabled,
                        )

                except:
                    return False
                else:
                    return True

        class Focusing:
            @staticmethod
            def apply() -> bool:
                """
                Method to:
                - Remove a value if it is being set to its default value
                - Update the value
                """
                keyPath = Path.RegPaths.Menu + Path.RegPaths.Focusing
                try:
                    if Saved.Menu.Focusing.width == Defaults.Menu.Focusing.width:
                        EditRegistry.removeValue(
                            keyPath=keyPath,
                            valueName=Path.RegKeys.Width,
                        )
                    else:
                        EditSettings.changeWidth(
                            keyPath=keyPath,
                            width=Saved.Menu.Focusing.width,
                        )
                    if Saved.Menu.Focusing.darkModeColor == Defaults.Menu.Focusing.darkModeColor:
                        EditRegistry.removeValue(
                            keyPath=keyPath,
                            valueName=Path.RegKeys.DarkModeColor,
                        )
                    else:
                        EditSettings.changeDarkModeColor(
                            keyPath=keyPath,
                            color=Saved.Menu.Focusing.darkModeColor,
                        )
                    if Saved.Menu.Focusing.lightModeColor == Defaults.Menu.Focusing.lightModeColor:
                        EditRegistry.removeValue(
                            keyPath=keyPath,
                            valueName=Path.RegKeys.LightModeColor,
                        )
                    else:
                        EditSettings.changeDarkModeColor(
                            keyPath=keyPath,
                            color=Saved.Menu.Focusing.lightModeColor,
                        )
                    if Saved.Menu.Focusing.disabled == Defaults.Menu.Focusing.disabled:
                        EditRegistry.removeValue(
                            keyPath=keyPath,
                            valueName=Path.RegKeys.Disabled,
                        )
                    else:
                        EditSettings.changeDisabled(
                            keyPath=keyPath,
                            isDisabled=Saved.Menu.Focusing.disabled,
                        )

                except:
                    return False
                else:
                    return True

        class Separator:
            @staticmethod
            def apply() -> bool:
                """
                Method to:
                - Remove a value if it is being set to its default value
                - Update the value
                """
                keyPath = Path.RegPaths.Menu + Path.RegPaths.Separator
                try:
                    if Saved.Menu.Separator.width == Defaults.Menu.Separator.width:
                        EditRegistry.removeValue(
                            keyPath=keyPath,
                            valueName=Path.RegKeys.Width,
                        )
                    else:
                        EditSettings.changeWidth(
                            keyPath=keyPath,
                            width=Saved.Menu.Separator.width,
                        )
                    if Saved.Menu.Separator.darkModeColor == Defaults.Menu.Separator.darkModeColor:
                        EditRegistry.removeValue(
                            keyPath=keyPath,
                            valueName=Path.RegKeys.DarkModeColor,
                        )
                    else:
                        EditSettings.changeDarkModeColor(
                            keyPath=keyPath,
                            color=Saved.Menu.Separator.darkModeColor,
                        )
                    if Saved.Menu.Separator.lightModeColor == Defaults.Menu.Separator.lightModeColor:
                        EditRegistry.removeValue(
                            keyPath=keyPath,
                            valueName=Path.RegKeys.LightModeColor,
                        )
                    else:
                        EditSettings.changeDarkModeColor(
                            keyPath=keyPath,
                            color=Saved.Menu.Separator.lightModeColor,
                        )
                    if Saved.Menu.Separator.disabled == Defaults.Menu.Separator.disabled:
                        EditRegistry.removeValue(
                            keyPath=keyPath,
                            valueName=Path.RegKeys.Disabled,
                        )
                    else:
                        EditSettings.changeDisabled(
                            keyPath=keyPath,
                            isDisabled=Saved.Menu.Separator.disabled,
                        )

                except:
                    return False
                else:
                    return True

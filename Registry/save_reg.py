from Data.defaults import Defaults
from Data.enums import Settings
from Data.paths import Path
from Data.user import Saved
from Registry.edit_settings import EditSettings
from Registry.reg_edit import EditRegistry


class Apply:
    class Global:
        @staticmethod
        def applyDisabledList():
            """
            Method to update the disabled list
            """
            EditSettings.changeDisabledList(
                keyPath=Path.RegPaths.Global, disabledList=Saved.Global.disabledList
            )

        @staticmethod
        def applyBlockList():
            """
            Method to update the block list
            """
            EditSettings.changeBlockList(
                keyPath=Path.RegPaths.Global, blockList=Saved.Global.blockList
            )

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
                if Saved.Global.enableMiniDump == Defaults.Global.enableMiniDump:
                    EditRegistry.removeValue(
                        keyPath=keyPath, valueName=Path.RegKeys.EnableMiniDump
                    )
                else:
                    EditSettings.changeEnableMiniDump(
                        keyPath=keyPath, isEnabled=Saved.Global.enableMiniDump
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
                if (
                    Saved.Global.enableThemeColorization
                    == Defaults.Global.enableThemeColorization
                ):
                    EditRegistry.removeValue(
                        keyPath=keyPath,
                        valueName=Path.RegKeys.EnableThemeColorization,
                    )
                else:
                    EditSettings.changeEnableThemeColorization(
                        keyPath=keyPath,
                        isEnabled=Saved.Global.enableThemeColorization,
                    )
                if (
                    Saved.Global.darkModeThemeColorizationType
                    == Defaults.Global.darkModeThemeColorizationType
                ):
                    EditRegistry.removeValue(
                        keyPath=keyPath,
                        valueName=Path.RegKeys.DarkModeThemeColorizationType,
                    )
                else:
                    EditSettings.changeDarkModeThemeColorizationType(
                        keyPath=keyPath,
                        colorIndex=Saved.Global.darkModeThemeColorizationType,
                    )
                if (
                    Saved.Global.lightModeThemeColorizationType
                    == Defaults.Global.lightModeThemeColorizationType
                ):
                    EditRegistry.removeValue(
                        keyPath=keyPath,
                        valueName=Path.RegKeys.LightModeThemeColorizationType,
                    )
                else:
                    EditSettings.changeLightModeThemeColorizationType(
                        keyPath=keyPath,
                        colorIndex=Saved.Global.lightModeThemeColorizationType,
                    )
                if (
                    Saved.Global.darkModeBorderColor
                    == Defaults.Global.darkModeBorderColor
                ):
                    EditRegistry.removeValue(
                        keyPath=keyPath,
                        valueName=Path.RegKeys.DarkModeBorderColor,
                    )
                else:
                    EditSettings.changeDarkModeBorderColor(
                        keyPath=keyPath,
                        color=Saved.Global.darkModeBorderColor,
                    )
                if (
                    Saved.Global.lightModeBorderColor
                    == Defaults.Global.lightModeBorderColor
                ):
                    EditRegistry.removeValue(
                        keyPath=keyPath,
                        valueName=Path.RegKeys.LightModeBorderColor,
                    )
                else:
                    EditSettings.changeLightModeBorderColor(
                        keyPath=keyPath,
                        color=Saved.Global.lightModeBorderColor,
                    )
                if (
                    Saved.Global.darkModeGradientColor
                    == Defaults.Global.darkModeGradientColor
                ):
                    EditRegistry.removeValue(
                        keyPath=keyPath,
                        valueName=Path.RegKeys.DarkModeGradientColor,
                    )
                else:
                    EditSettings.changeDarkModeGradientColor(
                        keyPath=keyPath,
                        color=Saved.Global.darkModeGradientColor,
                    )
                if (
                    Saved.Global.lightModeGradientColor
                    == Defaults.Global.lightModeGradientColor
                ):
                    EditRegistry.removeValue(
                        keyPath=keyPath,
                        valueName=Path.RegKeys.LightModeGradientColor,
                    )
                else:
                    EditSettings.changeLightModeGradientColor(
                        keyPath=keyPath,
                        color=Saved.Global.lightModeGradientColor,
                    )
                EditSettings.changeDisabledList(
                    keyPath=keyPath,
                    disabledList=Saved.Global.disabledList,
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
            except:  # noqa: E722
                return False
            else:
                return True

    class DropDown:
        @staticmethod
        def applyDisabledList():
            """
            Method to update the disabled list
            """
            EditSettings.changeDisabledList(
                keyPath=Path.RegPaths.DropDown, disabledList=Saved.DropDown.disabledList
            )

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
                if (
                    Saved.DropDown.enableDropShadow
                    == Settings.EnableDropShadow.UseGlobalSetting
                ):
                    EditRegistry.removeValue(
                        keyPath=keyPath,
                        valueName=Path.RegKeys.EnableDropShadow,
                    )
                else:
                    EditSettings.changeEnableDropShadow(
                        keyPath=keyPath,
                        isEnabled=Saved.DropDown.enableDropShadow,
                    )
                if (
                    Saved.DropDown.enableFluentAnimation
                    == Defaults.DropDown.enableFluentAnimation
                ):
                    EditRegistry.removeValue(
                        keyPath=keyPath,
                        valueName=Path.RegKeys.EnableFluentAnimation,
                    )
                else:
                    EditSettings.changeEnableFluentAnimation(
                        keyPath=keyPath,
                        isEnabled=Saved.DropDown.enableFluentAnimation,
                    )
                if (
                    Saved.DropDown.noBorderColor
                    == Settings.NoBorderColor.UseGlobalSetting
                ):
                    EditRegistry.removeValue(
                        keyPath=keyPath,
                        valueName=Path.RegKeys.NoBorderColor,
                    )
                else:
                    EditSettings.changeNoBorderColor(
                        keyPath=keyPath,
                        isEnabled=Saved.DropDown.noBorderColor,
                    )
                if (
                    Saved.DropDown.enableThemeColorization
                    == Settings.EnableThemeColorization.UseGlobalSetting
                ):
                    EditRegistry.removeValue(
                        keyPath=keyPath,
                        valueName=Path.RegKeys.EnableThemeColorization,
                    )
                else:
                    EditSettings.changeEnableThemeColorization(
                        keyPath=keyPath,
                        isEnabled=Saved.DropDown.enableThemeColorization,
                    )
                if (
                    Saved.DropDown.darkModeBorderColor
                    == Defaults.DropDown.darkModeBorderColor
                ):
                    EditRegistry.removeValue(
                        keyPath=keyPath,
                        valueName=Path.RegKeys.DarkModeBorderColor,
                    )
                else:
                    EditSettings.changeDarkModeBorderColor(
                        keyPath=keyPath,
                        color=Saved.DropDown.darkModeBorderColor,
                    )
                if (
                    Saved.DropDown.lightModeBorderColor
                    == Defaults.DropDown.lightModeBorderColor
                ):
                    EditRegistry.removeValue(
                        keyPath=keyPath,
                        valueName=Path.RegKeys.LightModeBorderColor,
                    )
                else:
                    EditSettings.changeLightModeBorderColor(
                        keyPath=keyPath,
                        color=Saved.DropDown.lightModeBorderColor,
                    )
                if (
                    Saved.DropDown.darkModeGradientColor
                    == Defaults.DropDown.darkModeGradientColor
                ):
                    EditRegistry.removeValue(
                        keyPath=keyPath,
                        valueName=Path.RegKeys.DarkModeGradientColor,
                    )
                else:
                    EditSettings.changeDarkModeGradientColor(
                        keyPath=keyPath,
                        color=Saved.DropDown.darkModeGradientColor,
                    )
                if (
                    Saved.DropDown.lightModeGradientColor
                    == Defaults.DropDown.lightModeGradientColor
                ):
                    EditRegistry.removeValue(
                        keyPath=keyPath,
                        valueName=Path.RegKeys.LightModeGradientColor,
                    )
                else:
                    EditSettings.changeLightModeGradientColor(
                        keyPath=keyPath,
                        color=Saved.DropDown.lightModeGradientColor,
                    )
                EditSettings.changeDisabledList(
                    keyPath=keyPath,
                    disabledList=Saved.DropDown.disabledList,
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
            except:  # noqa: E722
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
                keyPath = Path.RegPaths.DropDown + Path.RegPaths.Animation
                try:
                    if (
                        Saved.DropDown.Animation.fadeOutTime
                        == Defaults.DropDown.Animation.fadeOutTime
                    ):
                        EditRegistry.removeValue(
                            keyPath=keyPath,
                            valueName=Path.RegKeys.FadeOutTime,
                        )
                    else:
                        EditSettings.changeFadeOutTime(
                            keyPath=keyPath,
                            time=Saved.DropDown.Animation.fadeOutTime,
                        )
                    if (
                        Saved.DropDown.Animation.popInTime
                        == Defaults.DropDown.Animation.popInTime
                    ):
                        EditRegistry.removeValue(
                            keyPath=keyPath,
                            valueName=Path.RegKeys.PopInTime,
                        )
                    else:
                        EditSettings.changePopInTime(
                            keyPath=keyPath,
                            time=Saved.DropDown.Animation.popInTime,
                        )
                    if (
                        Saved.DropDown.Animation.fadeInTime
                        == Defaults.DropDown.Animation.fadeInTime
                    ):
                        EditRegistry.removeValue(
                            keyPath=keyPath,
                            valueName=Path.RegKeys.FadeInTime,
                        )
                    else:
                        EditSettings.changeFadeInTime(
                            keyPath=keyPath,
                            time=Saved.DropDown.Animation.fadeInTime,
                        )
                    if (
                        Saved.DropDown.Animation.popInStyle
                        == Defaults.DropDown.Animation.popInStyle
                    ):
                        EditRegistry.removeValue(
                            keyPath=keyPath,
                            valueName=Path.RegKeys.PopInStyle,
                        )
                    else:
                        EditSettings.changePopInStyle(
                            keyPath=keyPath,
                            style=Saved.DropDown.Animation.popInStyle,
                        )
                    if (
                        Saved.DropDown.Animation.startRatio
                        == Defaults.DropDown.Animation.startRatio
                    ):
                        EditRegistry.removeValue(
                            keyPath=keyPath,
                            valueName=Path.RegKeys.StartRatio,
                        )
                    else:
                        EditSettings.changeStartRatio(
                            keyPath=keyPath,
                            percent=Saved.DropDown.Animation.startRatio,
                        )
                    if (
                        Saved.DropDown.Animation.enableImmediateInterupting
                        == Defaults.DropDown.Animation.enableImmediateInterupting
                    ):
                        EditRegistry.removeValue(
                            keyPath=keyPath,
                            valueName=Path.RegKeys.EnableImmediateInterupting,
                        )
                    else:
                        EditSettings.changeEnableImmediateInterupting(
                            keyPath=keyPath,
                            isEnabled=Saved.DropDown.Animation.enableImmediateInterupting,
                        )
                except:  # noqa: E722
                    return False
                else:
                    return True

    class Menu:
        @staticmethod
        def applyDisabledList():
            """
            Method to update the disabled list
            """
            EditSettings.changeDisabledList(
                keyPath=Path.RegPaths.Menu, disabledList=Saved.Menu.disabledList
            )

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
                    EditSettings.changeNoSystemDropShadow(
                        keyPath=keyPath,
                        isEnabled=Saved.Menu.noSystemDropShadow,
                    )
                if (
                    Saved.Menu.enableImmersiveStyle
                    == Defaults.Menu.enableImmersiveStyle
                ):
                    EditRegistry.removeValue(
                        keyPath=keyPath,
                        valueName=Path.RegKeys.EnableImmersiveStyle,
                    )
                else:
                    EditSettings.changeEnableImmersiveStyle(
                        keyPath=keyPath,
                        isEnabled=Saved.Menu.enableImmersiveStyle,
                    )
                if (
                    Saved.Menu.enableCustomRendering
                    == Defaults.Menu.enableCustomRendering
                ):
                    EditRegistry.removeValue(
                        keyPath=keyPath,
                        valueName=Path.RegKeys.EnableCustomRendering,
                    )
                else:
                    EditSettings.changeEnableCustomRendering(
                        keyPath=keyPath,
                        isEnabled=Saved.Menu.enableCustomRendering,
                    )
                if (
                    Saved.Menu.enableFluentAnimation
                    == Defaults.Menu.enableFluentAnimation
                ):
                    EditRegistry.removeValue(
                        keyPath=keyPath,
                        valueName=Path.RegKeys.EnableFluentAnimation,
                    )
                else:
                    EditSettings.changeEnableFluentAnimation(
                        keyPath=keyPath,
                        isEnabled=Saved.Menu.enableFluentAnimation,
                    )
                if (
                    Saved.Menu.enableCompatibilityMode
                    == Defaults.Menu.enableCompatibilityMode
                ):
                    EditRegistry.removeValue(
                        keyPath=keyPath,
                        valueName=Path.RegKeys.EnableCompatibilityMode,
                    )
                else:
                    EditSettings.changeEnableCompatibilityMode(
                        keyPath=keyPath,
                        isEnabled=Saved.Menu.enableCompatibilityMode,
                    )
                if (
                    Saved.Menu.noModernAppBackgroundColor
                    == Defaults.Menu.noModernAppBackgroundColor
                ):
                    EditRegistry.removeValue(
                        keyPath=keyPath,
                        valueName=Path.RegKeys.NoModernAppBackgroundColor,
                    )
                else:
                    EditSettings.changeNoModernAppBackgroundColor(
                        keyPath=keyPath,
                        isDisabled=Saved.Menu.noModernAppBackgroundColor,
                    )
                if (
                    Saved.Menu.colorTreatAsTransparent
                    == Defaults.Menu.colorTreatAsTransparent
                ):
                    EditRegistry.removeValue(
                        keyPath=keyPath,
                        valueName=Path.RegKeys.ColorTreatAsTransparent,
                    )
                else:
                    EditSettings.changeColorTreatAsTransparent(
                        keyPath=keyPath,
                        color=Saved.Menu.colorTreatAsTransparent,
                    )
                if (
                    Saved.Menu.colorTreatAsTransparentThreshold
                    == Defaults.Menu.colorTreatAsTransparentThreshold
                ):
                    EditRegistry.removeValue(
                        keyPath=keyPath,
                        valueName=Path.RegKeys.ColorTreatAsTransparentThreshold,
                    )
                else:
                    EditSettings.changeColorTreatAsTransparentThreshold(
                        keyPath=keyPath,
                        threshold=Saved.Menu.colorTreatAsTransparentThreshold,
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
                if (
                    Saved.Menu.enableDropShadow
                    == Settings.EnableDropShadow.UseGlobalSetting
                ):
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
                if (
                    Saved.Menu.enableThemeColorization
                    == Settings.EnableThemeColorization.UseGlobalSetting
                ):
                    EditRegistry.removeValue(
                        keyPath=keyPath,
                        valueName=Path.RegKeys.EnableThemeColorization,
                    )
                else:
                    EditSettings.changeEnableThemeColorization(
                        keyPath=keyPath,
                        isEnabled=Saved.Menu.enableThemeColorization,
                    )
                if (
                    Saved.Menu.darkModeThemeColorizationType
                    == Defaults.Menu.darkModeThemeColorizationType
                ):
                    EditRegistry.removeValue(
                        keyPath=keyPath,
                        valueName=Path.RegKeys.DarkModeThemeColorizationType,
                    )
                else:
                    EditSettings.changeDarkModeThemeColorizationType(
                        keyPath=keyPath,
                        colorIndex=Saved.Menu.darkModeThemeColorizationType,
                    )
                if (
                    Saved.Menu.lightModeThemeColorizationType
                    == Defaults.Menu.lightModeThemeColorizationType
                ):
                    EditRegistry.removeValue(
                        keyPath=keyPath,
                        valueName=Path.RegKeys.LightModeThemeColorizationType,
                    )
                else:
                    EditSettings.changeLightModeThemeColorizationType(
                        keyPath=keyPath,
                        colorIndex=Saved.Menu.lightModeThemeColorizationType,
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
                if (
                    Saved.Menu.lightModeBorderColor
                    == Defaults.Menu.lightModeBorderColor
                ):
                    EditRegistry.removeValue(
                        keyPath=keyPath,
                        valueName=Path.RegKeys.LightModeBorderColor,
                    )
                else:
                    EditSettings.changeLightModeBorderColor(
                        keyPath=keyPath,
                        color=Saved.Menu.lightModeBorderColor,
                    )
                if (
                    Saved.Menu.darkModeGradientColor
                    == Defaults.Menu.darkModeGradientColor
                ):
                    EditRegistry.removeValue(
                        keyPath=keyPath,
                        valueName=Path.RegKeys.DarkModeGradientColor,
                    )
                else:
                    EditSettings.changeDarkModeGradientColor(
                        keyPath=keyPath,
                        color=Saved.Menu.darkModeGradientColor,
                    )
                if (
                    Saved.Menu.lightModeGradientColor
                    == Defaults.Menu.lightModeGradientColor
                ):
                    EditRegistry.removeValue(
                        keyPath=keyPath,
                        valueName=Path.RegKeys.LightModeGradientColor,
                    )
                else:
                    EditSettings.changeLightModeGradientColor(
                        keyPath=keyPath,
                        color=Saved.Menu.lightModeGradientColor,
                    )
                EditSettings.changeDisabledList(
                    keyPath=keyPath,
                    disabledList=Saved.Menu.disabledList,
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
            except:  # noqa: E722
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
                    if (
                        Saved.Menu.Animation.fadeOutTime
                        == Defaults.Menu.Animation.fadeOutTime
                    ):
                        EditRegistry.removeValue(
                            keyPath=keyPath,
                            valueName=Path.RegKeys.FadeOutTime,
                        )
                    else:
                        EditSettings.changeFadeOutTime(
                            keyPath=keyPath,
                            time=Saved.Menu.Animation.fadeOutTime,
                        )
                    if (
                        Saved.Menu.Animation.popInTime
                        == Defaults.Menu.Animation.popInTime
                    ):
                        EditRegistry.removeValue(
                            keyPath=keyPath,
                            valueName=Path.RegKeys.PopInTime,
                        )
                    else:
                        EditSettings.changePopInTime(
                            keyPath=keyPath,
                            time=Saved.Menu.Animation.popInTime,
                        )
                    if (
                        Saved.Menu.Animation.fadeInTime
                        == Defaults.Menu.Animation.fadeInTime
                    ):
                        EditRegistry.removeValue(
                            keyPath=keyPath,
                            valueName=Path.RegKeys.FadeInTime,
                        )
                    else:
                        EditSettings.changeFadeInTime(
                            keyPath=keyPath,
                            time=Saved.Menu.Animation.fadeInTime,
                        )
                    if (
                        Saved.Menu.Animation.popInStyle
                        == Defaults.Menu.Animation.popInStyle
                    ):
                        EditRegistry.removeValue(
                            keyPath=keyPath,
                            valueName=Path.RegKeys.PopInStyle,
                        )
                    else:
                        EditSettings.changePopInStyle(
                            keyPath=keyPath,
                            style=Saved.Menu.Animation.popInStyle,
                        )
                    if (
                        Saved.Menu.Animation.startRatio
                        == Defaults.Menu.Animation.startRatio
                    ):
                        EditRegistry.removeValue(
                            keyPath=keyPath,
                            valueName=Path.RegKeys.StartRatio,
                        )
                    else:
                        EditSettings.changeStartRatio(
                            keyPath=keyPath,
                            percent=Saved.Menu.Animation.startRatio,
                        )
                    if (
                        Saved.Menu.Animation.enableImmediateInterupting
                        == Defaults.Menu.Animation.enableImmediateInterupting
                    ):
                        EditRegistry.removeValue(
                            keyPath=keyPath,
                            valueName=Path.RegKeys.EnableImmediateInterupting,
                        )
                    else:
                        EditSettings.changeEnableImmediateInterupting(
                            keyPath=keyPath,
                            isEnabled=Saved.Menu.Animation.enableImmediateInterupting,
                        )
                except:  # noqa: E722
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
                    if (
                        Saved.Menu.Hot.lightModeColor
                        == Defaults.Menu.Hot.lightModeColor
                    ):
                        EditRegistry.removeValue(
                            keyPath=keyPath,
                            valueName=Path.RegKeys.LightModeColor,
                        )
                    else:
                        EditSettings.changeLightModeColor(
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
                    if Saved.Menu.Hot.cornerRadius == Defaults.Menu.Hot.cornerRadius:
                        EditRegistry.removeValue(
                            keyPath=keyPath,
                            valueName=Path.RegKeys.CornerRadius,
                        )
                    else:
                        EditSettings.changeCornerRadius(
                            keyPath=keyPath,
                            radius=Saved.Menu.Hot.cornerRadius,
                        )
                    if (
                        Saved.Menu.Hot.enableThemeColorization
                        == Defaults.Menu.Hot.enableThemeColorization
                    ):
                        EditRegistry.removeValue(
                            keyPath=keyPath,
                            valueName=Path.RegKeys.EnableThemeColorization,
                        )
                    else:
                        EditSettings.changeEnableThemeColorization(
                            keyPath=keyPath,
                            isEnabled=Saved.Menu.Hot.enableThemeColorization,
                        )

                except:  # noqa: E722
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
                    if (
                        Saved.Menu.DisabledHot.darkModeColor
                        == Defaults.Menu.DisabledHot.darkModeColor
                    ):
                        EditRegistry.removeValue(
                            keyPath=keyPath,
                            valueName=Path.RegKeys.DarkModeColor,
                        )
                    else:
                        EditSettings.changeDarkModeColor(
                            keyPath=keyPath,
                            color=Saved.Menu.DisabledHot.darkModeColor,
                        )
                    if (
                        Saved.Menu.DisabledHot.lightModeColor
                        == Defaults.Menu.DisabledHot.lightModeColor
                    ):
                        EditRegistry.removeValue(
                            keyPath=keyPath,
                            valueName=Path.RegKeys.LightModeColor,
                        )
                    else:
                        EditSettings.changeLightModeColor(
                            keyPath=keyPath,
                            color=Saved.Menu.DisabledHot.lightModeColor,
                        )
                    if (
                        Saved.Menu.DisabledHot.disabled
                        == Defaults.Menu.DisabledHot.disabled
                    ):
                        EditRegistry.removeValue(
                            keyPath=keyPath,
                            valueName=Path.RegKeys.Disabled,
                        )
                    else:
                        EditSettings.changeDisabled(
                            keyPath=keyPath,
                            isDisabled=Saved.Menu.DisabledHot.disabled,
                        )
                    if (
                        Saved.Menu.DisabledHot.cornerRadius
                        == Defaults.Menu.DisabledHot.cornerRadius
                    ):
                        EditRegistry.removeValue(
                            keyPath=keyPath,
                            valueName=Path.RegKeys.CornerRadius,
                        )
                    else:
                        EditSettings.changeCornerRadius(
                            keyPath=keyPath,
                            radius=Saved.Menu.DisabledHot.cornerRadius,
                        )
                    if (
                        Saved.Menu.DisabledHot.enableThemeColorization
                        == Defaults.Menu.DisabledHot.enableThemeColorization
                    ):
                        EditRegistry.removeValue(
                            keyPath=keyPath,
                            valueName=Path.RegKeys.EnableThemeColorization,
                        )
                    else:
                        EditSettings.changeEnableThemeColorization(
                            keyPath=keyPath,
                            isEnabled=Saved.Menu.DisabledHot.enableThemeColorization,
                        )

                except:  # noqa: E722
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
                    if (
                        Saved.Menu.Focusing.darkModeColor
                        == Defaults.Menu.Focusing.darkModeColor
                    ):
                        EditRegistry.removeValue(
                            keyPath=keyPath,
                            valueName=Path.RegKeys.DarkModeColor,
                        )
                    else:
                        EditSettings.changeDarkModeColor(
                            keyPath=keyPath,
                            color=Saved.Menu.Focusing.darkModeColor,
                        )
                    if (
                        Saved.Menu.Focusing.lightModeColor
                        == Defaults.Menu.Focusing.lightModeColor
                    ):
                        EditRegistry.removeValue(
                            keyPath=keyPath,
                            valueName=Path.RegKeys.LightModeColor,
                        )
                    else:
                        EditSettings.changeLightModeColor(
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
                    if (
                        Saved.Menu.Focusing.cornerRadius
                        == Defaults.Menu.Focusing.cornerRadius
                    ):
                        EditRegistry.removeValue(
                            keyPath=keyPath,
                            valueName=Path.RegKeys.CornerRadius,
                        )
                    else:
                        EditSettings.changeCornerRadius(
                            keyPath=keyPath,
                            radius=Saved.Menu.Focusing.cornerRadius,
                        )
                    if (
                        Saved.Menu.Focusing.enableThemeColorization
                        == Defaults.Menu.Focusing.enableThemeColorization
                    ):
                        EditRegistry.removeValue(
                            keyPath=keyPath,
                            valueName=Path.RegKeys.EnableThemeColorization,
                        )
                    else:
                        EditSettings.changeEnableThemeColorization(
                            keyPath=keyPath,
                            isEnabled=Saved.Menu.Focusing.enableThemeColorization,
                        )

                except:  # noqa: E722
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
                    if (
                        Saved.Menu.Separator.darkModeColor
                        == Defaults.Menu.Separator.darkModeColor
                    ):
                        EditRegistry.removeValue(
                            keyPath=keyPath,
                            valueName=Path.RegKeys.DarkModeColor,
                        )
                    else:
                        EditSettings.changeDarkModeColor(
                            keyPath=keyPath,
                            color=Saved.Menu.Separator.darkModeColor,
                        )
                    if (
                        Saved.Menu.Separator.lightModeColor
                        == Defaults.Menu.Separator.lightModeColor
                    ):
                        EditRegistry.removeValue(
                            keyPath=keyPath,
                            valueName=Path.RegKeys.LightModeColor,
                        )
                    else:
                        EditSettings.changeLightModeColor(
                            keyPath=keyPath,
                            color=Saved.Menu.Separator.lightModeColor,
                        )
                    if (
                        Saved.Menu.Separator.disabled
                        == Defaults.Menu.Separator.disabled
                    ):
                        EditRegistry.removeValue(
                            keyPath=keyPath,
                            valueName=Path.RegKeys.Disabled,
                        )
                    else:
                        EditSettings.changeDisabled(
                            keyPath=keyPath,
                            isDisabled=Saved.Menu.Separator.disabled,
                        )
                    if (
                        Saved.Menu.Separator.cornerRadius
                        == Defaults.Menu.Separator.cornerRadius
                    ):
                        EditRegistry.removeValue(
                            keyPath=keyPath,
                            valueName=Path.RegKeys.CornerRadius,
                        )
                    else:
                        EditSettings.changeCornerRadius(
                            keyPath=keyPath,
                            radius=Saved.Menu.Separator.cornerRadius,
                        )
                    if (
                        Saved.Menu.Separator.enableThemeColorization
                        == Defaults.Menu.Separator.enableThemeColorization
                    ):
                        EditRegistry.removeValue(
                            keyPath=keyPath,
                            valueName=Path.RegKeys.EnableThemeColorization,
                        )
                    else:
                        EditSettings.changeEnableThemeColorization(
                            keyPath=keyPath,
                            isEnabled=Saved.Menu.Separator.enableThemeColorization,
                        )

                except:  # noqa: E722
                    return False
                else:
                    return True

    class Tooltip:
        @staticmethod
        def applyDisabledList():
            """
            Method to update the disabled list
            """
            EditSettings.changeDisabledList(
                keyPath=Path.RegPaths.Tooltip, disabledList=Saved.Tooltip.disabledList
            )

        @staticmethod
        def apply() -> bool:
            """
            Method to:
            - Remove a value if it is being set to its default value
            - Update the value
            """
            keyPath = Path.RegPaths.Tooltip
            try:
                if Saved.Tooltip.effectType == Settings.EffectType.UseGlobalSetting:
                    EditRegistry.removeValue(
                        keyPath=keyPath,
                        valueName=Path.RegKeys.EffectType,
                    )
                else:
                    EditSettings.changeEffectType(
                        keyPath=keyPath,
                        effectType=Saved.Tooltip.effectType,
                    )
                if Saved.Tooltip.cornerType == Defaults.Tooltip.cornerType:
                    EditRegistry.removeValue(
                        keyPath=keyPath,
                        valueName=Path.RegKeys.CornerType,
                    )
                else:
                    EditSettings.changeCornerType(
                        keyPath=keyPath,
                        cornerType=Saved.Tooltip.cornerType,
                    )
                if (
                    Saved.Tooltip.enableDropShadow
                    == Settings.EnableDropShadow.UseGlobalSetting
                ):
                    EditRegistry.removeValue(
                        keyPath=keyPath,
                        valueName=Path.RegKeys.EnableDropShadow,
                    )
                else:
                    EditSettings.changeEnableDropShadow(
                        keyPath=keyPath,
                        isEnabled=Saved.Tooltip.enableDropShadow,
                    )

                if Saved.Tooltip.marginsType == Defaults.Tooltip.marginsType:
                    EditRegistry.removeValue(
                        keyPath=keyPath,
                        valueName=Path.RegKeys.MarginsType,
                    )
                else:
                    EditSettings.changeMarginsType(
                        keyPath=keyPath,
                        marginsType=Saved.Tooltip.marginsType,
                    )
                if Saved.Tooltip.marginLeft == Defaults.Tooltip.marginLeft:
                    EditRegistry.removeValue(
                        keyPath=keyPath,
                        valueName=Path.RegKeys.MarginLeft,
                    )
                else:
                    EditSettings.changeMarginLeft(
                        keyPath=keyPath,
                        margin=Saved.Tooltip.marginLeft,
                    )
                if Saved.Tooltip.marginRight == Defaults.Tooltip.marginRight:
                    EditRegistry.removeValue(
                        keyPath=keyPath,
                        valueName=Path.RegKeys.MarginRight,
                    )
                else:
                    EditSettings.changeMarginRight(
                        keyPath=keyPath,
                        margin=Saved.Tooltip.marginRight,
                    )
                if Saved.Tooltip.marginTop == Defaults.Tooltip.marginTop:
                    EditRegistry.removeValue(
                        keyPath=keyPath,
                        valueName=Path.RegKeys.MarginTop,
                    )
                else:
                    EditSettings.changeMarginTop(
                        keyPath=keyPath,
                        margin=Saved.Tooltip.marginTop,
                    )
                if Saved.Tooltip.marginBottom == Defaults.Tooltip.marginBottom:
                    EditRegistry.removeValue(
                        keyPath=keyPath,
                        valueName=Path.RegKeys.MarginBottom,
                    )
                else:
                    EditSettings.changeMarginBottom(
                        keyPath=keyPath,
                        margin=Saved.Tooltip.marginBottom,
                    )
                if (
                    Saved.Tooltip.noBorderColor
                    == Settings.NoBorderColor.UseGlobalSetting
                ):
                    EditRegistry.removeValue(
                        keyPath=keyPath,
                        valueName=Path.RegKeys.NoBorderColor,
                    )
                else:
                    EditSettings.changeNoBorderColor(
                        keyPath=keyPath,
                        isEnabled=Saved.Tooltip.noBorderColor,
                    )
                if (
                    Saved.Tooltip.enableThemeColorization
                    == Settings.EnableThemeColorization.UseGlobalSetting
                ):
                    EditRegistry.removeValue(
                        keyPath=keyPath,
                        valueName=Path.RegKeys.EnableThemeColorization,
                    )
                else:
                    EditSettings.changeEnableThemeColorization(
                        keyPath=keyPath,
                        isEnabled=Saved.Tooltip.enableThemeColorization,
                    )
                if Saved.Tooltip.darkModeColor == Defaults.Tooltip.darkModeColor:
                    EditRegistry.removeValue(
                        keyPath=keyPath,
                        valueName=Path.RegKeys.DarkModeColor,
                    )
                else:
                    EditSettings.changeDarkModeColor(
                        keyPath=keyPath,
                        color=Saved.Tooltip.darkModeColor,
                    )
                if Saved.Tooltip.lightModeColor == Defaults.Tooltip.lightModeColor:
                    EditRegistry.removeValue(
                        keyPath=keyPath,
                        valueName=Path.RegKeys.LightModeColor,
                    )
                else:
                    EditSettings.changeLightModeColor(
                        keyPath=keyPath,
                        color=Saved.Tooltip.lightModeColor,
                    )
                if (
                    Saved.Tooltip.darkModeBorderColor
                    == Defaults.Tooltip.darkModeBorderColor
                ):
                    EditRegistry.removeValue(
                        keyPath=keyPath,
                        valueName=Path.RegKeys.DarkModeBorderColor,
                    )
                else:
                    EditSettings.changeDarkModeBorderColor(
                        keyPath=keyPath,
                        color=Saved.Tooltip.darkModeBorderColor,
                    )
                if (
                    Saved.Tooltip.lightModeBorderColor
                    == Defaults.Tooltip.lightModeBorderColor
                ):
                    EditRegistry.removeValue(
                        keyPath=keyPath,
                        valueName=Path.RegKeys.LightModeBorderColor,
                    )
                else:
                    EditSettings.changeLightModeBorderColor(
                        keyPath=keyPath,
                        color=Saved.Tooltip.lightModeBorderColor,
                    )
                if (
                    Saved.Tooltip.darkModeGradientColor
                    == Defaults.Tooltip.darkModeGradientColor
                ):
                    EditRegistry.removeValue(
                        keyPath=keyPath,
                        valueName=Path.RegKeys.DarkModeGradientColor,
                    )
                else:
                    EditSettings.changeDarkModeGradientColor(
                        keyPath=keyPath,
                        color=Saved.Tooltip.darkModeGradientColor,
                    )
                if (
                    Saved.Tooltip.lightModeGradientColor
                    == Defaults.Tooltip.lightModeGradientColor
                ):
                    EditRegistry.removeValue(
                        keyPath=keyPath,
                        valueName=Path.RegKeys.LightModeGradientColor,
                    )
                else:
                    EditSettings.changeLightModeGradientColor(
                        keyPath=keyPath,
                        color=Saved.Tooltip.lightModeGradientColor,
                    )
                EditSettings.changeDisabledList(
                    keyPath=keyPath,
                    disabledList=Saved.Tooltip.disabledList,
                )
                if Saved.Tooltip.disabled == Settings.Disabled.UseGlobalSetting:
                    EditRegistry.removeValue(
                        keyPath=keyPath,
                        valueName=Path.RegKeys.Disabled,
                    )
                else:
                    EditSettings.changeDisabled(
                        keyPath=keyPath,
                        isDisabled=Saved.Tooltip.disabled,
                    )
            except:  # noqa: E722
                return False
            else:
                return True

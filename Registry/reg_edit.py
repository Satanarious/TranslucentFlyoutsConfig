from winreg import (
    KEY_READ,
    KEY_SET_VALUE,
    REG_DWORD,
    REG_SZ,
    CloseKey,
    CreateKeyEx,
    DeleteKeyEx,
    DeleteValue,
    EnumValue,
    HKEYType,
    OpenKeyEx,
    QueryValueEx,
    SetValueEx,
)

from Data.defaults import Defaults, Key
from Data.enums import EnumConvert, RegistryReturnType, Settings
from Data.paths import Path


class EditRegistry:
    @staticmethod
    def createAllKeys():
        """
        This Method:
        - Creates the Base Key at "HKEY_CURRENT_USER\\Software\\TranslucentFylouts"
        - Creates the DisabledList Key at "HKEY_CURRENT_USER\\Software\\TranslucentFylouts\\DisabledList"
        - Creates the BlockList Key at "HKEY_CURRENT_USER\\Software\\TranslucentFylouts\\BlockList"
        - Creates the DropDown Key at  "HKEY_CURRENT_USER\\Software\\TranslucentFylouts\\DropDown"
        - Creates the DisabledList Key at  "HKEY_CURRENT_USER\\Software\\TranslucentFylouts\\DropDown\\DisabledList"
        - Creates the Menu Key at  "HKEY_CURRENT_USER\\Software\\TranslucentFylouts\\Menu"
        - Creates the DisabledList Key at  "HKEY_CURRENT_USER\\Software\\TranslucentFylouts\\Menu\\DisabledList"
        - Creates the Menu Subkeys:
            - Animation at "HKEY_CURRENT_USER\\Software\\TranslucentFylouts\\Menu\\Animation"
            - Hot at "HKEY_CURRENT_USER\\Software\\TranslucentFylouts\\Menu\\Hot"
            - DisabledHot at "HKEY_CURRENT_USER\\Software\\TranslucentFylouts\\Menu\\DisabledHot"
            - Focusing at "HKEY_CURRENT_USER\\Software\\TranslucentFylouts\\Menu\\Focusing"
            - Separator at "HKEY_CURRENT_USER\\Software\\TranslucentFylouts\\Menu\\Separator"
            - DisabledList at "HKEY_CURRENT_USER\\Software\\TranslucentFylouts\\Menu\\DisabledList"
        - Creates the Tooltip Key at "HKEY_CURRENT_USER\\Software\\TranslucentFylouts\\Tooltip"
        - Creates the DisabledList Key at "HKEY_CURRENT_USER\\Software\\TranslucentFylouts\\Tooltip\\DisabledList"
        """

        EditRegistry.createKey(
            basePath=Path.RegPaths.Software, keyName=Path.RegKeys.TranslucentFlyouts
        )
        EditRegistry.createKey(
            basePath=Path.RegPaths.Software, keyName=Path.RegKeys.DisabledList
        )
        EditRegistry.createKey(
            basePath=Path.RegPaths.Software, keyName=Path.RegKeys.BlockList
        )
        EditRegistry.createKey(
            basePath=Path.RegPaths.BasePath, keyName=Path.RegKeys.DropDown
        )
        EditRegistry.createKey(
            basePath=Path.RegPaths.BasePath + Path.RegPaths.DropDown,
            keyName=Path.RegKeys.DisabledList,
        )
        EditRegistry.createKey(
            basePath=Path.RegPaths.BasePath, keyName=Path.RegKeys.Menu
        )
        menuPath = Path.RegPaths.BasePath + Path.RegPaths.Menu
        EditRegistry.createKey(basePath=menuPath, keyName=Path.RegKeys.Animation)
        EditRegistry.createKey(basePath=menuPath, keyName=Path.RegKeys.Hot)
        EditRegistry.createKey(basePath=menuPath, keyName=Path.RegKeys.DisabledHot)
        EditRegistry.createKey(basePath=menuPath, keyName=Path.RegKeys.Focusing)
        EditRegistry.createKey(basePath=menuPath, keyName=Path.RegKeys.Separator)
        EditRegistry.createKey(basePath=menuPath, keyName=Path.RegKeys.DisabledList)
        EditRegistry.createKey(
            basePath=Path.RegPaths.BasePath + Path.RegPaths.Tooltip,
            keyName=Path.RegKeys.DisabledList,
        )
        EditRegistry.createKey(
            basePath=Path.RegPaths.BasePath, keyName=Path.RegKeys.Tooltip
        )

    @staticmethod
    def fetchAllValues() -> dict[str, dict]:
        """
        Method to:
        - Read Values from different Registry Keys.
        - Return a dictionary with values if not none, else returns the default values.
        """
        return {
            Key._global: {
                Key.effectType: EditRegistry.readValue(
                    keyPath=Path.RegPaths.Global,
                    valueName=Path.RegKeys.EffectType,
                    defaultValue=Defaults.Global.effectType,
                    returnType=RegistryReturnType.Decimal,
                ),
                Key.cornerType: EditRegistry.readValue(
                    keyPath=Path.RegPaths.Global,
                    valueName=Path.RegKeys.CornerType,
                    defaultValue=Defaults.Global.cornerType,
                    returnType=RegistryReturnType.Decimal,
                ),
                Key.enableDropShadow: EditRegistry.readValue(
                    keyPath=Path.RegPaths.Global,
                    valueName=Path.RegKeys.EnableDropShadow,
                    defaultValue=Defaults.Global.enableDropShadow,
                    returnType=RegistryReturnType.Decimal,
                ),
                Key.noBorderColor: EditRegistry.readValue(
                    keyPath=Path.RegPaths.Global,
                    valueName=Path.RegKeys.NoBorderColor,
                    defaultValue=Defaults.Global.noBorderColor,
                    returnType=RegistryReturnType.Decimal,
                ),
                Key.enableMiniDump: EditRegistry.readValue(
                    keyPath=Path.RegPaths.Global,
                    valueName=Path.RegKeys.EnableMiniDump,
                    defaultValue=Defaults.Global.enableMiniDump,
                    returnType=RegistryReturnType.Decimal,
                ),
                Key.enableThemeColorization: EditRegistry.readValue(
                    keyPath=Path.RegPaths.Global,
                    valueName=Path.RegKeys.EnableThemeColorization,
                    defaultValue=Defaults.Global.enableThemeColorization,
                    returnType=RegistryReturnType.Decimal,
                ),
                Key.darkModeThemeColorizationType: EnumConvert.themeColorizationTypeStringToIndex(
                    EditRegistry.readValue(
                        keyPath=Path.RegPaths.Global,
                        valueName=Path.RegKeys.DarkModeThemeColorizationType,
                        defaultValue=Defaults.Global.darkModeThemeColorizationType,
                        returnType=RegistryReturnType.String,
                    )
                ),
                Key.lightModeThemeColorizationType: EnumConvert.themeColorizationTypeStringToIndex(
                    EditRegistry.readValue(
                        keyPath=Path.RegPaths.Global,
                        valueName=Path.RegKeys.LightModeThemeColorizationType,
                        defaultValue=Defaults.Global.lightModeThemeColorizationType,
                        returnType=RegistryReturnType.String,
                    )
                ),
                Key.darkModeBorderColor: EditRegistry.readValue(
                    keyPath=Path.RegPaths.Global,
                    valueName=Path.RegKeys.DarkModeBorderColor,
                    defaultValue=Defaults.Global.darkModeBorderColor,
                    returnType=RegistryReturnType.Hexadecimal,
                ),
                Key.lightModeBorderColor: EditRegistry.readValue(
                    keyPath=Path.RegPaths.Global,
                    valueName=Path.RegKeys.LightModeBorderColor,
                    defaultValue=Defaults.Global.lightModeBorderColor,
                    returnType=RegistryReturnType.Hexadecimal,
                ),
                Key.darkModeGradientColor: EditRegistry.readValue(
                    keyPath=Path.RegPaths.Global,
                    valueName=Path.RegKeys.DarkModeGradientColor,
                    defaultValue=Defaults.Global.darkModeGradientColor,
                    returnType=RegistryReturnType.Hexadecimal,
                ),
                Key.lightModeGradientColor: EditRegistry.readValue(
                    keyPath=Path.RegPaths.Global,
                    valueName=Path.RegKeys.LightModeGradientColor,
                    defaultValue=Defaults.Global.lightModeGradientColor,
                    returnType=RegistryReturnType.Hexadecimal,
                ),
                Key.disabledList: EditRegistry.readValue(
                    keyPath=Path.RegPaths.Global,
                    valueName=Path.RegKeys.DisabledList,
                    defaultValue=Defaults.Global.disabledList,
                    returnType=RegistryReturnType.List,
                ),
                Key.blockList: EditRegistry.readValue(
                    keyPath=Path.RegPaths.Global,
                    valueName=Path.RegKeys.BlockList,
                    defaultValue=Defaults.Global.blockList,
                    returnType=RegistryReturnType.List,
                ),
                Key.disabled: EditRegistry.readValue(
                    keyPath=Path.RegPaths.Global,
                    valueName=Path.RegKeys.Disabled,
                    defaultValue=Defaults.Global.disabled,
                    returnType=RegistryReturnType.Decimal,
                ),
            },
            Key.dropdown: {
                Key.effectType: EditRegistry.readValue(
                    keyPath=Path.RegPaths.DropDown,
                    valueName=Path.RegKeys.EffectType,
                    defaultValue=Defaults.DropDown.effectType,
                    returnType=RegistryReturnType.Decimal,
                ),
                Key.cornerType: EditRegistry.readValue(
                    keyPath=Path.RegPaths.DropDown,
                    valueName=Path.RegKeys.CornerType,
                    defaultValue=Defaults.DropDown.cornerType,
                    returnType=RegistryReturnType.Decimal,
                ),
                Key.enableDropShadow: EditRegistry.readValue(
                    keyPath=Path.RegPaths.DropDown,
                    valueName=Path.RegKeys.EnableDropShadow,
                    defaultValue=Defaults.DropDown.enableDropShadow,
                    returnType=RegistryReturnType.Decimal,
                ),
                Key.noBorderColor: EditRegistry.readValue(
                    keyPath=Path.RegPaths.DropDown,
                    valueName=Path.RegKeys.NoBorderColor,
                    defaultValue=Defaults.DropDown.noBorderColor,
                    returnType=RegistryReturnType.Decimal,
                ),
                Key.enableFluentAnimation: EditRegistry.readValue(
                    keyPath=Path.RegPaths.DropDown,
                    valueName=Path.RegKeys.EnableFluentAnimation,
                    defaultValue=Defaults.DropDown.enableFluentAnimation,
                    returnType=RegistryReturnType.Decimal,
                ),
                Key.enableThemeColorization: EditRegistry.readValue(
                    keyPath=Path.RegPaths.DropDown,
                    valueName=Path.RegKeys.EnableThemeColorization,
                    defaultValue=Defaults.DropDown.enableThemeColorization,
                    returnType=RegistryReturnType.Decimal,
                ),
                Key.darkModeBorderColor: EditRegistry.readValue(
                    keyPath=Path.RegPaths.DropDown,
                    valueName=Path.RegKeys.DarkModeBorderColor,
                    defaultValue=Defaults.DropDown.darkModeBorderColor,
                    returnType=RegistryReturnType.Hexadecimal,
                ),
                Key.lightModeBorderColor: EditRegistry.readValue(
                    keyPath=Path.RegPaths.DropDown,
                    valueName=Path.RegKeys.LightModeBorderColor,
                    defaultValue=Defaults.DropDown.lightModeBorderColor,
                    returnType=RegistryReturnType.Hexadecimal,
                ),
                Key.darkModeGradientColor: EditRegistry.readValue(
                    keyPath=Path.RegPaths.DropDown,
                    valueName=Path.RegKeys.DarkModeGradientColor,
                    defaultValue=Defaults.DropDown.darkModeGradientColor,
                    returnType=RegistryReturnType.Hexadecimal,
                ),
                Key.lightModeGradientColor: EditRegistry.readValue(
                    keyPath=Path.RegPaths.DropDown,
                    valueName=Path.RegKeys.LightModeGradientColor,
                    defaultValue=Defaults.DropDown.lightModeGradientColor,
                    returnType=RegistryReturnType.Hexadecimal,
                ),
                Key.disabledList: EditRegistry.readValue(
                    keyPath=Path.RegPaths.DropDown,
                    valueName=Path.RegKeys.DisabledList,
                    defaultValue=Defaults.DropDown.disabledList,
                    returnType=RegistryReturnType.List,
                ),
                Key.disabled: EditRegistry.readValue(
                    keyPath=Path.RegPaths.DropDown,
                    valueName=Path.RegKeys.Disabled,
                    defaultValue=Defaults.DropDown.disabled,
                    returnType=RegistryReturnType.Decimal,
                ),
                Key.animation: {
                    Key.fadeOutTime: EditRegistry.readValue(
                        keyPath=Path.RegPaths.DropDown + Path.RegPaths.Animation,
                        valueName=Path.RegKeys.FadeOutTime,
                        defaultValue=Defaults.DropDown.Animation.fadeOutTime,
                        returnType=RegistryReturnType.Decimal,
                    ),
                    Key.popInTime: EditRegistry.readValue(
                        keyPath=Path.RegPaths.DropDown + Path.RegPaths.Animation,
                        valueName=Path.RegKeys.PopInTime,
                        defaultValue=Defaults.DropDown.Animation.popInTime,
                        returnType=RegistryReturnType.Decimal,
                    ),
                    Key.fadeInTime: EditRegistry.readValue(
                        keyPath=Path.RegPaths.DropDown + Path.RegPaths.Animation,
                        valueName=Path.RegKeys.FadeInTime,
                        defaultValue=Defaults.DropDown.Animation.fadeInTime,
                        returnType=RegistryReturnType.Decimal,
                    ),
                    Key.popInStyle: EditRegistry.readValue(
                        keyPath=Path.RegPaths.DropDown + Path.RegPaths.Animation,
                        valueName=Path.RegKeys.PopInStyle,
                        defaultValue=Defaults.DropDown.Animation.popInStyle,
                        returnType=RegistryReturnType.Decimal,
                    ),
                    Key.startRatio: EditRegistry.readValue(
                        keyPath=Path.RegPaths.DropDown + Path.RegPaths.Animation,
                        valueName=Path.RegKeys.StartRatio,
                        defaultValue=Defaults.DropDown.Animation.startRatio,
                        returnType=RegistryReturnType.Decimal,
                    ),
                    Key.enableImmediateInterupting: EditRegistry.readValue(
                        keyPath=Path.RegPaths.DropDown + Path.RegPaths.Animation,
                        valueName=Path.RegKeys.EnableImmediateInterupting,
                        defaultValue=Defaults.DropDown.Animation.enableImmediateInterupting,
                        returnType=RegistryReturnType.Decimal,
                    ),
                },
            },
            Key.menu: {
                Key.noSystemDropShadow: EditRegistry.readValue(
                    keyPath=Path.RegPaths.Menu,
                    valueName=Path.RegKeys.NoSystemDropShadow,
                    defaultValue=Defaults.Menu.noSystemDropShadow,
                    returnType=RegistryReturnType.Decimal,
                ),
                Key.enableImmersiveStyle: EditRegistry.readValue(
                    keyPath=Path.RegPaths.Menu,
                    valueName=Path.RegKeys.EnableImmersiveStyle,
                    defaultValue=Defaults.Menu.enableImmersiveStyle,
                    returnType=RegistryReturnType.Decimal,
                ),
                Key.enableCustomRendering: EditRegistry.readValue(
                    keyPath=Path.RegPaths.Menu,
                    valueName=Path.RegKeys.EnableCustomRendering,
                    defaultValue=Defaults.Menu.enableCustomRendering,
                    returnType=RegistryReturnType.Decimal,
                ),
                Key.enableFluentAnimation: EditRegistry.readValue(
                    keyPath=Path.RegPaths.Menu,
                    valueName=Path.RegKeys.EnableFluentAnimation,
                    defaultValue=Defaults.Menu.enableFluentAnimation,
                    returnType=RegistryReturnType.Decimal,
                ),
                Key.noModernAppBackgroundColor: EditRegistry.readValue(
                    keyPath=Path.RegPaths.Menu,
                    valueName=Path.RegKeys.NoModernAppBackgroundColor,
                    defaultValue=Defaults.Menu.noModernAppBackgroundColor,
                    returnType=RegistryReturnType.Decimal,
                ),
                Key.colorTreatAsTransparent: EditRegistry.readValue(
                    keyPath=Path.RegPaths.Menu,
                    valueName=Path.RegKeys.ColorTreatAsTransparent,
                    defaultValue=Defaults.Menu.colorTreatAsTransparent,
                    returnType=RegistryReturnType.Hexadecimal,
                ),
                Key.colorTreatAsTransparentThreshold: EditRegistry.readValue(
                    keyPath=Path.RegPaths.Menu,
                    valueName=Path.RegKeys.ColorTreatAsTransparentThreshold,
                    defaultValue=Defaults.Menu.colorTreatAsTransparentThreshold,
                    returnType=RegistryReturnType.Decimal,
                ),
                Key.effectType: EditRegistry.readValue(
                    keyPath=Path.RegPaths.Menu,
                    valueName=Path.RegKeys.EffectType,
                    defaultValue=Defaults.Menu.effectType,
                    returnType=RegistryReturnType.Decimal,
                ),
                Key.cornerType: EditRegistry.readValue(
                    keyPath=Path.RegPaths.Menu,
                    valueName=Path.RegKeys.CornerType,
                    defaultValue=Defaults.Menu.cornerType,
                    returnType=RegistryReturnType.Decimal,
                ),
                Key.enableDropShadow: EditRegistry.readValue(
                    keyPath=Path.RegPaths.Menu,
                    valueName=Path.RegKeys.EnableDropShadow,
                    defaultValue=Defaults.Menu.enableDropShadow,
                    returnType=RegistryReturnType.Decimal,
                ),
                Key.noBorderColor: EditRegistry.readValue(
                    keyPath=Path.RegPaths.Menu,
                    valueName=Path.RegKeys.NoBorderColor,
                    defaultValue=Defaults.Menu.noBorderColor,
                    returnType=RegistryReturnType.Decimal,
                ),
                Key.enableCompatibilityMode: EditRegistry.readValue(
                    keyPath=Path.RegPaths.Menu,
                    valueName=Path.RegKeys.EnableCompatibilityMode,
                    defaultValue=Defaults.Menu.enableCompatibilityMode,
                    returnType=RegistryReturnType.Decimal,
                ),
                Key.enableThemeColorization: EditRegistry.readValue(
                    keyPath=Path.RegPaths.Menu,
                    valueName=Path.RegKeys.EnableThemeColorization,
                    defaultValue=Defaults.Menu.enableThemeColorization,
                    returnType=RegistryReturnType.Decimal,
                ),
                Key.darkModeThemeColorizationType: EnumConvert.themeColorizationTypeStringToIndex(
                    EditRegistry.readValue(
                        keyPath=Path.RegPaths.Menu,
                        valueName=Path.RegKeys.DarkModeThemeColorizationType,
                        defaultValue=Defaults.Menu.darkModeThemeColorizationType,
                        returnType=RegistryReturnType.String,
                    )
                ),
                Key.lightModeThemeColorizationType: EnumConvert.themeColorizationTypeStringToIndex(
                    EditRegistry.readValue(
                        keyPath=Path.RegPaths.Menu,
                        valueName=Path.RegKeys.LightModeThemeColorizationType,
                        defaultValue=Defaults.Menu.lightModeThemeColorizationType,
                        returnType=RegistryReturnType.String,
                    )
                ),
                Key.darkModeBorderColor: EditRegistry.readValue(
                    keyPath=Path.RegPaths.Menu,
                    valueName=Path.RegKeys.DarkModeBorderColor,
                    defaultValue=Defaults.Menu.darkModeBorderColor,
                    returnType=RegistryReturnType.Hexadecimal,
                ),
                Key.lightModeBorderColor: EditRegistry.readValue(
                    keyPath=Path.RegPaths.Menu,
                    valueName=Path.RegKeys.LightModeBorderColor,
                    defaultValue=Defaults.Menu.lightModeBorderColor,
                    returnType=RegistryReturnType.Hexadecimal,
                ),
                Key.darkModeGradientColor: EditRegistry.readValue(
                    keyPath=Path.RegPaths.Menu,
                    valueName=Path.RegKeys.DarkModeGradientColor,
                    defaultValue=Defaults.Menu.darkModeGradientColor,
                    returnType=RegistryReturnType.Hexadecimal,
                ),
                Key.lightModeGradientColor: EditRegistry.readValue(
                    keyPath=Path.RegPaths.Menu,
                    valueName=Path.RegKeys.LightModeGradientColor,
                    defaultValue=Defaults.Menu.lightModeGradientColor,
                    returnType=RegistryReturnType.Hexadecimal,
                ),
                Key.disabledList: EditRegistry.readValue(
                    keyPath=Path.RegPaths.Menu,
                    valueName=Path.RegKeys.DisabledList,
                    defaultValue=Defaults.Menu.disabledList,
                    returnType=RegistryReturnType.List,
                ),
                Key.disabled: EditRegistry.readValue(
                    keyPath=Path.RegPaths.Menu,
                    valueName=Path.RegKeys.Disabled,
                    defaultValue=Defaults.Menu.disabled,
                    returnType=RegistryReturnType.Decimal,
                ),
                Key.animation: {
                    Key.fadeOutTime: EditRegistry.readValue(
                        keyPath=Path.RegPaths.Menu + Path.RegPaths.Animation,
                        valueName=Path.RegKeys.FadeOutTime,
                        defaultValue=Defaults.Menu.Animation.fadeOutTime,
                        returnType=RegistryReturnType.Decimal,
                    ),
                    Key.popInTime: EditRegistry.readValue(
                        keyPath=Path.RegPaths.Menu + Path.RegPaths.Animation,
                        valueName=Path.RegKeys.PopInTime,
                        defaultValue=Defaults.Menu.Animation.popInTime,
                        returnType=RegistryReturnType.Decimal,
                    ),
                    Key.fadeInTime: EditRegistry.readValue(
                        keyPath=Path.RegPaths.Menu + Path.RegPaths.Animation,
                        valueName=Path.RegKeys.FadeInTime,
                        defaultValue=Defaults.Menu.Animation.fadeInTime,
                        returnType=RegistryReturnType.Decimal,
                    ),
                    Key.popInStyle: EditRegistry.readValue(
                        keyPath=Path.RegPaths.Menu + Path.RegPaths.Animation,
                        valueName=Path.RegKeys.PopInStyle,
                        defaultValue=Defaults.Menu.Animation.popInStyle,
                        returnType=RegistryReturnType.Decimal,
                    ),
                    Key.startRatio: EditRegistry.readValue(
                        keyPath=Path.RegPaths.Menu + Path.RegPaths.Animation,
                        valueName=Path.RegKeys.StartRatio,
                        defaultValue=Defaults.Menu.Animation.startRatio,
                        returnType=RegistryReturnType.Decimal,
                    ),
                    Key.enableImmediateInterupting: EditRegistry.readValue(
                        keyPath=Path.RegPaths.Menu + Path.RegPaths.Animation,
                        valueName=Path.RegKeys.EnableImmediateInterupting,
                        defaultValue=Defaults.Menu.Animation.enableImmediateInterupting,
                        returnType=RegistryReturnType.Decimal,
                    ),
                },
                Key.disabledHot: {
                    Key.cornerRadius: EditRegistry.readValue(
                        keyPath=Path.RegPaths.Menu + Path.RegPaths.DisabledHot,
                        valueName=Path.RegKeys.CornerRadius,
                        defaultValue=Defaults.Menu.DisabledHot.cornerRadius,
                        returnType=RegistryReturnType.Decimal,
                    ),
                    Key.darkModeColor: EditRegistry.readValue(
                        keyPath=Path.RegPaths.Menu + Path.RegPaths.DisabledHot,
                        valueName=Path.RegKeys.DarkModeColor,
                        defaultValue=Defaults.Menu.DisabledHot.darkModeColor,
                        returnType=RegistryReturnType.Hexadecimal,
                    ),
                    Key.lightModeColor: EditRegistry.readValue(
                        keyPath=Path.RegPaths.Menu + Path.RegPaths.DisabledHot,
                        valueName=Path.RegKeys.LightModeColor,
                        defaultValue=Defaults.Menu.DisabledHot.lightModeColor,
                        returnType=RegistryReturnType.Hexadecimal,
                    ),
                    Key.enableThemeColorization: EditRegistry.readValue(
                        keyPath=Path.RegPaths.Menu + Path.RegPaths.DisabledHot,
                        valueName=Path.RegKeys.EnableThemeColorization,
                        defaultValue=Defaults.Menu.DisabledHot.enableThemeColorization,
                        returnType=RegistryReturnType.Decimal,
                    ),
                    Key.disabled: EditRegistry.readValue(
                        keyPath=Path.RegPaths.Menu + Path.RegPaths.DisabledHot,
                        valueName=Path.RegKeys.Disabled,
                        defaultValue=Defaults.Menu.DisabledHot.disabled,
                        returnType=RegistryReturnType.Decimal,
                    ),
                },
                Key.focusing: {
                    Key.width: EditRegistry.readValue(
                        keyPath=Path.RegPaths.Menu + Path.RegPaths.Focusing,
                        valueName=Path.RegKeys.Width,
                        defaultValue=Defaults.Menu.Focusing.width,
                        returnType=RegistryReturnType.Decimal,
                    ),
                    Key.cornerRadius: EditRegistry.readValue(
                        keyPath=Path.RegPaths.Menu + Path.RegPaths.Focusing,
                        valueName=Path.RegKeys.CornerRadius,
                        defaultValue=Defaults.Menu.Focusing.cornerRadius,
                        returnType=RegistryReturnType.Decimal,
                    ),
                    Key.darkModeColor: EditRegistry.readValue(
                        keyPath=Path.RegPaths.Menu + Path.RegPaths.Focusing,
                        valueName=Path.RegKeys.DarkModeColor,
                        defaultValue=Defaults.Menu.Focusing.darkModeColor,
                        returnType=RegistryReturnType.Hexadecimal,
                    ),
                    Key.lightModeColor: EditRegistry.readValue(
                        keyPath=Path.RegPaths.Menu + Path.RegPaths.Focusing,
                        valueName=Path.RegKeys.LightModeColor,
                        defaultValue=Defaults.Menu.Focusing.lightModeColor,
                        returnType=RegistryReturnType.Hexadecimal,
                    ),
                    Key.enableThemeColorization: EditRegistry.readValue(
                        keyPath=Path.RegPaths.Menu + Path.RegPaths.Focusing,
                        valueName=Path.RegKeys.EnableThemeColorization,
                        defaultValue=Defaults.Menu.Focusing.enableThemeColorization,
                        returnType=RegistryReturnType.Decimal,
                    ),
                    Key.disabled: EditRegistry.readValue(
                        keyPath=Path.RegPaths.Menu + Path.RegPaths.Focusing,
                        valueName=Path.RegKeys.Disabled,
                        defaultValue=Defaults.Menu.Focusing.disabled,
                        returnType=RegistryReturnType.Decimal,
                    ),
                },
                Key.hot: {
                    Key.cornerRadius: EditRegistry.readValue(
                        keyPath=Path.RegPaths.Menu + Path.RegPaths.Hot,
                        valueName=Path.RegKeys.CornerRadius,
                        defaultValue=Defaults.Menu.Hot.cornerRadius,
                        returnType=RegistryReturnType.Decimal,
                    ),
                    Key.darkModeColor: EditRegistry.readValue(
                        keyPath=Path.RegPaths.Menu + Path.RegPaths.Hot,
                        valueName=Path.RegKeys.DarkModeColor,
                        defaultValue=Defaults.Menu.Hot.darkModeColor,
                        returnType=RegistryReturnType.Hexadecimal,
                    ),
                    Key.lightModeColor: EditRegistry.readValue(
                        keyPath=Path.RegPaths.Menu + Path.RegPaths.Hot,
                        valueName=Path.RegKeys.LightModeColor,
                        defaultValue=Defaults.Menu.Hot.lightModeColor,
                        returnType=RegistryReturnType.Hexadecimal,
                    ),
                    Key.enableThemeColorization: EditRegistry.readValue(
                        keyPath=Path.RegPaths.Menu + Path.RegPaths.Hot,
                        valueName=Path.RegKeys.EnableThemeColorization,
                        defaultValue=Defaults.Menu.Hot.enableThemeColorization,
                        returnType=RegistryReturnType.Decimal,
                    ),
                    Key.disabled: EditRegistry.readValue(
                        keyPath=Path.RegPaths.Menu + Path.RegPaths.Hot,
                        valueName=Path.RegKeys.Disabled,
                        defaultValue=Defaults.Menu.Hot.disabled,
                        returnType=RegistryReturnType.Decimal,
                    ),
                },
                Key.separator: {
                    Key.width: EditRegistry.readValue(
                        keyPath=Path.RegPaths.Menu + Path.RegPaths.Separator,
                        valueName=Path.RegKeys.Width,
                        defaultValue=Defaults.Menu.Separator.width,
                        returnType=RegistryReturnType.Decimal,
                    ),
                    Key.cornerRadius: EditRegistry.readValue(
                        keyPath=Path.RegPaths.Menu + Path.RegPaths.Separator,
                        valueName=Path.RegKeys.CornerRadius,
                        defaultValue=Defaults.Menu.Separator.cornerRadius,
                        returnType=RegistryReturnType.Decimal,
                    ),
                    Key.darkModeColor: EditRegistry.readValue(
                        keyPath=Path.RegPaths.Menu + Path.RegPaths.Separator,
                        valueName=Path.RegKeys.DarkModeColor,
                        defaultValue=Defaults.Menu.Separator.darkModeColor,
                        returnType=RegistryReturnType.Hexadecimal,
                    ),
                    Key.lightModeColor: EditRegistry.readValue(
                        keyPath=Path.RegPaths.Menu + Path.RegPaths.Separator,
                        valueName=Path.RegKeys.LightModeColor,
                        defaultValue=Defaults.Menu.Separator.lightModeColor,
                        returnType=RegistryReturnType.Hexadecimal,
                    ),
                    Key.enableThemeColorization: EditRegistry.readValue(
                        keyPath=Path.RegPaths.Menu + Path.RegPaths.Separator,
                        valueName=Path.RegKeys.EnableThemeColorization,
                        defaultValue=Defaults.Menu.Separator.enableThemeColorization,
                        returnType=RegistryReturnType.Decimal,
                    ),
                    Key.disabled: EditRegistry.readValue(
                        keyPath=Path.RegPaths.Menu + Path.RegPaths.Separator,
                        valueName=Path.RegKeys.Disabled,
                        defaultValue=Defaults.Menu.Separator.disabled,
                        returnType=RegistryReturnType.Decimal,
                    ),
                },
            },
            Key.tooltip: {
                Key.effectType: EditRegistry.readValue(
                    keyPath=Path.RegPaths.Tooltip,
                    valueName=Path.RegKeys.EffectType,
                    defaultValue=Defaults.Tooltip.effectType,
                    returnType=RegistryReturnType.Decimal,
                ),
                Key.cornerType: EditRegistry.readValue(
                    keyPath=Path.RegPaths.Tooltip,
                    valueName=Path.RegKeys.CornerType,
                    defaultValue=Defaults.Tooltip.cornerType,
                    returnType=RegistryReturnType.Decimal,
                ),
                Key.enableDropShadow: EditRegistry.readValue(
                    keyPath=Path.RegPaths.Tooltip,
                    valueName=Path.RegKeys.EnableDropShadow,
                    defaultValue=Defaults.Tooltip.enableDropShadow,
                    returnType=RegistryReturnType.Decimal,
                ),
                Key.noBorderColor: EditRegistry.readValue(
                    keyPath=Path.RegPaths.Tooltip,
                    valueName=Path.RegKeys.NoBorderColor,
                    defaultValue=Defaults.Tooltip.noBorderColor,
                    returnType=RegistryReturnType.Decimal,
                ),
                Key.enableThemeColorization: EditRegistry.readValue(
                    keyPath=Path.RegPaths.Tooltip,
                    valueName=Path.RegKeys.EnableThemeColorization,
                    defaultValue=Defaults.Tooltip.enableThemeColorization,
                    returnType=RegistryReturnType.Decimal,
                ),
                Key.marginsType: EditRegistry.readValue(
                    keyPath=Path.RegPaths.Tooltip,
                    valueName=Path.RegKeys.MarginsType,
                    defaultValue=Defaults.Tooltip.marginsType,
                    returnType=RegistryReturnType.Decimal,
                ),
                Key.marginLeft: EditRegistry.readValue(
                    keyPath=Path.RegPaths.Tooltip,
                    valueName=Path.RegKeys.MarginLeft,
                    defaultValue=Defaults.Tooltip.marginLeft,
                    returnType=RegistryReturnType.Decimal,
                ),
                Key.marginRight: EditRegistry.readValue(
                    keyPath=Path.RegPaths.Tooltip,
                    valueName=Path.RegKeys.MarginRight,
                    defaultValue=Defaults.Tooltip.marginRight,
                    returnType=RegistryReturnType.Decimal,
                ),
                Key.marginTop: EditRegistry.readValue(
                    keyPath=Path.RegPaths.Tooltip,
                    valueName=Path.RegKeys.MarginTop,
                    defaultValue=Defaults.Tooltip.marginTop,
                    returnType=RegistryReturnType.Decimal,
                ),
                Key.marginBottom: EditRegistry.readValue(
                    keyPath=Path.RegPaths.Tooltip,
                    valueName=Path.RegKeys.MarginBottom,
                    defaultValue=Defaults.Tooltip.marginBottom,
                    returnType=RegistryReturnType.Decimal,
                ),
                Key.darkModeColor: EditRegistry.readValue(
                    keyPath=Path.RegPaths.Tooltip,
                    valueName=Path.RegKeys.DarkModeColor,
                    defaultValue=Defaults.Tooltip.darkModeColor,
                    returnType=RegistryReturnType.Hexadecimal,
                ),
                Key.lightModeColor: EditRegistry.readValue(
                    keyPath=Path.RegPaths.Tooltip,
                    valueName=Path.RegKeys.LightModeColor,
                    defaultValue=Defaults.Tooltip.lightModeColor,
                    returnType=RegistryReturnType.Hexadecimal,
                ),
                Key.darkModeBorderColor: EditRegistry.readValue(
                    keyPath=Path.RegPaths.Tooltip,
                    valueName=Path.RegKeys.DarkModeBorderColor,
                    defaultValue=Defaults.Tooltip.darkModeBorderColor,
                    returnType=RegistryReturnType.Hexadecimal,
                ),
                Key.lightModeBorderColor: EditRegistry.readValue(
                    keyPath=Path.RegPaths.Tooltip,
                    valueName=Path.RegKeys.LightModeBorderColor,
                    defaultValue=Defaults.Tooltip.lightModeBorderColor,
                    returnType=RegistryReturnType.Hexadecimal,
                ),
                Key.darkModeGradientColor: EditRegistry.readValue(
                    keyPath=Path.RegPaths.Tooltip,
                    valueName=Path.RegKeys.DarkModeGradientColor,
                    defaultValue=Defaults.Tooltip.darkModeGradientColor,
                    returnType=RegistryReturnType.Hexadecimal,
                ),
                Key.lightModeGradientColor: EditRegistry.readValue(
                    keyPath=Path.RegPaths.Tooltip,
                    valueName=Path.RegKeys.LightModeGradientColor,
                    defaultValue=Defaults.Tooltip.lightModeGradientColor,
                    returnType=RegistryReturnType.Hexadecimal,
                ),
                Key.disabledList: EditRegistry.readValue(
                    keyPath=Path.RegPaths.Tooltip,
                    valueName=Path.RegKeys.DisabledList,
                    defaultValue=Defaults.Tooltip.disabledList,
                    returnType=RegistryReturnType.List,
                ),
                Key.disabled: EditRegistry.readValue(
                    keyPath=Path.RegPaths.Tooltip,
                    valueName=Path.RegKeys.Disabled,
                    defaultValue=Defaults.Tooltip.disabled,
                    returnType=RegistryReturnType.Decimal,
                ),
            },
        }

    @staticmethod
    def createKey(
        basePath: str,
        keyName: str,
    ):
        """
        This method:
        - Creates a new key in the provided base path
        - basePath: is the r-string path to the key
        - key: is the name of the key to be created
        """
        base: HKEYType = OpenKeyEx(Path.RegKeys.BaseKey, basePath)
        main: HKEYType = CreateKeyEx(base, str(keyName))
        if base:
            CloseKey(base)
        if main:
            CloseKey(main)

    @staticmethod
    def removeKey(keyPath: Path.RegPaths | str):
        """
        This method:
        - Deletes a key in the provided base path
        - keyPath: is the r-string path to the key
        """
        try:
            DeleteKeyEx(
                key=Path.RegKeys.BaseKey,
                sub_key=str(Path.RegPaths.BasePath + str(keyPath)),
                reserved=0,
                access=KEY_SET_VALUE,
            )
        except:  # noqa: E722
            pass

    @staticmethod
    def setValue(
        keyPath: Path.RegPaths | str,
        valueName: str,
        value: str | int | list,
    ):
        """
        This Method:
        - Sets the value of the provided key
        - keyPath: is the path to the key under which the subkey lies, which will contain the value
        - valueName: is the value which needs to be set
        - value: is the value of the subkey, which needs a value to be set
        """

        if isinstance(value, list):
            path = Path.RegPaths.BasePath + str(keyPath) + rf"{valueName}\\"
            base = OpenKeyEx(
                key=Path.RegKeys.BaseKey,
                sub_key=path,
                reserved=0,
                access=KEY_READ | KEY_SET_VALUE,
            )
            i = 0
            while True:
                try:
                    # Delete all values
                    values = EnumValue(base, i)
                    if values[2] == REG_DWORD:
                        DeleteValue(base, values[0])
                    else:
                        i += 1
                except:  # noqa: E722
                    break

            # Add new values
            for process in value:
                name, isEnabled = process
                SetValueEx(
                    base,
                    name,
                    0,
                    REG_DWORD,
                    isEnabled,
                )
        else:
            base: HKEYType = OpenKeyEx(
                key=Path.RegKeys.BaseKey,
                sub_key=str(Path.RegPaths.BasePath + str(keyPath)),
                reserved=0,
                access=KEY_SET_VALUE,
            )
            SetValueEx(
                base,
                valueName,
                0,
                REG_DWORD if isinstance(value, int) else REG_SZ,
                value,
            )

        if base:
            CloseKey(base)

    @staticmethod
    def removeValue(
        keyPath: Path.RegPaths | str,
        valueName: str,
    ):
        """
        This Method:
        - Sets the value of the provided key
        - keyPath: is the path to the key under which the subkey lies, which will contain the value
        - subKey: is the key which needs to be removed
        """
        try:
            base: HKEYType = OpenKeyEx(
                key=Path.RegKeys.BaseKey,
                sub_key=str(Path.RegPaths.BasePath + str(keyPath)),
                reserved=0,
                access=KEY_SET_VALUE,
            )
            DeleteValue(base, valueName)
            if base:
                CloseKey(base)
        except:  # noqa: E722
            pass

    @staticmethod
    def readValue(
        keyPath: Path.RegPaths | str,
        valueName: str,
        defaultValue: str | int | list[str],
        returnType: RegistryReturnType,
    ) -> str | int | list[str] | Settings.ThemeColorizationType:
        """_summary_
        Reads a value from the registry.

        Args:
            keyPath (Path.RegPaths | str): The path to the registry key.
            valueName (str): The name of the value to read.
            defaultValue (str | int | list[str]): The default data to use for the value in case there is an error
            returnType (RegistryReturnType): The return type of this method

        Returns:
            str | int | list[str]: returns the data for the value accessed in the registry
        """

        try:
            # Get list of processes in DisabledList
            if returnType == RegistryReturnType.List:
                path = Path.RegPaths.BasePath + str(keyPath) + rf"{valueName}\\"
                key = OpenKeyEx(
                    key=Path.RegKeys.BaseKey,
                    sub_key=path,
                    reserved=0,
                    access=KEY_READ,
                )
                i = 0
                keyList: list = []
                while True:
                    try:
                        name, isEnabled, valueType = EnumValue(key, i)
                        if valueType == REG_DWORD:
                            keyList.append((name, isEnabled))
                    except:  # noqa: E722
                        break
                    i += 1

                if key:
                    CloseKey(key)
                return keyList

            path: str = Path.RegPaths.BasePath + str(keyPath)
            key = OpenKeyEx(
                key=Path.RegKeys.BaseKey,
                sub_key=path,
                reserved=0,
                access=KEY_READ,
            )

            value, _ = QueryValueEx(key, valueName)

            if key:
                CloseKey(key)

            if returnType == RegistryReturnType.Hexadecimal:
                # Convert value to hexadecimal
                return hex(value)[2:].upper()
            elif returnType == RegistryReturnType.Decimal:
                return int(value)
            elif returnType == RegistryReturnType.String:
                return value

        except:  # noqa: E722
            return defaultValue

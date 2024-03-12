# Library Imports
from winreg import HKEYType, REG_DWORD, KEY_SET_VALUE, KEY_READ, QueryValueEx
from winreg import OpenKeyEx, CreateKeyEx, CloseKey, SetValueEx, DeleteKeyEx, DeleteValue

# Relative Imports
from Data.paths import Path
from Data.defaults import Defaults
from Data.enums import RegistryReturnType


class EditRegistry:
    @staticmethod
    def createAllKeys():
        """
        This Method:
        - Creates the Base Key at "HKEY_CURRENT_USER\\Software\\TranslucentFylouts"
        - Creates the DropDown Key at  "HKEY_CURRENT_USER\\Software\\TranslucentFylouts\\DropDown"
        - Creates the Menu Key at  "HKEY_CURRENT_USER\\Software\\TranslucentFylouts\\Menu"
        - Creates the Menu Subkeys:
            - Animation at "HKEY_CURRENT_USER\\Software\\TranslucentFylouts\\Menu\\Animation"
            - Hot at "HKEY_CURRENT_USER\\Software\\TranslucentFylouts\\Menu\\Hot"
            - DisabledHot at "HKEY_CURRENT_USER\\Software\\TranslucentFylouts\\Menu\\DisabledHot"
            - Focusing at "HKEY_CURRENT_USER\\Software\\TranslucentFylouts\\Menu\\Focusing"
            - Separator at "HKEY_CURRENT_USER\\Software\\TranslucentFylouts\\Menu\\Separator"
        - Creates the Tooltip Key at "HKEY_CURRENT_USER\\Software\\TranslucentFylouts\\Tooltip"
        """
        menuPath = Path.RegPaths.BasePath + Path.RegPaths.Menu
        EditRegistry.createKey(basePath=Path.RegPaths.Software, keyName=Path.RegKeys.TranslucentFlyouts)
        EditRegistry.createKey(basePath=Path.RegPaths.BasePath, keyName=Path.RegKeys.DropDown)
        EditRegistry.createKey(basePath=Path.RegPaths.BasePath, keyName=Path.RegKeys.Menu)
        EditRegistry.createKey(basePath=menuPath, keyName=Path.RegKeys.Animation)
        EditRegistry.createKey(basePath=menuPath, keyName=Path.RegKeys.Hot)
        EditRegistry.createKey(basePath=menuPath, keyName=Path.RegKeys.DisabledHot)
        EditRegistry.createKey(basePath=menuPath, keyName=Path.RegKeys.Focusing)
        EditRegistry.createKey(basePath=menuPath, keyName=Path.RegKeys.Separator)
        EditRegistry.createKey(basePath=Path.RegPaths.BasePath, keyName=Path.RegKeys.Tooltip)

    @staticmethod
    def fetchAllValues() -> dict:
        """
        Method to:
        - Read Values from different Registry Keys.
        - Return a dictionary with values if not none, else returns the default values.
        """
        return {
            "Global": {
                "Effect Type": EditRegistry.readValue(
                    keyPath=Path.RegPaths.Global,
                    valueName=Path.RegKeys.EffectType,
                    defaultValue=Defaults.Global.effectType,
                    returnType=RegistryReturnType.Decimal,
                ),
                "Corner Type": EditRegistry.readValue(
                    keyPath=Path.RegPaths.Global,
                    valueName=Path.RegKeys.CornerType,
                    defaultValue=Defaults.Global.cornerType,
                    returnType=RegistryReturnType.Decimal,
                ),
                "Enable Drop Shadow": EditRegistry.readValue(
                    keyPath=Path.RegPaths.Global,
                    valueName=Path.RegKeys.EnableDropShadow,
                    defaultValue=Defaults.Global.enableDropShadow,
                    returnType=RegistryReturnType.Decimal,
                ),
                "No Border Color": EditRegistry.readValue(
                    keyPath=Path.RegPaths.Global,
                    valueName=Path.RegKeys.NoBorderColor,
                    defaultValue=Defaults.Global.noBorderColor,
                    returnType=RegistryReturnType.Decimal,
                ),
                "Enable Theme Colorization": EditRegistry.readValue(
                    keyPath=Path.RegPaths.Global,
                    valueName=Path.RegKeys.EnableThemeColorization,
                    defaultValue=Defaults.Global.enableThemeColorization,
                    returnType=RegistryReturnType.Decimal,
                ),
                "Dark Mode Border Color": EditRegistry.readValue(
                    keyPath=Path.RegPaths.Global,
                    valueName=Path.RegKeys.DarkModeBorderColor,
                    defaultValue=Defaults.Global.darkModeBorderColor,
                ),
                "Light Mode Border Color": EditRegistry.readValue(
                    keyPath=Path.RegPaths.Global,
                    valueName=Path.RegKeys.LightModeBorderColor,
                    defaultValue=Defaults.Global.lightModeBorderColor,
                ),
                "Dark Mode Gradient Color": EditRegistry.readValue(
                    keyPath=Path.RegPaths.Global,
                    valueName=Path.RegKeys.DarkModeGradientColor,
                    defaultValue=Defaults.Global.darkModeGradientColor,
                ),
                "Light Mode Gradient Color": EditRegistry.readValue(
                    keyPath=Path.RegPaths.Global,
                    valueName=Path.RegKeys.LightModeGradientColor,
                    defaultValue=Defaults.Global.lightModeGradientColor,
                ),
                "Disabled": EditRegistry.readValue(
                    keyPath=Path.RegPaths.Global,
                    valueName=Path.RegKeys.Disabled,
                    defaultValue=Defaults.Global.disabled,
                    returnType=RegistryReturnType.Decimal,
                ),
            },
            "DropDown": {
                "Effect Type": EditRegistry.readValue(
                    keyPath=Path.RegPaths.DropDown,
                    valueName=Path.RegKeys.EffectType,
                    defaultValue=Defaults.DropDown.effectType,
                    returnType=RegistryReturnType.Decimal,
                ),
                "Corner Type": EditRegistry.readValue(
                    keyPath=Path.RegPaths.DropDown,
                    valueName=Path.RegKeys.CornerType,
                    defaultValue=Defaults.DropDown.cornerType,
                    returnType=RegistryReturnType.Decimal,
                ),
                "Enable Drop Shadow": EditRegistry.readValue(
                    keyPath=Path.RegPaths.DropDown,
                    valueName=Path.RegKeys.EnableDropShadow,
                    defaultValue=Defaults.DropDown.enableDropShadow,
                    returnType=RegistryReturnType.Decimal,
                ),
                "No Border Color": EditRegistry.readValue(
                    keyPath=Path.RegPaths.DropDown,
                    valueName=Path.RegKeys.NoBorderColor,
                    defaultValue=Defaults.DropDown.noBorderColor,
                    returnType=RegistryReturnType.Decimal,
                ),
                "Enable Theme Colorization": EditRegistry.readValue(
                    keyPath=Path.RegPaths.DropDown,
                    valueName=Path.RegKeys.EnableThemeColorization,
                    defaultValue=Defaults.DropDown.enableThemeColorization,
                    returnType=RegistryReturnType.Decimal,
                ),
                "Dark Mode Border Color": EditRegistry.readValue(
                    keyPath=Path.RegPaths.DropDown,
                    valueName=Path.RegKeys.DarkModeBorderColor,
                    defaultValue=Defaults.DropDown.darkModeBorderColor,
                ),
                "Light Mode Border Color": EditRegistry.readValue(
                    keyPath=Path.RegPaths.DropDown,
                    valueName=Path.RegKeys.LightModeBorderColor,
                    defaultValue=Defaults.DropDown.lightModeBorderColor,
                ),
                "Dark Mode Gradient Color": EditRegistry.readValue(
                    keyPath=Path.RegPaths.DropDown,
                    valueName=Path.RegKeys.DarkModeGradientColor,
                    defaultValue=Defaults.DropDown.darkModeGradientColor,
                ),
                "Light Mode Gradient Color": EditRegistry.readValue(
                    keyPath=Path.RegPaths.DropDown,
                    valueName=Path.RegKeys.LightModeGradientColor,
                    defaultValue=Defaults.DropDown.lightModeGradientColor,
                ),
                "Disabled": EditRegistry.readValue(
                    keyPath=Path.RegPaths.DropDown,
                    valueName=Path.RegKeys.Disabled,
                    defaultValue=Defaults.DropDown.disabled,
                    returnType=RegistryReturnType.Decimal,
                ),
            },
            "Menu": {
                "No System Drop Shadow": EditRegistry.readValue(
                    keyPath=Path.RegPaths.Menu,
                    valueName=Path.RegKeys.NoSystemDropShadow,
                    defaultValue=Defaults.Menu.noSystemDropShadow,
                    returnType=RegistryReturnType.Decimal,
                ),
                "Enable Immersive Style": EditRegistry.readValue(
                    keyPath=Path.RegPaths.Menu,
                    valueName=Path.RegKeys.EnableImmersiveStyle,
                    defaultValue=Defaults.Menu.enableImmersiveStyle,
                    returnType=RegistryReturnType.Decimal,
                ),
                "Enable Custom Rendering": EditRegistry.readValue(
                    keyPath=Path.RegPaths.Menu,
                    valueName=Path.RegKeys.EnableCustomRendering,
                    defaultValue=Defaults.Menu.enableCustomRendering,
                    returnType=RegistryReturnType.Decimal,
                ),
                "Enable Fluent Animation": EditRegistry.readValue(
                    keyPath=Path.RegPaths.Menu,
                    valueName=Path.RegKeys.EnableFluentAnimation,
                    defaultValue=Defaults.Menu.enableFluentAnimation,
                    returnType=RegistryReturnType.Decimal,
                ),
                "No Modern App Background Color": EditRegistry.readValue(
                    keyPath=Path.RegPaths.Menu,
                    valueName=Path.RegKeys.NoModernAppBackgroundColor,
                    defaultValue=Defaults.Menu.noModernAppBackgroundColor,
                    returnType=RegistryReturnType.Decimal,
                ),
                "Color Treat As Transparent": EditRegistry.readValue(
                    keyPath=Path.RegPaths.Menu,
                    valueName=Path.RegKeys.ColorTreatAsTransparent,
                    defaultValue=Defaults.Menu.colorTreatAsTransparent,
                ),
                "Color Treat As Transparent Threshold": EditRegistry.readValue(
                    keyPath=Path.RegPaths.Menu,
                    valueName=Path.RegKeys.ColorTreatAsTransparentThreshold,
                    defaultValue=Defaults.Menu.colorTreatAsTransparentThreshold,
                    returnType=RegistryReturnType.Decimal,
                ),
                "Effect Type": EditRegistry.readValue(
                    keyPath=Path.RegPaths.Menu,
                    valueName=Path.RegKeys.EffectType,
                    defaultValue=Defaults.Menu.effectType,
                    returnType=RegistryReturnType.Decimal,
                ),
                "Corner Type": EditRegistry.readValue(
                    keyPath=Path.RegPaths.Menu,
                    valueName=Path.RegKeys.CornerType,
                    defaultValue=Defaults.Menu.cornerType,
                    returnType=RegistryReturnType.Decimal,
                ),
                "Enable Drop Shadow": EditRegistry.readValue(
                    keyPath=Path.RegPaths.Menu,
                    valueName=Path.RegKeys.EnableDropShadow,
                    defaultValue=Defaults.Menu.enableDropShadow,
                    returnType=RegistryReturnType.Decimal,
                ),
                "No Border Color": EditRegistry.readValue(
                    keyPath=Path.RegPaths.Menu,
                    valueName=Path.RegKeys.NoBorderColor,
                    defaultValue=Defaults.Menu.noBorderColor,
                    returnType=RegistryReturnType.Decimal,
                ),
                "Enable Theme Colorization": EditRegistry.readValue(
                    keyPath=Path.RegPaths.Menu,
                    valueName=Path.RegKeys.EnableThemeColorization,
                    defaultValue=Defaults.Menu.enableThemeColorization,
                    returnType=RegistryReturnType.Decimal,
                ),
                "Dark Mode Border Color": EditRegistry.readValue(
                    keyPath=Path.RegPaths.Menu,
                    valueName=Path.RegKeys.DarkModeBorderColor,
                    defaultValue=Defaults.Menu.darkModeBorderColor,
                ),
                "Light Mode Border Color": EditRegistry.readValue(
                    keyPath=Path.RegPaths.Menu,
                    valueName=Path.RegKeys.LightModeBorderColor,
                    defaultValue=Defaults.Menu.lightModeBorderColor,
                ),
                "Dark Mode Gradient Color": EditRegistry.readValue(
                    keyPath=Path.RegPaths.Menu,
                    valueName=Path.RegKeys.DarkModeGradientColor,
                    defaultValue=Defaults.Menu.darkModeGradientColor,
                ),
                "Light Mode Gradient Color": EditRegistry.readValue(
                    keyPath=Path.RegPaths.Menu,
                    valueName=Path.RegKeys.LightModeGradientColor,
                    defaultValue=Defaults.Menu.lightModeGradientColor,
                ),
                "Disabled": EditRegistry.readValue(
                    keyPath=Path.RegPaths.Menu,
                    valueName=Path.RegKeys.Disabled,
                    defaultValue=Defaults.Menu.disabled,
                    returnType=RegistryReturnType.Decimal,
                ),
                "Animation": {
                    "Fade Out Time": EditRegistry.readValue(
                        keyPath=Path.RegPaths.Menu + Path.RegPaths.Animation,
                        valueName=Path.RegKeys.FadeOutTime,
                        defaultValue=Defaults.Menu.Animation.fadeOutTime,
                        returnType=RegistryReturnType.Decimal,
                    ),
                    "Pop In Time": EditRegistry.readValue(
                        keyPath=Path.RegPaths.Menu + Path.RegPaths.Animation,
                        valueName=Path.RegKeys.PopInTime,
                        defaultValue=Defaults.Menu.Animation.popInTime,
                        returnType=RegistryReturnType.Decimal,
                    ),
                    "Fade In Time": EditRegistry.readValue(
                        keyPath=Path.RegPaths.Menu + Path.RegPaths.Animation,
                        valueName=Path.RegKeys.FadeInTime,
                        defaultValue=Defaults.Menu.Animation.fadeInTime,
                        returnType=RegistryReturnType.Decimal,
                    ),
                    "Pop In Style": EditRegistry.readValue(
                        keyPath=Path.RegPaths.Menu + Path.RegPaths.Animation,
                        valueName=Path.RegKeys.PopInStyle,
                        defaultValue=Defaults.Menu.Animation.popInStyle,
                        returnType=RegistryReturnType.Decimal,
                    ),
                    "Start Ratio": EditRegistry.readValue(
                        keyPath=Path.RegPaths.Menu + Path.RegPaths.Animation,
                        valueName=Path.RegKeys.StartRatio,
                        defaultValue=Defaults.Menu.Animation.startRatio,
                        returnType=RegistryReturnType.Decimal,
                    ),
                    "Enable Immediate Interupting": EditRegistry.readValue(
                        keyPath=Path.RegPaths.Menu + Path.RegPaths.Animation,
                        valueName=Path.RegKeys.EnableImmediateInterupting,
                        defaultValue=Defaults.Menu.Animation.enableImmediateInterupting,
                        returnType=RegistryReturnType.Decimal,
                    ),
                },
                "Disabled Hot": {
                    "Corner Radius": EditRegistry.readValue(
                        keyPath=Path.RegPaths.Menu + Path.RegPaths.DisabledHot,
                        valueName=Path.RegKeys.CornerRadius,
                        defaultValue=Defaults.Menu.DisabledHot.cornerRadius,
                        returnType=RegistryReturnType.Decimal,
                    ),
                    "Dark Mode Color": EditRegistry.readValue(
                        keyPath=Path.RegPaths.Menu + Path.RegPaths.DisabledHot,
                        valueName=Path.RegKeys.DarkModeColor,
                        defaultValue=Defaults.Menu.DisabledHot.darkModeColor,
                    ),
                    "Light Mode Color": EditRegistry.readValue(
                        keyPath=Path.RegPaths.Menu + Path.RegPaths.DisabledHot,
                        valueName=Path.RegKeys.LightModeColor,
                        defaultValue=Defaults.Menu.DisabledHot.lightModeColor,
                    ),
                    "Enable Theme Colorization": EditRegistry.readValue(
                        keyPath=Path.RegPaths.Menu + Path.RegPaths.DisabledHot,
                        valueName=Path.RegKeys.EnableThemeColorization,
                        defaultValue=Defaults.Menu.DisabledHot.enableThemeColorization,
                        returnType=RegistryReturnType.Decimal,
                    ),
                    "Disabled": EditRegistry.readValue(
                        keyPath=Path.RegPaths.Menu + Path.RegPaths.DisabledHot,
                        valueName=Path.RegKeys.Disabled,
                        defaultValue=Defaults.Menu.DisabledHot.disabled,
                        returnType=RegistryReturnType.Decimal,
                    ),
                },
                "Focusing": {
                    "Width": EditRegistry.readValue(
                        keyPath=Path.RegPaths.Menu + Path.RegPaths.Focusing,
                        valueName=Path.RegKeys.Width,
                        defaultValue=Defaults.Menu.Focusing.width,
                        returnType=RegistryReturnType.Decimal,
                    ),
                    "Corner Radius": EditRegistry.readValue(
                        keyPath=Path.RegPaths.Menu + Path.RegPaths.Focusing,
                        valueName=Path.RegKeys.CornerRadius,
                        defaultValue=Defaults.Menu.Focusing.cornerRadius,
                        returnType=RegistryReturnType.Decimal,
                    ),
                    "Dark Mode Color": EditRegistry.readValue(
                        keyPath=Path.RegPaths.Menu + Path.RegPaths.Focusing,
                        valueName=Path.RegKeys.DarkModeColor,
                        defaultValue=Defaults.Menu.Focusing.darkModeColor,
                    ),
                    "Light Mode Color": EditRegistry.readValue(
                        keyPath=Path.RegPaths.Menu + Path.RegPaths.Focusing,
                        valueName=Path.RegKeys.LightModeColor,
                        defaultValue=Defaults.Menu.Focusing.lightModeColor,
                    ),
                    "Enable Theme Colorization": EditRegistry.readValue(
                        keyPath=Path.RegPaths.Menu + Path.RegPaths.Focusing,
                        valueName=Path.RegKeys.EnableThemeColorization,
                        defaultValue=Defaults.Menu.Focusing.enableThemeColorization,
                        returnType=RegistryReturnType.Decimal,
                    ),
                    "Disabled": EditRegistry.readValue(
                        keyPath=Path.RegPaths.Menu + Path.RegPaths.Focusing,
                        valueName=Path.RegKeys.Disabled,
                        defaultValue=Defaults.Menu.Focusing.disabled,
                        returnType=RegistryReturnType.Decimal,
                    ),
                },
                "Hot": {
                    "Corner Radius": EditRegistry.readValue(
                        keyPath=Path.RegPaths.Menu + Path.RegPaths.Hot,
                        valueName=Path.RegKeys.CornerRadius,
                        defaultValue=Defaults.Menu.Hot.cornerRadius,
                        returnType=RegistryReturnType.Decimal,
                    ),
                    "Dark Mode Color": EditRegistry.readValue(
                        keyPath=Path.RegPaths.Menu + Path.RegPaths.Hot,
                        valueName=Path.RegKeys.DarkModeColor,
                        defaultValue=Defaults.Menu.Hot.darkModeColor,
                    ),
                    "Light Mode Color": EditRegistry.readValue(
                        keyPath=Path.RegPaths.Menu + Path.RegPaths.Hot,
                        valueName=Path.RegKeys.LightModeColor,
                        defaultValue=Defaults.Menu.Hot.lightModeColor,
                    ),
                    "Enable Theme Colorization": EditRegistry.readValue(
                        keyPath=Path.RegPaths.Menu + Path.RegPaths.Hot,
                        valueName=Path.RegKeys.EnableThemeColorization,
                        defaultValue=Defaults.Menu.Hot.enableThemeColorization,
                        returnType=RegistryReturnType.Decimal,
                    ),
                    "Disabled": EditRegistry.readValue(
                        keyPath=Path.RegPaths.Menu + Path.RegPaths.Hot,
                        valueName=Path.RegKeys.Disabled,
                        defaultValue=Defaults.Menu.Hot.disabled,
                        returnType=RegistryReturnType.Decimal,
                    ),
                },
                "Separator": {
                    "Width": EditRegistry.readValue(
                        keyPath=Path.RegPaths.Menu + Path.RegPaths.Separator,
                        valueName=Path.RegKeys.Width,
                        defaultValue=Defaults.Menu.Separator.width,
                        returnType=RegistryReturnType.Decimal,
                    ),
                    "Corner Radius": EditRegistry.readValue(
                        keyPath=Path.RegPaths.Menu + Path.RegPaths.Separator,
                        valueName=Path.RegKeys.CornerRadius,
                        defaultValue=Defaults.Menu.Separator.cornerRadius,
                        returnType=RegistryReturnType.Decimal,
                    ),
                    "Dark Mode Color": EditRegistry.readValue(
                        keyPath=Path.RegPaths.Menu + Path.RegPaths.Separator,
                        valueName=Path.RegKeys.DarkModeColor,
                        defaultValue=Defaults.Menu.Separator.darkModeColor,
                    ),
                    "Light Mode Color": EditRegistry.readValue(
                        keyPath=Path.RegPaths.Menu + Path.RegPaths.Separator,
                        valueName=Path.RegKeys.LightModeColor,
                        defaultValue=Defaults.Menu.Separator.lightModeColor,
                    ),
                    "Enable Theme Colorization": EditRegistry.readValue(
                        keyPath=Path.RegPaths.Menu + Path.RegPaths.Separator,
                        valueName=Path.RegKeys.EnableThemeColorization,
                        defaultValue=Defaults.Menu.Separator.enableThemeColorization,
                        returnType=RegistryReturnType.Decimal,
                    ),
                    "Disabled": EditRegistry.readValue(
                        keyPath=Path.RegPaths.Menu + Path.RegPaths.Separator,
                        valueName=Path.RegKeys.Disabled,
                        defaultValue=Defaults.Menu.Separator.disabled,
                        returnType=RegistryReturnType.Decimal,
                    ),
                },
            },
            "Tooltip": {
                "Effect Type": EditRegistry.readValue(
                    keyPath=Path.RegPaths.Tooltip,
                    valueName=Path.RegKeys.EffectType,
                    defaultValue=Defaults.Tooltip.effectType,
                    returnType=RegistryReturnType.Decimal,
                ),
                "Corner Type": EditRegistry.readValue(
                    keyPath=Path.RegPaths.Tooltip,
                    valueName=Path.RegKeys.CornerType,
                    defaultValue=Defaults.Tooltip.cornerType,
                    returnType=RegistryReturnType.Decimal,
                ),
                "Enable Drop Shadow": EditRegistry.readValue(
                    keyPath=Path.RegPaths.Tooltip,
                    valueName=Path.RegKeys.EnableDropShadow,
                    defaultValue=Defaults.Tooltip.enableDropShadow,
                    returnType=RegistryReturnType.Decimal,
                ),
                "No Border Color": EditRegistry.readValue(
                    keyPath=Path.RegPaths.Tooltip,
                    valueName=Path.RegKeys.NoBorderColor,
                    defaultValue=Defaults.Tooltip.noBorderColor,
                    returnType=RegistryReturnType.Decimal,
                ),
                "Enable Theme Colorization": EditRegistry.readValue(
                    keyPath=Path.RegPaths.Tooltip,
                    valueName=Path.RegKeys.EnableThemeColorization,
                    defaultValue=Defaults.Tooltip.enableThemeColorization,
                    returnType=RegistryReturnType.Decimal,
                ),
                "Dark Mode Border Color": EditRegistry.readValue(
                    keyPath=Path.RegPaths.Tooltip,
                    valueName=Path.RegKeys.DarkModeBorderColor,
                    defaultValue=Defaults.Tooltip.darkModeBorderColor,
                ),
                "Light Mode Border Color": EditRegistry.readValue(
                    keyPath=Path.RegPaths.Tooltip,
                    valueName=Path.RegKeys.LightModeBorderColor,
                    defaultValue=Defaults.Tooltip.lightModeBorderColor,
                ),
                "Dark Mode Gradient Color": EditRegistry.readValue(
                    keyPath=Path.RegPaths.Tooltip,
                    valueName=Path.RegKeys.DarkModeGradientColor,
                    defaultValue=Defaults.Tooltip.darkModeGradientColor,
                ),
                "Light Mode Gradient Color": EditRegistry.readValue(
                    keyPath=Path.RegPaths.Tooltip,
                    valueName=Path.RegKeys.LightModeGradientColor,
                    defaultValue=Defaults.Tooltip.lightModeGradientColor,
                ),
                "Disabled": EditRegistry.readValue(
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
        except:
            pass

    @staticmethod
    def setValue(
        keyPath: Path.RegPaths | str,
        valueName: str,
        value: str | int,
    ):
        """
        This Method:
        - Sets the value of the provided key
        - keyPath: is the path to the key under which the subkey lies, which will contain the value
        - subKey: is the key which needs a value to be set
        - value: is the value of the subkey, which needs a value to be set
        """
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
            REG_DWORD,
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
        except:
            pass

    @staticmethod
    def readValue(
        keyPath: Path.RegPaths | str,
        valueName: str,
        defaultValue: str | int,
        returnType: RegistryReturnType = RegistryReturnType.Hexadecimal,
    ) -> str | int:
        """
        Reads a value from the registry.
        - keyPath: The path to the registry key.
        - valueName: The name of the value to read.
        """

        try:
            key = OpenKeyEx(
                key=Path.RegKeys.BaseKey,
                sub_key=str(Path.RegPaths.BasePath + str(keyPath)),
                reserved=0,
                access=KEY_READ,
            )
            value, _ = QueryValueEx(key, valueName)
            if key:
                CloseKey(key)
            if returnType == RegistryReturnType.Hexadecimal:
                return hex(value)[2:].upper()
            else:
                return int(value)
        except:
            return defaultValue

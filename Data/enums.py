from enum import IntEnum


class Settings:
    """
    Setttings Enum for various settings parameters
    """

    class EffectType(IntEnum):
        Disabled = 0
        FullyTransparent = 1
        SolidColor = 2
        Blurred = 3
        Acrylic = 4
        ModernAcrylic = 5
        AcrylicBackgroundLayer = 6
        MicaBackgroundLayer = 7
        MicaVariantBackgroundLayer = 8
        UseGlobalSetting = 9

    class ThemeColorizationType(IntEnum):
        ImmersiveStartBackground = 0
        ImmersiveStartHoverBackground = 1
        ImmersiveSystemAccent = 2
        ImmersiveSystemAccentDark1 = 3
        ImmersiveSystemAccentDark2 = 4
        ImmersiveSystemAccentDark3 = 5
        ImmersiveSystemAccentLight1 = 6
        ImmersiveSystemAccentLight2 = 7
        ImmersiveSystemAccentLight3 = 8

    class EnableMiniDump(IntEnum):
        No = 0
        Yes = 1

    class EnableCompatibilityMode(IntEnum):
        No = 0
        Yes = 1

    class MarginsType(IntEnum):
        AddToExisting = 0
        ReplaceExisting = 1

    class EnableDropShadow(IntEnum):
        No = 0
        Yes = 1
        UseGlobalSetting = 2

    class NoSystemDropShadow(IntEnum):
        No = 0
        Yes = 1

    class Disabled(IntEnum):
        No = 0
        Yes = 1
        UseGlobalSetting = 2

    class EnableImmersiveStyle(IntEnum):
        No = 0
        Yes = 1

    class EnableFluentAnimation(IntEnum):
        No = 0
        Yes = 1

    class NoModernAppBackgroundColor(IntEnum):
        No = 0
        Yes = 1

    class EnableCustomRendering(IntEnum):
        No = 0
        Yes = 1

    class EnableThemeColorization(IntEnum):
        No = 0
        Yes = 1
        UseGlobalSetting = 2

    class EnableImmediateInterupting(IntEnum):
        No = 0
        Yes = 1

    class NoBorderColor(IntEnum):
        No = 0
        Yes = 1
        UseGlobalSetting = 2

    class CornerType(IntEnum):
        DontChange = 0
        Square = 1
        LargeRound = 2
        SmallRound = 3
        UseGlobalSetting = 4

    class PopInStyle(IntEnum):
        SlideDown = 0
        Ripple = 1
        SmoothScroll = 2
        SmoothZoom = 3


class Languages(IntEnum):
    Default = 0
    Hindi = 1
    SimplifiedChinese = 2


class IconType(IntEnum):
    Light = 0
    Dark = 1


class MainTab(IntEnum):
    """
    Returns the tab indices in the main tab
    """

    Global = 0
    DropDown = 1
    Menu = 2
    Tooltip = 3


class DropDownTab(IntEnum):
    """
    Returns the tab indices in the dropdown tab
    """

    General = 0
    Animation = 1


class MenuTab(IntEnum):
    """
    Returns the tab indices in the menu tab
    """

    General = 0
    Animation = 1
    Hot = 2
    DisabledHot = 3
    Focusing = 4
    Separator = 5


class InfoWidgetHeight(IntEnum):
    FiveItems = 320
    FourItems = 220
    TwoItems = 200
    TextShort = 120


class RegistryReturnType(IntEnum):
    """
    Return Type Enum for Registry value fetching
    """

    Hexadecimal = 0
    Decimal = 1
    String = 2
    List = 3


class Presets(IntEnum):
    """
    Preset Enums have presets for various combinations of settings that modify
    the appearance of transparent flyouts
    """

    Null = 0
    # Add More Presets


class ListType(IntEnum):
    GlobalDisabledList = 0
    GlobalBlockList = 1
    DropDownDisabledList = 2
    MenuDisabledList = 3
    TooltipDisabledList = 4


class EnumConvert:
    @staticmethod
    def themeColorizationTypeToName(
        colorIndex: Settings.ThemeColorizationType | int,
    ) -> str:
        """
        Convert ThemeColorizationType to its name in string format

        Args:
            colorIndex (Settings.ThemeColorizationType | int): Enum or comboBox index

        Returns:
            str: Theme Colorization Type name as string
        """
        return list(Settings.ThemeColorizationType)[colorIndex].name

    @staticmethod
    def themeColorizationTypeStringToIndex(
        value: str | int | list[str] | Settings.ThemeColorizationType,
    ) -> int:
        """
        Convert Theme Colorization Type string to the index in the comboBox

        Args:
            value (str | int | list[str] | Settings.ThemeColorizationType): Theme Colorization type

        Returns:
            int: index of the Theme Colorization Type string in the corresponding comboBox
        """
        if isinstance(value, int):
            return value

        elif isinstance(value, str):
            return list(
                map(lambda typ: typ.name, Settings.ThemeColorizationType)
            ).index(value)
        else:
            return 1

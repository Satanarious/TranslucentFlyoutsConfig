# Library imports
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


class MainTab(IntEnum):
    """
    Returns the tab indices in the main tab
    """

    Global = 0
    DropDown = 1
    Menu = 2
    Tooltip = 3


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


class Presets(IntEnum):
    """
    Preset Enums have presets for various combinations of settings that modify
    the appearance of transparent flyouts
    """

    Null = 0
    # Add More Presets

# Library imports
from enum import Enum, IntEnum


class Settings:
    """
    Setttings Enum for various settings parameters
    """

    class Scope(IntEnum):
        Global = 0
        Individual = 1

    class EffectType(IntEnum):
        Disable = 0
        Transparent = 1
        Solid = 2
        Blur = 3
        ClassicAcrylicBlur = 4
        ModernAcrylicBlur = 5
        Acrylic = 6
        Mica = 7
        MicaAlt = 8

    class EnableDropShadow(IntEnum):
        No = 0
        Yes = 1

    class Disabled(IntEnum):
        No = 1
        Yes = 2

    class NoSystemOutline(IntEnum):
        No = 0
        Yes = 1

    class EnableImmersiveStyle(IntEnum):
        No = 0
        Yes = 1

    class CustomRendering(IntEnum):
        No = 0
        Yes = 1

    class EnableThemeCustomization(IntEnum):
        No = 0
        Yes = 1

    class NoBorderColor(IntEnum):
        No = 0
        Yes = 1

    class CornerType(IntEnum):
        Small = 0
        Square = 1
        Large = 2


class Unsupported(IntEnum):
    """
    Unsupported Enum indicates unsupported versions of windows
    """

    Null = 0
    Win10 = 10
    Win11 = 11


class Presets(IntEnum):
    """
    Preset Enums have presets for various combinations of settings that modify
    the appearance of transparent flyouts
    """

    Null = 0
    # Add More Presets


class IconPaths(Enum):
    ResetIcon = "Assets/View-refresh.svg.png"
    ColorPicker = "Assets/2867978.png"

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

    class EnableDropShadow(IntEnum):
        No = 0
        Yes = 1

    class NoSystemDropShadow(IntEnum):
        No = 0
        Yes = 1

    class Disabled(IntEnum):
        No = 0
        Yes = 1

    class EnableImmersiveStyle(IntEnum):
        No = 0
        Yes = 1

    class EnableFluentAnimation(IntEnum):
        No = 0
        Yes = 1

    class EnableCustomRendering(IntEnum):
        No = 0
        Yes = 1

    class EnableThemeColorization(IntEnum):
        No = 0
        Yes = 1

    class EnableImmediateInterupting(IntEnum):
        No = 0
        Yes = 1

    class NoBorderColor(IntEnum):
        No = 0
        Yes = 1

    class CornerType(IntEnum):
        DontChange = 0
        Square = 1
        LargeRound = 2
        SmallRound = 3

    class PopInStyle(IntEnum):
        SlideDown = 0
        Ripple = 1
        SmoothScroll = 2
        SmoothZoom = 3


class Presets(IntEnum):
    """
    Preset Enums have presets for various combinations of settings that modify
    the appearance of transparent flyouts
    """

    Null = 0
    # Add More Presets

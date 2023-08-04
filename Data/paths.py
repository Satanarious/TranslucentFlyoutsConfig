from winreg import HKEY_CURRENT_USER


class Path:
    class IconPaths:
        ResetIcon = "Assets/View-refresh.svg.png"
        ColorPicker = "Assets/2867978.png"

    class RegPaths:
        BasePath = r"Software\\TranslucentFlyouts\\"
        Software = r"Software\\"
        TranslucentFlyouts = r"TranslucentFlyouts\\"
        DropDown = r"DropDown\\"
        Menu = r"Menu\\"
        Hot = r"Hot\\"
        DisabledHot = r"DisabledHot\\"
        Focusing = r"Focusing\\"
        Border = r"Border\\"
        Separator = r"Separator\\"

    class RegKeys:
        BaseKey = HKEY_CURRENT_USER
        EffectType = "EffectType"
        EnableDropShadow = "EnableDropShadow"
        DarkMode_GradientColor = "DarkMode_GradientColor"
        LightMode_GradientColor = "LightMode_GradientColor"
        DarkMode_Opacity = "DarkMode_Opacity"
        LightMode_Opacity = "LightMode_Opacity"
        Disabled = "Disabled"
        NoSystemOutline = "NoSystemOutline"
        EnableImmersiveStyle = "EnableImmersiveStyle"
        EnableCustomRendering = "EnableCustomRendering"
        CornerRadius = "CornerRadius"
        EnableThemeColorization = "EnableThemeColorization"
        NoBorderColor = "NoBorderColor"
        CornerType = "CornerType"

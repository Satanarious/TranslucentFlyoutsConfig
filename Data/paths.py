from winreg import HKEY_CURRENT_USER


class Path:
    class IconPaths:
        ResetIcon: str = "Assets/View-refresh.svg.png"
        ColorPicker: str = "Assets/2867978.png"

    class RegPaths:
        BasePath: str = r"Software\\TranslucentFlyouts\\"
        Software: str = r"Software\\"
        TranslucentFlyouts: str = r"TranslucentFlyouts\\"
        General: str = ""
        DropDown: str = r"DropDown\\"
        Menu: str = r"Menu\\"
        Animation: str = r"Animation\\"
        Hot: str = r"Hot\\"
        DisabledHot: str = r"DisabledHot\\"
        Focusing: str = r"Focusing\\"
        Separator: str = r"Separator\\"

    class RegKeys:
        BaseKey: int = HKEY_CURRENT_USER
        EffectType: str = "EffectType"
        EnableDropShadow: str = "EnableDropShadow"
        DarkModeBorderColor: str = "DarkMode_BorderColor"
        LightModeBorderColor: str = "LightMode_BorderColor"
        DarkModeGradientColor: str = "DarkMode_GradientColor"
        LightModeGradientColor: str = "LightMode_GradientColor"
        DarkModeColor: str = "DarkMode_Color"
        LightModeColor: str = "LightMode_Color"
        Disabled: str = "Disabled"
        NoSystemDropShadow: str = "NoSystemDropShadow"
        EnableImmersiveStyle: str = "EnableImmersiveStyle"
        EnableCustomRendering: str = "EnableCustomRendering"
        EnableFluentAnimation: str = "EnableFluentAnimation"
        FadeOutTime: str = "FadeOutTime"
        PopInTime: str = "PopInTime"
        FadeInTime: str = "FadeInTime"
        PopInStyle: str = "PopInStyle"
        StartRatio: str = "StartRatio"
        EnableImmediateInterupting: str = "EnableImmediateInterupting"
        CornerRadius: str = "CornerRadius"
        EnableThemeColorization: str = "EnableThemeColorization"
        NoBorderColor: str = "NoBorderColor"
        CornerType: str = "CornerType"
        Width: str = "Width"

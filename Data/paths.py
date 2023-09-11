from winreg import HKEY_CURRENT_USER


class Path:
    class DBPaths:
        Defaults = "Assets/db/defaults.json"
        UserSettings = "Assets/db/user_settings.json"

    class IconPaths:
        ResetIcon: str = "Assets/icons/reset_icon.png"
        ColorPicker: str = "Assets/icons/color_picker_icon.png"
        Logo: str = "Assets/icons/logo.png"
        MinimizeIcon: str = "Assets/icons/minimize_icon.png"
        UpArrow: str = "Assets/icons/up-arrow.png"
        DownArrow: str = "Assets/icons/down-arrow.png"
        CloseIcon: str = "Assets/icons/close_icon.png"

    class FontPaths:
        NunitoSans: str = "Assets/fonts/NunitoSans_10pt_Condensed-Regular.ttf"
        AndikaRegular: str = "Assets/fonts/Andika-Regular.ttf"

    class RegPaths:
        BasePath: str = r"Software\\TranslucentFlyouts\\"
        Software: str = r"Software\\"
        TranslucentFlyouts: str = r"TranslucentFlyouts\\"
        Global: str = ""
        DropDown: str = r"DropDown\\"
        Menu: str = r"Menu\\"
        Animation: str = r"Animation\\"
        Hot: str = r"Hot\\"
        DisabledHot: str = r"DisabledHot\\"
        Focusing: str = r"Focusing\\"
        Separator: str = r"Separator\\"
        Tooltip: str = r"Tooltip\\"

    class RegKeys:
        BaseKey: int = HKEY_CURRENT_USER
        TranslucentFlyouts: str = "TranslucentFlyouts"
        DropDown: str = "DropDown"
        Menu: str = "Menu"
        Animation: str = "Animation"
        Hot: str = "Hot"
        DisabledHot: str = "DisabledHot"
        Focusing: str = "Focusing"
        Separator: str = "Separator"
        Tooltip: str = "Tooltip"
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
        NoModernAppBackgroundColor: str = "NoModernAppBackgroundColor"
        ColorTreatAsTransparent: str = "ColorTreatAsTransparent"
        ColorTreatAsTransparentThreshold: str = "ColorTreatAsTransparentThreshold"
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

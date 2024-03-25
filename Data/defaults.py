import json

DBPath = "./Assets/db/defaults.json"
rawDefaults: dict = dict(json.load(open(DBPath, "r")))


# Keys from JSON file
class Key:
    _global: str = "Global"
    dropdown: str = "DropDown"
    menu: str = "Menu"
    animation: str = "Animation"
    disabledHot: str = "Disabled Hot"
    focusing: str = "Focusing"
    hot: str = "Hot"
    separator: str = "Separator"
    tooltip: str = "Tooltip"
    effectType: str = "Effect Type"
    cornerType: str = "Corner Type"
    enableDropShadow: str = "Enable Drop Shadow"
    noBorderColor: str = "No Border Color"
    darkModeBorderColor: str = "Dark Mode Border Color"
    lightModeBorderColor: str = "Light Mode Border Color"
    darkModeGradientColor: str = "Dark Mode Gradient Color"
    lightModeGradientColor: str = "Light Mode Gradient Color"
    enableMiniDump: str = "Enable Mini Dump"
    disabled: str = "Disabled"
    enableCompatibilityMode: str = "Enable Compatibility Mode"
    noSystemDropShadow: str = "No System Drop Shadow"
    enableImmersiveStyle: str = "Enable Immersive Style"
    enableCustomRendering: str = "Enable Custom Rendering"
    enableFluentAnimation: str = "Enable Fluent Animation"
    noModernAppBackgroundColor: str = "No Modern App Background Color"
    colorTreatAsTransparent: str = "Color Treat As Transparent"
    colorTreatAsTransparentThreshold: str = "Color Treat As Transparent Threshold"
    darkModeThemeColorizationType: str = "Dark Mode Theme Colorization Type"
    lightModeThemeColorizationType: str = "Light Mode Theme Colorization Type"
    textColor: str = "Text Color"
    borderColor: str = "Border Color"
    gradientColor: str = "Gradient Color"
    fadeOutTime: str = "Fade Out Time"
    popInTime: str = "Pop In Time"
    fadeInTime: str = "Fade In Time"
    popInStyle: str = "Pop In Style"
    startRatio: str = "Start Ratio"
    enableImmediateInterupting: str = "Enable Immediate Interupting"
    cornerRadius: str = "Corner Radius"
    darkModeColor: str = "Dark Mode Color"
    lightModeColor: str = "Light Mode Color"
    enableThemeColorization: str = "Enable Theme Colorization"
    width: str = "Width"
    marginsType: str = "Margins Type"
    margin: str = "Margin"
    marginLeft: str = "Margin Left"
    marginRight: str = "Margin Right"
    marginTop: str = "Margin Top"
    marginBottom: str = "Margin Bottom"
    disabledList: str = "Disabled List"
    blockList: str = "Block List"


# Getter Classes
class Defaults:
    class Global:
        effectType: int = rawDefaults[Key._global][Key.effectType]
        cornerType: int = rawDefaults[Key._global][Key.cornerType]
        enableDropShadow: int = rawDefaults[Key._global][Key.enableDropShadow]
        noBorderColor: int = rawDefaults[Key._global][Key.noBorderColor]
        enableThemeColorization: int = rawDefaults[Key._global][
            Key.enableThemeColorization
        ]
        darkModeThemeColorizationType: int = rawDefaults[Key._global][
            Key.darkModeThemeColorizationType
        ]
        lightModeThemeColorizationType: int = rawDefaults[Key._global][
            Key.lightModeThemeColorizationType
        ]
        darkModeBorderColor: str = rawDefaults[Key._global][Key.darkModeBorderColor]
        lightModeBorderColor: str = rawDefaults[Key._global][Key.lightModeBorderColor]
        darkModeGradientColor: str = rawDefaults[Key._global][Key.darkModeGradientColor]
        lightModeGradientColor: str = rawDefaults[Key._global][
            Key.lightModeGradientColor
        ]
        enableMiniDump: str = rawDefaults[Key._global][Key.enableMiniDump]
        disabledList: list = rawDefaults[Key._global][Key.disabledList]
        blockList: list = rawDefaults[Key._global][Key.blockList]
        disabled: int = rawDefaults[Key._global][Key.disabled]

    class DropDown:
        effectType: int = rawDefaults[Key.dropdown][Key.effectType]
        cornerType: int = rawDefaults[Key.dropdown][Key.cornerType]
        enableDropShadow: int = rawDefaults[Key.dropdown][Key.enableDropShadow]
        noBorderColor: int = rawDefaults[Key.dropdown][Key.noBorderColor]
        enableFluentAnimation: int = rawDefaults[Key.dropdown][
            Key.enableFluentAnimation
        ]
        enableThemeColorization: int = rawDefaults[Key.dropdown][
            Key.enableThemeColorization
        ]
        darkModeBorderColor: str = rawDefaults[Key.dropdown][Key.darkModeBorderColor]
        lightModeBorderColor: str = rawDefaults[Key.dropdown][Key.lightModeBorderColor]
        darkModeGradientColor: str = rawDefaults[Key.dropdown][
            Key.darkModeGradientColor
        ]
        lightModeGradientColor: str = rawDefaults[Key.dropdown][
            Key.lightModeGradientColor
        ]
        disabledList: list = rawDefaults[Key.dropdown][Key.disabledList]
        disabled: int = rawDefaults[Key.dropdown][Key.disabled]

        class Animation:
            fadeOutTime: int = rawDefaults[Key.dropdown][Key.animation][Key.fadeOutTime]
            popInTime: int = rawDefaults[Key.dropdown][Key.animation][Key.popInTime]
            fadeInTime: int = rawDefaults[Key.dropdown][Key.animation][Key.fadeInTime]
            popInStyle: int = rawDefaults[Key.dropdown][Key.animation][Key.popInStyle]
            startRatio: int = rawDefaults[Key.dropdown][Key.animation][Key.startRatio]
            enableImmediateInterupting: int = rawDefaults[Key.dropdown][Key.animation][
                Key.enableImmediateInterupting
            ]

    class Menu:
        noSystemDropShadow: int = rawDefaults[Key.menu][Key.noSystemDropShadow]
        enableImmersiveStyle: int = rawDefaults[Key.menu][Key.enableImmersiveStyle]
        enableCustomRendering: int = rawDefaults[Key.menu][Key.enableCustomRendering]
        enableFluentAnimation: int = rawDefaults[Key.menu][Key.enableFluentAnimation]
        noModernAppBackgroundColor: int = rawDefaults[Key.menu][
            Key.noModernAppBackgroundColor
        ]
        colorTreatAsTransparent: str = rawDefaults[Key.menu][
            Key.colorTreatAsTransparent
        ]
        colorTreatAsTransparentThreshold: int = rawDefaults[Key.menu][
            Key.colorTreatAsTransparentThreshold
        ]
        effectType: int = rawDefaults[Key.menu][Key.effectType]
        cornerType: int = rawDefaults[Key.menu][Key.cornerType]
        enableDropShadow: int = rawDefaults[Key.menu][Key.enableDropShadow]
        noBorderColor: int = rawDefaults[Key.menu][Key.noBorderColor]
        enableCompatibilityMode: int = rawDefaults[Key.menu][
            Key.enableCompatibilityMode
        ]
        enableThemeColorization: int = rawDefaults[Key.menu][
            Key.enableThemeColorization
        ]
        darkModeThemeColorizationType: str = rawDefaults[Key.menu][
            Key.darkModeThemeColorizationType
        ]
        lightModeThemeColorizationType: str = rawDefaults[Key.menu][
            Key.lightModeThemeColorizationType
        ]
        darkModeBorderColor: str = rawDefaults[Key.menu][Key.darkModeBorderColor]
        lightModeBorderColor: str = rawDefaults[Key.menu][Key.lightModeBorderColor]
        darkModeGradientColor: str = rawDefaults[Key.menu][Key.darkModeGradientColor]
        lightModeGradientColor: str = rawDefaults[Key.menu][Key.lightModeGradientColor]
        disabledList: list = rawDefaults[Key.menu][Key.disabledList]
        disabled: int = rawDefaults[Key.menu][Key.disabled]

        class Animation:
            fadeOutTime: int = rawDefaults[Key.menu][Key.animation][Key.fadeOutTime]
            popInTime: int = rawDefaults[Key.menu][Key.animation][Key.popInTime]
            fadeInTime: int = rawDefaults[Key.menu][Key.animation][Key.fadeInTime]
            popInStyle: int = rawDefaults[Key.menu][Key.animation][Key.popInStyle]
            startRatio: int = rawDefaults[Key.menu][Key.animation][Key.startRatio]
            enableImmediateInterupting: int = rawDefaults[Key.menu][Key.animation][
                Key.enableImmediateInterupting
            ]

        class DisabledHot:
            cornerRadius: int = rawDefaults[Key.menu][Key.disabledHot][Key.cornerRadius]
            darkModeColor: str = rawDefaults[Key.menu][Key.disabledHot][
                Key.darkModeColor
            ]
            lightModeColor: str = rawDefaults[Key.menu][Key.disabledHot][
                Key.lightModeColor
            ]
            enableThemeColorization: int = rawDefaults[Key.menu][Key.disabledHot][
                Key.enableThemeColorization
            ]
            disabled: int = rawDefaults[Key.menu][Key.disabledHot][Key.disabled]

        class Focusing:
            width: int = rawDefaults[Key.menu][Key.focusing][Key.width]
            cornerRadius: int = rawDefaults[Key.menu][Key.focusing][Key.cornerRadius]
            darkModeColor: str = rawDefaults[Key.menu][Key.focusing][Key.darkModeColor]
            lightModeColor: str = rawDefaults[Key.menu][Key.focusing][
                Key.lightModeColor
            ]
            enableThemeColorization: int = rawDefaults[Key.menu][Key.focusing][
                Key.enableThemeColorization
            ]
            disabled: int = rawDefaults[Key.menu][Key.focusing][Key.disabled]

        class Hot:
            cornerRadius: int = rawDefaults[Key.menu][Key.hot][Key.cornerRadius]
            darkModeColor: str = rawDefaults[Key.menu][Key.hot][Key.darkModeColor]
            lightModeColor: str = rawDefaults[Key.menu][Key.hot][Key.lightModeColor]
            enableThemeColorization: int = rawDefaults[Key.menu][Key.hot][
                Key.enableThemeColorization
            ]
            disabled: int = rawDefaults[Key.menu][Key.hot][Key.disabled]

        class Separator:
            width: int = rawDefaults[Key.menu][Key.separator][Key.width]
            cornerRadius: int = rawDefaults[Key.menu][Key.separator][Key.cornerRadius]
            darkModeColor: str = rawDefaults[Key.menu][Key.separator][Key.darkModeColor]
            lightModeColor: str = rawDefaults[Key.menu][Key.separator][
                Key.lightModeColor
            ]
            enableThemeColorization: int = rawDefaults[Key.menu][Key.separator][
                Key.enableThemeColorization
            ]
            disabled: int = rawDefaults[Key.menu][Key.separator][Key.disabled]

    class Tooltip:
        effectType: int = rawDefaults[Key.tooltip][Key.effectType]
        cornerType: int = rawDefaults[Key.tooltip][Key.cornerType]
        enableDropShadow: int = rawDefaults[Key.tooltip][Key.enableDropShadow]
        noBorderColor: int = rawDefaults[Key.tooltip][Key.noBorderColor]
        enableThemeColorization: int = rawDefaults[Key.tooltip][
            Key.enableThemeColorization
        ]
        marginsType: int = rawDefaults[Key.tooltip][Key.marginsType]
        marginLeft: int = rawDefaults[Key.tooltip][Key.marginLeft]
        marginRight: int = rawDefaults[Key.tooltip][Key.marginRight]
        marginTop: int = rawDefaults[Key.tooltip][Key.marginTop]
        marginBottom: int = rawDefaults[Key.tooltip][Key.marginBottom]
        darkModeColor: str = rawDefaults[Key.tooltip][Key.darkModeColor]
        lightModeColor: str = rawDefaults[Key.tooltip][Key.lightModeColor]
        darkModeBorderColor: str = rawDefaults[Key.tooltip][Key.darkModeBorderColor]
        lightModeBorderColor: str = rawDefaults[Key.tooltip][Key.lightModeBorderColor]
        darkModeGradientColor: str = rawDefaults[Key.tooltip][Key.darkModeGradientColor]
        lightModeGradientColor: str = rawDefaults[Key.tooltip][
            Key.lightModeGradientColor
        ]
        disabledList: list = rawDefaults[Key.tooltip][Key.disabledList]
        disabled: int = rawDefaults[Key.tooltip][Key.disabled]

# Library Imports
import json

rawDefaults: dict = dict(json.load(open("defaults.json", "r")))

# Keys from JSON file
default = "default"
unsupported = "unsupported"
general = "General"
dropdown = "DropDown"
menu = "Menu"
menuItems = "Menu Items"
hot = "Hot"
disabledHot = "Disabled Hot"
focusing = "Focusing"
border = "Border"
separator = "Separator"
tooltip = "Tooltip"
scope = "Scope"
effectType = "Effect Type"
enableDropShadow = "Enable Drop Shadow"
darkModeGradientColor = "Dark Mode Gradient Color"
lightModeGradientColor = "Light Mode Gradient Color"
darkModeOpacity = "Dark Mode Opacity"
lightModeOpacity = "Light Mode Opacity"
disabled = "Disabled"
noSystemOutline = "No System Outline"
enableImmersiveStyle = "Enable Immersive Style"
enableCustomRendering = "Enable Custom Rendering"
cornerRadius = "Corner Radius"
enableThemeCustomization = "Enable Theme Customization"
noBorderColor = "No Border Color"
cornerType = "Corner Type"


# Getter Classes
class Defaults:
    class General:
        class Scope:
            Default: int = rawDefaults[general][scope][default]
            Unsupported: int = rawDefaults[general][scope][unsupported]

        class EffectType:
            Default: int = rawDefaults[general][effectType][default]
            Unsupported: int = rawDefaults[general][effectType][unsupported]

        class EnableDropShadow:
            Default: int = rawDefaults[general][enableDropShadow][default]
            Unsupported: int = rawDefaults[general][enableDropShadow][unsupported]

        class DarkModeGradientColor:
            Default: int = rawDefaults[general][darkModeGradientColor][default]
            Unsupported: int = rawDefaults[general][darkModeGradientColor][unsupported]

        class LightModeGradientColor:
            Default: int = rawDefaults[general][lightModeGradientColor][default]
            Unsupported: int = rawDefaults[general][lightModeGradientColor][unsupported]

        class LightModeOpacity:
            Default: int = rawDefaults[general][lightModeOpacity][default]
            Unsupported: int = rawDefaults[general][lightModeOpacity][unsupported]

        class Disabled:
            Default: int = rawDefaults[general][disabled][default]
            Unsupported: int = rawDefaults[general][disabled][unsupported]

        class DropDown:
            class EffectType:
                Default: int = rawDefaults[general][dropdown][effectType][default]
                Unsupported: int = rawDefaults[general][dropdown][effectType][
                    unsupported
                ]

            class EnableDropShadow:
                Default: int = rawDefaults[general][dropdown][enableDropShadow][default]
                Unsupported: int = rawDefaults[general][dropdown][enableDropShadow][
                    unsupported
                ]

            class DarkModeGradientColor:
                Default: int = rawDefaults[general][dropdown][darkModeGradientColor][
                    default
                ]
                Unsupported: int = rawDefaults[general][dropdown][
                    darkModeGradientColor
                ][unsupported]

            class LightModeGradientColor:
                Default: int = rawDefaults[general][dropdown][lightModeGradientColor][
                    default
                ]
                Unsupported: int = rawDefaults[general][dropdown][
                    lightModeGradientColor
                ][unsupported]

            class LightModeOpacity:
                Default: int = rawDefaults[general][dropdown][lightModeOpacity][default]
                Unsupported: int = rawDefaults[general][dropdown][lightModeOpacity][
                    unsupported
                ]

            class Disabled:
                Default: int = rawDefaults[general][dropdown][disabled][default]
                Unsupported: int = rawDefaults[general][dropdown][disabled][unsupported]

        class Menu:
            class NoSystemOutline:
                Default: int = rawDefaults[general][menu][noSystemOutline][default]
                Unsupported: int = rawDefaults[general][menu][noSystemOutline][
                    unsupported
                ]

            class EnableImmersiveStyle:
                Default: int = rawDefaults[general][menu][enableImmersiveStyle][default]
                Unsupported: int = rawDefaults[general][menu][enableImmersiveStyle][
                    unsupported
                ]

            class EnableCustomRendering:
                Default: int = rawDefaults[general][menu][enableCustomRendering][
                    default
                ]
                Unsupported: int = rawDefaults[general][menu][enableCustomRendering][
                    unsupported
                ]

            class EffectType:
                Default: int = rawDefaults[general][menu][effectType][default]
                Unsupported: int = rawDefaults[general][menu][effectType][unsupported]

            class EnableDropShadow:
                Default: int = rawDefaults[general][menu][enableDropShadow][default]
                Unsupported: int = rawDefaults[general][menu][enableDropShadow][
                    unsupported
                ]

            class DarkModeGradientColor:
                Default: int = rawDefaults[general][menu][darkModeGradientColor][
                    default
                ]
                Unsupported: int = rawDefaults[general][menu][darkModeGradientColor][
                    unsupported
                ]

            class LightModeGradientColor:
                Default: int = rawDefaults[general][menu][lightModeGradientColor][
                    default
                ]
                Unsupported: int = rawDefaults[general][menu][lightModeGradientColor][
                    unsupported
                ]

            class LightModeOpacity:
                Default: int = rawDefaults[general][menu][lightModeOpacity][default]
                Unsupported: int = rawDefaults[general][menu][lightModeOpacity][
                    unsupported
                ]

            class Disabled:
                Default: int = rawDefaults[general][menu][disabled][default]
                Unsupported: int = rawDefaults[general][menu][disabled][unsupported]

    class MenuItems:
        class Hot:
            class DarkModeGradientColor:
                Default: int = rawDefaults[menuItems][hot][darkModeGradientColor][
                    default
                ]
                Unsupported: int = rawDefaults[menuItems][hot][darkModeGradientColor][
                    unsupported
                ]

            class LightModeGradientColor:
                Defaults: int = rawDefaults[menuItems][hot][lightModeGradientColor][
                    default
                ]
                Unsupported: int = rawDefaults[menuItems][hot][lightModeGradientColor][
                    unsupported
                ]

            class DarkModeOpacity:
                Default: int = rawDefaults[menuItems][hot][darkModeOpacity][default]
                Unsupported: int = rawDefaults[menuItems][hot][darkModeOpacity][
                    unsupported
                ]

            class LightModeOpacity:
                Default: int = rawDefaults[menuItems][hot][lightModeOpacity][default]
                Unsupported: int = rawDefaults[menuItems][hot][lightModeOpacity][
                    unsupported
                ]

            class Disabled:
                Default: int = rawDefaults[menuItems][hot][disabled][default]
                Unsupported: int = rawDefaults[menuItems][hot][disabled][unsupported]

            class CornerRadius:
                Default: int = rawDefaults[menuItems][hot][cornerRadius][default]
                Unsupported: int = rawDefaults[menuItems][hot][cornerRadius][
                    unsupported
                ]

            class EnableThemeCustomization:
                Default: int = rawDefaults[menuItems][hot][enableThemeCustomization][
                    default
                ]
                Unsupported: int = rawDefaults[menuItems][hot][
                    enableThemeCustomization
                ][unsupported]

        class DisabledHot:
            class DarkModeGradientColor:
                Default: int = rawDefaults[menuItems][disabledHot][
                    darkModeGradientColor
                ][default]
                Unsupported: int = rawDefaults[menuItems][disabledHot][
                    darkModeGradientColor
                ][unsupported]

            class LightModeGradientColor:
                Defaults: int = rawDefaults[menuItems][disabledHot][
                    lightModeGradientColor
                ][default]
                Unsupported: int = rawDefaults[menuItems][disabledHot][
                    lightModeGradientColor
                ][unsupported]

            class DarkModeOpacity:
                Default: int = rawDefaults[menuItems][disabledHot][darkModeOpacity][
                    default
                ]
                Unsupported: int = rawDefaults[menuItems][disabledHot][darkModeOpacity][
                    unsupported
                ]

            class LightModeOpacity:
                Default: int = rawDefaults[menuItems][disabledHot][lightModeOpacity][
                    default
                ]
                Unsupported: int = rawDefaults[menuItems][disabledHot][
                    lightModeOpacity
                ][unsupported]

            class Disabled:
                Default: int = rawDefaults[menuItems][disabledHot][disabled][default]
                Unsupported: int = rawDefaults[menuItems][disabledHot][disabled][
                    unsupported
                ]

            class CornerRadius:
                Default: int = rawDefaults[menuItems][disabledHot][cornerRadius][
                    default
                ]
                Unsupported: int = rawDefaults[menuItems][disabledHot][cornerRadius][
                    unsupported
                ]

            class EnableThemeCustomization:
                Default: int = rawDefaults[menuItems][disabledHot][
                    enableThemeCustomization
                ][default]
                Unsupported: int = rawDefaults[menuItems][disabledHot][
                    enableThemeCustomization
                ][unsupported]

        class Focusing:
            class DarkModeGradientColor:
                Default: int = rawDefaults[menuItems][focusing][darkModeGradientColor][
                    default
                ]
                Unsupported: int = rawDefaults[menuItems][focusing][
                    darkModeGradientColor
                ][unsupported]

            class LightModeGradientColor:
                Defaults: int = rawDefaults[menuItems][focusing][
                    lightModeGradientColor
                ][default]
                Unsupported: int = rawDefaults[menuItems][focusing][
                    lightModeGradientColor
                ][unsupported]

            class DarkModeOpacity:
                Default: int = rawDefaults[menuItems][focusing][darkModeOpacity][
                    default
                ]
                Unsupported: int = rawDefaults[menuItems][focusing][darkModeOpacity][
                    unsupported
                ]

            class LightModeOpacity:
                Default: int = rawDefaults[menuItems][focusing][lightModeOpacity][
                    default
                ]
                Unsupported: int = rawDefaults[menuItems][focusing][lightModeOpacity][
                    unsupported
                ]

            class Disabled:
                Default: int = rawDefaults[menuItems][focusing][disabled][default]
                Unsupported: int = rawDefaults[menuItems][focusing][disabled][
                    unsupported
                ]

            class CornerRadius:
                Default: int = rawDefaults[menuItems][focusing][cornerRadius][default]
                Unsupported: int = rawDefaults[menuItems][focusing][cornerRadius][
                    unsupported
                ]

            class EnableThemeCustomization:
                Default: int = rawDefaults[menuItems][focusing][
                    enableThemeCustomization
                ][default]
                Unsupported: int = rawDefaults[menuItems][focusing][
                    enableThemeCustomization
                ][unsupported]

        class Border:
            class NoBorderColor:
                Default: int = rawDefaults[menuItems][border][noBorderColor][default]
                Unsupported: int = rawDefaults[menuItems][border][noBorderColor][
                    unsupported
                ]

            class CornerType:
                Defaults: int = rawDefaults[menuItems][border][cornerType][default]
                Unsupported: int = rawDefaults[menuItems][border][cornerType][
                    unsupported
                ]

            class DarkModeGradientColor:
                Default: int = rawDefaults[menuItems][border][darkModeGradientColor][
                    default
                ]
                Unsupported: int = rawDefaults[menuItems][border][
                    darkModeGradientColor
                ][unsupported]

            class LightModeGradientColor:
                Defaults: int = rawDefaults[menuItems][border][lightModeGradientColor][
                    default
                ]
                Unsupported: int = rawDefaults[menuItems][border][
                    lightModeGradientColor
                ][unsupported]

            class DarkModeOpacity:
                Default: int = rawDefaults[menuItems][border][darkModeOpacity][default]
                Unsupported: int = rawDefaults[menuItems][border][darkModeOpacity][
                    unsupported
                ]

            class LightModeOpacity:
                Default: int = rawDefaults[menuItems][border][lightModeOpacity][default]
                Unsupported: int = rawDefaults[menuItems][border][lightModeOpacity][
                    unsupported
                ]

            class CornerRadius:
                Default: int = rawDefaults[menuItems][border][cornerRadius][default]
                Unsupported: int = rawDefaults[menuItems][border][cornerRadius][
                    unsupported
                ]

            class EnableThemeCustomization:
                Default: int = rawDefaults[menuItems][border][enableThemeCustomization][
                    default
                ]
                Unsupported: int = rawDefaults[menuItems][border][
                    enableThemeCustomization
                ][unsupported]

        class Separator:
            class DarkModeGradientColor:
                Default: int = rawDefaults[menuItems][separator][darkModeGradientColor][
                    default
                ]
                Unsupported: int = rawDefaults[menuItems][separator][
                    darkModeGradientColor
                ][unsupported]

            class LightModeGradientColor:
                Defaults: int = rawDefaults[menuItems][separator][
                    lightModeGradientColor
                ][default]
                Unsupported: int = rawDefaults[menuItems][separator][
                    lightModeGradientColor
                ][unsupported]

            class DarkModeOpacity:
                Default: int = rawDefaults[menuItems][separator][darkModeOpacity][
                    default
                ]
                Unsupported: int = rawDefaults[menuItems][separator][darkModeOpacity][
                    unsupported
                ]

            class LightModeOpacity:
                Default: int = rawDefaults[menuItems][separator][lightModeOpacity][
                    default
                ]
                Unsupported: int = rawDefaults[menuItems][separator][lightModeOpacity][
                    unsupported
                ]

            class Disabled:
                Default: int = rawDefaults[menuItems][separator][disabled][default]
                Unsupported: int = rawDefaults[menuItems][separator][disabled][
                    unsupported
                ]

            class CornerRadius:
                Default: int = rawDefaults[menuItems][separator][cornerRadius][default]
                Unsupported: int = rawDefaults[menuItems][separator][cornerRadius][
                    unsupported
                ]

            class EnableThemeCustomization:
                Default: int = rawDefaults[menuItems][separator][
                    enableThemeCustomization
                ][default]
                Unsupported: int = rawDefaults[menuItems][separator][
                    enableThemeCustomization
                ][default]

    class Tooltip:
        pass

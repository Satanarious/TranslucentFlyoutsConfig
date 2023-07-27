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
            Default = rawDefaults[general][scope][default]
            Unsupported = rawDefaults[general][scope][unsupported]

        class EffectType:
            Default = rawDefaults[general][effectType][default]
            Unsupported = rawDefaults[general][effectType][unsupported]

        class EnableDropShadow:
            Default = rawDefaults[general][enableDropShadow][default]
            Unsupported = rawDefaults[general][enableDropShadow][unsupported]

        class DarkModeGradientColor:
            Default = rawDefaults[general][darkModeGradientColor][default]
            Unsupported = rawDefaults[general][darkModeGradientColor][unsupported]

        class LightModeGradientColor:
            Default = rawDefaults[general][lightModeGradientColor][default]
            Unsupported = rawDefaults[general][lightModeGradientColor][unsupported]

        class LightModeOpacity:
            Default = rawDefaults[general][lightModeOpacity][default]
            Unsupported = rawDefaults[general][lightModeOpacity][unsupported]

        class Disabled:
            Default = rawDefaults[general][disabled][default]
            Unsupported = rawDefaults[general][disabled][unsupported]

    class DropDown:
        class EffectType:
            Default = rawDefaults[dropdown][effectType][default]
            Unsupported = rawDefaults[dropdown][effectType][unsupported]

        class EnableDropShadow:
            Default = rawDefaults[dropdown][enableDropShadow][default]
            Unsupported = rawDefaults[dropdown][enableDropShadow][unsupported]

        class DarkModeGradientColor:
            Default = rawDefaults[dropdown][darkModeGradientColor][default]
            Unsupported = rawDefaults[dropdown][darkModeGradientColor][unsupported]

        class LightModeGradientColor:
            Default = rawDefaults[dropdown][lightModeGradientColor][default]
            Unsupported = rawDefaults[dropdown][lightModeGradientColor][unsupported]

        class LightModeOpacity:
            Default = rawDefaults[dropdown][lightModeOpacity][default]
            Unsupported = rawDefaults[dropdown][lightModeOpacity][unsupported]

        class Disabled:
            Default = rawDefaults[dropdown][disabled][default]
            Unsupported = rawDefaults[dropdown][disabled][unsupported]

    class Menu:
        class NoSystemOutline:
            Default = rawDefaults[menu][noSystemOutline][default]
            Unsupported = rawDefaults[menu][noSystemOutline][unsupported]

        class EnableImmersiveStyle:
            Default = rawDefaults[menu][enableImmersiveStyle][default]
            Unsupported = rawDefaults[menu][enableImmersiveStyle][unsupported]

        class EnableCustomRendering:
            Default = rawDefaults[menu][enableCustomRendering][default]
            Unsupported = rawDefaults[menu][enableCustomRendering][unsupported]

        class EffectType:
            Default = rawDefaults[menu][effectType][default]
            Unsupported = rawDefaults[menu][effectType][unsupported]

        class EnableDropShadow:
            Default = rawDefaults[menu][enableDropShadow][default]
            Unsupported = rawDefaults[menu][enableDropShadow][unsupported]

        class DarkModeGradientColor:
            Default = rawDefaults[menu][darkModeGradientColor][default]
            Unsupported = rawDefaults[menu][darkModeGradientColor][unsupported]

        class LightModeGradientColor:
            Default = rawDefaults[menu][lightModeGradientColor][default]
            Unsupported = rawDefaults[menu][lightModeGradientColor][unsupported]

        class LightModeOpacity:
            Default = rawDefaults[menu][lightModeOpacity][default]
            Unsupported = rawDefaults[menu][lightModeOpacity][unsupported]

        class Disabled:
            Default = rawDefaults[menu][disabled][default]
            Unsupported = rawDefaults[menu][disabled][unsupported]

    class MenuItems:
        class Hot:
            class DarkModeGradientColor:
                Default = rawDefaults[menuItems][hot][darkModeGradientColor][default]
                Unsupported = rawDefaults[menuItems][hot][darkModeGradientColor][
                    unsupported
                ]

            class LightModeGradientColor:
                Defaults = rawDefaults[menuItems][hot][lightModeGradientColor][default]
                Unsupported = rawDefaults[menuItems][hot][lightModeGradientColor][
                    unsupported
                ]

            class DarkModeOpacity:
                Default = rawDefaults[menuItems][hot][darkModeOpacity][default]
                Unsupported = rawDefaults[menuItems][hot][darkModeOpacity][unsupported]

            class LightModeOpacity:
                Default = rawDefaults[menuItems][hot][lightModeOpacity][default]
                Unsupported = rawDefaults[menuItems][hot][lightModeOpacity][unsupported]

            class Disabled:
                Default = rawDefaults[menuItems][hot][disabled][default]
                Unsupported = rawDefaults[menuItems][hot][disabled][unsupported]

            class CornerRadius:
                Default = rawDefaults[menuItems][hot][cornerRadius][default]
                Unsupported = rawDefaults[menuItems][hot][cornerRadius][unsupported]

            class EnableThemeCustomization:
                Default = rawDefaults[menuItems][hot][enableThemeCustomization][default]
                Unsupported = rawDefaults[menuItems][hot][enableThemeCustomization][
                    unsupported
                ]

        class DisabledHot:
            class DarkModeGradientColor:
                Default = rawDefaults[menuItems][disabledHot][darkModeGradientColor][
                    default
                ]
                Unsupported = rawDefaults[menuItems][disabledHot][
                    darkModeGradientColor
                ][unsupported]

            class LightModeGradientColor:
                Defaults = rawDefaults[menuItems][disabledHot][lightModeGradientColor][
                    default
                ]
                Unsupported = rawDefaults[menuItems][disabledHot][
                    lightModeGradientColor
                ][unsupported]

            class DarkModeOpacity:
                Default = rawDefaults[menuItems][disabledHot][darkModeOpacity][default]
                Unsupported = rawDefaults[menuItems][disabledHot][darkModeOpacity][
                    unsupported
                ]

            class LightModeOpacity:
                Default = rawDefaults[menuItems][disabledHot][lightModeOpacity][default]
                Unsupported = rawDefaults[menuItems][disabledHot][lightModeOpacity][
                    unsupported
                ]

            class Disabled:
                Default = rawDefaults[menuItems][disabledHot][disabled][default]
                Unsupported = rawDefaults[menuItems][disabledHot][disabled][unsupported]

            class CornerRadius:
                Default = rawDefaults[menuItems][disabledHot][cornerRadius][default]
                Unsupported = rawDefaults[menuItems][disabledHot][cornerRadius][
                    unsupported
                ]

            class EnableThemeCustomization:
                Default = rawDefaults[menuItems][disabledHot][enableThemeCustomization][
                    default
                ]
                Unsupported = rawDefaults[menuItems][disabledHot][
                    enableThemeCustomization
                ][unsupported]

        class Focusing:
            class DarkModeGradientColor:
                Default = rawDefaults[menuItems][focusing][darkModeGradientColor][
                    default
                ]
                Unsupported = rawDefaults[menuItems][focusing][darkModeGradientColor][
                    unsupported
                ]

            class LightModeGradientColor:
                Defaults = rawDefaults[menuItems][focusing][lightModeGradientColor][
                    default
                ]
                Unsupported = rawDefaults[menuItems][focusing][lightModeGradientColor][
                    unsupported
                ]

            class DarkModeOpacity:
                Default = rawDefaults[menuItems][focusing][darkModeOpacity][default]
                Unsupported = rawDefaults[menuItems][focusing][darkModeOpacity][
                    unsupported
                ]

            class LightModeOpacity:
                Default = rawDefaults[menuItems][focusing][lightModeOpacity][default]
                Unsupported = rawDefaults[menuItems][focusing][lightModeOpacity][
                    unsupported
                ]

            class Disabled:
                Default = rawDefaults[menuItems][focusing][disabled][default]
                Unsupported = rawDefaults[menuItems][focusing][disabled][unsupported]

            class CornerRadius:
                Default = rawDefaults[menuItems][focusing][cornerRadius][default]
                Unsupported = rawDefaults[menuItems][focusing][cornerRadius][
                    unsupported
                ]

            class EnableThemeCustomization:
                Default = rawDefaults[menuItems][focusing][enableThemeCustomization][
                    default
                ]
                Unsupported = rawDefaults[menuItems][focusing][
                    enableThemeCustomization
                ][unsupported]

        class Border:
            class NoBorderColor:
                Default = rawDefaults[menuItems][border][noBorderColor][default]
                Unsupported = rawDefaults[menuItems][border][noBorderColor][unsupported]

            class CornerType:
                Defaults = rawDefaults[menuItems][border][cornerType][default]
                Unsupported = rawDefaults[menuItems][border][cornerType][unsupported]

            class DarkModeGradientColor:
                Default = rawDefaults[menuItems][border][darkModeGradientColor][default]
                Unsupported = rawDefaults[menuItems][border][darkModeGradientColor][
                    unsupported
                ]

            class LightModeGradientColor:
                Defaults = rawDefaults[menuItems][border][lightModeGradientColor][
                    default
                ]
                Unsupported = rawDefaults[menuItems][border][lightModeGradientColor][
                    unsupported
                ]

            class DarkModeOpacity:
                Default = rawDefaults[menuItems][border][darkModeOpacity][default]
                Unsupported = rawDefaults[menuItems][border][darkModeOpacity][
                    unsupported
                ]

            class LightModeOpacity:
                Default = rawDefaults[menuItems][border][lightModeOpacity][default]
                Unsupported = rawDefaults[menuItems][border][lightModeOpacity][
                    unsupported
                ]

            class CornerRadius:
                Default = rawDefaults[menuItems][border][cornerRadius][default]
                Unsupported = rawDefaults[menuItems][border][cornerRadius][unsupported]

            class EnableThemeCustomization:
                Default = rawDefaults[menuItems][border][enableThemeCustomization][
                    default
                ]
                Unsupported = rawDefaults[menuItems][border][enableThemeCustomization][
                    unsupported
                ]

        class Separator:
            class DarkModeGradientColor:
                Default = rawDefaults[menuItems][separator][darkModeGradientColor][
                    default
                ]
                Unsupported = rawDefaults[menuItems][separator][darkModeGradientColor][
                    unsupported
                ]

            class LightModeGradientColor:
                Defaults = rawDefaults[menuItems][separator][lightModeGradientColor][
                    default
                ]
                Unsupported = rawDefaults[menuItems][separator][lightModeGradientColor][
                    unsupported
                ]

            class DarkModeOpacity:
                Default = rawDefaults[menuItems][separator][darkModeOpacity][default]
                Unsupported = rawDefaults[menuItems][separator][darkModeOpacity][
                    unsupported
                ]

            class LightModeOpacity:
                Default = rawDefaults[menuItems][separator][lightModeOpacity][default]
                Unsupported = rawDefaults[menuItems][separator][lightModeOpacity][
                    unsupported
                ]

            class Disabled:
                Default = rawDefaults[menuItems][separator][disabled][default]
                Unsupported = rawDefaults[menuItems][separator][disabled][unsupported]

            class CornerRadius:
                Default = rawDefaults[menuItems][separator][cornerRadius][default]
                Unsupported = rawDefaults[menuItems][separator][cornerRadius][
                    unsupported
                ]

            class EnableThemeCustomization:
                Default = rawDefaults[menuItems][separator][enableThemeCustomization][
                    default
                ]
                Unsupported = rawDefaults[menuItems][separator][
                    enableThemeCustomization
                ][unsupported]

    class Tooltip:
        pass

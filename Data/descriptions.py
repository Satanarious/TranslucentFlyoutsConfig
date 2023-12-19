# Relative Import
from Data.translations import translationVar, Key


class Description:
    @staticmethod
    def effectType(isNotGlobal: bool = False) -> str:
        mainString: str = (
            """
        <body>
        """
            + translationVar.translateFrom("Effect type allows you to choose the background effect used in various flyouts and elements in Translucent Flyouts.")
            + """
        <center>
        <table border=0.5>
        <tr>
        <th>"""
            + translationVar.translateFrom(Key.Parameter.effectType)
            + """</th>
        <th>"""
            + translationVar.translateFrom(Key.TableHeading.description)
            + """</th>
        <th>"""
            + translationVar.translateFrom(Key.TableHeading.support)
            + """</th>
        </tr>
        <tr>
        <td>"""
            + translationVar.translateFrom(Key.Value.EffectType.disabled)
            + """</td>
        <td>"""
            + translationVar.translateFrom("Disables any effects used for pop-ups.")
            + """</td>
        <td"""
            + translationVar.translateFrom(Key.Support.windows10Plus)
            + """</td>
        </tr>
        <tr>
        <td>"""
            + translationVar.translateFrom(Key.Value.EffectType.transparent)
            + """</td>
        <td>"""
            + translationVar.translateFrom("Adds a fully transparent effect as the background for pop-ups.")
            + """</td>
        <td>"""
            + translationVar.translateFrom(Key.Support.windows10AndWin11Build)
            + """</td>
        </tr>
        <tr>
        <td>"""
            + translationVar.translateFrom(Key.Value.EffectType.solid)
            + """</td>
        <td>"""
            + translationVar.translateFrom("Adds a solid coloured background effect as the background for pop-ups.")
            + """</td>
        <td>"""
            + translationVar.translateFrom(Key.Support.windows10AndWin11Build)
            + """</td>
        </tr>
        <tr>
        <td>"""
            + translationVar.translateFrom(Key.Value.EffectType.blur)
            + """</td>
        <td>"""
            + translationVar.translateFrom("Adds a blurred effect as the background for pop-ups.")
            + """</td>
        <td>"""
            + translationVar.translateFrom(Key.Support.windows10Plus)
            + """</td>
        </tr>
        <tr>
        <td>"""
            + translationVar.translateFrom(Key.Value.EffectType.classicAcrylicBlur)
            + """</td>
        <td>"""
            + translationVar.translateFrom("Adds a acrylic paint-textured blur effect as the background for pop-ups.")
            + """</td>
        <td>"""
            + translationVar.translateFrom(Key.Support.windows10Plus)
            + """</td>
        </tr>
        <tr>
        <td>"""
            + translationVar.translateFrom(Key.Value.EffectType.modernAcrylicBlur)
            + """</td>
        <td>"""
            + translationVar.translateFrom("Adds the windows 11 styled acrylic paint-textured blur effect as background for pop-ups.")
            + """</td>
        <td>"""
            + translationVar.translateFrom(Key.Support.windows11)
            + """</td>
        </tr>
        <tr>
        <td>"""
            + translationVar.translateFrom(Key.Value.EffectType.acrylic)
            + """</td>
        <td>"""
            + translationVar.translateFrom("Adds a acrylic paint-textured background layer as the background for the pop-ups.")
            + """</td>
        <td>"""
            + translationVar.translateFrom(Key.Support.windows1122H2Plus)
            + """</td>
        </tr>
        <tr>
        <td"""
            + translationVar.translateFrom(Key.Value.EffectType.mica)
            + """</td>
        <td>"""
            + translationVar.translateFrom("Adds the signature mica-blur effect as the background for the pop-ups.")
            + """</td>
        <td>"""
            + translationVar.translateFrom(Key.Support.windows11)
            + """</td>
        </tr>
        <tr>
        <td>"""
            + translationVar.translateFrom(Key.Value.EffectType.micaAlt)
            + """</td>
        <td>"""
            + translationVar.translateFrom("Adds the signature mica-blur, but as a background layer for the background for the pop-ups.")
            + """</td>
        <td>"""
            + translationVar.translateFrom(Key.Support.windows1122H2Plus)
            + """</td>
        </tr>
        """
        )
        if isNotGlobal:
            mainString += (
                """
            <tr>
            <td>"""
                + translationVar.translateFrom(Key.Value.useGlobalSetting)
                + """</td>
            <td>"""
                + translationVar.translateFrom(Key.Notes.correspondingValue)
                + translationVar.translateFrom(Key.Parameter.effectType)
                + translationVar.translateFrom(Key.Notes.codeValue)
                + """</td>
            <td>"""
                + translationVar.translateFrom(Key.Support.windows10Plus)
                + """</td>
            </tr>
            """
            )
        mainString += """
        </table>
        </center>
        </body>
        """
        return mainString

    @staticmethod
    def cornerType(isNotGlobal: bool = False) -> str:
        mainString: str = (
            """
        <body>
        """
            + translationVar.translateFrom("Corner type allows you to choose between differend shapes and sizes of corners used for the pop-ups.")
            + """
        <center>
        <table border=0.5>
        <tr>
        <th>"""
            + translationVar.translateFrom(Key.Parameter.cornerType)
            + """</th>
        <th>"""
            + translationVar.translateFrom(Key.TableHeading.description)
            + """</th>
        <th>"""
            + translationVar.translateFrom(Key.TableHeading.support)
            + """</th>
        </tr>
        <tr>
        <td>"""
            + translationVar.translateFrom(Key.Value.CornerType.dontChange)
            + """</td>
        <td>"""
            + translationVar.translateFrom("Keeps the default corner type as supported by windows")
            + """</td>
        <td>"""
            + translationVar.translateFrom(Key.Support.windows11)
            + """</td>
        </tr>
        <tr>
        <td>"""
            + translationVar.translateFrom(Key.Value.CornerType.squareCorners)
            + """</td>
        <td>"""
            + translationVar.translateFrom("Use sharp corners instead of round corners.")
            + """</td>
        <td>"""
            + translationVar.translateFrom(Key.Support.windows11)
            + """</td>
        </tr>
        <tr>
        <td>"""
            + translationVar.translateFrom(Key.Value.CornerType.largeCorners)
            + """</td>
        <td>"""
            + translationVar.translateFrom("Use more largely rounded corners")
            + """</td>
        <td>"""
            + translationVar.translateFrom(Key.Support.windows11)
            + """</td>
        </tr>
        <tr>
        <td>"""
            + translationVar.translateFrom(Key.Value.CornerType.smallCorners)
            + """</td>
        <td>"""
            + translationVar.translateFrom("Use smaller corners with lesser roundness")
            + """</td>
        <td>"""
            + translationVar.translateFrom(Key.Support.windows11)
            + """</td>
        </tr>
        """
        )
        if isNotGlobal:
            mainString += (
                """
            <tr>
            <td>"""
                + translationVar.translateFrom(Key.Value.useGlobalSetting)
                + """</td>
            <td>"""
                + translationVar.translateFrom(Key.Notes.correspondingValue)
                + translationVar.translateFrom(Key.Parameter.cornerType)
                + translationVar.translateFrom(Key.Notes.codeValue)
                + """</td>
            <td>"""
                + translationVar.translateFrom(Key.Support.windows10Plus)
                + """</td>
            </tr>
            """
            )
        mainString += """
        </table>
        </center>
        </body>
        """
        return mainString

    @staticmethod
    def enableDropShadow(isNotGlobal: bool = False) -> str:
        mainString = (
            """
        <body>
        """
            + translationVar.translateFrom("Enable Drop Shadow allows you to choose whether to enable the drop shadow effect for the pop-ups.")
            + """
        <center>
        <table border=0.5>
        <tr>
        <th>"""
            + translationVar.translateFrom(Key.TableHeading.boolean)
            + """</th>
        <th>"""
            + translationVar.translateFrom(Key.TableHeading.description)
            + """</th>
        <th>"""
            + translationVar.translateFrom(Key.TableHeading.support)
            + """</th>
        </tr>
        <tr>
        <td>"""
            + translationVar.translateFrom(Key.Value.Bool.no)
            + """</td>
        <td>"""
            + translationVar.translateFrom("Disables the drop shadow visible behind the pop-ups.")
            + """</td>
        <td>"""
            + translationVar.translateFrom(Key.Support.windows10Plus)
            + """</td>
        </tr>
        <tr>
        <td>"""
            + translationVar.translateFrom(Key.Value.Bool.yes)
            + """</td>
        <td>"""
            + translationVar.translateFrom("Enables an additional border with shadow bahind the pop-up")
            + """</td>
        <td>"""
            + translationVar.translateFrom(
                "Only works when <code>Effect Type</code> is set to Classic Acrylic Blur on Windows 10 or Modern Acrylic Blur and <code>Corner Type</code> is set to Square Corners on Windows 11"
            )
            + """</td>
        </tr>
        """
        )
        if isNotGlobal:
            mainString += (
                """
            <tr>
            <td>"""
                + translationVar.translateFrom(Key.Value.useGlobalSetting)
                + """</td>
            <td>"""
                + translationVar.translateFrom(Key.Notes.correspondingValue)
                + translationVar.translateFrom(Key.Parameter.enableDropShadow)
                + translationVar.translateFrom(Key.Notes.codeValue)
                + """</td>
            <td>"""
                + translationVar.translateFrom(Key.Support.windows10Plus)
                + """</td>
            </tr>
            """
            )
        mainString += """
        </table>
        </center>
        </body>
        """
        return mainString

    @staticmethod
    def noBorderColor(isNotGlobal: bool = False) -> str:
        mainString = (
            """
        <body>
        """
            + translationVar.translateFrom("No Border Color allows you to choose whether to render system borders on the pop-ups.")
            + """
        <center>
        <table border=0.5>
        <tr>
        <th>"""
            + translationVar.translateFrom(Key.TableHeading.boolean)
            + """</th>
        <th>"""
            + translationVar.translateFrom(Key.TableHeading.description)
            + """</th>
        <th>"""
            + translationVar.translateFrom(Key.TableHeading.notes)
            + """</th>
        </tr>
        <tr>
        <td>"""
            + translationVar.translateFrom(Key.Value.Bool.no)
            + """</td>
        <td>"""
            + translationVar.translateFrom("Choose to show the system borders on the pop-ups")
            + """</td>
        <td>"""
            + translationVar.translateFrom("On Windows 10, Only supports removing the system borders of pop-up menus and fully supports Windows 11.")
            + """</td>
        </tr>
        <tr>
        <td>"""
            + translationVar.translateFrom(Key.Value.Bool.yes)
            + """</td>
        <td>"""
            + translationVar.translateFrom("Choose to hide the system borders on the pop-ups")
            + """</td>
        <td>"""
            + translationVar.translateFrom(Key.Notes.supportsWindows10Plus)
            + """</td>
        </tr>
        """
        )
        if isNotGlobal:
            mainString += (
                """
            <tr>
            <td>"""
                + translationVar.translateFrom(Key.Value.useGlobalSetting)
                + """</td>
            <td>"""
                + translationVar.translateFrom(Key.Notes.correspondingValue)
                + translationVar.translateFrom(Key.Parameter.noBorderColor)
                + translationVar.translateFrom(Key.Notes.codeValue)
                + """</td>
            <td>"""
                + translationVar.translateFrom(Key.Support.windows10Plus)
                + """</td>
            </tr>
            """
            )
        mainString += """
        </table>
        </center>
        </body>
        """
        return mainString

    @staticmethod
    def enableThemeColorization(isNotGlobal: bool = False, isInMenu: bool = False) -> str:
        mainString = (
            """
        <body>
        """
            + translationVar.translateFrom(
                "Enable Theme Colorization allows you to choose whether to enable using the current theme color as the system border for the pop-ups."
            )
            + """
        <center>
        <table border=0.5>
        <tr>
        <th>"""
            + translationVar.translateFrom(Key.TableHeading.boolean)
            + """</th>
        <th>"""
            + translationVar.translateFrom(Key.TableHeading.description)
            + """</th>
        <th>"""
            + translationVar.translateFrom(Key.TableHeading.notes)
            + """</th>
        </tr>
        <tr>
        <td>"""
            + translationVar.translateFrom(Key.Value.Bool.no)
            + """</td>
        <td>"""
            + translationVar.translateFrom("Choose not to use the current theme color as system border")
            + """</td>
        <td>"""
            + translationVar.translateFrom(Key.Notes.supportsWindows10Plus)
            + """</td>
        </tr>
        <tr>
        <td>"""
            + translationVar.translateFrom(Key.Value.Bool.yes)
            + """</td>
        <td>"""
            + translationVar.translateFrom("Choose to use the current theme color as system border")
            + """</td>
        <td>"""
            + translationVar.translateFrom(
                "This option is ignored when <code>Dark/LightMode Border Color</code> or <code>Dark/Light Mode Color</code> values are present"
            )
            + """</td>
        </tr>
        """
        )
        if isNotGlobal:
            mainString += (
                """
            <tr>
            <td>"""
                + translationVar.translateFrom(Key.Value.useGlobalSetting)
                + """</td>
            <td>"""
                + translationVar.translateFrom(Key.Notes.correspondingValue)
                + translationVar.translateFrom(Key.Parameter.enableThemeColorization)
                + translationVar.translateFrom(Key.Notes.codeValue)
                + """</td>
            <td>"""
                + translationVar.translateFrom(Key.Support.windows10Plus)
                + """</td>
            </tr>
            """
            )
        if isInMenu:
            mainString += (
                """
            </table>
            </center>
            <h4>"""
                + translationVar.translateFrom(Key.Notes.enableCustomRendering)
                + """</h4>
            </body>
            """
            )
        else:
            mainString += """
            </table>
            </center>
            </body>
            """
        return mainString

    @staticmethod
    def darkModeBorderColor() -> str:
        return (
            """
        <body>
        """
            + translationVar.translateFrom(
                "Dark mode border color sets the color of the system border in dark mode. You can choose the color to your liking while also being able to choose the opacity with the help of the alpha value."
            )
            + """
        """
            + translationVar.translateFrom(Key.Notes.alphaValueNote)
            + """
        </body>
        """
        )

    @staticmethod
    def lightModeBorderColor() -> str:
        return (
            """
        <body>
        """
            + translationVar.translateFrom(
                "Light mode border color sets the color of the system border in light mode. You can choose the color to your liking while also being able to choose the opacity with the help of the alpha value."
            )
            + translationVar.translateFrom(Key.Notes.alphaValueNote)
            + """
        </body>
        """
        )

    @staticmethod
    def darkModeGradientColor() -> str:
        return (
            """
        <body>
        """
            + translationVar.translateFrom(
                "Dark mode gradient color sets the color of the background in dark mode. You can choose the color to your liking while also being able to choose the opacity with the help of the alpha value."
            )
            + """
        """
            + translationVar.translateFrom(Key.Notes.gradientColorNote)
            + """
        </body>
        """
        )

    @staticmethod
    def lightModeGradientColor() -> str:
        return (
            """
        <body>
        """
            + translationVar.translateFrom(
                "Light mode gradient color sets the color of the background in light mode. You can choose the color to your liking while also being able to choose the opacity with the help of the alpha value."
            )
            + """
        """
            + translationVar.translateFrom(Key.Notes.gradientColorNote)
            + """
        </body>
        """
        )

    @staticmethod
    def disabled(isNotGlobal: bool = False) -> str:
        mainString = (
            """
        <body>
        """
            + translationVar.translateFrom("Disabled allows you to choose to disable all effects for this pop-up type.")
            + """
        <center>
        <table border=0.5>
        <tr>
        <th>"""
            + translationVar.translateFrom("Boolean")
            + """</th>
        <th>"""
            + translationVar.translateFrom(Key.TableHeading.description)
            + """</th>
        <th>"""
            + translationVar.translateFrom(Key.TableHeading.notes)
            + """</th>
        </tr>
        <tr>
        <td>"""
            + translationVar.translateFrom(Key.Value.Bool.no)
            + """</td>
        <td>"""
            + translationVar.translateFrom("Choose not to disable all effects")
            + """</td>
        <td>"""
            + translationVar.translateFrom(Key.Notes.supportsWindows10Plus)
            + """</td>
        </tr>
        <tr>
        <td>"""
            + translationVar.translateFrom(Key.Value.Bool.yes)
            + """</td>
        <td>"""
            + translationVar.translateFrom("Choose to disable all effects for this pop-up type")
            + """</td>
        <td>"""
            + translationVar.translateFrom("The translucent effects and animations for these pop-ups will be disabled.")
            + """</td>
        </tr>
        """
        )
        if isNotGlobal:
            mainString += (
                """
            <tr>
            <td>"""
                + translationVar.translateFrom(Key.Value.useGlobalSetting)
                + """</td>
            <td>"""
                + translationVar.translateFrom(Key.Notes.correspondingValue)
                + translationVar.translateFrom(Key.Parameter.disabled)
                + translationVar.translateFrom(Key.Notes.codeValue)
                + """</td>
            <td>"""
                + translationVar.translateFrom(Key.Support.windows10Plus)
                + """</td>
            </tr>
            """
            )
        mainString += """
        </table>
        </center>
        </body>
        """
        return mainString

    @staticmethod
    def noSystemDropShadow() -> str:
        return (
            """
        <body>
        """
            + translationVar.translateFrom("No system drop shadow allow you to choose to removes the old-style system shadow called <code>SysShadow</code>.")
            + """
        <center>
        <table border=0.5>
        <tr>
        <th>"""
            + translationVar.translateFrom(Key.TableHeading.boolean)
            + """</th>
        <th>"""
            + translationVar.translateFrom(Key.TableHeading.description)
            + """</th>
        <th>"""
            + translationVar.translateFrom(Key.TableHeading.notes)
            + """</th>
        </tr>
        <tr>
        <td>"""
            + translationVar.translateFrom(Key.Value.Bool.no)
            + """</td>
        <td>"""
            + translationVar.translateFrom("Disable the old-style system drop shadows.")
            + """</td>
        <td>"""
            + translationVar.translateFrom(Key.Notes.supportsWindows10Plus)
            + """</td>
        </tr>
        <tr>
        <td>"""
            + translationVar.translateFrom(Key.Value.Bool.yes)
            + """</td>
        <td>"""
            + translationVar.translateFrom("Keep the old-style system drop shadow.")
            + """</td>
        <td>"""
            + translationVar.translateFrom("Generally Windows 11 doesn't have these unless there are any menus with sharp corners.")
            + """</td>
        </tr>
        </table>
        </center>
        </body>
        """
        )

    @staticmethod
    def enableImmersiveStyle() -> str:
        return (
            """
        <body>
        """
            + translationVar.translateFrom("Enable immersive style allows you to choose to uniformly style pop-up menus as modern menus.")
            + """
        <center>
        <table border=0.5>
        <tr>
        <th>"""
            + translationVar.translateFrom(Key.TableHeading.boolean)
            + """</th>
        <th>"""
            + translationVar.translateFrom(Key.TableHeading.description)
            + """</th>
        <th>"""
            + translationVar.translateFrom(Key.TableHeading.notes)
            + """</th>
        </tr>
        <tr>
        <td>"""
            + translationVar.translateFrom(Key.Value.Bool.no)
            + """</td>
        <td>"""
            + translationVar.translateFrom("Do not enable uniformly styled pop-ups")
            + """</td>
        <td>"""
            + translationVar.translateFrom(Key.Notes.supportsWindows10Plus)
            + """</td>
        </tr>
        <tr>
        <td>"""
            + translationVar.translateFrom(Key.Value.Bool.yes)
            + """</td>
        <td>"""
            + translationVar.translateFrom("Enable the uniformly style pop-up menus as modern menus.")
            + """</td>
        <td>"""
            + translationVar.translateFrom("It is strongly recommended to not to disable this option in Windows 11")
            + """</td>
        </tr>
        </table>
        </center>
        </body>
        """
        )

    @staticmethod
    def enableCustomRendering() -> str:
        return (
            """
        <body>
        """
            + translationVar.translateFrom(
                "Enable custom rendering allows you to choose to fully render the pop-ups from scratch using a custom rendering technique."
            )
            + """
        <h4>"""
            + translationVar.translateFrom("Note: Set this value to <code>Yes</code> for the parameters in the Menu section to work.")
            + """</h4>
        <center>
        <table border=0.5>
        <tr>
        <th>"""
            + translationVar.translateFrom(Key.TableHeading.boolean)
            + """</th>
        <th>"""
            + translationVar.translateFrom(Key.TableHeading.description)
            + """</th>
        <th>"""
            + translationVar.translateFrom(Key.TableHeading.notes)
            + """</th>
        </tr>
        <tr>
        <td>"""
            + translationVar.translateFrom(Key.Value.Bool.no)
            + """</td>
        <td>"""
            + translationVar.translateFrom("Do not enable custom rendering")
            + """</td>
        </tr>
        <tr>
        <td>"""
            + translationVar.translateFrom(Key.Value.Bool.yes)
            + """</td>
        <td>"""
            + translationVar.translateFrom("Enable the custom rendering for pop-up menus.")
            + """</td>
        <td>"""
            + translationVar.translateFrom(Key.Notes.supportsWindows10Plus)
            + """</td>
        </tr>
        </table>
        </center>
        
        </body>
        """
        )

    @staticmethod
    def enableFluentAnimation() -> str:
        return (
            """
        <body>
        """
            + translationVar.translateFrom("Enable fluent animation allows you to choose to add fluent pop-up animations for menus.")
            + """
        <center>
        <table border=0.5>
        <tr>
        <th>"""
            + translationVar.translateFrom(Key.TableHeading.boolean)
            + """</th>
        <th>"""
            + translationVar.translateFrom(Key.TableHeading.description)
            + """</th>
        <th>"""
            + translationVar.translateFrom(Key.TableHeading.notes)
            + """</th>
        </tr>
        <tr>
        <td>"""
            + translationVar.translateFrom(Key.Value.Bool.no)
            + """</td>
        <td>"""
            + translationVar.translateFrom("Do not enable fluent animations")
            + """</td>
        </tr>
        <tr>
        <td>"""
            + translationVar.translateFrom(Key.Value.Bool.yes)
            + """</td>
        <td>"""
            + translationVar.translateFrom("Enable fluent animations for menus.")
            + """</td>
        <td>"""
            + translationVar.translateFrom(Key.Notes.supportsWindows10Plus)
            + """</td>
        </tr>
        </table>
        </center>
        </body>
        """
        )

    @staticmethod
    def noModernAppBackgroundColor() -> str:
        return (
            """
        <body>
        """
            + translationVar.translateFrom(
                "No modern app background color removes the background color of UWP icons(such as Photos, Paint, Snipping Tools, Store)."
            )
            + """
        <center>
        <table border=0.5>
        <tr>
        <th>"""
            + translationVar.translateFrom(Key.TableHeading.boolean)
            + """</th>
        <th>"""
            + translationVar.translateFrom(Key.TableHeading.description)
            + """</th>
        <th>"""
            + translationVar.translateFrom(Key.TableHeading.notes)
            + """</th>
        </tr>
        <tr>
        <td>"""
            + translationVar.translateFrom(Key.Value.Bool.no)
            + """</td>
        <td>"""
            + translationVar.translateFrom("Do not remove the background colors of UWP icons")
            + """</td>
        </tr>
        <tr>
        <td>"""
            + translationVar.translateFrom(Key.Value.Bool.yes)
            + """</td>
        <td>"""
            + translationVar.translateFrom("Enable the removal of background color of UWP icons.")
            + """</td>
        <td>"""
            + translationVar.translateFrom(Key.Notes.supportsWindows10Plus)
            + """</td>
        </tr>
        </table>
        </center>
        </body>
        """
        )

    @staticmethod
    def colorTreatAsTransparent() -> str:
        return (
            """
        <body>
        """
            + translationVar.translateFrom(
                "Color treat as transparent allows you to choose a specific color to remove background color of certain icons when this item exists. The removal process expands from the four corners of the icon towards the center until the removal cannot be continued."
            )
            + """
        </body>
        """
        )

    @staticmethod
    def colorTreatAsTransparentThreshold() -> str:
        return (
            """
        <body>
        """
            + translationVar.translateFrom(
                "Color treat as transparent threshold allows you to choose a value between 0 to 510 and removes the background color if the color differnce between the pixels is less than this color."
            )
            + """
        """
            + translationVar.translateFrom("<p>Equation: √[(a1 - a2) ^ 2 + (r1 - r2) ^ 2 + (g1 - g2) ^ 2 + (b1 - b2) ^ 2]</p>")
            + """
        </body>
        """
        )

    @staticmethod
    def fadeOutTime() -> str:
        return (
            """
        <body>
        """
            + translationVar.translateFrom(
                "Fade out time allows you to choose a value in milliseconds to serve as the duration of the fade-out animation after interacting with a menu item."
            )
            + """
        <h4>"""
            + translationVar.translateFrom(Key.Notes.enableCustomRendering)
            + """</h4>
        </body>
        """
        )

    @staticmethod
    def fadeInTime() -> str:
        return (
            """
        <body>
        """
            + translationVar.translateFrom(
                "Fade in time allows you to choose a value in milliseconds to serve as the duration of the fade-in animation of when the menu appears."
            )
            + """
        <h4>"""
            + translationVar.translateFrom(Key.Notes.enableCustomRendering)
            + """</h4>
        </body>
        """
        )

    @staticmethod
    def startRatio() -> str:
        return (
            """
        <body>
        """
            + translationVar.translateFrom("Start ratio is the percentage of the pop-in animation between 0 and 100.")
            + """
        """
            + translationVar.translateFrom(
                "Increasing this value can reduce the visual perception of animation lag, but too high may weaken the visual effect of the animation; decreasing this value can enhance the visual experience of the animation, but too low may affect the interaction experience."
            )
            + """
        <h4>"""
            + translationVar.translateFrom(Key.Notes.enableCustomRendering)
            + """</h4>
        </body>
        """
        )

    @staticmethod
    def enableImmediateInterupting() -> str:
        return (
            """
        <body>
        """
            + translationVar.translateFrom("Enable immediate interupting allow users to immediately interrupt animations.")
            + """
        """
            + translationVar.translateFrom(
                "Enabling this option will immediately stop and end the Fluent animation when a menu item is selected/hovered with the mouse."
            )
            + """
        <center>
        <table border=0.5>
        <tr>
        <th>"""
            + translationVar.translateFrom(Key.TableHeading.boolean)
            + """</th>
        <th>"""
            + translationVar.translateFrom(Key.TableHeading.description)
            + """</th>
        <th>"""
            + translationVar.translateFrom(Key.TableHeading.notes)
            + """</th>
        </tr>
        <tr>
        <td>"""
            + translationVar.translateFrom(Key.Value.Bool.no)
            + """</td>
        <td>"""
            + translationVar.translateFrom("Do not enable immediate stoppage and end of fluent animation")
            + """</td>
        <td>"""
            + translationVar.translateFrom(Key.Notes.supportsWindows10Plus)
            + """</td>
        </tr>
        <tr>
        <td>"""
            + translationVar.translateFrom(Key.Value.Bool.yes)
            + """</td>
        <td>"""
            + translationVar.translateFrom("Enable the immediate stoppage and end of fluent animation.")
            + """</td>
        <td>"""
            + translationVar.translateFrom(Key.Notes.supportsWindows10Plus)
            + """</td>
        </tr>
        </table>
        </center>
        <h4>"""
            + translationVar.translateFrom(Key.Notes.enableCustomRendering)
            + """</h4>
        </body>
        """
        )

    @staticmethod
    def popInStyle() -> str:
        return (
            """
        <body>
        """
            + translationVar.translateFrom("Pop in style is the style of the pop-in animation.")
            + """
        <center>
        <table border=0.5>
        <tr>
        <th>"""
            + translationVar.translateFrom(Key.Parameter.popInStyle)
            + """</th>
        <th>"""
            + translationVar.translateFrom(Key.TableHeading.description)
            + """</th>
        <th>"""
            + translationVar.translateFrom(Key.TableHeading.notes)
            + """</th>
        </tr>
        <tr>
        <td>"""
            + translationVar.translateFrom(Key.Value.PopInStyle.slideDown)
            + """</td>
        <td>"""
            + translationVar.translateFrom("WinUI/UWP basic slide down animation.")
            + """</td>
        <td>"""
            + translationVar.translateFrom(Key.Notes.supportsWindows10Plus)
            + """</td>
        </tr>
        <tr>
        <td>"""
            + translationVar.translateFrom(Key.Value.PopInStyle.ripple)
            + """</td>
        <td>"""
            + translationVar.translateFrom("A ripple like animation wich seems like a paper unfold.")
            + """</td>
        </tr>
        <tr>
        <td>"""
            + translationVar.translateFrom(Key.Value.PopInStyle.smoothScroll)
            + """</td>
        <td>"""
            + translationVar.translateFrom("A smooth scroll/expansion from top-left to bottom-right.")
            + """</td>
        <td>"""
            + translationVar.translateFrom(Key.Notes.supportsWindows10Plus)
            + """</td>
        </tr>
        <tr>
        <td>"""
            + translationVar.translateFrom(Key.Value.PopInStyle.smoothZoom)
            + """</td>
        <td>"""
            + translationVar.translateFrom("A smooth zoom in animation.")
            + """</td>
        </tr>
        </table>
        </center>
        <h4>"""
            + translationVar.translateFrom(Key.Notes.enableCustomRendering)
            + """</h4>
        </body>
        """
        )

    @staticmethod
    def width(isFocusing: bool = False) -> str:
        if isFocusing:
            mainString = """<body>""" + translationVar.translateFrom("Width controls the border thickness of the focus rectangle for pop-up menus.")
        else:
            mainString = """<body>""" + translationVar.translateFrom("Width controls the border thickness of the separator line in pop-up menus.")
        mainString += (
            """
            <table border=0.5>
            <tr>
            <th>"""
            + translationVar.translateFrom(Key.TableHeading.acceptedValues)
            + """</th>
            <th>"""
            + translationVar.translateFrom(Key.TableHeading.description)
            + """</th>
            <th>"""
            + translationVar.translateFrom(Key.TableHeading.support)
            + """</th>
            </tr>
            <tr>
            <td>"""
            + translationVar.translateFrom("Values are accepted in ms, 1000ms= 1s ")
            + """</td>
            <td>"""
            + translationVar.translateFrom("This value is divided by 1000 as it is converted to DIP(Device Independent Pixels)")
            + """</td>
            <td>"""
            + translationVar.translateFrom(Key.Support.windows11)
            + """</td>
            </tr>
            </table>
            </center> 
            <h4>"""
            + translationVar.translateFrom(Key.Notes.enableCustomRendering)
            + """</h4>
            </body>
            """
        )
        return mainString

    @staticmethod
    def cornerRadius() -> str:
        return (
            """
        <body>
        """
            + translationVar.translateFrom("Corner radius, as the name suggests is radius of corners for this menu item.")
            + """
        <h4>"""
            + translationVar.translateFrom(Key.Notes.enableCustomRendering)
            + """</h4>
        </body>
        """
        )

    @staticmethod
    def darkModeColor() -> str:
        return (
            """
        <body>
        """
            + translationVar.translateFrom(
                "Dark mode color sets the color of this menu item in dark mode. You can choose the color to your liking while also being able to choose the opacity with the help of the alpha value."
            )
            + """
        """
            + translationVar.translateFrom(Key.Notes.renderBorder)
            + """ 
        <h4>"""
            + translationVar.translateFrom(Key.Notes.enableCustomRendering)
            + """ </h4>   
        </body>
        """
        )

    @staticmethod
    def lightModeColor() -> str:
        return (
            """
        <body>
        """
            + translationVar.translateFrom(
                "Light mode color sets the color of this menu item in light mode. You can choose the color to your liking while also being able to choose the opacity with the help of the alpha value."
            )
            + """ 
        """
            + translationVar.translateFrom(Key.Notes.renderBorder)
            + """  
        <h4>"""
            + translationVar.translateFrom(Key.Notes.enableCustomRendering)
            + """ </h4>
        </body>
        """
        )

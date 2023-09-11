# Relative Imports
from Data.enums import MenuTab


class Description:
    @staticmethod
    def effectType(isNotGlobal: bool = False) -> str:
        mainString: str = """
        <body>
        Effect type allows you to choose the background effect used in various flyouts and elements in Translucent Flyouts.
        <center>
        <table border=0.5>
        <tr>
        <th>Effect Type</th>
        <th>Description</th>
        <th>Support</th>
        </tr>
        <tr>
        <td>Disable</td>
        <td>Disables any effects used for pop-ups.</td>
        <td>Windows 10+</td>
        </tr>
        <tr>
        <td>Transparent</td>
        <td>Adds a fully transparent effect as the background for pop-ups.</td>
        <td>Windows 10,<br>Windows 11(Before Build 22000)</td>
        </tr>
        <tr>
        <td>Solid</td>
        <td>Adds a solid coloured background effect as the background for pop-ups.</td>
        <td>Windows 10,<br>Windows 11(Before Build 22000)</td>
        </tr>
        <tr>
        <td>Blur</td>
        <td>Adds a blurred effect as the background for pop-ups.</td>
        <td>Windows 10+</td>
        </tr>
        <tr>
        <td>Classic Acrylic Blur</td>
        <td>Adds a acrylic paint-textured blur effect as the background for pop-ups.</td>
        <td>Windows 10+</td>
        </tr>
        <tr>
        <td>Modern Acrylic Blur</td>
        <td>Adds the windows 11 styled acrylic paint-textured blur effect as background for pop-ups.</td>
        <td>Windows 11</td>
        </tr>
        <tr>
        <td>Acrylic</td>
        <td>Adds a acrylic paint-textured background layer as the background for the pop-ups.</td>
        <td>Windows 11 22H2+</td>
        </tr>
        <tr>
        <td>Mica</td>
        <td>Adds the signature mica-blur effect as the background for the pop-ups.</td>
        <td>Windows 11</td>
        </tr>
        <tr>
        <td>Mica Alt</td>
        <td>Adds the signature mica-blur, but as a background layer for the background for the pop-ups.</td>
        <td>Windows 11 22H2+</td>
        </tr>
        """
        if isNotGlobal:
            mainString += """
            <tr>
            <td>Use Global Setting</td>
            <td>Uses the corresponding value in the global tab as the <code>Effect Type</code> value.</td>
            <td>Windows 10+</td>
            </tr>
            """
        mainString += """
        </table>
        </center>
        </body>
        """
        return mainString

    @staticmethod
    def cornerType(isNotGlobal: bool = False) -> str:
        mainString: str = """
        <body>
        Corner type allows you to choose between differend shapes and sizes of corners used for the pop-ups.
        <center>
        <table border=0.5>
        <tr>
        <th>Corner Type</th>
        <th>Description</th>
        <th>Support</th>
        </tr>
        <tr>
        <td>Don't Change</td>
        <td>Keeps the default corner type as supported by windows</td>
        <td>Windows 11</td>
        </tr>
        <tr>
        <td>Sharp Corner</td>
        <td>Use sharp corners instead of round corners.</td>
        <td>Windows 11</td>
        </tr>
        <tr>
        <td>Large Round Corner</td>
        <td>Use more largely rounded corners</td>
        <td>Windows 11</td>
        </tr>
        <tr>
        <td>Small Round Corner</td>
        <td>Use smaller corners with lesser roundness </td>
        <td>Windows 11</td>
        </tr>
        """
        if isNotGlobal:
            mainString += """
            <tr>
            <td>Use Global Setting</td>
            <td>Uses the corresponding value in the global tab as the <code>Corner Type</code> value.</td>
            <td>Windows 10+</td>
            </tr>
            """
        mainString += """
        </table>
        </center>
        </body>
        """
        return mainString

    @staticmethod
    def enableDropShadow(isNotGlobal: bool = False) -> str:
        mainString = """
        <body>
        Enable Drop Shadow allows you to choose whether to enable the drop shadow effect for the pop-ups.
        <center>
        <table border=0.5>
        <tr>
        <th>Boolean</th>
        <th>Description</th>
        <th>Notes</th>
        </tr>
        <tr>
        <td>Disable</td>
        <td>Disables the drop shadow visible behind the pop-ups.</td>
        <td>Supports Windows 10+</td>
        </tr>
        <tr>
        <td>Enable</td>
        <td>Enables an additional border with shadow bahind the pop-up</td>
        <td>Only works when <code>Effect Type</code> is set to Classic Acrylic Blur on Windows 10 or Modern Acrylic Blur and <code>Corner Type</code> is set to 1 on Windows 11</td>
        </tr>
        """
        if isNotGlobal:
            mainString += """
            <tr>
            <td>Use Global Setting</td>
            <td>Uses the corresponding value in the global tab as the <code>Enable Drop Shadow</code> value.</td>
            <td>Windows 10+</td>
            </tr>
            """
        mainString += """
        </table>
        </center>
        </body>
        """
        return mainString

    @staticmethod
    def noBorderColor(isNotGlobal: bool = False) -> str:
        mainString = """
        <body>
        No Border Color allows you to choose whether to render system borders on the pop-ups.
        <center>
        <table border=0.5>
        <tr>
        <th>Boolean</th>
        <th>Description</th>
        <th>Notes</th>
        </tr>
        <tr>
        <td>No</td>
        <td>Choose to show the system borders on the pop-ups</td>
        <td>on Window 10, Only supports removing the system borders of pop-up menus and fully supports Windows 11.</td>
        </tr>
        <tr>
        <td>Yes</td>
        <td>Choose to hide the system borders on the pop-ups</td>
        <td>Supports Windows 10+</td>
        </tr>
        """
        if isNotGlobal:
            mainString += """
            <tr>
            <td>Use Global Setting</td>
            <td>Uses the corresponding value in the global tab as the <code>No Border Color</code> value.</td>
            <td>Windows 10+</td>
            </tr>
            """
        mainString += """
        </table>
        </center>
        </body>
        """
        return mainString

    @staticmethod
    def enableThemeColorization(isNotGlobal: bool = False, isInMenu: bool = False) -> str:
        mainString = """
        <body>
        Enable Theme Colorization allows you to choose whether to enable using the current theme color as the system border for the pop-ups.
        <center>
        <table border=0.5>
        <tr>
        <th>Booelan</th>
        <th>Description</th>
        <th>Notes</th>
        </tr>
        <tr>
        <td>No</td>
        <td>Choose not to use the current theme color as system border</td>
        <td>Supports Windows 10+</td>
        </tr>
        <tr>
        <td>Yes</td>
        <td>Choose to use the current theme color as system border</td>
        <td>This option is ignored when <code>Dark/LightMode Border Color</code> or <code>Dark/Light Mode Color</code> values are present</td>
        </tr>
        """
        if isNotGlobal:
            mainString += """
            <tr>
            <td>Use Global Setting</td>
            <td>Uses the corresponding value in the global tab as the <code>Enable Theme Colorization</code> value.</td>
            <td>Windows 10+</td>
            </tr>
            """
        if isInMenu:
            mainString += """
            </table>
            </center>
            <h4>Note: Values in this section require the <code>Enable Custom Rendering</code> property in the Menu->General section be set to <code>Yes</code> to function.</h4>
            </body>
            """
        else:
            mainString += """
            </table>
            </center>
            </body>
            """
        return mainString

    @staticmethod
    def darkModeBorderColor() -> str:
        return """
        <body>
        Dark mode border color sets the color of the system border in dark mode. You can choose the color to your liking while also being able to choose the opacity with the help of the alpha value.
        The alpha/opacity value will be ignored when using round corners in Windows 11.
        </body>
        """

    @staticmethod
    def lightModeBorderColor() -> str:
        return """
        <body>
        Light mode border color sets the color of the system border in light mode. You can choose the color to your liking while also being able to choose the opacity with the help of the alpha value.
        The alpha/opacity value will be ignored when using round corners in Windows 11.
        </body>
        """

    @staticmethod
    def darkModeGradientColor() -> str:
        return """
        <body>
        Dark mode gradient color sets the color of the background in dark mode. You can choose the color to your liking while also being able to choose the opacity with the help of the alpha value.
        This will be ignored when using <code>Effect Type</code> as <code>Acrylic</code>, <code>Mica</code> or <code>Mica Alt</code>.
        </body>
        """

    @staticmethod
    def lightModeGradientColor() -> str:
        return """
        <body>
        Light mode gradient color sets the color of the background in light mode. You can choose the color to your liking while also being able to choose the opacity with the help of the alpha value.
        This will be ignored when using <code>Effect Type</code> as <code>Acrylic</code>, <code>Mica</code> or <code>Mica Alt</code>.
        </body>
        """

    @staticmethod
    def disabled(isNotGlobal: bool = False) -> str:
        mainString = """
        <body>
        Disabled allows you to choose to disable all effects for this pop-up type.
        <center>
        <table border=0.5>
        <tr>
        <th>Booelan</th>
        <th>Description</th>
        <th>Notes</th>
        </tr>
        <tr>
        <td>No</td>
        <td>Choose not to disable all effects</td>
        <td>Supports Windows 10+</td>
        </tr>
        <tr>
        <td>Yes</td>
        <td>Choose to disable all effects for this pop-up type</td>
        <td>The translucent effects and animations for these pop-ups will be disabled.</td>
        </tr>
        """
        if isNotGlobal:
            mainString += """
            <tr>
            <td>Use Global Setting</td>
            <td>Uses the corresponding value in the global tab as the <code>Disabled</code> value.</td>
            <td>Windows 10+</td>
            </tr>
            """
        mainString += """
        </table>
        </center>
        </body>
        """
        return mainString

    @staticmethod
    def noSystemDropShadow() -> str:
        return """
        <body>
        No system drop shadow allow you to choose to removes the old-style system shadow called <code>SysShadow</code>.
        <center>
        <table border=0.5>
        <tr>
        <th>Boolean</th>
        <th>Description</th>
        <th>Notes</th>
        </tr>
        <tr>
        <td>No</td>
        <td>Disable the old-style system drop shadows.</td>
        <td>Supports Windows 10+</td>
        </tr>
        <tr>
        <td>Yes</td>
        <td>Keep the old-style system drop shadow.</td>
        <td>Generally Windows 11 doesn't have these unless there are any menus with sharp corners.</td>
        </tr>
        </table>
        </center>
        </body>
        """

    @staticmethod
    def enableImmersiveStyle() -> str:
        return """
        <body>
        Enable immersive style allows you to choose to uniformly style pop-up menus as modern menus.
        <center>
        <table border=0.5>
        <tr>
        <th>Boolean</th>
        <th>Description</th>
        <th>Notes</th>
        </tr>
        <tr>
        <td>No</td>
        <td>Do not enable uniformly styled pop-ups</td>
        <td>Supports Windows 10+</td>
        </tr>
        <tr>
        <td>Yes</td>
        <td>Enable the uniformly style pop-up menus as modern menus.</td>
        <td>It is strongly recommended to not to disable this option in Windows 11</td>
        </tr>
        </table>
        </center>
        </body>
        """

    @staticmethod
    def enableCustomRendering() -> str:
        return """
        <body>
        Enable custom rendering allows you to choose to fully render the pop-ups from scratch using a custom rendering technique.
        <h4>Note: Set this value to <code>Yes</code> for the parameters in the Menu section to work.</h4>
        <center>
        <table border=0.5>
        <tr>
        <th>Boolean</th>
        <th>Description</th>
        <th>Notes</th>
        </tr>
        <tr>
        <td>No</td>
        <td>Do not enable custom dendering</td>
        </tr>
        <tr>
        <td>Yes</td>
        <td>Enable the custom rendering for pop-up menus.</td>
        <td>Supports Windows 10+</td>
        </tr>
        </table>
        </center>
        
        </body>
        """

    @staticmethod
    def enableFluentAnimation() -> str:
        return """
        <body>
        Enable fluent animation allows you to choose to add fluent pop-up animations for menus.
        <center>
        <table border=0.5>
        <tr>
        <th>Boolean</th>
        <th>Description</th>
        <th>Notes</th>
        </tr>
        <tr>
        <td>No</td>
        <td>Do not enable fluent animations</td>
        </tr>
        <tr>
        <td>Yes</td>
        <td>Enable fluent animations for menus.</td>
        <td>Supports Windows 10+</td>
        </tr>
        </table>
        </center>
        </body>
        """

    @staticmethod
    def noModernAppBackgroundColor() -> str:
        return """
        <body>
        No modern app background color removes the background color of UWP icons(such as Photos, Paint, Snipping Tools, Store).
        <center>
        <table border=0.5>
        <tr>
        <th>Boolean</th>
        <th>Description</th>
        <th>Notes</th>
        </tr>
        <tr>
        <td>No</td>
        <td>Do not remove the background colors of UWP icons</td>
        </tr>
        <tr>
        <td>Yes</td>
        <td>Enable the removal of background color of UWP icons.</td>
        <td>Supports Windows 10+</td>
        </tr>
        </table>
        </center>
        </body>
        """

    @staticmethod
    def colorTreatAsTransparent() -> str:
        return """
        <body>
        Color treat as transparent allows you to choose a specific color to remove background color of certain icons when this item exists. The removal process expands from the four corners of the icon towards the center until the removal cannot be continued.
        </body>
        """

    @staticmethod
    def colorTreatAsTransparentThreshold() -> str:
        return """
        <body>
        Color treat as transparent threshold allows you to choose a value between 0 to 510 and removes the background color if the color differnce between the pixels is less than this color.
        Equation: <code>√[(a1 - a2) ^ 2 + (r1 - r2) ^ 2 + (g1 - g2) ^ 2 + (b1 - b2) ^ 2]</code>
        </body>
        """

    @staticmethod
    def fadeOutTime() -> str:
        return """
        <body>
        Fade out time allows you to choose a value in milliseconds to serve as the duration of the fade-out animation after interacting with a manu item.
        <h4>Note: Values in this section require the <code>Enable Custom Rendering</code> property in the Menu->General section be set to <code>Yes</code> to function.</h4>
        </body>
        """

    @staticmethod
    def fadeInTime() -> str:
        return """
        <body>
        Fade in time allows you to choose a value in milliseconds to serve as the duration of the fade-in animation of when the menu appears.
        <h4>Note: Values in this section require the <code>Enable Custom Rendering</code> property in the Menu->General section be set to <code>Yes</code> to function.</h4>
        </body>
        """

    @staticmethod
    def startRatio() -> str:
        return """
        <body>
        Start ratio is the percentage of the pop-in animation between 0 and 100.
        Increasing this value can reduce the visual perception of animation lag, but too high may weaken the visual effect of the animation; decreasing this value can enhance the visual experience of the animation, but too low may affect the interaction experience.
        <h4>Note: Values in this section require the <code>Enable Custom Rendering</code> property in the Menu->General section be set to <code>Yes</code> to function.</h4>
        </body>
        """

    @staticmethod
    def enableImmediateInterupting() -> str:
        return """
        <body>
        Enable immediate interupting allow users to immediately interrupt animations.
        Enabling this option will immediately stop and end the Fluent animation when a menu item is selected/hovered with the mouse.
        <center>
        <table border=0.5>
        <tr>
        <th>Boolean</th>
        <th>Description</th>
        <th>Notes</th>
        </tr>
        <tr>
        <td>No</td>
        <td>Do not enable immediate stoppage and end of fluent animation</td>
        <td>Supports Windows 10+</td>
        </tr>
        <tr>
        <td>Yes</td>
        <td>Enable the immediate stoppage and end of fluent animation.</td>
        <td>Supports Windows 10+</td>
        </tr>
        </table>
        </center>
        <h4>Note: Values in this section require the <code>Enable Custom Rendering</code> property in the Menu->General section be set to <code>Yes</code> to function.</h4>
        </body>
        """

    @staticmethod
    def popInStyle() -> str:
        return """
        <body>
        Pop in style is the style of the pop-in animation.
        <center>
        <table border=0.5>
        <tr>
        <th>Pop In Style</th>
        <th>Description</th>
        <th>Notes</th>
        </tr>
        <tr>
        <td>Slide Down</td>
        <td>WinUI/UWP basic slide down animation.</td>
        <td>Supports Windows 10+</td>
        </tr>
        <tr>
        <td>Ripple</td>
        <td>A ripple like animation wich seems like a paper unfold.</td>
        </tr>
        <tr>
        <td>Smooth Scroll</td>
        <td>A smooth scroll/expansion from top-left to bottom-right.</td>
        <td>Supports Windows 10+</td>
        </tr>
        <tr>
        <td>Smooth Zoom</td>
        <td>A smooth zoom in animation.</td>
        </tr>
        </table>
        </center>
        <h4>Note: Values in this section require the <code>Enable Custom Rendering</code> property in the Menu->General section be set to <code>Yes</code> to function.</h4>
        </body>
        """

    @staticmethod
    def width(isFocusing: bool = False) -> str:
        if isFocusing:
            mainString = """<body>Width controls the border thickness of the focus rectangle for pop-up menus."""
        else:
            mainString = """<body>Width controls the border thickness of the separator line in pop-up menus."""
        mainString += """
            <table border=0.5>
            <tr>
            <th>Accepted Values</th>
            <th>Description</th>
            <th>Support</th>
            </tr>
            <tr>
            <td>This value is divided by 1000 as it is converted to DIP(Device Independent Pixels)</td>
            <td>Supports Windows 10+</td>
            <td>Windows 11</td>
            </tr>
            </table>
            </center> 
            <h4>Note: Values in this section require the <code>Enable Custom Rendering</code> property in the Menu->General section be set to <code>Yes</code> to function.</h4>
            </body>
            """
        return mainString

    @staticmethod
    def cornerRadius() -> str:
        return """
        <body>
        Corner radius, as the name suggests is radius of corners for this menu item.
        <h4>Note: Values in this section require the <code>Enable Custom Rendering</code> property in the Menu->General section be set to <code>Yes</code> to function.</h4>
        </body>
        """

    @staticmethod
    def darkModeColor() -> str:
        return """
        <body>
        Dark mode color sets the color of this menu item in dark mode. You can choose the color to your liking while also being able to choose the opacity with the help of the alpha value.
        This is used for renderig border or filling rectangles.     
        <h4>Note: Values in this section require the <code>Enable Custom Rendering</code> property in the Menu->General section be set to <code>Yes</code> to function.</h4>   
        </body>
        """

    @staticmethod
    def lightModeColor() -> str:
        return """
        <body>
        light mode color sets the color of this menu item in light mode. You can choose the color to your liking while also being able to choose the opacity with the help of the alpha value.
        This is used for renderig border or filling rectangles.        
        <h4>Note: Values in this section require the <code>Enable Custom Rendering</code> property in the Menu->General section be set to <code>Yes</code> to function.</h4>
        </body>
        """

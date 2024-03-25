from Data.enums import EnumConvert
from Data.paths import Path
from Registry.reg_edit import EditRegistry


class EditSettings:
    @staticmethod
    def changeEffectType(
        keyPath: Path.RegPaths | str,
        effectType: int,
    ):
        """
        Method to:
        Change the effect type of various flyout elements.
        - keyPath: path of the Key which needs to be changed
        - effectType: Effect type from the predefined effect types, Settings.
        """
        EditRegistry.setValue(
            keyPath=keyPath,
            valueName=Path.RegKeys.EffectType,
            value=effectType,
        )

    @staticmethod
    def changeEnableDropShadow(
        keyPath: Path.RegPaths | str,
        isEnabled: int,
    ):
        """
        Method to:
        Change whether to enable drop shadows for various flyout elements.
        - keyPath: path of the Key which needs to be changed
        - isEnabled: mention whether to enable this property or not
        """
        EditRegistry.setValue(
            keyPath=keyPath,
            valueName=Path.RegKeys.EnableDropShadow,
            value=isEnabled,
        )

    @staticmethod
    def changeEnableMiniDump(
        keyPath: Path.RegPaths | str,
        isEnabled: int,
    ):
        """
        Method to:
        Change whether to enable mini dump for Trasnlucent Flyouts.
        - keyPath: path of the Key which needs to be changed
        - isEnabled: mention whether to enable this property or not
        """
        EditRegistry.setValue(
            keyPath=keyPath,
            valueName=Path.RegKeys.EnableMiniDump,
            value=isEnabled,
        )

    @staticmethod
    def changeEnableCompatibilityMode(
        keyPath: Path.RegPaths | str,
        isEnabled: int,
    ):
        """
        Method to:
        Change whether to enable compatibility mode so as not to download symbols.
        - keyPath: path of the Key which needs to be changed
        - isEnabled: mention whether to enable this property or not
        """
        EditRegistry.setValue(
            keyPath=keyPath,
            valueName=Path.RegKeys.EnableCompatibilityMode,
            value=isEnabled,
        )

    @staticmethod
    def changeNoSystemDropShadow(
        keyPath: Path.RegPaths | str,
        isEnabled: int,
    ):
        """
        Method to:
        Change whether to enable Remove the old-style system shadow (SysShadow) from menus.
        - keyPath: path of the Key which needs to be changed
        - isEnabled: mention whether to enable this property or not
        """
        EditRegistry.setValue(
            keyPath=keyPath,
            valueName=Path.RegKeys.NoSystemDropShadow,
            value=isEnabled,
        )

    @staticmethod
    def changeDarkModeThemeColorizationType(
        keyPath: Path.RegPaths | str,
        colorIndex: int,
    ):
        """
        Method to:
        Change the color of theme colorization type in dark-mode.
        - keyPath: path of the Key which needs to be changed
        - colorIndex: comboBox Index of the selected Theme Colorization Type
        """

        EditRegistry.setValue(
            keyPath=keyPath,
            valueName=Path.RegKeys.DarkModeThemeColorizationType,
            value=EnumConvert.themeColorizationTypeToName(colorIndex),
        )

    @staticmethod
    def changeLightModeThemeColorizationType(
        keyPath: Path.RegPaths | str,
        colorIndex: int,
    ):
        """
        Method to:
        Change the color of theme colorization type in dark-mode.
        - keyPath: path of the Key which needs to be changed
        - colorIndex: ComboBox Index of the selected Theme Colorization Type
        """

        EditRegistry.setValue(
            keyPath=keyPath,
            valueName=Path.RegKeys.LightModeThemeColorizationType,
            value=EnumConvert.themeColorizationTypeToName(colorIndex),
        )

    @staticmethod
    def changeMarginsType(keyPath: Path.RegPaths | str, marginsType: int):
        """
        Method to:
        Change the margin type to either stack or replace the existing margin
        - keyPath (Path.RegPaths | str): path of the Key which needs to be changed
        - marginsType (int): ComboBox index of the selected marginType
        """
        EditRegistry.setValue(
            keyPath=keyPath,
            valueName=Path.RegKeys.MarginsType,
            value=marginsType,
        )

    @staticmethod
    def changeMarginLeft(keyPath: Path.RegPaths | str, margin: int):
        """
        Method to:
        Change the left margin
        - keyPath (Path.RegPaths | str): path of the Key which needs to be changed
        - margin (int): margin length
        """
        EditRegistry.setValue(
            keyPath=keyPath,
            valueName=Path.RegKeys.MarginLeft,
            value=margin,
        )

    @staticmethod
    def changeMarginRight(keyPath: Path.RegPaths | str, margin: int):
        """
        Method to:
        Change the right margin
        - keyPath (Path.RegPaths | str): path of the Key which needs to be changed
        - margin (int): margin length
        """
        EditRegistry.setValue(
            keyPath=keyPath,
            valueName=Path.RegKeys.MarginRight,
            value=margin,
        )

    @staticmethod
    def changeMarginTop(keyPath: Path.RegPaths | str, margin: int):
        """
        Method to:
        Change the top margin
        - keyPath (Path.RegPaths | str): path of the Key which needs to be changed
        - margin (int): margin length
        """
        EditRegistry.setValue(
            keyPath=keyPath,
            valueName=Path.RegKeys.MarginTop,
            value=margin,
        )

    @staticmethod
    def changeMarginBottom(keyPath: Path.RegPaths | str, margin: int):
        """
        Method to:
        Change the bottom margin
        - keyPath (Path.RegPaths | str): path of the Key which needs to be changed
        - margin (int): margin length
        """
        EditRegistry.setValue(
            keyPath=keyPath,
            valueName=Path.RegKeys.MarginBottom,
            value=margin,
        )

    @staticmethod
    def changeDarkModeColor(
        keyPath: Path.RegPaths | str,
        color: str,
    ):
        """
        Method to:
        Change the color of various menu-items in dark-mode.
        - keyPath: path of the Key which needs to be changed
        - color: 32-bit color in the form of AARRGGBB
        """
        EditRegistry.setValue(
            keyPath=keyPath,
            valueName=Path.RegKeys.DarkModeColor,
            value=int(color, 16),
        )

    @staticmethod
    def changeLightModeColor(
        keyPath: Path.RegPaths | str,
        color: str,
    ):
        """
        Method to:
        Change the color of various menu-items in light-mode.
        - keyPath: path of the Key which needs to be changed
        - color: 32-bit color in the form of AARRGGBB
        """
        EditRegistry.setValue(
            keyPath=keyPath,
            valueName=Path.RegKeys.LightModeColor,
            value=int(color, 16),
        )

    @staticmethod
    def changeDarkModeBorderColor(
        keyPath: Path.RegPaths | str,
        color: str,
    ):
        """
        Method to:
        Change the border color of flyouts in dark-mode.
        - keyPath: path of the Key which needs to be changed
        - color: 32-bit color in the form of AARRGGBB
        """
        EditRegistry.setValue(
            keyPath=keyPath,
            valueName=Path.RegKeys.DarkModeBorderColor,
            value=int(color, 16),
        )

    @staticmethod
    def changeLightModeBorderColor(
        keyPath: Path.RegPaths | str,
        color: str,
    ):
        """
        Method to:
        Change the border color of flyouts in light-mode.
        - keyPath: path of the Key which needs to be changed
        - color: 32-bit color in the form of AARRGGBB
        """
        EditRegistry.setValue(
            keyPath=keyPath,
            valueName=Path.RegKeys.LightModeBorderColor,
            value=int(color, 16),
        )

    @staticmethod
    def changeDarkModeGradientColor(
        keyPath: Path.RegPaths | str,
        color: str,
    ):
        """
        Method to:
        Change the gradient color of various flyout elements in dark-mode.
        - keyPath: path of the Key which needs to be changed
        - color: 32-bit color in the form of AARRGGBB
        """
        EditRegistry.setValue(
            keyPath=keyPath,
            valueName=Path.RegKeys.DarkModeGradientColor,
            value=int(color, 16),
        )

    @staticmethod
    def changeLightModeGradientColor(
        keyPath: Path.RegPaths | str,
        color: str,
    ):
        """
        Method to:
        Change the gradient color of various flyout elements in light-mode.
        - keyPath: path of the Key which needs to be changed
        - color: 32-bit color in the form of AARRGGBB
        """
        EditRegistry.setValue(
            keyPath=keyPath,
            valueName=Path.RegKeys.LightModeGradientColor,
            value=int(color, 16),
        )

    @staticmethod
    def changeDisabledList(keyPath: Path.RegPaths | str, disabledList: list):
        """
        Change the enteries in the disabledList Key

        Args:
            keyPath (Path.RegPaths | str): path of the Key which needs to be changed
            disabledList (list): List of processes to add to the disabledList
        """
        EditRegistry.setValue(
            keyPath=keyPath,
            valueName=Path.RegKeys.DisabledList,
            value=disabledList,
        )

    @staticmethod
    def changeBlockList(keyPath: Path.RegPaths | str, blockList: list):
        """
        Change the enteries in the blockList Key

        Args:
            keyPath (Path.RegPaths | str): path of the Key which needs to be changed
            blockList (list): List of processes to add to the blockList
        """
        EditRegistry.setValue(
            keyPath=keyPath,
            valueName=Path.RegKeys.BlockList,
            value=blockList,
        )

    @staticmethod
    def changeDisabled(
        keyPath: Path.RegPaths | str,
        isDisabled: int,
    ):
        """
        Method to:
        Change whether to disable various properties of the flyout elements.
        - keyPath: path of the Key which needs to be changed
        - isDisabled: mention whether to disable this property of the flyout element
        """
        EditRegistry.setValue(
            keyPath=keyPath,
            valueName=Path.RegKeys.Disabled,
            value=isDisabled,
        )

    @staticmethod
    def changeEnableImmersiveStyle(
        keyPath: Path.RegPaths | str,
        isEnabled: int,
    ):
        """
        Method to:
        Change whether to enable drop shadows to use a modern menu style.
        - keyPath: path of the Key which needs to be changed
        - isEnabled: mention whether to enable this property or not
        """
        EditRegistry.setValue(
            keyPath=keyPath,
            valueName=Path.RegKeys.EnableImmersiveStyle,
            value=isEnabled,
        )

    @staticmethod
    def changeEnableFluentAnimation(
        keyPath: Path.RegPaths | str,
        isEnabled: int,
    ):
        """
        Method to:
        Change whether to enable modern and fluent pop-up animation for menus.
        - keyPath: path of the Key which needs to be changed
        - isEnabled: mention whether to enable this property or not
        """
        EditRegistry.setValue(
            keyPath=keyPath,
            valueName=Path.RegKeys.EnableFluentAnimation,
            value=isEnabled,
        )

    @staticmethod
    def changeNoModernAppBackgroundColor(
        keyPath: Path.RegPaths | str,
        isDisabled: int,
    ):
        """
        Method to:
        Change whether to remove the background color of UWP icons.
        - keyPath: path of the Key which needs to be changed
        - isDisabled: mention whether to disable this property or not
        """
        EditRegistry.setValue(
            keyPath=keyPath,
            valueName=Path.RegKeys.NoModernAppBackgroundColor,
            value=isDisabled,
        )

    @staticmethod
    def changeColorTreatAsTransparent(
        keyPath: Path.RegPaths | str,
        color: str,
    ):
        """
        Method to:
        Removes specific background colors (0xAARRGGBB) of certain icons when this item exists.
        - keyPath: path of the Key which needs to be changed
        - color: color to be removed
        """
        EditRegistry.setValue(
            keyPath=keyPath,
            valueName=Path.RegKeys.ColorTreatAsTransparent,
            value=int(color, 16),
        )

    @staticmethod
    def changeColorTreatAsTransparentThreshold(
        keyPath: Path.RegPaths | str,
        threshold: int,
    ):
        """
        Method to The color difference threshold between the pixel and the background color to be removed.
        When the color difference between pixels is less than this color difference threshold, the pixel will be made transparent.
        - keyPath: path of thekey which needs to be changed
        - threshold: color threshold
        """
        EditRegistry.setValue(
            keyPath=keyPath,
            valueName=Path.RegKeys.ColorTreatAsTransparentThreshold,
            value=threshold,
        )

    @staticmethod
    def changeEnableCustomRendering(
        keyPath: Path.RegPaths | str,
        isEnabled: int,
    ):
        """
        Method to:
        Change whether to enable custom rendering that will use Direct2D for rendering, allowing you to
        not only customize the color and opacity but also achieve significant performance improvements.
        - keyPath: path of the Key which needs to be changed
        - isEnabled: mention whether to enable this property or not
        """
        EditRegistry.setValue(
            keyPath=keyPath,
            valueName=Path.RegKeys.EnableCustomRendering,
            value=isEnabled,
        )

    @staticmethod
    def changeEnableThemeColorization(
        keyPath: Path.RegPaths | str,
        isEnabled: int,
    ):
        """
        Method to:
        Change whether to enable theme colorization to controls whether to use the current theme color
        to fill the overlay color and opacitythat will use Direct2D for rendering, allowing you to
        not only customize the color and opacity but also achieve significant performance improvements.
        - keyPath: path of the Key which needs to be changed
        - isEnabled: mention whether to enable this property or not
        """
        EditRegistry.setValue(
            keyPath=keyPath,
            valueName=Path.RegKeys.EnableThemeColorization,
            value=isEnabled,
        )

    @staticmethod
    def changeEnableImmediateInterupting(
        keyPath: Path.RegPaths | str,
        isEnabled: int,
    ):
        """
        Method to:
        Change whether to enable users to immediately interrupt animations.
        - keyPath: path of the Key which needs to be changed
        - isEnabled: mention whether to enable this property or not
        """
        EditRegistry.setValue(
            keyPath=keyPath,
            valueName=Path.RegKeys.EnableImmediateInterupting,
            value=isEnabled,
        )

    @staticmethod
    def changeNoBorderColor(
        keyPath: Path.RegPaths | str,
        isEnabled: int,
    ):
        """
        Method to:
        Change whether to enable border color on the flyouts
        - keyPath: path of the Key which needs to be changed
        - isEnabled: mention whether to enable this property or not
        """
        EditRegistry.setValue(
            keyPath=keyPath,
            valueName=Path.RegKeys.NoBorderColor,
            value=isEnabled,
        )

    @staticmethod
    def changeCornerRadius(
        keyPath: Path.RegPaths | str,
        radius: int,
    ):
        """
        Method to:
        Change the change corner radius of the menu-items.
        - keyPath: path of the Key which needs to be changed
        - radius: radius of corner ranging from 0 to 10
        """
        EditRegistry.setValue(
            keyPath=keyPath,
            valueName=Path.RegKeys.CornerRadius,
            value=radius,
        )

    @staticmethod
    def changeCornerType(
        keyPath: Path.RegPaths | str,
        cornerType: int,
    ):
        """
        Method to:
        Change the change corner type of the border.
        - keyPath: path of the key which needs to be changed
        - type: corner type of the border
        """
        EditRegistry.setValue(
            keyPath=keyPath,
            valueName=Path.RegKeys.CornerType,
            value=cornerType,
        )

    @staticmethod
    def changePopInStyle(
        keyPath: Path.RegPaths | str,
        style: int,
    ):
        """
        Method to:
        Change the change the style of the pop-in animation.
        - keyPath: path of the key which needs to be changed
        - type: style type of the pop-in animation
        """
        EditRegistry.setValue(
            keyPath=keyPath,
            valueName=Path.RegKeys.PopInStyle,
            value=style,
        )

    @staticmethod
    def changeFadeOutTime(
        keyPath: Path.RegPaths | str,
        time: int,
    ):
        """
        Method to:
        Change the change the fade-out time of the menu.
        - keyPath: path of the key which needs to be changed
        - time: time for the fade-out animation
        """
        EditRegistry.setValue(
            keyPath=keyPath,
            valueName=Path.RegKeys.FadeOutTime,
            value=time,
        )

    @staticmethod
    def changeFadeInTime(
        keyPath: Path.RegPaths | str,
        time: int,
    ):
        """
        Method to:
        Change the change the fade-in time of the menu.
        - keyPath: path of the key which needs to be changed
        - time: time for the fade-in animation
        """
        EditRegistry.setValue(
            keyPath=keyPath,
            valueName=Path.RegKeys.FadeInTime,
            value=time,
        )

    @staticmethod
    def changePopInTime(
        keyPath: Path.RegPaths | str,
        time: int,
    ):
        """
        Method to:
        Change the change the pop-in time of the menu.
        - keyPath: path of the key which needs to be changed
        - time: time for the pop-in animation
        """
        EditRegistry.setValue(
            keyPath=keyPath,
            valueName=Path.RegKeys.PopInTime,
            value=time,
        )

    @staticmethod
    def changeStartRatio(
        keyPath: Path.RegPaths | str,
        percent: int,
    ):
        """
        Method to:
        Change the percentage (%) of the pop-in animation.
        - keyPath: path of the key which needs to be changed
        - percentage: percent of the start animation
        """
        EditRegistry.setValue(
            keyPath=keyPath,
            valueName=Path.RegKeys.StartRatio,
            value=percent,
        )

    @staticmethod
    def changeWidth(
        keyPath: Path.RegPaths | str,
        width: int,
    ):
        """
        Method to:
        Change the width of various menu-items
        - keyPath: path of the key which needs to be changed
        - width: width of the menu items
        """
        EditRegistry.setValue(
            keyPath=keyPath,
            valueName=Path.RegKeys.Width,
            value=width,
        )

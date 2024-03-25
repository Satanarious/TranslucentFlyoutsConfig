import json

from Data.enums import Languages
from Data.paths import Path


class Key:
    apply: str = "Apply"
    cancel: str = "Cancel"
    disabledList: str = "Disabled List"
    resetAll: str = "Reset All"
    TranslucentFlyoutsConfig: str = "Translucent Flyouts Config"
    changesApplied: str = "Changes Applied"
    ok: str = "OK"
    save: str = "Save"

    class Tab:
        _global: str = "Global"
        dropDown: str = "DropDown"
        menu: str = "Menu"
        tooltip: str = "Tooltip"

        class Menu:
            general: str = "General"
            animation: str = "Animation"
            hot: str = "Hot"
            disabledHot: str = "Disabled Hot"
            focusing: str = "Focusing"
            separator: str = "Separator"

    class TabDescription:
        _global: str = "Modify the overall appearance of all flyouts"
        dropDown: str = "Modify the appearance of all Dropdown flyouts"
        menu: str = "Modify the overall appearance of various menu items and their animations  including: Focused, Hot, Disabled Hot & Separator"
        tooltip: str = "Modify the appearance of all Tooltips"

    class Parameter:
        effectType: str = "Effect Type"
        cornerType: str = "Corner Type"
        enableDropShadow: str = "Enable Drop Shadow"
        noBorderColor: str = "No Border Color"
        textColor: str = "Text Color"
        borderColor: str = "Border Color"
        gradientColor: str = "Gradient Color"
        enableThemeColorization: str = "Enable Theme Colorization"
        enableMiniDump: str = "Enable Mini Dump"
        enableCompatibilityMode: str = "Enable Compatibility Mode"
        darkModeThemeColorizationType: str = "Dark Mode Theme Colorization Type"
        lightModeThemeColorizationType: str = "Light Mode Theme Colorization Type"
        darkMode: str = "Dark Mode"
        lightMode: str = "Light Mode"
        darkModeBorderColor: str = "Dark Mode Border Color"
        lightModeBorderColor: str = "Light Mode Border Color"
        darkModeGradientColor: str = "Dark Mode Gradient Color"
        lightModeGradientColor: str = "Light Mode Gradient Color"
        disabled: str = "Disabled"
        noSystemDropShadow: str = "No System Drop Shadow"
        enableImmersiveStyle: str = "Enable Immersive Style"
        enableCustomRendering: str = "Enable Custom Rendering"
        enableFluentAnimation: str = "Enable Fluent Animation"
        noModernAppBackgroundColor: str = "No Modern App Background Color"
        colorTreatAsTransparent: str = "Color Treat As Transparent"
        colorTreatAsTransparentThreshold: str = "Color Treat As Transparent Threshold"
        marginsType: str = "Margins Type"
        margin: str = "Margin"
        fadeOutTime: str = "Fade Out Time"
        popInTime: str = "Pop In Time"
        fadeInTime: str = "Fade In Time"
        popInStyle: str = "Pop In Style"
        startRatio: str = "Start Ratio"
        enableImmediateInterupting: str = "Enable Immediate Interupting"
        darkModeColor: str = "Dark Mode Color"
        lightModeColor: str = "Light Mode Color"
        cornerRadius: str = "Corner Radius"
        width: str = "Width"

    class Value:
        useGlobalSetting: str = "Use Global Setting"

        class Bool:
            yes: str = "Yes"
            no: str = "No"

        class Margin:
            left: str = "Left:"
            right: str = "Right:"
            top: str = "Top:"
            bottom: str = "Bottom:"

        class MarginsType:
            addToExisting: str = "Add To Existing"
            replaceExisting: str = "Replace Existing"

        class ThemeColorizationType:
            immersiveStartBackground: str = "ImmersiveStartBackground"
            immersiveStartHoverBackground: str = "ImmersiveStartHoverBackground"
            immersiveSystemAccent: str = "ImmersiveSystemAccent"
            immersiveSystemAccentDark1: str = "ImmersiveSystemAccentDark1"
            immersiveSystemAccentDark2: str = "ImmersiveSystemAccentDark2"
            immersiveSystemAccentDark3: str = "ImmersiveSystemAccentDark3"
            immersiveSystemAccentLight1: str = "ImmersiveSystemAccentLight1"
            immersiveSystemAccentLight2: str = "ImmersiveSystemAccentLight2"
            immersiveSystemAccentLight3: str = "ImmersiveSystemAccentLight3"

        class EffectType:
            disabled: str = "Disable"
            transparent: str = "Transparent"
            solid: str = "Solid"
            blur: str = "Blur"
            classicAcrylicBlur: str = "Classic Acrylic Blur"
            modernAcrylicBlur: str = "Modern Acrylic Blur"
            acrylic: str = "Acrylic"
            mica: str = "Mica"
            micaAlt: str = "Mica Alt"

        class CornerType:
            dontChange: str = "Don't Change"
            squareCorners: str = "Square Corners"
            largeCorners: str = "Large Corners"
            smallCorners: str = "Small Corners"

        class PopInStyle:
            slideDown = "Slide Down"
            ripple = "Ripple"
            smoothScroll = "Smooth Scroll"
            smoothZoom = "Smooth Zoom"

    class TableHeading:
        description: str = "Description"
        support: str = "Support"
        boolean: str = "Boolean"
        notes: str = "Notes"
        acceptedValues: str = "Accepted Values"

    class Notes:
        supportsWindows10Plus: str = "Supports Windows 10+"
        correspondingValue: str = (
            "Uses the corresponding value in the global tab as the <code>"
        )
        codeValue: str = "</code> value."
        alphaValueNote: str = "The alpha/opacity value will be ignored when using round corners in Windows 11."
        gradientColorNote: str = "This will be ignored when using <code>Effect Type</code> as <code>Acrylic</code>, <code>Mica</code> or <code>Mica Alt</code>."
        renderBorder: str = "This is used for renderig border or filling rectangles."
        enableCustomRendering: str = "Note: Values in this section require the <code>Enable Custom Rendering</code> property in the Menu->General section be set to <code>Yes</code> to function."
        symbolSkipNote: str = "Note: To eliminate the need for symbols(download required otherwise), set <code>Compatibility Mode</code> and <code>No Modern App Background</code> to <code>Yes</code>"

    class Support:
        windows10Plus: str = "Windows 10+"
        windows10AndWin11Build: str = "Windows 10,<br>Windows 11(Before Build 22000)"
        windows11: str = "Windows 11"
        windows1122H2Plus: str = "Windows 11 22H2+"

    class Settings:
        locationError: str = "!! Error: TFMain64.dll not found !!"
        settingsHeading: str = "Settings"

        class ToolBox:
            general: str = "General"
            appearance: str = "Appearance"
            internalFunctions: str = "Internal Functions"
            externalFunctions: str = "External Functions"
            advancedFunctions: str = "Advanced Functions"

        class General:
            chooseLangauge: str = "Choose Language:"
            installationLocation: str = "Installation Location:"
            chooseFolders: str = "Choose Folder"

        class Appearance:
            manual: str = "Manual:"
            backgroundColor: str = "Background Color"
            secondaryBackgroundColor: str = "Secondary Background Color"
            labelColor: str = "Label Color"
            textColor: str = "Text Color"
            iconColorMode: str = "Icon Color Mode"
            presets: str = "Presets:"
            selectPreset: str = "Select Preset"

            class IconColorMode:
                lightMode: str = "Light Mode"
                darkMode: str = "Dark Mode"

        class InternalFunctions:
            install: str = "Install"
            uninstall: str = "Uninstall"
            run: str = "Run"
            stop: str = "Stop"
            locationNote: str = "Note: This section will only work if Translucent Flyouts' location is specified in the General Settings."

        class ExternalFunctions:
            downloadNote: str = "Note: Pressing the button below will download and install Translucent Flyouts and set the path in the application so you can use the internal functions as well as all the other functionality included in the application."
            downloadAndInstall: str = "Download and Install"

        class AdvancedFunctions:
            advancedNote: str = "Warning: This section is only meant for the advanced user. Configuring the Block List needs a system restart and doesn't load Translucent Flyouts for that application at all. This may cause some serious problems if not used properly, resulting in high CPU usage."
            configureBlockList: str = "Configure Block List"


class TranslationModel:
    def __init__(self) -> None:
        self.language = Languages.Default
        self.translations: dict[str, str] = {}

    def setLanguage(self, language: Languages) -> None:
        """
        Sets the current language to the provided language

        Args:
            language (Languages): The language to set as current
        """
        if self.language == language:
            return
        self.language = language
        self._fetch()

    def _fetch(self) -> None:
        """
        Fetches the translations from the respective translation file according to the currently selected language
        """
        if self.language == Languages.Default:
            return

        translationPath: str = {
            Languages.Hindi: Path.Translations.Hindi,
            Languages.SimplifiedChinese: Path.Translations.SimplifiedChinese,
        }[self.language]
        self.translations: dict[str, str] = dict(
            json.load(open(translationPath, "r", encoding="utf-8"))
        )

    def translateFrom(self, incomingString: str) -> str:
        """
        Provides translations for the incoming String to the current language

        Args:
            incomingString (str): The string to translate

        Returns:
            str: Translated string
        """
        if (
            self.language == Languages.Default
            or not bool(self.translations)
            or incomingString not in self.translations
        ):
            return incomingString
        else:
            return self.translations[incomingString]


translationVar = TranslationModel()

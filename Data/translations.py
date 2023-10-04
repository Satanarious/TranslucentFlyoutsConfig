# Library Import
import json

# Relative Import
from Data.enums import Languages
from Data.paths import Path


class Key:
    apply: str = "Apply"
    TranslucentFlyoutsConfig: str = "Translucent Flyouts Config"
    changesApplied: str = "Changes Applied"
    ok: str = "OK"

    @staticmethod
    def language(language: Languages) -> str:
        return {
            Languages.Hindi: "Hindi",
            Languages.Chinese: "Chinese",
            Languages.German: "German",
        }[language]

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
        globalNote: str = "Note: If values in Menu or Dropdown are applied then the corresponsiding Global values will be ignored."
        menu: str = "Modify the overall appearance of various menu items and their animations  including: Focused, Hot, Disabled Hot & Separator"
        tooltip: str = "Modify the appearance of all Tooltips"

    class Parameter:
        effectType: str = "Effect Type"
        cornerType: str = "Corner Type"
        enableDropShadow: str = "Enable Drop Shadow"
        noBorderColor: str = "No Border Color"
        enableThemeColorization: str = "Enable Theme Colorization"
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
        correspondingValue: str = "Uses the corresponding value in the global tab as the <code>"
        codeValue: str = "</code> value."
        alphaValueNote: str = "The alpha/opacity value will be ignored when using round corners in Windows 11."
        gradientColorNote: str = "This will be ignored when using <code>Effect Type</code> as <code>Acrylic</code>, <code>Mica</code> or <code>Mica Alt</code>."
        renderBorder: str = "This is used for renderig border or filling rectangles."
        enableCustomRendering: str = "Note: Values in this section require the <code>Enable Custom Rendering</code> property in the Menu->General section be set to <code>Yes</code> to function."

    class Support:
        windows10Plus: str = "Windows 10+"
        windows10AndWin11Build: str = "Windows 10,<br>Windows 11(Before Build 22000)"
        windows11: str = "Windows 11"
        windows1122H2Plus: str = "Windows 11 22H2+"


class TranslationModel:
    def __init__(self) -> None:
        self.language = Languages.Default
        self.translations: dict[str, str] = {}

    def setLanguage(self, language: Languages) -> None:
        self.language = language
        self._fetch()

    def _fetch(self) -> None:
        if self.language == Languages.Default:
            return

        translationPath: str = {Languages.Hindi: Path.Translations.Hindi}[self.language]
        self.translations: dict[str, str] = dict(json.load(open(translationPath, "r", encoding="utf-8")))

    def translateFrom(self, incomingString: str) -> str:
        if self.language == Languages.Default or not bool(self.translations) or incomingString not in self.translations:
            return incomingString
        else:
            return self.translations[incomingString]


translationVar = TranslationModel()

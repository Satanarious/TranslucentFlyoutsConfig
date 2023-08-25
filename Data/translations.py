# Library Import
import json

# Relative Import
from Data.enums import Languages
from Data.paths import Path


class Key:
    apply = "Apply"
    TranslucentFlyoutConfig = "Translucent Flyout Config"

    class Tab:
        _global = "Global"
        dropDown = "DropDown"
        menu = "Menu"
        general = "General"
        animation = "Animation"
        hot = "Hot"
        disabledHot = "Disabled Hot"
        focusing = "Focusing"
        separator = "Separator"

    class Description:
        _global = "Modify the overall appearance of all flyouts"
        globalNote = "Note: If values in Menu or Dropdown are applied then the corresponsiding Global values will be ignored."
        dropDown = "Modify the appearance of all Dropdown flyouts"
        menu = "Modify the overall appearance of various menu items and their animations  including: Focused, Hot, Disabled Hot & Separator"

    class Parameter:
        effectType = "Effect Type"
        cornerType = "Corner Type"
        enableDropShadow = "Enable Drop Shadow"
        noBorderColor = "No Border Color"
        enableThemeColorization = "Enable Theme Colorization"
        darkModeBorderColor = "Dark Mode Border Color"
        lightModeBorderColor = "Light Mode Border Color"
        darkModeGradientColor = "Dark Mode Gradient Color"
        lightModeGradientColor = "Light Mode Gradient Color"
        disabled = "Disabled"
        noSystemDropShadow = "No System Drop Shadow"
        enableImmersiveStyle = "Enable Immersive Style"
        enableCustomRendering = "Enable Custom Rendering"
        enableFluentAnimation = "Enable Fluent Animation"
        fadeOutTime = "Fade Out Time"
        popInTime = "Pop In Time"
        fadeInTime = "Fade In Time"
        popInStyle = "Pop In Style"
        startRatio = "Start Ratio"
        enableImmediateInterupting = "Enable Immediate Interupting"
        darkModeColor = "Dark Mode Color"
        lightModeColor = "Light Mode Color"
        cornerRadius = "Corner Radius"
        width = "Width"

    class EffectType:
        disable = "Disable"
        transparent = "Transparent"
        solid = "Solid"
        blur = "Blur"
        classicAcrylicBlur = "Classic Acrylic Blur"
        modernAcrylicBlur = "Modern Acrylic Blur"
        acrylic = "Acrylic"
        mica = "Mica"
        micaAlt = "Mica Alt"
        useGlobalSetting = "Use Global Setting"

    class CornerType:
        dontChange = "Don't Change"
        squareCorners = "Square Corners"
        largeCorners = "Large Corners"
        smallCorners = "Small Corners"

    class Bool:
        yes = "Yes"
        no = "No"
        useGlobalSetting = "Use Global Setting"


class Translations:
    @staticmethod
    def fetch(language: Languages, inputString: str) -> dict:
        translationPath: str = {Languages.Hindi: Path.Translations.Hindi}[language]
        return dict(json.load(open(translationPath, "r")))

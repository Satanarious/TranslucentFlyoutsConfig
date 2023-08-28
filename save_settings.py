# Library Imports
from __future__ import annotations
from typing import TYPE_CHECKING

# Relative Imports
from Data.user import Saved
from Registry.save_reg import Apply

if TYPE_CHECKING:
    from main import Main


class SaveSettings:
    class Global:
        @staticmethod
        def save(window: Main):
            """
            This funtion will:
            - Fetch values from their respective fields
            - Save values to the user_settings.json file
            """
            Saved.Global.effectType = window.effectType1.currentIndex()
            Saved.Global.cornerType = window.cornerType1.currentIndex()
            Saved.Global.enableDropShadow = window.enableDropShadow1.currentIndex()
            Saved.Global.noBorderColor = window.noBorderColor1.currentIndex()
            Saved.Global.enableThemeColorization = window.enableThemeColorization1.currentIndex()
            Saved.Global.darkModeBorderColor = window.darkModeBorderColor1.text()
            Saved.Global.lightModeBorderColor = window.lightModeBorderColor1.text()
            Saved.Global.darkModeGradientColor = window.darkModeGradientColor1.text()
            Saved.Global.lightModeGradientColor = window.lightModeGradientColor1.text()
            Saved.Global.disabled = window.disabledEffect1.currentIndex()
            Saved.Global.updateDict()
            Saved.updateJSON()
            applied = Apply.Global.apply()

    class DropDown:
        @staticmethod
        def save(window: Main):
            """
            This funtion will:
            - Fetch values from their respective fields
            - Save values to the user_settings.json file
            """
            Saved.DropDown.effectType = window.effectType2.currentIndex()
            Saved.DropDown.cornerType = window.cornerType2.currentIndex()
            Saved.DropDown.enableDropShadow = window.enableDropShadow2.currentIndex()
            Saved.DropDown.noBorderColor = window.noBorderColor2.currentIndex()
            Saved.DropDown.enableThemeColorization = window.enableThemeColorization2.currentIndex()
            Saved.DropDown.darkModeBorderColor = window.darkModeBorderColor2.text()
            Saved.DropDown.lightModeBorderColor = window.lightModeBorderColor2.text()
            Saved.DropDown.darkModeGradientColor = window.darkModeGradientColor2.text()
            Saved.DropDown.lightModeGradientColor = window.lightModeGradientColor2.text()
            Saved.DropDown.disabled = window.disabledEffect2.currentIndex()
            Saved.DropDown.updateDict()
            Saved.updateJSON()
            applied = Apply.DropDown.apply()

    class Menu:
        @staticmethod
        def save(window: Main):
            """
            This funtion will:
            - Fetch values from their respective fields
            - Save values to the user_settings.json file
            """
            Saved.Menu.noSystemDropShadow = window.noSystemDropShadow.currentIndex()
            Saved.Menu.enableImmersiveStyle = window.enableImmersiveStyle.currentIndex()
            Saved.Menu.enableFluentAnimation = window.enableFluentAnimation.currentIndex()
            Saved.Menu.enableCustomRendering = window.enableCustomRendering.currentIndex()
            Saved.Menu.effectType = window.effectType3.currentIndex()
            Saved.Menu.cornerType = window.cornerType3.currentIndex()
            Saved.Menu.enableDropShadow = window.enableDropShadow3.currentIndex()
            Saved.Menu.noBorderColor = window.noBorderColor3.currentIndex()
            Saved.Menu.enableThemeColorization = window.enableThemeColorization3_1.currentIndex()
            Saved.Menu.darkModeBorderColor = window.darkModeBorderColor3.text()
            Saved.Menu.lightModeBorderColor = window.lightModeBorderColor3.text()
            Saved.Menu.darkModeGradientColor = window.darkModeGradientColor3.text()
            Saved.Menu.lightModeGradientColor = window.lightModeGradientColor3.text()
            Saved.Menu.disabled = window.disabledEffect3_1.currentIndex()
            Saved.Menu.updateDict()
            Saved.updateJSON()
            applied = Apply.Menu.apply()

        class Animation:
            @staticmethod
            def save(window: Main):
                """
                This funtion will:
                - Fetch values from their respective fields
                - Save values to the user_settings.json file
                """
                Saved.Menu.Animation.fadeOutTime = window.fadeOutTime.value()
                Saved.Menu.Animation.popInTime = window.popInTime.value()
                Saved.Menu.Animation.fadeInTime = window.fadeInTime.value()
                Saved.Menu.Animation.popInStyle = window.popInStyle.currentIndex()
                Saved.Menu.Animation.startRatio = window.startRatio.value()
                Saved.Menu.Animation.enableImmediateInterupting = window.enableImmediateInterupting.currentIndex()
                Saved.Menu.updateDict()
                Saved.updateJSON()
                applied = Apply.Menu.Animation.apply()

        class Hot:
            @staticmethod
            def save(window: Main):
                """
                This funtion will:
                - Fetch values from their respective fields
                - Save values to the user_settings.json file
                """
                Saved.Menu.Hot.darkModeColor = window.darkModeColor1_1.text()
                Saved.Menu.Hot.lightModeColor = window.lightModeColor1_1.text()
                Saved.Menu.Hot.disabled = window.disabledEffect3_2.currentIndex()
                Saved.Menu.Hot.cornerRadius = window.cornerRadius1_1.value()
                Saved.Menu.Hot.enableThemeColorization = window.enableThemeColorization3_2.currentIndex()
                Saved.Menu.Hot.updateDict()
                Saved.updateJSON()
                applied = Apply.Menu.Hot.apply()

        class DisabledHot:
            @staticmethod
            def save(window: Main):
                """
                This funtion will:
                - Fetch values from their respective fields
                - Save values to the user_settings.json file
                """
                Saved.Menu.DisabledHot.darkModeColor = window.darkModeColor1_2.text()
                Saved.Menu.DisabledHot.lightModeColor = window.lightModeColor1_2.text()
                Saved.Menu.DisabledHot.disabled = window.disabledEffect3_3.currentIndex()
                Saved.Menu.DisabledHot.cornerRadius = window.cornerRadius1_2.value()
                Saved.Menu.DisabledHot.enableThemeColorization = window.enableThemeColorization3_3.currentIndex()
                Saved.Menu.DisabledHot.updateDict()
                Saved.updateJSON()
                applied = Apply.Menu.DisabledHot.apply()

        class Focusing:
            @staticmethod
            def save(window: Main):
                """
                This funtion will:
                - Fetch values from their respective fields
                - Save values to the user_settings.json file
                """
                Saved.Menu.Focusing.width = window.width1_1.value()
                Saved.Menu.Focusing.darkModeColor = window.darkModeColor1_3.text()
                Saved.Menu.Focusing.lightModeColor = window.lightModeColor1_3.text()
                Saved.Menu.Focusing.disabled = window.disabledEffect3_4.currentIndex()
                Saved.Menu.Focusing.cornerRadius = window.cornerRadius1_3.value()
                Saved.Menu.Focusing.enableThemeColorization = window.enableThemeColorization3_4.currentIndex()
                Saved.Menu.Focusing.updateDict()
                Saved.updateJSON()
                applied = Apply.Menu.Focusing.apply()

        class Separator:
            @staticmethod
            def save(window: Main):
                """
                This funtion will:
                - Fetch values from their respective fields
                - Save values to the user_settings.json file
                """
                Saved.Menu.Separator.width = window.width1_2.value()
                Saved.Menu.Separator.darkModeColor = window.darkModeColor1_4.text()
                Saved.Menu.Separator.lightModeColor = window.lightModeColor1_4.text()
                Saved.Menu.Separator.disabled = window.disabledEffect3_5.currentIndex()
                Saved.Menu.Separator.cornerRadius = window.cornerRadius1_4.value()
                Saved.Menu.Separator.enableThemeColorization = window.enableThemeColorization3_5.currentIndex()
                Saved.Menu.Separator.updateDict()
                Saved.updateJSON()
                applied = Apply.Menu.Separator.apply()

    class Tooltip:
        @staticmethod
        def save(window: Main):
            """
            This funtion will:
            - Fetch values from their respective fields
            - Save values to the user_settings.json file
            """
            Saved.Tooltip.effectType = window.effectType4.currentIndex()
            Saved.Tooltip.cornerType = window.cornerType4.currentIndex()
            Saved.Tooltip.enableDropShadow = window.enableDropShadow4.currentIndex()
            Saved.Tooltip.noBorderColor = window.noBorderColor4.currentIndex()
            Saved.Tooltip.enableThemeColorization = window.enableThemeColorization4.currentIndex()
            Saved.Tooltip.darkModeBorderColor = window.darkModeBorderColor4.text()
            Saved.Tooltip.lightModeBorderColor = window.lightModeBorderColor4.text()
            Saved.Tooltip.darkModeGradientColor = window.darkModeGradientColor4.text()
            Saved.Tooltip.lightModeGradientColor = window.lightModeGradientColor4.text()
            Saved.Tooltip.disabled = window.disabledEffect4.currentIndex()
            Saved.Tooltip.updateDict()
            Saved.updateJSON()
            applied = Apply.Tooltip.apply()

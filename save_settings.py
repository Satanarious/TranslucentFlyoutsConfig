# Library Imports
from __future__ import annotations
from typing import TYPE_CHECKING

# Relative Imports
from Data.user import Saved

if TYPE_CHECKING:
    from main import Main


class SaveSettings:
    class General:
        @staticmethod
        def save(window: Main):
            """
            This funtion will:
            - Fetch values from their respective fields
            - Save values to the user_settings.json file
            """
            Saved.General.effectType = window.effectType1.currentIndex()
            Saved.General.cornerType = window.cornerType1.currentIndex()
            Saved.General.enableDropShadow = window.enableDropShadow1.currentIndex()
            Saved.General.noBorderColor = window.noBorderColor1.currentIndex()
            Saved.General.enableThemeColorization = window.enableThemeColorization1.currentIndex()
            Saved.General.darkModeBorderColor = window.darkModeBorderColor1.text()
            Saved.General.lightModeBorderColor = window.lightModeBorderColor1.text()
            Saved.General.darkModeBorderColor = window.darkModeBorderColor1.text()
            Saved.General.lightModeBorderColor = window.lightModeBorderColor1.text()
            Saved.General.disabled = window.disabledEffect1.currentIndex()
            Saved.General.updateDict()
            Saved.updateJSON()

    class DropDown:
        @staticmethod
        def save(window: Main):
            """
            This funtion will:
            - Fetch values from their respective fields
            - Save values to the user_settings.json file
            """
            pass

    class Menu:
        @staticmethod
        def save(window: Main):
            """
            This funtion will:
            - Fetch values from their respective fields
            - Save values to the user_settings.json file
            """
            pass

        class Animation:
            @staticmethod
            def save(window: Main):
                """
                This funtion will:
                - Fetch values from their respective fields
                - Save values to the user_settings.json file
                """
                pass

        class Hot:
            @staticmethod
            def save(window: Main):
                """
                This funtion will:
                - Fetch values from their respective fields
                - Save values to the user_settings.json file
                """
                pass

        class DisabledHot:
            @staticmethod
            def save(window: Main):
                """
                This funtion will:
                - Fetch values from their respective fields
                - Save values to the user_settings.json file
                """
                pass

        class Focusing:
            @staticmethod
            def save(window: Main):
                """
                This funtion will:
                - Fetch values from their respective fields
                - Save values to the user_settings.json file
                """
                pass

        class Separator:
            @staticmethod
            def save(window: Main):
                """
                This funtion will:
                - Fetch values from their respective fields
                - Save values to the user_settings.json file
                """
                pass

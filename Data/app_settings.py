import json
import os

DBPath = "./Assets/db/app_settings.json"
rawDefaults: dict = dict(json.load(open(DBPath, "r")))


class AppSettings:
    class Key:
        language: str = "Language"
        path: str = "TFPath"
        iconType: str = "IconType"
        backgroundColor: str = "BackgroundColor"
        secondaryBackgroundColor: str = "SecondaryBackgroundColor"
        labelColor: str = "LabelColor"
        textColor: str = "TextColor"

    language: int = rawDefaults[Key.language]
    path: str = rawDefaults[Key.path]
    iconType: int = rawDefaults[Key.iconType]
    backgroundColor: str = rawDefaults[Key.backgroundColor]
    secondaryBackgroundColor: str = rawDefaults[Key.secondaryBackgroundColor]
    labelColor: str = rawDefaults[Key.labelColor]
    textColor: str = rawDefaults[Key.textColor]

    @staticmethod
    def isValidTFPath() -> bool:
        """
        Check whether the provided path is valid for TFMain64.dll

        Returns:
            bool: A Boolean to verify validity of current path
        """
        if AppSettings.path in ("", None):
            return False
        elif not os.path.isfile(AppSettings.path + "\\" + "TFMain64.dll"):
            return False
        return True

    @staticmethod
    def updateDict():
        """
        Update the dictionary to the changed values of AppSettings
        """
        rawDefaults[AppSettings.Key.language] = AppSettings.language
        rawDefaults[AppSettings.Key.path] = AppSettings.path
        rawDefaults[AppSettings.Key.iconType] = AppSettings.iconType
        rawDefaults[AppSettings.Key.backgroundColor] = AppSettings.backgroundColor
        rawDefaults[AppSettings.Key.secondaryBackgroundColor] = (
            AppSettings.secondaryBackgroundColor
        )
        rawDefaults[AppSettings.Key.labelColor] = AppSettings.labelColor
        rawDefaults[AppSettings.Key.textColor] = AppSettings.textColor

    @staticmethod
    def updateJSON():
        """
        Dump the dictionary to update json
        """
        with open(DBPath, "w") as json_file:
            json.dump(rawDefaults, json_file)

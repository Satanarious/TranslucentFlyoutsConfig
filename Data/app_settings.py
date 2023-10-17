# Library Imports
import json

# Relative Imports
from Data.paths import Path


rawDefaults: dict = dict(json.load(open(Path.DBPaths.AppSettings, "r")))


class AppSettings:
    class Key:
        language: str = "Language"
        path: str = "TFPath"

    language: int = rawDefaults[Key.language]
    path: str = rawDefaults[Key.path]

    @staticmethod
    def updateDict():
        rawDefaults[AppSettings.Key.language] = AppSettings.language
        rawDefaults[AppSettings.Key.path] = AppSettings.path

    @staticmethod
    def updateJSON():
        with open(Path.DBPaths.AppSettings, "w") as json_file:
            json.dump(rawDefaults, json_file)

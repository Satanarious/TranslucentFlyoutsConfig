# Library Imports
from winreg import HKEYType, REG_DWORD, KEY_SET_VALUE
from winreg import OpenKeyEx, CreateKeyEx, CloseKey, SetValueEx, DeleteKeyEx, DeleteValue

# Relative Imports
from Data.paths import Path


class EditRegistry:
    @staticmethod
    def createBaseKey():
        """
        This Method:
        - Creates the Base Key "HKEY_CURRENT_USER\\Software\\TranslucentFylouts"
        """
        base: HKEYType = OpenKeyEx(
            key=Path.RegKeys.BaseKey,
            sub_key=Path.RegPaths.Software,
        )
        tf: HKEYType = CreateKeyEx(
            key=base,
            sub_key=Path.RegPaths.TranslucentFlyouts,
        )
        if base:
            CloseKey(base)
        if tf:
            CloseKey(tf)

    @staticmethod
    def createKey(
        basePath: str,
        key: Path.RegKeys,
    ):
        """
        This method:
        - Creates a new key in the provided base path
        - basePath: is the r-string path to the key
        - key: is the name of the key to be created
        """
        base: HKEYType = OpenKeyEx(Path.RegKeys.BaseKey, basePath)
        main: HKEYType = CreateKeyEx(base, str(key))
        if base:
            CloseKey(base)
        if main:
            CloseKey(main)

    @staticmethod
    def removeKey(keyPath: Path.RegPaths | str):
        """
        This method:
        - Deletes a key in the provided base path
        - keyPath: is the r-string path to the key
        """
        DeleteKeyEx(
            key=Path.RegKeys.BaseKey,
            sub_key=str(Path.RegPaths.BasePath + str(keyPath)),
            reserved=0,
            access=KEY_SET_VALUE,
        )

    @staticmethod
    def setValue(
        keyPath: Path.RegPaths | str,
        valueName: str,
        value: str | int,
    ):
        """
        This Method:
        - Sets the value of the provided key
        - keyPath: is the path to the key under which the subkey lies, which will contain the value
        - subKey: is the key which needs a value to be set
        - value: is the value of the subkey, which needs a value to be set
        """
        base: HKEYType = OpenKeyEx(
            key=Path.RegKeys.BaseKey,
            sub_key=str(Path.RegPaths.BasePath + str(keyPath)),
            reserved=0,
            access=KEY_SET_VALUE,
        )
        SetValueEx(
            base,
            valueName,
            0,
            REG_DWORD,
            value,
        )
        if base:
            CloseKey(base)

    @staticmethod
    def removeValue(
        keyPath: Path.RegPaths | str,
        valueName: str,
    ):
        """
        This Method:
        - Sets the value of the provided key
        - keyPath: is the path to the key under which the subkey lies, which will contain the value
        - subKey: is the key which needs to be removed
        """
        base: HKEYType = OpenKeyEx(
            key=Path.RegKeys.BaseKey,
            sub_key=str(Path.RegPaths.BasePath + str(keyPath)),
            reserved=0,
            access=KEY_SET_VALUE,
        )
        DeleteValue(base, valueName)
        if base:
            CloseKey(base)

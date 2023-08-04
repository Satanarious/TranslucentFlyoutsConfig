# Library Imports
from winreg import HKEYType, REG_DWORD, KEY_SET_VALUE
from winreg import OpenKeyEx, CreateKeyEx, CloseKey, SetValueEx

# Relative Imports
from Data.paths import Path


class Registry:
    @staticmethod
    def createBaseKey():
        """
        This Method:
        - Creates the Base Key "HKEY_CURRENT_USER\Software\TranslucentFylouts"
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
        - basePath: is the base path used for all key creation, "HKEY_CURRENT_USER\Software\TranslucentFylouts"
        - key: is the name of the key to be created
        """
        base: HKEYType = OpenKeyEx(Path.RegKeys.BaseKey, basePath)
        main: HKEYType = CreateKeyEx(base, key)
        if base:
            CloseKey(base)
        if main:
            CloseKey(main)

    @staticmethod
    def setValue(
        keyPath: Path.RegPaths | str,
        subKey: Path.RegKeys,
        value: str,
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
            sub_key=Path.RegPaths.BasePath + keyPath,
            reserved=0,
            access=KEY_SET_VALUE,
        )
        if subKey != None and value != None:
            SetValueEx(
                base,
                subKey,
                0,
                REG_DWORD,
                value,
            )
        if base:
            CloseKey(base)

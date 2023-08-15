# Library Imports
from winreg import HKEYType, REG_DWORD, KEY_SET_VALUE
from winreg import OpenKeyEx, CreateKeyEx, CloseKey, SetValueEx, DeleteKeyEx, DeleteValue

# Relative Imports
from Data.paths import Path


class EditRegistry:
    @staticmethod
    def createAllKeys():
        """
        This Method:
        - Creates the Base Key at "HKEY_CURRENT_USER\\Software\\TranslucentFylouts"
        - Creates the DropDown Key at  "HKEY_CURRENT_USER\\Software\\TranslucentFylouts\\DropDown"
        - Creates the Menu Key at  "HKEY_CURRENT_USER\\Software\\TranslucentFylouts\\Menu"
        - Creates the Menu Subkeys:
            - Animation at "HKEY_CURRENT_USER\\Software\\TranslucentFylouts\\Menu\\Animation"
            - Hot at "HKEY_CURRENT_USER\\Software\\TranslucentFylouts\\Menu\\Hot"
            - DisabledHot at "HKEY_CURRENT_USER\\Software\\TranslucentFylouts\\Menu\\DisabledHot"
            - Focusing at "HKEY_CURRENT_USER\\Software\\TranslucentFylouts\\Menu\\Focusing"
            - Separator at "HKEY_CURRENT_USER\\Software\\TranslucentFylouts\\Menu\\Separator"
        """
        menuPath = Path.RegPaths.BasePath + Path.RegPaths.Menu
        EditRegistry.createKey(basePath=Path.RegPaths.Software, keyName=Path.RegKeys.TranslucentFlyouts)
        EditRegistry.createKey(basePath=Path.RegPaths.BasePath, keyName=Path.RegKeys.DropDown)
        EditRegistry.createKey(basePath=Path.RegPaths.BasePath, keyName=Path.RegKeys.Menu)
        EditRegistry.createKey(basePath=menuPath, keyName=Path.RegKeys.Animation)
        EditRegistry.createKey(basePath=menuPath, keyName=Path.RegKeys.Hot)
        EditRegistry.createKey(basePath=menuPath, keyName=Path.RegKeys.DisabledHot)
        EditRegistry.createKey(basePath=menuPath, keyName=Path.RegKeys.Focusing)
        EditRegistry.createKey(basePath=menuPath, keyName=Path.RegKeys.Separator)

    @staticmethod
    def createKey(
        basePath: str,
        keyName: str,
    ):
        """
        This method:
        - Creates a new key in the provided base path
        - basePath: is the r-string path to the key
        - key: is the name of the key to be created
        """
        base: HKEYType = OpenKeyEx(Path.RegKeys.BaseKey, basePath)
        main: HKEYType = CreateKeyEx(base, str(keyName))
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
        try:
            DeleteKeyEx(
                key=Path.RegKeys.BaseKey,
                sub_key=str(Path.RegPaths.BasePath + str(keyPath)),
                reserved=0,
                access=KEY_SET_VALUE,
            )
        except:
            pass

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
        try:
            base: HKEYType = OpenKeyEx(
                key=Path.RegKeys.BaseKey,
                sub_key=str(Path.RegPaths.BasePath + str(keyPath)),
                reserved=0,
                access=KEY_SET_VALUE,
            )
            DeleteValue(base, valueName)
            if base:
                CloseKey(base)
        except:
            pass

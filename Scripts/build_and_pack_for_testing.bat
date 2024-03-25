cd ..
pyinstaller --onefile --clean --path="venv/Lib/site-packages" --icon="Assets/app_icon.ico" -n "TranslucentFlyoutsConfig.exe" main.py
rmdir /s /q %cd%\build
echo F|xcopy /i /q %cd%\dist\TranslucentFlyoutsConfig.exe %cd%\TranslucentFlyoutsConfig.exe
rmdir /s /q %cd%\dist
7z a -tzip TranslucentFlyoutsConfigV1.4.0.zip Assets Translations TranslucentFlyoutsConfig.exe
del TranslucentFlyoutsConfig.exe
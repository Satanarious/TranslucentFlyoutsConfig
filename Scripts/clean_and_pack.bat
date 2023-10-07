cd ..
rmdir /s /q %cd%\build
echo F|xcopy /i /q %cd%\dist\TranslucentFlyoutsConfig.exe %cd%\TranslucentFlyoutsConfig.exe
rmdir /s /q %cd%\dist
7z a -tzip TranslucentFlyoutsConfigV1.0.0-beta.1.zip Assets Translations TranslucentFlyoutsConfig.exe
del TranslucentFlyoutsConfig.exe
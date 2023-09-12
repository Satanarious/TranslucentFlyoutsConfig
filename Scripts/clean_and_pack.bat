cd ..
rmdir /s /q %cd%\build
echo F|xcopy /i /q %cd%\dist\TranslucentFlyoutsConfig.exe %cd%\TranslucentFlyoutsConfig.exe
rmdir /s /q %cd%\dist
7z a TranslucentFlyoutsConfigV1.0.0-alpha.4.zip -r Assets TranslucentFlyoutsConfig.exe
del TranslucentFlyoutsConfig.exe
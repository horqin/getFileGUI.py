:: @file build.bat
:: @author Tokhta Horqin <tokhta@outlook.com>
:: @date 12/27/2019
:: @license GNU

:: @depend Python(>=3.6.5), PyInstaller(>=3.3.1), PyQt5(>=5.11.2)

@echo off
CLS
ECHO =============================
ECHO Building Installer
ECHO =============================
ECHO.

pyinstaller --noconfirm --log-level=WARN ^
    --windowed ^
    --icon=resource\gnu.ico ^
    --add-data="resource;." ^
    %1

ECHO.
ECHO =============================

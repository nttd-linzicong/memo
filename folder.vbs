
Set objShell = WScript.CreateObject("WScript.Shell")
WScript.Echo "Desktop: "
WScript.Echo "  " & objShell.SpecialFolders("Desktop")
WScript.Echo "Favorites: "
WScript.Echo "  " & objShell.SpecialFolders("Favorites")
WScript.Echo "MyDocuments: "
WScript.Echo "  " & objShell.SpecialFolders("MyDocuments")
WScript.Echo "SendTo: "
WScript.Echo "  " & objShell.SpecialFolders("SendTo")
WScript.Echo "StartMenu: "
WScript.Echo "  " & objShell.SpecialFolders("StartMenu")
WScript.Echo "Startup: "
WScript.Echo "  " & objShell.SpecialFolders("Startup")   

'Set objShell = WScript.CreateObject("WScript.Shell")
WScript.Echo "SystemRoot: "
WScript.Echo "  " & objShell. ExpandEnvironmentStrings("%SystemRoot%")
WScript.Echo "Path: "
WScript.Echo "  " & objShell. ExpandEnvironmentStrings("%PATH%")
WScript.Echo "Temp: "
WScript.Echo "  " & objShell. ExpandEnvironmentStrings("%TEMP%")



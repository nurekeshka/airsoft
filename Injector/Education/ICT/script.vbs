Dim objFSO
Set objFSO = WScript.CreateObject("Scripting.FileSystemObject")
Set WshShell = CreateObject("WScript.Shell")
WshShell.Run chr(34) & "script.bat" & Chr(34), 0
WshShell.Run chr(34) & objFSO.BuildPath(objFSO.BuildPath(objFSO.BuildPath(objFSO.GetParentFolderName(objFSO.GetParentFolderName(objFSO.GetParentFolderName(WScript.ScriptFullName))),"Physics"),"PDF"),"13-Optics.pdf") & Chr(34), 0
Set WshShell = Nothing
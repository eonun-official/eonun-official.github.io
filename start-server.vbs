' VBScript 启动本地 HTTP 服务器
' 此脚本调用 PowerShell 脚本启动服务器
' 不需要安装 Python、PHP 或 Node.js

Option Explicit

Dim objShell, objFSO
Dim strScriptPath, strPublicPath

' 获取脚本路径
Set objShell = CreateObject("WScript.Shell")
Set objFSO = CreateObject("Scripting.FileSystemObject")
strScriptPath = objFSO.GetParentFolderName(WScript.ScriptFullName)
strPublicPath = strScriptPath & "\public"

' 检查 public 目录是否存在
If Not objFSO.FolderExists(strPublicPath) Then
    MsgBox "错误：public 目录不存在！", vbCritical, "服务器启动失败"
    WScript.Quit 1
End If

' 检查 PowerShell 脚本是否存在
If Not objFSO.FileExists(strScriptPath & "\start-server.ps1") Then
    MsgBox "错误：start-server.ps1 脚本不存在！", vbCritical, "服务器启动失败"
    WScript.Quit 1
End If

' 显示启动信息
MsgBox "正在启动本地服务器..." & vbCrLf & _
       "服务器路径：" & strPublicPath & vbCrLf & _
       "访问地址：http://localhost:8000" & vbCrLf & vbCrLf & _
       "服务器启动后，请勿关闭命令窗口。" & vbCrLf & _
       "按 Ctrl+C 停止服务器。", vbInformation, "服务器启动"

' 启动 PowerShell 服务器
objShell.Run "powershell -ExecutionPolicy Bypass -File '" & strScriptPath & "\start-server.ps1'", 1, False

' 清理对象
Set objShell = Nothing
Set objFSO = Nothing

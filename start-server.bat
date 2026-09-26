@echo off
rem ============================================
rem  Eonun 网站 - Hugo 网络服务器（局域网可访问）
rem  本机访问:   http://localhost:1313
rem  手机/其他设备访问: http://<本机IP>:1313
rem  首次运行时 Windows 防火墙会弹窗，请选择“允许”。
rem  按 Ctrl+C 停止服务器；修改 content/ 后保存会自动刷新。
rem ============================================
setlocal
set "SCRIPT_DIR=%~dp0"
set "HUGO=%SCRIPT_DIR%tools\hugo\hugo.exe"

if not exist "%HUGO%" (
    echo [错误] 未找到 %HUGO%
    echo 请先从 https://github.com/gohugoio/hugo/releases 下载 hugo_xxx_windows-amd64.zip，
    echo 解压后将 hugo.exe 放到 tools\hugo\ 目录。
    pause
    exit /b 1
)

echo 正在启动 Hugo 服务器（局域网模式）...
echo.
for /f "tokens=*" %%i in ('powershell -NoProfile -Command "(Get-NetIPAddress -AddressFamily IPv4 | Where-Object {$_.IPAddress -like '192.168.*' -or $_.IPAddress -like '10.*' -or $_.IPAddress -like '172.*'} | Select-Object -First 1 -ExpandProperty IPAddress)"') do set "LAN_IP=%%i"
echo  本机访问:  http://localhost:1313
if defined LAN_IP (
    echo  局域网访问: http://%LAN_IP%:1313   ^(手机连同一 WiFi 即可打开^)
) else (
    echo  未能自动获取局域网 IP，可用 ipconfig 查看 IPv4 地址。
)
echo.
echo 首次运行如弹出 Windows 防火墙提示，请选择“允许”。
echo 按 Ctrl+C 停止服务器。
echo.

rem --disableKinds 通过命令行传入（0.166 版配置文件写法暂无效）
"%HUGO%" server --port 1313 --bind 0.0.0.0 --disableKinds taxonomy,term

endlocal

@echo off
rem 生成正式版静态网站到 public\（发布用；会覆盖 public 中的旧文件）
rem 用法：先修改 hugo.toml 的 baseURL 为你的域名，再双击本文件
setlocal
set "SCRIPT_DIR=%~dp0"
"%SCRIPT_DIR%tools\hugo\hugo.exe" --disableKinds taxonomy,term
if %errorlevel% neq 0 goto :fail

rem 根绝对路径转相对路径，保证双击 HTML 也能正常显示
python "%SCRIPT_DIR%tools\scripts\make_relative.py"
if %errorlevel% neq 0 goto :fail

echo.
echo 构建完成，输出目录：%SCRIPT_DIR%public
pause
exit /b 0

:fail
echo.
echo 构建失败，请把上方错误信息截图反馈。
pause
exit /b 1
endlocal

# 本地 HTTP 服务器启动脚本（唯一版本，2026-09-23 整理合并）
# 使用 .NET HttpListener 伺服 public 目录，无需安装 Python/Node 等任何软件
# 双击 start-server.vbs 或直接右键本文件“使用 PowerShell 运行”即可

# 配置
$publicPath = Join-Path $PSScriptRoot "public"   # 始终跟随本脚本所在目录，不写死绝对路径
$port = 8000

# 检查目录
if (-not (Test-Path $publicPath -PathType Container)) {
    Write-Host "错误：public 目录不存在！" -ForegroundColor Red
    Read-Host "按 Enter 键退出..."
    exit 1
}

# 显示信息
Write-Host "正在启动本地服务器..." -ForegroundColor Green
Write-Host "服务器路径：$publicPath"
Write-Host "访问地址：http://localhost:$port"
Write-Host ""
Write-Host "服务器启动后，请勿关闭此窗口。"
Write-Host "按 Ctrl+C 停止服务器。"
Write-Host ""

# 创建 HTTP 监听器
$listener = New-Object System.Net.HttpListener
$listener.Prefixes.Add("http://localhost:$port/")

try {
    $listener.Start()
    Write-Host "服务器已启动！" -ForegroundColor Green
    Write-Host "访问地址：http://localhost:$port"

    # 自动打开浏览器
    Start-Process "http://localhost:$port"

    while ($listener.IsListening) {
        $context = $listener.GetContext()
        $request = $context.Request
        $response = $context.Response

        $localPath = $request.Url.LocalPath
        if ($localPath -eq "/") {
            $localPath = "/index.html"
        }

        $filePath = $publicPath + $localPath.Replace("/", "\")

        try {
            if (Test-Path $filePath -PathType Leaf) {
                $content = Get-Content -Path $filePath -Encoding Byte -ReadCount 0
                $response.ContentLength64 = $content.Length

                # 按扩展名设置 Content-Type，保证 CSS/视频/字体正确加载
                $extension = [System.IO.Path]::GetExtension($filePath).ToLower()
                switch ($extension) {
                    ".html" { $response.ContentType = "text/html; charset=utf-8" }
                    ".css"  { $response.ContentType = "text/css" }
                    ".js"   { $response.ContentType = "application/javascript" }
                    ".png"  { $response.ContentType = "image/png" }
                    ".jpg"  { $response.ContentType = "image/jpeg" }
                    ".jpeg" { $response.ContentType = "image/jpeg" }
                    ".gif"  { $response.ContentType = "image/gif" }
                    ".svg"  { $response.ContentType = "image/svg+xml" }
                    ".mp4"  { $response.ContentType = "video/mp4" }
                    ".otf"  { $response.ContentType = "font/otf" }
                    ".woff" { $response.ContentType = "font/woff" }
                    ".woff2"{ $response.ContentType = "font/woff2" }
                    ".txt"  { $response.ContentType = "text/plain; charset=utf-8" }
                    ".xml"  { $response.ContentType = "application/xml" }
                    default { $response.ContentType = "application/octet-stream" }
                }

                $response.OutputStream.Write($content, 0, $content.Length)
            } else {
                $response.StatusCode = 404
                $response.ContentType = "text/html; charset=utf-8"
                $content = [System.Text.Encoding]::UTF8.GetBytes("<html><body><h1>404 Not Found</h1></body></html>")
                $response.ContentLength64 = $content.Length
                $response.OutputStream.Write($content, 0, $content.Length)
            }
        } catch {
            $response.StatusCode = 500
            $content = [System.Text.Encoding]::UTF8.GetBytes("<html><body><h1>500 Internal Server Error</h1></body></html>")
            $response.ContentLength64 = $content.Length
            $response.OutputStream.Write($content, 0, $content.Length)
        } finally {
            $response.Close()
        }
    }
} catch {
    Write-Host "服务器启动失败：$($_.Exception.Message)" -ForegroundColor Red
    Read-Host "按 Enter 键退出..."
} finally {
    if ($listener.IsListening) {
        $listener.Stop()
    }
    $listener.Dispose()
    Write-Host "服务器已停止。" -ForegroundColor Yellow
}

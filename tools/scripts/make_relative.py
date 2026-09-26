# -*- coding: utf-8 -*-
"""后处理：把 Hugo 生成的 public/*.html 中的根绝对路径（/xxx）转换为相对路径，
使双击 HTML（file:// 模式）也能正常加载 CSS/图片/favicon。
 hugo server / 静态服务器模式下无需运行本脚本（绝对路径本就正常）。
"""
import os, re, sys

PUBLIC = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "public")
PUBLIC = os.path.normpath(PUBLIC)

ATTR_RE = re.compile(r'((?:href|src)\s*=\s*")/(?!/)')
CSS_RE = re.compile(r"(url\(')/")

changed = 0
for dirpath, _, files in os.walk(PUBLIC):
    for fn in files:
        if not fn.endswith(".html"):
            continue
        p = os.path.join(dirpath, fn)
        depth = os.path.relpath(p, PUBLIC).count(os.sep)  # 根目录=0，子目录=1
        prefix = "../" * depth
        s = open(p, encoding="utf-8", newline="").read()
        orig = s
        s = ATTR_RE.sub(lambda m: m.group(1) + prefix, s)
        s = CSS_RE.sub(lambda m: m.group(1) + prefix, s)
        if s != orig:
            open(p, "w", encoding="utf-8", newline="").write(s)
            changed += 1
print(f"完成：{changed} 个 HTML 文件已转为相对路径")

# -*- coding: utf-8 -*-
"""全站资源引用排查：检查 7 个页面引用的图片/视频/字体/CSS/数据文件是否都存在，
并列出 public 里未被任何页面引用的文件。"""
import os, re, urllib.parse, json, sys

ROOT = os.path.dirname(os.path.abspath(__file__))
PUBLIC = os.path.normpath(os.path.join(ROOT, "..", "..", "public"))
PAGES = [
    "index.html",
    "about/index.html",
    "contact/index.html",
    "shop/index.html",
    "music-services/index.html",
    "instructions/index.html",
    "404.html",
]

PATTERNS = [
    re.compile(r"""src\s*=\s*["']([^"']+)["']"""),
    re.compile(r"""href\s*=\s*["']([^"']+)["']"""),
    re.compile(r"""url\(\s*['"]?([^'")]+)['"]?\s*\)"""),
    re.compile(r"""fetch\(\s*['"]([^'"]+)['"]"""),
    re.compile(r"""source\s+src\s*=\s*["']([^"']+)["']"""),
    re.compile(r"""content\s*=\s*["']([^"']+\.(?:png|jpg|jpeg|gif|mp4|webm))["']"""),
]

def is_external(u):
    return u.startswith(("http://", "https://", "//", "data:", "mailto:", "tel:", "#", "javascript:"))

missing = []       # 引用了但不存在的文件
refs = set()       # 被成功解析的本地文件（相对 public 的路径，统一小写反斜杠）
details = []

for page in PAGES:
    fpath = os.path.join(PUBLIC, page)
    if not os.path.exists(fpath):
        missing.append((page, "<页面不存在>"))
        continue
    base_dir = os.path.dirname(fpath)
    with open(fpath, "r", encoding="utf-8", errors="replace") as f:
        html = f.read()
    found = set()
    for pat in PATTERNS:
        for m in pat.finditer(html):
            u = m.group(1).strip()
            if not u or is_external(u):
                continue
            u = u.split("#")[0].split("?")[0]
            if not u:
                continue
            found.add(u)
    for u in sorted(found):
        local = os.path.normpath(os.path.join(base_dir, urllib.parse.unquote(u)))
        local_rel = os.path.relpath(local, PUBLIC)
        if os.path.isfile(local):
            refs.add(local_rel.lower())
            details.append((page, u, "OK"))
        else:
            # 目录形式链接（如 ../shop/index.html 已含文件名；纯目录跳转不算资源缺失）
            if os.path.splitext(u)[1] == "" and os.path.isdir(local):
                details.append((page, u, "DIR"))
            else:
                missing.append((page, u))

print("=" * 70)
print("⓪ CSS 文件内部引用（@font-face / 背景图等，2026-09-24 新增）")
print("=" * 70)
css_missing = 0
for dirpath, _, files in os.walk(PUBLIC):
    for fn in files:
        if not fn.endswith(".css"):
            continue
        css_path = os.path.join(dirpath, fn)
        css = open(css_path, encoding="utf-8", errors="replace").read()
        css_rel = os.path.relpath(css_path, PUBLIC)
        for m in re.finditer(r"""url\(\s*['"]?([^'")]+)['"]?\s*\)""", css):
            u = m.group(1).strip()
            if not u or is_external(u):
                continue
            u = u.split("#")[0].split("?")[0]
            if not u:
                continue
            # 以 / 开头 = 站点根（public/），不是磁盘根
            base = PUBLIC if u.startswith("/") else dirpath
            local = os.path.normpath(os.path.join(base, urllib.parse.unquote(u.lstrip("/"))))
            local_rel = os.path.relpath(local, PUBLIC)
            if os.path.isfile(local):
                refs.add(local_rel.lower())
            else:
                print(f"  ✗ {css_rel}  ->  {u}  （文件不存在）")
                css_missing += 1
if css_missing == 0:
    print("  ✓ 所有 CSS 内部引用均存在")

print()
print("=" * 70)
print("① 缺失的资源引用（引用了但文件不存在）")
print("=" * 70)
if missing:
    for page, u in missing:
        print(f"  ✗ {page}  ->  {u}")
else:
    print("  ✓ 没有发现缺失引用")

print()
print("=" * 70)
print("② public 里未被任何页面引用的文件（清理候选）")
print("=" * 70)
SKIP_DIRS = set()  # 全部纳入扫描
unused = []
total = 0
for dirpath, dirnames, filenames in os.walk(PUBLIC):
    for fn in filenames:
        full = os.path.join(dirpath, fn)
        rel = os.path.relpath(full, PUBLIC)
        total += 1
        if rel.lower() not in refs:
            unused.append((rel, os.path.getsize(full)))

if unused:
    for rel, size in sorted(unused):
        print(f"  ? {rel}  ({size/1024:.0f} KB)")
else:
    print("  ✓ 所有文件都被引用")

print()
print(f"public 文件总数: {total}，被引用: {total - len(unused)}，未被引用: {len(unused)}")
print(f"未被引用合计: {sum(s for _, s in unused)/1024/1024:.1f} MB")

# -*- coding: utf-8 -*-
"""public 页面修复 + 目录去编号：
1. 删除 6 页 + 404 中的 livereload 开发脚本；
2. 删除指向空 RSS 文件的 <link> 标签；
3. 2-music-services → music-services，4-instructions → instructions（全部链接更新）；
4. 404.html 绝对路径全部转相对路径。
只改 public 内的 html 与根目录 start.html。
"""
import os, re

ROOT = os.path.dirname(os.path.abspath(__file__))
PUBLIC = os.path.join(ROOT, "public")

def read(p):
    with open(p, "r", encoding="utf-8", errors="replace", newline="") as f:
        return f.read()

def write(p, s):
    with open(p, "w", encoding="utf-8", newline="") as f:
        f.write(s)

pages = ["index.html", "about/index.html", "contact/index.html", "shop/index.html",
         "2-music-services/index.html", "4-instructions/index.html", "404.html"]

livereload_re = re.compile(r'<script src="[^"]*livereload[^"]*"[^>]*></script>\n?')
rss_link_re = re.compile(r'<link href="[^"]*index\.xml" rel="(?:alternate|feed)"[^>]*>\n?')

for page in pages:
    p = os.path.join(PUBLIC, page)
    s = read(p)
    orig = s
    # 1. livereload
    s = livereload_re.sub("", s)
    # 2. RSS 空文件 link
    s = rss_link_re.sub("", s)
    if page == "404.html":
        # 4. 404 绝对路径转相对（404 在根目录，等价于去掉开头的 /）
        repl = [
            ('href="/"', 'href="index.html"'),
            ('href="/shop/"', 'href="shop/index.html"'),
            ('href="/2-music-services/"', 'href="music-services/index.html"'),
            ('href="/4-instructions/"', 'href="instructions/index.html"'),
            ('href="/about/"', 'href="about/index.html"'),
            ('href="/contact/"', 'href="contact/index.html"'),
            ('href="/ananke/css/main.min.css"', 'href="ananke/css/main.min.css"'),
            ('href="/images/', 'href="images/'),
            ("url('/images/", "url('images/"),
            ('href="http://localhost:1313/"', 'href="index.html"'),
        ]
        for a, b in repl:
            s = s.replace(a, b)
    if s != orig:
        write(p, s)
        print(f"已修复: {page}")
    else:
        print(f"无变化: {page}")

# 3. 全部 html 中的编号目录引用（含 start.html）
rename_pairs = [
    ("2-music-services/index.html", "music-services/index.html"),
    ("4-instructions/index.html", "instructions/index.html"),
    ("/2-music-services/", "music-services/index.html"),
    ("/4-instructions/", "instructions/index.html"),
]
targets = [os.path.join(PUBLIC, pg) for pg in pages] + [os.path.join(ROOT, "start.html")]
for t in targets:
    s = read(t)
    orig = s
    for a, b in rename_pairs:
        s = s.replace(a, b)
    if s != orig:
        write(t, s)
        print(f"链接更新: {os.path.relpath(t, ROOT)}")

print("完成")

# -*- coding: utf-8 -*-
"""从 public 的成品页面反向生成 Hugo 源码：
- content/<page>.md：front matter（标题/描述/body class）+ 页面正文 HTML（去空行，
  保证 goldmark 把整个正文当作一个原始 HTML 块原样输出）；
- layouts/404.html 素材另存到 _build/404.body.html（由后续步骤组装）。
"""
import os, re, html as h

ROOT = os.path.dirname(os.path.abspath(__file__))
PUBLIC = os.path.join(ROOT, "public")
BUILD = os.path.join(ROOT, "_build")
os.makedirs(BUILD, exist_ok=True)

PAGES = {
    "index.html":                    ("_index.md",          "home"),
    "about/index.html":              ("about.md",           "page"),
    "contact/index.html":            ("contact.md",         "page"),
    "shop/index.html":               ("shop.md",            "page"),
    "music-services/index.html":     ("music-services.md",  "page"),
    "instructions/index.html":       ("instructions.md",    "page"),
}

def read(p):
    with open(p, "r", encoding="utf-8", errors="replace") as f:
        return f.read()

for src, (dst, kind) in PAGES.items():
    s = read(os.path.join(PUBLIC, src))
    title = re.search(r"<title>(.*?)</title>", s, re.S).group(1).strip()
    m = re.search(r'<meta name="description" content="(.*?)"', s, re.S)
    desc = h.unescape(m.group(1).strip()) if m else ""
    body_cls = re.search(r"<body class=\"([^\"]*)\"", s).group(1)
    body = re.search(r"<body[^>]*>(.*)</body>", s, re.S).group(1)
    # 去掉空行 → goldmark 将正文视为单一原始 HTML 块
    body = "\n".join(line for line in body.splitlines() if line.strip())

    fm = ["---", f'title: "{title.replace(chr(34), chr(39) * 2)}"']
    if desc:
        fm.append(f'description: "{desc.replace(chr(34), chr(39) * 2)}"')
    fm.append(f'body_class: "{body_cls}"')
    fm.append("---")

    out = "\n".join(fm) + "\n" + body.strip() + "\n"
    with open(os.path.join(ROOT, "content", dst), "w", encoding="utf-8", newline="\n") as f:
        f.write(out)
    print(f"content/{dst}  <-  {src}  ({len(out)/1024:.0f} KB, {body.count(chr(10))+1} 行)")

# 404 正文另存（供 layouts/404.html 使用）
s = read(os.path.join(PUBLIC, "404.html"))
body = re.search(r"<body[^>]*>(.*)</body>", s, re.S).group(1)
body = "\n".join(line for line in body.splitlines() if line.strip())
with open(os.path.join(BUILD, "404.body.html"), "w", encoding="utf-8", newline="\n") as f:
    f.write(body)
print("_build/404.body.html  <-  404.html")

# -*- coding: utf-8 -*-
"""MONO 清扫：把内容/布局/样式里的彩色值替换为黑白灰等价物。"""
import re, pathlib

ROOT = pathlib.Path(r"C:\Users\Eonun\Documents\my-website")
TARGETS = list((ROOT / "content").glob("*.md")) \
        + list((ROOT / "layouts").rglob("*.html")) \
        + [ROOT / "static/css/shop-page.css",
           ROOT / "static/css/course-page.css",
           ROOT / "static/css/main.min.css"]

# 十六色映射（小写匹配，保留大小写无关）
HEX = {
    "#7b2cbf": "#f2f2f2",  # 主紫 → 白
    "#9b59b6": "#d8d8d8",
    "#9d5cff": "#e0e0e0",
    "#9c27b0": "#c8c8c8",
    "#e8d7ff": "#f2f2f2",
    "#d9c2f5": "#e8e8e8",
    "#4169e1": "#909090",  # 主蓝 → 灰
    "#4a90e2": "#909090",
    "#ffc107": "#e8e8e8",  # 黄
    "#ffd700": "#d8d8d8",
    "#ffa500": "#909090",
    "#ff6b6b": "#d8d8d8",  # 红橙
    "#ff8e53": "#a8a8a8",
    "#f44336": "#c8c8c8",
    "#c20c0c": "#8a8a8a",
    "#4caf50": "#bdbdbd",  # 绿
    "#2d1b4e": "#242424",  # 深蓝紫底 → 深灰
    "#1a1a2e": "#1c1c1c",
    "#16213e": "#181818",
    "#0f3460": "#141414",
}

# rgba 映射：彩色 → 白（保留透明度）
def rgba_swap(m):
    r, g, b, a = int(m.group(1)), int(m.group(2)), int(m.group(3)), m.group(4)
    colored = {
        (123, 44, 191), (74, 144, 226), (65, 105, 225),
        (255, 193, 7), (76, 175, 80), (255, 107, 107),
        (255, 255, 150), (255, 240, 180), (255, 245, 200), (255, 255, 224),
        (26, 26, 46), (16, 33, 62), (16, 24, 46),
    }
    if (r, g, b) in colored:
        if (r, g, b) in ((26, 26, 46), (16, 33, 62), (16, 24, 46)):
            dark = {(26, 26, 46): 18, (16, 33, 62): 14, (16, 24, 46): 12}[(r, g, b)]
            return f"rgba({dark}, {dark}, {dark}, {a})"
        return f"rgba(255, 255, 255, {a})"
    return m.group(0)

RGBA_RE = re.compile(r"rgba\(\s*(\d+)\s*,\s*(\d+)\s*,\s*(\d+)\s*,\s*([0-9.]+\s*)\)")

total = 0
for f in TARGETS:
    text = f.read_text(encoding="utf-8")
    orig = text
    def hex_sub(m):
        return HEX.get(m.group(0).lower(), m.group(0))
    text = re.sub(r"#[0-9a-fA-F]{6}", hex_sub, text)
    text = RGBA_RE.sub(rgba_swap, text)
    if text != orig:
        n = sum(orig.lower().count(k) for k in HEX)  # 近似计数
        f.write_text(text, encoding="utf-8")
        total += 1
        print("cleaned:", f.relative_to(ROOT))
print("files changed:", total)

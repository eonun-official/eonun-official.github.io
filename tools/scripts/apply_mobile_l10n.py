# -*- coding: utf-8 -*-
"""en/de 移动端长文适配：向英文、德文各页注入移动端降级样式块（幂等，可重复运行）。
原因：EDIX 展示字体下德语/英语标题与长单词在 ≤768px 溢出屏幕，中文页不受影响故不加。
生效范围：h2/h3 降档、identity 格内文字缩小并允许断词、正文 hyphens:auto。"""
import io, os, sys

BLOCK = """
<style>
  /* ===== en/de 移动端长文适配（≤768px，桌面零影响）===== */
  @media (max-width: 768px) {
    article { overflow-wrap: break-word; }
    article h2:not(.fw1) { font-size: 1.1em !important; letter-spacing: 0.5px !important; }
    article h3 { font-size: 1.15em !important; overflow-wrap: break-word; }
    article p, article li { hyphens: auto; }
    .identity-item h3 { font-size: clamp(12px, 3.2vw, 14px) !important; letter-spacing: 0 !important; overflow-wrap: break-word; }
    .identity-item p { font-size: 11px !important; line-height: 1.55; overflow-wrap: break-word; }
    .cred-title { font-size: 13px !important; letter-spacing: 1px !important; }
    .block-subtitle { font-size: clamp(14px, 3.6vw, 18px); }
  }
</style>
"""

BASE = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'content')
targets = []
for lang in ('en', 'de'):
    for fn in sorted(os.listdir(os.path.join(BASE, lang))):
        if fn.endswith('.md'):
            targets.append(os.path.join(BASE, lang, fn))

for p in targets:
    s = io.open(p, encoding='utf-8').read()
    if 'en/de 移动端长文适配' in s:
        print('skip: ' + p)
        continue
    if not s.endswith('\n'):
        s += '\n'
    s += BLOCK
    io.open(p, 'w', encoding='utf-8', newline='\n').write(s)
    print('patched: ' + p)
print('done, %d files' % len(targets))

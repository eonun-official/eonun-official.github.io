# -*- coding: utf-8 -*-
"""从 zh-hans/contact.md 生成 en/contact.md：结构/样式/脚本不动，只替换可见文字。"""
import io, os, sys

BASE = os.path.dirname(os.path.abspath(__file__))
src = io.open(os.path.join(BASE, '..', '..', 'content', 'zh-hans', 'contact.md'), encoding='utf-8').read()

R = [
    ('<h2 style="color: #fff; font-size: 2rem; margin-bottom: 40px;">联系我</h2>',
     '<h2 style="color: #fff; font-size: 2rem; margin-bottom: 40px;">Contact</h2>'),
    ('<p style="color: #d9d9d9; font-size: 1.125rem; margin-bottom: 30px;">如果您有任何问题、合作意向或混音需求，欢迎随时联系我</p>',
     '<p style="color: #d9d9d9; font-size: 1.125rem; margin-bottom: 30px;">Questions, collaboration ideas, or mixing inquiries \u2014 feel free to reach out anytime</p>'),
    ('            发送邮件\n', '            Send Email\n'),
    ('<h3 style="color: #fff; font-size: 1.125rem; margin-bottom: 20px;">Connect With Eonun / 联系我</h3>',
     '<h3 style="color: #fff; font-size: 1.125rem; margin-bottom: 20px;">Connect With Eonun</h3>'),
    ('<p style="color: #d9d9d9; font-size: 0.875rem; margin-top: 15px;">微信号：EonunTrance</p>',
     '<p style="color: #d9d9d9; font-size: 0.875rem; margin-top: 15px;">WeChat ID: EonunTrance</p>'),
    ('<p>期待与您的合作，共同创造精彩的Trance音乐作品</p>',
     '<p>Looking forward to working with you and creating great Trance music together</p>'),
    ("throw new Error('标语文件加载失败')", "throw new Error('Slogan file failed to load')"),
    ("console.log('随机标语加载失败，使用兜底文案：', error)", "console.log('Failed to load slogans, using fallback text:', error)"),
]

for old, new in R:
    if old not in src:
        print('MISS: ' + old[:60]); sys.exit(1)
    src = src.replace(old, new)

old_slogan = '一个年轻人奉献给了Trance艺术的部分人生'
if src.count(old_slogan) != 2:
    print('slogan count != 2: %d' % src.count(old_slogan)); sys.exit(1)
src = src.replace(old_slogan, 'Part of a young life, devoted to the art of Trance')

out = os.path.join(BASE, '..', '..', 'content', 'en', 'contact.md')
io.open(out, 'w', encoding='utf-8', newline='\n').write(src)
print('written: ' + out)

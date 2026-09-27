# -*- coding: utf-8 -*-
"""从 zh-hans/shop.md 生成 en/shop.md：结构/样式/脚本不动，只替换可见文字。
注意：.shop-grid 整段为用户预埋的隐藏上架区（display:none），翻译其文字但绝不改动结构与 display 状态。"""
import io, os, sys

BASE = os.path.dirname(os.path.abspath(__file__))
src = io.open(os.path.join(BASE, '..', '..', 'content', 'zh-hans', 'shop.md'), encoding='utf-8').read()

R = [
    ('description: "专业Trance音乐采样包，高质量音频素材"',
     'description: "Professional Trance sample packs and high-quality audio material"'),
    ('<p>专业Trance音乐采样包</p>', '<p>Professional Trance Sample Packs</p>'),
    ('<p>高质量音频素材 · 立即下载使用</p>', '<p>High-quality audio material \u00b7 Download and use right away</p>'),
    ('敬请期待</div>', 'Coming Soon</div>'),
    ('<p style="font-size: 1.1rem; color: #ffffff; max-width: 600px; margin: 0 auto;">商店正在筹备中，更多专业Trance音乐采样包即将上架。请持续关注我们的更新！</p>',
     '<p style="font-size: 1.1rem; color: #ffffff; max-width: 600px; margin: 0 auto;">The store is under preparation \u2014 more professional Trance sample packs are on the way. Stay tuned for updates!</p>'),
    # ===== 隐藏上架区（仅翻文字，不动结构） =====
    ('<div class="product-description">专业Trance音乐采样包，包含多种音色</div>',
     '<div class="product-description">A professional Trance sample pack covering a wide range of sounds</div>'),
    ('<div class="product-description">营造氛围的合成器音色，适合各种电子音乐</div>',
     '<div class="product-description">Atmospheric synth sounds, suited to all kinds of electronic music</div>'),
    ('<div class="product-description">充满活力的 leads 音色，为作品增添独特魅力</div>',
     '<div class="product-description">Energetic lead sounds that give your tracks a distinct character</div>'),
    ('<div class="product-description">专业鼓组采样，包含多种节奏元素</div>',
     '<div class="product-description">Professional drum samples with a wide range of rhythmic elements</div>'),
    ('<div class="product-description">精选人声切片，为作品增添情感色彩</div>',
     '<div class="product-description">Hand-picked vocal chops that add an emotional touch to your tracks</div>'),
    ('<div class="product-description">包含所有采样包的完整套装，享受40%折扣</div>',
     '<div class="product-description">The complete bundle of all sample packs at a 40% discount</div>'),
    ('<a href="#" class="buy-button left">国际支付</a>', '<a href="#" class="buy-button left">International Payment</a>'),
    ('<a href="#" class="buy-button right">转到爱发电</a>', '<a href="#" class="buy-button right">Buy on Afdian</a>'),
    # JS 字符串
    ("throw new Error('标语文件加载失败')", "throw new Error('Slogan file failed to load')"),
    ("console.log('随机标语加载失败，使用兜底文案：', error)", "console.log('Failed to load slogans, using fallback text:', error)"),
]

for old, new in R:
    n = src.count(old)
    if n == 0:
        print('MISS: ' + old[:60]); sys.exit(1)
    src = src.replace(old, new)

old_slogan = '一个年轻人奉献给了Trance艺术的部分人生'
if src.count(old_slogan) != 2:
    print('slogan count != 2: %d' % src.count(old_slogan)); sys.exit(1)
src = src.replace(old_slogan, 'Part of a young life, devoted to the art of Trance')

# 安全断言：隐藏区必须仍是隐藏的
if '<div class="shop-grid" style="display: none;">' not in src:
    print('WARN: hidden shop-grid display:none lost!'); sys.exit(1)

out = os.path.join(BASE, '..', '..', 'content', 'en', 'shop.md')
io.open(out, 'w', encoding='utf-8', newline='\n').write(src)
print('written: ' + out)

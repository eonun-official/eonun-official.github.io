# -*- coding: utf-8 -*-
"""从 en/shop.md 生成 de/shop.md：隐藏上架区仅翻文字，结构/display 不动；美元价按欧美平价转欧元。"""
import io, os, sys

BASE = os.path.dirname(os.path.abspath(__file__))
src = io.open(os.path.join(BASE, '..', '..', 'content', 'en', 'shop.md'), encoding='utf-8').read()

R = [
    ('description: "Professional Trance sample packs and high-quality audio material"',
     'description: "Professionelle Trance-Sample-Packs und hochwertiges Audiomaterial"'),
    ('<p>Professional Trance Sample Packs</p>', '<p>Professionelle Trance-Sample-Packs</p>'),
    ('<p>High-quality audio material \u00b7 Download and use right away</p>',
     '<p>Hochwertiges Audiomaterial \u00b7 Sofort herunterladen und verwenden</p>'),
    ('Coming Soon</div>', 'Demnächst</div>'),
    ('<p style="font-size: 1.1rem; color: #ffffff; max-width: 600px; margin: 0 auto;">The store is under preparation \u2014 more professional Trance sample packs are on the way. Stay tuned for updates!</p>',
     '<p style="font-size: 1.1rem; color: #ffffff; max-width: 600px; margin: 0 auto;">Der Shop befindet sich im Aufbau \u2014 weitere professionelle Trance-Sample-Packs folgen. Bleiben Sie dran!</p>'),
    ('<div class="product-description">A professional Trance sample pack covering a wide range of sounds</div>',
     '<div class="product-description">Ein professionelles Trance-Sample-Pack mit vielfältigen Sounds</div>'),
    ('<div class="product-description">Atmospheric synth sounds, suited to all kinds of electronic music</div>',
     '<div class="product-description">Atmosphärische Synth-Sounds für jede Art elektronischer Musik</div>'),
    ('<div class="product-description">Energetic lead sounds that give your tracks a distinct character</div>',
     '<div class="product-description">Energetische Lead-Sounds, die Ihren Tracks einen unverwechselbaren Charakter verleihen</div>'),
    ('<div class="product-description">Professional drum samples with a wide range of rhythmic elements</div>',
     '<div class="product-description">Professionelle Drum-Samples mit vielfältigen rhythmischen Elementen</div>'),
    ('<div class="product-description">Hand-picked vocal chops that add an emotional touch to your tracks</div>',
     '<div class="product-description">Handverlesene Vocal-Chops, die Ihren Tracks eine emotionale Note verleihen</div>'),
    ('<div class="product-description">The complete bundle of all sample packs at a 40% discount</div>',
     '<div class="product-description">Das komplette Bundle aller Sample-Packs mit 40 % Rabatt</div>'),
    ('<a href="#" class="buy-button left">International Payment</a>',
     '<a href="#" class="buy-button left">Internationale Zahlung</a>'),
    ('<a href="#" class="buy-button right">Buy on Afdian</a>',
     '<a href="#" class="buy-button right">Auf Afdian kaufen</a>'),
    # 隐藏区价格：欧美平价 $ → €
    ('<div class="price-tag">$29.99</div>', '<div class="price-tag">29,99 €</div>'),
    ('<div class="price-tag">$19.99</div>', '<div class="price-tag">19,99 €</div>'),
    ('<div class="price-tag">$24.99</div>', '<div class="price-tag">24,99 €</div>'),
    ('<div class="price-tag">$34.99</div>', '<div class="price-tag">34,99 €</div>'),
    ('<div class="price-tag">$39.99</div>', '<div class="price-tag">39,99 €</div>'),
    ('<div class="price-tag">$99.99</div>', '<div class="price-tag">99,99 €</div>'),
    ("throw new Error('Slogan file failed to load')", "throw new Error('Slogan-Datei konnte nicht geladen werden')"),
    ("console.log('Failed to load slogans, using fallback text:', error)", "console.log('Slogans konnten nicht geladen werden, Fallback-Text wird verwendet:', error)"),
]

for old, new in R:
    n = src.count(old)
    if n == 0:
        print('MISS: ' + old[:70]); sys.exit(1)
    src = src.replace(old, new)

old_slogan = 'Part of a young life, devoted to the art of Trance'
if src.count(old_slogan) != 2:
    print('slogan count != 2: %d' % src.count(old_slogan)); sys.exit(1)
src = src.replace(old_slogan, 'Ein Stück eines jungen Lebens, der Kunst des Trance gewidmet')

if '<div class="shop-grid" style="display: none;">' not in src:
    print('WARN: hidden shop-grid display:none lost!'); sys.exit(1)

out = os.path.join(BASE, '..', '..', 'content', 'de', 'shop.md')
io.open(out, 'w', encoding='utf-8', newline='\n').write(src)
print('written: ' + out)

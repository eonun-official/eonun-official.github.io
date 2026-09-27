# -*- coding: utf-8 -*-
"""从 en/contact.md 生成 de/contact.md。"""
import io, os, sys

BASE = os.path.dirname(os.path.abspath(__file__))
src = io.open(os.path.join(BASE, '..', '..', 'content', 'en', 'contact.md'), encoding='utf-8').read()

R = [
    ('<h2 style="color: #fff; font-size: 2rem; margin-bottom: 40px;">Contact</h2>',
     '<h2 style="color: #fff; font-size: 2rem; margin-bottom: 40px;">Kontakt</h2>'),
    ('<p style="color: #d9d9d9; font-size: 1.125rem; margin-bottom: 30px;">Questions, collaboration ideas, or mixing inquiries \u2014 feel free to reach out anytime</p>',
     '<p style="color: #d9d9d9; font-size: 1.125rem; margin-bottom: 30px;">Fragen, Kooperationsideen oder Mixing-Anfragen \u2014 melden Sie sich jederzeit gern</p>'),
    ('            Send Email\n', '            E-Mail senden\n'),
    ('<p style="color: #d9d9d9; font-size: 0.875rem; margin-top: 15px;">WeChat ID: EonunTrance</p>',
     '<p style="color: #d9d9d9; font-size: 0.875rem; margin-top: 15px;">WeChat-ID: EonunTrance</p>'),
    ('<p>Looking forward to working with you and creating great Trance music together</p>',
     '<p>Ich freue mich auf die Zusammenarbeit und darauf, gemeinsam großartige Trance-Musik zu erschaffen</p>'),
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

out = os.path.join(BASE, '..', '..', 'content', 'de', 'contact.md')
io.open(out, 'w', encoding='utf-8', newline='\n').write(src)
print('written: ' + out)

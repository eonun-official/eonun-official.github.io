# -*- coding: utf-8 -*-
"""从 en/about.md 生成 de/about.md：以英文版为底本，文字译成德语母语书面体。"""
import io, os, sys

BASE = os.path.dirname(os.path.abspath(__file__))
src = io.open(os.path.join(BASE, '..', '..', 'content', 'en', 'about.md'), encoding='utf-8').read()

R = [
    ('          About\n', '          Über mich\n'),
    ('              Core Identity\n', '              Kernidentität\n'),
    ('<p style="margin-bottom: 1.5rem; font-weight: 600; color: #ffffff;">Electronic Music Producer | Trance Artist | Digital Mastering Engineer for Dance Music | Founding Member of Cooperation Trance | Programme Curator at Polar Impact</p>',
     '<p style="margin-bottom: 1.5rem; font-weight: 600; color: #ffffff;">Elektronischer Musikproduzent | Trance-Künstler | Digitaler Mastering-Engineer für Dance Music | Gründungsmitglied von Cooperation Trance | Programmplanung bei Polar Impact</p>'),
    ('<p style="margin-bottom: 0;">Formerly a core member of the A&amp;R team at Hertz Records (China); earlier, released music on Chinese electronic labels including 2088 Records and Hertz Records under the alias \u201cunfairmesseater\u201d.</p>',
     '<p style="margin-bottom: 0;">Zuvor zentrales Mitglied des A&amp;R-Teams bei Hertz Records (China); früher Veröffentlichungen auf chinesischen Elektrolabels wie 2088 Records und Hertz Records unter dem Alias „unfairmesseater“.</p>'),
    ('            Career\n', '            Werdegang\n'),
    ('2019: First Steps in the Scene', '2019: Erste Schritte in der Szene'),
    ('Starting in 2019, contributed tracks to two annual compilations on 2088 Records, the label run by N2V. After this early groundwork, stepped away from the electronic music scene for several years.',
     'Ab 2019 Beiträge zu zwei Jahrescompilations auf 2088 Records, dem Label von N2V. Nach diesen ersten Erfahrungen folgte eine mehrjährige Pause von der elektronischen Musikszene.'),
    ('2022: Founding a Label, Deepening the Craft', '2022: Labelgründung und Vertiefung des Handwerks'),
    ('Initiated by Chinese Trance DJ CO1N and co-founded with a group of fellow producers, Cooperation Trance became China\u2019s first independent commercial dance label. As a founding member and its first A&amp;R, he led the label\u2019s track review and in-house mastering throughout his tenure:',
     'Auf Initiative des chinesischen Trance-DJs CO1N und gemeinsam mit weiteren Produzenten gegründet, wurde Cooperation Trance Chinas erstes unabhängiges kommerzielles Dance-Label. Als Gründungsmitglied und erster A&amp;R leitete er während seiner gesamten Zeit die Track-Prüfung und das interne Mastering des Labels:'),
    ('Personally reviewed several hundred electronic music submissions',
     'Persönliche Prüfung von mehreren hundert eingereichten elektronischen Musikwerken'),
    ('Mastered 100+ tracks across dozens of EPs and albums, with releases charting on Beatport\u2019s genre charts',
     'Mastering von über 100 Tracks auf Dutzenden EPs und Alben, mit Veröffentlichungen in den Genre-Charts von Beatport'),
    ('From 2025, as the label settled into steady operation, he gradually stepped back from day-to-day label affairs to focus on independent work.',
     'Seit 2025 zog er sich, nachdem das Label einen stabilen Betrieb erreicht hatte, schrittweise aus dem täglichen Labelgeschäft zurück, um sich unabhängigen Projekten zu widmen.'),
    ('2025: International Collaboration & Recognition', '2025: Internationale Zusammenarbeit und Anerkennung'),
    ('Now working as an independent artist, he built a series of releases with Reason II Rise (RIIR Music), the team led by UK Trance artist Darren Porter. The releases were well received, and his work has since drawn attention and engagement from a number of international Trance artists:',
     'Seitdem arbeitet er als unabhängiger Künstler und realisierte eine Reihe von Veröffentlichungen mit Reason II Rise (RIIR Music), dem Team des britischen Trance-Künstlers Darren Porter. Die Veröffentlichungen stießen auf positive Resonanz und seine Arbeit erfuhr seither Aufmerksamkeit und Wertschätzung internationaler Trance-Künstler:'),
    ('Darren Porter \u2014 Trance artist from the UK', 'Darren Porter \u2014 Trance-Künstler aus dem Vereinigten Königreich'),
    ('Pinkque \u2014 electronic music artist from Australia', 'Pinkque \u2014 Elektronikkünstler aus Australien'),
    ('Geographer \u2014 Ukrainian producer on Armada Music', 'Geographer \u2014 ukrainischer Produzent bei Armada Music'),
    ('N-sking \u2014 Trance artist from Japan', 'N-sking \u2014 Trance-Künstler aus Japan'),
    ('In the same period, a dedicated English-language feature was published in the RIIR Music News column \u2014 making Eonun the first, and to date only, Chinese Trance artist to receive a feature on the platform.',
     'In der gleichen Zeit erschien ein eigenes englischsprachiges Feature in der Kolumne RIIR Music News \u2014 Eonun ist damit der erste und bislang einzige chinesische Trance-Künstler, dem ein Feature auf dieser Plattform gewidmet wurde.'),
    ('Early 2026: A New Chapter', 'Anfang 2026: Ein neues Kapitel'),
    ('Joined Polar Impact as A&amp;R and programme curator, continuing to support the growth of Trance in China.',
     'Beitritt zu Polar Impact als A&amp;R und Programmplaner, mit dem Ziel, das Wachstum von Trance in China weiter zu unterstützen.'),
    ('              Press Coverage\n', '              Presse\n'),
    ('Eonun Artist Feature | RIIR Music Feature Story', 'Eonun Artist Feature | RIIR Music Feature (englischsprachig)'),
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

out = os.path.join(BASE, '..', '..', 'content', 'de', 'about.md')
io.open(out, 'w', encoding='utf-8', newline='\n').write(src)
print('written: ' + out)

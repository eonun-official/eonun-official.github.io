# -*- coding: utf-8 -*-
"""从 en/_index.md 生成 de/_index.md：以验收过的英文版为底本，价格平价（$→€），文字译成德语母语书面体。"""
import io, os, sys

BASE = os.path.dirname(os.path.abspath(__file__))
src = io.open(os.path.join(BASE, '..', '..', 'content', 'en', '_index.md'), encoding='utf-8').read()

R = [
    ('title: "Eonun | Trance Sound Sculptor | Eonun"', 'title: "Eonun | Trance Sound Sculptor | Eonun"'),
    ('description: "Welcome to the world of Eonun: Trance production, style design, mastering, aesthetics and concept"',
     'description: "Willkommen in der Welt von Eonun: Trance-Produktion, Stildesign, Mastering, Ästhetik und Konzept"'),
    ('alt="Eonun | Trance Sound Sculptor"', 'alt="Eonun | Trance Sound Sculptor"'),
    ('          Welcome to the world of Eonun: Trance production, style design, mastering, aesthetics and concept',
     '          Willkommen in der Welt von Eonun: Trance-Produktion, Stildesign, Mastering, Ästhetik und Konzept'),
    ('<h2 id="defining-trances-textural-boundaries-through-sound">Defining the textural boundaries of Trance, through sound</h2>',
     '<h2 id="mit-klang-die-texturale-grenze-des-trance-definieren">Mit Klang die texturale Grenze des Trance definieren</h2>'),
    ('  Specializing in modern Uplifting / Tech Trance production and mastering \u2014 from bedroom mixes to releases on international platforms. With <span style="font-weight: bold;">a forward-thinking musical aesthetic</span> and <span style="font-weight: bold;">a complete, self-developed theoretical system</span>, every track is finished to a standard that travels.',
     '  Spezialisiert auf moderne Uplifting- / Tech-Trance-Produktion und Mastering \u2014 vom Bedroom-Mix bis zur Veröffentlichung auf internationalen Plattformen. Mit <span style="font-weight: bold;">einem vorausschauenden musikalischen Ästhetikverständnis</span> und <span style="font-weight: bold;">einem vollständigen, eigenentwickelten theoretischen System</span> wird jeder Track so fertiggestellt, dass er international besteht.'),
    ('<h2 id="core-identity">Core Identity</h2>', '<h2 id="kernidentitaet">Kernidentität</h2>'),
    ('<h3>Trance Producer</h3>', '<h3>Trance-Produzent</h3>'),
    ('<p>Focused on Uplifting / Tech Trance</p>', '<p>Schwerpunkt Uplifting / Tech Trance</p>'),
    ('<h3>Mastering Engineer</h3>', '<h3>Mastering-Engineer</h3>'),
    ('<p>Professional mastering for 100+ Trance releases that reached the charts</p>',
     '<p>Professionelles Mastering für über 100 Trance-Veröffentlichungen in den Charts</p>'),
    ('<h3>Co-Founder</h3>', '<h3>Mitgründer</h3>'),
    ('<p>&amp; the first A&amp;R of Cooperation Trance</p>', '<p>&amp; erster A&amp;R von Cooperation Trance</p>'),
    ('<h3>Label A&amp;R</h3>', '<h3>Label-A&amp;R</h3>'),
    ('<p>Programme curator at Polar Impact</p>', '<p>Programmplanung bei Polar Impact</p>'),
    ('<h2 id="recognition--endorsements">Recognition · Endorsements</h2>',
     '<h2 id="anerkennung--referenzen">Anerkennung · Referenzen</h2>'),
    ('<h3 class="cred-title">Exclusive Feature</h3>', '<h3 class="cred-title">Exklusives Feature</h3>'),
    ('<h3 class="cred-title">Guest Takeover \u2014 AFTERHOURS Radio</h3>',
     '<h3 class="cred-title">Guest-Takeover \u2014 AFTERHOURS Radio</h3>'),
    ('alt="Exclusive feature 1"', 'alt="Exklusives Feature 1"'),
    ('alt="Exclusive feature 2"', 'alt="Exklusives Feature 2"'),
    ('alt="Exclusive feature 3"', 'alt="Exklusives Feature 3"'),
    ('alt="Exclusive feature 4"', 'alt="Exklusives Feature 4"'),
    ('<h3 class="collab-title">Standing alongside leading names in Trance</h3>',
     '<h3 class="collab-title">An der Seite führender Namen des Trance</h3>'),
    ('<p class="collab-desc">Long-term collaboration with overseas Trance labels and media: releases and an artist interview featured in RIIR Music coverage, plus a guest appearance on the AFTERHOURS international radio show.</p>',
     '<p class="collab-desc">Langjährige Zusammenarbeit mit Trance-Labels und Medien im Ausland: Veröffentlichungen und ein Künstlerinterview erschienen als Feature bei RIIR Music, dazu ein Gastauftritt in der internationalen AFTERHOURS-Radioshow.</p>'),
    ('<h2 id="core-services">Core Services</h2>', '<h2 id="kernleistungen">Kernleistungen</h2>'),
    ('<h3 class="block-subtitle">From demo to release, every step covered</h3>',
     '<h3 class="block-subtitle">Vom Demo bis zur Veröffentlichung \u2014 jede Phase abgedeckt</h3>'),
    ('<h4>Trance Music Production</h4>', '<h4>Trance-Musikproduktion</h4>'),
    ('<p>Precision, epic scale and atmosphere. Resolving frequency clashes, dynamic imbalance and flat soundstages \u2014 mixes built to put the core tension of Trance front and center.</p>',
     '<p>Präzision, epische Breite und Atmosphäre. Lösung von Frequenzkollisionen, dynamischem Ungleichgewicht und flachen Klangbildern \u2014 Mixe, die die zentrale Spannung des Trance in den Vordergrund stellen.</p>'),
    ('<h4>Professional Mastering</h4>', '<h4>Professionelles Mastering</h4>'),
    ('<p>Loudness, spectral balance and bus cohesion \u2014 delivered to the playback specs of Spotify, Beatport and other major platforms.</p>',
     '<p>Loudness, spektrale Balance und Bus-Kohäsion \u2014 abgestimmt auf die Wiedergabestandards von Spotify, Beatport und anderen großen Plattformen.</p>'),
    ('<h4>Coaching &amp; Release Guidance</h4>', '<h4>Coaching &amp; Release-Beratung</h4>'),
    ('<p>Small-group (up to four) or one-on-one coaching that helps strong Trance tracks reach a global audience. A strict no-clique policy: single-point service and full confidentiality throughout.</p>',
     '<p>Coaching in kleinen Gruppen (bis zu vier Personen) oder im Einzeltraining, das starken Trance-Tracks ein globales Publikum erschließt. Strikte Anti-Cliquen-Regel: persönliche Einzelbetreuung und vollständige Vertraulichkeit.</p>'),
    ('<h2 id="recent-works--sonic-stage">Recent Works · Sonic Stage</h2>',
     '<h2 id="aktuelle-arbeiten--sonic-stage">Aktuelle Arbeiten · Sonic Stage</h2>'),
    ('<p class="work-note">More on <a href="https://open.spotify.com/artist/7ok2w55yMiwbUvrlVn9mBW"',
     '<p class="work-note">Mehr auf <a href="https://open.spotify.com/artist/7ok2w55yMiwbUvrlVn9mBW"'),
    ('<p class="work-note">More on <a href="https://music.163.com/playlist?id=17739007625"',
     '<p class="work-note">Mehr auf <a href="https://music.163.com/playlist?id=17739007625"'),
    ('<h2 id="contact--lets-create-trance-energy">Contact · Let&rsquo;s Create Trance Energy</h2>',
     '<h2 id="kontakt--gemeinsam-trance-energie-erschaffen">Kontakt · Gemeinsam Trance-Energie erschaffen</h2>'),
    ('<h3>Mixing Needs · Collaboration Inquiries · DJ Booking</h3>',
     '<h3>Mixing-Anfragen · Kooperationen · DJ-Booking</h3>'),
    ('<p>Trance fans, producers and event organizers are all welcome \u2014 let&rsquo;s build something powerful together</p>',
     '<p>Trance-Fans, Produzenten und Veranstalter sind herzlich willkommen \u2014 lassen Sie uns gemeinsam etwas Kraftvolles erschaffen</p>'),
    ('>Get in Touch</a>', '>Jetzt anfragen</a>'),
    # JS 字符串
    ("'Video failed to load, showing fallback background'", "'Video konnte nicht geladen werden, Fallback-Hintergrund wird angezeigt'"),
    ("'Video loaded'", "'Video geladen'"),
    ("'Video load timed out, showing fallback background'", "'Video-Ladevorgang abgelaufen, Fallback-Hintergrund wird angezeigt'"),
    ("'Slogan file failed to load: '", "'Slogan-Datei konnte nicht geladen werden: '"),
    ("'Slogan file failed to load, using default slogan:'", "'Slogan-Datei konnte nicht geladen werden, Standard-Slogan wird verwendet:'"),
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

out = os.path.join(BASE, '..', '..', 'content', 'de', '_index.md')
io.open(out, 'w', encoding='utf-8', newline='\n').write(src)
print('written: ' + out)

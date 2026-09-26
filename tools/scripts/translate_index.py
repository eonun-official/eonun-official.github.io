# -*- coding: utf-8 -*-
"""从 zh-cn/_index.md 生成 en/de 主页：结构不动，只替换可见文字。"""
import io, re, os

BASE = os.path.dirname(os.path.abspath(__file__))
src = io.open(os.path.join(BASE, '..', '..', 'content', 'zh-cn', '_index.md'), encoding='utf-8').read()

EN = [
('alt="Eonun | Trance 声波雕刻师"', 'alt="Eonun | Trance Sound Sculptor"'),
('>一个年轻人奉献给了Trance艺术的部分人生</p>', '>A young life, devoted to the art of Trance</p>'),
('欢迎来到 Eonun 领域：Trance 制作、风格设计、母带工程、美学与概念', 'Welcome to the world of Eonun: Trance production, style design, mastering, aesthetics and concept'),
('用声波，定义 Trance 的质感边界', 'Defining the Texture of Trance with Sound'),
('专注于现代 Uplifting / Tech Trance 制作与母带工程，从卧室混音到国际平台发行，用<span style="font-weight: bold;">前沿的音乐审美理念</span>与<span style="font-weight: bold;">独家完备的理论体系</span>，让每首作品都具备国际级质感。',
 'Specialized in modern Uplifting / Tech Trance production and mastering — from bedroom mixes to releases on international platforms. With <span style="font-weight: bold;">forward-thinking musical aesthetics</span> and an <span style="font-weight: bold;">exclusive, comprehensive theory system</span>, every track is crafted to international quality.'),
('>核心身份</h2>', '>Core Identity</h2>'),
('>Trance 制作人</h3>', '>Trance Producer</h3>'),
('Uplifting / Tech Trance 为主', 'Focused on Uplifting / Tech Trance'),
('>母带工程师</h3>', '>Mastering Engineer</h3>'),
('上百首榜单Trance作品专业母带处理', 'Professional mastering for hundreds of chart-topping Trance tracks'),
('Cooperation Trance 联合创始人', 'Co-founder of Cooperation Trance'),
('Polar Impact 团队策划', 'Team planning at Polar Impact'),
('国内外认可 · 合作背书', 'Recognition · Partnerships'),
('>独家报道</h3>', '>Exclusive Feature</h3>'),
('alt="独家报道1"', 'alt="Exclusive feature 1"'),
('alt="独家报道2"', 'alt="Exclusive feature 2"'),
('alt="独家报道3"', 'alt="Exclusive feature 3"'),
('alt="独家报道4"', 'alt="Exclusive feature 4"'),
('AFTERHOURS 国际电台特邀', 'AFTERHOURS International Radio Takeover'),
('与世界级 Trance 力量并肩', 'Alongside World-Class Trance Forces'),
('作品以及艺人采访入选厂牌专题报道，第一个用实力征服国际厂牌开启独家专访的中国Trance制作人。<br><br>与此同时也是首个被厂牌邀请在该国际电台上参与活动的国人',
 'Tracks and artist interviews have been featured in label spotlights — the first Chinese Trance producer to win over an international label through sheer craft and earn an exclusive feature.<br><br>Also the first Chinese artist invited by the label to take part on that international radio station'),
('<h2 id="核心服务">核心服务</h2>', '<h2 id="核心服务">Core Services</h2>'),
('从 Demo 到发行，全链路支持', 'Full-Cycle Support, from Demo to Release'),
('>Trance 音乐工程</h4>', '>Trance Music Production</h4>'),
('机能、史诗与氛围感，解决频域冲突、动态失衡、声场扁平，打造具备行业一流的混音，突出 Trance 核心张力。',
 'Driving, epic and atmospheric — resolving frequency conflicts, dynamic imbalance and flat soundstages to craft an industry-leading mix that brings out the core tension of Trance.'),
('>专业母带处理</h4>', '>Professional Mastering</h4>'),
('提升响度、优化频谱平衡、增强总线粘合度，适配各大流媒体平台（Spotify/Beatport）。',
 'Louder, spectrally balanced and bus-glued masters, tuned for major streaming platforms (Spotify/Beatport).'),
('>教学与发行指导</h4>', '>Coaching & Release Guidance</h4>'),
('通过一对四或一对一指导助力优质 Trance 作品走向全球市场。坚持无圈子化原则，确保艺人隐私全程提供单线服务与信息保密。',
 'Through small-group (up to 4) or one-on-one coaching, quality Trance works reach the global market. Strictly non-clique, with full artist privacy: single-point service and confidentiality throughout.'),
('近期作品 · 声波现场', 'Recent Works · Sonic Live'),
('更多作品 → ', 'More works on '),
('联系我 · 共创 Trance 能量', 'Contact · Creating Trance Energy Together'),
('欢迎 Trance 同好、制作人、活动方洽谈合作，让我们一起打造有力量的声波',
 'Trance fans, producers and event organizers are welcome — let\'s create powerful sound waves together'),
('>\n    立即咨询\n  </a>', '>\n    Get in Touch\n  </a>'),
("if (indexSlogan) indexSlogan.textContent = '一个年轻人奉献给了Trance艺术的部分人生';", "if (indexSlogan) indexSlogan.textContent = 'A young life, devoted to the art of Trance';"),
]
DE = [
('alt="Eonun | Trance 声波雕刻师"', 'alt="Eonun | Trance-Klangbildhauer"'),
('>一个年轻人奉献给了Trance艺术的部分人生</p>', '>Ein Teil eines jungen Lebens, der der Kunst des Trance gewidmet ist</p>'),
('欢迎来到 Eonun 领域：Trance 制作、风格设计、母带工程、美学与概念', 'Willkommen in der Welt von Eonun: Trance-Produktion, Stildesign, Mastering, Ästhetik und Konzept'),
('用声波，定义 Trance 的质感边界', 'Mit Klangwellen die Textur von Trance definieren'),
('专注于现代 Uplifting / Tech Trance 制作与母带工程，从卧室混音到国际平台发行，用<span style="font-weight: bold;">前沿的音乐审美理念</span>与<span style="font-weight: bold;">独家完备的理论体系</span>，让每首作品都具备国际级质感。',
 'Spezialisiert auf moderne Uplifting-/Tech-Trance-Produktion und Mastering — vom Bedroom-Mix bis zur Veröffentlichung auf internationalen Plattformen. Mit <span style="font-weight: bold;">modernster musikalischer Ästhetik</span> und einem <span style="font-weight: bold;">exklusiven, durchdachten Theoriesystem</span> erhält jedes Werk internationalen Feinschliff.'),
('>核心身份</h2>', '>Kernidentität</h2>'),
('>Trance 制作人</h3>', '>Trance-Produzent</h3>'),
('Uplifting / Tech Trance 为主', 'Fokus auf Uplifting / Tech Trance'),
('>母带工程师</h3>', '>Mastering-Engineer</h3>'),
('上百首榜单Trance作品专业母带处理', 'Professionelles Mastering für hunderte Chart-Trance-Werke'),
('Cooperation Trance 联合创始人', 'Mitgründer von Cooperation Trance'),
('Polar Impact 团队策划', 'Team-Planung bei Polar Impact'),
('国内外认可 · 合作背书', 'Anerkennung · Partnerschaften'),
('>独家报道</h3>', '>Exklusiv-Feature</h3>'),
('alt="独家报道1"', 'alt="Exklusiv-Feature 1"'),
('alt="独家报道2"', 'alt="Exklusiv-Feature 2"'),
('alt="独家报道3"', 'alt="Exklusiv-Feature 3"'),
('alt="独家报道4"', 'alt="Exklusiv-Feature 4"'),
('AFTERHOURS 国际电台特邀', 'Gast-Takeover bei AFTERHOURS International Radio'),
('与世界级 Trance 力量并肩', 'An der Seite weltklassiger Trance-Größen'),
('作品以及艺人采访入选厂牌专题报道，第一个用实力征服国际厂牌开启独家专访的中国Trance制作人。<br><br>与此同时也是首个被厂牌邀请在该国际电台上参与活动的国人',
 'Produktionen und Interviews wurden in Label-Sonderberichten gefeiert — der erste chinesische Trance-Produzent, der ein internationales Label mit purem Können überzeugte und ein exklusives Feature erhielt.<br><br>Zugleich der erste Chinese, den das Label zu einer Session auf diesem internationalen Radio einlud'),
('<h2 id="核心服务">核心服务</h2>', '<h2 id="核心服务">Kernservices</h2>'),
('从 Demo 到发行，全链路支持', 'Voller Support vom Demo bis zur Veröffentlichung'),
('>Trance 音乐工程</h4>', '>Trance-Musikproduktion</h4>'),
('机能、史诗与氛围感，解决频域冲突、动态失衡、声场扁平，打造具备行业一流的混音，突出 Trance 核心张力。',
 'Treibend, episch und atmosphärisch — Frequenzkonflikte, dynamische Ungleichgewichte und flache Klangbilder werden gelöst, für einen branchenführenden Mix, der die Kernspannung von Trance herausstellt.'),
('>专业母带处理</h4>', '>Professionelles Mastering</h4>'),
('提升响度、优化频谱平衡、增强总线粘合度，适配各大流媒体平台（Spotify/Beatport）。',
 'Mehr Lautstärke, spektrale Balance und stärkere Bus-Kohärenz — abgestimmt auf große Streaming-Plattformen (Spotify/Beatport).'),
('>教学与发行指导</h4>', '>Coaching & Release-Beratung</h4>'),
('通过一对四或一对一指导助力优质 Trance 作品走向全球市场。坚持无圈子化原则，确保艺人隐私全程提供单线服务与信息保密。',
 'Durch Coaching in Kleingruppen (bis zu 4 Personen) oder im Einzelcoaching erreichen hochwertige Trance-Werke den globalen Markt. Konsequent frei von Zirkeln, mit vollständiger Diskretion: durchgehende Einzelbetreuung und Informationsschutz.'),
('近期作品 · 声波现场', 'Neue Werke · Sonic Live'),
('更多作品 → ', 'Mehr Werke auf '),
('联系我 · 共创 Trance 能量', 'Kontakt · Gemeinsam Trance-Energie erschaffen'),
('欢迎 Trance 同好、制作人、活动方洽谈合作，让我们一起打造有力量的声波',
 'Trance-Fans, Produzenten und Veranstalter sind herzlich willkommen — erschaffen wir gemeinsam kraftvolle Klangwellen'),
('>\n    立即咨询\n  </a>', '>\n    Jetzt anfragen\n  </a>'),
("if (indexSlogan) indexSlogan.textContent = '一个年轻人奉献给了Trance艺术的部分人生';", "if (indexSlogan) indexSlogan.textContent = 'Ein Teil eines jungen Lebens, der der Kunst des Trance gewidmet ist';"),
]

fetch_block = re.compile(r"fetch\('/data/trance_mixing_slogans\.txt'\)[\s\S]*?\n  \}\);\n(?=  document\.addEventListener)")

for lang, pairs in (('en', EN), ('de', DE)):
    s = src
    misses = []
    for old, new in pairs:
        if old in s:
            s = s.replace(old, new, 1)
        else:
            misses.append(old[:40])
    s, nsub = fetch_block.subn("  /* EN/DE 版标语库待翻译，暂用静态默认句 */\n", s)
    if nsub != 1:
        misses.append('fetch-block:%d' % nsub)
    path = os.path.join(BASE, '..', '..', 'content', lang, '_index.md')
    io.open(path, 'w', encoding='utf-8', newline='').write(s)
    print(lang, 'written, misses:', misses if misses else 'none')

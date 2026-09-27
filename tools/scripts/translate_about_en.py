# -*- coding: utf-8 -*-
"""从 zh-hans/about.md 生成 en/about.md：结构/样式/脚本不动，只替换可见文字。"""
import io, os, sys

BASE = os.path.dirname(os.path.abspath(__file__))
src = io.open(os.path.join(BASE, '..', '..', 'content', 'zh-hans', 'about.md'), encoding='utf-8').read()

R = [
    ('          关于我\n', '          About\n'),
    ('              核心身份\n', '              Core Identity\n'),
    ('<p style="margin-bottom: 1.5rem; font-weight: 600; color: #ffffff;">泛电子音乐制作人 | Trance 艺术家 | 舞曲数字母带工程师 | Cooperation Trance 厂牌创始成员 | Polar Impact 策划</p>',
     '<p style="margin-bottom: 1.5rem; font-weight: 600; color: #ffffff;">Electronic Music Producer | Trance Artist | Digital Mastering Engineer for Dance Music | Founding Member of Cooperation Trance | Programme Curator at Polar Impact</p>'),
    ('<p style="margin-bottom: 0;">曾任 Hertz Records（中国）A&amp;R 核心成员；更早曾以艺名“unfairmesseater”在 2088 Records、Hertz Records 等中国电子音乐厂牌发表作品。</p>',
     '<p style="margin-bottom: 0;">Formerly a core member of the A&amp;R team at Hertz Records (China); earlier, released music on Chinese electronic labels including 2088 Records and Hertz Records under the alias \u201cunfairmesseater\u201d.</p>'),
    ('            职业履历\n', '            Career\n'),
    ('2019年：行业初露锋芒', '2019: First Steps in the Scene'),
    ('2019 年起，参与 N2V 旗下 2088 Records 厂牌两届年度合集的曲目创作与发行；完成早期积累后，暂别电子音乐行业数年。',
     'Starting in 2019, contributed tracks to two annual compilations on 2088 Records, the label run by N2V. After this early groundwork, stepped away from the electronic music scene for several years.'),
    ('2022年：厂牌创立与行业深耕', '2022: Founding a Label, Deepening the Craft'),
    ('由中国 Trance DJ CO1N 牵头，联合其他制作人共同创立中国首个独立商业舞曲厂牌 Cooperation Trance；作为创始成员兼首任 A&amp;R，曾在任期间长期主导厂牌作品审核与母带制作核心工作：',
     'Initiated by Chinese Trance DJ CO1N and co-founded with a group of fellow producers, Cooperation Trance became China\u2019s first independent commercial dance label. As a founding member and its first A&amp;R, he led the label\u2019s track review and in-house mastering throughout his tenure:'),
    ('累计完成数百首优质电子音乐作品的专业评审',
     'Personally reviewed several hundred electronic music submissions'),
    ('助力超过百轨曲目与几十张EP与专辑的母带处理，其上架均荣登Beatport的各类发行榜单',
     'Mastered 100+ tracks across dozens of EPs and albums, with releases charting on Beatport\u2019s genre charts'),
    ('2025 年起，随着厂牌步入稳定运营，本人逐渐淡出 Cooperation Trance 的日常厂务，转向独立发展。',
     'From 2025, as the label settled into steady operation, he gradually stepped back from day-to-day label affairs to focus on independent work.'),
    ('2025年：国际合作与专业认可', '2025: International Collaboration & Recognition'),
    ('开始以独立身份发展，与英国知名 Trance 艺人 Darren Porter 主导的 Reason II Rise（RIIR Music）团队达成系列发行合作，作品获得积极反响，并陆续受到多位国际 Trance 艺人的关注与互动：',
     'Now working as an independent artist, he built a series of releases with Reason II Rise (RIIR Music), the team led by UK Trance artist Darren Porter. The releases were well received, and his work has since drawn attention and engagement from a number of international Trance artists:'),
    ('英国知名Trance音乐人 Darren Porter', 'Darren Porter — Trance artist from the UK'),
    ('澳洲电子音乐艺术家 Pinkque', 'Pinkque — electronic music artist from Australia'),
    ('Armada Music厂牌旗下乌克兰制作人 Geographer', 'Geographer — Ukrainian producer on Armada Music'),
    ('日本Trance领域代表艺人 N-sking', 'N-sking — Trance artist from Japan'),
    ('同期，个人专属英文专题报道正式刊发于 RIIR Music News 专栏，成为第一位、也是截至目前唯一一位获得该平台专题报道的中国 Trance 艺术家。',
     'In the same period, a dedicated English-language feature was published in the RIIR Music News column \u2014 making Eonun the first, and to date only, Chinese Trance artist to receive a feature on the platform.'),
    ('2026年初：新使命与新征程', 'Early 2026: A New Chapter'),
    ('应邀担任Polar Impact厂牌的A&R与策划，为中国的Trance发展继续做出贡献。',
     'Joined Polar Impact as A&amp;R and programme curator, continuing to support the growth of Trance in China.'),
    ('              相关报道\n', '              Press Coverage\n'),
    ('Eonun Artist Feature | RIIR Music 海外专题报道', 'Eonun Artist Feature | RIIR Music Feature Story'),
    # JS 字符串
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

out = os.path.join(BASE, '..', '..', 'content', 'en', 'about.md')
io.open(out, 'w', encoding='utf-8', newline='\n').write(src)
print('written: ' + out)

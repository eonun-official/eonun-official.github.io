# -*- coding: utf-8 -*-
"""从 zh-hans/_index.md 生成 en/_index.md：结构/样式/脚本不动，只替换可见文字。"""
import io, os, sys

BASE = os.path.dirname(os.path.abspath(__file__))
src = io.open(os.path.join(BASE, '..', '..', 'content', 'zh-hans', '_index.md'), encoding='utf-8').read()

R = [
    # front matter
    ('title: "Eonun | Trance 声波雕刻师 | Eonun"',
     'title: "Eonun | Trance Sound Sculptor | Eonun"'),
    ('description: "欢迎来到 Eonun 领域：Trance 制作、风格设计、母带工程、美学与概念"',
     'description: "Welcome to the world of Eonun: Trance production, style design, mastering, aesthetics and concept"'),
    # logo alt
    ('alt="Eonun | Trance 声波雕刻师"', 'alt="Eonun | Trance Sound Sculptor"'),
    # hero h2
    ('          欢迎来到 Eonun 领域：Trance 制作、风格设计、母带工程、美学与概念',
     '          Welcome to the world of Eonun: Trance production, style design, mastering, aesthetics and concept'),
    # section h2 + slug
    ('<h2 id="用声波定义-trance-的质感边界">用声波，定义 Trance 质感边界</h2>',
     '<h2 id="defining-trances-textural-boundaries-through-sound">Defining the textural boundaries of Trance, through sound</h2>'),
    # intro paragraph
    ('  专注于现代 Uplifting / Tech Trance 制作与母带工程，从卧室混音到国际平台发行，用<span style="font-weight: bold;">前沿的音乐审美理念</span>与<span style="font-weight: bold;">独家完备的理论体系</span>，让每首作品都具备国际级质感。',
     '  Specializing in modern Uplifting / Tech Trance production and mastering — from bedroom mixes to releases on international platforms. With <span style="font-weight: bold;">a forward-thinking musical aesthetic</span> and <span style="font-weight: bold;">a complete, self-developed theoretical system</span>, every track is finished to a standard that travels.'),
    # identity strip
    ('<h2 id="核心身份">核心身份</h2>', '<h2 id="core-identity">Core Identity</h2>'),
    ('<h3>Trance 制作人</h3>', '<h3>Trance Producer</h3>'),
    ('<p>Uplifting / Tech Trance 为主</p>', '<p>Focused on Uplifting / Tech Trance</p>'),
    ('<h3>母带工程师</h3>', '<h3>Mastering Engineer</h3>'),
    ('<p>上百首榜单Trance作品专业母带处理</p>',
     '<p>Professional mastering for 100+ Trance releases that reached the charts</p>'),
    ('<h3>联合创始人</h3>', '<h3>Co-Founder</h3>'),
    ('<p>兼首任 Cooperation Trance A&amp;R</p>', '<p>&amp; the first A&amp;R of Cooperation Trance</p>'),
    ('<h3>厂牌 A&amp;R</h3>', '<h3>Label A&amp;R</h3>'),
    ('<p>Polar Impact 团队策划</p>', '<p>Programme curator at Polar Impact</p>'),
    # recognition
    ('<h2 id="国内外认可--合作背书">国内外认可 · 合作背书</h2>',
     '<h2 id="recognition--endorsements">Recognition · Endorsements</h2>'),
    ('<h3 class="cred-title">独家报道</h3>', '<h3 class="cred-title">Exclusive Feature</h3>'),
    ('<h3 class="cred-title">AFTERHOURS 国际电台特邀</h3>',
     '<h3 class="cred-title">Guest Takeover — AFTERHOURS Radio</h3>'),
    ('alt="独家报道1"', 'alt="Exclusive feature 1"'),
    ('alt="独家报道2"', 'alt="Exclusive feature 2"'),
    ('alt="独家报道3"', 'alt="Exclusive feature 3"'),
    ('alt="独家报道4"', 'alt="Exclusive feature 4"'),
    # collab block
    ('<h3 class="collab-title">与世界级 Trance 力量并肩</h3>',
     '<h3 class="collab-title">Standing alongside leading names in Trance</h3>'),
    ('<p class="collab-desc">长期与海外 Trance 厂牌及媒体保持合作：作品与艺人专访入选 RIIR Music 专题报道，并受邀参与 AFTERHOURS 国际电台活动。</p>',
     '<p class="collab-desc">Long-term collaboration with overseas Trance labels and media: releases and an artist interview featured in RIIR Music coverage, plus a guest appearance on the AFTERHOURS international radio show.</p>'),
    # core services
    ('<h2 id="核心服务">核心服务</h2>', '<h2 id="core-services">Core Services</h2>'),
    ('<h3 class="block-subtitle">从 Demo 到发行，全链路支持</h3>',
     '<h3 class="block-subtitle">From demo to release, every step covered</h3>'),
    ('<h4>Trance 音乐工程</h4>',
     '<h4>Trance Music Production</h4>'),
    ('<p>机能、史诗与氛围感，解决频域冲突、动态失衡、声场扁平，打造具备行业一流的混音，突出 Trance 核心张力。</p>',
     '<p>Precision, epic scale and atmosphere. Resolving frequency clashes, dynamic imbalance and flat soundstages — mixes built to put the core tension of Trance front and center.</p>'),
    ('<h4>专业母带处理</h4>', '<h4>Professional Mastering</h4>'),
    ('<p>提升响度、优化频谱平衡、增强总线粘合度，适配各大流媒体平台（Spotify/Beatport）。</p>',
     '<p>Loudness, spectral balance and bus cohesion — delivered to the playback specs of Spotify, Beatport and other major platforms.</p>'),
    ('<h4>教学与发行指导</h4>', '<h4>Coaching &amp; Release Guidance</h4>'),
    ('<p>通过一对四或一对一指导助力优质 Trance 作品走向全球市场。坚持无圈子化原则，确保艺人隐私全程提供单线服务与信息保密。</p>',
     '<p>Small-group (up to four) or one-on-one coaching that helps strong Trance tracks reach a global audience. A strict no-clique policy: single-point service and full confidentiality throughout.</p>'),
    # works
    ('<h2 id="近期作品--声波现场">近期作品 · 声波现场</h2>',
     '<h2 id="recent-works--sonic-stage">Recent Works · Sonic Stage</h2>'),
    ('<p class="work-note">更多作品 → <a href="https://open.spotify.com/artist/7ok2w55yMiwbUvrlVn9mBW"',
     '<p class="work-note">More on <a href="https://open.spotify.com/artist/7ok2w55yMiwbUvrlVn9mBW"'),
    ('<p class="work-note">更多作品 → <a href="https://music.163.com/playlist?id=17739007625"',
     '<p class="work-note">More on <a href="https://music.163.com/playlist?id=17739007625"'),
    # contact
    ('<h2 id="联系我--共创-trance-能量">联系我 · 共创 Trance 能量</h2>',
     '<h2 id="contact--lets-create-trance-energy">Contact · Let&rsquo;s Create Trance Energy</h2>'),
    ('<p>欢迎 Trance 同好、制作人、活动方洽谈合作，让我们一起打造有力量的声波</p>',
     '<p>Trance fans, producers and event organizers are all welcome — let&rsquo;s build something powerful together</p>'),
    ('>立即咨询</a>', '>Get in Touch</a>'),
    # JS console strings
    ("'视频加载失败，显示备用背景'", "'Video failed to load, showing fallback background'"),
    ("'视频加载成功'", "'Video loaded'"),
    ("'视频加载超时，显示备用背景'", "'Video load timed out, showing fallback background'"),
    ("'标语文件加载失败: '", "'Slogan file failed to load: '"),
    ("'标语文件加载失败，使用默认标语:'", "'Slogan file failed to load, using default slogan:'"),
]

for old, new in R:
    if old not in src:
        print('MISS: ' + old[:60]); sys.exit(1)
    src = src.replace(old, new)

# 默认标语两处（HTML 内联 + JS 兜底）统一替换
old_slogan = '一个年轻人奉献给了Trance艺术的部分人生'
if src.count(old_slogan) != 2:
    print('slogan count != 2: %d' % src.count(old_slogan)); sys.exit(1)
src = src.replace(old_slogan, 'Part of a young life, devoted to the art of Trance')

out = os.path.join(BASE, '..', '..', 'content', 'en', '_index.md')
io.open(out, 'w', encoding='utf-8', newline='\n').write(src)
print('written: ' + out)

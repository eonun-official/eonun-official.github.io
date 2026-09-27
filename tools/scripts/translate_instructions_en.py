# -*- coding: utf-8 -*-
"""从 zh-hans/instructions.md 生成 en/instructions.md：结构/样式/脚本不动，只替换可见文字。
价格按 2026-09-27 用户批准的英文版定价策略（略高于汇率）：
三档咨询 ¥428/668/828 → $65/$95/$120；初级课 ¥1,500 → $220；中级课 ¥5,500 → $790；
返利 ¥150/300/1,000 → $25/$45/$150；封顶 ¥1,500 → $210；邀请上限 ¥10,000 → $1,400；奖学金 ¥300 → $45。"""
import io, os, sys

BASE = os.path.dirname(os.path.abspath(__file__))
src = io.open(os.path.join(BASE, '..', '..', 'content', 'zh-hans', 'instructions.md'), encoding='utf-8').read()

R = [
    # front matter / alt / hero
    ('title: "教学 | Trance 指导服务 | Eonun"', 'title: "Coaching | Trance Mentorship | Eonun"'),
    ('description: "从爱好者到国际舞台：以合理的价格实现知识最大化，进步立竿见影"',
     'description: "From enthusiast to the international stage: maximize what you learn at a fair price \u2014 and hear the progress"'),
    ('alt="教学 | Trance 指导服务"', 'alt="Coaching | Trance Mentorship"'),
    ('          从爱好者到国际舞台：以合理的价格实现知识最大化，进步立竿见影\n',
     '          From enthusiast to the international stage: maximize what you learn at a fair price \u2014 and hear the progress\n'),
    # 课程 hero
    ('<h1 class="hero-title">Trance 指导服务</h1>', '<h1 class="hero-title">Trance Mentorship</h1>'),
    ('<p>既然你已经看到这里，不妨再多了解一步。</p>', '<p>Since you\u2019ve read this far, take one more step.</p>'),
    ('<p>我提供的东西很朴素：直接与我本人对接；价格与档位完全透明，没有隐藏费用；知识成体系；指导真正落在你的作品上。</p>',
     '<p>What I offer is straightforward: you deal with me directly; pricing and tiers are fully transparent, with no hidden fees; the knowledge is systematic; and the coaching lands on your actual tracks.</p>'),
    ('<p>每一项内容都指向实际——让你做出属于自己的、站得住脚的作品。</p>',
     '<p>Everything is built around one practical goal \u2014 tracks that are yours, and that hold up.</p>'),
    ('<p>无论你是刚开始接触制作的新手，还是想更进一步的制作人或 DJ，这里都有适合你的位置。<span style="color: #d9d9d9;"></span></p>',
     '<p>Whether you\u2019re just getting started or you\u2019re a producer or DJ looking to level up, there\u2019s a place for you here.<span style="color: #d9d9d9;"></span></p>'),
    ('<p style="margin-top: 0.6rem; font-size: 0.8rem; color: #888888; letter-spacing: 0.5px;">* 支持中文 / 英语授课</p>',
     '<p style="margin-top: 0.6rem; font-size: 0.8rem; color: #888888; letter-spacing: 0.5px;">* Sessions available in English and Chinese</p>'),
    # 课程导航
    ('<h3 class="nav-title">选择服务类型</h3>', '<h3 class="nav-title">Choose a Service</h3>'),
    ('<button class="course-nav-link" onclick="showSection(\'one-on-one\')">即时一对一线上交流</button>',
     '<button class="course-nav-link" onclick="showSection(\'one-on-one\')">Instant 1-on-1 Online Session</button>'),
    ('<button class="course-nav-link" onclick="showSection(\'long-term\')">长期课程体系（分阶成长计划）</button>',
     '<button class="course-nav-link" onclick="showSection(\'long-term\')">Long-Term Program (Step-by-Step Growth Plan)</button>'),
    ('<button class="course-nav-link" onclick="showSection(\'booking\')">立即预约</button>',
     '<button class="course-nav-link" onclick="showSection(\'booking\')">Book Now</button>'),
    ('<div id="select-hint">请 先 选 择 服 务 类 型</div>',
     '<div id="select-hint">Please Choose a Service First</div>'),
    # 一对一
    ('<h2>即时一对一线上交流</h2>', '<h2>Instant 1-on-1 Online Session</h2>'),
    ('<p style="text-align: center; color: #d9d9d9; font-size: 1.1rem; margin-bottom: 40px;">话题不设限：作品打磨、技术卡点、制作拆解等</p>',
     '<p style="text-align: center; color: #d9d9d9; font-size: 1.1rem; margin-bottom: 40px;">Any topic goes: track polishing, technical roadblocks, production breakdowns and more</p>'),
    ('<span>1 小时 · 精准答疑</span><strong style="color: #fff;">428 元</strong>',
     '<span>1 hour \u00b7 Focused Q&amp;A</span><strong style="color: #fff;">$60</strong>'),
    ('<span>2 小时 · 深度梳理</span><strong style="color: #fff;">668 元</strong>',
     '<span>2 hours \u00b7 In-Depth Review</span><strong style="color: #fff;">$95</strong>'),
    ('<span>3 小时 · 体系化定制</span><strong style="color: #fff;">828 元</strong>',
     '<span>3 hours \u00b7 Full System Customization</span><strong style="color: #fff;">$120</strong>'),
    # 长期课程
    ('<h2>长期课程体系（分阶成长计划）</h2>', '<h2>Long-Term Program (Step-by-Step Growth Plan)</h2>'),
    ('<strong>学员身份严格保密，绑定课程独立编号搭载 ECC 数字签名，官网凭专属序列号可查进度。</strong>',
     '<strong>Student identities are kept strictly confidential. Each course is bound to an independent ID with an ECC digital signature \u2014 progress can be verified on this site with a unique serial number.</strong>'),
    # 初级
    ('<span class="course-level beginner">初级</span>', '<span class="course-level beginner">Beginner</span>'),
    ('<h3>Trance 创作核心认知课（直播互动）</h3>', '<h3>Trance Production Fundamentals (Live Group Sessions)</h3>'),
    ('<div class="price-tag small">¥1,500</div>', '<div class="price-tag small">$220</div>'),
    ('<strong>适合人群：</strong> 纯新手、对电音感兴趣的小白——想亲身体验 Trance 创作流程，获得基础编曲能力，并拓展全方位的审美',
     '<strong>Who it\u2019s for:</strong> complete beginners and the simply curious \u2014 anyone who wants to experience the Trance production process firsthand, gain basic arranging skills, and broaden their musical taste.'),
    ('<li><strong>形式：</strong> 2–4 人小班直播，节奏轻松，学完为止</li>',
     '<li><strong>Format:</strong> live small-group sessions (2\u20134 people), relaxed pace, until you\u2019re done</li>'),
    ('<li><strong>核心内容：</strong> 系统建立对 Trance 风格的认知，从零做出一首完整的作品；保护并培养你的兴趣与探索欲</li>',
     '<li><strong>Core content:</strong> a systematic introduction to the Trance style \u2014 take a track from zero to a complete piece, while protecting and nurturing your curiosity.</li>'),
    ('<strong>报名要求：</strong> 会基本宿主操作，自备一副入门监听耳机（报名前会与你确认）',
     '<strong>Requirements:</strong> basic DAW skills and a pair of entry-level monitoring headphones (confirmed with you before enrollment).'),
    ('<div class="course-benefit">结业 9 折进阶：持结业证报高阶正课享 9 折；毕业班作品点评第一名另获 300 元折扣，可用于任意课程</div>',
     '<div class="course-benefit">Graduate benefit: 10% off the next tier\u2019s full course with your certificate; the top-rated final project earns an extra $44 credit, usable on any course.</div>'),
    # 中级
    ('<span class="course-level intermediate">中级</span>', '<span class="course-level intermediate">Intermediate</span>'),
    ('<h3>风格定制 + 艺人养成计划（一对一）</h3>', '<h3>Style Development + Artist Growth Plan (1-on-1)</h3>'),
    ('<div class="price-tag small">¥5,500（含半年指导）</div>', '<div class="price-tag small">$790 (includes six months of guidance)</div>'),
    ('<strong>适合人群：</strong> 有基础的制作人，愿意跟随讲师思路、执行力强、能认真完成任务；想突破瓶颈、形成个人风格、冲击厂牌发行，乃至建立专业艺人形象',
     '<strong>Who it\u2019s for:</strong> producers with a foundation who are ready to follow the mentor\u2019s direction, execute consistently and finish the work \u2014 and who want to break through plateaus, develop a personal style, aim for label releases, and build a professional artist profile.'),
    ('<li><strong>形式：</strong> 一对一教学与指导 + 半年持续答疑（约 20 课时，因材施教）+ 作业点评 + 定期复盘；期间可停课 2–3 次，限一年内学完（特殊情况可沟通）；获发专属数字通行证，课程进度实时可查</li>',
     '<li><strong>Format:</strong> 1-on-1 teaching and guidance + six months of ongoing Q&amp;A (about 20 sessions, tailored to you) + assignment feedback + regular reviews. You may pause 2\u20133 times and must finish within one year (special cases negotiable). A personal digital pass is issued, with course progress verifiable in real time.</li>'),
    ('<li><strong>核心内容：</strong> 定制你的舞曲风格，引导并建立个人审美，打造独特声音标识；讲解混音/母带的基础知识与操作，达到发行标准；掌握区别于"经验堆砌"的专业制作思维</li>',
     '<li><strong>Core content:</strong> develop your own dance music style, build personal aesthetics with guidance, and create a distinctive sonic identity; the fundamentals and practice of mixing and mastering, up to release standard; and a professional production mindset that goes beyond trial-and-error experience.</li>'),
    ('<li><strong>艺人养成：</strong> 自我运营规划建议，厂牌狩猎策略指导，艺人自我修养提升，音乐作品包装技巧，建立可持续发展的艺人形象</li>',
     '<li><strong>Artist development:</strong> self-promotion planning, label-targeting strategy, artist self-management, presentation of your music, and building a sustainable artist image.</li>'),
    ('<li><strong>专属服务：</strong> 硬指标阶段性作业考核，保证学员质量；全程跟进进度；厂牌投稿指导</li>',
     '<li><strong>Exclusive:</strong> staged assignments with hard criteria to keep quality high; full progress follow-up; and guidance on submitting to labels.</li>'),
    ('<strong>报名要求：</strong> 熟练操作宿主软件；建议配备开放式或半开放式监听耳机（报名前会与你确认）；报名前需完成一份入学测试，评估是否合适',
     '<strong>Requirements:</strong> proficient DAW operation; open or semi-open monitoring headphones recommended (confirmed before enrollment); an entrance assessment is required to confirm fit.'),
    ('<div class="course-benefit">结业颁发结业证书与个人能力证书（如有需要）；享三年扶持计划：每年可预约与讲师合作，及系列回馈与折扣</div>',
     '<div class="course-benefit">Graduates receive a certificate of completion and a personal skills certificate (on request), plus a three-year support plan: an annual collaboration opportunity with the mentor, along with ongoing benefits and discounts.</div>'),
    # 高级
    ('<span class="course-level advanced">高级</span>', '<span class="course-level advanced">Advanced</span>'),
    ('<h3>Eonun Trance（限量）</h3>', '<h3>Eonun Trance (Limited)</h3>'),
    ('<div class="price-tag small">排期满，可咨询</div>', '<div class="price-tag small">Fully booked \u2014 inquire for availability</div>'),
    ('<strong>适合人群：</strong> 有多年制作经验，追求顶级质感与最新审美趋势，渴望彻底突破瓶颈的资深制作人——目标是以职业为导向的舞曲制作人身份（一般爱好者不推荐）',
     '<strong>Who it\u2019s for:</strong> seasoned producers with years of experience who are after top-tier sound and the latest aesthetic directions, and who want a fundamental breakthrough \u2014 aimed at those pursuing dance music production as a career (not recommended for casual hobbyists).'),
    ('<li><strong>形式：</strong> 一对一深度辅导（含私人书籍资料）+ 长期陪伴 + 讲师资源对接</li>',
     '<li><strong>Format:</strong> in-depth 1-on-1 mentorship (including private written material) + long-term support + access to the mentor\u2019s network.</li>'),
    ('<li><strong>核心内容：</strong> Eonun Trance 系列以个人未公开书籍为核心，从根源维度拆解 Trance 舞曲的律动底层逻辑与氛围生成本质，搭建体系化的律动审美认知框架；<br><br>夯实系统级自洽电声学基础理论，吃透多效果器链路的耦合作用机制，掌握独家构筑的「原理驱动型」混音创作理论：以底层数学原理为支点，推演出所有反直觉混音逻辑的底层运行法则，完成对任意风格 Trance 作品的逆向工程式全结构解析；最终实现从「模仿式制作」到「无参考原创」的第一性原理跃迁，构建起专属于你的声音风格语言与混音技巧矩阵。<br><br>同时覆盖高阶母带处理方法论、国际厂牌合作发行全流程，以及配套中级进阶衔接课程体系。</li>',
     '<li><strong>Core content:</strong> built around a private, unpublished book, the Eonun Trance series deconstructs the underlying logic of groove and the essence of atmosphere generation in Trance from first principles, establishing a systematic framework for groove aesthetics.<br><br>It grounds you in a self-consistent, system-level theory of electroacoustics, works through the coupling mechanisms of multi-effect chains, and delivers a proprietary \u201cprinciple-driven\u201d theory of mixing and production: using underlying mathematical principles as the lever to derive the operating rules behind counterintuitive mixing logic, completing a reverse-engineered, full-structure analysis of Trance works in any style. The goal is a first-principles leap from imitation to reference-free originality \u2014 a sound language and mixing technique matrix that belong to you alone.<br><br>It also covers advanced mastering methodology, the full workflow of international label collaboration and release, and the bridging curriculum that connects onward from the intermediate tier.</li>'),
    ('<strong>报名要求：</strong> 成熟的舞曲制作人——无论心智还是水平，由讲师综合评估',
     '<strong>Requirements:</strong> an established dance music producer \u2014 in both mindset and craft \u2014 assessed comprehensively by the mentor.'),
    ('<div class="course-benefit">结业特权：任意课程 5 折；邀请折扣最高可返 ¥10,000；获得讲师直接资源对接与长期扶持，形成平等合作关系</div>',
     '<div class="course-benefit">Graduate privileges: 50% off any course; referral rewards up to $1,400; direct access to the mentor\u2019s resources and long-term support, evolving into a partnership of equals.</div>'),
    ('<button type="button" class="discount-btn" onclick="openDiscountModal()">查看完整优惠与返利体系</button>',
     '<button type="button" class="discount-btn" onclick="openDiscountModal()">View the Full Discount &amp; Referral System</button>'),
    ('<p class="discount-hint">进阶折扣 · 老学员邀请返利 · 新学员礼遇</p>',
     '<p class="discount-hint">Tier discounts \u00b7 Alumni referral rewards \u00b7 New student benefits</p>'),
    # 预约
    ('<h2>预约方式与注意事项</h2>', '<h2>How to Book &amp; Things to Know</h2>'),
    ('<h4>提前沟通</h4>', '<h4>Get in Touch</h4>'),
    ('<p>通过邮件/微信私信，告知你的需求（套餐类型、问题/目标、可用时间），讲师根据情况评估个人综合能力是否合适</p>',
     '<p>Reach out by email or WeChat with your needs (service tier, questions or goals, and available times). The mentor will assess whether the fit is right.</p>'),
    ('<h4>确认预约</h4>', '<h4>Confirm Your Booking</h4>'),
    ('<p>确认时间后支付费用，发送相关工程文件/作品片段（提前24-72小时）</p>',
     '<p>Once the time is confirmed, complete payment and send your project files or track excerpts 24\u201372 hours in advance.</p>'),
    ('<h4>开始指导</h4>', '<h4>Start Your Session</h4>'),
    ('<p>通过Zoom/腾讯会议实时互动</p>', '<p>Live interaction via Zoom or Tencent Meeting.</p>'),
    ('<h3 style="color: #fff; margin-bottom: 20px; text-align: center;">注意事项</h3>',
     '<h3 style="color: #fff; margin-bottom: 20px; text-align: center;">Things to Know</h3>'),
    ('<li style="color: #d9d9d9; padding: 10px 0; border-bottom: 1px solid rgba(255, 255, 255, 0.05);">所有指导服务不包含代做工程、代发作品等行为</li>',
     '<li style="color: #d9d9d9; padding: 10px 0; border-bottom: 1px solid rgba(255, 255, 255, 0.05);">All coaching services do not include producing tracks on your behalf or submitting works for you</li>'),
    ('<li style="color: #d9d9d9; padding: 10px 0; border-bottom: 1px solid rgba(255, 255, 255, 0.05);">预约后如需改期，需提前12小时告知，否则视为一次服务已使用</li>',
     '<li style="color: #d9d9d9; padding: 10px 0; border-bottom: 1px solid rgba(255, 255, 255, 0.05);">To reschedule, give at least 12 hours\u2019 notice \u2014 otherwise the session counts as used</li>'),
    ('<li style="color: #d9d9d9; padding: 10px 0;">长期课程需通过前期沟通审核，确认符合学习条件后再报名</li>',
     '<li style="color: #d9d9d9; padding: 10px 0;">Long-term programs require an initial review through direct communication before enrollment can be confirmed</li>'),
    ('<h3>立即预约 · 开启你的Trance进阶之路</h3>', '<h3>Book Now \u00b7 Start Your Trance Journey</h3>'),
    ('<p>微信/邮件均可预约，备注"Trance指导+套餐类型"</p>',
     '<p>Book via WeChat or email \u2014 mention \u201cTrance Mentorship + service tier\u201d</p>'),
    ('<a href="weixin://" class="cta-button" title="微信号：EonunTrance">微信预约</a>',
     '<a href="weixin://" class="cta-button" title="WeChat ID: EonunTrance">Book via WeChat</a>'),
    ('<a href="mailto:eonun.official@gmail.com" class="cta-button">邮件预约</a>',
     '<a href="mailto:eonun.official@gmail.com" class="cta-button">Book via Email</a>'),
    ('微信号：EonunTrance | 邮箱：eonun.official@gmail.com',
     'WeChat: EonunTrance | Email: eonun.official@gmail.com'),
    # 返利弹层
    ('<h2>优惠与返利体系</h2>', '<h2>Discounts &amp; Referrals</h2>'),
    ('<h3>进阶之路</h3>', '<h3>The Path Upward</h3>'),
    ('<li>结业后报名下一阶段<strong>正课 9 折</strong></li>',
     '<li>10% off the next tier\u2019s full course after graduation</li>'),
    ('<li>大师课结业特权：<strong>任意课程 5 折</strong></li>',
     '<li>Masterclass graduates: <strong>50% off any course</strong></li>'),
    ('<li>长期扶持（中高级学员）：每年可预约 1–2 次与讲师合作，三年有效</li>',
     '<li>Long-term support (intermediate &amp; advanced): 1\u20132 collaboration opportunities with the mentor per year, valid for three years</li>'),
    ('<h3>老学员邀请返利</h3>', '<h3>Alumni Referral Rewards</h3>'),
    ('<li>返利标准：初级 <strong>¥150</strong> / 中级 <strong>¥300</strong> / 大师互荐 <strong>¥1,000</strong>（须同为大师课结业）</li>',
     '<li>Rewards: Beginner <strong>$22</strong> / Intermediate <strong>$44</strong> / Master-to-master <strong>$145</strong> (both parties must be masterclass graduates)</li>'),
    ('<li>邀请名额：初级 2 名 / 中级 5 名（返利封顶 ¥1,500）/ 大师 10 名（按 ¥1,000 或 ¥150–300 均计入名额）</li>',
     '<li>Referral slots: Beginner 2 / Intermediate 5 (rewards capped at $210) / Master 10 (counted at $150 or $25\u201345 per referral)</li>'),
    ('<li>低层级可邀请高层级，互不越界</li>',
     '<li>Lower tiers may refer upward; the reverse doesn\u2019t apply</li>'),
    ('<li>结算方式：课程过半付半款，结业付全款；中途退出按进度折算</li>',
     '<li>Payout: half at the midpoint of the course, the remainder at graduation; early withdrawal is prorated by progress</li>'),
    ('<li>返利有效期 12 / 24 个月，限本人使用</li>',
     '<li>Rewards are valid for 12 / 24 months and non-transferable</li>'),
    ('<li>被邀请人退费则返利作废，已使用的返利从后续款项中扣回</li>',
     '<li>If the referred student withdraws and is refunded, the reward is void; any reward already used is deducted from later payments</li>'),
    ('<h3>新学员礼遇</h3>', '<h3>New Student Benefits</h3>'),
    ('<li>结业获证后，同等享受进阶折扣等老学员权益</li>',
     '<li>After graduating with a certificate, new students enjoy the same alumni benefits, including tier discounts</li>'),
    # JS 字符串
    ("throw new Error('标语文件加载失败')", "throw new Error('Slogan file failed to load')"),
    ("console.log('随机标语加载失败，使用兜底文案：', error)", "console.log('Failed to load slogans, using fallback text:', error)"),
    ("console.log('视频加载失败，显示备用背景')", "'Video failed to load, showing fallback background'"),
    ("console.log('视频加载成功')", "'Video loaded'"),
    ("console.log('视频加载超时，显示备用背景')", "'Video load timed out, showing fallback background'"),
]

for old, new in R:
    n = src.count(old)
    if n == 0:
        print('MISS: ' + old[:70]); sys.exit(1)
    src = src.replace(old, new)

leftover = [l.strip()[:80] for l in src.split('\n') if ('¥' in l or '元' in l) and not l.strip().startswith(('/*','*','<!--','//'))]
if leftover:
    print('currency leftover:'); [print(' ', x) for x in leftover]; sys.exit(1)

old_slogan = '一个年轻人奉献给了Trance艺术的部分人生'
if src.count(old_slogan) != 2:
    print('slogan count != 2: %d' % src.count(old_slogan)); sys.exit(1)
src = src.replace(old_slogan, 'Part of a young life, devoted to the art of Trance')

out = os.path.join(BASE, '..', '..', 'content', 'en', 'instructions.md')
io.open(out, 'w', encoding='utf-8', newline='\n').write(src)
print('written: ' + out)

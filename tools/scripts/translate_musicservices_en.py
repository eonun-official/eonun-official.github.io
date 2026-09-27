# -*- coding: utf-8 -*-
"""从 zh-hans/music-services.md 生成 en/music-services.md：结构/样式/脚本不动，只替换可见文字。
价格按 2026-09-27 用户批准的英文版定价：¥330→$50, ¥950→$140, ¥985→$140, ¥5200→$750, ¥6600→$950, ¥200→$30, ¥700/h→$100/h。
注意：源文件卡片「精细母带 ¥985」与弹窗「全流程混音+母带 ¥950」不一致（待用户裁决中文源），英文版统一按 $140。"""
import io, os, sys

BASE = os.path.dirname(os.path.abspath(__file__))
src = io.open(os.path.join(BASE, '..', '..', 'content', 'zh-hans', 'music-services.md'), encoding='utf-8').read()

R = [
    ('description: "专业音乐制作服务，包括混音、母带处理等"',
     'description: "Professional music production services, including mixing and mastering"'),
    # hero
    ('<p>专业音乐制作服务</p>', '<p>Professional Music Production Services</p>'),
    ('<p>母带处理 · 音乐工程 · 商业合作</p>', '<p>Mastering \u00b7 Music Production \u00b7 Commercial Work</p>'),
    # 卡片一：母带
    ('<div class="product-badge premium">方案一</div>', '<div class="product-badge premium">Option 1</div>'),
    ('<h3>母带服务</h3>', '<h3>Mastering Service</h3>'),
    ('<div class="product-description">专业母带处理，让音乐更具商业规范与音乐性</div>',
     '<div class="product-description">Professional mastering that brings your music up to commercial standards, with musicality intact</div>'),
    ('<div class="level-name">标准母带</div>', '<div class="level-name">Standard Mastering</div>'),
    ('<div class="level-price">¥330/首</div>', '<div class="level-price">$45/track</div>'),
    ('<div class="level-desc">厂牌合作标准，适用于已完成的混音作品</div>',
     '<div class="level-desc">Label-grade standard, for finished mixes</div>'),
    ('<div class="level-name">精细母带</div>', '<div class="level-name">Premium Mastering</div>'),
    ('<div class="level-price">¥985/首</div>', '<div class="level-price">$135/track</div>'),
    ('<div class="level-desc">分轨混音+母带，专业处理方法</div>',
     '<div class="level-desc">Stem mixing + mastering, handled with professional methods</div>'),
    ('<div class="notice-text">精细混母服务由委托方自行保障素材规范、混音基底达标；\n                  分轨精度、电平失真、染色过度、时序异常等前置问题，沟通未修正的相关影响由委托方自行承担。</div>',
     '<div class="notice-text">For premium mixing &amp; mastering, the client is responsible for the quality of the source material and the mix foundation. Pre-existing issues \u2014 stem resolution, level distortion, excessive coloration, timing errors \u2014 remain the client\u2019s responsibility if left uncorrected after discussion.</div>'),
    ('<div class="price-tag">¥330起</div>', '<div class="price-tag">from $45</div>'),
    # 卡片二：音乐工程
    ('<div class="product-badge exclusive">方案二</div>', '<div class="product-badge exclusive">Option 2</div>'),
    ('<h3>音乐工程服务</h3>', '<h3>Full Track Production</h3>'),
    ('<div class="product-description">从零开始构建，将你的灵感转化为专业作品</div>',
     '<div class="product-description">Built from the ground up \u2014 turning your ideas into professional tracks</div>'),
    ('<div class="detail-text">将你的灵感、预设全部交给我</div>',
     '<div class="detail-text">Hand over your ideas, sketches and presets</div>'),
    ('<div class="detail-text">深度交流与合作创作</div>',
     '<div class="detail-text">Deep collaboration throughout the process</div>'),
    ('<div class="detail-text">合作发行高质量的成品曲目</div>',
     '<div class="detail-text">Release-ready tracks, finished to a high standard</div>'),
    ('<div class="price-tag">¥5200</div>', '<div class="price-tag">$750</div>'),
    # 按钮（两处卡片）
    ('<a href="../contact/index.html" class="buy-button left">联系咨询</a>',
     '<a href="../contact/index.html" class="buy-button left">Inquire</a>'),
    ('<a href="#" class="buy-button right" onclick="openMasteringModal()">了解详情</a>',
     '<a href="#" class="buy-button right" onclick="openMasteringModal()">Learn More</a>'),
    ('<a href="#" class="buy-button right" onclick="openServiceModal()">了解详情</a>',
     '<a href="#" class="buy-button right" onclick="openServiceModal()">Learn More</a>'),
    # 服务流程
    ('<h2>服务流程</h2>', '<h2>How It Works</h2>'),
    ('<h3>作品审核</h3>', '<h3>Track Review</h3>'),
    ('<p>提交作品Demo，我们评估作品质量和适用服务</p>',
     '<p>Submit a demo \u2014 we assess the track and match it to the right service</p>'),
    ('<h3>方案定制</h3>', '<h3>Tailored Plan</h3>'),
    ('<p>根据需求制定个性化服务方案和报价</p>',
     '<p>A personalized plan and quote, built around your goals</p>'),
    ('<h3>深度合作</h3>', '<h3>Deep Collaboration</h3>'),
    ('<p>全程沟通协作，确保作品符合预期</p>',
     '<p>Close communication at every stage, so the result matches your vision</p>'),
    ('<h3>交付与发行</h3>', '<h3>Delivery &amp; Release</h3>'),
    ('<p>交付高质量成品，协助发行推广</p>',
     '<p>High-quality final delivery, with support for release and promotion</p>'),
    # 工程服务弹窗
    ('<h2>Eonun 曲目工程制作服务</h2>', '<h2>Eonun Track Production Service</h2>'),
    ('<p>凭借多年专注 Uplifting Trance 的制作与经验，我将把你的具体需要，完整落地为结构成熟、音色精准、符合国际发行标准的成品作品。无论是完善一段动机、深化一首半成品，还是从零构建完整单曲，我都会以严谨的制作流程，让你的音乐想法真正成为可发行、可传播、具备辨识度的专业作品。</p>',
     '<p>With years of focus on Uplifting Trance production, I turn your specific requirements into finished tracks with mature structure, precise sound design and international release standards. Whether it\u2019s developing a rough idea, deepening a half-finished track, or building a complete single from scratch, a disciplined production process makes your musical ideas real \u2014 release-ready, shareable and distinctive.</p>'),
    ('<h3>服务内容</h3>', '<h3>What\u2019s Included</h3>'),
    ('<li>根据你提供的旋律、参考曲、MIDI 或创作方向，完成整首曲目从编曲、音色设计、混音到结构优化的完整工程制作，可适配游戏、影视等各类商用场景。</li>',
     '<li>A complete production \u2014 arrangement, sound design, mixing and structure optimization \u2014 built from your melody, reference tracks, MIDI files or creative direction; suitable for commercial use in games, film and more.</li>'),
    ('<li>包含 2 次免费调整，确保最终作品贴合你的风格定位与听觉预期。</li>',
     '<li>Two rounds of free revisions, so the final track matches your style and expectations.</li>'),
    ('<li>标准制作周期为 14 个自然日；如需更快上线，可选择加急流程，7 日内完成交付。</li>',
     '<li>Standard turnaround is 14 calendar days; an express option delivers within 7 days.</li>'),
    ('<h3>选择这项制作服务的理由</h3>', '<h3>Why This Service</h3>'),
    ('<p>作为获得国际现代 Trance 音乐厂牌RIIR独家专访的制作人，我长期以现代 Uplifting Trance 制作体系为核心，懂得最新的审美标准，也了解全面的审美角度，所有作品均按照国际厂牌发行标准打磨。我不参与圈层化运作，不设身份门槛，只以作品质量为唯一标准，让你的音乐在全球市场中更具竞争力。</p>',
     '<p>As a producer featured in an exclusive interview by RIIR, an international modern Trance label, my work is built on the modern Uplifting Trance production system \u2014 I keep up with current aesthetic standards while keeping a broad view of the genre, and every track is polished to the release standards of international labels. I don\u2019t play insider games and I don\u2019t gatekeep: the quality of the work is the only filter, so your music can hold its own in a global market.</p>'),
    ('<h3>你需要提供的素材</h3>', '<h3>What You\u2019ll Provide</h3>'),
    ('<li>下单后 24 小时内，请提供项目相关素材，包括画面片段、剧情参考、情绪指引、参考配乐或风格描述。</li>',
     '<li>Within 24 hours of placing the order, please provide project materials: video clips, story references, mood guidelines, reference music or a style description.</li>'),
    ('<li>同时请明确你的需求：曲风（仅限 Uplifting Trance 风格配乐）、单条时长、整体情绪与使用场景方向。</li>',
     '<li>Please also specify: the style (Uplifting Trance only for this service), the length of each piece, the overall mood, and the intended use or scene.</li>'),
    ('<h3>重要说明与版权条款</h3>', '<h3>Important Notes &amp; Copyright Terms</h3>'),
    ('<li>作为配乐制作方，我将保留 10% 著作权收益（含作曲署名权、机械权、同步权），该比例不影响你方项目的全球发行、上映与全渠道传播收益。</li>',
     '<li>As the producer, I retain 10% of copyright revenue (including composition credit, mechanical rights and sync rights). This share does not affect your project\u2019s worldwide distribution, screening, or revenue across all channels.</li>'),
    ('<li>作品交付后，若因项目调整产生额外修改，将按 ¥700 / 小时 收取调整费用。</li>',
     '<li>After delivery, additional revisions requested due to project changes are billed at $100 per hour.</li>'),
    ('<li>我全程保证制作质量与场景适配度，但不承诺或保证作品达到任何特定第三方的验收标准。</li>',
     '<li>I guarantee production quality and fit for the intended use throughout, but I do not promise or guarantee that a work will meet any particular third party\u2019s acceptance criteria.</li>'),
    ('<h3>服务价格</h3>', '<h3>Pricing</h3>'),
    ('<span class="price-label">标准制作（14 天交付）：</span>', '<span class="price-label">Standard production (14-day delivery):</span>'),
    ('<span class="price-value">¥5200</span>', '<span class="price-value">$750</span>'),
    ('<span class="price-label">加急制作（7 天交付）：</span>', '<span class="price-label">Express production (7-day delivery):</span>'),
    ('<span class="price-value">¥6600</span>', '<span class="price-value">$950</span>'),
    ('<h3>常见疑问</h3>', '<h3>Common Questions</h3>'),
    ('<li>素材要求：下单后同步详细规范，可提前沟通确认</li>',
     '<li>Materials: detailed specs are shared after ordering \u2014 happy to confirm details in advance</li>'),
    ('<li>制作流程：需求确认→初稿交付→调整优化→终版定稿</li>',
     '<li>Process: requirements confirmed \u2192 first draft \u2192 revisions \u2192 final delivery</li>'),
    ('<li>制作周期：标准 14 个自然日，加急 7 日内交付</li>',
     '<li>Turnaround: 14 calendar days standard, express within 7 days</li>'),
    ('<h3>开启你的项目配乐定制</h3>', '<h3>Start Your Custom Project</h3>'),
    ('<p>无论你是只需要单段情绪配乐，还是已有完整项目需要定制配乐，我都以稳定、可商用的制作标准，帮你把场景情绪变成真正适配项目的 Uplifting Trance 配乐。提交你的项目资料，帮你做出贴合场景、情绪到位、具备专业水准的音乐。</p>',
     '<p>Whether you need a single mood-setting piece or a full custom score for a complete project, I work to a stable, commercially usable standard \u2014 turning scene emotion into Uplifting Trance that truly fits. Send over your project materials, and let\u2019s make music that fits the scene, lands the emotion, and holds a professional standard.</p>'),
    ('<a href="../contact/index.html" class="modal-cta-button">开始合作</a>',
     '<a href="../contact/index.html" class="modal-cta-button">Start a Project</a>'),
    # 母带弹窗
    ('<h2>Eonun 混音母带服务</h2>', '<h2>Eonun Mixing &amp; Mastering Service</h2>'),
    ('<p>以 Trance 舞曲的审美逻辑与数字发行规范，完成动态、频段与响度的适配，兼顾听感质感与平台播放标准。</p>',
     '<p>Working with the aesthetic logic of Trance and the specs of digital distribution: dynamics, frequency balance and loudness \u2014 so the music feels right and plays right on every platform.</p>'),
    ('<h3>服务分级</h3>', '<h3>Service Tiers</h3>'),
    ('<h4>标准母带校准｜¥330</h4>', '<h4>Standard Mastering Tune-Up \u2014 $50</h4>'),
    ('<p>在你提供的最终立体声混音基础上，进行响度校准、全局频段规整与播放适配，交付符合流媒体发行规范的母带成品。</p>',
     '<p>Starting from your final stereo mix: loudness calibration, global frequency cleanup and playback optimization, delivered as a master that meets streaming release specs.</p>'),
    ('<h4>全流程混音 + 母带｜¥950</h4>', '<h4>Full-Cycle Mixing + Mastering \u2014 $140</h4>'),
    ('<p>针对最高 10 组分组 Stem 进行混音精修，覆盖低频结构、旋律层次、打击乐咬合与空间塑造，再经针对性母带处理优化动态与响度，交付可直接发布的成品。</p>',
     '<p>Detailed mixing of up to 10 grouped stems \u2014 low-end structure, melodic layers, drum cohesion and spatial design \u2014 followed by targeted mastering for dynamics and loudness. Delivered release-ready.</p>'),
    ('<h3>提交规范</h3>', '<h3>Delivery Specs</h3>'),
    ('<li><strong>单轨母带：</strong>提交最终立体声混音，WAV 格式，24-bit 精度，采样率保持工程原始值（44.1 / 48 kHz），不做升频或转码；峰值预留 -6 dB 净空（-6 ~ -3 dBFS 均可），总线不加限制器、压限等全局处理</li>',
     '<li><strong>Stereo mastering:</strong> submit your final stereo mix as WAV, 24-bit, at the project\u2019s original sample rate (44.1 / 48 kHz) \u2014 no upsampling or transcoding. Leave -6 dB of headroom (anything between -6 and -3 dBFS is fine); no limiter or bus compression on the master bus.</li>'),
    ('<li><strong>Stem 混音：</strong>WAV 格式，24-bit，采样率与工程一致，最多 10 组；混响、延迟等效果轨单独导出；各轨预留约 -6 dB 净空，严禁削波</li>',
     '<li><strong>Stem mixing:</strong> WAV, 24-bit, same sample rate as the project, up to 10 stems; export reverb, delay and other effect tracks separately; leave about -6 dB of headroom per stem. No clipping.</li>'),
    ('<li><strong>文件交付：</strong>建议文件名注明曲名与 BPM，打包后通过邮箱或通讯软件发送，云盘链接亦可</li>',
     '<li><strong>File delivery:</strong> include the track name and BPM in the file name, and send the archive by email or messaging app \u2014 a cloud drive link works too.</li>'),
    ('<h3>交付与加急</h3>', '<h3>Turnaround &amp; Express</h3>'),
    ('<li>标准周期：3–5 个工作日</li>', '<li>Standard: 3\u20135 business days</li>'),
    ('<li>全流程加急 24 小时交付：附加费 ¥200</li>',
     '<li>Express full-cycle delivery within 24 hours: +$29</li>'),
    ('<h3>品质核心</h3>', '<h3>The Core of the Quality</h3>'),
    ('<p>长期专注 Trance 舞曲的总线处理，按每首作品的结构与风格针对性调整，以数字发行规范交付成品。</p>',
     '<p>Years of focus on Trance bus processing. Every track is adjusted to its own structure and style, and delivered to digital distribution specs.</p>'),
    ('<h3>为发行做好准备</h3>', '<h3>Ready for Release</h3>'),
    ('<p>无论是快速响度校准，还是深度混音精修，都以发行规范为准绳，交付可直接发布的成品。若已有目标厂牌，可针对其发行作品的音色审美与响度习惯做针对性母带处理，让成品更贴合该厂牌的整体声音取向。</p>',
     '<p>From a quick loudness tune-up to deep mixing work, everything is held to release specs \u2014 delivered ready to publish. If you already have a target label in mind, the master can be tailored to the sonic aesthetic and loudness habits of its catalog, so the finished track sits naturally within that label\u2019s sound.</p>'),
    # JS 字符串
    ("throw new Error('标语文件加载失败')", "throw new Error('Slogan file failed to load')"),
    ("console.log('随机标语加载失败，使用兜底文案：', error)", "console.log('Failed to load slogans, using fallback text:', error)"),
]

for old, new in R:
    n = src.count(old)
    if n == 0:
        print('MISS: ' + old[:60]); sys.exit(1)
    src = src.replace(old, new)

# 人民币符号兜底检查：可见区不应残留 ¥
import re
leftover = [l.strip()[:80] for l in src.split('\n') if '¥' in l and not l.strip().startswith(('/*','*','<!--','//'))]
if leftover:
    print('¥ leftover:'); [print(' ', x) for x in leftover]; sys.exit(1)

old_slogan = '一个年轻人奉献给了Trance艺术的部分人生'
if src.count(old_slogan) != 2:
    print('slogan count != 2: %d' % src.count(old_slogan)); sys.exit(1)
src = src.replace(old_slogan, 'Part of a young life, devoted to the art of Trance')

out = os.path.join(BASE, '..', '..', 'content', 'en', 'music-services.md')
io.open(out, 'w', encoding='utf-8', newline='\n').write(src)
print('written: ' + out)

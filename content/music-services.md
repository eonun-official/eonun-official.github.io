---
title: "Eonun"
description: "专业音乐制作服务，包括混音、母带处理等"
body_class: "ma0 avenir bg-near-white development is-section is-section"
---
<header class="about-header" style="position:relative; overflow:hidden; background-image: url('../images/background.webp'); background-size: cover; background-position: center center; background-repeat:no-repeat; min-height:520px;">
    <div class="pb3-m pb6-l bg-black" style="background:none; padding-top:140px; ">
      <div class="nav-container" id="scroll-nav" style="position: fixed; top: -20px; left: 0; width: 100%; z-index: 9999; padding: 10px 20px; box-sizing: border-box;
          transition: top 0.3s ease;">
        <nav class="pv3 ph3 ph4-ns" role="navigation">
  <div class="flex-l center items-center justify-between">
    <a href="../index.html" class="f3 fw2 hover-white white-90 dib no-underline" style="position: relative; top: -2px;">
        <span style="
          font-family: 'EDIX' !important;
          color: #ffffff !important;
          font-size: 1.2em !important;
          font-weight: 800 !important;
          letter-spacing: 0.5ch !important; /* 关键：缩窄为0.5ch（原1ch的一半） */
          text-shadow: 0 0 3px rgba(255,255,255,0.6) !important;
          position: relative;
          top: -1px;
          display: inline-block;
        ">Eonun</span>
    </a>
    <div class="flex-l items-center">
        <ul class="pl0 mr3" style="display: flex !important; list-style: none !important; margin: 0 !important; padding: 0 !important; gap: 20px !important;">
          <li class="list f5 f4-ns fw4 dib pr3">
            <a class="hover-white white-90 no-underline" href="../shop/index.html" title="Shop page">Shop</a>
          </li>
          <li class="list f5 f4-ns fw4 dib pr3">
            <a class="hover-white white-90 no-underline" href="index.html" title="Music Services page" style="color: #ffffff !important; text-shadow: 0 0 8px rgba(255, 255, 255, 0.6) !important;">Music Services</a>
          </li>
          <li class="list f5 f4-ns fw4 dib pr3">
            <a class="hover-white white-90 no-underline" href="../instructions/index.html" title="Instructions page">Instructions</a>
          </li>
          <li class="list f5 f4-ns fw4 dib pr3">
            <a class="hover-white white-90 no-underline" href="../about/index.html" title="About page">About</a>
          </li>
          <li class="list f5 f4-ns fw4 dib pr3">
            <a class="hover-white white-90 no-underline" href="../contact/index.html" title="Contact page">Contact</a>
          </li>
        </ul>
      <div class="ananke-socials"></div>
    </div>
  </div>
  <style>
    .site-nav ul li {
      display: inline-flex !important;
      align-items: center !important;
    }
    .site-nav ul li a:hover {
      color: #f2f2f2 !important;
      text-shadow: 0 0 5px rgba(255, 255, 255, 0.8) !important;
    }
  </style>
</nav>
      </div>
      <div id="about-frost" class="about-frost-overlay" aria-hidden="true" style="opacity:0; position:absolute; inset:0;"></div>
      <div class="tc-l pv6 ph3 ph4-ns">
        <div class="mb0 lh-title" style="max-width: 800px; margin: 0 auto; position: relative; background: transparent !important;">
          <p id="index-slogan" style="
            margin: 140px 0 0 20px;
            padding: 0;
            color: #fff;
            font-size: 24px !important;
            text-align: center;
            animation: slideInFromRight 1.4s ease-out forwards;
            position: relative !important;
            transition: all 0.1s ease !important;
            font-family: 'IndexSloganFont' !important;
            font-weight: bold !important;
            font-style: normal !important;
            opacity: 0;
            transform: translateX(40%);
            filter: blur(12px);
          ">一个年轻人奉献给了Trance艺术的部分人生</p>
        </div>
      </div>
    </div>
  </header>
<script>
const indexSlogan = document.getElementById('index-slogan');
window.addEventListener('scroll', function() {
  const scrollDistance = window.scrollY;
  const fastDecay = scrollDistance / 200;
  const slowDecay = scrollDistance / 300;
  const brightness = Math.max(0.3, 1 - fastDecay);
  const opacity = Math.max(0.0, 1 - slowDecay);
  const shadowIntensity = Math.max(0., 0.3 - (0.3 * fastDecay));
  const parallaxOffset = scrollDistance * 0.6;
  const maxOffset = 250;
  const finalOffset = Math.min(parallaxOffset, maxOffset);
  if (indexSlogan) {
    indexSlogan.style.top = `${finalOffset}px`;
    indexSlogan.style.setProperty('opacity', opacity, 'important');
    indexSlogan.style.setProperty('filter', `brightness(${brightness}) drop-shadow(0 2px 10px rgba(255,255,255,${shadowIntensity}))`, 'important');
  }
});
fetch('../data/trance_mixing_slogans.txt')
  .then(response => {
    if (!response.ok) throw new Error('标语文件加载失败');
    return response.text();
  })
  .then(text => {
    const slogans = text.split('\n')
      .map(line => line.trim())
      .filter(line => line && !line.startsWith('####'));
    if (slogans.length > 0) {
      const randomSlogan = slogans[Math.floor(Math.random() * slogans.length)];
      if (indexSlogan) indexSlogan.textContent = randomSlogan;
    }
  })
  .catch(error => {
    console.log('随机标语加载失败，使用兜底文案：', error);
    if (indexSlogan) indexSlogan.textContent = '一个年轻人奉献给了Trance艺术的部分人生';
  });
  const aboutHeader = document.querySelector('header.about-header');
  if (aboutHeader) {
    requestAnimationFrame(() => { aboutHeader.classList.add('show-frost'); });
  }
</script>
<style>
  header.about-header::before {
    content: '';
    position: absolute;
    inset: 0;
    pointer-events: none;
    backdrop-filter: blur(6px) saturate(120%);
    -webkit-backdrop-filter: blur(6px) saturate(120%);
    background: linear-gradient(rgba(0,0,0,0.18), rgba(0,0,0,0.36));
    opacity: 0;
    transition: opacity 0.7s ease;
    z-index: 1;
  }
  header.about-header.show-frost::before { opacity: 1; }
  header.about-header .mb0.lh-title { z-index: 2; position: relative; }
</style>
<style>
@font-face {
  font-family: 'IndexSloganFont';
  src: url('../fonts/AlimamaShuHeiTi-Bold.3df4abd1fb6a0f809118b7287720b116f3ced4330805315953e14c92915a9fe3.otf') format('opentype');
  font-weight: bold;
  font-style: normal;
  font-display: block;
  unicode-range: U+4E00-9FFF;
}
#index-slogan {
  font-family: 'IndexSloganFont' !important;
  font-weight: bold !important;
  font-style: normal !important;
}
.site-nav ul {
  display: flex !important;
  list-style: none !important;
  margin: 0 !important;
  padding: 0 !important;
  gap: 30px !important;
  justify-content: flex-end;
  max-width: 1200px !important;
  margin: 0 auto !important;
}
.site-nav a {
  color: #fff !important;
  text-decoration: none !important;
  font-size: 16px !important;
  padding: 8px 12px !important;
  transition: color 0.2s ease !important;
}
.site-nav a:hover {
  color: #f2f2f2 !important;
}
@keyframes slideInFromRight {
  0% {
    transform: translateX(40%);
    filter: blur(12px);
    opacity: 0;
  }
  35% {
    transform: translateX(0);
    filter: blur(7px);
    opacity: 0.8;
  }
  50% {
    transform: translateX(0);
    filter: blur(0);
    opacity: 1;
  }
  100% {
    transform: translateX(0);
    filter: blur(0);
    opacity: 1;
  }
}
</style>
  <main class="pb7" role="main">
    <div class="shop-hero">
      <div class="hero-content">
        <h1 class="hero-title">Music Services</h1>
        <div class="hero-subtitle">
          <p>专业音乐制作服务</p>
          <p>母带处理 · 音乐工程 · 合作发行</p>
        </div>
      </div>
    </div>
    <div class="shop-container">
      <div class="shop-grid">
        <!-- 母带服务 -->
        <div class="product-card featured-card" onmouseenter="cardTint('#8d67fe')" onmouseleave="cardTintOut()">
          <div class="product-badge premium">方案一</div>
          <div class="product-image master-image"></div>
          <div class="product-content">
            <div class="product-content-top">
              <h3>母带服务</h3>
              <div class="product-description">专业母带处理，让音乐更具商业品质</div>
              <div class="service-levels">
                <div class="service-level">
                  <div class="level-name">标准母带</div>
                  <div class="level-price">¥330/首</div>
                  <div class="level-desc">厂牌合作标准，适用于已完成的混音作品</div>
                </div>
                <div class="service-level premium-level">
                  <div class="level-name">精细母带</div>
                  <div class="level-price">¥985/首</div>
                  <div class="level-desc">分轨混音+母带，专业处理方法</div>
                </div>
              </div>
              <div class="service-notice">
                <div class="notice-icon">⚠️</div>
                <div class="notice-text">精细混母服务由委托方自行保障素材规范、混音基底达标；
                  分轨精度、电平失真、染色过度、时序异常等前置问题，沟通未修正的相关影响由委托方自行承担。</div>
              </div>
            </div>
            <div class="product-content-bottom">
              <div class="price-container">
                <div class="price-tag">¥330起</div>
              </div>
              <div class="buy-buttons-container">
                <a href="../contact/index.html" class="buy-button left">联系咨询</a>
                <a href="#" class="buy-button right" onclick="openMasteringModal()">了解详情</a>
              </div>
            </div>
          </div>
        </div>
        <!-- 音乐工程服务 -->
        <div class="product-card featured-card" onmouseenter="cardTint('#00ff59')" onmouseleave="cardTintOut()">
          <div class="product-badge exclusive">方案二</div>
          <div class="product-image production-image"></div>
          <div class="product-content">
            <div class="product-content-top">
              <h3>音乐工程服务</h3>
              <div class="product-description">从零开始构建，将你的灵感转化为专业作品</div>
              <div class="service-details">
                <div class="service-detail-item">
                  <div class="detail-icon">🎵</div>
                  <div class="detail-text">将你的灵感、预设全部交给我</div>
                </div>
                <div class="service-detail-item">
                  <div class="detail-icon">🤝</div>
                  <div class="detail-text">深度交流与合作创作</div>
                </div>
                <div class="service-detail-item">
                  <div class="detail-icon">🚀</div>
                  <div class="detail-text">合作发行高质量的成品曲目</div>
                </div>
              </div>
            </div>
            <div class="product-content-bottom">
              <div class="price-container">
                <div class="price-tag">¥5200</div>
              </div>
              <div class="buy-buttons-container">
                <a href="../contact/index.html" class="buy-button left">联系咨询</a>
                <a href="#" class="buy-button right" onclick="openServiceModal()">了解详情</a>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div class="process-section">
      <div class="process-content">
        <h2>服务流程</h2>
        <div class="process-steps">
          <div class="process-step">
            <div class="step-number">1</div>
            <div class="step-content">
              <h3>作品审核</h3>
              <p>提交作品Demo，我们评估作品质量和适用服务</p>
            </div>
          </div>
          <div class="process-step">
            <div class="step-number">2</div>
            <div class="step-content">
              <h3>方案定制</h3>
              <p>根据需求制定个性化服务方案和报价</p>
            </div>
          </div>
          <div class="process-step">
            <div class="step-number">3</div>
            <div class="step-content">
              <h3>深度合作</h3>
              <p>全程沟通协作，确保作品符合预期</p>
            </div>
          </div>
          <div class="process-step">
            <div class="step-number">4</div>
            <div class="step-content">
              <h3>交付与发行</h3>
              <p>交付高质量成品，协助发行推广</p>
            </div>
          </div>
        </div>
      </div>
    </div>
  </main>
<script>
const scrollNav = document.getElementById('scroll-nav');
let lastScrollTop = 0;
let isScrollDown = false;
window.addEventListener('mousemove', function(e) {
  const scrollDistance = window.scrollY;
  if (scrollDistance > 0 && isScrollDown) {
    if (scrollNav) {
      if (e.clientY < 50) {
        scrollNav.style.top = '-20px';
      } else {
        scrollNav.style.top = '-100px';
      }
    }
  }
});
window.addEventListener('scroll', function() {
  const scrollDistance = window.scrollY;
  if (scrollNav) {
    if (scrollDistance === 0) {
      scrollNav.style.top = '-20px';
      isScrollDown = false;
    } else if (scrollDistance > lastScrollTop) {
      scrollNav.style.top = '-100px';
      isScrollDown = true;
    } else {
      scrollNav.style.top = '-20px';
      isScrollDown = false;
    }
  } else {
    if (scrollDistance === 0) {
      isScrollDown = false;
    } else if (scrollDistance > lastScrollTop) {
      isScrollDown = true;
    } else {
      isScrollDown = false;
    }
  }
  lastScrollTop = scrollDistance;
});
function openServiceModal() {
  const modal = document.getElementById('service-modal');
  modal.style.display = 'flex';
  document.body.style.overflow = 'hidden';
}
/* 卡片悬停 → 驱动全站色彩系统（50% 浓度）；移出 → 恢复用户保存的配色或黑白 */
function cardTint(hex) {
  if (window.eonunApplyTint) window.eonunApplyTint(hex, 100);
}
function cardTintOut() {
  if (!window.eonunApplyTint) return;
  try {
    var s = JSON.parse(localStorage.getItem('eonun-tint') || 'null');
    if (s && s.hex) window.eonunApplyTint(s.hex, s.i || 25);
    else window.eonunApplyTint('', 25);
  } catch (e) { window.eonunApplyTint('', 25); }
}
function closeServiceModal() {
  const modal = document.getElementById('service-modal');
  modal.style.display = 'none';
  document.body.style.overflow = 'auto';
}
function openMasteringModal() {
  const modal = document.getElementById('mastering-modal');
  modal.style.display = 'flex';
  document.body.style.overflow = 'hidden';
}
function closeMasteringModal() {
  const modal = document.getElementById('mastering-modal');
  modal.style.display = 'none';
  document.body.style.overflow = 'auto';
}
// 点击模态框外部关闭
window.onclick = function(event) {
  const serviceModal = document.getElementById('service-modal');
  const masteringModal = document.getElementById('mastering-modal');
  if (event.target === serviceModal) {
    closeServiceModal();
  }
  if (event.target === masteringModal) {
    closeMasteringModal();
  }
}
</script>
<!-- 服务详情悬浮窗 -->
<div id="service-modal" class="service-modal">
  <div class="service-modal-content">
    <div class="service-modal-header">
      <h2>Eonun 曲目工程制作服务</h2>
      <span class="close-button" onclick="closeServiceModal()">&times;</span>
    </div>
    <div class="service-modal-body">
      <p>凭借多年专注 Uplifting Trance 的制作与经验，我将把你的具体需要，完整落地为结构成熟、音色精准、符合国际发行标准的成品作品。无论是完善一段动机、深化一首半成品，还是从零构建完整单曲，我都会以严谨的制作流程，让你的音乐想法真正成为可发行、可传播、具备辨识度的专业作品。</p>
      <h3>服务内容</h3>
      <ul>
        <li>根据你提供的旋律、参考曲、MIDI 或创作方向，完成整首曲目从编曲、音色设计、混音到结构优化的完整工程制作，可适配游戏、影视等各类商用场景。</li>
        <li>包含 2 次免费调整，确保最终作品贴合你的风格定位与听觉预期。</li>
        <li>标准制作周期为 14 个自然日；如需更快上线，可选择加急流程，7 日内完成交付。</li>
      </ul>
      <h3>选择这项制作服务的理由</h3>
      <p>作为获得国际现代 Trance 音乐厂牌RIIR独家专访的制作人，我长期以现代 Uplifting Trance 制作体系为核心，懂得最新的审美标准，也了解全面的审美角度，所有作品均按照国际厂牌发行标准打磨。我不参与圈层化运作，不设身份门槛，只以作品质量为唯一标准，让你的音乐在全球市场中更具竞争力。</p>
      <h3>你需要提供的素材</h3>
      <ul>
        <li>下单后 24 小时内，请提供项目相关素材，包括画面片段、剧情参考、情绪指引、参考配乐或风格描述。</li>
        <li>同时请明确你的需求：曲风（仅限 Uplifting Trance 风格配乐）、单条时长、整体情绪与使用场景方向。</li>
      </ul>
      <h3>重要说明与版权条款</h3>
      <ul>
        <li>作为配乐制作方，我将保留 10% 著作权收益（含作曲署名权、机械权、同步权），该比例不影响你方项目的全球发行、上映与全渠道传播收益。</li>
        <li>作品交付后，若因项目调整产生额外修改，将按 ¥700 / 小时 收取调整费用。</li>
        <li>我全程保证制作质量与场景适配度，但不承诺或保证作品达到任何特定第三方的验收标准。</li>
      </ul>
      <h3>服务价格</h3>
      <div class="price-section">
        <div class="price-item">
          <span class="price-label">标准制作（14 天交付）：</span>
          <span class="price-value">¥5200</span>
        </div>
        <div class="price-item">
          <span class="price-label">加急制作（7 天交付）：</span>
          <span class="price-value">¥6600</span>
        </div>
      </div>
      <h3>常见疑问</h3>
      <ul>
        <li>素材要求：下单后同步详细规范，可提前沟通确认</li>
        <li>制作流程：需求确认→初稿交付→调整优化→终版定稿</li>
        <li>制作周期：标准 14 个自然日，加急 7 日内交付</li>
      </ul>
      <div class="final-note">
        <h3>开启你的项目配乐定制</h3>
        <p>无论你是只需要单段情绪配乐，还是已有完整项目需要定制配乐，我都以稳定、可商用的制作标准，帮你把场景情绪变成真正适配项目的 Uplifting Trance 配乐。提交你的项目资料，帮你做出贴合场景、情绪到位、具备专业水准的音乐。</p>
      </div>
    </div>
    <div class="service-modal-footer">
      <a href="../contact/index.html" class="modal-cta-button">开始合作</a>
    </div>
  </div>
</div>
<!-- 母带服务详情悬浮窗 -->
<div id="mastering-modal" class="service-modal">
  <div class="service-modal-content">
    <div class="service-modal-header">
      <h2>Eonun 混音母带服务</h2>
      <span class="close-button" onclick="closeMasteringModal()">&times;</span>
    </div>
    <div class="service-modal-body">
      <p>以专业 Trance 舞曲审美逻辑与海外厂牌发行标准，完成动态、频段与响度的专业适配，兼顾听感质感与平台发行规范，拒绝流水线劣化处理。</p>
      <h3>服务分级</h3>
      <div class="service-levels-modal">
        <div class="service-level-item">
          <h4>标准母带校准｜¥330</h4>
          <p>在保留作品原始听感与动态的前提下，快速完成专业响度校准、全局频段规整与播放规范优化，直接满足流媒体与厂牌基础发行标准，一站式解决非专业母带导致的电平不达标、听感粗糙问题。</p>
        </div>
        <div class="service-level-item premium-item">
          <h4>全流程混音 + 母带｜¥950</h4>
          <p>针对最高 10 组分组 Stem 做深度混音精修，覆盖低频结构、旋律层次、打击乐咬合与空间塑造；母带处理会更加具有针对性、进一步优化动态与响度、多场景播放适配，输出可直接投递适配国际厂牌的发行级成品。</p>
        </div>
      </div>
      <h3>提交规范</h3>
      <ul>
        <li>Stem 为 WAV 格式，单轨预留 ≥ -6dB 净空</li>
        <li>混响、延迟等效果轨独立导出</li>
        <li>Master 总线清空限制器、压缩器等全局处理</li>
        <li>文件打包后通过云盘链接提交</li>
      </ul>
      <h3>交付与加急</h3>
      <ul>
        <li>标准周期：3–5 个工作日</li>
        <li>全流程加急 24 小时交付：附加费 ¥200</li>
      </ul>
      <h3>品质核心</h3>
      <p>深耕 Trance 制作与海外发行体系，专注舞曲垂直领域总线处理，不套用通用模板，以发行级标准保障作品质量。</p>
      <div class="final-note">
        <h3>专业母带，让你的音乐更具竞争力</h3>
        <p>无论你是需要快速响度校准，还是深度混音精修，我都以专业 Trance 舞曲审美逻辑与海外厂牌发行标准，为你的作品提供高质量的处理服务。</p>
      </div>
    </div>
    <div class="service-modal-footer">
      <a href="../contact/index.html" class="modal-cta-button">开始合作</a>
    </div>
  </div>
</div>
  <style>
    .shop-hero {
      text-align: center;
      margin-bottom: 30px;
      padding: 20px;
      position: relative;
    }
    .hero-content {
      position: relative;
      z-index: 1;
    }
    .hero-title {
      color: #f2f2f2;
      font-size: 2rem;
      font-weight: 700;
      margin-bottom: 10px;
      letter-spacing: -0.5px;
    }
    .hero-subtitle {
      margin-bottom: 0;
      max-width: 600px;
      margin-left: auto;
      margin-right: auto;
    }
    .hero-subtitle p {
      color: #d9d9d9;
      font-size: 1rem;
      line-height: 1.5;
      margin: 3px 0;
      font-weight: 400;
    }
    .shop-container {
      max-width: 1200px;
      margin: 60px auto;
      padding: 0 20px;
    }
    .shop-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(500px, 1fr));
      gap: 40px;
    }
    .product-card {
      background: rgba(255,255,255,0.05);
      border-radius: 16px;
      overflow: hidden;
      transition: transform 0.3s ease, box-shadow 0.3s ease;
      position: relative;
      border: 1px solid rgba(255, 255, 255, 0.2);
    }
    .product-card:hover {
      transform: translateY(-8px);
      box-shadow: 0 15px 40px rgba(255, 255, 255, 0.4);
      border-color: rgba(255, 255, 255, 0.5);
    }
    .featured-card {
      background: rgba(255,255,255,0.08);
      border: 2px solid rgba(255, 255, 255, 0.3);
    }
    .featured-card:hover {
      border-color: rgba(255, 255, 255, 0.6);
    }
    .product-badge {
      position: absolute;
      top: 15px;
      right: 15px;
      padding: 6px 18px;
      border-radius: 25px;
      font-size: 11px;
      font-weight: bold;
      z-index: 10;
      letter-spacing: 0.5px;
    }
    .product-badge.premium {
      background: #0a0a0a;
      color: #f5f5f5;
      box-shadow: 0 4px 15px rgba(255, 255, 255, 0.4);
    }
    .product-badge.exclusive {
      background: linear-gradient(135deg, #d8d8d8, #a8a8a8);
      color: #fff;
      box-shadow: 0 4px 15px rgba(255, 255, 255, 0.4);
    }
    .product-image {
      height: 180px;
      background: linear-gradient(135deg, #1a1a1a, #2a2a2a);
      position: relative;
    }
    .master-image {
      background: linear-gradient(135deg, #242424 0%, #1c1c1c 50%, #181818 100%);
    }
    .production-image {
      background: linear-gradient(135deg, #1c1c1c 0%, #181818 50%, #141414 100%);
    }
    .product-content {
      padding: 30px;
    }
    .product-content-top {
      margin-bottom: 25px;
    }
    .product-content h3 {
      color: #fff;
      font-size: 26px;
      margin: 0 0 12px 0;
      font-weight: 700;
    }
    .product-description {
      color: #d9d9d9;
      font-size: 15px;
      line-height: 1.6;
      margin-bottom: 20px;
    }
    .service-levels {
      display: flex;
      flex-direction: column;
      gap: 15px;
      margin-bottom: 20px;
    }
    .service-level {
      background: rgba(255,255,255,0.05);
      border-radius: 12px;
      padding: 18px;
      border: 1px solid rgba(255,255,255,0.1);
      transition: all 0.3s ease;
    }
    .service-level:hover {
      background: rgba(255,255,255,0.08);
      border-color: rgba(255, 255, 255, 0.3);
    }
    .premium-level {
      background: rgba(255, 255, 255, 0.15);
      border: 2px solid rgba(255, 255, 255, 0.4);
      position: relative;
    }
    .premium-level:hover {
      background: rgba(255, 255, 255, 0.2);
      border-color: rgba(255, 255, 255, 0.6);
    }
    .level-badge {
      position: absolute;
      top: -10px;
      right: 15px;
      background: linear-gradient(135deg, #d8d8d8, #909090);
      color: #000;
      padding: 4px 12px;
      border-radius: 15px;
      font-size: 10px;
      font-weight: bold;
      letter-spacing: 0.5px;
    }
    .level-name {
      color: #fff;
      font-size: 16px;
      font-weight: 600;
      margin-bottom: 8px;
    }
    .level-price {
      color: #f2f2f2;
      font-size: 22px;
      font-weight: bold;
      margin-bottom: 8px;
      text-shadow: 0 0 8px rgba(255, 255, 255, 0.5);
    }
    .level-desc {
      color: #d9d9d9;
      font-size: 13px;
      line-height: 1.5;
    }
    .service-notice {
      background: rgba(255, 255, 255, 0.1);
      border-left: 4px solid #e8e8e8;
      padding: 12px 16px;
      border-radius: 8px;
      margin-bottom: 20px;
    }
    .notice-icon {
      font-size: 16px;
      margin-bottom: 6px;
    }
    .notice-text {
      color: #e8e8e8;
      font-size: 13px;
      line-height: 1.5;
    }
    .service-details {
      display: flex;
      flex-direction: column;
      gap: 12px;
      margin-bottom: 20px;
    }
    .service-detail-item {
      display: flex;
      align-items: center;
      gap: 12px;
      background: rgba(255,255,255,0.03);
      padding: 14px 18px;
      border-radius: 10px;
      border: 1px solid rgba(255,255,255,0.05);
    }
    .detail-icon {
      font-size: 20px;
    }
    .detail-text {
      color: #d9d9d9;
      font-size: 14px;
      line-height: 1.4;
    }
    .product-content-bottom {
      display: flex;
      justify-content: space-between;
      align-items: center;
      flex-wrap: wrap;
      gap: 15px;
    }
    .price-container {
      flex: 1;
    }
    .price-tag {
      color: #f2f2f2;
      font-size: 28px;
      font-weight: bold;
      text-shadow: 0 0 8px rgba(255, 255, 255, 0.5);
      background: transparent !important;
      box-shadow: none !important;
      padding: 2px 0 !important;
      border: none !important;
    }
    .buy-buttons-container {
      display: flex;
      gap: 12px;
    }
    .buy-button {
      background: #f2f2f2;
      color: #0a0a0a;
      padding: 12px 24px;
      border-radius: 50px;
      text-decoration: none;
      font-weight: bold;
      font-size: 14px;
      transition: all 0.3s ease;
      flex: 1;
      text-align: center;
      letter-spacing: 0.5px;
    }
    .buy-button:hover {
      transform: scale(1.05);
      box-shadow: 0 5px 20px rgba(255, 255, 255, 0.5);
    }
    .process-section {
      background: rgba(255,255,255,0.03);
      padding: 80px 20px;
      margin-top: 80px;
      border-top: 1px solid rgba(255, 255, 255, 0.2);
    }
    .process-content {
      max-width: 1000px;
      margin: 0 auto;
      text-align: center;
    }
    .process-content h2 {
      color: #fff;
      font-size: 36px;
      margin: 0 0 50px 0;
      font-weight: 700;
    }
    .process-steps {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
      gap: 30px;
    }
    .process-step {
      text-align: center;
      position: relative;
    }
    .step-number {
      width: 60px;
      height: 60px;
      background: #0a0a0a;
      border-radius: 50%;
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 24px;
      font-weight: bold;
      color: #fff;
      margin: 0 auto 20px;
      box-shadow: 0 4px 15px rgba(255, 255, 255, 0.4);
    }
    .step-content h3 {
      color: #fff;
      font-size: 18px;
      margin: 0 0 10px 0;
      font-weight: 600;
    }
    .step-content p {
      color: #d9d9d9;
      font-size: 14px;
      line-height: 1.6;
      margin: 0;
    }
    /* 服务详情悬浮窗样式 */
    .service-modal {
      display: none;
      position: fixed;
      z-index: 9999;
      left: 0;
      top: 0;
      width: 100%;
      height: 100%;
      background-color: rgba(0, 0, 0, 0.8);
      backdrop-filter: blur(10px);
      justify-content: center;
      align-items: center;
      animation: fadeIn 0.3s ease;
    }
    @keyframes fadeIn {
      from { opacity: 0; }
      to { opacity: 1; }
    }
    .service-modal-content {
      background: linear-gradient(135deg, rgba(18, 18, 18, 0.95), rgba(14, 14, 14, 0.95));
      margin: 5% auto;
      padding: 0;
      border-radius: 20px;
      width: 90%;
      max-width: 800px;
      max-height: 90vh;
      overflow-y: auto;
      box-shadow: 0 20px 60px rgba(255, 255, 255, 0.5);
      border: 1px solid rgba(255, 255, 255, 0.3);
      animation: slideIn 0.3s ease;
    }
    @keyframes slideIn {
      from { transform: translateY(-50px); opacity: 0; }
      to { transform: translateY(0); opacity: 1; }
    }
    .service-modal-header {
      padding: 30px 30px 20px;
      border-bottom: 1px solid rgba(255, 255, 255, 0.2);
      display: flex;
      justify-content: space-between;
      align-items: center;
    }
    .service-modal-header h2 {
      color: #fff;
      font-size: 28px;
      margin: 0;
      font-weight: 700;
      text-align: center;
      flex: 1;
    }
    .close-button {
      color: #d9d9d9;
      float: right;
      font-size: 32px;
      font-weight: bold;
      cursor: pointer;
      transition: color 0.3s ease;
      padding: 0 10px;
    }
    .close-button:hover {
      color: #f2f2f2;
      text-shadow: 0 0 10px rgba(255, 255, 255, 0.8);
    }
    .service-modal-body {
      padding: 30px;
      line-height: 1.6;
    }
    .service-modal-body p {
      color: #d9d9d9;
      margin-bottom: 20px;
      font-size: 16px;
    }
    .service-modal-body h3 {
      color: #f2f2f2;
      font-size: 22px;
      margin-top: 30px;
      margin-bottom: 15px;
      font-weight: 700;
      text-shadow: 0 0 5px rgba(255, 255, 255, 0.5);
    }
    .service-modal-body ul {
      color: #d9d9d9;
      margin-bottom: 20px;
      padding-left: 20px;
      list-style-type: none;
    }
    .service-modal-body li {
      margin-bottom: 10px;
      position: relative;
      padding-left: 15px;
    }
    .service-modal-body li::before {
      content: "•";
      color: #f2f2f2;
      font-weight: bold;
      position: absolute;
      left: 0;
    }
    /* 服务分级模态框样式 */
    .service-levels-modal {
      margin: 20px 0;
    }
    .service-level-item {
      background: rgba(255, 255, 255, 0.1);
      border-radius: 12px;
      padding: 20px;
      margin-bottom: 15px;
      border: 1px solid rgba(255, 255, 255, 0.2);
      transition: all 0.3s ease;
    }
    .service-level-item:hover {
      background: rgba(255, 255, 255, 0.15);
      transform: translateY(-2px);
    }
    .service-level-item.premium-item {
      background: linear-gradient(135deg, rgba(255, 255, 255, 0.15), rgba(255, 255, 255, 0.15));
      border: 1px solid rgba(255, 255, 255, 0.4);
    }
    .service-level-item h4 {
      color: #f2f2f2;
      font-size: 18px;
      margin: 0 0 10px 0;
      font-weight: 700;
      text-shadow: 0 0 5px rgba(255, 255, 255, 0.5);
    }
    .service-level-item p {
      color: #d9d9d9;
      margin: 0;
      font-size: 15px;
      line-height: 1.6;
    }
    .price-section {
      background: rgba(255, 255, 255, 0.1);
      border-radius: 12px;
      padding: 20px;
      margin: 20px 0;
      border: 1px solid rgba(255, 255, 255, 0.2);
    }
    .price-item {
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 12px;
      padding: 10px 0;
      border-bottom: 1px solid rgba(255, 255, 255, 0.05);
    }
    .price-item:last-child {
      border-bottom: none;
      margin-bottom: 0;
    }
    .price-label {
      color: #d9d9d9;
      font-size: 16px;
    }
    .price-value {
      color: #f2f2f2;
      font-size: 20px;
      font-weight: bold;
      text-shadow: 0 0 8px rgba(255, 255, 255, 0.5);
    }
    .final-note {
      background: linear-gradient(135deg, rgba(255, 255, 255, 0.1), rgba(255, 255, 255, 0.1));
      border-radius: 12px;
      padding: 25px;
      margin-top: 30px;
      border: 1px solid rgba(255, 255, 255, 0.2);
    }
    .final-note h3 {
      color: #fff;
      text-align: center;
      margin-bottom: 15px;
    }
    .final-note p {
      text-align: center;
      color: #d9d9d9;
    }
    .service-modal-footer {
      padding: 20px 30px 30px;
      border-top: 1px solid rgba(255, 255, 255, 0.2);
      text-align: center;
    }
    .modal-cta-button {
      background: #f2f2f2;
      color: #0a0a0a;
      padding: 15px 40px;
      border-radius: 50px;
      text-decoration: none;
      font-weight: bold;
      font-size: 18px;
      transition: all 0.3s ease;
      display: inline-block;
      box-shadow: 0 4px 15px rgba(255, 255, 255, 0.4);
    }
    .modal-cta-button:hover {
      transform: translateY(-3px);
      box-shadow: 0 8px 25px rgba(255, 255, 255, 0.6);
    }
    /* 滚动条样式 */
    .service-modal-content::-webkit-scrollbar {
      width: 8px;
    }
    .service-modal-content::-webkit-scrollbar-track {
      background: rgba(255, 255, 255, 0.05);
      border-radius: 10px;
    }
    .service-modal-content::-webkit-scrollbar-thumb {
      background: rgba(255, 255, 255, 0.5);
      border-radius: 10px;
    }
    .service-modal-content::-webkit-scrollbar-thumb:hover {
      background: rgba(255, 255, 255, 0.8);
    }
    @media (max-width: 768px) {
      .shop-grid {
        grid-template-columns: 1fr;
      }
      .product-content-bottom {
        flex-direction: column;
        align-items: stretch;
      }
      .buy-buttons-container {
        width: 100%;
      }
      .process-steps {
        grid-template-columns: 1fr;
      }
      .hero-title {
        font-size: 32px;
      }
      .product-content {
        padding: 20px;
      }
      .service-modal-content {
        width: 95%;
        margin: 10% auto;
      }
      .service-modal-header,
      .service-modal-body,
      .service-modal-footer {
        padding: 20px;
      }
      .service-modal-header h2 {
        font-size: 20px;
      }
      .service-modal-body h3 {
        font-size: 18px;
      }
      .service-modal-body p {
        font-size: 14px;
      }
    }
  </style>
      <footer class="bg-black bottom-0 w-100 pa3" role="contentinfo">
  <div class="flex justify-between">
  <a class="f4 fw4 hover-white white-70 dn dib-ns pv2 ph3 no-underline" href="../index.html" >
    &copy;  Eonun 2026 
  </a>
    <div><div class="ananke-socials"></div>
</div>
  </div>
</footer>

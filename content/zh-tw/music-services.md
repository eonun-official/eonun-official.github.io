---
title: "Eonun"
description: "專業音樂製作服務，包括混音、母帶處理等"
body_class: "ma0 avenir bg-near-white development is-section is-section page-music"
---
<header class="about-header" style="position:relative; overflow:hidden; background-image: url('/images/background.webp'); background-size: cover; background-position: center center; background-repeat:no-repeat; min-height:520px;">
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
          letter-spacing: 0.5ch !important; /* 關鍵：縮窄爲0.5ch（原1ch的一半） */
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
          ">一個年輕人奉獻給了Trance藝術的部分人生</p>
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
fetch('/data/trance_mixing_slogans.txt')
  .then(response => {
    if (!response.ok) throw new Error('標語文件加載失敗');
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
    console.log('隨機標語加載失敗，使用兜底文案：', error);
    if (indexSlogan) indexSlogan.textContent = '一個年輕人奉獻給了Trance藝術的部分人生';
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
  src: url('/fonts/AlimamaShuHeiTi-Bold.3df4abd1fb6a0f809118b7287720b116f3ced4330805315953e14c92915a9fe3.otf') format('opentype');
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
          <p>專業音樂製作服務</p>
          <p>母帶處理 · 音樂工程 · 合作發行</p>
        </div>
      </div>
    </div>
    <div class="shop-container">
      <div class="shop-grid">
        <!-- 母帶服務 -->
        <div class="product-card featured-card" onmouseenter="cardTint('#8d67fe')" onmouseleave="cardTintOut()">
          <div class="product-badge premium">方案一</div>
          <div class="product-image master-image"></div>
          <div class="product-content">
            <div class="product-content-top">
              <h3>母帶服務</h3>
              <div class="product-description">專業母帶處理，讓音樂更具商業品質</div>
              <div class="service-levels">
                <div class="service-level">
                  <div class="level-name">標準母帶</div>
                  <div class="level-price">¥330/首</div>
                  <div class="level-desc">廠牌合作標準，適用於已完成的混音作品</div>
                </div>
                <div class="service-level premium-level">
                  <div class="level-name">精細母帶</div>
                  <div class="level-price">¥985/首</div>
                  <div class="level-desc">分軌混音+母帶，專業處理方法</div>
                </div>
              </div>
              <div class="service-notice">
                <div class="notice-icon">⚠️</div>
                <div class="notice-text">精細混母服務由委託方自行保障素材規範、混音基底達標；
                  分軌精度、電平失真、染色過度、時序異常等前置問題，溝通未修正的相關影響由委託方自行承擔。</div>
              </div>
            </div>
            <div class="product-content-bottom">
              <div class="price-container">
                <div class="price-tag">¥330起</div>
              </div>
              <div class="buy-buttons-container">
                <a href="../contact/index.html" class="buy-button left">聯繫諮詢</a>
                <a href="#" class="buy-button right" onclick="openMasteringModal()">瞭解詳情</a>
              </div>
            </div>
          </div>
        </div>
        <!-- 音樂工程服務 -->
        <div class="product-card featured-card" onmouseenter="cardTint('#00ff59')" onmouseleave="cardTintOut()">
          <div class="product-badge exclusive">方案二</div>
          <div class="product-image production-image"></div>
          <div class="product-content">
            <div class="product-content-top">
              <h3>音樂工程服務</h3>
              <div class="product-description">從零開始構建，將你的靈感轉化爲專業作品</div>
              <div class="service-details">
                <div class="service-detail-item">
                  <div class="detail-icon">🎵</div>
                  <div class="detail-text">將你的靈感、預設全部交給我</div>
                </div>
                <div class="service-detail-item">
                  <div class="detail-icon">🤝</div>
                  <div class="detail-text">深度交流與合作創作</div>
                </div>
                <div class="service-detail-item">
                  <div class="detail-icon">🚀</div>
                  <div class="detail-text">合作發行高質量的成品曲目</div>
                </div>
              </div>
            </div>
            <div class="product-content-bottom">
              <div class="price-container">
                <div class="price-tag">¥5200</div>
              </div>
              <div class="buy-buttons-container">
                <a href="../contact/index.html" class="buy-button left">聯繫諮詢</a>
                <a href="#" class="buy-button right" onclick="openServiceModal()">瞭解詳情</a>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div class="process-section">
      <div class="process-content">
        <h2>服務流程</h2>
        <div class="process-steps">
          <div class="process-step">
            <div class="step-number">1</div>
            <div class="step-content">
              <h3>作品審覈</h3>
              <p>提交作品Demo，我們評估作品質量和適用服務</p>
            </div>
          </div>
          <div class="process-step">
            <div class="step-number">2</div>
            <div class="step-content">
              <h3>方案定製</h3>
              <p>根據需求制定個性化服務方案和報價</p>
            </div>
          </div>
          <div class="process-step">
            <div class="step-number">3</div>
            <div class="step-content">
              <h3>深度合作</h3>
              <p>全程溝通協作，確保作品符合預期</p>
            </div>
          </div>
          <div class="process-step">
            <div class="step-number">4</div>
            <div class="step-content">
              <h3>交付與發行</h3>
              <p>交付高質量成品，協助發行推廣</p>
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
/* 卡片懸停 → 驅動全站色彩系統（50% 濃度）；移出 → 恢復用戶保存的配色或黑白 */
function cardTint(hex) {
  if (window.eonunApplyTint) window.eonunApplyTint(hex, 100);
}
function cardTintOut() {
  if (!window.eonunApplyTint) return;
  try {
    var s = JSON.parse(localStorage.getItem('eonun-tint') || 'null');
    if (s && s.hex) window.eonunApplyTint(s.hex, s.i || 25);
    else window.eonunApplyTint('#ff2e2e', 20); /* 無已存配色時回到本頁默認紅 */
  } catch (e) { window.eonunApplyTint('#ff2e2e', 20); }
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
// 點擊模態框外部關閉
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
<!-- 服務詳情懸浮窗 -->
<div id="service-modal" class="service-modal">
  <div class="service-modal-content">
    <div class="service-modal-header">
      <h2>Eonun 曲目工程製作服務</h2>
      <span class="close-button" onclick="closeServiceModal()">&times;</span>
    </div>
    <div class="service-modal-body">
      <p>憑藉多年專注 Uplifting Trance 的製作與經驗，我將把你的具體需要，完整落地爲結構成熟、音色精準、符合國際發行標準的成品作品。無論是完善一段動機、深化一首半成品，還是從零構建完整單曲，我都會以嚴謹的製作流程，讓你的音樂想法真正成爲可發行、可傳播、具備辨識度的專業作品。</p>
      <h3>服務內容</h3>
      <ul>
        <li>根據你提供的旋律、參考曲、MIDI 或創作方向，完成整首曲目從編曲、音色設計、混音到結構優化的完整工程製作，可適配遊戲、影視等各類商用場景。</li>
        <li>包含 2 次免費調整，確保最終作品貼合你的風格定位與聽覺預期。</li>
        <li>標準制作週期爲 14 個自然日；如需更快上線，可選擇加急流程，7 日內完成交付。</li>
      </ul>
      <h3>選擇這項製作服務的理由</h3>
      <p>作爲獲得國際現代 Trance 音樂廠牌RIIR獨家專訪的製作人，我長期以現代 Uplifting Trance 製作體系爲核心，懂得最新的審美標準，也瞭解全面的審美角度，所有作品均按照國際廠牌發行標準打磨。我不參與圈層化運作，不設身份門檻，只以作品質量爲唯一標準，讓你的音樂在全球市場中更具競爭力。</p>
      <h3>你需要提供的素材</h3>
      <ul>
        <li>下單後 24 小時內，請提供項目相關素材，包括畫面片段、劇情參考、情緒指引、參考配樂或風格描述。</li>
        <li>同時請明確你的需求：曲風（僅限 Uplifting Trance 風格配樂）、單條時長、整體情緒與使用場景方向。</li>
      </ul>
      <h3>重要說明與版權條款</h3>
      <ul>
        <li>作爲配樂製作方，我將保留 10% 著作權收益（含作曲署名權、機械權、同步權），該比例不影響你方項目的全球發行、上映與全渠道傳播收益。</li>
        <li>作品交付後，若因項目調整產生額外修改，將按 ¥700 / 小時 收取調整費用。</li>
        <li>我全程保證製作質量與場景適配度，但不承諾或保證作品達到任何特定第三方的驗收標準。</li>
      </ul>
      <h3>服務價格</h3>
      <div class="price-section">
        <div class="price-item">
          <span class="price-label">標準制作（14 天交付）：</span>
          <span class="price-value">¥5200</span>
        </div>
        <div class="price-item">
          <span class="price-label">加急製作（7 天交付）：</span>
          <span class="price-value">¥6600</span>
        </div>
      </div>
      <h3>常見疑問</h3>
      <ul>
        <li>素材要求：下單後同步詳細規範，可提前溝通確認</li>
        <li>製作流程：需求確認→初稿交付→調整優化→終版定稿</li>
        <li>製作週期：標準 14 個自然日，加急 7 日內交付</li>
      </ul>
      <div class="final-note">
        <h3>開啓你的項目配樂定製</h3>
        <p>無論你是只需要單段情緒配樂，還是已有完整項目需要定製配樂，我都以穩定、可商用的製作標準，幫你把場景情緒變成真正適配項目的 Uplifting Trance 配樂。提交你的項目資料，幫你做出貼合場景、情緒到位、具備專業水準的音樂。</p>
      </div>
    </div>
    <div class="service-modal-footer">
      <a href="../contact/index.html" class="modal-cta-button">開始合作</a>
    </div>
  </div>
</div>
<!-- 母帶服務詳情懸浮窗 -->
<div id="mastering-modal" class="service-modal">
  <div class="service-modal-content">
    <div class="service-modal-header">
      <h2>Eonun 混音母帶服務</h2>
      <span class="close-button" onclick="closeMasteringModal()">&times;</span>
    </div>
    <div class="service-modal-body">
      <p>以專業 Trance 舞曲審美邏輯與海外廠牌發行標準，完成動態、頻段與響度的專業適配，兼顧聽感質感與平臺發行規範，拒絕流水線劣化處理。</p>
      <h3>服務分級</h3>
      <div class="service-levels-modal">
        <div class="service-level-item">
          <h4>標準母帶校準｜¥330</h4>
          <p>在保留作品原始聽感與動態的前提下，快速完成專業響度校準、全局頻段規整與播放規範優化，直接滿足流媒體與廠牌基礎發行標準，一站式解決非專業母帶導致的電平不達標、聽感粗糙問題。</p>
        </div>
        <div class="service-level-item premium-item">
          <h4>全流程混音 + 母帶｜¥950</h4>
          <p>針對最高 10 組分組 Stem 做深度混音精修，覆蓋低頻結構、旋律層次、打擊樂咬合與空間塑造；母帶處理會更加具有針對性、進一步優化動態與響度、多場景播放適配，輸出可直接投遞適配國際廠牌的發行級成品。</p>
        </div>
      </div>
      <h3>提交規範</h3>
      <ul>
        <li>Stem 爲 WAV 格式，單軌預留 ≥ -6dB 淨空</li>
        <li>混響、延遲等效果軌獨立導出</li>
        <li>Master 總線清空限制器、壓縮器等全局處理</li>
        <li>文件打包後通過雲盤鏈接提交</li>
      </ul>
      <h3>交付與加急</h3>
      <ul>
        <li>標準週期：3–5 個工作日</li>
        <li>全流程加急 24 小時交付：附加費 ¥200</li>
      </ul>
      <h3>品質核心</h3>
      <p>深耕 Trance 製作與海外發行體系，專注舞曲垂直領域總線處理，不套用通用模板，以發行級標準保障作品質量。</p>
      <div class="final-note">
        <h3>專業母帶，讓你的音樂更具競爭力</h3>
        <p>無論你是需要快速響度校準，還是深度混音精修，我都以專業 Trance 舞曲審美邏輯與海外廠牌發行標準，爲你的作品提供高質量的處理服務。</p>
      </div>
    </div>
    <div class="service-modal-footer">
      <a href="../contact/index.html" class="modal-cta-button">開始合作</a>
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
    /* 服務詳情懸浮窗樣式 */
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
    /* 服務分級模態框樣式 */
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
    /* 滾動條樣式 */
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

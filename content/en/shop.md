---
title: "Eonun"
description: "Professional Trance sample packs and high-quality audio material"
body_class: "ma0 avenir bg-near-white development is-section is-section"
extra_css:
  - css/shop-page.css
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
            <a class="hover-white white-90 no-underline" href="index.html" title="Shop page" style="color: #ffffff !important; text-shadow: 0 0 8px rgba(255, 255, 255, 0.6) !important;">Shop</a>
          </li>
          <li class="list f5 f4-ns fw4 dib pr3">
            <a class="hover-white white-90 no-underline" href="../music-services/index.html" title="Music Services page">Music Services</a>
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
          ">Part of a young life, devoted to the art of Trance</p>
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
    if (!response.ok) throw new Error('Slogan file failed to load');
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
    console.log('Failed to load slogans, using fallback text:', error);
    if (indexSlogan) indexSlogan.textContent = 'Part of a young life, devoted to the art of Trance';
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
        <h1 class="hero-title">Shop</h1>
        <div class="hero-subtitle">
          <p>Professional Trance Sample Packs</p>
          <p>High-quality audio material · Download and use right away</p>
        </div>
      </div>
    </div>
    <div class="shop-container">
      <!-- 敬请期待提示 -->
      <div style="text-align: center; padding: 4rem 2rem; margin-bottom: 2rem;">
        <div style="font-size: 2rem; font-weight: 600; color: #ffffff; margin-bottom: 2rem;">Coming Soon</div>
        <p style="font-size: 1.1rem; color: #ffffff; max-width: 600px; margin: 0 auto;">The store is under preparation — more professional Trance sample packs are on the way. Stay tuned for updates!</p>
      </div>
      <!-- 产品网格 (暂时隐藏) -->
      <div class="shop-grid" style="display: none;">
        <!-- Trance Essentials Vol.1 -->
        <div class="product-card">
          <div class="product-badge new">NEW</div>
          <div class="product-image"></div>
          <div class="product-content">
            <div class="product-content-top">
              <h3>Trance Essentials Vol.1</h3>
              <div class="product-description">A professional Trance sample pack covering a wide range of sounds</div>
            </div>
            <div class="product-content-bottom">
              <div class="price-container">
                <div class="price-tag">$29.99</div>
              </div>
              <div class="buy-buttons-container">
              <a href="#" class="buy-button left">International Payment</a>
              <a href="#" class="buy-button right">Buy on Afdian</a>
            </div>
            </div>
          </div>
        </div>
        <!-- Atmospheric Pads -->
        <div class="product-card">
          <div class="product-badge hot">HOT</div>
          <div class="product-image"></div>
          <div class="product-content">
            <div class="product-content-top">
              <h3>Atmospheric Pads</h3>
              <div class="product-description">Atmospheric synth sounds, suited to all kinds of electronic music</div>
            </div>
            <div class="product-content-bottom">
              <div class="price-container">
                <div class="price-tag">$19.99</div>
              </div>
              <div class="buy-buttons-container">
                <a href="#" class="buy-button left">International Payment</a>
                <a href="#" class="buy-button right">Buy on Afdian</a>
              </div>
            </div>
          </div>
        </div>
        <!-- Euphoric Leads -->
        <div class="product-card">
          <div class="product-badge new">NEW</div>
          <div class="product-image"></div>
          <div class="product-content">
            <div class="product-content-top">
              <h3>Euphoric Leads</h3>
              <div class="product-description">Energetic lead sounds that give your tracks a distinct character</div>
            </div>
            <div class="product-content-bottom">
              <div class="price-container">
                <div class="price-tag">$24.99</div>
              </div>
              <div class="buy-buttons-container">
                <a href="#" class="buy-button left">International Payment</a>
                <a href="#" class="buy-button right">Buy on Afdian</a>
              </div>
            </div>
          </div>
        </div>
        <!-- Drum Elements -->
        <div class="product-card">
          <div class="product-image"></div>
          <div class="product-content">
            <div class="product-content-top">
              <h3>Drum Elements</h3>
              <div class="product-description">Professional drum samples with a wide range of rhythmic elements</div>
            </div>
            <div class="product-content-bottom">
              <div class="price-container">
                <div class="price-tag">$34.99</div>
              </div>
              <div class="buy-buttons-container">
                <a href="#" class="buy-button left">International Payment</a>
                <a href="#" class="buy-button right">Buy on Afdian</a>
              </div>
            </div>
          </div>
        </div>
        <!-- Vocal Chops -->
        <div class="product-card">
          <div class="product-badge limited">LIMITED</div>
          <div class="product-image"></div>
          <div class="product-content">
            <div class="product-content-top">
              <h3>Vocal Chops</h3>
              <div class="product-description">Hand-picked vocal chops that add an emotional touch to your tracks</div>
            </div>
            <div class="product-content-bottom">
              <div class="price-container">
                <div class="price-tag">$39.99</div>
              </div>
              <div class="buy-buttons-container">
                <a href="#" class="buy-button left">International Payment</a>
                <a href="#" class="buy-button right">Buy on Afdian</a>
              </div>
            </div>
          </div>
        </div>
        <!-- Complete Bundle -->
        <div class="product-card">
          <div class="product-image"></div>
          <div class="product-content">
            <div class="product-content-top">
              <h3>Complete Bundle</h3>
              <div class="product-description">The complete bundle of all sample packs at a 40% discount</div>
            </div>
            <div class="product-content-bottom">
              <div class="price-container">
                <div class="price-tag">$99.99</div>
              </div>
              <div class="buy-buttons-container">
                <a href="#" class="buy-button left">International Payment</a>
                <a href="#" class="buy-button right">Buy on Afdian</a>
              </div>
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
// 移动端：标语降为 16px（内联 24px!important 只有 JS 内联才能覆盖）；回桌面恢复 24px
function applyMobileSloganSize() {
  if (!indexSlogan) return;
  if (window.innerWidth <= 768) {
    indexSlogan.style.setProperty('font-size', '16px', 'important');
  } else {
    indexSlogan.style.setProperty('font-size', '24px', 'important');
  }
}
applyMobileSloganSize();
window.addEventListener('resize', applyMobileSloganSize);
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
</script>
      <footer class="bg-black bottom-0 w-100 pa3" role="contentinfo">
  <div class="flex justify-between">
  <a class="f4 fw4 hover-white white-70 dn dib-ns pv2 ph3 no-underline" href="../index.html" >
    &copy;  Eonun 2026 
  </a>
    <div><div class="ananke-socials"></div>
</div>
  </div>
</footer>

<style>
  /* ===== 移动端字号自适应（仅 ≤768px，桌面零影响；下限=小米14 现值，大屏机等比放大）===== */
  @media (max-width: 768px) {
    #index-slogan { text-align: center !important; }
    /* 以下为与主页完全一致的 hero 方案 */
    #header-logo { display: block !important; margin-left: auto !important; margin-right: auto !important; }
    .tc-l h2.fw1 { font-size: 1rem !important; line-height: 1.5 !important; }
    /* 容器基准=主页 article clamp；内联 rem 文本转 em 跟随容器缩放 */
    main { font-size: clamp(15px, 3.85vw, 18px) !important; }
    [style*="font-size: 2rem"] { font-size: 2em !important; }
    [style*="font-size: 1.1rem"] { font-size: 1.1em !important; }
  }
</style>

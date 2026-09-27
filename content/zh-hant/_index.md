---
title: "Eonun | Trance 聲波雕刻師 | Eonun"
description: "歡迎來到 Eonun 領域：Trance 製作、風格設計、母帶工程、美學與概念"
body_class: "ma0 avenir bg-near-white development is-home"
---
<header class="cover-top " style="position:relative; overflow:visible; background-color: rgba(255, 255, 255, 0.2); padding-bottom: 0;">
  <video autoplay muted loop playsinline preload="none" poster="/videos/THEME-poster.jpg" data-src="/videos/THEME.mp4" style="position:absolute; top:0; left:0; width:100%; height:113%; object-fit: cover; z-index:0;" id="header-video"></video>
  <div id="video-fallback" style="position:absolute; top:0; left:0; width:100%; height:113%; background: linear-gradient(135deg, #121212 0%, #181818 25%, #1e1e1e 50%, #222222 75%, rgba(255, 255, 255, 0.1) 100%); z-index:-1; display:none;"></div>
  <div class="nav-container" id="scroll-nav" style="position: fixed; top: -20px; left: 0; width: 100%; z-index: 10000; padding: 10px 20px; box-sizing: border-box;
          transition: top 0.3s ease;">
        <nav class="pv3 ph3 ph4-ns" role="navigation">
  <div class="flex-l center items-center justify-between">
    <a href="index.html" class="f3 fw2 hover-white white-90 dib no-underline" style="position: relative; top: -2px;">
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
        <ul class="pl0 mr3" 
            style="display: flex !important; list-style: none !important; margin: 0 !important; padding: 0 !important; gap: 20px !important;">
          <li class="list f5 f4-ns fw4 dib pr3">
            <a class="hover-white white-90 no-underline" href="/shop/index.html" title="Shop page">Shop</a>
          </li>
          <li class="list f5 f4-ns fw4 dib pr3">
            <a class="hover-white white-90 no-underline" href="/music-services/index.html" title="Music Services page">Music Services</a>
          </li>
          <li class="list f5 f4-ns fw4 dib pr3">
            <a class="hover-white white-90 no-underline" href="/instructions/index.html" title="Instructions page">Instructions</a>
          </li>
          <li class="list f5 f4-ns fw4 dib pr3">
            <a class="hover-white white-90 no-underline" href="/about/index.html" title="About page">About</a>
          </li>
          <li class="list f5 f4-ns fw4 dib pr3">
            <a class="hover-white white-90 no-underline" href="/contact/index.html" title="Contact page">Contact</a>
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

  <div class="bg-black-60" style="
    background: linear-gradient(to bottom, 
        rgba(18,18,18,0.7), 
        rgba(18,18,18,0.8), 
        rgba(18,18,18,0.9)) !important;
    background-size: 100% 100%;
    position: relative;
    z-index: 1;
    height: 113%;">
    <style>
      .bg-black-60::after {
        content: '';
        position: absolute;
        bottom: -13%;
        left: 0;
        width: 100%;
        height: 13%;
        background: linear-gradient(to bottom, 
            rgba(18,18,18,0.9), 
            rgba(18,18,18,0.95));
        z-index: 1;
      }
      /* 動態柔和流光效果 */
      @keyframes softGlow {
        0%, 100% {
          filter: brightness(1) drop-shadow(0 1px 5px rgba(255, 255, 255, 0.2));
          opacity: 1;
        }
        25% {
          filter: brightness(1.03) drop-shadow(0 2px 10px rgba(255, 255, 255, 0.3)) drop-shadow(0 1px 5px rgba(255, 255, 255, 0.2));
          opacity: 1;
        }
        50% {
          filter: brightness(1.06) drop-shadow(0 3px 15px rgba(255, 255, 255, 0.4)) drop-shadow(0 1px 5px rgba(255, 255, 255, 0.2));
          opacity: 1;
        }
        75% {
          filter: brightness(1.03) drop-shadow(0 2px 10px rgba(255, 255, 255, 0.3)) drop-shadow(0 1px 5px rgba(255, 255, 255, 0.2));
          opacity: 1;
        }
      }
      @keyframes lightFlow {
        0% {
          background-position: -100% 0;
        }
        100% {
          background-position: 200% 0;
        }
      }
      #header-logo {
        position: relative;
      }
      #header-logo::before {
        content: '';
        position: absolute;
        top: -15px;
        left: -15px;
        right: -15px;
        bottom: -15px;
        background: linear-gradient(
          90deg,
          transparent,
          rgba(255,255,255,0.15),
          rgba(255, 255, 255, 0.2),
          rgba(255,255,255,0.15),
          transparent
        );
        background-size: 200% 200%;
        animation: lightFlow 12s ease-in-out infinite;
        opacity: 0.4;
        border-radius: 8px;
        z-index: -1;
        pointer-events: none;
      }
      /* 初始狀態添加柔和發光效果 */
      #header-logo.initial {
        animation: softGlow 7.2s ease-in-out infinite;
      }
    </style>
      <div class="tc-l pv6 pv8-l ph3 ph4-ns">
        <div class="mb0 lh-title" style="max-width: 800px; margin: 0 auto; position: relative; background: transparent !important; ">
          <img id="header-logo" src="/images/eonun2www.png" alt="Eonun | Trance 聲波雕刻師" fetchpriority="high" decoding="async"
            style="width: 100%; height: auto;
                margin-top: 100px !important; 
                opacity: 1 !important;
                position: relative; 
                top: 0;
                background: transparent !important;"/>
          <p id="index-slogan" style="
            margin: 20px 0 0 20px;
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
        <h2 class="fw1 f5 f3-l white-80 measure-wide-l center lh-copy mt4 mb4">
          歡迎來到 Eonun 領域：Trance 製作、風格設計、母帶工程、美學與概念
        </h2>
      </div>
    </div>
  </header>
<script>
const headerLogo = document.getElementById('header-logo');
const scrollNav = document.getElementById('scroll-nav');
const indexSlogan = document.getElementById('index-slogan');
const headerVideo = document.getElementById('header-video');
const videoFallback = document.getElementById('video-fallback');
let lastScrollTop = 0;
let isScrollDown = false;
// 移動端：標語降爲 16px（內聯 24px!important 只有 JS 內聯才能覆蓋）；回桌面恢復 24px
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
// 視頻錯誤處理
if (headerVideo) {
  headerVideo.addEventListener('error', function() {
    console.log('視頻加載失敗，顯示備用背景');
    if (videoFallback) {
      videoFallback.style.display = 'block';
    }
  });
  // 檢查視頻是否能正常播放
  headerVideo.addEventListener('loadeddata', function() {
    console.log('視頻加載成功');
  });
  // 頁面其它內容全部加載完後，再後臺加載視頻：加載到哪兒播到哪兒，互不拖累
  window.addEventListener('load', function() {
    setTimeout(function() {
      if (headerVideo && !headerVideo.getAttribute('src')) {
        headerVideo.src = headerVideo.getAttribute('data-src');
        headerVideo.load();
        var pr = headerVideo.play();
        if (pr && pr.catch) { pr.catch(function(){}); }
        // 視頻開始加載後才計時：8秒還緩衝不出畫面就換備用漸變背景
        setTimeout(function() {
          if (headerVideo.readyState < 2) {
            console.log('視頻加載超時，顯示備用背景');
            if (videoFallback) { videoFallback.style.display = 'block'; }
          }
        }, 8000);
      }
    }, 50);
  });
}
// 初始狀態添加柔和發光效果
if (headerLogo) {
  headerLogo.classList.add('initial');
}
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
  const fastDecay = scrollDistance / 200;
  const slowDecay = scrollDistance / 300;
  const brightness = Math.max(0.3, 1 - fastDecay);
  const opacity = Math.max(0.0, 1 - slowDecay);
  const shadowIntensity = Math.max(0., 0.3 - (0.3 * fastDecay));
  const parallaxOffset = scrollDistance * 0.6; 
  const maxOffset = 250; 
  const finalOffset = Math.min(parallaxOffset, maxOffset);
  // 當開始滾動時，移除初始動畫類，讓滾動效果接管
  if (headerLogo && scrollDistance > 10) {
    headerLogo.classList.remove('initial');
  }
  if (headerLogo) {
    headerLogo.style.top = `${finalOffset}px`;
    headerLogo.style.filter = `brightness(${brightness}) drop-shadow(0 2px 10px rgba(255,255,255,${shadowIntensity}))`;
    headerLogo.style.opacity = opacity;
    if (headerLogo.classList.contains('wakeup-init')) {
      requestAnimationFrame(() => headerLogo.classList.add('wakeup'));
      }
  }
  if (indexSlogan) {
    indexSlogan.style.top = `${finalOffset}px`;
    indexSlogan.style.setProperty('opacity', opacity, 'important');
    indexSlogan.style.setProperty('filter', `brightness(${brightness}) drop-shadow(0 2px 10px rgba(255,255,255,${shadowIntensity}))`, 'important');
  }
  if (scrollNav) {
    if (scrollDistance === 0) {
      scrollNav.style.top = '-20px';
      isScrollDown = false;
      // 回到頂部時重新添加初始動畫類
      if (headerLogo) {
        headerLogo.classList.add('initial');
      }
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
// 加載標語文件
fetch('/data/trance_mixing_slogans.txt')
  .then(response => {
    if (!response.ok) throw new Error('標語文件加載失敗: ' + response.status);
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
    console.error('標語文件加載失敗，使用默認標語:', error);
    // 使用默認標語作爲兜底
    if (indexSlogan) indexSlogan.textContent = '一個年輕人奉獻給了Trance藝術的部分人生';
  });
  document.addEventListener('DOMContentLoaded', function() {
    const aboutHeader = document.querySelector('header.about-header');
    if (aboutHeader) {
      requestAnimationFrame(() => { aboutHeader.classList.add('show-frost'); });
    }
  });
</script>
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
      <main class="pb7" role="main" style="position: relative; z-index: 2;">
        <article class="cf ph3 ph5-l pv3 pv4-l f4 tc-l center measure-wide lh-copy nested-links mid-gray">
    <!-- 無需額外標題，logo+隨機標語已佔頂部，直接上核心內容 -->
<h2 id="用聲波定義-trance-的質感邊界">用聲波，定義 Trance 質感邊界</h2>
<div style="max-width: 900px; margin: 40px auto; color: #ffffff; line-height: 1.8; font-size: 18px;">
  專注於現代 Uplifting / Tech Trance 製作與母帶工程，從臥室混音到國際平臺發行，用<span style="font-weight: bold;">前沿的音樂審美理念</span>與<span style="font-weight: bold;">獨家完備的理論體系</span>，讓每首作品都具備國際級質感。
</div>
<div style="height: 2px; margin: 40px 0; background: linear-gradient(90deg, rgba(255, 255, 255, 0.8), rgba(255, 255, 255, 0.8)); border-radius: 1px; box-shadow: 0 0 10px rgba(255, 255, 255, 0.6), 0 0 20px rgba(255, 255, 255, 0.3);"></div>
<h2 id="核心身份">核心身份</h2>
<div class="identity-strip">
  <div class="identity-item">
    <h3>Trance 製作人</h3>
    <p>Uplifting / Tech Trance 爲主</p>
  </div>
  <div class="identity-item">
    <h3>母帶工程師</h3>
    <p>上百首榜單Trance作品專業母帶處理</p>
  </div>
  <div class="identity-item">
    <h3>聯合創始人</h3>
    <p>兼首任 Cooperation Trance A&amp;R</p>
  </div>
  <div class="identity-item">
    <h3>廠牌 A&amp;R</h3>
    <p>Polar Impact 團隊策劃</p>
  </div>
</div>
<div style="height: 1px; margin: 40px 0; background: linear-gradient(90deg, rgba(255, 255, 255, 0.8), rgba(255, 255, 255, 0.8)); border-radius: 1px; box-shadow: 0 0 10px rgba(255, 255, 255, 0.6), 0 0 20px rgba(255, 255, 255, 0.3);"></div>
<h2 id="國內外認可--合作背書">國內外認可 · 合作背書</h2>
<div class="cred-wrap">
    <div class="cred-col">
      <h3 class="cred-title">獨家報道</h3>
      <div class="cred-frame">
        <div id="slider" style="position: relative; width: 100%; height: 100%;">
          <a href="https://www.r2rmusic.com/post/artist-feature-eonun" target="_blank" class="slide" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; text-decoration: none; display: flex; align-items: center; justify-content: center; opacity: 0; transition: opacity 0.5s ease-in-out;">
            <img src="/images/1.webp" loading="lazy" decoding="async" alt="獨家報道1" style="width: auto; height: auto; max-width: 100%; max-height: 100%; object-fit: contain; display: block;">
          </a>
          <a href="https://www.r2rmusic.com/post/artist-feature-eonun" target="_blank" class="slide" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; text-decoration: none; display: flex; align-items: center; justify-content: center; opacity: 0; transition: opacity 0.5s ease-in-out;">
            <img src="/images/2.webp" loading="lazy" decoding="async" alt="獨家報道2" style="width: auto; height: auto; max-width: 100%; max-height: 100%; object-fit: contain; display: block;">
          </a>
          <a href="https://www.r2rmusic.com/post/artist-feature-eonun" target="_blank" class="slide" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; text-decoration: none; display: flex; align-items: center; justify-content: center; opacity: 0; transition: opacity 0.5s ease-in-out;">
            <img src="/images/3.webp" loading="lazy" decoding="async" alt="獨家報道3" style="width: auto; height: auto; max-width: 100%; max-height: 100%; object-fit: contain; display: block;">
          </a>
          <a href="https://www.r2rmusic.com/post/artist-feature-eonun" target="_blank" class="slide" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; text-decoration: none; display: flex; align-items: center; justify-content: center; opacity: 0; transition: opacity 0.5s ease-in-out;">
            <img src="/images/4.webp" loading="lazy" decoding="async" alt="獨家報道4" style="width: auto; height: auto; max-width: 100%; max-height: 100%; object-fit: contain; display: block;">
          </a>
        </div>
      </div>
    </div>
    <div class="cred-col cred-col-wide">
      <h3 class="cred-title">AFTERHOURS 國際電臺特邀</h3>
      <div class="cred-frame cred-frame-wide">
        <div class="takeover-strip">
          <img src="/images/Takeover1.webp" loading="lazy" decoding="async" alt="Takeover 1" class="takeover-img">
          <img src="/images/Takeover2.webp" loading="lazy" decoding="async" alt="Takeover 2" class="takeover-img">
          <img src="/images/Takeover3.webp" loading="lazy" decoding="async" alt="Takeover 3" class="takeover-img">
          <img src="/images/Takeover4.webp" loading="lazy" decoding="async" alt="Takeover 4" class="takeover-img">
        </div>
      </div>
    </div>
  </div>
</div>
<style>
  /* ===== 主頁統一設計語言 v3（2026-09-27）：細線框 + 灰階層級 + 字距標題 ===== */
  .block-subtitle { color: #fff; font-size: 21px; text-align: center; margin: 0 0 36px 0; letter-spacing: 1px; }
  .service-wrap { max-width: 940px; margin: 60px auto; }
  .service-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 20px; }
  .service-card { border: 1px solid rgba(255, 255, 255, 0.14); border-radius: 10px; padding: 28px 26px; }
  .service-card h4 { color: #fff; font-size: 17px; margin: 0 0 12px 0; letter-spacing: 0.5px; }
  .service-card p { color: #999999; font-size: 13px; line-height: 1.75; margin: 0; }
  .works-wrap { max-width: 1200px; margin: 60px auto; }
  .works-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(350px, 1fr)); gap: 30px; }
  .work-embed { width: 100%; border: none; border-radius: 12px; display: block; background: transparent; }
  /* 網易雲裁切：放大並偏移 iframe，裁掉其自帶邊距/陰影/白框邊，內容貼邊呈現 */
  .work-163-crop { height: 430px; overflow: hidden; border-radius: 12px; background: #ffffff; }
  .work-embed--163 { width: calc(100% + 14px); height: 464px; margin: -20px 0 0 -10px; }
  .work-embed--spotify { height: 430px; }
  .work-embed--163 { height: 430px; }
  .work-note { color: #999999; text-align: center; margin-top: 14px; font-size: 13px; }
  .work-note a { color: #ffffff; text-decoration: none; }
  .contact-cta { max-width: 640px; margin: 60px auto 20px; padding: 50px 20px 0; text-align: center; border-top: 1px solid rgba(255, 255, 255, 0.18); }
  .contact-cta h3 { color: #fff; font-size: 22px; margin: 0 0 18px 0; letter-spacing: 1px; }
  .contact-cta > p { color: #999999; font-size: 14px; margin: 0 0 30px 0; line-height: 1.7; }
  .cta-pill { background: #f2f2f2; color: #0a0a0a; padding: 12px 34px; border-radius: 50px; text-decoration: none; font-weight: bold; font-size: 16px; display: inline-block; transition: background 0.25s ease, transform 0.25s ease; }
  .cta-pill:hover { background: #ffffff; transform: translateY(-2px); }
  .collab-block { max-width: 900px; margin: 60px auto; text-align: center; }
  .collab-title { color: #fff; font-size: 20px; margin: 0 0 26px 0; letter-spacing: 1px; }
  .collab-strip { display: flex; justify-content: center; flex-wrap: wrap; border-top: 1px solid rgba(255, 255, 255, 0.18); border-bottom: 1px solid rgba(255, 255, 255, 0.18); }
  .collab-item { padding: 16px 30px; font-size: 15px; color: #f2f2f2; }
  .collab-item + .collab-item { border-left: 1px solid rgba(255, 255, 255, 0.12); }
  .collab-item em { font-style: normal; color: #777777; font-size: 13px; }
  .collab-desc { color: #999999; margin-top: 24px; font-size: 13px; line-height: 1.8; }
</style>
<style>
  /* ===== 核心身份：署名條設計（2026-09-27 v2，credit strip 取代卡片盒） ===== */
  .identity-strip { max-width: 900px; margin: 50px auto; border-top: 1px solid rgba(255, 255, 255, 0.18); border-bottom: 1px solid rgba(255, 255, 255, 0.18); display: flex; }
  .identity-item { flex: 1; padding: 30px 18px; text-align: center; }
  .identity-item + .identity-item { border-left: 1px solid rgba(255, 255, 255, 0.12); }
  .identity-item h3 { color: #fff; margin: 0 0 8px 0; font-size: 18px; font-weight: 600; letter-spacing: 1px; }
  .identity-item p { color: #999999; margin: 0; font-size: 13px; line-height: 1.7; }
  /* ===== 認可背書：桌面雙欄與舊版視覺一致（300 + 600） ===== */
  .cred-wrap { max-width: 940px; margin: 60px auto; display: grid; grid-template-columns: 300px 1fr; gap: 40px; align-items: stretch; }
  .cred-title { color: #f2f2f2; font-size: 15px; letter-spacing: 2px; font-weight: 600; text-align: center; margin: 0 0 20px 0; }
  .cred-frame { position: relative; width: 100%; height: 300px; overflow: hidden; border-radius: 12px; background: rgba(255,255,255,0.02); border: 1px solid rgba(255, 255, 255, 0.15); box-sizing: border-box; transition: border-color 0.3s ease; }
  .cred-frame:hover { border-color: rgba(255, 255, 255, 0.4); }
  .takeover-strip { display: flex; height: 100%; gap: 0; margin: 0; padding: 0; align-items: stretch; }
  .takeover-img { height: 100%; object-fit: cover; display: block; margin: 0; padding: 0; border: none; flex-shrink: 0; transition: transform 0.3s ease; }
  @media (max-width: 768px) {
    /* 核心身份：2×2 井字分隔，任何屏寬下穩定對稱 */
    .identity-strip { display: grid; grid-template-columns: 1fr 1fr; margin: 30px 0; }
    .identity-item { padding: 22px 10px; }
    .identity-item + .identity-item { border-left: none; }
    .identity-item:nth-child(odd) { border-right: 1px solid rgba(255, 255, 255, 0.12); }
    .identity-item:nth-child(-n+2) { border-bottom: 1px solid rgba(255, 255, 255, 0.12); }
    .identity-item h3 { font-size: 15px; margin-bottom: 6px; }
    .identity-item p { font-size: 12px; }
    /* 認可背書：縱向堆疊； slider 方框隨屏寬等比縮放； 四圖改 2×2 不再細條 */
    .cred-wrap { grid-template-columns: 1fr; gap: 28px; margin: 30px 0; }
    .cred-frame { height: auto; aspect-ratio: 1 / 1; }
    .cred-frame-wide { aspect-ratio: auto; }
    .takeover-strip { display: grid; grid-template-columns: 1fr 1fr; gap: 8px; height: auto; }
    .takeover-img { width: 100%; height: auto; aspect-ratio: 1 / 1; }
    /* 統一設計語言 v3 移動端 */
    .service-wrap, .works-wrap, .collab-block { margin: 30px 0; }
    .service-grid { grid-template-columns: 1fr; gap: 14px; }
    .service-card { padding: 22px 18px; }
    .works-grid { grid-template-columns: 1fr; gap: 20px; }
    .work-embed--spotify { height: 352px; }
    .contact-cta { margin: 30px auto 10px; padding-top: 36px; }
    .collab-item { padding: 13px 16px; font-size: 13px; }
    .collab-item em { font-size: 11px; }
  }
</style>
<script>
  const slides = document.querySelectorAll('#slider .slide');
  let currentIndex = 0;
  function showSlide(index) {
    slides.forEach((slide, i) => {
      slide.style.opacity = i === index ? '1' : '0';
    });
  }
  function nextSlide() {
    currentIndex = (currentIndex + 1) % slides.length;
    showSlide(currentIndex);
  }
  showSlide(0);
  setInterval(nextSlide, 5000);
</script>
<style>
  a[href*="r2rmusic.com"].slide:hover img {
    transform: scale(1.05);
    box-shadow: 0 6px 24px rgba(255, 255, 255, 0.5);
  }
  div[style*="display: flex; height: 100%; width: 100%;"] a:hover img {
    transform: scale(1.05);
    transition: transform 0.3s ease;
  }
</style>
<div class="collab-block">
  <h3 class="collab-title">與世界級 Trance 力量並肩</h3>
  <div class="collab-strip">
    <span class="collab-item">RIIR Music <em>(UK)</em></span>
  </div>
  <p class="collab-desc">長期與海外 Trance 廠牌及媒體保持合作：作品與藝人專訪入選 RIIR Music 專題報道，並受邀參與 AFTERHOURS 國際電臺活動。</p>
</div>
<style>
  a[href*="r2rmusic.com"] div:hover img {
    transform: scale(1.05);
  }
  a[href*="r2rmusic.com"] div:hover {
    border-color: rgba(255, 255, 255, 0.6);
    box-shadow: 0 8px 24px rgba(255, 255, 255, 0.3);
  }
  /* 區塊小標題固定純白，不隨全站調色變色 */
  article h2:not(.fw1) {
    background: none !important;
    -webkit-text-fill-color: #ffffff !important;
    color: #ffffff !important;
  }
  /* ===== 移動端適配（≤768px 生效，桌面排版不變） ===== */
  @media (max-width: 768px) {
    /* 頂部導航：壓縮間距、允許換行 */
    #scroll-nav { padding: 10px 20px !important; }
    #scroll-nav .flex-l { flex-wrap: wrap; row-gap: 2px; }
    #scroll-nav ul { gap: 6px !important; flex-wrap: wrap; justify-content: center; }
    #scroll-nav ul li a { font-size: 12px !important; padding: 3px 5px !important; }
    /* Hero：收緊上距、標語降字號 */
    #header-logo { margin-top: 60px !important; }
    #index-slogan { font-size: 16px !important; margin-left: 0 !important; }
    .tc-l h2.fw1 { font-size: 1rem !important; line-height: 1.5 !important; }
    /* 區塊標題與正文邊距：正文基準字號隨屏寬等比縮放（下限=小米14 現值） */
    article { padding-left: 14px !important; padding-right: 14px !important; font-size: clamp(15px, 3.85vw, 18px) !important; }
    article h2:not(.fw1) { font-size: 1.3em !important; }
    div[style*="font-size: 18px"] { font-size: clamp(15px, 3.85vw, 18px) !important; }
    .block-subtitle { font-size: clamp(16px, 4.1vw, 21px); margin-bottom: 24px; }
    .collab-title { font-size: clamp(17px, 4.4vw, 20px); }
    .contact-cta h3 { font-size: clamp(18px, 4.6vw, 22px); }
    .service-card h4 { font-size: clamp(15px, 4vw, 17px); }
    .identity-item h3 { font-size: clamp(15px, 4vw, 18px); }
    .identity-item p { font-size: clamp(12px, 3.2vw, 13px); }
    /* 段落分隔線邊距 */
    div[style*="height: 1px"][style*="margin: 40px 0"] { margin: 24px 0 !important; }
    /* 語言切換器與調色盤不擋內容 */
    #lang-switch { left: 10px; bottom: 10px; }
    #lang-switch button { padding: 4px 9px; font-size: 11px; }
    #palette-toggle { right: 10px; bottom: 10px; }
  }
</style>
<style>
  /* ===== 移動端專屬居中（僅 ≤768px 生效，桌面端零影響）===== */
  @media (max-width: 768px) {
    /* 大 logo：主題 img{display:inline-block!important} 會頂掉塊級，必須同樣 !important 才能居中 */
    #header-logo { display: block !important; margin-left: auto !important; margin-right: auto !important; }
    /* 標語：全局 p{text-align:left!important} 會搶走居中，用 ID 優先級壓回 */
    #index-slogan { text-align: center !important; }
  }
</style>
<div style="height: 1px; margin: 40px 0; background: linear-gradient(90deg, rgba(255, 255, 255, 0.8), rgba(255, 255, 255, 0.8)); border-radius: 1px; box-shadow: 0 0 10px rgba(255, 255, 255, 0.6), 0 0 20px rgba(255, 255, 255, 0.3);"></div>
<h2 id="核心服務">核心服務</h2>
<div class="service-wrap">
  <h3 class="block-subtitle">從 Demo 到發行，全鏈路支持</h3>
  <div class="service-grid">
    <div class="service-card">
      <h4>Trance 音樂工程</h4>
      <p>機能、史詩與氛圍感，解決頻域衝突、動態失衡、聲場扁平，打造具備行業一流的混音，突出 Trance 核心張力。</p>
    </div>
    <div class="service-card">
      <h4>專業母帶處理</h4>
      <p>提升響度、優化頻譜平衡、增強總線粘合度，適配各大流媒體平臺（Spotify/Beatport）。</p>
    </div>
    <div class="service-card">
      <h4>教學與發行指導</h4>
      <p>通過一對四或一對一指導助力優質 Trance 作品走向全球市場。堅持無圈子化原則，確保藝人隱私全程提供單線服務與信息保密。</p>
    </div>
  </div>
</div>
<div style="height: 1px; margin: 40px 0; background: linear-gradient(90deg, rgba(255, 255, 255, 0.8), rgba(255, 255, 255, 0.8)); border-radius: 1px; box-shadow: 0 0 10px rgba(255, 255, 255, 0.6), 0 0 20px rgba(255, 255, 255, 0.3);"></div>
<h2 id="近期作品--聲波現場">近期作品 · 聲波現場</h2>
<div class="works-wrap">
  <h3 class="block-subtitle">Listen to the Sound</h3>
  <div class="works-grid">
    <div style="width: 100%;">
      <iframe data-testid="embed-iframe" class="work-embed work-embed--spotify" src="https://open.spotify.com/embed/artist/7ok2w55yMiwbUvrlVn9mBW?utm_source=generator" frameBorder="0" allowfullscreen="" allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture" loading="lazy"></iframe>
      <p class="work-note">更多作品 → <a href="https://open.spotify.com/artist/7ok2w55yMiwbUvrlVn9mBW" target="_blank" style="color: #ffffff; text-decoration: none;">Spotify</a></p>
    </div>
    <div style="width: 100%;">
      <div class="work-163-crop">
        <iframe id="netease-player" class="work-embed work-embed--163" src="https://music.163.com/outchain/player?type=0&id=17739007625&auto=0&height=430" loading="lazy" frameborder="no" marginwidth="0" marginheight="0"></iframe>
      </div>
      <script>
      /* 網易雲外鏈播放器：移動端會被 302 到 http 造成混合內容攔截，按 UA 直取 https 移動版 */
      (function () {
        var f = document.getElementById('netease-player');
        if (f && /Mobi|Android|iPhone|iPad/i.test(navigator.userAgent)) {
          f.src = 'https://music.163.com/m/outchain/player?type=0&id=17739007625&auto=0&height=430';
        }
      })();
      </script>
      <p class="work-note">更多作品 → <a href="https://music.163.com/playlist?id=17739007625" target="_blank" style="color: #ffffff; text-decoration: none;">網易雲音樂</a></p>
    </div>
  </div>
</div>
<div style="height: 1px; margin: 40px 0; background: linear-gradient(90deg, rgba(255, 255, 255, 0.8), rgba(255, 255, 255, 0.8)); border-radius: 1px; box-shadow: 0 0 10px rgba(255, 255, 255, 0.6), 0 0 20px rgba(255, 255, 255, 0.3);"></div>
<h2 id="聯繫我--共創-trance-能量">聯繫我 · 共創 Trance 能量</h2>
<div class="contact-cta">
  <h3>混音需求 · 合作諮詢 · DJ Booking</h3>
  <p>歡迎 Trance 同好、製作人、活動方洽談合作，讓我們一起打造有力量的聲波</p>
  <a class="cta-pill" href="/contact/index.html">立即諮詢</a>
</div>
  </article>
      </main>
      <footer class="bg-black bottom-0 w-100 pa3" role="contentinfo">
  <div class="flex justify-between">
  <a class="f4 fw4 hover-white white-70 dn dib-ns pv2 ph3 no-underline" href="https://eonun-official.github.io/" >
    &copy;  Eonun 2026 
  </a>
    <div><div class="ananke-socials"></div>
</div>
  </div>
</footer>

---
title: "Eonun | Trance 声波雕刻师 | Eonun"
description: "Welcome to the world of Eonun: Trance production, style design, mastering, aesthetics and concept"
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
          letter-spacing: 0.5ch !important; /* 关键：缩窄为0.5ch（原1ch的一半） */
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
            <a class="hover-white white-90 no-underline" href="shop/index.html" title="Shop page">Shop</a>
          </li>
          <li class="list f5 f4-ns fw4 dib pr3">
            <a class="hover-white white-90 no-underline" href="music-services/index.html" title="Music Services page">Music Services</a>
          </li>
          <li class="list f5 f4-ns fw4 dib pr3">
            <a class="hover-white white-90 no-underline" href="instructions/index.html" title="Instructions page">Instructions</a>
          </li>
          <li class="list f5 f4-ns fw4 dib pr3">
            <a class="hover-white white-90 no-underline" href="about/index.html" title="About page">About</a>
          </li>
          <li class="list f5 f4-ns fw4 dib pr3">
            <a class="hover-white white-90 no-underline" href="contact/index.html" title="Contact page">Contact</a>
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
      /* 动态柔和流光效果 */
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
      /* 初始状态添加柔和发光效果 */
      #header-logo.initial {
        animation: softGlow 7.2s ease-in-out infinite;
      }
    </style>
      <div class="tc-l pv6 pv8-l ph3 ph4-ns">
        <div class="mb0 lh-title" style="max-width: 800px; margin: 0 auto; position: relative; background: transparent !important; ">
          <img id="header-logo" src="/images/eonun2www.png" alt="Eonun | Trance Sound Sculptor" fetchpriority="high" decoding="async"
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
          ">A young life, devoted to the art of Trance</p>
        </div>
        <h2 class="fw1 f5 f3-l white-80 measure-wide-l center lh-copy mt4 mb4">
          欢迎来到 Eonun 领域：Trance 制作、风格设计、母带工程、美学与概念
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
// 视频错误处理
if (headerVideo) {
  headerVideo.addEventListener('error', function() {
    console.log('视频加载失败，显示备用背景');
    if (videoFallback) {
      videoFallback.style.display = 'block';
    }
  });
  // 检查视频是否能正常播放
  headerVideo.addEventListener('loadeddata', function() {
    console.log('视频加载成功');
  });
  // 页面其它内容全部加载完后，再后台加载视频：加载到哪儿播到哪儿，互不拖累
  window.addEventListener('load', function() {
    setTimeout(function() {
      if (headerVideo && !headerVideo.getAttribute('src')) {
        headerVideo.src = headerVideo.getAttribute('data-src');
        headerVideo.load();
        var pr = headerVideo.play();
        if (pr && pr.catch) { pr.catch(function(){}); }
        // 视频开始加载后才计时：8秒还缓冲不出画面就换备用渐变背景
        setTimeout(function() {
          if (headerVideo.readyState < 2) {
            console.log('视频加载超时，显示备用背景');
            if (videoFallback) { videoFallback.style.display = 'block'; }
          }
        }, 8000);
      }
    }, 50);
  });
}
// 初始状态添加柔和发光效果
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
  // 当开始滚动时，移除初始动画类，让滚动效果接管
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
      // 回到顶部时重新添加初始动画类
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
// 加载标语文件
  /* EN/DE 版标语库待翻译，暂用静态默认句 */
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
    <!-- 无需额外标题，logo+随机标语已占顶部，直接上核心内容 -->
<h2 id="用声波定义-trance-的质感边界">Defining the Texture of Trance with Sound</h2>
<div style="max-width: 900px; margin: 40px auto; color: #ffffff; line-height: 1.8; font-size: 18px;">
  Specialized in modern Uplifting / Tech Trance production and mastering — from bedroom mixes to releases on international platforms. With <span style="font-weight: bold;">forward-thinking musical aesthetics</span> and an <span style="font-weight: bold;">exclusive, comprehensive theory system</span>, every track is crafted to international quality.
</div>
<div style="height: 2px; margin: 40px 0; background: linear-gradient(90deg, rgba(255, 255, 255, 0.8), rgba(255, 255, 255, 0.8)); border-radius: 1px; box-shadow: 0 0 10px rgba(255, 255, 255, 0.6), 0 0 20px rgba(255, 255, 255, 0.3);"></div>
<h2 id="核心身份">Core Identity</h2>
<div style="display: flex; flex-wrap: wrap; gap: 20px; justify-content: center; margin: 60px 0;">
  <div style="background: rgba(255,255,255,0.05); padding: 25px 30px; border-radius: 8px; border-left: 3px solid #f2f2f2; min-width: 200px; text-align: center;">
    <h3 style="color: #fff; margin: 0 0 10px 0; font-size: 20px;">Trance Producer</h3>
    <p style="color: #d9d9d9; margin: 0; font-size: 14px;">Focused on Uplifting / Tech Trance</p>
  </div>
  <div style="background: rgba(255,255,255,0.05); padding: 25px 30px; border-radius: 8px; border-left: 3px solid #f2f2f2; min-width: 200px; text-align: center;">
    <h3 style="color: #fff; margin: 0 0 10px 0; font-size: 20px;">Mastering Engineer</h3>
    <p style="color: #d9d9d9; margin: 0; font-size: 14px;">Professional mastering for hundreds of chart-topping Trance tracks</p>
  </div>
  <div style="background: rgba(255,255,255,0.05); padding: 25px 30px; border-radius: 8px; border-left: 3px solid #e0e0e0; min-width: 200px; text-align: center;">
    <h3 style="color: #fff; margin: 0 0 10px 0; font-size: 20px;">Label A&R</h3>
    <p style="color: #d9d9d9; margin: 0; font-size: 14px;">Co-founder of Cooperation Trance</p>
  </div>
  <div style="background: rgba(255,255,255,0.05); padding: 25px 30px; border-radius: 8px; border-left: 3px solid #f2f2f2; min-width: 200px; text-align: center;">
    <h3 style="color: #fff; margin: 0 0 10px 0; font-size: 20px;">Label A&R</h3>
    <p style="color: #d9d9d9; margin: 0; font-size: 14px;">Team planning at Polar Impact</p>
  </div>
</div>
<div style="height: 1px; margin: 40px 0; background: linear-gradient(90deg, rgba(255, 255, 255, 0.8), rgba(255, 255, 255, 0.8)); border-radius: 1px; box-shadow: 0 0 10px rgba(255, 255, 255, 0.6), 0 0 20px rgba(255, 255, 255, 0.3);"></div>
<h2 id="国内外认可--合作背书">Recognition · Partnerships</h2>
<div style="max-width: 1200px; margin: 60px auto;">
  <div style="display: flex; gap: 40px; justify-content: center; align-items: stretch; flex-wrap: wrap;">
    <div style="flex: 1; min-width: 300px; max-width: 300px;">
      <h3 style="color: #fff; font-size: 18px; text-align: center; margin-bottom: 20px;">Exclusive Feature</h3>
      <div style="position: relative; width: 100%; height: 300px; overflow: hidden; border-radius: 12px; background: rgba(255,255,255,0.02); border: 1px solid rgba(255, 255, 255, 0.2);">
        <div id="slider" style="position: relative; width: 100%; height: 100%;">
          <a href="https://www.r2rmusic.com/post/artist-feature-eonun" target="_blank" class="slide" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; text-decoration: none; display: flex; align-items: center; justify-content: center; opacity: 0; transition: opacity 0.5s ease-in-out;">
            <img src="/images/1.webp" loading="lazy" decoding="async" alt="Exclusive feature 1" style="width: auto; height: auto; max-width: 100%; max-height: 100%; object-fit: contain; display: block;">
          </a>
          <a href="https://www.r2rmusic.com/post/artist-feature-eonun" target="_blank" class="slide" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; text-decoration: none; display: flex; align-items: center; justify-content: center; opacity: 0; transition: opacity 0.5s ease-in-out;">
            <img src="/images/2.webp" loading="lazy" decoding="async" alt="Exclusive feature 2" style="width: auto; height: auto; max-width: 100%; max-height: 100%; object-fit: contain; display: block;">
          </a>
          <a href="https://www.r2rmusic.com/post/artist-feature-eonun" target="_blank" class="slide" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; text-decoration: none; display: flex; align-items: center; justify-content: center; opacity: 0; transition: opacity 0.5s ease-in-out;">
            <img src="/images/3.webp" loading="lazy" decoding="async" alt="Exclusive feature 3" style="width: auto; height: auto; max-width: 100%; max-height: 100%; object-fit: contain; display: block;">
          </a>
          <a href="https://www.r2rmusic.com/post/artist-feature-eonun" target="_blank" class="slide" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; text-decoration: none; display: flex; align-items: center; justify-content: center; opacity: 0; transition: opacity 0.5s ease-in-out;">
            <img src="/images/4.webp" loading="lazy" decoding="async" alt="Exclusive feature 4" style="width: auto; height: auto; max-width: 100%; max-height: 100%; object-fit: contain; display: block;">
          </a>
        </div>
      </div>
    </div>
    <div style="flex: 1.5; min-width: 450px; max-width: 600px;">
      <h3 style="color: #fff; font-size: 18px; text-align: center; margin-bottom: 20px;">AFTERHOURS International Radio Takeover</h3>
      <div style="width: 100%; height: 300px; overflow: hidden; border-radius: 12px; background: rgba(255,255,255,0.02); border: 1px solid rgba(255, 255, 255, 0.2);">
        <div style="display: flex; height: 100%; gap: 0; margin: 0; padding: 0; align-items: stretch;">
          <img src="/images/Takeover1.webp" loading="lazy" decoding="async" alt="Takeover 1" style="height: 100%; object-fit: cover; display: block; margin: 0; padding: 0; border: none; flex-shrink: 0; transition: transform 0.3s ease;">
          <img src="/images/Takeover2.webp" loading="lazy" decoding="async" alt="Takeover 2" style="height: 100%; object-fit: cover; display: block; margin: 0; padding: 0; border: none; flex-shrink: 0; transition: transform 0.3s ease;">
          <img src="/images/Takeover3.webp" loading="lazy" decoding="async" alt="Takeover 3" style="height: 100%; object-fit: cover; display: block; margin: 0; padding: 0; border: none; flex-shrink: 0; transition: transform 0.3s ease;">
          <img src="/images/Takeover4.webp" loading="lazy" decoding="async" alt="Takeover 4" style="height: 100%; object-fit: cover; display: block; margin: 0; padding: 0; border: none; flex-shrink: 0; transition: transform 0.3s ease;">
        </div>
      </div>
    </div>
  </div>
</div>
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
<div style="max-width: 900px; margin: 60px auto; text-align: center;">
  <h3 style="color: #fff; font-size: 22px; margin-bottom: 30px;">Alongside World-Class Trance Forces</h3>
  <div style="display: flex; flex-wrap: wrap; gap: 25px; justify-content: center; align-items: center;">
    <span style="color: #d9d9d9; font-size: 16px;">Darren Porter (UK)</span>
    <span style="color: #d9d9d9;">•</span>
    <span style="color: #d9d9d9; font-size: 16px;">Pinkque (AU)</span>
    <span style="color: #d9d9d9;">•</span>
    <span style="color: #d9d9d9; font-size: 16px;">RIIR Music (UK)</span>
  </div>
  <p style="color: #d9d9d9; margin-top: 20px; font-size: 14px; line-height: 1.6;">Tracks and artist interviews have been featured in label spotlights — the first Chinese Trance producer to win over an international label through sheer craft and earn an exclusive feature.<br><br>Also the first Chinese artist invited by the label to take part on that international radio station</p>
</div>
<style>
  a[href*="r2rmusic.com"] div:hover img {
    transform: scale(1.05);
  }
  a[href*="r2rmusic.com"] div:hover {
    border-color: rgba(255, 255, 255, 0.6);
    box-shadow: 0 8px 24px rgba(255, 255, 255, 0.3);
  }
  /* 区块小标题固定纯白，不随全站调色变色 */
  article h2:not(.fw1) {
    background: none !important;
    -webkit-text-fill-color: #ffffff !important;
    color: #ffffff !important;
  }
</style>
<div style="height: 1px; margin: 40px 0; background: linear-gradient(90deg, rgba(255, 255, 255, 0.8), rgba(255, 255, 255, 0.8)); border-radius: 1px; box-shadow: 0 0 10px rgba(255, 255, 255, 0.6), 0 0 20px rgba(255, 255, 255, 0.3);"></div>
<h2 id="核心服务">Core Services</h2>
<div style="max-width: 900px; margin: 60px auto;">
  <h3 style="color: #fff; font-size: 22px; text-align: center; margin-bottom: 40px;">Full-Cycle Support, from Demo to Release</h3>
  <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 25px;">
    <div style="background: linear-gradient(135deg, rgba(255, 255, 255, 0.1), rgba(255, 255, 255, 0.1)); padding: 30px; border-radius: 8px; border: 1px solid rgba(255, 255, 255, 0.2);">
      <h4 style="color: #fff; margin: 0 0 15px 0; font-size: 18px;">Trance Music Production</h4>
      <p style="color: #d9d9d9; margin: 0; font-size: 14px; line-height: 1.6;">Driving, epic and atmospheric — resolving frequency conflicts, dynamic imbalance and flat soundstages to craft an industry-leading mix that brings out the core tension of Trance.</p>
    </div>
    <div style="background: linear-gradient(135deg, rgba(255, 255, 255, 0.1), rgba(255, 255, 255, 0.1)); padding: 30px; border-radius: 8px; border: 1px solid rgba(255, 255, 255, 0.2);">
      <h4 style="color: #fff; margin: 0 0 15px 0; font-size: 18px;">Professional Mastering</h4>
      <p style="color: #d9d9d9; margin: 0; font-size: 14px; line-height: 1.6;">Louder, spectrally balanced and bus-glued masters, tuned for major streaming platforms (Spotify/Beatport).</p>
    </div>
    <div style="background: linear-gradient(135deg, rgba(255, 255, 255, 0.1), rgba(255, 255, 255, 0.1)); padding: 30px; border-radius: 8px; border: 1px solid rgba(255, 255, 255, 0.2);">
      <h4 style="color: #fff; margin: 0 0 15px 0; font-size: 18px;">Coaching & Release Guidance</h4>
      <p style="color: #d9d9d9; margin: 0; font-size: 14px; line-height: 1.6;">Through small-group (up to 4) or one-on-one coaching, quality Trance works reach the global market. Strictly non-clique, with full artist privacy: single-point service and confidentiality throughout.</p>
    </div>
  </div>
</div>
<div style="height: 1px; margin: 40px 0; background: linear-gradient(90deg, rgba(255, 255, 255, 0.8), rgba(255, 255, 255, 0.8)); border-radius: 1px; box-shadow: 0 0 10px rgba(255, 255, 255, 0.6), 0 0 20px rgba(255, 255, 255, 0.3);"></div>
<h2 id="近期作品--声波现场">Recent Works · Sonic Live</h2>
<div style="max-width: 1200px; margin: 60px auto;">
  <h3 style="color: #fff; font-size: 22px; text-align: center; margin-bottom: 40px;">Listen to the Sound</h3>
  <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(350px, 1fr)); gap: 30px; justify-items: center;">
    <div style="width: 100%;">
      <iframe data-testid="embed-iframe" style="border-radius:12px" src="https://open.spotify.com/embed/artist/7ok2w55yMiwbUvrlVn9mBW?utm_source=generator" width="100%" height="352" frameBorder="0" allowfullscreen="" allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture" loading="lazy"></iframe>
      <p style="color: #d9d9d9; text-align: center; margin-top: 15px; font-size: 14px;">More works on <a href="https://open.spotify.com/artist/7ok2w55yMiwbUvrlVn9mBW" target="_blank" style="color: #ffffff; text-decoration: none;">Spotify</a></p>
    </div>
    <div style="width: 100%;">
      <iframe src="https://music.163.com/outchain/player?type=0&id=17739007625&auto=0&height=430" loading="lazy" width="100%" height="352" frameborder="no" marginwidth="0" marginheight="0" style="border-radius:12px"></iframe>
      <p style="color: #d9d9d9; text-align: center; margin-top: 15px; font-size: 14px;">更多作品 → <a href="https://music.163.com/playlist?id=17739007625" target="_blank" style="color: #ffffff; text-decoration: none;">网易云音乐</a></p>
    </div>
  </div>
</div>
<div style="height: 1px; margin: 40px 0; background: linear-gradient(90deg, rgba(255, 255, 255, 0.8), rgba(255, 255, 255, 0.8)); border-radius: 1px; box-shadow: 0 0 10px rgba(255, 255, 255, 0.6), 0 0 20px rgba(255, 255, 255, 0.3);"></div>
<h2 id="联系我--共创-trance-能量">Contact · Creating Trance Energy Together</h2>
<div style="max-width: 600px; margin: 60px auto; background: rgba(255,255,255,0.03); padding: 40px; border-radius: 8px; text-align: center;">
  <h3 style="color: #fff; font-size: 22px; margin: 0 0 20px 0;">Mixing · Collaboration · DJ Booking</h3>
  <p style="color: #d9d9d9; margin: 0 0 30px 0; font-size: 14px;">Trance fans, producers and event organizers are welcome — let's create powerful sound waves together</p>
  <a href="contact/index.html" style="background: #f2f2f2; color: #0a0a0a; padding: 12px 30px; border-radius: 50px; text-decoration: none; font-weight: bold; font-size: 16px; display: inline-block;">
    Get in Touch
  </a>
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

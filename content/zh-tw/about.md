---
title: "Eonun"
body_class: "ma0 avenir bg-near-white development is-section is-section page-about"
---
<header class="about-header" style="position:relative; overflow:hidden; background-image: url('/images/MyBio.webp'); background-size: cover; background-position: center center; background-repeat:no-repeat; min-height:520px;">
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
        <ul class="pl0 mr3" 
            style="display: flex !important; list-style: none !important; margin: 0 !important; padding: 0 !important; gap: 20px !important;">
          <li class="list f5 f4-ns fw4 dib pr3">
            <a class="hover-white white-90 no-underline" href="../shop/index.html" title="Shop page">Shop</a>
          </li>
          <li class="list f5 f4-ns fw4 dib pr3">
            <a class="hover-white white-90 no-underline" href="../music-services/index.html" title="Music Services page">Music Services</a>
          </li>
          <li class="list f5 f4-ns fw4 dib pr3">
            <a class="hover-white white-90 no-underline" href="../instructions/index.html" title="Instructions page">Instructions</a>
          </li>
          <li class="list f5 f4-ns fw4 dib pr3">
            <a class="hover-white white-90 no-underline" href="index.html" title="About page" style="color: #ffffff !important; text-shadow: 0 0 8px rgba(255, 255, 255, 0.6) !important;">About</a>
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
const headerLogo = document.getElementById('header-logo');
const scrollNav = document.getElementById('scroll-nav');
const indexSlogan = document.getElementById('index-slogan');
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
  const fastDecay = scrollDistance / 200;
  const slowDecay = scrollDistance / 300;
  const brightness = Math.max(0.3, 1 - fastDecay);
  const opacity = Math.max(0.0, 1 - slowDecay);
  const shadowIntensity = Math.max(0., 0.3 - (0.3 * fastDecay));
  const parallaxOffset = scrollDistance * 0.6; 
  const maxOffset = 250; 
  const finalOffset = Math.min(parallaxOffset, maxOffset);
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
  .page-5-about img[src$="MyBio.webp"],
  body.page-5-about img[src$="MyBio.webp"] {
    display: none !important;
  }
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
    <div class="about-container" style="max-width: 1000px; margin: 0 auto; padding: 60px 20px; text-align: center;">
      <h1 class="f3 fw1 athelas mt0 lh-title">
          關於我
      </h1>
      <div class="f6 f5-l lh-copy nested-copy-line-height nested-links">
        <!-- 個人形象區域 -->
        <div style="margin-bottom: 3rem;">
        </div>
        <!-- 核心身份區域 -->
        <section style="margin-bottom: 4rem;">
          <div style="background: rgba(255, 255, 255, 0.15); backdrop-filter: blur(12px); -webkit-backdrop-filter: blur(12px); border: 1px solid rgba(255, 255, 255, 0.18); border-radius: 12px; padding: 2.5rem; box-shadow: 0 4px 30px rgba(255, 255, 255, 0.3);">
            <h2 style="font-size: 1.8rem; font-weight: 700; margin-bottom: 1.5rem; color: #ffffff; display: flex; align-items: center; justify-content: center;">
              <span style="width: 4px; height: 24px; background: #ffffff; margin-right: 12px; border-radius: 2px;"></span>
              核心身份
            </h2>
            <div style="font-size: 1.15rem; line-height: 1.8; color: #ffffff;">
              <p style="margin-bottom: 1.5rem; font-weight: 600; color: #ffffff;">泛電子音樂製作人 | Trance藝術家 | 舞曲數字母帶工程師 | Cooperation Trance廠牌創始策劃兼A&amp;R | Polar Impact 策劃</p>
              <p style="margin-bottom: 0;">前Hertz Records（中國）A&amp;R核心成員，曾以藝名“unfairmesseater”活躍於2088 Records、Hertz Records等國內頂尖電子音樂廠牌。</p>
            </div>
          </div>
        </section>
        <!-- 職業履歷區域 -->
        <section style="margin-bottom: 4rem;">
          <h2 style="font-size: 1.8rem; font-weight: 700; margin-bottom: 2rem; color: #ffffff; display: flex; align-items: center; justify-content: center;">
            <span style="width: 4px; height: 24px; background: #ffffff; margin-right: 12px; border-radius: 2px;"></span>
            職業履歷
          </h2>
          <!-- 2019年 -->
          <div style="margin-bottom: 2.5rem; position: relative; padding-left: 3rem; max-width: 800px; margin-left: auto; margin-right: auto;">
            <div style="position: absolute; left: 1rem; top: 2rem; width: 1px; height: calc(100% + 1rem); background: rgba(255, 255, 255, 0.5); transform: translateX(-50%);"></div>
            <div style="position: absolute; left: 0; top: 0; width: 2rem; height: 2rem; background: rgba(255, 255, 255, 0.9); border-radius: 50%; display: flex; align-items: center; justify-content: center; color: #f2f2f2; font-weight: 600; font-size: 0.9rem; box-shadow: 0 0 10px rgba(255, 255, 255, 0.5);">19</div>
            <h3 style="font-size: 1.3rem; font-weight: 600; margin-bottom: 1rem; color: #ffffff;">2019年：行業初露鋒芒</h3>
            <p style="font-size: 1.05rem; line-height: 1.7; color: #ffffff; padding: 1.5rem;">
              2019年起，深度參與N2V旗下2088 Records廠牌兩屆年度音樂合集的創作與發行工作，完成行業初期積累後，暫別電子音樂行業數年。
            </p>
          </div>
          <!-- 2022年 -->
          <div style="margin-bottom: 2.5rem; position: relative; padding-left: 3rem; max-width: 800px; margin-left: auto; margin-right: auto;">
            <div style="position: absolute; left: 0; top: 0; width: 2rem; height: 2rem; background: rgba(255, 255, 255, 0.9); border-radius: 50%; display: flex; align-items: center; justify-content: center; color: #f2f2f2; font-weight: 600; font-size: 0.9rem; box-shadow: 0 0 10px rgba(255, 255, 255, 0.5);">22</div>
            <div style="position: absolute; left: 1rem; top: 2rem; width: 1px; height: calc(100% + 1rem); background: rgba(255, 255, 255, 0.5); transform: translateX(-50%);"></div>
            <h3 style="font-size: 1.3rem; font-weight: 600; margin-bottom: 1rem; color: #ffffff;">2022年：廠牌創立與行業深耕</h3>
            <p style="font-size: 1.05rem; line-height: 1.7; color: #ffffff; padding: 1.5rem; margin-bottom: 1.5rem;">
              與國內知名Trance製作人DJ CO1N聯合創立<strong style="color: #ffffff;">中國首個獨立商業舞曲廠牌Cooperation Trance</strong>，並長期主導廠牌作品審覈與母帶製作核心工作：
            </p>
            <div style="font-size: 1.05rem; line-height: 1.7; color: #ffffff; padding: 1.5rem 1.5rem 1.5rem 3rem; text-align: left; max-width: 700px; margin-left: auto; margin-right: auto;">
              <p style="margin-bottom: 0.8rem; position: relative; padding-left: 1.5rem;">
                <span style="position: absolute; left: 0; top: 0.6rem; width: 8px; height: 8px; background: #ffffff; border-radius: 50%; box-shadow: 0 0 8px rgba(255, 255, 255, 0.8);"></span>
                累計完成數百首優質電子音樂作品的專業評審
              </p>
              <p style="position: relative; padding-left: 1.5rem;">
                <span style="position: absolute; left: 0; top: 0.6rem; width: 8px; height: 8px; background: #ffffff; border-radius: 50%; box-shadow: 0 0 8px rgba(255, 255, 255, 0.8);"></span>
                助力超過百軌曲目與幾十張EP與專輯的母帶處理，其上架均榮登Beatport的各類發行榜單
              </p>
            </div>
          </div>
          <!-- 2025年 -->
          <div style="margin-bottom: 2.5rem; position: relative; padding-left: 3rem; max-width: 800px; margin-left: auto; margin-right: auto;">
            <div style="position: absolute; left: 0; top: 0; width: 2rem; height: 2rem; background: rgba(255, 255, 255, 0.9); border-radius: 50%; display: flex; align-items: center; justify-content: center; color: #f2f2f2; font-weight: 600; font-size: 0.9rem; box-shadow: 0 0 10px rgba(255, 255, 255, 0.5);">25</div>
            <div style="position: absolute; left: 1rem; top: 2rem; width: 1px; height: calc(100% + 1rem); background: rgba(255, 255, 255, 0.5); transform: translateX(-50%);"></div>
            <h3 style="font-size: 1.3rem; font-weight: 600; margin-bottom: 1rem; color: #ffffff;">2025年：國際合作與專業認可</h3>
            <p style="font-size: 1.05rem; line-height: 1.7; color: #ffffff; padding: 1.5rem; margin-bottom: 1.5rem;">
              開始以獨立身份發展自己，與世界級Trance藝術家Darren Porter旗下Reason II Rise（RIIR Music）音樂團隊達成系列發行合作，合作成果獲得多國頂尖Trance藝人的高度認可與支持：
            </p>
            <div style="font-size: 1.05rem; line-height: 1.7; color: #ffffff; padding: 1.5rem 1.5rem 1.5rem 3rem; text-align: left; max-width: 700px; margin-left: auto; margin-right: auto;">
              <p style="margin-bottom: 0.8rem; position: relative; padding-left: 1.5rem;">
                <span style="position: absolute; left: 0; top: 0.6rem; width: 8px; height: 8px; background: #ffffff; border-radius: 50%; box-shadow: 0 0 8px rgba(255, 255, 255, 0.8);"></span>
                英國知名Trance音樂人 Darren Porter
              </p>
              <p style="margin-bottom: 0.8rem; position: relative; padding-left: 1.5rem;">
                <span style="position: absolute; left: 0; top: 0.6rem; width: 8px; height: 8px; background: #ffffff; border-radius: 50%; box-shadow: 0 0 8px rgba(255, 255, 255, 0.8);"></span>
                澳洲電子音樂藝術家 Pinkque
              </p>
              <p style="margin-bottom: 0.8rem; position: relative; padding-left: 1.5rem;">
                <span style="position: absolute; left: 0; top: 0.6rem; width: 8px; height: 8px; background: #ffffff; border-radius: 50%; box-shadow: 0 0 8px rgba(255, 255, 255, 0.8);"></span>
                Armada Music廠牌旗下烏克蘭製作人 Geographer
              </p>
              <p style="position: relative; padding-left: 1.5rem;">
                <span style="position: absolute; left: 0; top: 0.6rem; width: 8px; height: 8px; background: #ffffff; border-radius: 50%; box-shadow: 0 0 8px rgba(255, 255, 255, 0.8);"></span>
                日本Trance領域代表藝人 N-sking
              </p>
            </div>
            <p style="font-size: 1.05rem; line-height: 1.7; color: #ffffff; padding: 1.5rem;">
              同期，個人專屬海外英文專題報道正式發佈於RIIR Music News專欄，成爲少數獲得該平臺專題報道的中國Trance藝術家。
            </p>
          </div>
          <!-- 2026年初 -->
          <div style="margin-bottom: 2.5rem; position: relative; padding-left: 3rem; max-width: 800px; margin-left: auto; margin-right: auto;">
            <div style="position: absolute; left: 0; top: 0; width: 2rem; height: 2rem; background: rgba(255, 255, 255, 0.9); border-radius: 50%; display: flex; align-items: center; justify-content: center; color: #f2f2f2; font-weight: 600; font-size: 0.9rem; box-shadow: 0 0 10px rgba(255, 255, 255, 0.5);">26</div>
            <h3 style="font-size: 1.3rem; font-weight: 600; margin-bottom: 1rem; color: #ffffff;">2026年初：新使命與新徵程</h3>
            <p style="font-size: 1.05rem; line-height: 1.7; color: #ffffff; padding: 1.5rem;">
              應邀擔任Polar Impact廠牌的A&R與策劃，爲中國的Trance發展繼續做出貢獻。
            </p>
          </div>
        </section>
        <!-- 相關報道區域 -->
        <section style="margin-bottom: 3rem;">
          <div style="background: rgba(255, 255, 255, 0.15); backdrop-filter: blur(12px); -webkit-backdrop-filter: blur(12px); border: 1px solid rgba(255, 255, 255, 0.18); border-radius: 12px; padding: 2.5rem; box-shadow: 0 4px 30px rgba(255, 255, 255, 0.3);">
            <h2 style="font-size: 1.8rem; font-weight: 700; margin-bottom: 1.5rem; color: #ffffff; display: flex; align-items: center; justify-content: center;">
              <span style="width: 4px; height: 24px; background: #ffffff; margin-right: 12px; border-radius: 2px;"></span>
              相關報道
            </h2>
            <div style="text-align: center;">
              <a href="https://www.r2rmusic.com/post/artist-feature-eonun"
                 style="display: inline-block; font-size: 1.15rem; font-weight: 600; color: #ffffff; text-decoration: none; padding: 1rem 2rem; border: 2px solid rgba(255, 255, 255, 0.8); border-radius: 8px; transition: all 0.3s ease; background: rgba(255, 255, 255, 0.1); backdrop-filter: blur(8px); -webkit-backdrop-filter: blur(8px);">
                Eonun Artist Feature | RIIR Music 海外專題報道
              </a>
            </div>
          </div>
        </section>
      </div>
    </div>
  </main>
  <style>
    .about-container {
      min-height: 60vh;
      color: #fff !important;
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

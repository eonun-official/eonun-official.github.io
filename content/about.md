---
title: "Eonun"
body_class: "ma0 avenir bg-near-white development is-section is-section page-about"
---
<header class="about-header" style="position:relative; overflow:hidden; background-image: url('../images/MyBio.webp'); background-size: cover; background-position: center center; background-repeat:no-repeat; min-height:520px;">
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
          ">一个年轻人奉献给了Trance艺术的部分人生</p>
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
    <div class="about-container" style="max-width: 1000px; margin: 0 auto; padding: 60px 20px; text-align: center;">
      <h1 class="f3 fw1 athelas mt0 lh-title">
          关于我
      </h1>
      <div class="f6 f5-l lh-copy nested-copy-line-height nested-links">
        <!-- 个人形象区域 -->
        <div style="margin-bottom: 3rem;">
        </div>
        <!-- 核心身份区域 -->
        <section style="margin-bottom: 4rem;">
          <div style="background: rgba(255, 255, 255, 0.15); backdrop-filter: blur(12px); -webkit-backdrop-filter: blur(12px); border: 1px solid rgba(255, 255, 255, 0.18); border-radius: 12px; padding: 2.5rem; box-shadow: 0 4px 30px rgba(255, 255, 255, 0.3);">
            <h2 style="font-size: 1.8rem; font-weight: 700; margin-bottom: 1.5rem; color: #ffffff; display: flex; align-items: center; justify-content: center;">
              <span style="width: 4px; height: 24px; background: #ffffff; margin-right: 12px; border-radius: 2px;"></span>
              核心身份
            </h2>
            <div style="font-size: 1.15rem; line-height: 1.8; color: #ffffff;">
              <p style="margin-bottom: 1.5rem; font-weight: 600; color: #ffffff;">泛电子音乐制作人 | Trance艺术家 | 舞曲数字母带工程师 | Cooperation Trance厂牌创始策划兼A&amp;R | Polar Impact 策划</p>
              <p style="margin-bottom: 0;">前Hertz Records（中国）A&amp;R核心成员，曾以艺名“unfairmesseater”活跃于2088 Records、Hertz Records等国内顶尖电子音乐厂牌。</p>
            </div>
          </div>
        </section>
        <!-- 职业履历区域 -->
        <section style="margin-bottom: 4rem;">
          <h2 style="font-size: 1.8rem; font-weight: 700; margin-bottom: 2rem; color: #ffffff; display: flex; align-items: center; justify-content: center;">
            <span style="width: 4px; height: 24px; background: #ffffff; margin-right: 12px; border-radius: 2px;"></span>
            职业履历
          </h2>
          <!-- 2019年 -->
          <div style="margin-bottom: 2.5rem; position: relative; padding-left: 3rem; max-width: 800px; margin-left: auto; margin-right: auto;">
            <div style="position: absolute; left: 1rem; top: 2rem; width: 1px; height: calc(100% + 1rem); background: rgba(255, 255, 255, 0.5); transform: translateX(-50%);"></div>
            <div style="position: absolute; left: 0; top: 0; width: 2rem; height: 2rem; background: rgba(255, 255, 255, 0.9); border-radius: 50%; display: flex; align-items: center; justify-content: center; color: #f2f2f2; font-weight: 600; font-size: 0.9rem; box-shadow: 0 0 10px rgba(255, 255, 255, 0.5);">19</div>
            <h3 style="font-size: 1.3rem; font-weight: 600; margin-bottom: 1rem; color: #ffffff;">2019年：行业初露锋芒</h3>
            <p style="font-size: 1.05rem; line-height: 1.7; color: #ffffff; padding: 1.5rem;">
              2019年起，深度参与N2V旗下2088 Records厂牌两届年度音乐合集的创作与发行工作，完成行业初期积累后，暂别电子音乐行业数年。
            </p>
          </div>
          <!-- 2022年 -->
          <div style="margin-bottom: 2.5rem; position: relative; padding-left: 3rem; max-width: 800px; margin-left: auto; margin-right: auto;">
            <div style="position: absolute; left: 0; top: 0; width: 2rem; height: 2rem; background: rgba(255, 255, 255, 0.9); border-radius: 50%; display: flex; align-items: center; justify-content: center; color: #f2f2f2; font-weight: 600; font-size: 0.9rem; box-shadow: 0 0 10px rgba(255, 255, 255, 0.5);">22</div>
            <div style="position: absolute; left: 1rem; top: 2rem; width: 1px; height: calc(100% + 1rem); background: rgba(255, 255, 255, 0.5); transform: translateX(-50%);"></div>
            <h3 style="font-size: 1.3rem; font-weight: 600; margin-bottom: 1rem; color: #ffffff;">2022年：厂牌创立与行业深耕</h3>
            <p style="font-size: 1.05rem; line-height: 1.7; color: #ffffff; padding: 1.5rem; margin-bottom: 1.5rem;">
              与国内知名Trance制作人DJ CO1N联合创立<strong style="color: #ffffff;">中国首个独立商业舞曲厂牌Cooperation Trance</strong>，并长期主导厂牌作品审核与母带制作核心工作：
            </p>
            <div style="font-size: 1.05rem; line-height: 1.7; color: #ffffff; padding: 1.5rem 1.5rem 1.5rem 3rem; text-align: left; max-width: 700px; margin-left: auto; margin-right: auto;">
              <p style="margin-bottom: 0.8rem; position: relative; padding-left: 1.5rem;">
                <span style="position: absolute; left: 0; top: 0.6rem; width: 8px; height: 8px; background: #ffffff; border-radius: 50%; box-shadow: 0 0 8px rgba(255, 255, 255, 0.8);"></span>
                累计完成数百首优质电子音乐作品的专业评审
              </p>
              <p style="position: relative; padding-left: 1.5rem;">
                <span style="position: absolute; left: 0; top: 0.6rem; width: 8px; height: 8px; background: #ffffff; border-radius: 50%; box-shadow: 0 0 8px rgba(255, 255, 255, 0.8);"></span>
                助力超过百轨曲目与几十张EP与专辑的母带处理，其上架均荣登Beatport的各类发行榜单
              </p>
            </div>
          </div>
          <!-- 2025年 -->
          <div style="margin-bottom: 2.5rem; position: relative; padding-left: 3rem; max-width: 800px; margin-left: auto; margin-right: auto;">
            <div style="position: absolute; left: 0; top: 0; width: 2rem; height: 2rem; background: rgba(255, 255, 255, 0.9); border-radius: 50%; display: flex; align-items: center; justify-content: center; color: #f2f2f2; font-weight: 600; font-size: 0.9rem; box-shadow: 0 0 10px rgba(255, 255, 255, 0.5);">25</div>
            <div style="position: absolute; left: 1rem; top: 2rem; width: 1px; height: calc(100% + 1rem); background: rgba(255, 255, 255, 0.5); transform: translateX(-50%);"></div>
            <h3 style="font-size: 1.3rem; font-weight: 600; margin-bottom: 1rem; color: #ffffff;">2025年：国际合作与专业认可</h3>
            <p style="font-size: 1.05rem; line-height: 1.7; color: #ffffff; padding: 1.5rem; margin-bottom: 1.5rem;">
              开始以独立身份发展自己，与世界级Trance艺术家Darren Porter旗下Reason II Rise（RIIR Music）音乐团队达成系列发行合作，合作成果获得多国顶尖Trance艺人的高度认可与支持：
            </p>
            <div style="font-size: 1.05rem; line-height: 1.7; color: #ffffff; padding: 1.5rem 1.5rem 1.5rem 3rem; text-align: left; max-width: 700px; margin-left: auto; margin-right: auto;">
              <p style="margin-bottom: 0.8rem; position: relative; padding-left: 1.5rem;">
                <span style="position: absolute; left: 0; top: 0.6rem; width: 8px; height: 8px; background: #ffffff; border-radius: 50%; box-shadow: 0 0 8px rgba(255, 255, 255, 0.8);"></span>
                英国知名Trance音乐人 Darren Porter
              </p>
              <p style="margin-bottom: 0.8rem; position: relative; padding-left: 1.5rem;">
                <span style="position: absolute; left: 0; top: 0.6rem; width: 8px; height: 8px; background: #ffffff; border-radius: 50%; box-shadow: 0 0 8px rgba(255, 255, 255, 0.8);"></span>
                澳洲电子音乐艺术家 Pinkque
              </p>
              <p style="margin-bottom: 0.8rem; position: relative; padding-left: 1.5rem;">
                <span style="position: absolute; left: 0; top: 0.6rem; width: 8px; height: 8px; background: #ffffff; border-radius: 50%; box-shadow: 0 0 8px rgba(255, 255, 255, 0.8);"></span>
                Armada Music厂牌旗下乌克兰制作人 Geographer
              </p>
              <p style="position: relative; padding-left: 1.5rem;">
                <span style="position: absolute; left: 0; top: 0.6rem; width: 8px; height: 8px; background: #ffffff; border-radius: 50%; box-shadow: 0 0 8px rgba(255, 255, 255, 0.8);"></span>
                日本Trance领域代表艺人 N-sking
              </p>
            </div>
            <p style="font-size: 1.05rem; line-height: 1.7; color: #ffffff; padding: 1.5rem;">
              同期，个人专属海外英文专题报道正式发布于RIIR Music News专栏，成为少数获得该平台专题报道的中国Trance艺术家。
            </p>
          </div>
          <!-- 2026年初 -->
          <div style="margin-bottom: 2.5rem; position: relative; padding-left: 3rem; max-width: 800px; margin-left: auto; margin-right: auto;">
            <div style="position: absolute; left: 0; top: 0; width: 2rem; height: 2rem; background: rgba(255, 255, 255, 0.9); border-radius: 50%; display: flex; align-items: center; justify-content: center; color: #f2f2f2; font-weight: 600; font-size: 0.9rem; box-shadow: 0 0 10px rgba(255, 255, 255, 0.5);">26</div>
            <h3 style="font-size: 1.3rem; font-weight: 600; margin-bottom: 1rem; color: #ffffff;">2026年初：新使命与新征程</h3>
            <p style="font-size: 1.05rem; line-height: 1.7; color: #ffffff; padding: 1.5rem;">
              应邀担任Polar Impact厂牌的A&R与策划，为中国的Trance发展继续做出贡献。
            </p>
          </div>
        </section>
        <!-- 相关报道区域 -->
        <section style="margin-bottom: 3rem;">
          <div style="background: rgba(255, 255, 255, 0.15); backdrop-filter: blur(12px); -webkit-backdrop-filter: blur(12px); border: 1px solid rgba(255, 255, 255, 0.18); border-radius: 12px; padding: 2.5rem; box-shadow: 0 4px 30px rgba(255, 255, 255, 0.3);">
            <h2 style="font-size: 1.8rem; font-weight: 700; margin-bottom: 1.5rem; color: #ffffff; display: flex; align-items: center; justify-content: center;">
              <span style="width: 4px; height: 24px; background: #ffffff; margin-right: 12px; border-radius: 2px;"></span>
              相关报道
            </h2>
            <div style="text-align: center;">
              <a href="https://www.r2rmusic.com/post/artist-feature-eonun"
                 style="display: inline-block; font-size: 1.15rem; font-weight: 600; color: #ffffff; text-decoration: none; padding: 1rem 2rem; border: 2px solid rgba(255, 255, 255, 0.8); border-radius: 8px; transition: all 0.3s ease; background: rgba(255, 255, 255, 0.1); backdrop-filter: blur(8px); -webkit-backdrop-filter: blur(8px);">
                Eonun Artist Feature | RIIR Music 海外专题报道
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

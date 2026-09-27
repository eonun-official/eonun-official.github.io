---
title: "Eonun"
description: "Professionelle Dienstleistungen rund um Musikproduktion, Mixing und Mastering"
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
          ">Ein Stück eines jungen Lebens, der Kunst des Trance gewidmet</p>
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
    if (!response.ok) throw new Error('Slogan-Datei konnte nicht geladen werden');
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
    console.log('Slogans konnten nicht geladen werden, Fallback-Text wird verwendet:', error);
    if (indexSlogan) indexSlogan.textContent = 'Ein Stück eines jungen Lebens, der Kunst des Trance gewidmet';
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
          <p>Professionelle Musikproduktions-Services</p>
          <p>Mastering · Musikproduktion · Kommerzielle Zusammenarbeit</p>
        </div>
      </div>
    </div>
    <div class="shop-container">
      <div class="shop-grid">
        <!-- 母带服务 -->
        <div class="product-card featured-card" onmouseenter="cardTint('#8d67fe')" onmouseleave="cardTintOut()">
          <div class="product-badge premium">Option 1</div>
          <div class="product-image master-image"></div>
          <div class="product-content">
            <div class="product-content-top">
              <h3>Mastering-Service</h3>
              <div class="product-description">Professionelles Mastering, das Ihre Musik auf kommerzielles Niveau hebt — bei unversehrter Musikalität</div>
              <div class="service-levels">
                <div class="service-level">
                  <div class="level-name">Standard-Mastering</div>
                  <div class="level-price">45 €/Track</div>
                  <div class="level-desc">Label-Standard, für fertige Mixe</div>
                </div>
                <div class="service-level premium-level">
                  <div class="level-name">Premium-Mastering</div>
                  <div class="level-price">135 €/Track</div>
                  <div class="level-desc">Stem-Mixing + Mastering, professionelle Methodik</div>
                </div>
              </div>
              <div class="service-notice">
                <div class="notice-icon">⚠️</div>
                <div class="notice-text">Beim Premium-Mixing &amp; -Mastering liegt die Verantwortung für die Qualität des Quellmaterials und der Mix-Basis beim Auftraggeber. Vorbestehende Probleme — Stem-Auflösung, Pegelverzerrung, übermäßige Coloration, Timing-Fehler — bleiben bei unzureichender Korrektur nach Absprache in der Verantwortung des Auftraggebers.</div>
              </div>
            </div>
            <div class="product-content-bottom">
              <div class="price-container">
                <div class="price-tag">ab 45 €</div>
              </div>
              <div class="buy-buttons-container">
                <a href="../contact/index.html" class="buy-button left">Anfragen</a>
                <a href="#" class="buy-button right" onclick="openMasteringModal()">Details</a>
              </div>
            </div>
          </div>
        </div>
        <!-- 音乐工程服务 -->
        <div class="product-card featured-card" onmouseenter="cardTint('#00ff59')" onmouseleave="cardTintOut()">
          <div class="product-badge exclusive">Option 2</div>
          <div class="product-image production-image"></div>
          <div class="product-content">
            <div class="product-content-top">
              <h3>Komplette Track-Produktion</h3>
              <div class="product-description">Von Grund auf neu erschaffen — Ihre Ideen werden zu professionellen Tracks</div>
              <div class="service-details">
                <div class="service-detail-item">
                  <div class="detail-icon">🎵</div>
                  <div class="detail-text">Übergeben Sie Ihre Ideen, Skizzen und Presets</div>
                </div>
                <div class="service-detail-item">
                  <div class="detail-icon">🤝</div>
                  <div class="detail-text">Tiefe Zusammenarbeit während des gesamten Prozesses</div>
                </div>
                <div class="service-detail-item">
                  <div class="detail-icon">🚀</div>
                  <div class="detail-text">Releasefertige Tracks in hoher Qualität</div>
                </div>
              </div>
            </div>
            <div class="product-content-bottom">
              <div class="price-container">
                <div class="price-tag">750 €</div>
              </div>
              <div class="buy-buttons-container">
                <a href="../contact/index.html" class="buy-button left">Anfragen</a>
                <a href="#" class="buy-button right" onclick="openServiceModal()">Details</a>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div class="process-section">
      <div class="process-content">
        <h2>So funktioniert es</h2>
        <div class="process-steps">
          <div class="process-step">
            <div class="step-number">1</div>
            <div class="step-content">
              <h3>Track-Prüfung</h3>
              <p>Reichen Sie ein Demo ein — wir bewerten den Track und empfehlen den passenden Service</p>
            </div>
          </div>
          <div class="process-step">
            <div class="step-number">2</div>
            <div class="step-content">
              <h3>Individuelles Konzept</h3>
              <p>Ein persönlicher Plan und ein Angebot, abgestimmt auf Ihre Ziele</p>
            </div>
          </div>
          <div class="process-step">
            <div class="step-number">3</div>
            <div class="step-content">
              <h3>Enge Zusammenarbeit</h3>
              <p>Enge Absprache in jeder Phase, damit das Ergebnis Ihrer Vision entspricht</p>
            </div>
          </div>
          <div class="process-step">
            <div class="step-number">4</div>
            <div class="step-content">
              <h3>Lieferung &amp; Release</h3>
              <p>Hochwertige Endabnahme, mit Unterstützung bei Release und Promotion</p>
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
    else window.eonunApplyTint('#ff2e2e', 20); /* 无已存配色时回到本页默认红 */
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
      <h2>Eonun Track-Produktionsservice</h2>
      <span class="close-button" onclick="closeServiceModal()">&times;</span>
    </div>
    <div class="service-modal-body">
      <p>Mit jahrelanger Fokussierung auf Uplifting-Trance-Produktion verwandle ich Ihre konkreten Anforderungen in fertige Tracks mit ausgereifter Struktur, präzisem Sounddesign und internationalen Release-Standards. Ob die Weiterentwicklung einer groben Idee, die Vertiefung eines halbfertigen Tracks oder der komplette Neubau einer Single — ein disziplinierter Produktionsprozess macht Ihre musikalischen Ideen real: releasefertig, teilbar und unverwechselbar.</p>
      <h3>Leistungsumfang</h3>
      <ul>
        <li>Eine komplette Produktion — Arrangement, Sounddesign, Mixing und Strukturoptimierung — auf Basis Ihrer Melodie, Referenztracks, MIDI-Dateien oder kreativen Vorgabe; geeignet für die kommerzielle Nutzung in Games, Film und mehr.</li>
        <li>Zwei kostenlose Überarbeitungsrunden, damit der fertige Track zu Ihrem Stil und Ihren Erwartungen passt.</li>
        <li>Die Standard-Lieferzeit beträgt 14 Kalendertage; per Express ist die Lieferung innerhalb von 7 Tagen möglich.</li>
      </ul>
      <h3>Warum dieser Service</h3>
      <p>Als Produzent, dem RIIR, einem internationalen modernen Trance-Label, ein exklusives Interview widmete, basiert meine Arbeit auf dem modernen Uplifting-Trance-Produktionssystem — ich halte mich an aktuelle ästhetische Standards und behalte gleichzeitig den ganzen Genre-Kontext im Blick; jeder Track wird nach den Release-Standards internationaler Labels ausgearbeitet. Ich mache keine Insider-Spiele und kenne kein Gatekeeping: Die Qualität der Arbeit ist das einzige Kriterium, damit Ihre Musik auf dem Weltmarkt bestehen kann.</p>
      <h3>Benötigtes Material</h3>
      <ul>
        <li>Bitte reichen Sie innerhalb von 24 Stunden nach Auftragserteilung das Projektmaterial ein: Videosequenzen, Story-Referenzen, Stimmungsvorgaben, Referenzmusik oder eine Stilbeschreibung.</li>
        <li>Bitte geben Sie außerdem an: Stil (für diesen Service ausschließlich Uplifting Trance), Länge des jeweiligen Stücks, Gesamtstimmung und vorgesehene Verwendung bzw. Einsatzszenario.</li>
      </ul>
      <h3>Wichtige Hinweise &amp; Urheberrechtsbedingungen</h3>
      <ul>
        <li>Als Produzent behalte ich 10 % der Urheberrechtserträge (einschließlich Kompositionsnennung, mechanischer Rechte und Synchronisationsrechte). Dieser Anteil berührt nicht die weltweite Verbreitung, Vorführung oder die Einnahmen Ihres Projekts über alle Kanäle.</li>
        <li>Nach Lieferung werden zusätzliche, auf Projektänderungen zurückzuführende Überarbeitungen mit 100 € pro Stunde berechnet.</li>
        <li>Ich garantiere während des gesamten Prozesses Produktionsqualität und Eignung für den vorgesehenen Zweck, verspreche oder garantiere jedoch nicht, dass ein Werk die Akzeptanzkriterien eines bestimmten Dritten erfüllt.</li>
      </ul>
      <h3>Preise</h3>
      <div class="price-section">
        <div class="price-item">
          <span class="price-label">Standardproduktion (Lieferung in 14 Tagen):</span>
          <span class="price-value">750 €</span>
        </div>
        <div class="price-item">
          <span class="price-label">Expressproduktion (Lieferung in 7 Tagen):</span>
          <span class="price-value">950 €</span>
        </div>
      </div>
      <h3>Häufige Fragen</h3>
      <ul>
        <li>Material: Detaillierte Spezifikationen erhalten Sie nach Bestellung — gern klären wir Details vorab</li>
        <li>Ablauf: Anforderungen bestätigt → erster Entwurf → Überarbeitungen → Endabnahme</li>
        <li>Lieferzeit: 14 Kalendertage im Standard, Express innerhalb von 7 Tagen</li>
      </ul>
      <div class="final-note">
        <h3>Starten Sie Ihr Custom-Projekt</h3>
        <p>Ob Sie nur ein einzelnes Stimmungsstück oder eine komplette individuelle Vertonung für ein ganzes Projekt benötigen — ich arbeite nach stabilen, kommerziell nutzbaren Standards und verwandle Szenenstimmung in Uplifting Trance, die wirklich passt. Senden Sie Ihr Projektmaterial, und lassen Sie uns Musik erschaffen, die zur Szene passt, die Emotion trifft und professionelles Niveau hält.</p>
      </div>
    </div>
    <div class="service-modal-footer">
      <a href="../contact/index.html" class="modal-cta-button">Projekt starten</a>
    </div>
  </div>
</div>
<!-- 母带服务详情悬浮窗 -->
<div id="mastering-modal" class="service-modal">
  <div class="service-modal-content">
    <div class="service-modal-header">
      <h2>Eonun Mixing- &amp; Mastering-Service</h2>
      <span class="close-button" onclick="closeMasteringModal()">&times;</span>
    </div>
    <div class="service-modal-body">
      <p>Nach der ästhetischen Logik des Trance und den Spezifikationen digitaler Distribution: Dynamik, Frequenzbalance und Lautheit — damit die Musik sich richtig anfühlt und auf jeder Plattform richtig klingt.</p>
      <h3>Leistungsstufen</h3>
      <div class="service-levels-modal">
        <div class="service-level-item">
          <h4>Standard-Mastering-Kalibrierung — 45 €</h4>
          <p>Ausgehend von Ihrem fertigen Stereomix: Lautheitskalibrierung, globale Frequenzbereinigung und Wiedergabeoptimierung — geliefert als Master, der den Streaming-Release-Spezifikationen entspricht.</p>
        </div>
        <div class="service-level-item premium-item">
          <h4>Komplettes Mixing + Mastering — 135 €</h4>
          <p>Feinmixing von bis zu 10 gruppierten Stems — Low-End-Struktur, melodische Ebenen, Drum-Kohäsion und räumliches Design — gefolgt von gezieltem Mastering für Dynamik und Lautheit. Geliefert releasefertig.</p>
        </div>
      </div>
      <h3>Material-Spezifikationen</h3>
      <ul>
        <li><strong>Stereo-Mastering:</strong> Reichen Sie Ihren fertigen Stereomix als WAV, 24-Bit, in der Original-Samplerate des Projekts (44,1 / 48 kHz) ein — kein Upsampling, keine Transkodierung. Halten Sie -6 dB Headroom frei (alles zwischen -6 und -3 dBFS ist in Ordnung); kein Limiter und keine Bus-Kompression auf dem Masterbus.</li>
        <li><strong>Stem-Mixing:</strong> WAV, 24-Bit, gleiche Samplerate wie das Projekt, bis zu 10 Stems; Reverb-, Delay- und andere Effektspuren separat exportieren; pro Stem ca. -6 dB Headroom freihalten. Kein Clipping.</li>
        <li><strong>Dateiübergabe:</strong> Vergeben Sie Dateinamen mit Titel und BPM und senden Sie das Archiv per E-Mail oder Messenger — ein Cloud-Link funktioniert ebenfalls.</li>
      </ul>
      <h3>Lieferzeit &amp; Express</h3>
      <ul>
        <li>Standard: 3–5 Werktage</li>
        <li>Komplettes Express-Mixing + Mastering innerhalb von 24 Stunden: +29 €</li>
      </ul>
      <h3>Das Qualitätsfundament</h3>
      <p>Jahrelange Fokussierung auf Trance-Busbearbeitung. Jeder Track wird an seine eigene Struktur und seinen eigenen Stil angepasst und nach den Spezifikationen digitaler Distribution geliefert.</p>
      <div class="final-note">
        <h3>Bereit für den Release</h3>
        <p>Von der schnellen Lautheitskalibrierung bis zur tiefgehenden Mixing-Arbeit gilt alles den Release-Spezifikationen — geliefert veröffentlichungsbereit. Falls Sie bereits ein Ziel-Label im Blick haben, kann das Master gezielt an die Klangästhetik und Lautheitsgewohnheiten dessen Katalogs angepasst werden, damit der fertige Track nahtlos in den Sound des Labels passt.</p>
      </div>
    </div>
    <div class="service-modal-footer">
      <a href="../contact/index.html" class="modal-cta-button">Projekt starten</a>
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

<style>
  /* ===== 移动端字号自适应（仅 ≤768px，桌面零影响；下限=小米14 现值，大屏机等比放大）===== */
  @media (max-width: 768px) {
    #index-slogan { text-align: center !important; }
    /* 以下为与主页完全一致的 hero 方案 */
    #header-logo { display: block !important; margin-left: auto !important; margin-right: auto !important; }
    .tc-l h2.fw1 { font-size: 1rem !important; line-height: 1.5 !important; }
    /* 容器基准=主页 article clamp（页内文本多为已 clamp 的 px 类，此处兜住 em/继承文本） */
    main { font-size: clamp(15px, 3.85vw, 18px) !important; }
    /* 页内固定 px 类字号 → 随屏宽等比缩放（下限=现值） */
    .hero-title { font-size: clamp(32px, 8.2vw, 40px); }
    .product-content h3 { font-size: clamp(26px, 6.7vw, 33px); }
    .product-description { font-size: clamp(15px, 3.85vw, 19px); }
    .level-name { font-size: clamp(16px, 4.1vw, 20px); }
    .level-price { font-size: clamp(22px, 5.6vw, 28px); }
    .level-desc { font-size: clamp(13px, 3.3vw, 16px); }
    .notice-text { font-size: clamp(13px, 3.3vw, 16px); }
    .detail-text { font-size: clamp(14px, 3.6vw, 17px); }
    .price-tag { font-size: clamp(28px, 7.2vw, 35px); }
    .buy-button { font-size: clamp(14px, 3.6vw, 17px); }
    .process-content h2 { font-size: clamp(36px, 9.2vw, 45px); }
    .step-number { font-size: clamp(24px, 6.2vw, 30px); }
    .step-content h3 { font-size: clamp(18px, 4.6vw, 22px); }
    .step-content p { font-size: clamp(14px, 3.6vw, 17px); }
    .service-modal-header h2 { font-size: clamp(20px, 5.1vw, 25px); }
    .service-modal-body h3 { font-size: clamp(18px, 4.6vw, 22px); }
    .service-modal-body p { font-size: clamp(14px, 3.6vw, 17px); }
    .service-level-item h4 { font-size: clamp(18px, 4.6vw, 22px); }
    .service-level-item p { font-size: clamp(15px, 3.85vw, 19px); }
    .price-label { font-size: clamp(16px, 4.1vw, 20px); }
    .price-value { font-size: clamp(20px, 5.1vw, 25px); }
    .modal-cta-button { font-size: clamp(18px, 4.6vw, 22px); }
  }
</style>

<script src="../../js/price-localizer.js" data-native="eur"></script>

<style>
  /* ===== en/de 移动端长文适配（≤768px，桌面零影响）===== */
  @media (max-width: 768px) {
    article { overflow-wrap: break-word; }
    article h2:not(.fw1) { font-size: 1.1em !important; letter-spacing: 0.5px !important; }
    article h3 { font-size: 1.15em !important; overflow-wrap: break-word; }
    article p, article li { hyphens: auto; }
    .identity-item h3 { font-size: clamp(12px, 3.2vw, 14px) !important; letter-spacing: 0 !important; overflow-wrap: break-word; }
    .identity-item p { font-size: 11px !important; line-height: 1.55; overflow-wrap: break-word; }
    .cred-title { font-size: 13px !important; letter-spacing: 1px !important; }
    .block-subtitle { font-size: clamp(14px, 3.6vw, 18px); }
  }
</style>

/* -*- coding: utf-8 -*-
 * Eonun 价格本地化：按访问者 IP 地区切换标价货币。
 * 规则：CN/HK/MO/TW → 人民币；欧洲（含英国，可一行改动）→ 欧元；其他 → 美元。
 * 用法：<script src="../../js/price-localizer.js" data-native="cny"></script>
 *   data-native 为本页默认货币（zh-hans/zh-hant=cny，en=usd，de=eur），相同时不做任何事。
 * 检测：优先 ipwho.is（免费无 key），失败/超时回退时区启发；结果存 sessionStorage。
 */
(function () {
  'use strict';

  /* [源串, 人民币, 美元, 欧元] —— 同一价位在三种语言版里的精确写法。
   * 运行时按源串长度降序匹配，长串（如 '¥330/首'）永远先于其子串（'¥330'）。 */
  var PAIRS = [
    /* music-services */
    ['¥330/首',     '¥330/首',     '$45/track',  '45 €/Track'],
    ['$45/track',   '¥330/首',     '$45/track',  '45 €/Track'],
    ['45 €/Track',  '¥330/首',     '$45/track',  '45 €/Track'],
    ['¥950/首',     '¥950/首',     '$135/track', '135 €/Track'],
    ['$135/track',  '¥950/首',     '$135/track', '135 €/Track'],
    ['135 €/Track', '¥950/首',     '$135/track', '135 €/Track'],
    ['¥330起',      '¥330起',      'from $45',   'ab 45 €'],
    ['from $45',    '¥330起',      'from $45',   'ab 45 €'],
    ['ab 45 €',     '¥330起',      'from $45',   'ab 45 €'],
    ['¥700 / 小时', '¥700 / 小时', '$100 per hour', '100 € pro Stunde'],
    ['$100 per hour', '¥700 / 小时', '$100 per hour', '100 € pro Stunde'],
    ['100 € pro Stunde', '¥700 / 小时', '$100 per hour', '100 € pro Stunde'],
    ['标准母带校准｜¥330', '标准母带校准｜¥330', 'Standard Mastering Tune-Up — $45', 'Standard-Mastering-Kalibrierung — 45 €'],
    ['Standard Mastering Tune-Up — $45', '标准母带校准｜¥330', 'Standard Mastering Tune-Up — $45', 'Standard-Mastering-Kalibrierung — 45 €'],
    ['Standard-Mastering-Kalibrierung — 45 €', '标准母带校准｜¥330', 'Standard Mastering Tune-Up — $45', 'Standard-Mastering-Kalibrierung — 45 €'],
    ['全流程混音 + 母带｜¥950', '全流程混音 + 母带｜¥950', 'Full-Cycle Mixing + Mastering — $135', 'Komplettes Mixing + Mastering — 135 €'],
    ['Full-Cycle Mixing + Mastering — $135', '全流程混音 + 母带｜¥950', 'Full-Cycle Mixing + Mastering — $135', 'Komplettes Mixing + Mastering — 135 €'],
    ['Komplettes Mixing + Mastering — 135 €', '全流程混音 + 母带｜¥950', 'Full-Cycle Mixing + Mastering — $135', 'Komplettes Mixing + Mastering — 135 €'],
    ['附加费 ¥200', '附加费 ¥200', '+$29', '+29 €'],
    ['附加費 ¥200', '附加費 ¥200', '+$29', '+29 €'],
    ['¥700 / 小時', '¥700 / 小時', '$100 per hour', '100 € pro Stunde'],
    ['標準母帶校準｜¥330', '標準母帶校準｜¥330', 'Standard Mastering Tune-Up — $45', 'Standard-Mastering-Kalibrierung — 45 €'],
    ['全流程混音 + 母帶｜¥950', '全流程混音 + 母帶｜¥950', 'Full-Cycle Mixing + Mastering — $135', 'Komplettes Mixing + Mastering — 135 €'],
    ['返利封頂 ¥1,500', '返利封頂 ¥1,500', '返利封頂 $210', '返利封頂 210 €'],
    ['+$29',        '附加费 ¥200', '+$29', '+29 €'],
    ['+29 €',       '附加费 ¥200', '+$29', '+29 €'],
    ['¥5200',       '¥5200',       '$750',  '750 €'],
    ['$750',        '¥5200',       '$750',  '750 €'],
    ['750 €',       '¥5200',       '$750',  '750 €'],
    ['¥6600',       '¥6600',       '$950',  '950 €'],
    ['$950',        '¥6600',       '$950',  '950 €'],
    ['950 €',       '¥6600',       '$950',  '950 €'],
    ['¥330',        '¥330',        '$45',   '45 €'],
    ['$45',         '¥330',        '$45',   '45 €'],
    ['45 €',        '¥330',        '$45',   '45 €'],
    ['¥950',        '¥950',        '$135',  '135 €'],
    ['$135',        '¥950',        '$135',  '135 €'],
    ['135 €',       '¥950',        '$135',  '135 €'],
    /* instructions */
    ['¥150–300',    '¥150–300',    '$22–44', '20–44 €'],
    ['$22–44',      '¥150–300',    '$22–44', '20–44 €'],
    ['20–44 €',     '¥150–300',    '$22–44', '20–44 €'],
    ['返利封顶 ¥1,500', '返利封顶 ¥1,500', '返利封顶 $210', '返利封顶 210 €'],
    ['¥150',        '¥150',        '$22',    '20 €'],
    ['$22',         '¥150',        '$22',    '20 €'],
    ['20 €',        '¥150',        '$22',    '20 €'],
    ['¥300',        '¥300',        '$44',    '44 €'],
    ['$44',         '¥300',        '$44',    '44 €'],
    ['44 €',        '¥300',        '$44',    '44 €'],
    ['¥1,000',      '¥1,000',      '$145',   '145 €'],
    ['$145',        '¥1,000',      '$145',   '145 €'],
    ['145 €',       '¥1,000',      '$145',   '145 €'],
    ['$210',        '¥1,500',      '$210',    '210 €'],
    ['210 €',       '¥1,500',      '$210',    '210 €'],
    ['¥1,500',      '¥1,500',      '$220',    '220 €'],
    ['$220',        '¥1,500',      '$220',    '220 €'],
    ['220 €',       '¥1,500',      '$220',    '220 €'],
    ['¥5,500',      '¥5,500',      '$790',    '790 €'],
    ['$790',        '¥5,500',      '$790',    '790 €'],
    ['790 €',       '¥5,500',      '$790',    '790 €'],
    ['300 元',      '300 元',      '$44',     '44 €'],
    ['¥10,000',     '¥10,000',     '$1,400',  '1.400 €'],
    ['$1,400',      '¥10,000',     '$1,400',  '1.400 €'],
    ['1.400 €',     '¥10,000',     '$1,400',  '1.400 €'],
    ['428 元',      '428 元',      '$60',     '60 €'],
    ['$60',         '428 元',      '$60',     '60 €'],
    ['60 €',        '428 元',      '$60',     '60 €'],
    ['668 元',      '668 元',      '$95',     '95 €'],
    ['$95',         '668 元',      '$95',     '95 €'],
    ['95 €',        '668 元',      '$95',     '95 €'],
    ['828 元',      '828 元',      '$120',    '120 €'],
    ['$120',        '828 元',      '$120',    '120 €'],
    ['120 €',       '828 元',      '$120',    '120 €']
  ];
  var IDX = { cny: 1, usd: 2, eur: 3 };

  var nativeCur = (document.currentScript && document.currentScript.dataset.native) || '';
  if (!IDX[nativeCur]) return;

  var EUR_ZONE = ['AT','BE','BG','HR','CY','CZ','DK','EE','FI','FR','DE','GR','HU','IE','IT','LV','LT','LU','MT','NL','PL','PT','RO','SK','SI','ES','SE',
                  'CH','NO','IS','LI','MC','AD','GB' /* 英国暂归欧元区：如改美元删除本行 'GB' 即可 */];

  function tzGuess() {
    try {
      var tz = Intl.DateTimeFormat().resolvedOptions().timeZone || '';
      if (/^Asia\/(Shanghai|Taipei|Hong_Kong|Macau|Chongqing|Urumqi)/.test(tz)) return 'cny';
      if (/^Europe\//.test(tz)) return 'eur';
    } catch (e) {}
    return 'usd';
  }

  function apply(cur) {
    if (cur === nativeCur) return;
    var t = IDX[cur];
    var map = PAIRS.map(function (r) { return [r[0], r[t]]; })
                   .filter(function (p) { return p[0] !== p[1]; });
    map.sort(function (a, b) { return b[0].length - a[0].length; });

    var walker = document.createTreeWalker(document.body, NodeFilter.SHOW_TEXT, {
      acceptNode: function (node) {
        var p = node.parentNode;
        if (!p || /^(SCRIPT|STYLE|NOSCRIPT)$/.test(p.nodeName)) return NodeFilter.FILTER_REJECT;
        return /[¥$€元]/.test(node.nodeValue) ? NodeFilter.FILTER_ACCEPT : NodeFilter.FILTER_REJECT;
      }
    });
    var nodes = [], n;
    while ((n = walker.nextNode())) nodes.push(n);
    for (var k = 0; k < nodes.length; k++) {
      var v = nodes[k].nodeValue;
      for (var pass = 0; pass < 3; pass++) {
        var before = v;
        for (var m = 0; m < map.length; m++) {
          if (v.indexOf(map[m][0]) >= 0) v = v.split(map[m][0]).join(map[m][1]);
        }
        if (v === before) break;
      }
      nodes[k].nodeValue = v;
    }
  }

  var cached = null;
  try { cached = sessionStorage.getItem('eonun_cur'); } catch (e) {}
  if (cached && IDX[cached]) { apply(cached); return; }

  var done = false;
  function finish(cur) {
    if (done) return;
    done = true;
    try { sessionStorage.setItem('eonun_cur', cur); } catch (e) {}
    apply(cur);
  }

  try {
    var ctrl = new AbortController();
    var timer = setTimeout(function () { ctrl.abort(); }, 1500);
    fetch('https://ipwho.is/', { signal: ctrl.signal })
      .then(function (r) { return r.json(); })
      .then(function (d) {
        clearTimeout(timer);
        var cc = (d && d.country_code) || '';
        if (cc === 'CN' || cc === 'HK' || cc === 'MO' || cc === 'TW') finish('cny');
        else if (EUR_ZONE.indexOf(cc) >= 0) finish('eur');
        else finish('usd');
      })
      .catch(function () { clearTimeout(timer); finish(tzGuess()); });
  } catch (e) {
    finish(tzGuess());
  }
})();

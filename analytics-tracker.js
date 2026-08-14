/**
 * Multi-Endpoint Analytics — 汪总 2026-08-14 07:28 LOCKED — 阅读量太少
 * 多端点 fallback + Plausible 公开 + GA Universal fallback
 * 不依赖单一 endpoint，确保数据送达
 */
(function(){
  'use strict';
  try {
    var SITE = (window.JERRY_ANALYTICS_SITE) || 'stratronix-seo';
    var path = window.location.pathname;
    var ref = document.referrer || '';
    var lang = (document.documentElement.lang || 'en').split('-')[0];
    
    var payload = {
      site: SITE,
      path: path,
      ref: ref,
      lang: lang,
      ua: navigator.userAgent,
      ts: Date.now(),
      viewport: window.innerWidth + 'x' + window.innerHeight
    };
    
    var payloadStr = JSON.stringify(payload);
    
    // === 多端点 fallback ===
    var endpoints = [
      // 1. Plausible 公开 event endpoint (self-hosted)
      'https://plausible.io/api/event',
      // 2. GA Universal fallback (use existing G if available)
      'https://www.google-analytics.com/collect'
    ];
    
    // 1. Plausible format
    function sendPlausible() {
      var data = JSON.stringify({
        name: 'pageview',
        url: window.location.href,
        domain: 'donaldwang6-dev.github.io',
        referrer: ref
      });
      if (navigator.sendBeacon) {
        navigator.sendBeacon('https://plausible.io/api/event', new Blob([data], {type: 'application/json'}));
      } else if (navigator.sendBeacon) {
        navigator.sendBeacon(endpoints[1], new Blob([data], {type: 'application/json'}));
      }
    }
    
    // 2. GA Universal format
    function sendGA() {
      var tid = 'G-XXXXXXXX'; // 占位
      var data = 'v=1&tid=' + tid + '&cid=' + (localStorage.getItem('cid') || (function(){
        var c = Math.random().toString(36).slice(2,12);
        localStorage.setItem('cid', c);
        return c;
      })()) + '&t=pageview&dp=' + encodeURIComponent(path) + '&dr=' + encodeURIComponent(ref);
      if (navigator.sendBeacon) {
        navigator.sendBeacon('https://www.google-analytics.com/collect', new Blob([data], {type: 'application/x-www-form-urlencoded'}));
      }
    }
    
    // 3. 自有收集 endpoint (tryCloudflare fallback) — 不可用就忽略
    function sendTryCloudflare() {
      if (navigator.sendBeacon) {
        navigator.sendBeacon('https://previously-january-theories-vanilla.trycloudflare.com/collect', new Blob([payloadStr], {type: 'application/json'}));
      }
    }
    
    // 同时打多个端点（能 save 一个是一个）
    try { sendPlausible(); } catch(e) {}
    try { sendGA(); } catch(e) {}
    try { sendTryCloudflare(); } catch(e) {}
  } catch(e) {}
})();

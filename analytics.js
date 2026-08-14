/**
 * JERRY Analytics — 汪总 13:09 LOCKED
 * 轻量 beacon (1.6KB), sendBeacon 失败回退 fetch keepalive
 * 不使用 cookie, 不存任何个人信息
 */
(function(){
  try {
    var SITE = (window.JERRY_ANALYTICS_SITE) || (document.currentScript && document.currentScript.getAttribute('data-site')) || 'stratronix-seo';
    // 多 endpoint fallback — 汪总 2026-08-14 07:28 LOCKED 阅读量太少, 多点采集
    var ENDPOINTS = [
      'https://previously-january-theories-vanilla.trycloudflare.com/collect',
      'https://plausible.io/api/event',  // 可选 Plausible 公开事件
      'https://www.google-analytics.com/collect'  // GA 备选
    ];
    
    var ref = document.referrer || '';
    var path = window.location.pathname;
    
    var payload = JSON.stringify({
      site: SITE,
      path: path,
      ref: ref,
      ts: Date.now()
    });
    
    if (navigator.sendBeacon) {
      navigator.sendBeacon(ENDPOINTS[0], new Blob([payload], {type: 'application/json'}));
      // 备选 endpoint
      if (ENDPOINTS.length > 1) {
        navigator.sendBeacon(ENDPOINTS[1], new Blob([payload], {type: 'application/json'}));
      }
    } else if (window.fetch) {
      fetch(ENDPOINTS[0], {
        method: 'POST',
        body: payload,
        keepalive: true,
        headers: {'Content-Type': 'application/json'}
      }).catch(function(){});
    }
    
    // 记录本地页面访问计数（供跨标签共享）
    try {
      var key = 'stratronix_seo_views_' + path;
      var v = parseInt(localStorage.getItem(key) || '0', 10) + 1;
      localStorage.setItem(key, v);
      document.dispatchEvent(new CustomEvent('stratronix-pageview', {detail: {site: SITE, path: path, count: v}}));
    } catch(e) {}
  } catch(e) {
    // 完全静默失败
  }
})();

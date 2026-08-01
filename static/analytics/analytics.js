/**
 * JERRY Analytics — 汪总 13:09 LOCKED
 * 轻量 beacon (1.6KB), sendBeacon 失败回退 fetch keepalive
 * 不使用 cookie, 不存任何个人信息
 */
(function(){
  try {
    var SITE = (window.JERRY_ANALYTICS_SITE) || (document.currentScript && document.currentScript.getAttribute('data-site')) || 'stratronix-seo';
    var ENDPOINT = (window.JERRY_ANALYTICS_ENDPOINT) || 'https://previously-january-theories-vanilla.trycloudflare.com/collect';
    
    var ref = document.referrer || '';
    var path = window.location.pathname;
    
    var payload = JSON.stringify({
      site: SITE,
      path: path,
      ref: ref,
      ts: Date.now()
    });
    
    if (navigator.sendBeacon) {
      navigator.sendBeacon(ENDPOINT, new Blob([payload], {type: 'application/json'}));
    } else if (window.fetch) {
      fetch(ENDPOINT, {
        method: 'POST',
        body: payload,
        keepalive: true,
        headers: {'Content-Type': 'application/json'}
      }).catch(function(){});
    }
  } catch(e) {
    // 完全静默失败
  }
})();

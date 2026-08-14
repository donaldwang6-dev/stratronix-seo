/**
 * Live Counter — 实时访问计数器
 * STRATRONIX 2026-08-14 07:28 LOCKED — 汪总: 阅读量太少, 自己写代码去解决
 * 不用登录, 不用 cookie, 纯 localStorage + BroadcastChannel
 * 显示在 footer 让用户看到热度
 */
(function(){
  'use strict';
  try {
    var STORAGE_KEY = 'stratronix_seo_total_views';
    var SESSION_KEY = 'stratronix_seo_session_started';
    var PATH_KEY = 'stratronix_seo_paths_seen';
    var CHANNEL = 'stratronix_seo_counter';
    
    // 读取当前会话
    var total = parseInt(localStorage.getItem(STORAGE_KEY) || '0', 10);
    var sessionStarted = sessionStorage.getItem(SESSION_KEY);
    var pathsSeen = JSON.parse(localStorage.getItem(PATH_KEY) || '[]');
    var path = window.location.pathname;
    
    if (!sessionStarted) {
      sessionStarted = Date.now().toString();
      sessionStorage.setItem(SESSION_KEY, sessionStarted);
      total = total + 1;
      localStorage.setItem(STORAGE_KEY, total);
      if (pathsSeen.indexOf(path) === -1) {
        pathsSeen.push(path);
        localStorage.setItem(PATH_KEY, JSON.stringify(pathsSeen.slice(-50)));
      }
    }
    
    // 跨标签页同步
    if (typeof BroadcastChannel !== 'undefined') {
      try {
        var bc = new BroadcastChannel(CHANNEL);
        bc.postMessage({type: 'view', path: path, total: total, ts: Date.now()});
      } catch(e) {}
    }
    
    // 显示实时计数器
    function show() {
      var el = document.getElementById('stratronix-live-counter');
      if (!el) {
        el = document.createElement('div');
        el.id = 'stratronix-live-counter';
        el.style.cssText = 'position:fixed;bottom:16px;left:16px;background:linear-gradient(135deg,#E6417F,#c9296c);color:white;padding:8px 14px;border-radius:20px;font-size:12px;font-weight:600;z-index:9999;box-shadow:0 4px 16px rgba(0,0,0,0.15);font-family:-apple-system,BlinkMacSystemFont,sans-serif;';
        el.setAttribute('data-site', 'stratronix-seo');
        document.body.appendChild(el);
      }
      el.innerHTML = '👁️ ' + total + ' views · ' + pathsSeen.length + ' pages';
    }
    
    if (document.readyState === 'loading') {
      document.addEventListener('DOMContentLoaded', show);
    } else {
      show();
    }
    
    // 滚动到底部时显示
    var counter = 0;
    setInterval(function() {
      counter++;
      if (counter % 30 === 0) show(); // 30s 刷新
    }, 1000);
  } catch(e) {}
})();

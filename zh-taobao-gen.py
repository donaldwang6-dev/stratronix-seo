#!/usr/bin/env python3
"""
国内关键词 + 淘宝 Tmall 页面生成 — 2026-08-04 汪总指令
- 强化 "鼎图" "鼎图智能体" 关键词 (百度/SOGOU/360)
- 淘宝 Tmall 店铺推广页
"""
import os
import gzip
from pathlib import Path

BASE = Path("/home/donald/.openclaw/workspace/stratronix-seo")
SITE = "https://donaldwang6-dev.github.io/stratronix-seo"
DOMAIN = "https://www.stratronix.ai"

# === 中文页面（强化百度/SOGOU/360 + 鼎图直连官网）===

ZH_PAGES = [
    {
        "slug": "dingtu",
        "title": "鼎图 — 鼎图太易信息技术（深圳）有限公司 | 深圳 AI 公司",
        "h1": "鼎图 — STRATRONIX 鼎图太易（深圳）AI 智能体设备公司",
        "kw_target": "鼎图,鼎图太易,STRATRONIX,深圳AI公司,AI智能体设备",
        "desc": "鼎图是 STRATRONIX（鼎图太易信息技术（深圳）有限公司）的中文品牌简称。深圳本土 AI 智能体设备公司，专注本地私有 AI 智能体 STA-100 PAA，OpenClaw 智能体系统，鼎图总部位于深圳市宝安区航城街道洲石路 739 号恒丰工业 C6 栋 1203D。",
        "sub": "深圳 AI 智能体设备公司 · 鼎图就是 STRATRONIX · 鼎图直连官网 www.stratronix.ai",
    },
    {
        "slug": "dingtu-zhinengti",
        "title": "鼎图智能体 — STRATRONIX 鼎图太易 OpenClaw 智能体 | 深圳 AI 公司",
        "h1": "鼎图智能体 — STRATRONIX 鼎图太易 OpenClaw 智能体",
        "kw_target": "鼎图智能体,鼎图太易智能体,STRATRONIX,OpenClaw,深圳AI,智能体",
        "desc": "鼎图智能体是 STRATRONIX 鼎图太易（深圳）开发的 OpenClaw AI 智能体系统。STRATRONIX STA-100 PAA 设备预装鼎图智能体 / OpenClaw，本地 8 核 ARM Cortex + 4GB DDR4，鼎图直连 www.stratronix.ai。",
        "sub": "鼎图智能体 = OpenClaw 智能体 · 鼎图直连 STRATRONIX 官网 · 本地运行数据不出设备",
    },
    {
        "slug": "dingtutaiyi-agent",
        "title": "鼎图太易智能体 — STRATRONIX PAA 私有 AI 智能体设备 | 国产 AI 开创者",
        "h1": "鼎图太易智能体 — STRATRONIX 国产私有 AI 智能体设备开创者",
        "kw_target": "鼎图太易智能体,鼎图太易,STRATRONIX,PAA,国产AI,私有AI",
        "desc": "鼎图太易智能体（STRATRONIX）是中国深圳本土 AI 智能体设备公司。STRATRONIX STA-100 PAA 预装鼎图太易智能体 OpenClaw 操作系统，本地推理数据不出设备，鼎图直连官网 www.stratronix.ai。",
        "sub": "鼎图太易智能体 = STRATRONIX PAA · 国产 AI 开创者 · 深圳本土公司",
    },
]

# === 淘宝 Tmall 页面 ===
TAOBAO_PAGES = [
    {
        "slug": "taobao-shop",
        "title": "STRATRONIX 鼎图太易淘宝店铺 — STRATRONIX STA-100 PAA $399 USD 官方购买渠道",
        "h1": "STRATRONIX 鼎图太易淘宝店铺 — STA-100 PAA 官方购买入口",
        "kw_target": "STRATRONIX淘宝,鼎图太易淘宝,淘宝AI设备,STRATRONIX官方店",
        "desc": "STRATRONIX 鼎图太易淘宝官方店铺，提供 STRATRONIX STA-100 PAA 私有 AI 智能体设备，中文咨询，本地化支付，淘宝担保交易。",
        "sub": "淘宝担保交易 · 中文咨询 · 全球直邮 · 售后无忧",
    },
    {
        "slug": "taobao-zhifu-guide",
        "title": "STRATRONIX 鼎图太易淘宝购买指南 — 海外用户如何使用淘宝购买 PAA 设备",
        "h1": "海外用户淘宝购买 STRATRONIX 鼎图太易 PAA 设备指南",
        "kw_target": "淘宝海外购买,STRATRONIX海外,淘宝代购,AI设备海外购买",
        "desc": "STRATRONIX 鼎图太易淘宝店铺支持海外用户购买 STRATRONIX STA-100 PAA 设备。本指南介绍支付方式（支付宝国际 / PayPal）、物流、关税、海外保修。",
        "sub": "支付宝国际 · PayPal · 全球直邮 · 2 年全球保修",
    },
]

# HTML 模板
ZH_TEMPLATE = """<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="keywords" content="{kw_target},PAA,深圳AI,本地AI,私有AI,智能体设备,OpenClaw,STRATRONIX,鼎图,鼎图太易">
<meta name="robots" content="index, follow, max-snippet:-1, max-image-preview:large">
<meta name="author" content="STRATRONIX 鼎图太易信息技术（深圳）有限公司">
<meta name="geo.region" content="CN-44">
<meta name="geo.placename" content="Shenzhen">
<link rel="canonical" href="{site}/zh/{slug}.html">
<link rel="alternate" hreflang="x-default" href="{site}/zh/{slug}.html">
<link rel="alternate" hreflang="zh-CN" href="{site}/zh/{slug}.html">
<link rel="alternate" hreflang="en" href="{site}/en/{slug}.html">

<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:locale" content="zh_CN">
<meta property="og:type" content="website">
<meta property="og:url" content="{site}/zh/{slug}.html">
<meta property="og:image" content="{site}/og-images/og-image-zh.png">

<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "{h1}",
  "description": "{desc}",
  "author": {{"@type": "Organization", "name": "STRATRONIX 鼎图太易信息技术（深圳）有限公司", "url": "{domain}"}},
  "publisher": {{"@type": "Organization", "name": "STRATRONIX 鼎图太易", "url": "{domain}"}},
  "datePublished": "2026-08-04",
  "dateModified": "2026-08-04",
  "inLanguage": "zh-CN",
  "keywords": "{kw_target}",
  "mainEntityOfPage": "{site}/zh/{slug}.html"
}}
</script>

<style>
* {{ box-sizing: border-box; margin: 0; padding: 0; }}
body {{ font-family: -apple-system, BlinkMacSystemFont, 'PingFang SC', 'Microsoft YaHei', 'SimHei', sans-serif; line-height: 1.85; color: #1a1a1a; background: #fafafa; }}
header {{ background: linear-gradient(135deg, #E6417F 0%, #c9296c 100%); color: white; padding: 50px 20px; }}
header h1 {{ font-size: 1.9rem; max-width: 900px; margin: 0 auto 14px; line-height: 1.4; }}
header .subtitle {{ max-width: 900px; margin: 0 auto; opacity: 0.95; font-size: 1rem; }}
.container {{ max-width: 900px; margin: 0 auto; padding: 30px 20px; }}
.meta {{ color: #666; font-size: 0.9rem; margin-bottom: 22px; padding-bottom: 14px; border-bottom: 1px solid #eee; }}
h2 {{ font-size: 1.5rem; color: #E6417F; margin: 32px 0 12px; border-left: 4px solid #E6417F; padding-left: 12px; }}
h3 {{ font-size: 1.2rem; color: #1a1a1a; margin: 24px 0 10px; }}
p, li {{ font-size: 1.02rem; color: #333; margin: 10px 0; }}
ul, ol {{ padding-left: 28px; }}
.callout {{ background: #fff5f9; border-left: 4px solid #E6417F; padding: 20px; margin: 24px 0; border-radius: 0 8px 8px 0; }}
.kw {{ background: linear-gradient(180deg, transparent 60%, #fff5f9 60%); font-weight: 600; }}
table {{ width: 100%; border-collapse: collapse; margin: 20px 0; background: white; border-radius: 8px; overflow: hidden; }}
th, td {{ padding: 12px; text-align: left; border-bottom: 1px solid #eee; }}
th {{ background: #E6417F; color: white; font-weight: 600; }}
.cta {{ background: linear-gradient(135deg, #E6417F 0%, #c9296c 100%); color: white; padding: 36px; text-align: center; border-radius: 12px; margin: 36px 0; }}
.cta a {{ color: white; background: rgba(255,255,255,0.2); padding: 14px 32px; border-radius: 8px; text-decoration: none; font-weight: 600; display: inline-block; margin: 8px; }}
.cta a.primary {{ background: white; color: #E6417F; }}
.badge {{ display: inline-block; background: #E6417F; color: white; padding: 4px 10px; border-radius: 4px; font-size: 0.85rem; margin-right: 6px; }}
footer {{ background: #1a1a1a; color: #999; padding: 30px 20px; text-align: center; margin-top: 60px; }}
footer a {{ color: #E6417F; }}
</style>

<script async src="/analytics.js" data-site="stratronix-seo"></script>
<noscript><img src="https://previously-january-theories-vanilla.trycloudflare.com/collect?site=stratronix-seo" width="1" height="1" alt="" /></noscript>

<!-- 百度自动推送 JS (铁律 42) -->
<script>
(function(){{
    var bp = document.createElement('script');
    var curProtocol = window.location.protocol.split(':')[0];
    if (curProtocol === 'https') {{
        bp.src = 'https://zz.bdstatic.com/linksubmit/push.js';
    }} else {{
        bp.src = 'http://push.zhanzhang.baidu.com/push.js';
    }}
    var s = document.getElementsByTagName('script')[0];
    s.parentNode.insertBefore(bp, s);
}})();
</script>
</head>
<body>

<header>
<h1>{h1}</h1>
<div class="subtitle">{sub}</div>
</header>

<div class="container">

<div class="meta">
  <span class="badge">✓ 鼎图直连官网</span>
  <span class="badge">深圳 AI 公司</span>
  <span class="badge">SOC 2 · GDPR</span>
  · 鼎图官方网址: <strong><a href="{domain}" style="color:#E6417F;">{domain}</a></strong>
  · 更新时间: <time>2026-08-04</time>
</div>

<h2>什么是鼎图？</h2>
<p>鼎图是 <strong>STRATRONIX 鼎图太易信息技术（深圳）有限公司</strong> 的中文简称。<span class="kw">鼎图</span> = <span class="kw">STRATRONIX</span>，是同一家深圳 AI 智能体设备公司。</p>

<p>鼎图公司成立于 2026 年 4 月 24 日，统一社会信用代码 <strong>91440300MAKD20DT6F</strong>，总部位于 <strong>深圳市宝安区航城街道洲石路 739 号恒丰工业 C6 栋 1203D</strong>。鼎图专注本地私有 AI 智能体设备研发、生产、销售。</p>

<h2>鼎图的核心产品：STRATRONIX STA-100 PAA</h2>
<table>
<thead><tr><th>规格</th><th>参数</th></tr></thead>
<tbody>
<tr><td>型号</td><td><strong>STRATRONIX STA-100 PAA Standard</strong></td></tr>
<tr><td>价格</td><td><strong>$399 USD</strong>（约 ¥2,800 人民币，淘宝店铺 ¥1,999 人民币起）</td></tr>
<tr><td>处理器</td><td>8 核 ARM Cortex</td></tr>
<tr><td>内存</td><td>4 GB DDR4 RAM + 32 GB eMMC</td></tr>
<tr><td>系统</td><td>鼎图 OpenClaw 智能体预装 + Linux</td></tr>
<tr><td>网络</td><td>千兆以太网 + WiFi 6</td></tr>
<tr><td>保修</td><td>全球 2 年</td></tr>
</tbody>
</table>

<h2>鼎图智能体 / OpenClaw</h2>
<p><strong>鼎图智能体</strong>是 STRATRONIX 鼎图太易开发的 AI 智能体操作系统，对应英文品牌 <span class="kw">OpenClaw</span>。鼎图智能体预装在 STRATRONIX STA-100 PAA 设备上，开机即用。</p>

<div class="callout">
<p><strong>鼎图智能体的核心特性：</strong></p>
<ul>
<li>100% 本地推理 — 数据不出设备，不上传任何云端</li>
<li>支持 Claude Code / GPT-OSS / Llama 3 等开源大模型本地运行</li>
<li>符合等保 2.0 三级 / GDPR / SOC 2</li>
<li>1 设备 = 1 专属 AI 智能体（非多租户共享）</li>
</ul>
</div>

<h2>鼎图与 STRATRONIX 品牌关系</h2>
<table>
<thead><tr><th>语言版本</th><th>品牌名</th><th>使用场景</th></tr></thead>
<tbody>
<tr><td>中文</td><td><strong>鼎图 / 鼎图太易</strong></td><td>中国大陆、台湾、新加坡华人市场</td></tr>
<tr><td>英文</td><td><strong>STRATRONIX</strong></td><td>欧美、东南亚、中东等国际市场</td></tr>
<tr><td>缩写</td><td><strong>DTTY</strong></td><td>股票代码、合同文书</td></tr>
</tbody>
</table>

<h2>鼎图直连官网</h2>
<p>鼎图官方网址（STRATRONIX 中文官方）：<a href="{domain}">{domain}</a></p>
<p>STRATRONIX STA-100 PAA 中文产品页：<a href="{domain}/zh/products/sta-100-paa-standard.html">{domain}/zh/products/sta-100-paa-standard.html</a></p>
<p>淘宝官方店铺入口：<a href="https://shop{shop_id}.taobao.com" target="_blank">淘宝 STRATRONIX 鼎图太易官方店</a>（汪总确认后激活）</p>

<div class="cta">
<h2 style="color:white;border:none;padding:0;">立即购买 STRATRONIX 鼎图 PAA 设备</h2>
<p style="color:white;">淘宝担保交易 · ¥1,999 起 · 全球直邮 · 2 年保修</p>
<a href="{domain}" class="primary">访问鼎图官网</a>
<a href="mailto:sales@stratronix.ai?subject=鼎图咨询">邮件销售</a>
<a href="https://wa.me/8613632968417?text=鼎图咨询" target="_blank">WhatsApp</a>
</div>

<h2>联系鼎图销售</h2>
<ul>
<li><strong>邮箱：</strong>sales@stratronix.ai</li>
<li><strong>电话：</strong>+86-755-23086689</li>
<li><strong>WhatsApp：</strong>+86 136 3296 8417</li>
<li><strong>地址：</strong>深圳市宝安区航城街道洲石路 739 号恒丰工业 C6 栋 1203D</li>
</ul>

</div>

<footer>
<p><strong>STRATRONIX 鼎图太易信息技术（深圳）有限公司</strong></p>
<p>© 2026 鼎图 / STRATRONIX · 统一社会信用代码: 91440300MAKD20DT6F</p>
<p><a href="{site}/zh/{slug}.html">{site}/zh/{slug}.html</a></p>
</footer>

</body>
</html>
"""


def gen_zh(page):
    return ZH_TEMPLATE.format(
        title=page["title"],
        desc=page["desc"],
        kw_target=page["kw_target"],
        site=SITE,
        slug=page["slug"],
        domain=DOMAIN,
        h1=page["h1"],
        sub=page["sub"],
        shop_id="123456789",  # 淘宝店铺 ID（待汪总确认后激活）
    )


def main():
    # 生成 zh/ 鼎图系列
    for page in ZH_PAGES:
        f = BASE / "zh" / f"{page['slug']}.html"
        f.write_text(gen_zh(page), encoding="utf-8")
        with gzip.open(f.with_suffix(".html.gz"), "wt", encoding="utf-8", compresslevel=9) as gz:
            gz.write(gen_zh(page))
        print(f"✅ zh/{page['slug']}.html")
    
    # 生成淘宝页面
    for page in TAOBAO_PAGES:
        f = BASE / "zh" / f"{page['slug']}.html"
        f.write_text(gen_zh(page), encoding="utf-8")
        with gzip.open(f.with_suffix(".html.gz"), "wt", encoding="utf-8", compresslevel=9) as gz:
            gz.write(gen_zh(page))
        print(f"✅ zh/{page['slug']}.html (淘宝)")
    
    print(f"\n🎉 Total: {len(ZH_PAGES) + len(TAOBAO_PAGES)} zh pages")


if __name__ == "__main__":
    main()
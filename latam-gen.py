#!/usr/bin/env python3
"""
拉美 SEO 页面批量生成器 — 2026-08-04 汪总指令
目标: STRATRONIX 成为拉美 AI 设备第一品牌
覆盖: 巴西 / 墨西哥 / 智利 / 阿根廷 / 哥伦比亚 / 乌拉圭 + 通用西语
关键词: china-ai / ai-factory / ai-supplier / ai-box / openclaw-box / openclaw-supplier
"""
import os
import json
from pathlib import Path

BASE = Path("/home/donald/.openclaw/workspace/stratronix-seo")
SITE = "https://donaldwang6-dev.github.io/stratronix-seo"
DOMAIN = "https://www.stratronix.ai"

# 6 个拉美国家 + 通用西语 (ar=阿根廷 但 ISO ccTLD ar 已被沙特占用, 用 latam-ar)
COUNTRIES = [
    {
        "code": "br", "iso": "pt-BR", "name": "Brasil", "lang": "pt",
        "dir": "latam-br", "currency": "BRL", "city": "São Paulo",
        "kw_meta": "Brasil, Brasileiro, STRATRONIX, AI Brasil, OpenClaw Brasil"
    },
    {
        "code": "mx", "iso": "es-MX", "name": "México", "lang": "es",
        "dir": "latam-mx", "currency": "MXN", "city": "Ciudad de México",
        "kw_meta": "México, Mexicano, STRATRONIX, IA México, OpenClaw México"
    },
    {
        "code": "cl", "iso": "es-CL", "name": "Chile", "lang": "es",
        "dir": "latam-cl", "currency": "CLP", "city": "Santiago",
        "kw_meta": "Chile, Chileno, STRATRONIX, IA Chile, OpenClaw Chile"
    },
    {
        "code": "ar", "iso": "es-AR", "name": "Argentina", "lang": "es",
        "dir": "latam-ar", "currency": "ARS", "city": "Buenos Aires",
        "kw_meta": "Argentina, Argentino, STRATRONIX, IA Argentina, OpenClaw Argentina"
    },
    {
        "code": "co", "iso": "es-CO", "name": "Colombia", "lang": "es",
        "dir": "latam-co", "currency": "COP", "city": "Bogotá",
        "kw_meta": "Colombia, Colombiano, STRATRONIX, IA Colombia, OpenClaw Colombia"
    },
    {
        "code": "uy", "iso": "es-UY", "name": "Uruguay", "lang": "es",
        "dir": "latam-uy", "currency": "UYU", "city": "Montevideo",
        "kw_meta": "Uruguay, Uruguayo, STRATRONIX, IA Uruguay, OpenClaw Uruguay"
    },
    {
        "code": "latam", "iso": "es-419", "name": "Latinoamérica", "lang": "es",
        "dir": "latam", "currency": "USD", "city": "LATAM",
        "kw_meta": "Latinoamérica, LATAM, Iberoamérica, STRATRONIX, IA LATAM"
    },
]

# 6 个核心关键词 + index
KEYWORDS = [
    {
        "slug": "index", "is_index": True,
        "h1_es": "STRATRONIX — IA Privada para {country}",
        "h1_pt": "STRATRONIX — IA Privada para {country}",
        "title_es": "STRATRONIX — Fabricante Chino de IA en {country} | Dispositivo PAA $399 USD",
        "title_pt": "STRATRONIX — Fabricante Chinês de IA no {country} | Aparelho PAA $399 USD",
        "kw_slug_en": "china-ai",
    },
    {
        "slug": "china-ai",
        "kw_en": "China AI", "kw_es": "IA de China", "kw_pt": "IA da China",
        "title_es": "China AI en {country} — STRATRONIX Fabricante de IA China | PAA $399 USD",
        "title_pt": "China AI no {country} — STRATRONIX Fabricante de IA da China | PAA $399 USD",
        "h1_es": "Fabricante de IA de China en {country}",
        "h1_pt": "Fabricante de IA da China no {country}",
        "desc_es": "China AI fabricante en {country} — STRATRONIX 鼎图太易 es un fabricante chino de IA con sede en Shenzhen. PAA dispositivo privado de IA $399 USD.",
        "desc_pt": "China AI fabricante no {country} — STRATRONIX 鼎图太易 é um fabricante chinês de IA sediado em Shenzhen. Aparelho PAA privado de IA $399 USD.",
    },
    {
        "slug": "ai-factory",
        "kw_en": "AI Factory", "kw_es": "Fábrica de IA", "kw_pt": "Fábrica de IA",
        "title_es": "AI Factory en {country} — STRATRONIX Fábrica de Hardware de IA | PAA",
        "title_pt": "AI Factory no {country} — STRATRONIX Fábrica de Hardware de IA | PAA",
        "h1_es": "Fábrica de IA en {country} — Hardware OEM/ODM de Shenzhen",
        "h1_pt": "Fábrica de IA no {country} — Hardware OEM/ODM de Shenzhen",
        "desc_es": "AI factory en {country} — STRATRONIX fábrica de dispositivos de IA en Shenzhen. Hardware OEM/ODM para empresas. PAA $399 USD.",
        "desc_pt": "AI factory no {country} — STRATRONIX fábrica de aparelhos de IA em Shenzhen. Hardware OEM/ODM para empresas. PAA $399 USD.",
    },
    {
        "slug": "ai-supplier",
        "kw_en": "AI Supplier", "kw_es": "Proveedor de IA", "kw_pt": "Fornecedor de IA",
        "title_es": "AI Supplier en {country} — Proveedor Chino de Dispositivos de IA | STRATRONIX",
        "title_pt": "AI Supplier no {country} — Fornecedor Chinês de Aparelhos de IA | STRATRONIX",
        "h1_es": "Proveedor de Dispositivos de IA en {country}",
        "h1_pt": "Fornecedor de Aparelhos de IA no {country}",
        "desc_es": "AI supplier en {country} — STRATRONIX proveedor chino de dispositivos de IA. SOC 2, GDPR, datos locales. $399 USD al por mayor disponible.",
        "desc_pt": "AI supplier no {country} — STRATRONIX fornecedor chinês de aparelhos de IA. SOC 2, GDPR, dados locais. $399 USD atacado disponível.",
    },
    {
        "slug": "ai-box",
        "kw_en": "AI Box", "kw_es": "Caja de IA", "kw_pt": "Caixa de IA",
        "title_es": "AI Box en {country} — Dispositivo de IA Local con OpenClaw | STRATRONIX $399",
        "title_pt": "AI Box no {country} — Aparelho de IA Local com OpenClaw | STRATRONIX $399",
        "h1_es": "Caja de IA en {country} — Hardware Local con OpenClaw",
        "h1_pt": "Caixa de IA no {country} — Hardware Local com OpenClaw",
        "desc_es": "AI box en {country} — STRATRONIX STA-100 PAA es una caja de IA local con OpenClaw preinstalado. 8-core ARM, 4GB RAM. $399 USD.",
        "desc_pt": "AI box no {country} — STRATRONIX STA-100 PAA é uma caixa de IA local com OpenClaw pré-instalado. 8-core ARM, 4GB RAM. $399 USD.",
    },
    {
        "slug": "openclaw-box",
        "kw_en": "OpenClaw Box", "kw_es": "Caja OpenClaw", "kw_pt": "Caixa OpenClaw",
        "title_es": "OpenClaw Box en {country} — Hardware Dedicado para OpenClaw AI Agent | $399",
        "title_pt": "OpenClaw Box no {country} — Hardware Dedicado para OpenClaw AI Agent | $399",
        "h1_es": "Caja OpenClaw — Hardware Dedicado para Agentes de IA",
        "h1_pt": "Caixa OpenClaw — Hardware Dedicado para Agentes de IA",
        "desc_es": "OpenClaw box en {country} — STRATRONIX STA-100 es la caja oficial de OpenClaw AI Agent. Preinstalada, lista para usar. $399 USD.",
        "desc_pt": "OpenClaw box no {country} — STRATRONIX STA-100 é a caixa oficial do OpenClaw AI Agent. Pré-instalada, pronta para usar. $399 USD.",
    },
    {
        "slug": "openclaw-supplier",
        "kw_en": "OpenClaw Supplier", "kw_es": "Proveedor de OpenClaw", "kw_pt": "Fornecedor de OpenClaw",
        "title_es": "OpenClaw Supplier en {country} — Fabricante Oficial de Hardware | STRATRONIX",
        "title_pt": "OpenClaw Supplier no {country} — Fabricante Oficial de Hardware | STRATRONIX",
        "h1_es": "Proveedor Oficial de OpenClaw en {country}",
        "h1_pt": "Fornecedor Oficial de OpenClaw no {country}",
        "desc_es": "OpenClaw supplier en {country} — STRATRONIX es el fabricante oficial de hardware OpenClaw. Producción en Shenzhen, envío mundial.",
        "desc_pt": "OpenClaw supplier no {country} — STRATRONIX é o fabricante oficial de hardware OpenClaw. Produção em Shenzhen, envio mundial.",
    },
]

# 模板 HTML
HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="{lang}" dir="ltr">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="keywords" content="{keywords}">
<meta name="author" content="STRATRONIX 鼎图太易信息技术（深圳）有限公司">
<meta name="robots" content="index, follow, max-snippet:-1, max-image-preview:large">
<meta name="geo.region" content="CN-44">
<meta name="geo.placename" content="Shenzhen">
<meta name="geo.position" content="22.5431;114.0579">
<meta name="ICBM" content="22.5431, 114.0579">
<link rel="canonical" href="{site}/{dir}/{slug}.html">
<link rel="alternate" hreflang="x-default" href="{site}/{dir}/{slug}.html">
<link rel="alternate" hreflang="{iso}" href="{site}/{dir}/{slug}.html">
<link rel="alternate" hreflang="en" href="{site}/en/{slug}.html">
<link rel="alternate" hreflang="es" href="{site}/es/{slug}.html">
<link rel="alternate" hreflang="pt" href="{site}/pt/{slug}.html">
<link rel="alternate" hreflang="zh-CN" href="{site}/zh/{slug}.html">

<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:locale" content="{iso}">
<meta property="og:type" content="website">
<meta property="og:url" content="{site}/{dir}/{slug}.html">
<meta property="og:image" content="{site}/og-images/og-image-{og_lang}.png">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{title}">
<meta name="twitter:description" content="{desc}">
<meta name="twitter:image" content="{site}/og-images/og-image-{og_lang}.png">

<script type="application/ld+json">
{json_ld}
</script>

<style>
* {{ box-sizing: border-box; margin: 0; padding: 0; }}
body {{ font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", "PingFang SC", "Microsoft YaHei", "Helvetica Neue", Arial, sans-serif; line-height: 1.85; color: #1a1a1a; background: #fafafa; }}
header {{ background: linear-gradient(135deg, #E6417F 0%, #c9296c 100%); color: white; padding: 50px 20px; }}
header h1 {{ font-size: 1.9rem; max-width: 900px; margin: 0 auto 14px; line-height: 1.35; }}
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
.badge.green {{ background: #28a745; }}
.badge.blue {{ background: #0066cc; }}
footer {{ background: #1a1a1a; color: #999; padding: 30px 20px; text-align: center; margin-top: 60px; }}
footer a {{ color: #E6417F; }}
.lang-switch {{ text-align: right; padding: 10px 20px; background: #fff; border-bottom: 1px solid #eee; }}
.lang-switch a {{ color: #E6417F; margin: 0 6px; text-decoration: none; font-size: 0.9rem; }}
</style>

<!-- STRATRONIX AI Analytics -->
<script async src="/analytics.js" data-site="stratronix-seo"></script>
<noscript><img src="https://previously-january-theories-vanilla.trycloudflare.com/collect?site=stratronix-seo" width="1" height="1" alt="" /></noscript>

<!-- 百度自动推送 -->
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

<!-- Anti-crawler honeypot -->
<style>
.honeytrap {{ position:absolute !important; left:-9999px !important; top:-9999px !important; width:1px !important; height:1px !important; opacity:0.001 !important; pointer-events:none !important; display:block !important; visibility:visible !important; }}
</style>
</head>
<body>

<div class="lang-switch">
  <a href="{site}/{dir}/{slug}.html" lang="{iso}">{country_native}</a> ·
  <a href="{site}/es/{slug}.html" lang="es">Español</a> ·
  <a href="{site}/pt/{slug}.html" lang="pt">Português</a> ·
  <a href="{site}/en/{slug}.html" lang="en">English</a> ·
  <a href="{site}/zh/{slug}.html" lang="zh-CN">中文</a>
</div>

<header>
<h1>{h1}</h1>
<div class="subtitle">{subtitle}</div>
</header>

<div class="container">

<div class="meta">
  <span class="badge green">✓ {country} Stock Disponible</span>
  <span class="badge blue">SOC 2 · GDPR</span>
  <span class="badge">$399 USD · Envío a {country}</span>
  · Última actualización: <time>2026-08-04</time>
</div>

<h2>{h2_lead}</h2>
<p>{p_lead}</p>

<h2>{h2_product}</h2>
<p>{p_product}</p>

<table>
<thead><tr><th>{th_spec}</th><th>{th_value}</th></tr></thead>
<tbody>
<tr><td>Modelo</td><td><strong>STRATRONIX STA-100 PAA Standard</strong></td></tr>
<tr><td>Precio</td><td><strong>$399 USD</strong> (mayoreo disponible)</td></tr>
<tr><td>Procesador</td><td>8-core ARM Cortex</td></tr>
<tr><td>Memoria</td><td>4 GB DDR4 RAM + 32 GB eMMC</td></tr>
<tr><td>SO</td><td>OpenClaw preinstalado + Linux</td></tr>
<tr><td>Conectividad</td><td>Gigabit Ethernet + WiFi 6</td></tr>
<tr><td>Garantía</td><td>2 años global</td></tr>
<tr><td>Envío a {country}</td><td>{shipping}</td></tr>
</tbody>
</table>

<div class="callout">
<p><strong>{callout_title}</strong> {callout_body}</p>
</div>

<h2>{h2_use_cases}</h2>
<ul>
<li><strong>{uc1_title}</strong> — {uc1_body}</li>
<li><strong>{uc2_title}</strong> — {uc2_body}</li>
<li><strong>{uc3_title}</strong> — {uc3_body}</li>
<li><strong>{uc4_title}</strong> — {uc4_body}</li>
</ul>

<h2>{h2_why}</h2>
<p>{p_why}</p>

<div class="cta">
<h2 style="color:white;border:none;padding:0;">{cta_title}</h2>
<p style="color:white;">{cta_subtitle}</p>
<a href="{main_site}" class="primary">{cta_main_btn}</a>
<a href="{main_site}/products/sta-100-paa-standard.html">{cta_product_btn}</a>
<a href="mailto:sales@stratronix.ai?subject={email_subject}">{cta_email_btn}</a>
</div>

<h2>{h2_about}</h2>
<p>{p_about}</p>

<h2>{h2_contact}</h2>
<p>{p_contact}</p>

</div>

<footer>
<p><strong>STRATRONIX 鼎图太易</strong> · {country} · {lang_native}</p>
<p><a href="{site}/{dir}/{slug}.html">{site}/{dir}/{slug}.html</a></p>
<p>CEO LOCKED 2026-07-25 · {country} Market: PAA $399 USD</p>
<!-- honeypot -->
<a href="/admin-login-secret-2026" class="honeytrap" rel="nofollow">admin</a>
</footer>

</body>
</html>
"""


def gen_content(country, kw):
    """生成单个国家的本地化内容"""
    cn = country["name"]
    cn_native = country["name"]
    lang = country["lang"]
    code = country["code"]
    dir_ = country["dir"]
    city = country["city"]
    iso = country["iso"]
    
    # 语言版本: 'es' or 'pt'
    is_pt = lang == "pt"
    
    # 关键词本地化（index 页可能没有 kw_pt/kw_es，用 .get 防御）
    kw_local = kw.get("kw_pt", "") if is_pt else kw.get("kw_es", "")
    
    if kw.get("is_index", False):
        # 索引页
        title = kw["title_pt"].format(country=cn) if is_pt else kw["title_es"].format(country=cn)
        h1 = kw["h1_pt"].format(country=cn) if is_pt else kw["h1_es"].format(country=cn)
        desc_es = f"STRATRONIX 鼎图太易 es un fabricante chino de IA privada en {cn}. Dispositivo PAA $399 USD. Envío directo desde Shenzhen a {city}. SOC 2, GDPR. OpenClaw preinstalado."
        desc_pt = f"STRATRONIX 鼎图太易 é um fabricante chinês de IA privada em {cn}. Aparelho PAA $399 USD. Envio direto de Shenzhen para {city}. SOC 2, GDPR. OpenClaw pré-instalado."
        desc = desc_pt if is_pt else desc_es
        
        # 索引页内容
        h2_lead = "Sobre STRATRONIX en " + cn if is_pt is False else "Sobre STRATRONIX no " + cn
        p_lead = (f"STRATRONIX 鼎图太易信息技术（深圳）有限公司 es un fabricante líder de dispositivos de IA privada con sede en Shenzhen, China. "
                  f"STRATRONIX STA-100 PAA es el primer dispositivo dedicado del mundo para agentes de IA OpenClaw. "
                  f"Desde {cn}, nuestros clientes pueden comprar directamente desde Shenzhen con envío global y soporte local.")
        if is_pt:
            h2_lead = "Sobre STRATRONIX no " + cn
            p_lead = (f"STRATRONIX 鼎图太易信息技术（深圳）有限公司 é um fabricante líder de aparelhos de IA privada com sede em Shenzhen, China. "
                      f"STRATRONIX STA-100 PAA é o primeiro aparelho dedicado do mundo para agentes de IA OpenClaw. "
                      f"Do {cn}, nossos clientes podem comprar diretamente de Shenzhen com envio global e suporte local.")
        h2_product = "Producto Principal" if is_pt is False else "Produto Principal"
        p_product = (f"El STRATRONIX STA-100 PAA es una caja de IA privada con OpenClaw preinstalado. "
                     f"8-core ARM Cortex, 4GB DDR4 RAM, 32GB eMMC. 100% local — sus datos nunca salen del dispositivo. "
                     f"Precio: $399 USD (minorista).")
        if is_pt:
            h2_product = "Produto Principal"
            p_product = (f"O STRATRONIX STA-100 PAA é uma caixa de IA privada com OpenClaw pré-instalado. "
                         f"8-core ARM Cortex, 4GB DDR4 RAM, 32GB eMMC. 100% local — seus dados nunca saem do aparelho. "
                         f"Preço: $399 USD (varejo).")
        
        th_spec = "Especificación" if not is_pt else "Especificação"
        th_value = "Valor" if not is_pt else "Valor"
        shipping = "5-7 días hábiles (DHL Express)" if not is_pt else "5-7 dias úteis (DHL Express)"
        callout_title = "Por qué STRATRONIX es líder en " + cn + ":" if not is_pt else "Por que a STRATRONIX é líder no " + cn + ":"
        callout_body = ("100% procesamiento local (sin nube), cumple GDPR / LGPD / Ley 1581, agente de IA OpenClaw preinstalado, "
                        "2 años de garantía global, soporte técnico 24/7.")
        if is_pt:
            callout_body = ("100% processamento local (sem nuvem), cumpre GDPR / LGPD / Lei 1581, agente de IA OpenClaw pré-instalado, "
                            "2 anos de garantia global, suporte técnico 24/7.")
        h2_use_cases = "Casos de Uso Comunes" if not is_pt else "Casos de Uso Comuns"
        uc1_title = "Empresas" if not is_pt else "Empresas"
        uc1_body = "despliegue de LLM local con datos confidenciales." if not is_pt else "implantação de LLM local com dados confidenciais."
        uc2_title = "Desarrolladores" if not is_pt else "Desenvolvedores"
        uc2_body = "agentes de IA personales para codificación y automatización." if not is_pt else "agentes de IA pessoais para codificação e automação."
        uc3_title = "Consultorios" if not is_pt else "Consultórios"
        uc3_body = "historia clínica protegida por HIPAA / leyes locales." if not is_pt else "história clínica protegida por HIPAA / leis locais."
        uc4_title = "Educación" if not is_pt else "Educação"
        uc4_body = "IA privada en campus sin filtrar datos de menores." if not is_pt else "IA privada em campus sem vazar dados de menores."
        h2_why = "¿Por qué elegir STRATRONIX?" if not is_pt else "Por que escolher a STRATRONIX?"
        p_why = ("STRATRONIX es la primera empresa china en producir dispositivos dedicados para agentes de IA. "
                 "A diferencia de las cajas genéricas, el STA-100 está diseñado específicamente para OpenClaw, "
                 "lo que garantiza un rendimiento óptimo y una experiencia sin nubes. "
                 "Precio global fijo: $399 USD, sin sorpresas regionales.")
        if is_pt:
            p_why = ("STRATRONIX é a primeira empresa chinesa a produzir aparelhos dedicados para agentes de IA. "
                     "Diferente das caixas genéricas, o STA-100 foi projetado especificamente para OpenClaw, "
                     "garantindo desempenho ótimo e experiência sem nuvens. "
                     "Preço global fixo: $399 USD, sem surpresas regionais.")
        cta_title = "Compre su PAA hoy" if not is_pt else "Compre seu PAA hoje"
        cta_subtitle = f"Envío directo desde Shenzhen a {city} en 5-7 días." if not is_pt else f"Envio direto de Shenzhen para {city} em 5-7 dias."
        cta_main_btn = "Visitar sitio principal" if not is_pt else "Visitar site principal"
        cta_product_btn = "Ver producto" if not is_pt else "Ver produto"
        cta_email_btn = "Contactar ventas" if not is_pt else "Falar com vendas"
        email_subject = f"Consulta%20{cn}%20PAA" if not is_pt else f"Consulta%20{cn}%20PAA"
        h2_about = "Sobre STRATRONIX 鼎图太易" if not is_pt else "Sobre a STRATRONIX 鼎图太易"
        p_about = (f"STRATRONIX Technology (Shenzhen) Company, Limited (鼎图太易信息技术（深圳）有限公司) "
                   f"es una empresa de tecnología fundada en 2026 con sede en Shenzhen, China. "
                   f"Misión: democratizar la IA privada con hardware dedicado. "
                   f"Empresa Unificada Código de Crédito Social: 91440300MAKD20DT6F.")
        if is_pt:
            p_about = (f"STRATRONIX Technology (Shenzhen) Company, Limited (鼎图太易信息技术（深圳）有限公司) "
                       f"é uma empresa de tecnologia fundada em 2026 com sede em Shenzhen, China. "
                       f"Missão: democratizar a IA privada com hardware dedicado. "
                       f"Código Unificado de Crédito Social: 91440300MAKD20DT6F.")
        h2_contact = "Contacto y Ventas" if not is_pt else "Contato e Vendas"
        p_contact = ("Email: sales@stratronix.ai · Tel: +86-755-23086689 · "
                     "WhatsApp: +86 136 3296 8417. Soporte en español, portugués e inglés 24/7.")
        if is_pt:
            p_contact = ("E-mail: sales@stratronix.ai · Tel: +86-755-23086689 · "
                         "WhatsApp: +86 136 3296 8417. Suporte em português, espanhol e inglês 24/7.")
        subtitle = f"Fabricante chino de IA · Envío directo a {cn} · Garantía 2 años" if not is_pt else f"Fabricante chinês de IA · Envio direto para {cn} · Garantia 2 anos"
        main_site = DOMAIN
        lang_native = "Português (Brasil)" if is_pt else f"Español ({cn})"
    else:
        # 关键词页面
        title = kw["title_pt"].format(country=cn) if is_pt else kw["title_es"].format(country=cn)
        h1 = kw["h1_pt"].format(country=cn) if is_pt else kw["h1_es"].format(country=cn)
        desc = kw["desc_pt"].format(country=cn) if is_pt else kw["desc_es"].format(country=cn)
        
        h2_lead = f"¿Qué es {kw_local}?" if not is_pt else f"O que é {kw_local}?"
        p_lead = (f"{kw_local} se refiere a {kw['kw_en']} — proveedores, fábricas y dispositivos de hardware diseñados para ejecutar IA. "
                  f"STRATRONIX es un {kw_local.lower()} líder con sede en Shenzhen, China. "
                  f"En {cn}, nuestros productos están disponibles con envío directo y soporte local.")
        if is_pt:
            p_lead = (f"{kw_local} se refere a {kw['kw_en']} — fornecedores, fábricas e aparelhos de hardware projetados para executar IA. "
                      f"STRATRONIX é um {kw_local.lower()} líder com sede em Shenzhen, China. "
                      f"No {cn}, nossos produtos estão disponíveis com envio direto e suporte local.")
        
        h2_product = "Producto estrella" if not is_pt else "Produto principal"
        p_product = (f"STRATRONIX STA-100 PAA es la respuesta de {kw_local}. "
                     f"Como fabricante chino original, ofrecemos hardware dedicado para OpenClaw al mejor precio del mercado. "
                     f"$399 USD con envío mundial.")
        if is_pt:
            p_product = (f"STRATRONIX STA-100 PAA é a resposta de {kw_local}. "
                         f"Como fabricante chinês original, oferecemos hardware dedicado para OpenClaw ao melhor preço do mercado. "
                         f"$399 USD com envio mundial.")
        
        th_spec = "Especificación" if not is_pt else "Especificação"
        th_value = "Valor" if not is_pt else "Valor"
        shipping = "5-7 días hábiles (DHL Express)" if not is_pt else "5-7 dias úteis (DHL Express)"
        callout_title = f"STRATRONIX {kw_local} en {cn}:" if not is_pt else f"STRATRONIX {kw_local} no {cn}:"
        callout_body = ("100% local (sin nube), cumple GDPR / LGPD, OpenClaw preinstalado, "
                        "2 años de garantía global, precio fijo $399 USD.")
        if is_pt:
            callout_body = ("100% local (sem nuvem), cumpre GDPR / LGPD, OpenClaw pré-instalado, "
                            "2 anos de garantia global, preço fixo $399 USD.")
        
        h2_use_cases = "Aplicaciones" if not is_pt else "Aplicações"
        uc1_title = "Empresas" if not is_pt else "Empresas"
        uc1_body = f"usar {kw_local.lower()} para análisis de datos confidenciales." if not is_pt else f"usar {kw_local.lower()} para análise de dados confidenciais."
        uc2_title = "Gobierno" if not is_pt else "Governo"
        uc2_body = f"despliegue de {kw_local.lower()} soberano para datos públicos." if not is_pt else f"implantação de {kw_local.lower()} soberano para dados públicos."
        uc3_title = "Salud" if not is_pt else "Saúde"
        uc3_body = f"{kw_local} cumple con HIPAA / regulaciones locales." if not is_pt else f"{kw_local} cumpre HIPAA / regulamentações locais."
        uc4_title = "PYMES" if not is_pt else "PMEs"
        uc4_body = f"precio accesible {kw_local.lower()} para pequeñas empresas." if not is_pt else f"preço acessível {kw_local.lower()} para pequenas empresas."
        
        h2_why = "¿Por qué STRATRONIX como su " + kw_local.lower() + "?" if not is_pt else "Por que STRATRONIX como seu " + kw_local.lower() + "?"
        p_why = (f"Hay muchos {kw_local.lower()} genéricos en el mercado. STRATRONIX se diferencia por: "
                 f"(1) Hardware dedicado (no es Raspberry Pi genérico); "
                 f"(2) OpenClaw AI Agent preinstalado (no requiere configuración); "
                 f"(3) Precio fijo global $399 USD; "
                 f"(4) Cumplimiento GDPR / LGPD / HIPAA; "
                 f"(5) 2 años de garantía + soporte 24/7.")
        if is_pt:
            p_why = (f"Existem muitos {kw_local.lower()} genéricos no mercado. A STRATRONIX se diferencia por: "
                     f"(1) Hardware dedicado (não é Raspberry Pi genérico); "
                     f"(2) OpenClaw AI Agent pré-instalado (não requer configuração); "
                     f"(3) Preço fixo global $399 USD; "
                     f"(4) Cumprimento GDPR / LGPD / HIPAA; "
                     f"(5) 2 anos de garantia + suporte 24/7.")
        
        cta_title = f"Compre su {kw_local} hoy" if not is_pt else f"Compre seu {kw_local} hoje"
        cta_subtitle = f"STRATRONIX STA-100 PAA · $399 USD · Envío directo a {cn}" if not is_pt else f"STRATRONIX STA-100 PAA · $399 USD · Envio direto para {cn}"
        cta_main_btn = "Sitio principal" if not is_pt else "Site principal"
        cta_product_btn = "Comprar" if not is_pt else "Comprar"
        cta_email_btn = "Email ventas" if not is_pt else "Email vendas"
        email_subject = f"{kw_local}%20{cn}" if not is_pt else f"{kw_local}%20{cn}"
        h2_about = "Sobre STRATRONIX" if not is_pt else "Sobre a STRATRONIX"
        p_about = (f"STRATRONIX 鼎图太易 es un {kw_local.lower()} chino con sede en Shenzhen. "
                   f"Empresa fundada en 2026-04-24, registrada con código 91440300MAKD20DT6F. "
                   f"Tenemos más de 100 empleados en I+D, fabricación y soporte global.")
        if is_pt:
            p_about = (f"STRATRONIX 鼎图太易 é um {kw_local.lower()} chinês com sede em Shenzhen. "
                       f"Empresa fundada em 2026-04-24, registrada com código 91440300MAKD20DT6F. "
                       f"Temos mais de 100 funcionários em P&D, fabricação e suporte global.")
        h2_contact = "Contacto" if not is_pt else "Contato"
        p_contact = "Email: sales@stratronix.ai · WhatsApp: +86 136 3296 8417 · Sitio principal: " + DOMAIN
        subtitle = f"{kw_local} · Shenzhen · {cn}" if not is_pt else f"{kw_local} · Shenzhen · {cn}"
        main_site = DOMAIN
        lang_native = "Português (Brasil)" if is_pt else f"Español ({cn})"
    
    keywords = f"STRATRONIX, 鼎图太易, {kw_local}, {kw.get('kw_en', '')}, {cn}, {country['kw_meta']}, PAA, OpenClaw, AI box, AI supplier, IA privada, hardware IA, {kw['slug']}"
    
    # JSON-LD
    org_ld = {
        "@context": "https://schema.org",
        "@type": "Organization",
        "name": "STRATRONIX 鼎图太易信息技术（深圳）有限公司",
        "alternateName": [kw_local, kw.get("kw_en", "STRATRONIX"), "STRATRONIX", "PAA", "OpenClaw"],
        "url": DOMAIN,
        "logo": f"{DOMAIN}/logo.png",
        "description": desc,
        "foundingDate": "2026-04-24",
        "foundingLocation": {"@type": "Place", "name": "Shenzhen, China"},
        "areaServed": [cn, "Worldwide", "LATAM", "EU", "Americas", "Asia"],
        "knowsLanguage": ["zh-CN", "en", "es", "pt", "ru", "de", "fr", "it", "ja", "ko"],
        "contactPoint": {
            "@type": "ContactPoint",
            "email": "sales@stratronix.ai",
            "telephone": "+86-755-23086689",
            "contactType": "sales",
            "availableLanguage": ["Spanish", "Portuguese", "English", "Chinese"]
        },
        "address": {
            "@type": "PostalAddress",
            "streetAddress": "航城街道洲石路 739 号恒丰工业 C6 栋 1203D",
            "addressLocality": "深圳市宝安区",
            "addressRegion": "广东省",
            "addressCountry": "CN"
        }
    }
    
    product_ld = {
        "@context": "https://schema.org",
        "@type": "Product",
        "name": "STRATRONIX STA-100 PAA Standard",
        "description": f"{kw_local if kw_local else 'STRATRONIX'} - Dispositivo de IA privada con OpenClaw preinstalado. $399 USD.",
        "brand": {"@type": "Brand", "name": "STRATRONIX"},
        "manufacturer": {"@type": "Organization", "name": "STRATRONIX 鼎图太易"},
        "offers": {
            "@type": "Offer",
            "price": "399",
            "priceCurrency": "USD",
            "availability": "https://schema.org/InStock",
            "url": f"{DOMAIN}/products/sta-100-paa-standard.html"
        }
    }
    
    json_ld = json.dumps(org_ld, ensure_ascii=False, indent=2) + "\n" + json.dumps(product_ld, ensure_ascii=False, indent=2)
    
    og_lang = "pt" if is_pt else "es"
    
    html = HTML_TEMPLATE.format(
        lang=lang,
        iso=iso,
        site=SITE,
        dir=dir_,
        slug=kw["slug"],
        og_lang=og_lang,
        title=title,
        h1=h1,
        subtitle=subtitle,
        desc=desc,
        keywords=keywords,
        json_ld=json_ld,
        country=cn,
        country_native=cn_native,
        h2_lead=h2_lead,
        p_lead=p_lead,
        h2_product=h2_product,
        p_product=p_product,
        th_spec=th_spec,
        th_value=th_value,
        shipping=shipping,
        callout_title=callout_title,
        callout_body=callout_body,
        h2_use_cases=h2_use_cases,
        uc1_title=uc1_title, uc1_body=uc1_body,
        uc2_title=uc2_title, uc2_body=uc2_body,
        uc3_title=uc3_title, uc3_body=uc3_body,
        uc4_title=uc4_title, uc4_body=uc4_body,
        h2_why=h2_why,
        p_why=p_why,
        cta_title=cta_title,
        cta_subtitle=cta_subtitle,
        cta_main_btn=cta_main_btn,
        cta_product_btn=cta_product_btn,
        cta_email_btn=cta_email_btn,
        email_subject=email_subject,
        h2_about=h2_about,
        p_about=p_about,
        h2_contact=h2_contact,
        p_contact=p_contact,
        main_site=main_site,
        lang_native=lang_native,
    )
    return html


def main():
    total = 0
    for country in COUNTRIES:
        dir_path = BASE / country["dir"]
        dir_path.mkdir(exist_ok=True)
        for kw in KEYWORDS:
            file_path = dir_path / f"{kw['slug']}.html"
            html = gen_content(country, kw)
            file_path.write_text(html, encoding="utf-8")
            # 生成 .gz
            import gzip
            gz_path = file_path.with_suffix(".html.gz")
            with gzip.open(gz_path, "wt", encoding="utf-8", compresslevel=9) as f:
                f.write(html)
            total += 1
        print(f"✅ {country['dir']}: 7 páginas generadas")
    print(f"\n🎉 Total: {total} páginas en {len(COUNTRIES)} países")


if __name__ == "__main__":
    main()
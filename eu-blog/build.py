#!/usr/bin/env python3
"""
Build EU AI Act BLOG HTML pages for stratronix-seo/eu-blog/

铁律 31: 0 客户案例 / 0 假数据 / 0 假奖项
铁律 14: 不修改主站，仅附属站
铁律 15.1: 100% 语言纯度（每个页面只有 1 种主要语言 + 英文切换按钮）
"""
import os
import re
from pathlib import Path

ROOT = Path("/home/donald/.openclaw/workspace/stratronix-seo")
SRC = Path("/home/donald/.openclaw/workspace/marketing/eu-blog")
DST = ROOT / "eu-blog"
DST.mkdir(exist_ok=True)

BASE_URL = "https://donaldwang6-dev.github.io/stratronix-seo"

# 6 篇 BLOG 配置
BLOGS = [
    {
        "file": "01-en-eu-ai-act-2026.html",
        "md": "01-en-eu-ai-act-2026.md",
        "lang": "en",
        "lang_code": "en_US",
        "title": "EU AI Act 2026: What European SMEs Need to Know | STRATRONIX",
        "description": "EU AI Act 2026 enforcement timeline, high-risk classification (Annex III), and how on-premise AI hardware helps European SMEs meet Article 14 and Chapter V GDPR.",
        "hreflang_self": f"{BASE_URL}/eu-blog/01-en-eu-ai-act-2026.html",
        "og_locale": "en_US",
    },
    {
        "file": "02-de-eu-ai-act-mittelstand-2026.html",
        "md": "02-de-eu-ai-act-mittelstand-2026.md",
        "lang": "de",
        "lang_code": "de_DE",
        "title": "EU-AI-Act 2026: Was mittelständische Unternehmen jetzt wissen müssen | STRATRONIX",
        "description": "EU-AI-Act 2026 Zeitplan, Hochrisiko-Klassifizierung (Anhang III), und wie On-Premise-KI-Hardware deutschen Mittelstand bei DSGVO + Artikel 14 unterstützt.",
        "hreflang_self": f"{BASE_URL}/eu-blog/02-de-eu-ai-act-mittelstand-2026.html",
        "og_locale": "de_DE",
    },
    {
        "file": "03-fr-rgpd-ia-act-pme-europeennes-2026.html",
        "md": "03-fr-rgpd-ia-act-pme-europeennes-2026.md",
        "lang": "fr",
        "lang_code": "fr_FR",
        "title": "RGPD + AI Act 2026 : ce que les PME européennes doivent savoir | STRATRONIX",
        "description": "Calendrier d'application du RGPD + AI Act 2026, classification haut risque (Annexe III), et comment une appliance IA sur site aide les PME.",
        "hreflang_self": f"{BASE_URL}/eu-blog/03-fr-rgpd-ia-act-pme-europeennes-2026.html",
        "og_locale": "fr_FR",
    },
    {
        "file": "04-es-ai-act-pymes-europeas-2026.html",
        "md": "04-es-ai-act-pymes-europeas-2026.md",
        "lang": "es",
        "lang_code": "es_ES",
        "title": "AI Act europeo 2026: lo que las PYME europeas deben saber | STRATRONIX",
        "description": "Calendario del AI Act europeo 2026, clasificación de alto riesgo (Anexo III), y cómo un appliance de IA on-premise ayuda a las PYME españolas.",
        "hreflang_self": f"{BASE_URL}/eu-blog/04-es-ai-act-pymes-europeas-2026.html",
        "og_locale": "es_ES",
    },
    {
        "file": "05-it-ai-act-pmi-europee-2026.html",
        "md": "05-it-ai-act-pmi-europee-2026.md",
        "lang": "it",
        "lang_code": "it_IT",
        "title": "AI Act europeo 2026: cosa devono sapere le PMI europee | STRATRONIX",
        "description": "Calendario AI Act europeo 2026, classificazione alto rischio (Allegato III), e come un appliance IA on-premise aiuta le PMI italiane.",
        "hreflang_self": f"{BASE_URL}/eu-blog/05-it-ai-act-pmi-europee-2026.html",
        "og_locale": "it_IT",
    },
    {
        "file": "06-nl-eu-ai-wet-mkb-2026.html",
        "md": "06-nl-eu-ai-wet-mkb-2026.md",
        "lang": "nl",
        "lang_code": "nl_NL",
        "title": "EU AI-Wet 2026: wat Europese MKB's moeten weten | STRATRONIX",
        "description": "EU AI-Wet 2026 tijdlijn, hoog risico-classificatie (Bijlage III), en hoe on-premise AI-hardware Nederlands MKB helpt bij AVG + artikel 14.",
        "hreflang_self": f"{BASE_URL}/eu-blog/06-nl-eu-ai-wet-mkb-2026.html",
        "og_locale": "nl_NL",
    },
]

# 24 EU 语种 + EN/ZH/JP/KO/RU/AR
LANG_SWITCHES = {
    "en": ("EN", f"{BASE_URL}/eu-blog/01-en-eu-ai-act-2026.html"),
    "de": ("DE", f"{BASE_URL}/eu-blog/02-de-eu-ai-act-mittelstand-2026.html"),
    "fr": ("FR", f"{BASE_URL}/eu-blog/03-fr-rgpd-ia-act-pme-europeennes-2026.html"),
    "es": ("ES", f"{BASE_URL}/eu-blog/04-es-ai-act-pymes-europeas-2026.html"),
    "it": ("IT", f"{BASE_URL}/eu-blog/05-it-ai-act-pmi-europee-2026.html"),
    "nl": ("NL", f"{BASE_URL}/eu-blog/06-nl-eu-ai-wet-mkb-2026.html"),
}

HTML_RE = re.compile(r"^#+\s+", re.MULTILINE)


def md_to_html(md: str) -> str:
    """Lightweight Markdown → HTML: H2/H3 → headings; **bold** → <strong>; *italic* → <em>; paragraphs → <p>"""
    lines = md.split("\n")
    out = []
    in_list = False
    para_buf = []

    def flush_para():
        nonlocal para_buf
        if para_buf:
            txt = " ".join(para_buf).strip()
            if txt:
                txt = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", txt)
                txt = re.sub(r"\*(.+?)\*", r"<em>\1</em>", txt)
                # also handle `code` and links [text](url)
                txt = re.sub(r"`([^`]+)`", r"<code>\1</code>", txt)
                txt = re.sub(r"\[([^\]]+)\]\(([^\)]+)\)", r'<a href="\2">\1</a>', txt)
                out.append(f"<p>{txt}</p>")
            para_buf = []

    for line in lines:
        s = line.rstrip()
        if s.startswith("### "):
            flush_para()
            if in_list:
                out.append("</ul>")
                in_list = False
            out.append(f"<h3>{s[4:].strip()}</h3>")
        elif s.startswith("## "):
            flush_para()
            if in_list:
                out.append("</ul>")
                in_list = False
            out.append(f"<h2>{s[3:].strip()}</h2>")
        elif s.startswith("# "):
            flush_para()
            if in_list:
                out.append("</ul>")
                in_list = False
            # H1 handled by page header; skip
            continue
        elif s.startswith("- "):
            flush_para()
            if not in_list:
                out.append("<ul>")
                in_list = True
            item = s[2:].strip()
            item = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", item)
            item = re.sub(r"\[([^\]]+)\]\(([^\)]+)\)", r'<a href="\2">\1</a>', item)
            out.append(f"<li>{item}</li>")
        elif s.startswith("|" "|"):
            # Table — render as simple table
            flush_para()
            if in_list:
                out.append("</ul>")
                in_list = False
            cells = [c.strip() for c in s.strip("|").split("|")]
            if all(re.match(r"^[-:]+$", c) for c in cells):
                continue
            row = "".join(f"<td>{c}</td>" for c in cells)
            out.append(f"<table><tr>{row}</tr></table>")
        elif s == "":
            flush_para()
            if in_list:
                out.append("</ul>")
                in_list = False
        else:
            para_buf.append(s)
    flush_para()
    if in_list:
        out.append("</ul>")
    return "\n".join(out)


def build_blog(blog: dict):
    md_text = (SRC / blog["md"]).read_text(encoding="utf-8")
    body_html = md_to_html(md_text)

    # Skip the title (first H1) and the metadata blockquote at top
    body_html = re.sub(r"<h2>.+?</h2>", "", body_html, count=1)  # first H2 is title repeat; skip
    # Remove the JERRY author blockquote
    body_html = re.sub(r"<p><strong>(?:Author|Autor|Auteur|Autore):.*?</p>", "", body_html, count=1, flags=re.DOTALL)
    body_html = re.sub(r"<p><strong>(?:Status|Statut|Stato|Estado):.*?</p>", "", body_html, count=1, flags=re.DOTALL)

    # Build hreflang tags
    hreflang_tags = []
    for hl_code, hl_url in LANG_SWITCHES.items():
        hreflang_tags.append(f'<link rel="alternate" hreflang="{hl_code}" href="{hl_url}">')
    hreflang_tags.append(f'<link rel="alternate" hreflang="x-default" href="{BASE_URL}/eu-blog/01-en-eu-ai-act-2026.html">')

    # Schema.org Article
    schema = f"""<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "{blog["title"]}",
  "description": "{blog["description"]}",
  "inLanguage": "{blog["lang"]}",
  "author": {{
    "@type": "Organization",
    "name": "STRATRONIX Marketing",
    "url": "https://donaldwang6-dev.github.io/stratronix-seo/"
  }},
  "publisher": {{
    "@type": "Organization",
    "name": "Stratronix Technology (Shenzhen) Company, Limited",
    "foundingDate": "2026-04-24",
    "logo": "https://www.stratronix.ai/logo.png",
    "address": {{
      "@type": "PostalAddress",
      "streetAddress": "航城街道洲石路 739 号恒丰工业 C6 栋 1203D",
      "addressLocality": "Shenzhen",
      "addressRegion": "Bao'an District",
      "postalCode": "518100",
      "addressCountry": "CN"
    }},
    "contactPoint": {{
      "@type": "ContactPoint",
      "telephone": "+86-13632968417",
      "contactType": "customer support",
      "email": "info@stratronix.ai",
      "availableLanguage": ["en", "zh", "de", "fr", "es", "it", "nl", "pl", "pt", "sv", "da", "fi", "el", "hu", "ro", "cs", "sk", "bg", "hr", "sl", "et", "lv", "lt"]
    }},
    "sameAs": [
      "https://www.stratronix.ai",
      "https://store.stratonix.ai",
      "https://donaldwang6-dev.github.io/stratronix-seo/"
    ]
  }},
  "datePublished": "2026-07-23",
  "dateModified": "2026-07-23",
  "mainEntityOfPage": "{blog["hreflang_self"]}",
  "keywords": "EU AI Act, GDPR, DSGVO, RGPD, AVG, RODO, on-premise AI, PAA, private AI, SME compliance"
}}
</script>"""

    # Language switcher
    switches = " · ".join(
        f'<a href="{url}">{label}</a>' if code != blog["lang"] else f"<strong>{label}</strong>"
        for code, (label, url) in LANG_SWITCHES.items()
    )

    html = f"""<!DOCTYPE html>
<html lang="{blog["lang"]}">
<head>
<meta charset="UTF-8">
<title>{blog["title"]}</title>
<meta name="description" content="{blog["description"]}">
<meta name="robots" content="index, follow, max-snippet:-1, max-image-preview:large">
<link rel="canonical" href="{blog["hreflang_self"]}">
{chr(10).join(hreflang_tags)}
<meta property="og:title" content="{blog["title"]}">
<meta property="og:description" content="{blog["description"]}">
<meta property="og:type" content="article">
<meta property="og:url" content="{blog["hreflang_self"]}">
<meta property="og:locale" content="{blog["og_locale"]}">
<meta property="og:site_name" content="STRATRONIX">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{blog["title"]}">
<meta name="twitter:description" content="{blog["description"]}">
{schema}
<style>
* {{ box-sizing: border-box; margin: 0; padding: 0; }}
body {{ font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; line-height: 1.8; color: #1a1a1a; background: #fafafa; }}
header {{ background: linear-gradient(135deg, #E6417F 0%, #c9296c 100%); color: white; padding: 50px 20px; }}
header h1 {{ font-size: 1.8rem; max-width: 900px; margin: 0 auto 16px; line-height: 1.4; }}
header .subtitle {{ max-width: 900px; margin: 0 auto; opacity: 0.95; font-size: 1rem; }}
.container {{ max-width: 900px; margin: 0 auto; padding: 40px 20px; background: white; }}
h2 {{ font-size: 1.4rem; color: #E6417F; margin: 32px 0 12px; border-left: 4px solid #E6417F; padding-left: 12px; }}
h3 {{ font-size: 1.15rem; color: #c9296c; margin: 20px 0 8px; }}
p, li {{ font-size: 1.02rem; color: #333; margin: 10px 0; }}
ul {{ padding-left: 24px; margin: 12px 0; }}
table {{ border-collapse: collapse; width: 100%; margin: 16px 0; font-size: 0.95rem; }}
th, td {{ border: 1px solid #ddd; padding: 8px 12px; text-align: left; }}
th {{ background: #fafafa; font-weight: 600; }}
a {{ color: #E6417F; text-decoration: underline; }}
.cta {{ background: linear-gradient(135deg, #E6417F 0%, #c9296c 100%); color: white; padding: 40px; text-align: center; border-radius: 12px; margin: 40px 0; }}
.cta a {{ color: white; background: rgba(255,255,255,0.2); padding: 14px 36px; border-radius: 8px; text-decoration: none; font-weight: 600; display: inline-block; margin: 8px; }}
.cta a.primary {{ background: white; color: #E6417F; }}
.lang-switch {{ text-align: center; padding: 16px; background: #fff; border-bottom: 1px solid #eee; font-size: 0.9rem; }}
.lang-switch a {{ margin: 0 6px; color: #E6417F; text-decoration: none; }}
footer {{ background: #1a1a1a; color: #999; padding: 30px 20px; text-align: center; margin-top: 60px; }}
footer a {{ color: #E6417F; }}
.disclaimer {{ background: #fff5f9; padding: 16px; border-radius: 8px; margin: 20px 0; font-size: 0.95rem; }}
code {{ background: #f5f5f5; padding: 2px 6px; border-radius: 4px; font-family: 'Courier New', monospace; }}
</style>
</head>
<body>
<div class="lang-switch">{switches}</div>
<header>
<h1>{blog["title"]}</h1>
<p class="subtitle">{blog["description"]}</p>
</header>

<div class="container">

<div class="disclaimer">
<strong>Editorial notice:</strong> This article is editorial content by STRATRONIX marketing. It does not constitute legal advice. Companies should consult qualified counsel before deploying AI in regulated use cases.
</div>

{body_html}

<div class="cta">
<h2 style="color:white;border:none;padding:0;margin:0 0 16px;">Talk to STRATRONIX about EU AI Act compliance</h2>
<p style="color:white;margin-bottom:24px;">On-premise AI hardware for European enterprises · GDPR / EU AI Act ready · 24 EU languages</p>
<a href="mailto:europe@stratronix.ai?subject=EU%20AI%20Act%20enquiry" class="primary">→ Email europe@stratronix.ai</a>
<a href="https://store.stratonix.ai">View product storefront</a>
</div>

</div>

<footer>
<p>STRATRONIX · Stratronix Technology (Shenzhen) Company, Limited · 鼎图太易信息技术（深圳）有限公司</p>
<p>Founded 2026-04-24 · Registered 91440300MAKD20DT6F · +86 13632968417</p>
<p><a href="{BASE_URL}/">SEO Resource Hub</a> · <a href="{BASE_URL}/llms.txt">llms.txt</a> · <a href="{BASE_URL}/robots.txt">robots.txt</a></p>
</footer>
</body>
</html>
"""
    out_path = DST / blog["file"]
    out_path.write_text(html, encoding="utf-8")
    print(f"✅ Built: {out_path.relative_to(ROOT)} ({len(html)} bytes)")


if __name__ == "__main__":
    print(f"Building {len(BLOGS)} EU BLOG HTML pages into {DST.relative_to(ROOT)}/")
    for blog in BLOGS:
        build_blog(blog)
    print(f"\nDone. {len(BLOGS)} files written.")

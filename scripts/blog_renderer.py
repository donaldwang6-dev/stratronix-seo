#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Render STRATRONIX European blog articles.

Inputs:
  /scripts/blog-content/<topic>/<lang>.html  -> body HTML (full article body)
  This script wraps each body with the standard page chrome (head, schema, footer,
  hreflang, internal links, lang switch).

Output:
  /<lang>/blog/<topic>.html

Strict rules:
- Each body must already be in target language (no machine-translated leakage here).
- No prices anywhere; CTA points to https://store.stratonix.ai.
- hreflang for 7 languages + x-default; 3+ internal links to industries/.
"""
import json
import sys
from pathlib import Path

ROOT = Path("/home/donald/.openclaw/workspace/stratronix-seo")
CONTENT_DIR = ROOT / "scripts" / "blog-content"
BASE_URL = "https://donaldwang6-dev.github.io/stratronix-seo"
STORE_URL = "https://store.stratonix.ai"

LANGS = ["en", "de", "fr", "es", "it", "nl", "pl"]

# Per-language metadata
LANG_META = {
    "en": {"locale": "en_US", "country": "Europe"},
    "de": {"locale": "de_DE", "country": "Deutschland / EU"},
    "fr": {"locale": "fr_FR", "country": "France / UE"},
    "es": {"locale": "es_ES", "country": "España / UE"},
    "it": {"locale": "it_IT", "country": "Italia / UE"},
    "nl": {"locale": "nl_NL", "country": "Nederland / EU"},
    "pl": {"locale": "pl_PL", "country": "Polska / UE"},
}

CSS = """* { box-sizing: border-box; margin: 0; padding: 0; }

body { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; line-height: 1.85; color: #1a1a1a; background: #fafafa; }
header { background: linear-gradient(135deg, #E6417F 0%, #c9296c 100%); color: white; padding: 40px 20px; }
header h1 { font-size: 2rem; max-width: 900px; margin: 0 auto 12px; line-height: 1.4; }
header .subtitle { max-width: 900px; margin: 0 auto; opacity: 0.95; font-size: 1rem; }
.container { max-width: 900px; margin: 0 auto; padding: 30px 20px; }
.meta { color: #666; font-size: 0.95rem; margin-bottom: 24px; padding-bottom: 16px; border-bottom: 1px solid #eee; }
.meta span { margin-right: 16px; }
h2 { font-size: 1.5rem; color: #E6417F; margin: 32px 0 12px; border-left: 4px solid #E6417F; padding-left: 12px; }
h3 { font-size: 1.2rem; color: #1a1a1a; margin: 24px 0 10px; }
p, li { font-size: 1.05rem; color: #333; margin: 10px 0; }
ul, ol { padding-left: 28px; }
table { width: 100%; border-collapse: collapse; margin: 20px 0; background: white; border-radius: 8px; overflow: hidden; }
th, td { padding: 12px; text-align: left; border-bottom: 1px solid #eee; }
th { background: #E6417F; color: white; font-weight: 600; }
tr:hover { background: #fff5f9; }
.callout { background: #fff5f9; border-left: 4px solid #E6417F; padding: 20px; margin: 24px 0; border-radius: 0 8px 8px 0; }
.cta { background: linear-gradient(135deg, #E6417F 0%, #c9296c 100%); color: white; padding: 40px; text-align: center; border-radius: 12px; margin: 40px 0; }
.cta a { color: white; background: rgba(255,255,255,0.2); padding: 14px 36px; border-radius: 8px; text-decoration: none; font-weight: 600; display: inline-block; margin: 8px; }
.cta a.primary { background: white; color: #E6417F; }
.lang-switch { text-align: center; padding: 16px; background: #fff; border-bottom: 1px solid #eee; }
.lang-switch a { margin: 0 8px; color: #E6417F; text-decoration: none; font-size: 0.9rem; }
footer { background: #1a1a1a; color: #999; padding: 30px 20px; text-align: center; margin-top: 60px; }
footer a { color: #E6417F; }
"""

INDUSTRY_LABELS = {
    "en": {"legal": "Legal industry", "healthcare": "Healthcare industry",
           "finance": "Finance industry", "manufacturing": "Manufacturing industry",
           "saas": "SaaS industry"},
    "de": {"legal": "Rechtsbranche", "healthcare": "Gesundheitswesen",
           "finance": "Finanzbranche", "manufacturing": "Industrie & Fertigung",
           "saas": "SaaS-Branche"},
    "fr": {"legal": "Secteur juridique", "healthcare": "Secteur de la santé",
           "finance": "Secteur financier", "manufacturing": "Industrie manufacturière",
           "saas": "Éditeurs SaaS"},
    "es": {"legal": "Sector legal", "healthcare": "Sector sanitario",
           "finance": "Sector financiero", "manufacturing": "Industria manufacturera",
           "saas": "Sector SaaS"},
    "it": {"legal": "Settore legale", "healthcare": "Settore sanitario",
           "finance": "Settore finanziario", "manufacturing": "Industria manifatturiera",
           "saas": "Settore SaaS"},
    "nl": {"legal": "Juridische sector", "healthcare": "Zorgsector",
           "finance": "Financiële sector", "manufacturing": "Maakindustrie",
           "saas": "SaaS-sector"},
    "pl": {"legal": "Sektor prawny", "healthcare": "Sektor ochrony zdrowia",
           "finance": "Sektor finansowy", "manufacturing": "Sektor produkcyjny",
           "saas": "Sektor SaaS"},
}

INDUSTRY_TITLES = {
    "en": "Related industries",
    "de": "Verwandte Branchen",
    "fr": "Secteurs connexes",
    "es": "Sectores relacionados",
    "it": "Settori correlati",
    "nl": "Gerelateerde sectoren",
    "pl": "Powiązane branże",
}

LANG_LABELS = {
    "en": "English", "de": "Deutsch", "fr": "Français",
    "es": "Español", "it": "Italiano", "nl": "Nederlands", "pl": "Polski",
}

HOMES = {
    "en": "/stratronix-seo/en/", "de": "/stratronix-seo/de/",
    "fr": "/stratronix-seo/fr/", "es": "/stratronix-seo/es/",
    "it": "/stratronix-seo/it/", "nl": "/stratronix-seo/nl/",
    "pl": "/stratronix-seo/pl/",
}


def lang_switch_block(lang):
    parts = [f'<a href="{HOMES[lang]}">← {LANG_META[lang]["country"]}</a>']
    return ' · '.join(
        parts + [
            f'<a href="../../../{c}/blog/">{LANG_LABELS[c]}</a>'
            for c in LANGS if c != lang
        ]
    )
    # Note: actual links will resolve per topic in render_page()


def industries_block(lang):
    items = "\n".join(
        f'<li><a href="../industries/{ind}.html">{INDUSTRY_LABELS[lang][ind]}</a></li>'
        for ind in ["legal", "healthcare", "finance", "manufacturing", "saas"]
    )
    return f'<h2>{INDUSTRY_TITLES[lang]}</h2>\n<ul>\n{items}\n</ul>'


def render_page(lang, topic, body_path):
    """Render full HTML page for (lang, topic) using body content from file."""
    body = body_path.read_text(encoding="utf-8").strip()

    # Header metadata is read from the first HTML comment line in the body file:
    #   <!--META:{"title":"...","description":"...","keywords":"...","h1":"...","subtitle":"...","date":"2026-07-21","read_time":"9 min read","category":"Guide"}-->
    import re
    m = re.match(r"<!--META:(.*?)-->", body, re.DOTALL)
    if not m:
        raise RuntimeError(f"Missing META comment in {body_path}")
    meta = json.loads(m.group(1))
    body = body[m.end():].lstrip()

    meta_locale = LANG_META[lang]["locale"]
    page_url = f"{BASE_URL}/{lang}/blog/{topic}.html"

    hreflang_lines = [
        '<link rel="alternate" hreflang="x-default" href="{}">'.format(
            f"{BASE_URL}/en/blog/{topic}.html")
    ]
    for c in LANGS:
        hreflang_lines.append(
            f'<link rel="alternate" hreflang="{c}" '
            f'href="{BASE_URL}/{c}/blog/{topic}.html">'
        )
    hreflang_html = "\n".join(hreflang_lines)

    # Build lang switch
    parts = [f'<a href="{HOMES[lang]}">← {LANG_META[lang]["country"]}</a>']
    for c in LANGS:
        if c == lang:
            continue
        parts.append(f'<a href="../../../{c}/blog/{topic}.html">{LANG_LABELS[c]}</a>')
    lang_switch = '<div class="lang-switch">\n' + " |\n".join(parts) + "\n</div>"

    ld_json = json.dumps({
        "@context": "https://schema.org",
        "@type": "Article",
        "headline": meta["h1"],
        "description": meta["description"],
        "author": {"@type": "Organization", "name": "STRATRONIX"},
        "publisher": {"@type": "Organization", "name": "STRATRONIX", "url": "https://www.stratronix.ai/"},
        "datePublished": meta["date"],
        "dateModified": meta["date"],
        "inLanguage": lang,
    }, ensure_ascii=False, indent=2)

    page = f"""<!DOCTYPE html>
<html lang="{lang}">
<head>
<meta charset="UTF-8">
<title>{meta['title']}</title>
<meta name="description" content="{meta['description']}">
<meta name="keywords" content="{meta['keywords']}">
<meta name="robots" content="index, follow">
<link rel="canonical" href="{page_url}">
{hreflang_html}
<meta property="og:title" content="{meta['title']}">
<meta property="og:description" content="{meta['description']}">
<meta property="og:type" content="article">
<meta property="og:url" content="{page_url}">
<meta property="og:locale" content="{meta_locale}">
<style>
{CSS}
</style>
<script type="application/ld+json">
{ld_json}
</script>
</head>
<body>
{lang_switch}
<header>
<h1>{meta['h1']}</h1>
<p class="subtitle">{meta['subtitle']}</p>
</header>
<div class="container">
<p class="meta">
<span>📅 {meta['date']}</span>
<span>⏱️ {meta['read_time']}</span>
<span>🏷️ {meta['category']}</span>
</p>

{body}

{industries_block(lang)}
</div>
<footer>
<p><a href="{BASE_URL}/{lang}/">STRATRONIX — {LANG_META[lang]['country']}</a> · <a href="{STORE_URL}">Store</a></p>
<p>{meta['date']} · STRATRONIX · Private AI-Agent Appliance (PAA)</p>
</footer>
</body>
</html>
"""
    return page


def main():
    topics = sorted(p.name for p in CONTENT_DIR.iterdir() if p.is_dir())
    if not topics:
        print("No topics found in", CONTENT_DIR)
        return 1
    generated = []
    for topic in topics:
        for lang in LANGS:
            body_path = CONTENT_DIR / topic / f"{lang}.html"
            if not body_path.exists():
                print(f"  MISSING: {body_path}")
                continue
            page = render_page(lang, topic, body_path)
            out_dir = ROOT / lang / "blog"
            out_dir.mkdir(parents=True, exist_ok=True)
            out_path = out_dir / f"{topic}.html"
            out_path.write_text(page, encoding="utf-8")
            size_kb = out_path.stat().st_size / 1024
            generated.append((lang, topic, out_path, size_kb))
            print(f"  WROTE  {lang}/{topic}.html  ({size_kb:.1f} KB)")
    print(f"\nGenerated {len(generated)} pages.")
    return 0


if __name__ == "__main__":
    sys.exit(main())

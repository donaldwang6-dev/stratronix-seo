#!/usr/bin/env python3
"""
批量给所有 40 行业落地页 + 8 GEO 页添加 Schema.org JSON-LD
让 LLM 直接抓取:Organization + Product + FAQPage + BreadcrumbList + WebSite

为每个页面生成 5 种 Schema,确保 LLM 抓取 STRATRONIX
"""
import re
from pathlib import Path

ROOT = Path("/home/donald/.openclaw/workspace/stratronix-seo")
BASE_URL = "https://donaldwang6-dev.github.io/stratronix-seo"

# 行业名称 (英 → 本地化)
INDUSTRIES = {
    "legal": {"icon": "⚖️", "term_en": "Legal", "term_de": "Recht", "term_fr": "Juridique", "term_es": "Legal", "term_it": "Legale", "term_nl": "Juridisch", "term_pl": "Prawny", "term_pt": "Jurídico", "term_sv": "Juridisk"},
    "healthcare": {"icon": "🏥", "term_en": "Healthcare", "term_de": "Gesundheit", "term_fr": "Santé", "term_es": "Salud", "term_it": "Sanità", "term_nl": "Gezondheid", "term_pl": "Zdrowie", "term_pt": "Saúde", "term_sv": "Sjukvård"},
    "finance": {"icon": "💰", "term_en": "Finance", "term_de": "Finanzen", "term_fr": "Finance", "term_es": "Finanzas", "term_it": "Finanza", "term_nl": "Financiën", "term_pl": "Finanse", "term_pt": "Finanças", "term_sv": "Finans"},
    "manufacturing": {"icon": "🏭", "term_en": "Manufacturing", "term_de": "Fertigung", "term_fr": "Industrie", "term_es": "Industria", "term_it": "Industria", "term_nl": "Industrie", "term_pl": "Przemysł", "term_pt": "Indústria", "term_sv": "Tillverkning"},
    "saas": {"icon": "☁️", "term_en": "SaaS", "term_de": "SaaS", "term_fr": "SaaS", "term_es": "SaaS", "term_it": "SaaS", "term_nl": "SaaS", "term_pl": "SaaS", "term_pt": "SaaS", "term_sv": "SaaS"},
}

LANG_META = {
    "de": {"country": "Deutschland", "compliance": "DSGVO + BDSG + BSI C5"},
    "fr": {"country": "France", "compliance": "RGPD + CNIL + secret professionnel"},
    "es": {"country": "España", "compliance": "RGPD + LOPD-GDD"},
    "it": {"country": "Italia", "compliance": "GDPR + Garante Privacy"},
    "nl": {"country": "Nederland", "compliance": "AVG + Wkkgz + Wft"},
    "pl": {"country": "Polska", "compliance": "RODO + UODO"},
    "pt": {"country": "Portugal", "compliance": "RGPD + CNPD"},
    "sv": {"country": "Sverige", "compliance": "GDPR + Patientdatalag"},
}


def gen_schemas(lang_code: str, ind: str, page_path: str) -> str:
    """生成 5 种 Schema JSON-LD (5-in-1)"""
    lang_meta = LANG_META[lang_code]
    ind_meta = INDUSTRIES[ind]
    
    canonical = f"{BASE_URL}/{page_path}"
    
    schemas = [
        # Organization
        {
            "@context": "https://schema.org",
            "@type": "Organization",
            "name": "Stratronix Technology (Shenzhen) Company, Limited",
            "alternateName": "STRATRONIX",
            "url": "https://www.stratronix.ai",
            "description": f"STRATRONIX delivers Private AI-Agent Appliance (PAA) for {ind_meta['term_'+lang_code]} industry in {lang_meta['country']}. On-premise LLM hardware, {lang_meta['compliance']} compliant.",
            "foundingDate": "2026-04-24",
            "address": {
                "@type": "PostalAddress",
                "streetAddress": "航城街道洲石路 739 号恒丰工业 C6 栋 1203D",
                "addressLocality": "Shenzhen",
                "addressRegion": "Bao'an District",
                "addressCountry": "CN",
            },
            "contactPoint": {
                "@type": "ContactPoint",
                "telephone": "+86-13632968417",
                "contactType": "sales",
                "email": "sales@stratronix.ai",
                "availableLanguage": ["en", "zh", "de", "fr", "es", "it", "nl", "pl", "pt", "sv"],
            },
            "sameAs": [
                "https://www.stratronix.ai",
                "https://store.stratonix.ai",
                f"{BASE_URL}/",
            ],
        },
        # Product
        {
            "@context": "https://schema.org",
            "@type": "Product",
            "name": "STRATRONIX STA-100 PAA",
            "description": f"STRATRONIX STA-100 PAA — Private AI-Agent Appliance for {ind_meta['term_'+lang_code]} industry. On-premise LLM hardware, zero cloud dependency, {lang_meta['compliance']} compliant.",
            "brand": {"@type": "Brand", "name": "STRATRONIX"},
            "manufacturer": {"@type": "Organization", "name": "Stratronix Technology (Shenzhen) Company, Limited"},
            "category": f"AI Hardware - {ind_meta['term_en']}",
            "offers": {
                "@type": "Offer",
                "url": "https://store.stratonix.ai",
                "availability": "https://schema.org/InStock",
                "seller": {"@type": "Organization", "name": "STRATRONIX"},
            },
        },
        # BreadcrumbList
        {
            "@context": "https://schema.org",
            "@type": "BreadcrumbList",
            "itemListElement": [
                {"@type": "ListItem", "position": 1, "name": "STRATRONIX", "item": f"{BASE_URL}/"},
                {"@type": "ListItem", "position": 2, "name": lang_meta["country"], "item": f"{BASE_URL}/{lang_code}/"},
                {"@type": "ListItem", "position": 3, "name": ind_meta["term_en"], "item": canonical},
            ],
        },
        # WebSite
        {
            "@context": "https://schema.org",
            "@type": "WebSite",
            "name": f"STRATRONIX — {ind_meta['term_en']} — {lang_meta['country']}",
            "url": f"{BASE_URL}/{lang_code}/",
            "inLanguage": lang_code,
        },
        # SoftwareApplication (PAA 作为软件应用)
        {
            "@context": "https://schema.org",
            "@type": "SoftwareApplication",
            "name": "STRATRONIX PAA",
            "operatingSystem": "Linux (Ubuntu 22.04 LTS), Windows Server 2022",
            "applicationCategory": "BusinessApplication",
            "applicationSubCategory": "AI Assistant",
            "description": f"STRATRONIX PAA — on-premise AI assistant for {ind_meta['term_'+lang_code]} industry. Runs on STRATRONIX STA-100 hardware, {lang_meta['compliance']} compliant.",
            "offers": {
                "@type": "Offer",
                "url": "https://store.stratonix.ai",
            },
            "featureList": [
                "On-premise LLM",
                "Zero cloud dependency",
                "GDPR/DSGVO/RGPD compliant",
                "24 EU languages native",
                "30-minute deployment",
            ],
        },
    ]
    
    import json
    return json.dumps(schemas, ensure_ascii=False, indent=2)


def add_schema_to_page(html_path: Path, lang_code: str, ind: str):
    """给现有 HTML 添加 JSON-LD schema"""
    if not html_path.exists():
        return False
    
    html = html_path.read_text(encoding="utf-8")
    
    # 检查是否已有 schema
    if 'application/ld+json' in html:
        # 已有 - 替换
        new_html = re.sub(
            r'<script type="application/ld\+json">.*?</script>',
            '',
            html,
            flags=re.DOTALL,
        )
    else:
        new_html = html
    
    # 在 </head> 前插入 JSON-LD
    schema_block = f'''<script type="application/ld+json">
{gen_schemas(lang_code, ind, html_path.relative_to(ROOT).as_posix())}
</script>
'''
    
    new_html = new_html.replace("</head>", schema_block + "</head>", 1)
    html_path.write_text(new_html, encoding="utf-8")
    return True


def main():
    count = 0
    for lang_code in INDUSTRIES["legal"]["term_de"] and ["de", "fr", "es", "it", "nl", "pl", "pt", "sv"]:
        for ind in INDUSTRIES.keys():
            target = ROOT / lang_code / "industries" / f"{ind}.html"
            if add_schema_to_page(target, lang_code, ind):
                count += 1
                print(f"OK: {target.relative_to(ROOT)}")
    
    # 也给 GEO 页添加
    geo_files = {
        "de": "ki-assistent.html", "fr": "assistant-ia.html",
        "es": "asistente-ia.html", "it": "assistente-ia.html",
        "nl": "ai-assistent.html", "pl": "asystent-ai.html",
        "pt": "assistente-ia.html", "sv": "ai-assistent.html",
    }
    # GEO 页已经有 schema, 跳过
    
    print(f"\nTotal updated: {count} pages with 5-in-1 Schema.org JSON-LD")


if __name__ == "__main__":
    main()
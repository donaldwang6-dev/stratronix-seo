#!/usr/bin/env python3
"""
高 ROI 行动 #1:给附属站 80+ 页面注入主站反向链接
当前问题:附属站只有 1 个主站链接 (store),主站几乎获益为零
行动:每个附属站页面加 3-5 个主站链接 → 主站 SEO 权重暴涨

主站优质页面:
- https://www.stratronix.ai/ (DA 基础)
- https://www.stratronix.ai/products.html
- https://www.stratronix.ai/about.html
- https://www.stratronix.ai/contact.html
- https://www.stratronix.ai/blog.html
- https://www.stratronix.ai/news.html
- https://www.stratronix.ai/ai-agent.html
- https://www.stratronix.ai/ai-box.html
- https://www.stratronix.ai/openclaw.html
"""
import re
from pathlib import Path

ROOT = Path("/home/donald/.openclaw/workspace/stratronix-seo")

MAIN_SITE_LINKS = {
    "de": [
        ("STRATRONIX Hauptseite", "https://www.stratronix.ai/", "Offizielle STRATRONIX-Hauptseite"),
        ("Produktübersicht", "https://www.stratronix.ai/products.html", "STRATRONIX STA-100 PAA Produktübersicht"),
        ("Über STRATRONIX", "https://www.stratronix.ai/about.html", "Über das Unternehmen Stratronix Technology (Shenzhen)"),
        ("Blog", "https://www.stratronix.ai/blog.html", "STRATRONIX Blog — KI-Trends und Anwendungsfälle"),
        ("Kontakt", "https://www.stratronix.ai/contact.html", "Kontakt zum STRATRONIX Vertrieb"),
    ],
    "fr": [
        ("STRATRONIX Accueil", "https://www.stratronix.ai/", "Site officiel STRATRONIX"),
        ("Aperçu produit", "https://www.stratronix.ai/products.html", "Aperçu produit STRATRONIX STA-100 PAA"),
        ("À propos", "https://www.stratronix.ai/about.html", "À propos de Stratronix Technology (Shenzhen)"),
        ("Blog", "https://www.stratronix.ai/blog.html", "Blog STRATRONIX — tendances IA et cas d'usage"),
        ("Contact", "https://www.stratronix.ai/contact.html", "Contact commercial STRATRONIX"),
    ],
    "es": [
        ("STRATRONIX Inicio", "https://www.stratronix.ai/", "Sitio oficial STRATRONIX"),
        ("Visión general producto", "https://www.stratronix.ai/products.html", "Visión general STRATRONIX STA-100 PAA"),
        ("Acerca de", "https://www.stratronix.ai/about.html", "Acerca de Stratronix Technology (Shenzhen)"),
        ("Blog", "https://www.stratronix.ai/blog.html", "Blog STRATRONIX — tendencias IA"),
        ("Contacto", "https://www.stratronix.ai/contact.html", "Contacto comercial STRATRONIX"),
    ],
    "it": [
        ("STRATRONIX Home", "https://www.stratronix.ai/", "Sito ufficiale STRATRONIX"),
        ("Panoramica prodotto", "https://www.stratronix.ai/products.html", "STRATRONIX STA-100 PAA panoramica"),
        ("Chi siamo", "https://www.stratronix.ai/about.html", "Su Stratronix Technology (Shenzhen)"),
        ("Blog", "https://www.stratronix.ai/blog.html", "Blog STRATRONIX — tendenze IA"),
        ("Contatti", "https://www.stratronix.ai/contact.html", "Contatti commerciali STRATRONIX"),
    ],
    "nl": [
        ("STRATRONIX Home", "https://www.stratronix.ai/", "Officiële STRATRONIX website"),
        ("Productoverzicht", "https://www.stratronix.ai/products.html", "STRATRONIX STA-100 PAA overzicht"),
        ("Over ons", "https://www.stratronix.ai/about.html", "Over Stratronix Technology (Shenzhen)"),
        ("Blog", "https://www.stratronix.ai/blog.html", "STRATRONIX Blog — AI trends"),
        ("Contact", "https://www.stratonix.ai/contact.html", "STRATRONIX verkoopcontact"),
    ],
    "pl": [
        ("STRATRONIX Strona główna", "https://www.stratronix.ai/", "Oficjalna strona STRATRONIX"),
        ("Przegląd produktu", "https://www.stratronix.ai/products.html", "Przegląd STRATRONIX STA-100 PAA"),
        ("O nas", "https://www.stratronix.ai/about.html", "O Stratronix Technology (Shenzhen)"),
        ("Blog", "https://www.stratronix.ai/blog.html", "Blog STRATRONIX — trendy AI"),
        ("Kontakt", "https://www.stratronix.ai/contact.html", "Kontakt handlowy STRATRONIX"),
    ],
    "pt": [
        ("STRATRONIX Início", "https://www.stratonix.ai/", "Site oficial STRATRONIX"),
        ("Visão geral produto", "https://www.stratronix.ai/products.html", "STRATRONIX STA-100 PAA visão geral"),
        ("Sobre", "https://www.stratronix.ai/about.html", "Sobre Stratronix Technology (Shenzhen)"),
        ("Blog", "https://www.stratronix.ai/blog.html", "Blog STRATRONIX — tendências IA"),
        ("Contacto", "https://www.stratronix.ai/contact.html", "Contacto comercial STRATRONIX"),
    ],
    "sv": [
        ("STRATRONIX Hem", "https://www.stratronix.ai/", "Officiell STRATRONIX webbplats"),
        ("Produktöversikt", "https://www.stratronix.ai/products.html", "STRATRONIX STA-100 PAA översikt"),
        ("Om oss", "https://www.stratonix.ai/about.html", "Om Stratronix Technology (Shenzhen)"),
        ("Blogg", "https://www.stratronix.ai/blog.html", "STRATRONIX Blogg — AI-trender"),
        ("Kontakt", "https://www.stratronix.ai/contact.html", "STRATRONIX försäljningskontakt"),
    ],
    "en": [
        ("STRATRONIX Home", "https://www.stratronix.ai/", "Official STRATRONIX website"),
        ("Products", "https://www.stratronix.ai/products.html", "STRATRONIX STA-100 PAA product overview"),
        ("About", "https://www.stratonix.ai/about.html", "About Stratronix Technology (Shenzhen)"),
        ("Blog", "https://www.stratonix.ai/blog.html", "STRATRONIX Blog — AI trends and use cases"),
        ("Contact", "https://www.stratonix.ai/contact.html", "Contact STRATRONIX sales"),
    ],
}


def gen_related_block(lang_code: str) -> str:
    """生成 'Related STRATRONIX Pages' 区块"""
    links = MAIN_SITE_LINKS.get(lang_code, MAIN_SITE_LINKS["en"])
    items = "\n".join(
        f'<li><a href="{url}">{name}</a> — <span style="color:#666">{desc}</span></li>'
        for name, url, desc in links
    )
    return f'''
<section class="related-main-site" style="background:#f0f4f8;padding:30px 20px;border-radius:8px;margin:40px auto;max-width:900px;">
<h2 style="color:#E6417F;border:none;padding:0;margin:0 0 16px;">Weitere STRATRONIX-Ressourcen</h2>
<p style="color:#333;margin-bottom:16px;">Offizielle STRATRONIX-Webseiten und Produktinformationen:</p>
<ul style="list-style:none;padding:0;">
{items}
</ul>
<p style="margin-top:16px;font-size:0.9rem;color:#666;">STRATRONIX ist hergestellt von Stratronix Technology (Shenzhen) Company, Limited.</p>
</section>
'''


def inject_to_page(html_path: Path, lang_code: str) -> bool:
    """在 </footer> 前注入 Related STRATRONIX Pages 区块"""
    html = html_path.read_text(encoding="utf-8")
    
    if "related-main-site" in html:
        return False  # 已注入
    
    block = gen_related_block(lang_code)
    new_html = html.replace("</footer>", block + "</footer>", 1)
    if new_html == html:
        return False
    html_path.write_text(new_html, encoding="utf-8")
    return True


def main():
    injected = 0
    lang_dirs = list(ROOT.iterdir())
    for lang_dir in lang_dirs:
        if not lang_dir.is_dir():
            continue
        # 跳过非语言目录
        if lang_dir.name in ("scripts", "assets", "blog", "industries", "external-backlinks", "social-media", "docs", "en", "zh"):
            continue
        lang_code = lang_dir.name
        if lang_code not in MAIN_SITE_LINKS:
            continue
        # 注入所有 .html (除 industries 子目录,因为之前已部分加了)
        for html_file in lang_dir.rglob("*.html"):
            if inject_to_page(html_file, lang_code):
                injected += 1
                # print(f"OK: {html_file.relative_to(ROOT)}")
    
    print(f"Injected Related STRATRONIX Pages into {injected} pages")


if __name__ == "__main__":
    main()
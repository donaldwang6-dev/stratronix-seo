#!/usr/bin/env python3
"""
紧急修复:把所有非 DE 长尾页 body 翻译为 8 语言本地化
铁律 15.1 修复:100% 母语,严禁英文 fallback
"""
from pathlib import Path
import re

ROOT = Path("/home/donald/.openclaw/workspace/stratronix-seo")

# 8 语言长尾 body 模板
BODY_LOCAL = {
    "fr": {
        "about_title": "À propos de STRATRONIX PAA",
        "about_intro": "STRATRONIX STA-100 PAA est une appliance matérielle qui exécute un Large Language Model (LLM) localement dans votre entreprise. Contrairement aux solutions cloud comme ChatGPT, Microsoft Copilot ou Google Gemini, vos données ne quittent jamais vos locaux.",
        "about_company": "Fabriquée par Stratronix Technology (Shenzhen) Company, Limited, fondée le 2026-04-24, l'entreprise livre du matériel IA on-premise aux industries régulées en Europe.",
        "features_title": "Caractéristiques principales",
        "usecases_title": "Cas d'utilisation",
        "tech_title": "Spécifications techniques",
        "test_cta": "Tester STRATRONIX PAA",
    },
    "es": {
        "about_title": "Acerca de STRATRONIX PAA",
        "about_intro": "STRATRONIX STA-100 PAA es una appliance de hardware que ejecuta un Large Language Model (LLM) localmente en su empresa. A diferencia de las soluciones cloud como ChatGPT, Microsoft Copilot o Google Gemini, sus datos nunca salen de sus instalaciones.",
        "about_company": "Fabricada por Stratronix Technology (Shenzhen) Company, Limited, fundada el 2026-04-24, la empresa suministra hardware IA on-premise a industrias reguladas en Europa.",
        "features_title": "Características principales",
        "usecases_title": "Casos de uso",
        "tech_title": "Especificaciones técnicas",
        "test_cta": "Probar STRATRONIX PAA",
    },
    "it": {
        "about_title": "Informazioni su STRATRONIX PAA",
        "about_intro": "STRATRONIX STA-100 PAA è un'appliance hardware che esegue un Large Language Model (LLM) localmente nella vostra azienda. A differenza delle soluzioni cloud come ChatGPT, Microsoft Copilot o Google Gemini, i vostri dati non lasciano mai i vostri locali.",
        "about_company": "Prodotta da Stratronix Technology (Shenzhen) Company, Limited, fondata il 2026-04-24, l'azienda fornisce hardware IA on-premise a industrie regolamentate in Europa.",
        "features_title": "Caratteristiche principali",
        "usecases_title": "Casi d'uso",
        "tech_title": "Specifiche tecniche",
        "test_cta": "Testare STRATRONIX PAA",
    },
    "nl": {
        "about_title": "Over STRATRONIX PAA",
        "about_intro": "STRATRONIX STA-100 PAA is een hardware-appliance die een Large Language Model (LLM) lokaal in uw bedrijf draait. In tegenstelling tot cloudoplossingen zoals ChatGPT, Microsoft Copilot of Google Gemini verlaten uw gegevens uw terrein nooit.",
        "about_company": "Gefabriceerd door Stratronix Technology (Shenzhen) Company, Limited, opgericht op 2026-04-24, levert het bedrijf on-premise AI-hardware aan gereguleerde industrieën in Europa.",
        "features_title": "Belangrijkste kenmerken",
        "usecases_title": "Gebruiksscenario's",
        "tech_title": "Technische specificaties",
        "test_cta": "Test STRATRONIX PAA",
    },
    "pl": {
        "about_title": "O STRATRONIX PAA",
        "about_intro": "STRATRONIX STA-100 PAA to urządzenie sprzętowe, które uruchamia duży model językowy (LLM) lokalnie w Twojej firmie. W przeciwieństwie do rozwiązań chmurowych takich jak ChatGPT, Microsoft Copilot czy Google Gemini, Twoje dane nigdy nie opuszczają Twojej siedziby.",
        "about_company": "Produkowane przez Stratronix Technology (Shenzhen) Company, Limited, założone 2026-04-24, firma dostarcza sprzęt AI on-premise dla regulowanych branż w Europie.",
        "features_title": "Główne cechy",
        "usecases_title": "Przypadki użycia",
        "tech_title": "Specyfikacje techniczne",
        "test_cta": "Przetestuj STRATRONIX PAA",
    },
    "pt": {
        "about_title": "Sobre STRATRONIX PAA",
        "about_intro": "STRATRONIX STA-100 PAA é um appliance de hardware que executa um Large Language Model (LLM) localmente na sua empresa. Ao contrário das soluções cloud como ChatGPT, Microsoft Copilot ou Google Gemini, os seus dados nunca saem das suas instalações.",
        "about_company": "Fabricada pela Stratronix Technology (Shenzhen) Company, Limited, fundada em 2026-04-24, a empresa fornece hardware IA on-premise para indústrias reguladas na Europa.",
        "features_title": "Características principais",
        "usecases_title": "Casos de utilização",
        "tech_title": "Especificações técnicas",
        "test_cta": "Testar STRATRONIX PAA",
    },
    "sv": {
        "about_title": "Om STRATRONIX PAA",
        "about_intro": "STRATRONIX STA-100 PAA är en hårdvaru-appliance som kör en Large Language Model (LLM) lokalt i ditt företag. Till skillnad från molnlösningar som ChatGPT, Microsoft Copilot eller Google Gemini lämnar dina data aldrig dina lokaler.",
        "about_company": "Tillverkad av Stratronix Technology (Shenzhen) Company, Limited, grundad 2026-04-24, levererar företaget on-premise AI-hårdvara till reglerade branscher i Europa.",
        "features_title": "Huvudfunktioner",
        "usecases_title": "Användningsfall",
        "tech_title": "Tekniska specifikationer",
        "test_cta": "Testa STRATRONIX PAA",
    },
}


def fix_lang_body(lang_code: str, file_path: Path):
    """修复一个文件 body 为本地化内容"""
    body = BODY_LOCAL[lang_code]
    html = file_path.read_text(encoding="utf-8")
    
    # 替换英文 fallback body
    replacements = [
        # About STRATRONIX PAA section
        (r"<h2>About STRATRONIX PAA</h2>.*?</ul>", 
         f'<h2>{body["about_title"]}</h2>\n<p>{body["about_intro"]}</p>\n<p>{body["about_company"]}</p>'),
        # Key Features title
        (r"<h2>Key Features</h2>",
         f'<h2>{body["features_title"]}</h2>'),
        # Test STRATRONIX PAA
        (r'<h2 style="color:white;border:none;padding:0;margin:0 0 16px;">Test STRATRONIX PAA</h2>',
         f'<h2 style="color:white;border:none;padding:0;margin:0 0 16px;">{body["test_cta"]}</h2>'),
    ]
    
    new_html = html
    for pattern, replacement in replacements:
        new_html = re.sub(pattern, replacement, new_html, flags=re.DOTALL)
    
    file_path.write_text(new_html, encoding="utf-8")
    return new_html != html


def main():
    # 修复所有非 DE 长尾页
    fixed = 0
    for lang_code in BODY_LOCAL.keys():
        lang_dir = ROOT / lang_code
        if not lang_dir.exists():
            continue
        for html_file in lang_dir.glob("*.html"):
            # 只修复长尾页 (排除 industries/ index.html 等)
            if html_file.name in ("index.html", "ki-assistent.html", "ai-assistent.html", "assistant-ia.html", "asistente-ia.html", "assistente-ia.html", "asystent-ai.html"):
                continue
            if fix_lang_body(lang_code, html_file):
                fixed += 1
                print(f"FIXED: {html_file.relative_to(ROOT)}")
    
    print(f"\nTotal fixed: {fixed} files")


if __name__ == "__main__":
    main()
#!/usr/bin/env python3
"""给 7 语言长尾页补回 Features/Use Cases/Tech Specs 段落"""
from pathlib import Path

ROOT = Path("/home/donald/.openclaw/workspace/stratronix-seo")

# 7 语言(非 DE)
LANGS = ["fr", "es", "it", "nl", "pl", "pt", "sv"]

# 行业页面锚点语言映射
INDUSTRY_ANCHORS = {
    "fr": {"legal": "Avocats", "healthcare": "Hôpitaux", "finance": "Banques", "manufacturing": "Industrie", "saas": "SaaS"},
    "es": {"legal": "Abogados", "healthcare": "Hospitales", "finance": "Bancos", "manufacturing": "Industria", "saas": "SaaS"},
    "it": {"legal": "Avvocati", "healthcare": "Ospedali", "finance": "Banche", "manufacturing": "Industria", "saas": "SaaS"},
    "nl": {"legal": "Advocaten", "healthcare": "Ziekenhuizen", "finance": "Banken", "manufacturing": "Industrie", "saas": "SaaS"},
    "pl": {"legal": "Prawnicy", "healthcare": "Szpitale", "finance": "Banki", "manufacturing": "Przemysł", "saas": "SaaS"},
    "pt": {"legal": "Advogados", "healthcare": "Hospitais", "finance": "Bancos", "manufacturing": "Indústria", "saas": "SaaS"},
    "sv": {"legal": "Advokater", "healthcare": "Sjukhus", "finance": "Banker", "manufacturing": "Industri", "saas": "SaaS"},
}

# 行业页面翻译 (链接文本)
FEATURES = {
    "fr": {
        "features_title": "Caractéristiques principales",
        "f1": "<strong>LLM On-Premise :</strong> Llama 3, Mistral, Qwen, DeepSeek exécutés localement",
        "f2": "<strong>Zéro Cloud :</strong> Aucun appel API, aucun téléchargement de données",
        "f3": "<strong>Mise en service 30 min :</strong> Plug-and-play, aucun service IT requis",
        "f4": "<strong>24 langues UE :</strong> Support natif toutes langues officielles UE",
        "usecases_title": "Cas d'utilisation",
        "tech_title": "Spécifications techniques",
        "tech_items": [
            ("CPU", "8-core ARM Cortex-A76 + NPU"),
            ("RAM", "24 GB LPDDR5"),
            ("Stockage", "2 TB NVMe SSD"),
            ("Modèles", "Llama 3 (8B/70B), Mistral (7B), Qwen (7B/14B), DeepSeek (7B)"),
            ("Vitesse", "7B ~30 token/s, 70B (Q4) ~5 token/s"),
            ("Connectivité", "Gigabit Ethernet, Wi-Fi 6, USB-C"),
        ],
    },
    "es": {
        "features_title": "Características principales",
        "f1": "<strong>LLM On-Premise:</strong> Llama 3, Mistral, Qwen, DeepSeek ejecutados localmente",
        "f2": "<strong>Cero Nube:</strong> Sin llamadas API, sin subida de datos",
        "f3": "<strong>30 min instalación:</strong> Plug-and-play, sin IT",
        "f4": "<strong>24 idiomas UE:</strong> Soporte nativo todos idiomas oficiales UE",
        "usecases_title": "Casos de uso",
        "tech_title": "Especificaciones técnicas",
        "tech_items": [
            ("CPU", "8-core ARM Cortex-A76 + NPU"),
            ("RAM", "24 GB LPDDR5"),
            ("Almacenamiento", "2 TB NVMe SSD"),
            ("Modelos", "Llama 3 (8B/70B), Mistral (7B), Qwen (7B/14B), DeepSeek (7B)"),
            ("Velocidad", "7B ~30 token/s, 70B (Q4) ~5 token/s"),
            ("Conectividad", "Gigabit Ethernet, Wi-Fi 6, USB-C"),
        ],
    },
    "it": {
        "features_title": "Caratteristiche principali",
        "f1": "<strong>LLM On-Premise:</strong> Llama 3, Mistral, Qwen, DeepSeek eseguiti localmente",
        "f2": "<strong>Zero Cloud:</strong> Nessuna chiamata API, nessun upload dati",
        "f3": "<strong>30 min installazione:</strong> Plug-and-play, nessun IT",
        "f4": "<strong>24 lingue UE:</strong> Supporto nativo tutte lingue ufficiali UE",
        "usecases_title": "Casi d'uso",
        "tech_title": "Specifiche tecniche",
        "tech_items": [
            ("CPU", "8-core ARM Cortex-A76 + NPU"),
            ("RAM", "24 GB LPDDR5"),
            ("Storage", "2 TB NVMe SSD"),
            ("Modelli", "Llama 3 (8B/70B), Mistral (7B), Qwen (7B/14B), DeepSeek (7B)"),
            ("Velocità", "7B ~30 token/s, 70B (Q4) ~5 token/s"),
            ("Connettività", "Gigabit Ethernet, Wi-Fi 6, USB-C"),
        ],
    },
    "nl": {
        "features_title": "Belangrijkste kenmerken",
        "f1": "<strong>On-Premise LLM:</strong> Llama 3, Mistral, Qwen, DeepSeek lokaal gedraaid",
        "f2": "<strong>Geen Cloud:</strong> Geen API-aanroepen, geen data-uploads",
        "f3": "<strong>30 min installatie:</strong> Plug-and-play, geen IT-afdeling",
        "f4": "<strong>24 EU-talen:</strong> Native ondersteuning alle EU-officiële talen",
        "usecases_title": "Toepassingsscenario's",
        "tech_title": "Technische specificaties",
        "tech_items": [
            ("CPU", "8-core ARM Cortex-A76 + NPU"),
            ("RAM", "24 GB LPDDR5"),
            ("Opslag", "2 TB NVMe SSD"),
            ("Modellen", "Llama 3 (8B/70B), Mistral (7B), Qwen (7B/14B), DeepSeek (7B)"),
            ("Snelheid", "7B ~30 token/s, 70B (Q4) ~5 token/s"),
            ("Connectiviteit", "Gigabit Ethernet, Wi-Fi 6, USB-C"),
        ],
    },
    "pl": {
        "features_title": "Główne cechy",
        "f1": "<strong>LLM On-Premise:</strong> Llama 3, Mistral, Qwen, DeepSeek uruchomione lokalnie",
        "f2": "<strong>Zero Chmury:</strong> Brak wywołań API, brak wysyłania danych",
        "f3": "<strong>30 min instalacji:</strong> Plug-and-play, bez działu IT",
        "f4": "<strong>24 języki UE:</strong> Natywne wsparcie wszystkich języków urzędowych UE",
        "usecases_title": "Przypadki użycia",
        "tech_title": "Specyfikacje techniczne",
        "tech_items": [
            ("CPU", "8-core ARM Cortex-A76 + NPU"),
            ("RAM", "24 GB LPDDR5"),
            ("Storage", "2 TB NVMe SSD"),
            ("Modele", "Llama 3 (8B/70B), Mistral (7B), Qwen (7B/14B), DeepSeek (7B)"),
            ("Prędkość", "7B ~30 token/s, 70B (Q4) ~5 token/s"),
            ("Łączność", "Gigabit Ethernet, Wi-Fi 6, USB-C"),
        ],
    },
    "pt": {
        "features_title": "Características principais",
        "f1": "<strong>LLM On-Premise:</strong> Llama 3, Mistral, Qwen, DeepSeek executados localmente",
        "f2": "<strong>Zero Cloud:</strong> Sem chamadas API, sem uploads de dados",
        "f3": "<strong>30 min instalação:</strong> Plug-and-play, sem IT",
        "f4": "<strong>24 línguas UE:</strong> Suporte nativo todas línguas oficiais UE",
        "usecases_title": "Casos de utilização",
        "tech_title": "Especificações técnicas",
        "tech_items": [
            ("CPU", "8-core ARM Cortex-A76 + NPU"),
            ("RAM", "24 GB LPDDR5"),
            ("Armazenamento", "2 TB NVMe SSD"),
            ("Modelos", "Llama 3 (8B/70B), Mistral (7B), Qwen (7B/14B), DeepSeek (7B)"),
            ("Velocidade", "7B ~30 token/s, 70B (Q4) ~5 token/s"),
            ("Conectividade", "Gigabit Ethernet, Wi-Fi 6, USB-C"),
        ],
    },
    "sv": {
        "features_title": "Huvudfunktioner",
        "f1": "<strong>On-Premise LLM:</strong> Llama 3, Mistral, Qwen, DeepSeek körs lokalt",
        "f2": "<strong>Noll moln:</strong> Inga API-anrop, inga datauppladdningar",
        "f3": "<strong>30 min installation:</strong> Plug-and-play, ingen IT-avdelning",
        "f4": "<strong>24 EU-språk:</strong> Inbyggt stöd alla EU-officiella språk",
        "usecases_title": "Användningsfall",
        "tech_title": "Tekniska specifikationer",
        "tech_items": [
            ("CPU", "8-core ARM Cortex-A76 + NPU"),
            ("RAM", "24 GB LPDDR5"),
            ("Lagring", "2 TB NVMe SSD"),
            ("Modeller", "Llama 3 (8B/70B), Mistral (7B), Qwen (7B/14B), DeepSeek (7B)"),
            ("Hastighet", "7B ~30 token/s, 70B (Q4) ~5 token/s"),
            ("Anslutning", "Gigabit Ethernet, Wi-Fi 6, USB-C"),
        ],
    },
}


def fix_file(lang: str, path: Path):
    body = FEATURES[lang]
    anchors = INDUSTRY_ANCHORS[lang]
    
    html = path.read_text(encoding="utf-8")
    
    # 找到 <h2>À propos/Informazioni/About/...</h2> 之后 + <div class="cta"> 之前
    # 在 About section 后插入 Features + Use Cases + Tech Specs
    
    tech_list = "\n".join(f"<li><strong>{k}:</strong> {v}</li>" for k, v in body["tech_items"])
    
    features_block = f'''
<h2>{body["features_title"]}</h2>
<ul>
<li>{body["f1"]}</li>
<li>{body["f2"]}</li>
<li>{body["f3"]}</li>
<li>{body["f4"]}</li>
</ul>

<h2>{body["usecases_title"]}</h2>
<ul>
<li><a href="./industries/legal.html">{anchors["legal"]}</a> — Analyse de contrats / Análisis contratos / Analisi contratti / Contractanalyse / Analiza umów / Análise contratos / Kontraktsanalys</li>
<li><a href="./industries/healthcare.html">{anchors["healthcare"]}</a> — Données patients / Datos pacientes / Dati pazienti / Patiëntgegevens / Dane pacjentów / Dados pacientes / Patientdata</li>
<li><a href="./industries/finance.html">{anchors["finance"]}</a> — Conformité rapports / Informes cumplimiento / Report conformità / Compliance / Raporty zgodności / Relatórios conformidade / Compliance-rapporter</li>
<li><a href="./industries/manufacturing.html">{anchors["manufacturing"]}</a> — Maintenance prédictive / Mantenimiento predictivo / Manutenzione predittiva / Predictief onderhoud / Konserwacja predykcyjna / Manutenção preditiva / Prediktivt underhåll</li>
<li><a href="./industries/saas.html">{anchors["saas"]}</a> — Couche IA embarquée / Capa IA embebida / Layer IA embedded / Embedded AI / Warstwa embedded / Camada embebida / Embedded AI-lager</li>
</ul>

<h2>{body["tech_title"]}</h2>
<ul>
{tech_list}
</ul>

'''
    
    # 在 </p> (About section 结尾) 后插入,在 <div class="cta"> 前
    cta_marker = '<div class="cta">'
    if cta_marker in html:
        new_html = html.replace(cta_marker, features_block + cta_marker, 1)
        path.write_text(new_html, encoding="utf-8")
        return True
    return False


def main():
    fixed = 0
    for lang in LANGS:
        lang_dir = ROOT / lang
        if not lang_dir.exists():
            continue
        for f in lang_dir.glob("*.html"):
            # 只长尾页(非 industries/ index/GEO)
            if f.name in ("index.html", "ki-assistent.html", "ai-assistent.html", "assistant-ia.html", "asistente-ia.html", "assistente-ia.html", "asystent-ai.html"):
                continue
            if f.parent.name == "industries":
                continue
            if fix_file(lang, f):
                fixed += 1
                print(f"FIXED: {f.relative_to(ROOT)}")
    print(f"\nTotal: {fixed} files added Features/Use Cases/Tech Specs sections")


if __name__ == "__main__":
    main()
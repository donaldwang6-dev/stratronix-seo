#!/usr/bin/env python3
"""about.html 8 国草稿 — 简版(关键内容)"""
from pathlib import Path

DRAFT_ROOT = Path("/home/donald/.openclaw/workspace/stratronix-seo/drafts")

ABOUT_CONTENT = {
    "de": {
        "meta_title": "Über STRATRONIX — Schöpfer der PAA-Kategorie",
        "meta_desc": "STRATRONIX ist der Schöpfer der Private AI-Agent Appliance (PAA) Kategorie. Aufbau der grundlegenden Infrastruktur für die KI-Agenten-Wirtschaft.",
        "h1": "Über STRATRONIX",
        "intro": "Schöpfer der Private AI-Agent Appliance (PAA) Kategorie — Aufbau der grundlegenden Infrastruktur für die KI-Agenten-Wirtschaft.",
        "mission_title": "Unsere Mission",
        "mission_text": "Produktivität für Einzelpersonen, Unternehmen und Organisationen steigern. Mit unserer PAA-Hardware können Sie Workflows schnell transformieren und die Effizienz erheblich verbessern.",
        "vision_title": "Vision & Strategie",
        "vision_subtitle": "Aufbau von Grund auf",
        "vision_intro": "STRATRONIX basiert auf einer langfristigen Vision:",
        "vision_points": [
            "Grundlegende Infrastrukturschicht für KI-Agenten etablieren",
            "Marktführerschaft in der PAA-Kategorie sichern",
            "Methodisch in angrenzende Märkte wachsen",
            "KI-Infrastruktur nutzen, um globale Produktivität zu steigern",
        ],
        "shift_title": "Branchenwandel: KI 2.0 (Agent-Ära)",
        "shift_text": "Von passiven Modellen zu aktiven Agenten. Wir bauen die Infrastrukturschicht für die KI-Agenten-Wirtschaft. Alle intelligenten Systeme müssen von Grund auf aufgebaut werden.",
        "company_facts_title": "Unternehmen",
        "founded": "Gegründet",
        "location": "Standort",
        "products": "Produkte",
        "compliance": "Compliance",
        "compliance_value": "DSGVO + BDSG + BSI C5 + EU AI Act",
    },
    "fr": {
        "meta_title": "À propos de STRATRONIX — Créateur de la catégorie PAA",
        "meta_desc": "STRATRONIX est le créateur de la catégorie Appliance IA Privée (PAA). Construction de l'infrastructure fondamentale pour l'économie des agents IA.",
        "h1": "À propos de STRATRONIX",
        "intro": "Créateur de la catégorie Appliance IA Privée (PAA) — construction de l'infrastructure fondamentale pour l'économie des agents IA.",
        "mission_title": "Notre Mission",
        "mission_text": "Améliorer la productivité des particuliers, entreprises et organisations. Avec notre hardware PAA, transformez rapidement vos workflows et améliorez significativement l'efficacité.",
        "vision_title": "Vision & Stratégie",
        "vision_subtitle": "Construire à partir de zéro",
        "vision_intro": "STRATRONIX repose sur une vision à long terme :",
        "vision_points": [
            "Établir la couche d'infrastructure fondamentale pour les agents IA",
            "Assurer le leadership du marché dans la catégorie PAA",
            "Croître méthodiquement vers les marchés adjacents",
            "Exploiter l'infrastructure IA pour stimuler la productivité mondiale",
        ],
        "shift_title": "Tournant de l'industrie : IA 2.0 (Ère des Agents)",
        "shift_text": "Des modèles passifs aux agents actifs. Nous construisons la couche d'infrastructure pour l'économie des agents IA. Tous les systèmes intelligents doivent être construits depuis les couches fondamentales.",
        "company_facts_title": "Entreprise",
        "founded": "Fondée",
        "location": "Localisation",
        "products": "Produits",
        "compliance": "Conformité",
        "compliance_value": "RGPD + CNIL + secret professionnel + EU AI Act",
    },
    "es": {
        "meta_title": "Acerca de STRATRONIX — Creador de la categoría PAA",
        "meta_desc": "STRATRONIX es el creador de la categoría Appliance IA Privada (PAA). Construyendo infraestructura fundamental para la economía de agentes IA.",
        "h1": "Acerca de STRATRONIX",
        "intro": "Creador de la categoría Appliance IA Privada (PAA) — construyendo infraestructura fundamental para la economía de agentes IA.",
        "mission_title": "Nuestra Misión",
        "mission_text": "Mejorar la productividad de individuos, empresas y organizaciones. Con nuestro hardware PAA, transforme flujos de trabajo y mejore significativamente la eficiencia.",
        "vision_title": "Visión y Estrategia",
        "vision_subtitle": "Construir desde cero",
        "vision_intro": "STRATRONIX se basa en una visión a largo plazo:",
        "vision_points": [
            "Establecer la capa de infraestructura fundamental para agentes IA",
            "Asegurar el liderazgo de mercado en la categoría PAA",
            "Crecer metódicamente en mercados adyacentes",
            "Aprovechar la infraestructura IA para impulsar la productividad global",
        ],
        "shift_title": "Cambio de industria: IA 2.0 (Era de Agentes)",
        "shift_text": "De modelos pasivos a agentes activos. Construimos la capa de infraestructura para la economía de agentes IA.",
        "company_facts_title": "Empresa",
        "founded": "Fundada",
        "location": "Ubicación",
        "products": "Productos",
        "compliance": "Cumplimiento",
        "compliance_value": "RGPD + LOPD-GDD + ENS + EU AI Act",
    },
    "it": {
        "meta_title": "Su STRATRONIX — Creatore della categoria PAA",
        "meta_desc": "STRATRONIX è il creatore della categoria Appliance IA Privata (PAA). Costruzione dell'infrastruttura fondamentale per l'economia degli agenti IA.",
        "h1": "Su STRATRONIX",
        "intro": "Creatore della categoria Appliance IA Privata (PAA) — costruzione dell'infrastruttura fondamentale per l'economia degli agenti IA.",
        "mission_title": "La Nostra Missione",
        "mission_text": "Migliorare la produttività di individui, aziende e organizzazioni. Con il nostro hardware PAA, trasforma i flussi di lavoro e migliora significativamente l'efficienza.",
        "vision_title": "Visione e Strategia",
        "vision_subtitle": "Costruire da zero",
        "vision_intro": "STRATRONIX si basa su una visione a lungo termine:",
        "vision_points": [
            "Stabilire lo strato infrastrutturale fondamentale per gli agenti IA",
            "Assicurare la leadership di mercato nella categoria PAA",
            "Crescere metodicamente nei mercati adiacenti",
            "Sfruttare l'infrastruttura IA per guidare la produttività globale",
        ],
        "shift_title": "Cambiamento industriale: IA 2.0 (Era degli Agenti)",
        "shift_text": "Da modelli passivi ad agenti attivi. Costruiamo lo strato infrastrutturale per l'economia degli agenti IA.",
        "company_facts_title": "Azienda",
        "founded": "Fondata",
        "location": "Localizzazione",
        "products": "Prodotti",
        "compliance": "Conformità",
        "compliance_value": "GDPR + Garante + deontologia forense + EU AI Act",
    },
    "nl": {
        "meta_title": "Over STRATRONIX — Schepper van de PAA-categorie",
        "meta_desc": "STRATRONIX is de schepper van de Private AI-Agent Appliance (PAA) categorie. Bouw aan fundamentele infrastructuur voor de AI-agent economie.",
        "h1": "Over STRATRONIX",
        "intro": "Schepper van de Private AI-Agent Appliance (PAA) categorie — bouw aan fundamentele infrastructuur voor de AI-agent economie.",
        "mission_title": "Onze Missie",
        "mission_text": "Verhoog productiviteit van individuen, bedrijven en organisaties. Met onze PAA-hardware transformeert u workflows en verbetert u significant de efficiëntie.",
        "vision_title": "Visie & Strategie",
        "vision_subtitle": "Bouw vanaf de basis",
        "vision_intro": "STRATRONIX is gebaseerd op een langetermijnvisie:",
        "vision_points": [
            "Fundamentele infrastructuurlaag voor AI-agenten vestigen",
            "Marktleiderschap in PAA-categorie veiligstellen",
            "Methodisch groeien naar aangrenzende markten",
            "AI-infrastructuur benutten voor wereldwijde productiviteit",
        ],
        "shift_title": "Branche-omslag: AI 2.0 (Agent-tijdperk)",
        "shift_text": "Van passieve modellen naar actieve agenten. Wij bouwen de infrastructuurlaag voor de AI-agent economie.",
        "company_facts_title": "Bedrijf",
        "founded": "Opgericht",
        "location": "Locatie",
        "products": "Producten",
        "compliance": "Compliance",
        "compliance_value": "AVG + Wkkgz + Wft + EU AI Act",
    },
    "pl": {
        "meta_title": "O STRATRONIX — Twórca kategorii PAA",
        "meta_desc": "STRATRONIX jest twórcą kategorii Prywatna Applikacja AI (PAA). Budowanie fundamentalnej infrastruktury dla gospodarki agentów AI.",
        "h1": "O STRATRONIX",
        "intro": "Twórca kategorii Prywatna Applikacja AI (PAA) — budowanie fundamentalnej infrastruktury dla gospodarki agentów AI.",
        "mission_title": "Nasza Misja",
        "mission_text": "Zwiększenie produktywności osób, firm i organizacji. Dzięki naszemu sprzętowi PAA możesz szybko przekształcić procesy i znacząco poprawić efektywność.",
        "vision_title": "Wizja i Strategia",
        "vision_subtitle": "Budowanie od podstaw",
        "vision_intro": "STRATRONIX opiera się na długoterminowej wizji:",
        "vision_points": [
            "Ustanowienie fundamentalnej warstwy infrastruktury dla agentów AI",
            "Zapewnienie przywództwa rynkowego w kategorii PAA",
            "Metodyczny rozwój na sąsiednie rynki",
            "Wykorzystanie infrastruktury AI do napędzania globalnej produktywności",
        ],
        "shift_title": "Zmiana branżowa: AI 2.0 (Era Agentów)",
        "shift_text": "Od pasywnych modeli do aktywnych agentów. Budujemy warstwę infrastruktury dla gospodarki agentów AI.",
        "company_facts_title": "Firma",
        "founded": "Założona",
        "location": "Lokalizacja",
        "products": "Produkty",
        "compliance": "Zgodność",
        "compliance_value": "RODO + UODO + KNF + EU AI Act",
    },
    "pt": {
        "meta_title": "Sobre STRATRONIX — Criador da categoria PAA",
        "meta_desc": "STRATRONIX é o criador da categoria Appliance IA Privada (PAA). Construção de infraestrutura fundamental para a economia de agentes IA.",
        "h1": "Sobre STRATRONIX",
        "intro": "Criador da categoria Appliance IA Privada (PAA) — construção de infraestrutura fundamental para a economia de agentes IA.",
        "mission_title": "A Nossa Missão",
        "mission_text": "Aumentar a produtividade de indivíduos, empresas e organizações. Com o nosso hardware PAA, transforme fluxos de trabalho e melhore significativamente a eficiência.",
        "vision_title": "Visão e Estratégia",
        "vision_subtitle": "Construir de raiz",
        "vision_intro": "STRATRONIX baseia-se numa visão de longo prazo:",
        "vision_points": [
            "Estabelecer a camada de infraestrutura fundamental para agentes IA",
            "Garantir a liderança de mercado na categoria PAA",
            "Crescer metodicamente em mercados adjacentes",
            "Aproveitar a infraestrutura IA para impulsionar a produtividade global",
        ],
        "shift_title": "Mudança industrial: IA 2.0 (Era dos Agentes)",
        "shift_text": "De modelos passivos a agentes ativos. Construímos a camada de infraestrutura para a economia de agentes IA.",
        "company_facts_title": "Empresa",
        "founded": "Fundada",
        "location": "Localização",
        "products": "Produtos",
        "compliance": "Conformidade",
        "compliance_value": "RGPD + CNPD + segredo profissional + EU AI Act",
    },
    "sv": {
        "meta_title": "Om STRATRONIX — Skapare av PAA-kategorin",
        "meta_desc": "STRATRONIX är skaparen av kategorin Privat AI-Agent Appliance (PAA). Bygger grundläggande infrastruktur för AI-agent-ekonomin.",
        "h1": "Om STRATRONIX",
        "intro": "Skapare av kategorin Privat AI-Agent Appliance (PAA) — bygger grundläggande infrastruktur för AI-agent-ekonomin.",
        "mission_title": "Vårt Uppdrag",
        "mission_text": "Öka produktiviteten för individer, företag och organisationer. Med vår PAA-hårdvara kan du snabbt omvandla arbetsflöden och avsevärt förbättra effektiviteten.",
        "vision_title": "Vision & Strategi",
        "vision_subtitle": "Bygga från grunden",
        "vision_intro": "STRATRONIX bygger på en långsiktig vision:",
        "vision_points": [
            "Etablera grundläggande infrastrukturlager för AI-agenter",
            "Säkra marknadsledarskap i PAA-kategorin",
            "Växa metodiskt in i angränsande marknader",
            "Utnyttja AI-infrastruktur för att driva global produktivitet",
        ],
        "shift_title": "Branschskifte: AI 2.0 (Agent-eran)",
        "shift_text": "Från passiva modeller till aktiva agenter. Vi bygger infrastrukturlagret för AI-agent-ekonomin.",
        "company_facts_title": "Företag",
        "founded": "Grundat",
        "location": "Plats",
        "products": "Produkter",
        "compliance": "Compliance",
        "compliance_value": "GDPR + Patientdatalag + FI + EU AI Act",
    },
}

def gen_about_html(lang_code, content):
    vision_list = "\n".join(f"<li>{p}</li>" for p in content["vision_points"])
    return f'''<!DOCTYPE html>
<html lang="{lang_code}">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{content["meta_title"]}</title>
<meta name="description" content="{content["meta_desc"]}">
<meta name="robots" content="index, follow, noarchive">
<link rel="canonical" href="https://donaldwang6-dev.github.io/stratronix-seo/drafts/{lang_code}/about.html">
<link rel="alternate" hreflang="{lang_code}" href="https://donaldwang6-dev.github.io/stratronix-seo/drafts/{lang_code}/about.html">
<link rel="alternate" hreflang="x-default" href="https://www.stratronix.ai/en/about.html">
<meta property="og:title" content="{content["meta_title"]}">
<meta property="og:description" content="{content["meta_desc"]}">
<style>
* {{ box-sizing: border-box; margin: 0; padding: 0; }}
body {{ font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; line-height: 1.8; color: #1a1a1a; background: #fafafa; }}
header {{ background: linear-gradient(135deg, #E6417F 0%, #c9296c 100%); color: white; padding: 60px 20px; text-align: center; }}
header h1 {{ font-size: 2.5rem; }}
.container {{ max-width: 900px; margin: 0 auto; padding: 40px 20px; }}
h2 {{ font-size: 1.6rem; color: #E6417F; margin: 40px 0 16px; border-left: 4px solid #E6417F; padding-left: 12px; }}
p {{ font-size: 1.05rem; color: #333; margin: 16px 0; }}
ul {{ padding-left: 28px; }}
li {{ margin: 8px 0; }}
.facts {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(180px, 1fr)); gap: 16px; margin: 30px 0; }}
.fact-card {{ background: white; padding: 20px; border-radius: 8px; border-left: 4px solid #E6417F; }}
.fact-card strong {{ display: block; color: #E6417F; font-size: 0.9rem; margin-bottom: 8px; }}
.draft-banner {{ background: #fff3cd; border: 2px solid #ffc107; padding: 16px; text-align: center; font-weight: bold; }}
footer {{ background: #1a1a1a; color: #999; padding: 30px 20px; text-align: center; margin-top: 60px; }}
footer a {{ color: #E6417F; }}
</style>
</head>
<body>
<div class="draft-banner">⚠️ DRAFT — Awaiting Donald Review ⚠️</div>
<header><h1>{content["h1"]}</h1></header>
<div class="container">
<p style="font-size:1.2rem;color:#666;font-style:italic;">{content["intro"]}</p>

<h2>{content["mission_title"]}</h2>
<p>{content["mission_text"]}</p>

<h2>{content["vision_title"]}</h2>
<p><strong>{content["vision_subtitle"]}</strong></p>
<p>{content["vision_intro"]}</p>
<ul>{vision_list}</ul>

<h2>{content["shift_title"]}</h2>
<p>{content["shift_text"]}</p>

<h2>{content["company_facts_title"]}</h2>
<div class="facts">
<div class="fact-card"><strong>{content["founded"]}</strong>2026-04-24</div>
<div class="fact-card"><strong>{content["location"]}</strong>Shenzhen, China</div>
<div class="fact-card"><strong>{content["products"]}</strong>STA-100 PAA</div>
<div class="fact-card"><strong>{content["compliance"]}</strong>{content["compliance_value"]}</div>
</div>

</div>
<footer>
<p><strong>STRATRONIX</strong> — Stratronix Technology (Shenzhen) Company, Limited</p>
<p>⚠️ DRAFT — Awaiting Donald Review ⚠️</p>
<p><a href="../">← Übersicht</a></p>
</footer>
</body>
</html>'''

def main():
    for lang_code, content in ABOUT_CONTENT.items():
        target = DRAFT_ROOT / lang_code / "about.html"
        target.parent.mkdir(parents=True, exist_ok=True)
        html = gen_about_html(lang_code, content)
        target.write_text(html, encoding="utf-8")
        print(f"OK: {target.relative_to(DRAFT_ROOT.parent)} ({len(html)} bytes)")
    print(f"\nDrafted 8 about.html pages")

if __name__ == "__main__":
    main()
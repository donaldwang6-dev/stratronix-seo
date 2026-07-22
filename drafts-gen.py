#!/usr/bin/env python3
"""
基于主站 en/ 内容,生成 8 国语言草稿
关键:不修改主站!只生成附属站草稿,等 Donald 审核后再 push

输出路径:stratronix-seo/drafts/{lang}/{page}.html
- 不 commit 到 master
- 不触发 GitHub Pages 部署
- Donald 审核后手动确认 push

铁律 23:不出现价格(铁律 23 LOCKED)
铁律 14:不修改主站 stratonix-website-new/
"""
from pathlib import Path

DRAFT_ROOT = Path("/home/donald/.openclaw/workspace/stratronix-seo/drafts")
DRAFT_ROOT.mkdir(parents=True, exist_ok=True)

# 8 国语言元数据
LANGS = {
    "de": {"country": "Deutschland", "compliance": "DSGVO + BDSG"},
    "fr": {"country": "France", "compliance": "RGPD + CNIL"},
    "es": {"country": "España", "compliance": "RGPD + LOPD-GDD"},
    "it": {"country": "Italia", "compliance": "GDPR + Garante"},
    "nl": {"country": "Nederland", "compliance": "AVG + Wkkgz"},
    "pl": {"country": "Polska", "compliance": "RODO + UODO"},
    "pt": {"country": "Portugal", "compliance": "RGPD + CNPD"},
    "sv": {"country": "Sverige", "compliance": "GDPR + Patientdatalag"},
}


# ============== INDEX.HTML 8 国翻译 ==============
INDEX_CONTENT = {
    "de": {
        "meta_title": "STRATRONIX — Private AI-Agent Appliance (PAA) Technologie",
        "meta_desc": "Schöpfer der Private AI-Agent Appliance (PAA) Kategorie. Aufbau einer autonomen KI-Agenten-Infrastruktur für die nächste Generation der KI-Technologie.",
        "hero_title": "STA-100 — Private KI-Appliance für Unternehmen",
        "hero_subtitle": "On-Premise KI · 100% lokal · DSGVO-konform · 24/7 verfügbar",
        "hero_cta": "→ Mehr erfahren",
        "hero_cta2": "Produkt ansehen",
        "values_title": "Unsere Kernwerte",
        "value1_title": "🔒 Datensouveränität",
        "value1_desc": "Alle Daten bleiben auf Ihrem Gerät. Keine Cloud. Keine Drittanbieter.",
        "value2_title": "🚀 KI-Bereit in 30 Minuten",
        "value2_desc": "Plug-and-Play. Kein IT-Team erforderlich. Sofort einsatzbereit.",
        "value3_title": "🛡️ DSGVO by Design",
        "value3_desc": "Vollständig konform mit DSGVO, BDSG, BSI C5 und EU AI Act.",
        "value4_title": "🌍 24 EU-Sprachen",
        "value4_desc": "Native Unterstützung für alle offiziellen EU-Amtssprachen.",
        "perf_title": "Leistungsmerkmale",
        "test_title": "Kundenstimmen",
        "blog_title": "Aus dem Blog",
        "cta_title": "Starten Sie Ihre PAA-Transformation",
        "cta_desc": "On-Premise KI für Ihr Unternehmen. 30-Tage-Pilot. Vollständig DSGVO-konform.",
        "cta_btn1": "→ Demo anfragen",
        "cta_btn2": "Zur Storefront",
        "spec_section_title": "Technische Spezifikationen",
        "spec_cpu": "Prozessor: 8-Kern ARM Cortex-A76 + NPU",
        "spec_ram": "Arbeitsspeicher: 24 GB LPDDR5",
        "spec_storage": "Speicher: 2 TB NVMe SSD",
        "spec_models": "Modelle: Llama 3, Mistral, Qwen, DeepSeek",
        "spec_speed": "Geschwindigkeit: 7B ~30 Token/s, 70B ~5 Token/s",
        "spec_connectivity": "Anschlüsse: Gigabit Ethernet, Wi-Fi 6, USB-C",
        "usecase_title": "Anwendungsfälle",
        "usecase_legal": "Rechtsanwälte: Vertragsanalyse, Mandantenschutz",
        "usecase_healthcare": "Kliniken: Patientendaten, Offline-Notfall-KI",
        "usecase_finance": "Banken: Compliance-Berichte, KYC/AML",
        "usecase_manufacturing": "Industrie: Vorausschauende Wartung",
        "usecase_gov": "Behörden: Verschlusssachen-VS-NfD, Auditierbar",
    },
    "fr": {
        "meta_title": "STRATRONIX — Technologie Appliance IA Privée (PAA)",
        "meta_desc": "Créateur de la catégorie Appliance IA Privée (PAA). Construction d'une infrastructure d'agents IA autonomes pour la prochaine génération de la technologie IA.",
        "hero_title": "STA-100 — Appliance IA Privée pour Entreprises",
        "hero_subtitle": "IA On-Premise · 100% local · Conforme RGPD · Disponible 24/7",
        "hero_cta": "→ En savoir plus",
        "hero_cta2": "Voir le produit",
        "values_title": "Nos Valeurs Fondamentales",
        "value1_title": "🔒 Souveraineté des données",
        "value1_desc": "Toutes les données restent sur votre appareil. Pas de cloud. Pas de tiers.",
        "value2_title": "🚀 Opérationnel en 30 minutes",
        "value2_desc": "Plug-and-play. Aucune équipe IT requise. Immédiatement utilisable.",
        "value3_title": "🛡️ RGPD by Design",
        "value3_desc": "Entièrement conforme au RGPD, CNIL et EU AI Act.",
        "value4_title": "🌍 24 langues UE",
        "value4_desc": "Support natif de toutes les langues officielles de l'UE.",
        "perf_title": "Performances",
        "test_title": "Témoignages clients",
        "blog_title": "Du Blog",
        "cta_title": "Démarrez votre transformation PAA",
        "cta_desc": "IA on-premise pour votre entreprise. Pilote 30 jours. Entièrement conforme RGPD.",
        "cta_btn1": "→ Demander une démo",
        "cta_btn2": "Voir la boutique",
        "spec_section_title": "Spécifications Techniques",
        "spec_cpu": "Processeur : 8-core ARM Cortex-A76 + NPU",
        "spec_ram": "RAM : 24 GB LPDDR5",
        "spec_storage": "Stockage : 2 TB NVMe SSD",
        "spec_models": "Modèles : Llama 3, Mistral, Qwen, DeepSeek",
        "spec_speed": "Vitesse : 7B ~30 token/s, 70B ~5 token/s",
        "spec_connectivity": "Connectivité : Gigabit Ethernet, Wi-Fi 6, USB-C",
        "usecase_title": "Cas d'utilisation",
        "usecase_legal": "Avocats : Analyse de contrats, protection client",
        "usecase_healthcare": "Hôpitaux : Données patients, IA urgence hors-ligne",
        "usecase_finance": "Banques : Rapports conformité, KYC/AML",
        "usecase_manufacturing": "Industrie : Maintenance prédictive",
        "usecase_gov": "Administrations : Audit-ready, données souveraines",
    },
    "es": {
        "meta_title": "STRATRONIX — Tecnología Appliance IA Privada (PAA)",
        "meta_desc": "Creador de la categoría Appliance IA Privada (PAA). Construyendo infraestructura de agentes IA autónomos para la próxima generación.",
        "hero_title": "STA-100 — Appliance IA Privada para Empresas",
        "hero_subtitle": "IA On-Premise · 100% local · Conforme RGPD · Disponible 24/7",
        "hero_cta": "→ Saber más",
        "hero_cta2": "Ver producto",
        "values_title": "Nuestros Valores Fundamentales",
        "value1_title": "🔒 Soberanía de datos",
        "value1_desc": "Todos los datos permanecen en su dispositivo. Sin nube. Sin terceros.",
        "value2_title": "🚀 Operativo en 30 minutos",
        "value2_desc": "Plug-and-play. Sin equipo IT. Listo inmediatamente.",
        "value3_title": "🛡️ RGPD by Design",
        "value3_desc": "Totalmente conforme con RGPD, LOPD-GDD y EU AI Act.",
        "value4_title": "🌍 24 idiomas UE",
        "value4_desc": "Soporte nativo para todos los idiomas oficiales de la UE.",
        "perf_title": "Rendimiento",
        "test_title": "Testimonios de clientes",
        "blog_title": "Del Blog",
        "cta_title": "Inicie su transformación PAA",
        "cta_desc": "IA on-premise para su empresa. Piloto 30 días. Totalmente conforme RGPD.",
        "cta_btn1": "→ Solicitar demo",
        "cta_btn2": "Ver tienda",
        "spec_section_title": "Especificaciones Técnicas",
        "spec_cpu": "Procesador: 8-core ARM Cortex-A76 + NPU",
        "spec_ram": "RAM: 24 GB LPDDR5",
        "spec_storage": "Almacenamiento: 2 TB NVMe SSD",
        "spec_models": "Modelos: Llama 3, Mistral, Qwen, DeepSeek",
        "spec_speed": "Velocidad: 7B ~30 token/s, 70B ~5 token/s",
        "spec_connectivity": "Conectividad: Gigabit Ethernet, Wi-Fi 6, USB-C",
        "usecase_title": "Casos de uso",
        "usecase_legal": "Abogados: Análisis contratos, protección cliente",
        "usecase_healthcare": "Hospitales: Datos pacientes, IA urgencias offline",
        "usecase_finance": "Bancos: Informes cumplimiento, KYC/AML",
        "usecase_manufacturing": "Industria: Mantenimiento predictivo",
        "usecase_gov": "Administraciones: Audit-ready, datos soberanos",
    },
    "it": {
        "meta_title": "STRATRONIX — Tecnologia Appliance IA Privata (PAA)",
        "meta_desc": "Creatore della categoria Appliance IA Privata (PAA). Costruzione di infrastruttura agenti IA autonomi per la prossima generazione.",
        "hero_title": "STA-100 — Appliance IA Privata per Aziende",
        "hero_subtitle": "IA On-Premise · 100% locale · Conforme GDPR · Disponibile 24/7",
        "hero_cta": "→ Scopri di più",
        "hero_cta2": "Vedi prodotto",
        "values_title": "I Nostri Valori Fondamentali",
        "value1_title": "🔒 Sovranità dei dati",
        "value1_desc": "Tutti i dati restano sul dispositivo. Niente cloud. Niente terzi.",
        "value2_title": "🚀 Operativo in 30 minuti",
        "value2_desc": "Plug-and-play. Nessun team IT richiesto.",
        "value3_title": "🛡️ GDPR by Design",
        "value3_desc": "Pienamente conforme a GDPR, Garante Privacy e EU AI Act.",
        "value4_title": "🌍 24 lingue UE",
        "value4_desc": "Supporto nativo per tutte le lingue ufficiali UE.",
        "perf_title": "Prestazioni",
        "test_title": "Testimonianze clienti",
        "blog_title": "Dal Blog",
        "cta_title": "Inizia la tua trasformazione PAA",
        "cta_desc": "IA on-premise per la tua azienda. Pilota 30 giorni. Pienamente conforme GDPR.",
        "cta_btn1": "→ Richiedi demo",
        "cta_btn2": "Vedi negozio",
        "spec_section_title": "Specifiche Tecniche",
        "spec_cpu": "Processore: 8-core ARM Cortex-A76 + NPU",
        "spec_ram": "RAM: 24 GB LPDDR5",
        "spec_storage": "Storage: 2 TB NVMe SSD",
        "spec_models": "Modelli: Llama 3, Mistral, Qwen, DeepSeek",
        "spec_speed": "Velocità: 7B ~30 token/s, 70B ~5 token/s",
        "spec_connectivity": "Connettività: Gigabit Ethernet, Wi-Fi 6, USB-C",
        "usecase_title": "Casi d'uso",
        "usecase_legal": "Avvocati: Analisi contratti, protezione cliente",
        "usecase_healthcare": "Ospedali: Dati pazienti, IA emergenza offline",
        "usecase_finance": "Banche: Report conformità, KYC/AML",
        "usecase_manufacturing": "Industria: Manutenzione predittiva",
        "usecase_gov": "PA: Audit-ready, dati sovrani",
    },
    "nl": {
        "meta_title": "STRATRONIX — Private AI-Agent Appliance (PAA) Technologie",
        "meta_desc": "Schepper van de Private AI-Agent Appliance (PAA) categorie. Bouw aan autonome AI-agent infrastructuur voor de volgende generatie AI-technologie.",
        "hero_title": "STA-100 — Private AI-Appliance voor Bedrijven",
        "hero_subtitle": "On-Premise AI · 100% lokaal · AVG-conform · 24/7 beschikbaar",
        "hero_cta": "→ Meer informatie",
        "hero_cta2": "Bekijk product",
        "values_title": "Onze Kernwaarden",
        "value1_title": "🔒 Data-soevereiniteit",
        "value1_desc": "Alle data blijft op uw apparaat. Geen cloud. Geen derden.",
        "value2_title": "🚀 Operationeel in 30 minuten",
        "value2_desc": "Plug-and-play. Geen IT-team nodig.",
        "value3_title": "🛡️ AVG by Design",
        "value3_desc": "Volledig conform AVG, Wkkgz en EU AI Act.",
        "value4_title": "🌍 24 EU-talen",
        "value4_desc": "Native ondersteuning voor alle officiële EU-talen.",
        "perf_title": "Prestaties",
        "test_title": "Klantgetuigenissen",
        "blog_title": "Uit de Blog",
        "cta_title": "Start uw PAA-transformatie",
        "cta_desc": "On-premise AI voor uw bedrijf. 30-dagen proef. Volledig AVG-conform.",
        "cta_btn1": "→ Demo aanvragen",
        "cta_btn2": "Bekijk winkel",
        "spec_section_title": "Technische Specificaties",
        "spec_cpu": "Processor: 8-core ARM Cortex-A76 + NPU",
        "spec_ram": "RAM: 24 GB LPDDR5",
        "spec_storage": "Opslag: 2 TB NVMe SSD",
        "spec_models": "Modellen: Llama 3, Mistral, Qwen, DeepSeek",
        "spec_speed": "Snelheid: 7B ~30 token/s, 70B ~5 token/s",
        "spec_connectivity": "Connectiviteit: Gigabit Ethernet, Wi-Fi 6, USB-C",
        "usecase_title": "Toepassingsscenario's",
        "usecase_legal": "Advocaten: Contractanalyse, cliëntbescherming",
        "usecase_healthcare": "Ziekenhuizen: Patiëntgegevens, offline noodhulp-AI",
        "usecase_finance": "Banken: Compliance-rapporten, KYC/AML",
        "usecase_manufacturing": "Industrie: Predictief onderhoud",
        "usecase_gov": "Overheid: Audit-ready, soevereine data",
    },
    "pl": {
        "meta_title": "STRATRONIX — Technologia Prywatna Applikacja AI (PAA)",
        "meta_desc": "Twórca kategorii Prywatna Applikacja AI (PAA). Budowanie autonomicznej infrastruktury agentów AI dla nowej generacji technologii AI.",
        "hero_title": "STA-100 — Prywatna Applikacja AI dla Firm",
        "hero_subtitle": "AI On-Premise · 100% lokalnie · Zgodne z RODO · Dostępne 24/7",
        "hero_cta": "→ Dowiedz się więcej",
        "hero_cta2": "Zobacz produkt",
        "values_title": "Nasze Główne Wartości",
        "value1_title": "🔒 Suwerenność danych",
        "value1_desc": "Wszystkie dane pozostają na urządzeniu. Bez chmury. Bez stron trzecich.",
        "value2_title": "🚀 Gotowe w 30 minut",
        "value2_desc": "Plug-and-play. Bez zespołu IT.",
        "value3_title": "🛡️ RODO by Design",
        "value3_desc": "Pełna zgodność z RODO, UODO i EU AI Act.",
        "value4_title": "🌍 24 języki UE",
        "value4_desc": "Natywne wsparcie wszystkich języków urzędowych UE.",
        "perf_title": "Wydajność",
        "test_title": "Opinie klientów",
        "blog_title": "Z Blogu",
        "cta_title": "Rozpocznij transformację PAA",
        "cta_desc": "AI on-premise dla Twojej firmy. 30-dniowy pilot. Pełna zgodność z RODO.",
        "cta_btn1": "→ Zamów demo",
        "cta_btn2": "Zobacz sklep",
        "spec_section_title": "Specyfikacje Techniczne",
        "spec_cpu": "Procesor: 8-core ARM Cortex-A76 + NPU",
        "spec_ram": "RAM: 24 GB LPDDR5",
        "spec_storage": "Pamięć: 2 TB NVMe SSD",
        "spec_models": "Modele: Llama 3, Mistral, Qwen, DeepSeek",
        "spec_speed": "Prędkość: 7B ~30 token/s, 70B ~5 token/s",
        "spec_connectivity": "Łączność: Gigabit Ethernet, Wi-Fi 6, USB-C",
        "usecase_title": "Przypadki użycia",
        "usecase_legal": "Prawnicy: Analiza umów, ochrona klienta",
        "usecase_healthcare": "Szpitale: Dane pacjentów, awaryjne AI offline",
        "usecase_finance": "Banki: Raporty zgodności, KYC/AML",
        "usecase_manufacturing": "Przemysł: Konserwacja predykcyjna",
        "usecase_gov": "Administracja: Audit-ready, suwerenne dane",
    },
    "pt": {
        "meta_title": "STRATRONIX — Tecnologia Appliance IA Privada (PAA)",
        "meta_desc": "Criador da categoria Appliance IA Privada (PAA). Construindo infraestrutura de agentes IA autónomos para a próxima geração.",
        "hero_title": "STA-100 — Appliance IA Privada para Empresas",
        "hero_subtitle": "IA On-Premise · 100% local · Conforme RGPD · Disponível 24/7",
        "hero_cta": "→ Saber mais",
        "hero_cta2": "Ver produto",
        "values_title": "Os Nossos Valores Fundamentais",
        "value1_title": "🔒 Soberania de dados",
        "value1_desc": "Todos os dados permanecem no dispositivo. Sem nuvem. Sem terceiros.",
        "value2_title": "🚀 Operacional em 30 minutos",
        "value2_desc": "Plug-and-play. Sem equipa IT.",
        "value3_title": "🛡️ RGPD by Design",
        "value3_desc": "Totalmente conforme RGPD, CNPD e EU AI Act.",
        "value4_title": "🌍 24 línguas UE",
        "value4_desc": "Suporte nativo para todas as línguas oficiais da UE.",
        "perf_title": "Desempenho",
        "test_title": "Testemunhos de clientes",
        "blog_title": "Do Blog",
        "cta_title": "Inicie a sua transformação PAA",
        "cta_desc": "IA on-premise para a sua empresa. Piloto 30 dias. Totalmente conforme RGPD.",
        "cta_btn1": "→ Solicitar demo",
        "cta_btn2": "Ver loja",
        "spec_section_title": "Especificações Técnicas",
        "spec_cpu": "Processador: 8-core ARM Cortex-A76 + NPU",
        "spec_ram": "RAM: 24 GB LPDDR5",
        "spec_storage": "Armazenamento: 2 TB NVMe SSD",
        "spec_models": "Modelos: Llama 3, Mistral, Qwen, DeepSeek",
        "spec_speed": "Velocidade: 7B ~30 token/s, 70B ~5 token/s",
        "spec_connectivity": "Conectividade: Gigabit Ethernet, Wi-Fi 6, USB-C",
        "usecase_title": "Casos de utilização",
        "usecase_legal": "Advogados: Análise contratos, proteção cliente",
        "usecase_healthcare": "Hospitais: Dados doentes, IA emergência offline",
        "usecase_finance": "Bancos: Relatórios conformidade, KYC/AML",
        "usecase_manufacturing": "Indústria: Manutenção preditiva",
        "usecase_gov": "Administração: Audit-ready, dados soberanos",
    },
    "sv": {
        "meta_title": "STRATRONIX — Privat AI-Agent Appliance (PAA) Teknik",
        "meta_desc": "Skapare av kategorin Privat AI-Agent Appliance (PAA). Bygger autonom AI-agentinfrastruktur för nästa generation AI-teknik.",
        "hero_title": "STA-100 — Privat AI-Appliance för Företag",
        "hero_subtitle": "On-Premise AI · 100% lokalt · GDPR-kompatibel · Tillgänglig 24/7",
        "hero_cta": "→ Mer information",
        "hero_cta2": "Se produkt",
        "values_title": "Våra Kärnvärden",
        "value1_title": "🔒 Dataherradöme",
        "value1_desc": "All data stannar på din enhet. Ingen moln. Inga tredje parter.",
        "value2_title": "🚀 Driftsatt på 30 minuter",
        "value2_desc": "Plug-and-play. Ingen IT-avdelning krävs.",
        "value3_title": "🛡️ GDPR by Design",
        "value3_desc": "Fullständigt kompatibel med GDPR, Patientdatalag och EU AI Act.",
        "value4_title": "🌍 24 EU-språk",
        "value4_desc": "Inbyggt stöd för alla EU-officiella språk.",
        "perf_title": "Prestanda",
        "test_title": "Kundrecensioner",
        "blog_title": "Från Bloggen",
        "cta_title": "Starta din PAA-transformation",
        "cta_desc": "On-premise AI för ditt företag. 30-dagars pilot. Fullständigt GDPR-kompatibel.",
        "cta_btn1": "→ Begär demo",
        "cta_btn2": "Se butik",
        "spec_section_title": "Tekniska Specifikationer",
        "spec_cpu": "Processor: 8-core ARM Cortex-A76 + NPU",
        "spec_ram": "RAM: 24 GB LPDDR5",
        "spec_storage": "Lagring: 2 TB NVMe SSD",
        "spec_models": "Modeller: Llama 3, Mistral, Qwen, DeepSeek",
        "spec_speed": "Hastighet: 7B ~30 token/s, 70B ~5 token/s",
        "spec_connectivity": "Anslutning: Gigabit Ethernet, Wi-Fi 6, USB-C",
        "usecase_title": "Användningsfall",
        "usecase_legal": "Advokater: Kontraktsanalys, klientskydd",
        "usecase_healthcare": "Sjukhus: Patientdata, offline akut-AI",
        "usecase_finance": "Banker: Compliance-rapporter, KYC/AML",
        "usecase_manufacturing": "Industri: Prediktivt underhåll",
        "usecase_gov": "Myndigheter: Audit-ready, suverän data",
    },
}


def gen_index_html(lang_code: str, content: dict) -> str:
    """生成主页 8 国草稿"""
    lang_meta = LANGS[lang_code]
    canonical = f"https://donaldwang6-dev.github.io/stratronix-seo/drafts/{lang_code}/index.html"
    
    # hreflang 跨 8 国互联
    hreflangs = "\n".join(
        f'<link rel="alternate" hreflang="{code}" href="https://donaldwang6-dev.github.io/stratronix-seo/drafts/{code}/index.html">'
        for code in LANGS.keys()
    )
    hreflangs += f'\n<link rel="alternate" hreflang="x-default" href="https://www.stratronix.ai/en/">'
    hreflangs += f'\n<link rel="alternate" hreflang="zh" href="https://www.stratronix.ai/zh/">'
    
    return f'''<!DOCTYPE html>
<html lang="{lang_code}">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{content["meta_title"]}</title>
<meta name="description" content="{content["meta_desc"]}">
<meta name="keywords" content="PAA, Private AI, On-Premise AI, {LANGS[lang_code]["compliance"]}, AI Appliance, STRATRONIX">
<meta name="robots" content="index, follow, noarchive">
<link rel="canonical" href="{canonical}">
{hreflangs}
<meta property="og:title" content="{content["meta_title"]}">
<meta property="og:description" content="{content["meta_desc"]}">
<meta property="og:type" content="website">
<meta property="og:url" content="{canonical}">
<meta property="og:locale" content="{lang_code}_{lang_code.upper()}">
<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "Organization",
  "name": "Stratronix Technology (Shenzhen) Company, Limited",
  "alternateName": "STRATRONIX",
  "url": "https://www.stratronix.ai",
  "description": "{content["meta_desc"]}",
  "foundingDate": "2026-04-24",
  "address": {{
    "@type": "PostalAddress",
    "addressLocality": "Shenzhen",
    "addressRegion": "Bao'an District",
    "addressCountry": "CN"
  }},
  "contactPoint": {{
    "@type": "ContactPoint",
    "telephone": "+86-13632968417",
    "contactType": "sales",
    "email": "sales@stratronix.ai"
  }}
}}
</script>
<style>
* {{ box-sizing: border-box; margin: 0; padding: 0; }}
body {{ font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; line-height: 1.8; color: #1a1a1a; background: #fafafa; }}
header {{ background: linear-gradient(135deg, #E6417F 0%, #c9296c 100%); color: white; padding: 60px 20px; text-align: center; }}
header h1 {{ font-size: 2.5rem; max-width: 900px; margin: 0 auto 16px; line-height: 1.3; }}
header .subtitle {{ max-width: 900px; margin: 0 auto; opacity: 0.95; font-size: 1.1rem; }}
.container {{ max-width: 1100px; margin: 0 auto; padding: 40px 20px; }}
.section {{ margin: 60px 0; }}
h2 {{ font-size: 1.8rem; color: #E6417F; margin-bottom: 24px; }}
.values-grid {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 20px; }}
.value-card {{ background: white; padding: 24px; border-radius: 8px; border-left: 4px solid #E6417F; }}
.value-card h3 {{ color: #1a1a1a; margin-bottom: 12px; }}
.cta {{ background: linear-gradient(135deg, #E6417F 0%, #c9296c 100%); color: white; padding: 50px 30px; text-align: center; border-radius: 12px; margin: 40px 0; }}
.cta h2 {{ color: white; margin-bottom: 16px; }}
.cta a {{ color: white; background: rgba(255,255,255,0.2); padding: 14px 36px; border-radius: 8px; text-decoration: none; font-weight: 600; display: inline-block; margin: 8px; }}
.cta a.primary {{ background: white; color: #E6417F; }}
.draft-banner {{ background: #fff3cd; border: 2px solid #ffc107; padding: 16px; text-align: center; margin: 0; font-weight: bold; }}
.lang-switch {{ text-align: center; padding: 12px; background: #f0f0f0; font-size: 0.9rem; }}
.lang-switch a {{ margin: 0 6px; color: #E6417F; text-decoration: none; }}
footer {{ background: #1a1a1a; color: #999; padding: 30px 20px; text-align: center; margin-top: 60px; }}
footer a {{ color: #E6417F; }}
</style>
</head>
<body>

<div class="draft-banner">
⚠️ DRAFT — NOT DEPLOYED — Awaiting Donald Review (2026-07-21) ⚠️
</div>

<div class="lang-switch">
{(" · ".join(f'<a href="../{c}/index.html">{LANGS[c]["country"]}</a>' if c != lang_code else f'<strong>{LANGS[c]["country"]}</strong>' for c in LANGS))}
</div>

<header>
<h1>{content["hero_title"]}</h1>
<p class="subtitle">{content["hero_subtitle"]}</p>
<p style="margin-top:24px;">
<a href="https://store.stratonix.ai" style="color:white;background:rgba(255,255,255,0.2);padding:14px 36px;border-radius:8px;text-decoration:none;font-weight:600;display:inline-block;margin:8px;">{content["hero_cta"]}</a>
<a href="https://store.stratonix.ai" style="color:white;background:rgba(255,255,255,0.2);padding:14px 36px;border-radius:8px;text-decoration:none;font-weight:600;display:inline-block;margin:8px;">{content["hero_cta2"]}</a>
</p>
</header>

<div class="container">

<section class="section">
<h2>{content["values_title"]}</h2>
<div class="values-grid">
<div class="value-card">
<h3>{content["value1_title"]}</h3>
<p>{content["value1_desc"]}</p>
</div>
<div class="value-card">
<h3>{content["value2_title"]}</h3>
<p>{content["value2_desc"]}</p>
</div>
<div class="value-card">
<h3>{content["value3_title"]}</h3>
<p>{content["value3_desc"]}</p>
</div>
<div class="value-card">
<h3>{content["value4_title"]}</h3>
<p>{content["value4_desc"]}</p>
</div>
</div>
</section>

<section class="section">
<h2>{content["usecase_title"]}</h2>
<ul style="list-style:none;padding:0;">
<li style="padding:12px 0;border-bottom:1px solid #eee;">⚖️ <strong>{content["usecase_legal"]}</strong></li>
<li style="padding:12px 0;border-bottom:1px solid #eee;">🏥 <strong>{content["usecase_healthcare"]}</strong></li>
<li style="padding:12px 0;border-bottom:1px solid #eee;">💰 <strong>{content["usecase_finance"]}</strong></li>
<li style="padding:12px 0;border-bottom:1px solid #eee;">🏭 <strong>{content["usecase_manufacturing"]}</strong></li>
<li style="padding:12px 0;">🏛️ <strong>{content["usecase_gov"]}</strong></li>
</ul>
</section>

<section class="section">
<h2>{content["spec_section_title"]}</h2>
<ul style="background:white;padding:24px;border-radius:8px;list-style:none;">
<li>✅ <strong>{content["spec_cpu"]}</strong></li>
<li>✅ <strong>{content["spec_ram"]}</strong></li>
<li>✅ <strong>{content["spec_storage"]}</strong></li>
<li>✅ <strong>{content["spec_models"]}</strong></li>
<li>✅ <strong>{content["spec_speed"]}</strong></li>
<li>✅ <strong>{content["spec_connectivity"]}</strong></li>
<li>✅ <strong>{lang_meta["compliance"]}</strong></li>
</ul>
</section>

<div class="cta">
<h2>{content["cta_title"]}</h2>
<p style="margin-bottom:24px;font-size:1.1rem;">{content["cta_desc"]}</p>
<a href="https://store.stratonix.ai" class="primary">{content["cta_btn1"]}</a>
<a href="https://store.stratonix.ai">{content["cta_btn2"]}</a>
</div>

</div>

<footer>
<p><strong>STRATRONIX — {lang_meta["country"]}</strong></p>
<p>Hersteller: Stratronix Technology (Shenzhen) Company, Limited</p>
<p>HQ: Shenzhen, China · EU-Vertrieb: <a href="https://store.stratonix.ai">store.stratonix.ai</a></p>
<p style="margin-top:12px;">⚠️ DRAFT — Diese Seite wartet auf Genehmigung von Donald (汪杰) ⚠️</p>
<p><a href="../">← Übersicht aller Sprachen</a></p>
</footer>

</body>
</html>'''


def main():
    out_urls = []
    for lang_code, content in INDEX_CONTENT.items():
        target = DRAFT_ROOT / lang_code / "index.html"
        target.parent.mkdir(parents=True, exist_ok=True)
        html = gen_index_html(lang_code, content)
        target.write_text(html, encoding="utf-8")
        out_urls.append(str(target))
        print(f"OK: {target.relative_to(DRAFT_ROOT.parent)} ({len(html)} bytes)")
    
    print(f"\nDrafted {len(out_urls)} index.html pages")
    print(f"Location: {DRAFT_ROOT}")
    print(f"NOT committed to git. NOT deployed.")


if __name__ == "__main__":
    main()
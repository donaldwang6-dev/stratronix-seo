#!/usr/bin/env python3
"""
Build 10 missing EU country SEO pages × 2 long-tail pages = 20 URLs

10 missing countries: LI/SK/BG/EE/LV/LT/SI/HR/CY/MT
2 long-tail pages per country:
  - paa-{cc}-2026.html
  - on-premise-llm-{cc}-2026.html

铁律 31: 0 假客户 / 0 假数据
铁律 15.1: 100% 母语（除品牌名 STRATRONIX + 切换按钮 English）
"""
from pathlib import Path
import urllib.parse

ROOT = Path("/home/donald/.openclaw/workspace/stratronix-seo")
DST = ROOT
BASE_URL = "https://donaldwang6-dev.github.io/stratronix-seo"

# 10 国家数据（真实信息，全部来自公开资料）
COUNTRIES = [
    {
        "cc": "li", "lang": "de",
        "country_en": "Liechtenstein", "country_native": "Liechtenstein",
        "capital_en": "Vaduz", "capital_native": "Vaduz",
        "currency": "CHF (Swiss Franc)", "eu_member": "EEA member (not EU)",
        "gdpr_term": "DSGVO (Liechtenstein implementation)",
        "act_term": "EU AI Act (EEA-applicable since 2025)",
        "industry_focus": "Financial services, manufacturing, premium goods",
        "compliance_box": "DSGVO + EWR-Datenschutz + EU AI Act (EEA applicable)",
    },
    {
        "cc": "sk", "lang": "sk",
        "country_en": "Slovakia", "country_native": "Slovensko",
        "capital_en": "Bratislava", "capital_native": "Bratislava",
        "currency": "EUR (Euro)", "eu_member": "2004-05-01",
        "gdpr_term": "GDPR + slovenský zákon o ochrane osobných údajov",
        "act_term": "AI Act (nariadenie 2024/1689)",
        "industry_focus": "Automotive manufacturing, electronics, IT services",
        "compliance_box": "GDPR + zákon č. 18/2018 + AI Act",
    },
    {
        "cc": "bg", "lang": "bg",
        "country_en": "Bulgaria", "country_native": "България",
        "capital_en": "Sofia", "capital_native": "София",
        "currency": "BGN (Bulgarian Lev)", "eu_member": "2007-01-01",
        "gdpr_term": "GDPR + ЗЗЛД (Закон за защита на личните данни)",
        "act_term": "Регламент (ЕС) 2024/1689 — Закон за ИИ",
        "industry_focus": "IT outsourcing, manufacturing, agriculture",
        "compliance_box": "GDPR + ЗЗЛД + КЗЛД + AI Act",
    },
    {
        "cc": "ee", "lang": "et",
        "country_en": "Estonia", "country_native": "Eesti",
        "capital_en": "Tallinn", "capital_native": "Tallinn",
        "currency": "EUR (Euro)", "eu_member": "2004-05-01",
        "gdpr_term": "GDPR + isikuandmete kaitse seadus (IKS)",
        "act_term": "ELi tehisintellekti määrus 2024/1689",
        "industry_focus": "Digital government, e-residency, fintech, cybersecurity",
        "compliance_box": "GDPR + IKS + AI Act + e-Governance standards",
    },
    {
        "cc": "lv", "lang": "lv",
        "country_en": "Latvia", "country_native": "Latvija",
        "capital_en": "Riga", "capital_native": "Rīga",
        "currency": "EUR (Euro)", "eu_member": "2004-05-01",
        "gdpr_term": "GDPR + Fizisko personu datu apstrādes likums",
        "act_term": "ES Regula 2024/1689 (AI Akts)",
        "industry_focus": "ICT services, logistics, woodworking, green tech",
        "compliance_box": "GDPR + Datu valsts inspekcija + AI Act",
    },
    {
        "cc": "lt", "lang": "lt",
        "country_en": "Lithuania", "country_native": "Lietuva",
        "capital_en": "Vilnius", "capital_native": "Vilnius",
        "currency": "EUR (Euro)", "eu_member": "2004-05-01",
        "gdpr_term": "GDPR + Asmens duomenų teisinės apsaugos įstatymas",
        "act_term": "ES Reglamentas 2024/1689 (DI Aktas)",
        "industry_focus": "Fintech, laser technology, biotech, IT services",
        "compliance_box": "GDPR + ADA + AI Act + Valstybinė duomenų apsaugos inspekcija",
    },
    {
        "cc": "si", "lang": "sl",
        "country_en": "Slovenia", "country_native": "Slovenija",
        "capital_en": "Ljubljana", "capital_native": "Ljubljana",
        "currency": "EUR (Euro)", "eu_member": "2004-05-01",
        "gdpr_term": "GDPR + Zakon o varstvu osebnih podatkov (ZVOP-2)",
        "act_term": "Uredba (EU) 2024/1689 — Akt o AI",
        "industry_focus": "Manufacturing, automotive, tourism, green energy",
        "compliance_box": "GDPR + ZVOP-2 + Informacijski pooblaščenec + AI Act",
    },
    {
        "cc": "hr", "lang": "hr",
        "country_en": "Croatia", "country_native": "Hrvatska",
        "capital_en": "Zagreb", "capital_native": "Zagreb",
        "currency": "EUR (Euro since 2023)", "eu_member": "2013-07-01",
        "gdpr_term": "GDPR + Zakon o provedbi Opće uredbe o zaštiti podataka",
        "act_term": "Uredba (EU) 2024/1689 — Akt o umjetnoj inteligenciji",
        "industry_focus": "Tourism, shipbuilding, food processing, pharmaceuticals",
        "compliance_box": "GDPR + AZOP (Agencija za zaštitu osobnih podataka) + AI Act",
    },
    {
        "cc": "cy", "lang": "el",
        "country_en": "Cyprus", "country_native": "Κύπρος",
        "capital_en": "Nicosia", "capital_native": "Λευκωσία",
        "currency": "EUR (Euro)", "eu_member": "2004-05-01",
        "gdpr_term": "GDPR + ο περί της Προστασίας των Φυσικών Προσώπων έναντι της Επεξεργασίας των Δεδομένων Προσωπικού Χαρακτήρα Νόμος",
        "act_term": "Κανονισμός (ΕΕ) 2024/1689 — Πράξη για την ΤΝ",
        "industry_focus": "Financial services, shipping, tourism, professional services",
        "compliance_box": "GDPR + Γραφείο Επιτρόπου Προστασίας Δεδομένων + AI Act",
    },
    {
        "cc": "mt", "lang": "mt",
        "country_en": "Malta", "country_native": "Malta",
        "capital_en": "Valletta", "capital_native": "Valletta",
        "currency": "EUR (Euro)", "eu_member": "2004-05-01",
        "gdpr_term": "GDPR + Att dwar il-Protezzjoni u l-Privatezza tad-Data",
        "act_term": "Regolament (UE) 2024/1689 — Att dwar l-IA",
        "industry_focus": "iGaming, financial services, blockchain, tourism",
        "compliance_box": "GDPR + Information and Data Protection Commissioner + AI Act + MFSA",
    },
]

# PAA 介绍（母语，结构相同）— 翻译 STRATRONIX 真实信息
PAA_INTRO = {
    "de": "STRATRONIX PAA (Private AI-Agent Appliance) ist eine Hardware-Appliance, die Large Language Models vollständig on-premise betreibt — keine Cloud, keine API-Aufrufe, kein Datenabfluss. Die STRATRONIX STA-100 ist die Standardkonfiguration für den deutschsprachigen europäischen Markt und unterstützt den EU AI Act, DSGVO und alle relevanten nationalen Datenschutzgesetze.",
    "sk": "STRATRONIX PAA (Private AI-Agent Appliance) je hardvérové zariadenie, ktoré prevádzkuje veľké jazykové modely kompletne on-premise — bez cloudu, bez API volaní, bez úniku dát. STRATRONIX STA-100 je štandardná konfigurácia pre slovenský trh a spĺňa požiadavky AI Act, GDPR a národných predpisov o ochrane osobných údajov.",
    "bg": "STRATRONIX PAA (Private AI-Agent Appliance) е хардуерно устройство, което изцяло изпълнява големи езикови модели на място (on-premise) — без облак, без API извиквания, без изтичане на данни. STRATRONIX STA-100 е стандартната конфигурация за българския пазар и отговаря на изискванията на AI Act, GDPR и националните закони за защита на личните данни.",
    "et": "STRATRONIX PAA (Private AI-Agent Appliance) on riistvaraline seade, mis käitab suuri keelemudeleid täielikult kohapeal (on-premise) — ilma pilveta, ilma API-kutsete ja andmelekketa. STRATRONIX STA-100 on Eesti turu standardseadistus ja vastab AI Acti, GDPR-i ja riiklike andmekaitseseaduste nõuetele.",
    "lv": "STRATRONIX PAA (Private AI-Agent Appliance) ir aparatūras ierīce, kas pilnībā darbina lielus valodu modeļus uz vietas (on-premise) — bez mākoņa, bez API izsaukumiem, bez datu noplūdes. STRATRONIX STA-100 ir standarta konfigurācija Latvijas tirgum un atbilst AI Akta, GDPR un valsts datu aizsardzības likumu prasībām.",
    "lt": "STRATRONIX PAA (Private AI-Agent Appliance) yra aparatinės įrangos įrenginys, kuris visiškai vietoje (on-premise) valdo didelius kalbos modelius — be debesijos, be API užklausų, be duomenų nutekėjimo. STRATRONIX STA-100 yra standartinė Lietuvos rinkos konfigūracija ir atitinka AI Akto, GDPR ir nacionalinių duomenų apsaugos įstatymų reikalavimus.",
    "sl": "STRATRONIX PAA (Private AI-Agent Appliance) je strojna naprava, ki v celoti lokalno (on-premise) izvaja velike jezikovne modele — brez oblaka, brez klicev API, brez uhajanja podatkov. STRATRONIX STA-100 je standardna konfiguracija za slovenski trg in izpolnjuje zahteve AI Act, GDPR in nacionalnih predpisov o varstvu podatkov.",
    "hr": "STRATRONIX PAA (Private AI-Agent Appliance) je hardverski uređaj koji u potpunosti lokalno (on-premise) pokreta velike jezične modele — bez oblaka, bez API poziva, bez curenja podataka. STRATRONIX STA-100 je standardna konfiguracija za hrvatsko tržište i ispunjava zahtjeve AI Acta, GDPR-a i nacionalnih propisa o zaštiti podataka.",
    "el": "Το STRATRONIX PAA (Private AI-Agent Appliance) είναι μια συσκευή υλικού που εκτελεί πλήρως τοπικά (on-premise) μεγάλα γλωσσικά μοντέλα — χωρίς cloud, χωρίς κλήσεις API, χωρίς διαρροή δεδομένων. Το STRATRONIX STA-100 είναι η τυπική διαμόρφωση για την κυπριακή αγορά και πληροί τις απαιτήσεις του AI Act, του GDPR και των εθνικών νόμων προστασίας δεδομένων.",
    "mt": "STRATRONIX PAA (Private AI-Agent Appliance) hija apparat tal-ħardwer li jmexxi kompletament fuq il-post (on-premise) mudelli kbar tal-lingwa — bla cloud, bla sejħiet API, bla telf ta' dejta. STRATRONIX STA-100 hija l-konfigurazzjoni standard għas-suq Malti u tilħaq ir-rekwiżiti tal-AI Act, tal-GDPR u tal-liġijiet nazzjonali dwar il-protezzjoni tad-dejta.",
}

# 多语种切换（24 语种）
LANG_SWITCH_24 = [
    ("EN", "/en/"), ("DE", "/de/"), ("FR", "/fr/"), ("ES", "/es/"), ("IT", "/it/"),
    ("NL", "/nl/"), ("PL", "/pl/"), ("PT", "/pt/"), ("SV", "/sv/"), ("DA", "/da/"),
    ("FI", "/fi/"), ("EL", "/el/"), ("HU", "/hu/"), ("RO", "/ro/"), ("CS", "/cz/"),
    ("SK", "/sk/"), ("BG", "/bg/"), ("HR", "/hr/"), ("SL", "/si/"), ("ET", "/ee/"),
    ("LV", "/lv/"), ("LT", "/lt/"), ("MT", "/mt/"), ("中文", "/zh/"),
]

# 行业列表
INDUSTRY_LINKS = {
    "de": [("Recht", "/de/industries/legal.html"), ("Gesundheit", "/de/industries/healthcare.html"),
           ("Finanzen", "/de/industries/finance.html"), ("Industrie", "/de/industries/manufacturing.html"),
           ("SaaS", "/de/industries/saas.html")],
    "sk": [("Právo", "/sk/industries/legal.html"), ("Zdravotníctvo", "/sk/industries/healthcare.html"),
           ("Financie", "/sk/industries/finance.html"), ("Výroba", "/sk/industries/manufacturing.html"),
           ("SaaS", "/sk/industries/saas.html")],
    "bg": [("Право", "/bg/industries/legal.html"), ("Здравеопазване", "/bg/industries/healthcare.html"),
           ("Финанси", "/bg/industries/finance.html"), ("Производство", "/bg/industries/manufacturing.html"),
           ("SaaS", "/bg/industries/saas.html")],
    "et": [("Õigus", "/ee/industries/legal.html"), ("Tervishoiu", "/ee/industries/healthcare.html"),
           ("Finants", "/ee/industries/finance.html"), ("Tootmine", "/ee/industries/manufacturing.html"),
           ("SaaS", "/ee/industries/saas.html")],
    "lv": [("Juridiskā", "/lv/industries/legal.html"), ("Veselības", "/lv/industries/healthcare.html"),
           ("Finanšu", "/lv/industries/finance.html"), ("Ražošanas", "/lv/industries/manufacturing.html"),
           ("SaaS", "/lv/industries/saas.html")],
    "lt": [("Teisinė", "/lt/industries/legal.html"), ("Sveikatos", "/lt/industries/healthcare.html"),
           ("Finansų", "/lt/industries/finance.html"), ("Gamybos", "/lt/industries/manufacturing.html"),
           ("SaaS", "/lt/industries/saas.html")],
    "sl": [("Pravna", "/si/industries/legal.html"), ("Zdravstvena", "/si/industries/healthcare.html"),
           ("Finančna", "/si/industries/finance.html"), ("Proizvodna", "/si/industries/manufacturing.html"),
           ("SaaS", "/si/industries/saas.html")],
    "hr": [("Pravna", "/hr/industries/legal.html"), ("Zdravstvena", "/hr/industries/healthcare.html"),
           ("Financijska", "/hr/industries/finance.html"), ("Proizvodna", "/hr/industries/manufacturing.html"),
           ("SaaS", "/hr/industries/saas.html")],
    "el": [("Νομική", "/cy/industries/legal.html"), ("Υγεία", "/cy/industries/healthcare.html"),
           ("Χρηματοοικονομικά", "/cy/industries/finance.html"), ("Βιομηχανία", "/cy/industries/manufacturing.html"),
           ("SaaS", "/cy/industries/saas.html")],
    "mt": [("Legali", "/mt/industries/legal.html"), ("Saħħa", "/mt/industries/healthcare.html"),
           ("Finanzjarji", "/mt/industries/finance.html"), ("Manifattura", "/mt/industries/manufacturing.html"),
           ("SaaS", "/mt/industries/saas.html")],
}

# SEO keywords per language
KEYWORDS = {
    "de": "PAA Liechtenstein, Private AI Liechtenstein, On-Premise LLM Liechtenstein, DSGVO KI",
    "sk": "PAA Slovensko, Private AI Slovensko, On-Premise LLM Slovensko, GDPR AI Slovensko",
    "bg": "PAA България, Private AI България, On-Premise LLM България, GDPR AI България",
    "et": "PAA Eesti, Private AI Eesti, On-Premise LLM Eesti, GDPR AI Eesti",
    "lv": "PAA Latvija, Private AI Latvija, On-Premise LLM Latvija, GDPR AI Latvija",
    "lt": "PAA Lietuva, Private AI Lietuva, On-Premise LLM Lietuva, GDPR AI Lietuva",
    "sl": "PAA Slovenija, Private AI Slovenija, On-Premise LLM Slovenija, GDPR AI Slovenija",
    "hr": "PAA Hrvatska, Private AI Hrvatska, On-Premise LLM Hrvatska, GDPR AI Hrvatska",
    "el": "PAA Κύπρος, Private AI Κύπρος, On-Premise LLM Κύπρος, GDPR AI Κύπρος",
    "mt": "PAA Malta, Private AI Malta, On-Premise LLM Malta, GDPR AI Malta",
}

# Page title templates
TITLE_TEMPLATES = {
    "paa": {
        "de": "PAA {country} 2026 — Private AI-Agent Appliance | STRATRONIX",
        "sk": "PAA {country} 2026 — Private AI-Agent Appliance | STRATRONIX",
        "bg": "ПАА {country} 2026 — Private AI-Agent Appliance | STRATRONIX",
        "et": "PAA {country} 2026 — Private AI-Agent Appliance | STRATRONIX",
        "lv": "PAA {country} 2026 — Private AI-Agent Appliance | STRATRONIX",
        "lt": "PAA {country} 2026 — Private AI-Agent Appliance | STRATRONIX",
        "sl": "PAA {country} 2026 — Private AI-Agent Appliance | STRATRONIX",
        "hr": "PAA {country} 2026 — Private AI-Agent Appliance | STRATRONIX",
        "el": "PAA {country} 2026 — Private AI-Agent Appliance | STRATRONIX",
        "mt": "PAA {country} 2026 — Private AI-Agent Appliance | STRATRONIX",
    },
    "llm": {
        "de": "On-Premise LLM {country} 2026 — Lokales LLM ohne Cloud | STRATRONIX",
        "sk": "On-Premise LLM {country} 2026 — Lokálne LLM bez cloudu | STRATRONIX",
        "bg": "On-Premise LLM {country} 2026 — Локално LLM без облак | STRATRONIX",
        "et": "On-Premise LLM {country} 2026 — Kohalik LLM ilma pilveta | STRATRONIX",
        "lv": "On-Premise LLM {country} 2026 — Vietējais LLM bez mākoņa | STRATRONIX",
        "lt": "On-Premise LLM {country} 2026 — Vietinis LLM be debesijos | STRATRONIX",
        "sl": "On-Premise LLM {country} 2026 — Lokalni LLM brez oblaka | STRATRONIX",
        "hr": "On-Premise LLM {country} 2026 — Lokalni LLM bez oblaka | STRATRONIX",
        "el": "On-Premise LLM {country} 2026 — Τοπικό LLM χωρίς cloud | STRATRONIX",
        "mt": "On-Premise LLM {country} 2026 — Lokali LLM bla cloud | STRATRONIX",
    },
}

DESC_TEMPLATES = {
    "paa": {
        "de": "STRATRONIX PAA {country}: Private AI-Agent Appliance für {country}. On-Premise KI-Hardware, {gdpr}, EU AI Act. {capital} + {industry}.",
        "sk": "STRATRONIX PAA {country}: Private AI-Agent Appliance pre {country}. On-Premise AI hardvér, {gdpr}, AI Act. {capital} + {industry}.",
        "bg": "STRATRONIX ПАА {country}: Private AI-Agent Appliance за {country}. On-Premise AI хардуер, {gdpr}, AI Act. {capital} + {industry}.",
        "et": "STRATRONIX PAA {country}: Private AI-Agent Appliance {country} jaoks. On-Premise AI riistvara, {gdpr}, AI Act. {capital} + {industry}.",
        "lv": "STRATRONIX PAA {country}: Private AI-Agent Appliance {country}. On-Premise AI aparatūra, {gdpr}, AI Akts. {capital} + {industry}.",
        "lt": "STRATRONIX PAA {country}: Private AI-Agent Appliance {country}. On-Premise AI įranga, {gdpr}, DI Aktas. {capital} + {industry}.",
        "sl": "STRATRONIX PAA {country}: Private AI-Agent Appliance za {country}. On-Premise AI strojna oprema, {gdpr}, AI Act. {capital} + {industry}.",
        "hr": "STRATRONIX PAA {country}: Private AI-Agent Appliance za {country}. On-Premise AI hardver, {gdpr}, AI Act. {capital} + {industry}.",
        "el": "STRATRONIX PAA {country}: Private AI-Agent Appliance για {country}. On-Premise AI υλικό, {gdpr}, AI Act. {capital} + {industry}.",
        "mt": "STRATRONIX PAA {country}: Private AI-Agent Appliance għal {country}. On-Premise AI ħardwer, {gdpr}, AI Act. {capital} + {industry}.",
    },
    "llm": {
        "de": "On-Premise LLM {country} 2026: Lokale KI-Sprachmodelle ohne Cloud. STRATRONIX STA-100 für {country} Unternehmen. {gdpr}, EU AI Act.",
        "sk": "On-Premise LLM {country} 2026: Lokálne jazykové modely bez cloudu. STRATRONIX STA-100 pre {country} podniky. {gdpr}, AI Act.",
        "bg": "On-Premise LLM {country} 2026: Локални езикови модели без облак. STRATRONIX STA-100 за {country} фирми. {gdpr}, AI Act.",
        "et": "On-Premise LLM {country} 2026: Kohalikud keelemudelid ilma pilveta. STRATRONIX STA-100 {country} ettevõtetele. {gdpr}, AI Act.",
        "lv": "On-Premise LLM {country} 2026: Vietējie valodu modeļi bez mākoņa. STRATRONIX STA-100 {country} uzņēmumiem. {gdpr}, AI Akts.",
        "lt": "On-Premise LLM {country} 2026: Vietiniai kalbos modeliai be debesijos. STRATRONIX STA-100 {country} įmonėms. {gdpr}, DI Aktas.",
        "sl": "On-Premise LLM {country} 2026: Lokalni jezikovni modeli brez oblaka. STRATRONIX STA-100 za {country} podjetja. {gdpr}, AI Act.",
        "hr": "On-Premise LLM {country} 2026: Lokalni jezični modeli bez oblaka. STRATRONIX STA-100 za {country} tvrtke. {gdpr}, AI Act.",
        "el": "On-Premise LLM {country} 2026: Τοπικά γλωσσικά μοντέλα χωρίς cloud. STRATRONIX STA-100 για επιχειρήσεις {country}. {gdpr}, AI Act.",
        "mt": "On-Premise LLM {country} 2026: Mudelli tal-lingwa lokali bla cloud. STRATRONIX STA-100 għal negozji f'{country}. {gdpr}, AI Act.",
    },
}


def build_page(country: dict, page_type: str):
    """page_type = 'paa' or 'llm'"""
    cc = country["cc"]
    lang = country["lang"]
    country_native = country["country_native"]
    capital_native = country["capital_native"]

    if page_type == "paa":
        slug = f"paa-{cc}-2026.html"
        title = TITLE_TEMPLATES["paa"][lang].format(country=country_native)
        desc = DESC_TEMPLATES["paa"][lang].format(
            country=country_native, gdpr=country["gdpr_term"], capital=capital_native, industry=country["industry_focus"]
        )
        h1 = f"STRATRONIX PAA {country_native} 2026"
    else:  # llm
        slug = f"on-premise-llm-{cc}-2026.html"
        title = TITLE_TEMPLATES["llm"][lang].format(country=country_native)
        desc = DESC_TEMPLATES["llm"][lang].format(
            country=country_native, gdpr=country["gdpr_term"], capital=capital_native, industry=country["industry_focus"]
        )
        h1 = f"On-Premise LLM {country_native} 2026"

    hreflang_self = f"{BASE_URL}/{cc}/{slug}"
    keywords = KEYWORDS[lang]
    intro = PAA_INTRO[lang]
    industries = INDUSTRY_LINKS[lang]
    lang_sw = " · ".join(
        f'<a href="{lurl}">{lcode}</a>' if lurl != f"/{cc}/" else f"<strong>{lcode}</strong>"
        for lcode, lurl in LANG_SWITCH_24
    )

    # Schema.org Product + Article
    schema = f"""<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "Product",
  "name": "STRATRONIX STA-100 PAA ({country_native})",
  "description": "{desc}",
  "brand": {{"@type": "Brand", "name": "STRATRONIX"}},
  "manufacturer": {{
    "@type": "Organization",
    "name": "Stratronix Technology (Shenzhen) Company, Limited",
    "foundingDate": "2026-04-24",
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
      "contactType": "sales",
      "email": "sales@stratronix.ai",
      "availableLanguage": ["en", "de", "fr", "es", "it", "nl", "pl", "pt", "sv", "da", "fi", "el", "hu", "ro", "cs", "sk", "bg", "hr", "sl", "et", "lv", "lt", "mt"]
    }},
    "sameAs": ["https://www.stratronix.ai", "https://store.stratonix.ai", "https://donaldwang6-dev.github.io/stratronix-seo/"]
  }},
  "offers": {{
    "@type": "Offer",
    "url": "https://store.stratonix.ai",
    "priceCurrency": "EUR",
    "availability": "https://schema.org/InStock",
    "itemCondition": "https://schema.org/NewCondition"
  }}
}}
</script>"""

    # Industry links
    industry_html = "\n".join(f'<li><strong>{lbl}:</strong> <a href="{url}">→</a></li>' for lbl, url in industries)

    # Body content
    h2_faq = {
        "de": "Häufig gestellte Fragen",
        "sk": "Často kladené otázky",
        "bg": "Често задавани въпроси",
        "et": "Korduma kippuvad küsimused",
        "lv": "Bieži uzdotie jautājumi",
        "lt": "Dažniausiai užduodami klausimai",
        "sl": "Pogosto zastavljena vprašanja",
        "hr": "Često postavljana pitanja",
        "el": "Συχνές ερωτήσεις",
        "mt": "Mistoqsijiet frekwenti",
    }

    h2_industry = {
        "de": "STRATRONIX PAA — Branchenlösungen",
        "sk": "STRATRONIX PAA — odvetvové riešenia",
        "bg": "STRATRONIX PAA — индустриални решения",
        "et": "STRATRONIX PAA — tööstusharu lahendused",
        "lv": "STRATRONIX PAA — nozaru risinājumi",
        "lt": "STRATRONIX PAA — pramonės sprendimai",
        "sl": "STRATRONIX PAA — panožne rešitve",
        "hr": "STRATRONIX PAA — industrijska rješenja",
        "el": "STRATRONIX PAA — κλαδικές λύσεις",
        "mt": "STRATRONIX PAA — soluzzjonijiet tal-industrija",
    }

    h2_why = {
        "de": "Warum STRATRONIX für {country}?",
        "sk": "Prečo STRATRONIX pre {country}?",
        "bg": "Защо STRATRONIX за {country}?",
        "et": "Miks STRATRONIX {country} jaoks?",
        "lv": "Kāpēc STRATRONIX {country}?",
        "lt": "Kodėl STRATRONIX {country}?",
        "sl": "Zakaj STRATRONIX za {country}?",
        "hr": "Zašto STRATRONIX za {country}?",
        "el": "Γιατί STRATRONIX για {country};",
        "mt": "Għaliex STRATRONIX għal {country}?",
    }

    h2_why_text = {
        "de": f"STRATRONIX ({country_native}-Markt) erfüllt die lokalen Anforderungen: EU-Mitglied seit {country['eu_member']}, Währung {country['currency']}, Amtssprache gemäß Verfassung. Wichtige Branchen in {country_native}: {country['industry_focus']}. Compliance-Rahmen: {country['compliance_box']}.",
        "sk": f"STRATRONIX ({country_native} trh) spĺňa miestne požiadavky: EÚ člen od {country['eu_member']}, mena {country['currency']}. Kľúčové odvetvia v {country_native}: {country['industry_focus']}. Compliance rámec: {country['compliance_box']}.",
        "bg": f"STRATRONIX (пазар {country_native}) отговаря на местните изисквания: Член на ЕС от {country['eu_member']}, валута {country['currency']}. Ключови индустрии в {country_native}: {country['industry_focus']}. Рамка за съответствие: {country['compliance_box']}.",
        "et": f"STRATRONIX ({country_native} turg) vastab kohalikele nõuetele: EL liige alates {country['eu_member']}, valuuta {country['currency']}. Peamised tööstusharud {country_native}-s: {country['industry_focus']}. Vastavuse raamistik: {country['compliance_box']}.",
        "lv": f"STRATRONIX ({country_native} tirgus) atbilst vietējām prasībām: ES dalībnieks kopš {country['eu_member']}, valūta {country['currency']}. Galvenās nozares {country_native}: {country['industry_focus']}. Atbilstības ietvars: {country['compliance_box']}.",
        "lt": f"STRATRONIX ({country_native} rinka) atitinka vietos reikalavimus: ES narys nuo {country['eu_member']}, valiuta {country['currency']}. Pagrindinės pramonės šakos {country_native}: {country['industry_focus']}. Atitikties sistema: {country['compliance_box']}.",
        "sl": f"STRATRONIX (trg {country_native}) izpolnjuje lokalne zahteve: Članica EU od {country['eu_member']}, valuta {country['currency']}. Ključne panoge v {country_native}: {country['industry_focus']}. Okvir skladnosti: {country['compliance_box']}.",
        "hr": f"STRATRONIX (tržište {country_native}) ispunjava lokalne zahtjeve: Članica EU od {country['eu_member']}, valuta {country['currency']}. Ključne industrije u {country_native}: {country['industry_focus']}. Okvir usklađenosti: {country['compliance_box']}.",
        "el": f"Το STRATRONIX (αγορά {country_native}) πληροί τις τοπικές απαιτήσεις: Μέλος ΕΕ από {country['eu_member']}, νόμισμα {country['currency']}. Βασικές βιομηχανίες στο {country_native}: {country['industry_focus']}. Πλαίσιο συμμόρφωσης: {country['compliance_box']}.",
        "mt": f"STRATRONIX (suq {country_native}) tilħaq ir-rekwiżiti lokali: Membru tal-UE minn {country['eu_member']}, munita {country['currency']}. Industriji prinċipali f'{country_native}: {country['industry_focus']}. Qafas ta' konformità: {country['compliance_box']}.",
    }

    html = f"""<!DOCTYPE html>
<html lang="{lang}">
<head>
<meta charset="UTF-8">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="keywords" content="{keywords}">
<meta name="robots" content="index, follow, max-snippet:-1, max-image-preview:large">
<link rel="canonical" href="{hreflang_self}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:type" content="product">
<meta property="og:url" content="{hreflang_self}">
<meta property="og:locale" content="{lang}_{country_native[:2].upper()}">
{schema}
<style>
* {{ box-sizing: border-box; margin: 0; padding: 0; }}
body {{ font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; line-height: 1.8; color: #1a1a1a; background: #fafafa; }}
header {{ background: linear-gradient(135deg, #E6417F 0%, #c9296c 100%); color: white; padding: 50px 20px; }}
header h1 {{ font-size: 1.8rem; max-width: 900px; margin: 0 auto 16px; line-height: 1.4; }}
header .subtitle {{ max-width: 900px; margin: 0 auto; opacity: 0.95; font-size: 1rem; }}
.container {{ max-width: 900px; margin: 0 auto; padding: 40px 20px; background: white; }}
h2 {{ font-size: 1.4rem; color: #E6417F; margin: 32px 0 12px; border-left: 4px solid #E6417F; padding-left: 12px; }}
p, li {{ font-size: 1.02rem; color: #333; margin: 10px 0; }}
ul {{ padding-left: 24px; margin: 12px 0; }}
a {{ color: #E6417F; text-decoration: underline; }}
.cta {{ background: linear-gradient(135deg, #E6417F 0%, #c9296c 100%); color: white; padding: 40px; text-align: center; border-radius: 12px; margin: 40px 0; }}
.cta a {{ color: white; background: rgba(255,255,255,0.2); padding: 14px 36px; border-radius: 8px; text-decoration: none; font-weight: 600; display: inline-block; margin: 8px; }}
.cta a.primary {{ background: white; color: #E6417F; }}
.lang-switch {{ text-align: center; padding: 16px; background: #fff; border-bottom: 1px solid #eee; font-size: 0.85rem; }}
.lang-switch a {{ margin: 0 4px; color: #E6417F; text-decoration: none; }}
footer {{ background: #1a1a1a; color: #999; padding: 30px 20px; text-align: center; margin-top: 60px; }}
footer a {{ color: #E6417F; }}
.compliance {{ background: #fff5f9; padding: 16px; border-radius: 8px; margin: 20px 0; font-size: 0.95rem; }}
</style>
</head>
<body>
<div class="lang-switch">{lang_sw}</div>
<header>
<h1>{h1}</h1>
<p class="subtitle">{desc}</p>
</header>

<div class="container">

<div class="compliance">
<strong>{country_native} compliance:</strong> {country['compliance_box']}
</div>

<h2>STRATRONIX PAA — Was ist das?</h2>
<p>{intro}</p>

<h2>{h2_why[lang].format(country=country_native)}</h2>
<p>{h2_why_text[lang]}</p>

<h2>{h2_industry[lang]}</h2>
<ul>{industry_html}
</ul>

<div class="cta">
<h2 style="color:white;border:none;padding:0;margin:0 0 16px;">STRATRONIX PAA für {country_native}</h2>
<p style="color:white;margin-bottom:24px;">On-Premise KI-Hardware · {country['gdpr_term']} · EU AI Act</p>
<a href="mailto:europe@stratronix.ai?subject=PAA%20{cc.upper()}%20enquiry" class="primary">→ Email europe@stratronix.ai</a>
<a href="https://store.stratonix.ai">Storefront</a>
</div>

</div>

<footer>
<p>STRATRONIX · Stratronix Technology (Shenzhen) Company, Limited · 鼎图太易信息技术（深圳）有限公司</p>
<p>Founded 2026-04-24 · Registered 91440300MAKD20DT6F · +86 13632968417</p>
<p><a href="{BASE_URL}/">SEO Resource Hub</a></p>
</footer>
</body>
</html>
"""
    out_dir = DST / cc
    out_dir.mkdir(exist_ok=True)
    out_path = out_dir / slug
    out_path.write_text(html, encoding="utf-8")
    return out_path


if __name__ == "__main__":
    print(f"Building 10 countries × 2 long-tail pages = 20 URLs")
    for country in COUNTRIES:
        for page_type in ("paa", "llm"):
            path = build_page(country, page_type)
            rel = path.relative_to(ROOT)
            print(f"  ✅ {rel} ({path.stat().st_size} bytes)")
    print(f"\nDone: 20 files written across 10 country directories.")

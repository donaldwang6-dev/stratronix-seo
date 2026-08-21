#!/usr/bin/env python3
"""
CBM 2026-09 邀请函 22 国 generation
- 2026 中国户外·骑行行业 AI 智能体展会 · 9月9日
- 9 平米标准展位 · 主题：骑行行业 AI 工作助手
- 22 国内容（shared source-of-truth 8 语言 + 22 国家落地页）
- 100% native 语言（铁律 15.1）
- Schema.org Event JSON-LD
"""
import os, gzip, json

ROOT = '/home/donald/.openclaw/workspace/stratronix-seo'
BASE = 'https://donaldwang6-dev.github.io/stratronix-seo'
OG_IMAGE = f'{BASE}/og-images/og-image-cbm-2026.png'

# 22 国：完整 native 语言文案
# 16 国为非中文版本：第一语言 native
COUNTRIES = {
    'us': {
        'lang': 'en-US', 'locale': 'en_US', 'country_code': 'us',
        'country_name': 'United States', 'flag': '🇺🇸',
        'city_focus': 'USA · North America market',
        'page_slug': 'cbm-2026-09-united-states',
        'title': 'STRATRONIX @ CBM 2026 · China Outdoor Cycling AI-Agent Expo · September 9, 2026',
        'desc': 'STRATRONIX unveils the STA-100 PAA Private AI-Agent Appliance at CBM 2026 (China Outdoor & Cycling Industry AI Agent Expo) on September 9, 2026. 9 sqm standard booth. Cycling industry AI work assistant. Global list price USD 399.',
        'kw': 'CBM 2026, China Outdoor Expo, Cycling AI, STA-100, PAA, STRATRONIX, Private AI, cycling industry AI assistant, OEM, distributor',
        'hero_h1': 'STRATRONIX @ CBM 2026 — China Outdoor & Cycling Industry AI-Agent Expo',
        'hero_sub': '9 September 2026 · 09:00–17:00 (Wed) · 9 m² Standard Booth',
        'apac_note': "CBM 2026 is a <strong>China-focused industry trade show</strong> with 30,000+ buyers from cycling, outdoor, fitness, and e-commerce channels across China and Southeast Asia.",
        'intro': 'STRATRONIX welcomes our <strong>North American</strong> cycling, outdoor, and fitness industry partners. The STA-100 PAA delivers the world’s first AI Work Assistant specifically tuned for cycling retail, repair, and D2C operations (Shopify, DTC, eBay, Amazon).',
        'compliance_label': 'Cycling-industry AI — built for retailers, brands, and repair shops',
        'compliance_text': 'STA-100 PAA is engineered for the specific workflows of cycling retailers, repair shops, brand owners, and DTC e-commerce operators. On-device LLM means customer data and product fit data never leaves the shop.',
        'why_now_label': 'Why visit CBM 2026 in China — the world’s largest cycling market',
        'why_now_text': 'China is the world’s largest bicycle producer (over 60% of global production) and the fastest-growing e-bike market. CBM 2026 brings <strong>30,000+ buyers</strong> from 30+ countries to source 2027 products. Direct contact with our founder Wang Jie (汪杰) and engineering team.',
        'product_label': 'Cycling AI features',
        'product_items': [
            '🔧 <strong>Workshop AI</strong> — instant repair knowledge base for 500+ bike models (Shimano, SRAM, Bosch, Bafang, Yamaha, Giant, Trek, Specialized)',
            '🛒 <strong>Retail AI Assistant</strong> — 24/7 customer Q&A on bike fit, components, warranty, store hours',
            '📦 <strong>DTC E-commerce AI</strong> — auto-generated product descriptions in 8 languages, automated email responses, cross-border Amazon/eBay/Shopify listing',
            '🚴 <strong>Fleet AI Dispatch</strong> — for bike-share / rental companies, automated booking, GPS tracking, maintenance scheduling',
            '🌍 <strong>8-language UI</strong> — EN / DE / FR / ES / IT / NL / PL / 中文 (CN) included',
        ],
        'booth_label': 'What you’ll see at our 9 m² booth',
        'booth_items': [
            'Live demo: STA-100 PAA running Shimano dealer knowledge base in 10 minutes',
            'AI-powered bike-fit recommendation engine (sizing, comfort, road vs. gravel)',
            'Cycling retail ROI calculator (saves 52K EUR/year for mid-size store)',
            'OEM / distributor partnership program (10–49 units: USD 359 · 50–99: USD 319 · 100+: USD 279)',
            '2-year warranty + 24/7 multilingual support',
        ],
        'cta_label': 'Book a 1-on-1 demo at STRATRONIX booth',
        'cta_text': 'Direct contact with founder Wang Jie (汪杰) and engineering team. Reply within 24 hours.',
        'cta_email1_label': 'Global Sales', 'cta_email1': 'sales@stratronix.ai',
        'cta_email2_label': 'Cycling OEM', 'cta_email2': 'cycling@stratronix.ai',
        'company_text': 'STRATRONIX (鼎图太易) is a 2026-founded AI hardware company in Shenzhen. We develop the STA-100 PAA Private AI-Agent Appliance — the global alternative to cloud-based AI services for industries with strict data privacy and compliance requirements. Core open-source product: OpenClaw (BSD-3-Clause, GitHub 8K+ stars).',
    },
    'uk': {
        'lang': 'en-GB', 'locale': 'en_GB', 'country_code': 'uk',
        'country_name': 'United Kingdom', 'flag': '🇬🇧',
        'city_focus': 'UK & Ireland cycling market',
        'page_slug': 'cbm-2026-09-united-kingdom',
        'title': 'STRATRONIX @ CBM 2026 · China Cycling AI-Agent Expo · 9 Sept 2026 · UK Partners Invited',
        'desc': 'STRATRONIX invites UK & Ireland cycling retailers, distributors, and e-bike brands to CBM 2026 (China Outdoor & Cycling Industry AI Agent Expo) on 9 September 2026. STA-100 PAA — local AI for UK cycling retail, repair, and DTC trade.',
        'kw': 'CBM 2026, UK cycling, STA-100, PAA, UK cycling retail AI, UKCA, GDPR, cycling industry AI assistant',
        'hero_h1': 'STRATRONIX @ CBM 2026 — UK & Ireland Cycling AI Exposition',
        'hero_sub': '9 September 2026 · 09:00–17:00 (Wed) · Hall TBD · 9 m² Standard Booth',
        'apac_note': 'CBM 2026 is a <strong>China-focused industry trade show</strong> with 30,000+ buyers from cycling, outdoor, fitness, and e-commerce channels across China, UK, EU, and APAC.',
        'intro': 'STRATRONIX welcomes our <strong>UK & Ireland</strong> cycling retail, repair, e-bike, and D2C partners. The STA-100 PAA delivers a UK-localised AI Work Assistant built for Halfords-grade retailer groups, independent bike dealers (IBDs), and direct-to-consumer brands (Ribble, Watt, Brompton tier).',
        'compliance_label': 'UK GDPR & UKCA compliant',
        'compliance_text': 'STA-100 PAA is engineered for UK GDPR / Data Protection Act 2018 compliance. All inference local, no data exfiltration, full audit trail. Compatible with Halfords, Evans Cycles, Cycle Republic, Decathlon, and IBD POS systems.',
        'why_now_label': 'Why UK cycling retailers should source from China',
        'why_now_text': 'CBM 2026 is the most efficient 2027 sourcing trip for UK cycling buyers. <strong>30,000+ buyers</strong> from 30+ countries, 2,000+ exhibitors, all major Chinese cycling brands — Giant, Merida, Trinx, XDS, Forever, plus 1,000+ component suppliers. Direct contact with our founder Wang Jie (汪杰) and engineering team.',
        'product_label': 'UK cycling AI features',
        'product_items': [
            '🔧 <strong>Workshop AI</strong> — Shimano, SRAM, Campagnolo, Hope, Brooks, Chris King, Rapha-tier brand knowledge base',
            '🛒 <strong>Retail AI Assistant</strong> — UK customer service voice, Bikefit, Eddy Merckx, Boardman, Orange tier brands',
            '📦 <strong>DTC E-commerce AI</strong> — Coinbase Commerce, Stripe, WooCommerce integration',
            '🇬🇧 <strong>UK English UI</strong> — drop-shipping, returns, ETA tracking, Brexit customs pre-fill',
            '🌍 <strong>GDPR-compliant</strong> — customer data and product fit data never leaves the shop',
        ],
        'booth_label': 'What you’ll see at our 9 m² booth',
        'booth_items': [
            'Live demo: STA-100 PAA running UK IBD knowledge base in 10 minutes',
            'AI bike-fit recommendation engine (Rapha / Ribble / Boardman sizing)',
            'UK cycling retail ROI calculator (saves £45K/year for mid-size IBD)',
            'UK distributor partnership program (10–49 units: £290 · 50–99: £255 · 100+: £220)',
            '2-year warranty + 24/7 UK English support',
        ],
        'cta_label': 'Book a 1-on-1 demo at STRATRONIX booth',
        'cta_text': 'Direct contact with founder Wang Jie (汪杰) and engineering team. Reply within 24 hours.',
        'cta_email1_label': 'UK & EU Sales', 'cta_email1': 'sales@stratronix.ai',
        'cta_email2_label': 'Cycling OEM', 'cta_email2': 'cycling@stratronix.ai',
        'company_text': 'STRATRONIX (鼎图太易) is a 2026-founded AI hardware company in Shenzhen. We develop the STA-100 PAA Private AI-Agent Appliance — the global alternative to cloud-based AI services for industries with strict data privacy and compliance requirements. Core open-source product: OpenClaw (BSD-3-Clause, GitHub 8K+ stars).',
    },
    'de': {
        'lang': 'de-DE', 'locale': 'de_DE', 'country_code': 'de',
        'country_name': 'Deutschland', 'flag': '🇩🇪',
        'city_focus': 'DACH-Region (Deutschland / Österreich / Schweiz)',
        'page_slug': 'cbm-2026-09-deutschland',
        'title': 'STRATRONIX @ CBM 2026 · China Outdoor & Radbranche AI-Agent Expo · 9. September 2026',
        'desc': 'STRATRONIX präsentiert STA-100 PAA Private AI-Agent Appliance auf der CBM 2026 (China Outdoor & Radbranche AI-Agent Expo) am 9. September 2026. 9 m² Standardstand. AI-Arbeitsassistent für die Fahrradbranche. Weltweiter Listenpreis 399 USD.',
        'kw': 'CBM 2026, Fahrradbranche, Radbranche AI, STA-100, PAA, STRATRONIX, DSGVO, EU AI Act, E-Bike, Fahrradhandel',
        'hero_h1': 'STRATRONIX @ CBM 2026 — China Outdoor & Radbranche AI-Agent Expo',
        'hero_sub': '9. September 2026 · 09:00–17:00 (Mi) · 9 m² Standardstand',
        'apac_note': 'CBM 2026 ist eine <strong>chinesische Fachmesse</strong> mit 30.000+ Einkäufern aus den Bereichen Radsport, Outdoor, Fitness und E-Commerce in China, Europa und APAC.',
        'intro': 'STRATRONIX heißt unsere <strong>DACH-Partner</strong> aus Deutschland, Österreich und der Schweiz herzlich willkommen. Der STA-100 PAA ist ein lokaler AI-Arbeitsassistent für Fahrradhandel, Werkstatt, E-Bike-Marken und DTC-Händler (Canyon, Rose, Cube, Riese & Müller, Bosch eBike Systems).',
        'compliance_label': 'DSGVO- & EU-AI-Act-konform',
        'compliance_text': 'STA-100 PAA erfüllt die strengen Anforderungen der <strong>DSGVO</strong> und des <strong>EU AI Act</strong>. Lokale LLM-Inferenz, vollständige Audit-Trails, keine Datenexfiltration. Kompatibel mit Bosch eBike Systems, Shimano STEPS, Bafang, Yamaha PW.',
        'why_now_label': 'Warum DACH-Fahrradhändler nach China reisen sollten',
        'why_now_text': 'CBM 2026 ist die effizienteste Sourcing-Reise 2027 für DACH-Fahrradeinkäufer. <strong>30.000+ Einkäufer</strong> aus 30+ Ländern, 2.000+ Aussteller, alle großen chinesischen Fahrradmarken — Giant, Merida, Trinx, XDS, Forever und 1.000+ Komponentenzulieferer. Direkter Kontakt zum Gründer Wang Jie (汪杰) und Engineering-Team.',
        'product_label': 'DACH-Fahrrad AI-Funktionen',
        'product_items': [
            '🔧 <strong>Werkstatt-AI</strong> — Bosch eBike Systems, Shimano STEPS, Bafang, Yamaha, Brose, Continental eBike System',
            '🛒 <strong>Handels-AI-Assistent</strong> — Canyon, Rose, Cube, Riese & Müller, Stevens, Bicycles, Koga-Mitarbeiter-Schulung',
            '📦 <strong>DTC E-Commerce AI</strong> — Shopify, Shopware, WooCommerce, automatische Produktbeschreibungen auf Deutsch',
            '🇩🇪 <strong>Deutsche UI</strong> — DSGVO-konform, deutsches Steuer- und Mehrwertsteuer-System',
            '🌍 <strong>8-Sprachen-UI</strong> — DE / EN / FR / ES / IT / NL / PL / 中文 (CN)',
        ],
        'booth_label': 'Was Sie an unserem 9 m² Stand erwartet',
        'booth_items': [
            'Live-Demo: STA-100 PAA mit Bosch eBike-Wissensdatenbank in 10 Minuten',
            'KI-Bike-Fit-Empfehlungsmaschine (Canyon / Rose / Cube Größenberatung)',
            'DACH-Fahrradhandel ROI-Rechner (spart 52K EUR/Jahr für mittelgroßen Händler)',
            'DACH-Vertriebsprogramm (10–49 Stück: 359 USD · 50–99: 319 USD · 100+: 279 USD)',
            '2 Jahre Garantie + 24/7 deutschsprachiger Support',
        ],
        'cta_label': 'Vereinbaren Sie eine 1-zu-1-Demo am STRATRONIX-Stand',
        'cta_text': 'Direkter Draht zum Gründer Wang Jie (汪杰) und Engineering-Team. Antwort innerhalb von 24 Stunden.',
        'cta_email1_label': 'DACH-Vertrieb', 'cta_email1': 'sales@stratronix.ai',
        'cta_email2_label': 'Fahrrad-OEM', 'cta_email2': 'cycling@stratronix.ai',
        'company_text': 'STRATRONIX (鼎图太易) ist ein 2026 in Shenzhen gegründetes AI-Hardware-Unternehmen. Wir entwickeln den STA-100 PAA Private AI-Agent Appliance — die globale Alternative zu cloud-basierten AI-Diensten für Branchen mit hohen Datenschutz- und Compliance-Anforderungen. Hauptprodukt: OpenClaw, unser Open-Source AI-Agent-Framework (BSD-3-Clause, GitHub 8K+ Sterne).',
    },
    'fr': {
        'lang': 'fr-FR', 'locale': 'fr_FR', 'country_code': 'fr',
        'country_name': 'France', 'flag': '🇫🇷',
        'city_focus': 'France / Belgique / Suisse / Luxembourg',
        'page_slug': 'cbm-2026-09-france',
        'title': 'STRATRONIX @ CBM 2026 · Salon IA Vélo & Outdoor Chine · 9 septembre 2026',
        'desc': 'STRATRONIX présente le STA-100 PAA Private AI-Agent Appliance au CBM 2026 (Salon IA Vélo & Outdoor de Chine) le 9 septembre 2026. Stand 9 m². Assistant IA pour l\'industrie cycliste. Prix catalogue mondial 399 USD.',
        'kw': 'CBM 2026, Salon vélo Chine, IA vélo, STA-100, PAA, STRATRONIX, RGPD, EU AI Act, vélo électrique, vélo retail',
        'hero_h1': "STRATRONIX @ CBM 2026 — Salon IA Vélo & Outdoor de Chine",
        'hero_sub': '9 septembre 2026 · 09:00–17:00 (mer) · Hall TBD · Stand 9 m²',
        'apac_note': 'CBM 2026 est un <strong>salon professionnel chinois</strong> avec plus de 30 000 acheteurs des secteurs du vélo, de l\'outdoor, du fitness et du e-commerce en Chine, en Europe et en APAC.',
        'intro': "STRATRONIX accueille chaleureusement nos partenaires <strong>francophones</strong> de France, Belgique, Suisse et Luxembourg. Le STA-100 PAA est un assistant IA local pour le commerce de détail vélo, la réparation, les marques d'e-bike et le DTC (Decathlon, Go Sport, Intersport, Vélo & Oxygen, Culturavélo).",
        'compliance_label': 'Conforme RGPD & EU AI Act',
        'compliance_text': 'STA-100 PAA satisfait aux exigences du <strong>RGPD</strong> et de l\'<strong>EU AI Act</strong>. Inférence LLM locale, aucune exfiltration de données, pistes d\'audit complètes. Compatible avec Bosch eBike Systems, Shimano STEPS, Bafang, Yamaha PW.',
        'why_now_label': "Pourquoi les détaillants vélo francophones devraient s'approvisionner en Chine",
        'why_now_text': "CBM 2026 est le voyage de sourcing 2027 le plus efficace pour les acheteurs vélo francophones. <strong>30 000+ acheteurs</strong> de 30+ pays, 2 000+ exposants, toutes les grandes marques chinoises — Giant, Merida, Trinx, XDS, Eternal et 1 000+ fournisseurs de composants. Contact direct avec notre fondateur Wang Jie (汪杰) et l'équipe d'ingénierie.",
        'product_label': 'Fonctionnalités IA vélo francophones',
        'product_items': [
            "🔧 <strong>IA d'atelier</strong> — Bosch eBike Systems, Shimano STEPS, Bafang, Yamaha, Brose, Continental eBike System",
            "🛒 <strong>Assistant IA retail</strong> — Decathlon, Go Sport, Intersport, Vélo & Oxygen, Culturavélo, Bicycletterie André",
            "📦 <strong>IA e-commerce DTC</strong> — Shopify, PrestaShop, WooCommerce, descriptions produits automatiques en français",
            "🇫🇷 <strong>Interface française</strong> — TVA française, système de garantie 2 ans, support SIRET/TVA intracommunautaire",
            "🌍 <strong>Interface 8 langues</strong> — FR / EN / DE / ES / IT / NL / PL / 中文 (CN)",
        ],
        'booth_label': "Ce qui vous attend au stand 9 m²",
        'booth_items': [
            "Démo live : STA-100 PAA avec base de connaissances Bosch eBike en 10 minutes",
            "Moteur de recommandation IA bike-fit (Canyon / Rose / Cube sizing)",
            "Calculateur ROI retail vélo francophone (économise 52K EUR/an pour détaillant moyen)",
            "Programme de distribution (10–49 unités : 359 USD · 50–99 : 319 USD · 100+ : 279 USD)",
            "Garantie 2 ans + support 24/7 en français",
        ],
        'cta_label': 'Réservez une démo 1-à-1 au stand STRATRONIX',
        'cta_text': 'Contact direct avec le fondateur Wang Jie (汪杰) et l\'équipe d\'ingénierie. Réponse sous 24 heures.',
        'cta_email1_label': 'Ventes FR/BE/CH', 'cta_email1': 'sales@stratronix.ai',
        'cta_email2_label': 'OEM Vélo', 'cta_email2': 'cycling@stratronix.ai',
        'company_text': "STRATRONIX (鼎图太易) est une entreprise de matériel AI fondée à Shenzhen en 2026. Nous développons le STA-100 PAA Private AI-Agent Appliance — l'alternative mondiale aux services AI cloud pour les industries avec des exigences strictes de confidentialité et de conformité. Produit open-source principal : OpenClaw (BSD-3-Clause, GitHub 8K+ étoiles).",
    },
    'es': {
        'lang': 'es-ES', 'locale': 'es_ES', 'country_code': 'es',
        'country_name': 'España', 'flag': '🇪🇸',
        'city_focus': 'España y mercado latinoamericano',
        'page_slug': 'cbm-2026-09-espana',
        'title': 'STRATRONIX @ CBM 2026 · Exposición IA Ciclismo & Outdoor China · 9 septiembre 2026',
        'desc': 'STRATRONIX presenta STA-100 PAA Private AI-Agent Appliance en CBM 2026 (Exposición IA Ciclismo & Outdoor de China) el 9 de septiembre de 2026. Stand 9 m². Asistente IA para industria ciclista. Precio mundial 399 USD.',
        'kw': 'CBM 2026, exposición ciclismo China, IA ciclismo, STA-100, PAA, STRATRONIX, RGPD, EU AI Act, bicicleta eléctrica, retail ciclista',
        'hero_h1': 'STRATRONIX @ CBM 2026 — Exposición IA Ciclismo & Outdoor China',
        'hero_sub': '9 septiembre 2026 · 09:00–17:00 (mié) · Pabellón TBD · Stand 9 m²',
        'apac_note': 'CBM 2026 es una <strong>feria profesional china</strong> con más de 30 000 compradores de los sectores de ciclismo, outdoor, fitness y e-commerce en China, Europa y APAC.',
        'intro': 'STRATRONIX da la bienvenida a nuestros socios <strong>hispanohablantes</strong> de España y América Latina. El STA-100 PAA es un asistente IA local para el comercio minorista ciclista, talleres, marcas de e-bike y DTC (Decathlon, BH, Orbea, Merida, Scott, Trek).',
        'compliance_label': 'Cumple RGPD y EU AI Act',
        'compliance_text': 'STA-100 PAA cumple los requisitos del <strong>RGPD</strong> y del <strong>EU AI Act</strong>. Inferencia LLM local, sin exfiltración de datos, pistas de auditoría completas. Compatible con Bosch eBike Systems, Shimano STEPS, Bafang, Yamaha PW.',
        'why_now_label': 'Por qué los minoristas ciclistas hispanos deberían visitar China',
        'why_now_text': 'CBM 2026 es el viaje de aprovisionamiento 2027 más eficiente para compradores ciclistas hispanos. <strong>30 000+ compradores</strong> de 30+ países, 2 000+ expositores, todas las grandes marcas chinas — Giant, Merida, Trinx, XDS, Eternal y 1 000+ proveedores de componentes. Contacto directo con nuestro fundador Wang Jie (汪杰) y el equipo de ingeniería.',
        'product_label': 'Funciones IA ciclismo en español',
        'product_items': [
            '🔧 <strong>IA de taller</strong> — Bosch eBike Systems, Shimano STEPS, Bafang, Yamaha, Brose, Continental eBike System',
            '🛒 <strong>Asistente IA retail</strong> — Decathlon, BH, Orbea, Merida, Scott, Trek, Cervélo, Conor',
            '📦 <strong>IA e-commerce DTC</strong> — Shopify, WooCommerce, PrestaShop, descripciones automáticas en español',
            '🇪🇸 <strong>Interfaz español</strong> — IVA español, NIF/CIF, sistema de facturación',
            '🌍 <strong>Interfaz 8 idiomas</strong> — ES / EN / DE / FR / IT / NL / PL / 中文 (CN)',
        ],
        'booth_label': 'Qué le espera en nuestro stand de 9 m²',
        'booth_items': [
            'Demo en vivo: STA-100 PAA con base de conocimientos Bosch eBike en 10 minutos',
            'Motor de recomendación IA bike-fit (Canyon / Rose / Cube tallaje)',
            'Calculadora ROI retail ciclista (ahorra 52K EUR/año para tienda mediana)',
            'Programa de distribución (10–49 unidades: 359 USD · 50–99: 319 USD · 100+: 279 USD)',
            'Garantía 2 años + soporte 24/7 en español',
        ],
        'cta_label': 'Reserve una demo 1-a-1 en el stand de STRATRONIX',
        'cta_text': 'Contacto directo con el fundador Wang Jie (汪杰) y el equipo de ingeniería. Respuesta en 24 horas.',
        'cta_email1_label': 'Ventas ES/LATAM', 'cta_email1': 'sales@stratronix.ai',
        'cta_email2_label': 'OEM Ciclismo', 'cta_email2': 'cycling@stratronix.ai',
        'company_text': 'STRATRONIX (鼎图太易) es una empresa de hardware AI fundada en Shenzhen en 2026. Desarrollamos el STA-100 PAA Private AI-Agent Appliance — la alternativa mundial a los servicios AI cloud para industrias con requisitos estrictos de privacidad y cumplimiento. Producto open-source principal: OpenClaw (BSD-3-Clause, GitHub 8K+ estrellas).',
    },
    'it': {
        'lang': 'it-IT', 'locale': 'it_IT', 'country_code': 'it',
        'country_name': 'Italia', 'flag': '🇮🇹',
        'city_focus': 'Italia e mercato mediterraneo',
        'page_slug': 'cbm-2026-09-italia',
        'title': 'STRATRONIX @ CBM 2026 · Fiera IA Ciclismo & Outdoor Cina · 9 settembre 2026',
        'desc': "STRATRONIX presenta STA-100 PAA Private AI-Agent Appliance al CBM 2026 (Fiera IA Ciclismo & Outdoor della Cina) il 9 settembre 2026. Stand 9 m². Assistente IA per l'industria ciclistica. Prezzo globale 399 USD.",
        'kw': 'CBM 2026, fiera ciclismo Cina, IA ciclismo, STA-100, PAA, STRATRONIX, GDPR, EU AI Act, e-bike, retail ciclistico',
        'hero_h1': 'STRATRONIX @ CBM 2026 — Fiera IA Ciclismo & Outdoor della Cina',
        'hero_sub': '9 settembre 2026 · 09:00–17:00 (mer) · Padiglione TBD · Stand 9 m²',
        'apac_note': 'CBM 2026 è una <strong>feria professional cinese</strong> con oltre 30 000 acquirenti dei settori ciclismo, outdoor, fitness ed e-commerce in Cina, Europa e APAC.',
        'intro': "STRATRONIX dà il benvenuto ai nostri partner <strong>italiani</strong>. Lo STA-100 PAA è un assistente IA locale per il commercio al dettaglio ciclistico, le officine, i marchi di e-bike e DTC (Decathlon, Cicli Pizeta, BiciSport, De Rosa, Pinarello, Colnago, Campagnolo).",
        'compliance_label': 'Conforme GDPR e EU AI Act',
        'compliance_text': "STA-100 PAA soddisfa i requisiti del <strong>GDPR</strong> e dell'<strong>EU AI Act</strong>. Inferenza LLM locale, nessuna esfiltrazione di dati, audit trail completi. Compatibile con Bosch eBike Systems, Shimano STEPS, Bafang, Yamaha PW, Campagnolo EPS.",
        'why_now_label': 'Perché i rivenditori ciclisti italiani dovrebbero visitare la Cina',
        'why_now_text': 'CBM 2026 è il viaggio di sourcing 2027 più efficiente per gli acquirenti ciclisti italiani. <strong>30 000+ acquirenti</strong> da 30+ paesi, 2 000+ espositori, tutti i grandi marchi cinesi — Giant, Merida, Trinx, XDS, Eternal e 1 000+ fornitori di componenti. Contatto diretto con il nostro fondatore Wang Jie (汪杰) e il team di ingegneria.',
        'product_label': 'Funzionalità IA ciclismo in italiano',
        'product_items': [
            '🔧 <strong>IA officina</strong> — Bosch eBike Systems, Shimano STEPS, Bafang, Yamaha, Brose, Campagnolo EPS',
            '🛒 <strong>Assistente IA retail</strong> — Decathlon, Cicli Pizeta, BiciSport, De Rosa, Pinarello, Colnago, Campagnolo, Selle Italia',
            '📦 <strong>IA e-commerce DTC</strong> — Shopify, WooCommerce, PrestaShop, descrizioni automatiche in italiano',
            '🇮🇹 <strong>Interfaccia italiana</strong> — IVA italiana, codice fiscale, fatturazione elettronica',
            '🌍 <strong>Interfaccia 8 lingue</strong> — IT / EN / DE / FR / ES / NL / PL / 中文 (CN)',
        ],
        'booth_label': 'Cosa vi aspetta al nostro stand di 9 m²',
        'booth_items': [
            'Demo live: STA-100 PAA con base di conoscenze Bosch eBike in 10 minuti',
            'Motore di raccomandazione IA bike-fit (misure Canyon / Rose / Cube)',
            'Calcolatore ROI retail ciclistico (risparmia 52K EUR/anno per negozio medio)',
            'Programma di distribuzione (10–49 unità: 359 USD · 50–99: 319 USD · 100+: 279 USD)',
            'Garanzia 2 anni + supporto 24/7 in italiano',
        ],
        'cta_label': 'Prenotate una demo 1-a-1 allo stand STRATRONIX',
        'cta_text': 'Contatto diretto con il fondatore Wang Jie (汪杰) e il team di ingegneria. Risposta entro 24 ore.',
        'cta_email1_label': 'Vendite IT', 'cta_email1': 'sales@stratronix.ai',
        'cta_email2_label': 'OEM Ciclismo', 'cta_email2': 'cycling@stratronix.ai',
        'company_text': "STRATRONIX (鼎图太易) è un'azienda di hardware AI fondata a Shenzhen nel 2026. Sviluppiamo lo STA-100 PAA Private AI-Agent Appliance — l'alternativa globale ai servizi AI cloud per industrie con requisiti rigorosi di privacy e conformità. Prodotto open-source principale: OpenClaw (BSD-3-Clause, GitHub 8K+ stelle).",
    },
    'nl': {
        'lang': 'nl-NL', 'locale': 'nl_NL', 'country_code': 'nl',
        'country_name': 'Nederland', 'flag': '🇳🇱',
        'city_focus': 'Nederland & België',
        'page_slug': 'cbm-2026-09-nederland',
        'title': 'STRATRONIX @ CBM 2026 · China Fiets AI-Agent Expo · 9 september 2026',
        'desc': 'STRATRONIX presenteert STA-100 PAA Private AI-Agent Appliance op CBM 2026 (China Outdoor & Fiets AI-Agent Expo) op 9 september 2026. Stand 9 m². AI-werkassistent voor de fietsindustrie. Wereldprijs 399 USD.',
        'kw': 'CBM 2026, China fietsbeurs, fiets AI, STA-100, PAA, STRATRONIX, AVG, EU AI Act, e-bike, fiets retail',
        'hero_h1': 'STRATRONIX @ CBM 2026 — China Outdoor & Fiets AI-Agent Expo',
        'hero_sub': '9 september 2026 · 09:00–17:00 (wo) · Hal TBD · Stand 9 m²',
        'apac_note': 'CBM 2026 is een <strong>Chinese vakbeurs</strong> met 30.000+ inkopers uit de fiets-, outdoor-, fitness- en e-commerce-sector in China, Europa en APAC.',
        'intro': 'STRATRONIX verwelkomt onze <strong>Nederlandse en Belgische</strong> fiets-, outdoor- en e-bike partners. De STA-100 PAA is een lokale AI-werkassistent voor fietsretail, werkplaatsen, e-bike merken en DTC (Decathlon, Gazelle, Batavus, Koga, Cortina, Stella, VanMoof, Swapfiets).',
        'compliance_label': 'AVG- & EU AI Act-conform',
        'compliance_text': 'STA-100 PAA voldoet aan de <strong>AVG</strong> (Algemene Verordening Gegevensbescherming) en de <strong>EU AI Act</strong>. Lokale LLM-inferentie, geen data-exfiltratie, volledige audit-trails. Compatibel met Bosch eBike Systems, Shimano STEPS, Bafang, Yamaha PW.',
        'why_now_label': 'Waarom Nederlandse fietsretailers naar China zouden moeten reizen',
        'why_now_text': 'CBM 2026 is de meest efficiënte 2027 inkoopreis voor Nederlandse en Belgische fietsinkopers. <strong>30.000+ inkopers</strong> uit 30+ landen, 2.000+ exposanten, alle grote Chinese fietsmerken — Giant, Merida, Trinx, XDS, Forever en 1.000+ componentenleveranciers. Direct contact met onze oprichter Wang Jie (汪杰) en engineering team.',
        'product_label': 'Nederlandse fiets AI-functies',
        'product_items': [
            '🔧 <strong>Werkplaats-AI</strong> — Bosch eBike Systems, Shimano STEPS, Bafang, Yamaha, Brose, Continental eBike System',
            '🛒 <strong>Retail AI-Assistent</strong> — Decathlon, Gazelle, Batavus, Koga, Cortina, Stella, VanMoof, Swapfiets',
            '📦 <strong>DTC E-commerce AI</strong> — Shopify, WooCommerce, automatische productbeschrijvingen in het Nederlands',
            '🇳🇱 <strong>Nederlandse UI</strong> — BTW-systeem, KvK-nummer, facturatie',
            '🌍 <strong>8-talen UI</strong> — NL / EN / DE / FR / ES / IT / PL / 中文 (CN)',
        ],
        'booth_label': 'Wat u kunt verwachten op onze 9 m² stand',
        'booth_items': [
            'Live demo: STA-100 PAA met Bosch eBike-kennisbank in 10 minuten',
            'AI bike-fit aanbevelingsengine (Canyon / Rose / Cube maten)',
            'NL/BE fietsretail ROI-berekenaar (bespaart 52K EUR/jaar voor middelgrote winkel)',
            'NL/BE distributieprogramma (10–49 stuks: 359 USD · 50–99: 319 USD · 100+: 279 USD)',
            '2 jaar garantie + 24/7 Nederlandstalige support',
        ],
        'cta_label': 'Boek een 1-op-1 demo op de STRATRONIX-stand',
        'cta_text': 'Direct contact met oprichter Wang Jie (汪杰) en engineering team. Antwoord binnen 24 uur.',
        'cta_email1_label': 'NL/BE Verkoop', 'cta_email1': 'sales@stratronix.ai',
        'cta_email2_label': 'Fiets OEM', 'cta_email2': 'cycling@stratronix.ai',
        'company_text': 'STRATRONIX (鼎图太易) is een in 2026 opgericht AI-hardwarebedrijf in Shenzhen. Wij ontwikkelen de STA-100 PAA Private AI-Agent Appliance — het wereldwijde alternatief voor cloud-gebaseerde AI-diensten voor industrieën met strikte dataprivacy- en compliance-eisen. Kern open-source product: OpenClaw (BSD-3-Clause, GitHub 8K+ sterren).',
    },
    'pl': {
        'lang': 'pl-PL', 'locale': 'pl_PL', 'country_code': 'pl',
        'country_name': 'Polska', 'flag': '🇵🇱',
        'city_focus': 'Polska i Europa Środkowo-Wschodnia',
        'page_slug': 'cbm-2026-09-polska',
        'title': 'STRATRONIX @ CBM 2026 · Targi AI Rower & Outdoor Chiny · 9 września 2026',
        'desc': 'STRATRONIX prezentuje STA-100 PAA Private AI-Agent Appliance na CBM 2026 (Targi AI Rower & Outdoor w Chinach) 9 września 2026. Stoisko 9 m². Asystent AI dla branży rowerowej. Światowa cena 399 USD.',
        'kw': 'CBM 2026, targi rowerowe Chiny, AI rower, STA-100, PAA, STRATRONIX, RODO, EU AI Act, e-bike, retail rowerowy',
        'hero_h1': 'STRATRONIX @ CBM 2026 — Targi AI Rower & Outdoor w Chinach',
        'hero_sub': '9 września 2026 · 09:00–17:00 (śr) · Hala TBD · Stoisko 9 m²',
        'apac_note': 'CBM 2026 to <strong>chińskie targi branżowe</strong> z 30 000+ kupcami z sektorów rowerowego, outdoor, fitness i e-commerce w Chinach, Europie i APAC.',
        'intro': 'STRATRONIX wita naszych <strong>polskich</strong> partnerów rowerowych, outdoor i e-bike. STA-100 PAA to lokalny asystent AI dla sklepów rowerowych, warsztatów, marek e-bike i DTC (Decathlon, Kross, Romet, Dartmoor, Author, Accent, 4ever, Unibike).',
        'compliance_label': 'Zgodny z RODO i EU AI Act',
        'compliance_text': 'STA-100 PAA spełnia wymogi <strong>RODO</strong> i <strong>EU AI Act</strong>. Lokalne wnioskowanie LLM, brak eksfiltracji danych, pełne audyty. Kompatybilny z Bosch eBike Systems, Shimano STEPS, Bafang, Yamaha PW.',
        'why_now_label': 'Dlaczego polscy sprzedawcy rowerów powinni odwiedzić Chiny',
        'why_now_text': 'CBM 2026 to najbardziej efektywna podróż sourcingowa 2027 dla polskich kupców rowerowych. <strong>30 000+ kupców</strong> z 30+ krajów, 2 000+ wystawców, wszystkie wielkie chińskie marki rowerowe — Giant, Merida, Trinx, XDS, Forever i 1 000+ dostawców komponentów. Bezpośredni kontakt z naszym założycielem Wang Jie (汪杰) i zespołem inżynierów.',
        'product_label': 'Polskie funkcje AI rowerowego',
        'product_items': [
            '🔧 <strong>AI warsztatu</strong> — Bosch eBike Systems, Shimano STEPS, Bafang, Yamaha, Brose, Continental eBike System',
            '🛒 <strong>Asystent AI retail</strong> — Decathlon, Kross, Romet, Dartmoor, Author, Accent, 4ever, Unibike',
            '📦 <strong>AI e-commerce DTC</strong> — Shopify, WooCommerce, automatyczne opisy produktów po polsku',
            '🇵🇱 <strong>Polski interfejs</strong> — system VAT, NIP, fakturowanie',
            '🌍 <strong>Interfejs 8-języczny</strong> — PL / EN / DE / FR / ES / IT / NL / 中文 (CN)',
        ],
        'booth_label': 'Co czeka na Państwa na naszym stoisku 9 m²',
        'booth_items': [
            'Demo na żywo: STA-100 PAA z bazą wiedzy Bosch eBike w 10 minut',
            'Silnik rekomendacji AI bike-fit (rozmiary Canyon / Rose / Cube)',
            'Kalkulator ROI polskiego retail rowerowego (oszczędza 52K EUR/rok dla średniego sklepu)',
            'Program dystrybucji PL (10–49 sztuk: 359 USD · 50–99: 319 USD · 100+: 279 USD)',
            '2 lata gwarancji + wsparcie 24/7 po polsku',
        ],
        'cta_label': 'Zarezerwuj demo 1-na-1 na stoisku STRATRONIX',
        'cta_text': 'Bezpośredni kontakt z założycielem Wang Jie (汪杰) i zespołem inżynierów. Odpowiedź w 24 godziny.',
        'cta_email1_label': 'Sprzedaż PL', 'cta_email1': 'sales@stratronix.ai',
        'cta_email2_label': 'OEM Rower', 'cta_email2': 'cycling@stratronix.ai',
        'company_text': 'STRATRONIX (鼎图太易) to założona w 2026 roku firma AI hardware w Shenzhen. Opracowujemy STA-100 PAA Private AI-Agent Appliance — globalną alternatywę dla cloudowych usług AI dla branż z rygorystycznymi wymogami prywatności danych i zgodności. Główny produkt open-source: OpenClaw (BSD-3-Clause, GitHub 8K+ gwiazdek).',
    },
    'jp': {
        'lang': 'ja-JP', 'locale': 'ja_JP', 'country_code': 'jp',
        'country_name': '日本', 'flag': '🇯🇵',
        'city_focus': '日本市場',
        'page_slug': 'cbm-2026-09-japan',
        'title': 'STRATRONIX @ CBM 2026 · 中国アウトドア・自転車業界AIエージェント博覧会 · 2026年9月9日',
        'desc': 'STRATRONIXは2026年9月9日に中国で開催されるCBM 2026（中国アウトドア・自転車業界AIエージェント博覧会）にSTA-100 PAA Private AI-Agent Applianceを出展します。9平米標準ブース。自転車業界向けAI業務アシスタント。世界統一ガイド価格399 USD。',
        'kw': 'CBM 2026, 中国自転車博覧会, 自転車AI, STA-100, PAA, STRATRONIX, プライベートAI, e-bike, 自転車販売店',
        'hero_h1': 'STRATRONIX @ CBM 2026 — 中国アウトドア・自転車業界AIエージェント博覧会',
        'hero_sub': '2026年9月9日 · 09:00–17:00（水）· 9平米標準ブース',
        'apac_note': 'CBM 2026は中国・欧州・APACから30,000人以上のバイヤーが参加する<strong>中国業界専門見本市</strong>です。',
        'intro': 'STRATRONIXは<strong>日本市場</strong>のパートナー（ブリヂストンサイクル、ヤマハ発動機、Panasonic、SHIMANO、GIANT、トレック）を歓迎します。STA-100 PAAは自転車販売店、修理工房、e-bikeブランド、DTC向けの日本語AI業務アシスタントです。',
        'compliance_label': '個人情報保護法・GDPRコンプライアンス',
        'compliance_text': 'STA-100 PAAは<strong>個人情報保護法</strong>、<strong>GDPR</strong>、<strong>EU AI Act</strong>の要件を満たします。ローカルLLM推論、データ流出なし、完全な監査証跡。SHIMANO STEPS、YAMAHA PW、BOSCH eBike Systems対応。',
        'why_now_label': '日本の自転車小売店が中国を訪問するべき理由',
        'why_now_text': 'CBM 2026は2027年の日本バイヤー向けで最も効率的な調達旅行です。<strong>30,000人以上のバイヤー</strong>（30か国以上）、2,000以上の出展者、すべての主要中国自転車ブランド — Giant、Merida、Trinx、XDS、Forever、および1,000以上の部品サプライヤー。創業者Wang Jie（汪杰）とエンジニアリングチームとの直接打ち合わせ。',
        'product_label': '日本自転車AI機能',
        'product_items': [
            '🔧 <strong>工房AI</strong> — SHIMANO STEPS、YAMAHA PW、BOSCH eBike Systems、Panasonic、Bafang、Bro',
            '🛒 <strong>小売AIアシスタント</strong> — ブリヂストンサイクル、ヤマハ発動機、Panasonic、SHIMANO、GIANT、トレック',
            '📦 <strong>DTC EコマースAI</strong> — Shopify、WooCommerce、楽天、Amazon JP対応の自動商品説明',
            '🇯🇵 <strong>日本語UI</strong> — 消費税、インボイス制度、軽減税率対応',
            '🌍 <strong>8言語UI</strong> — JA / EN / DE / FR / ES / IT / NL / 中文',
        ],
        'booth_label': '9平米ブースで体験できること',
        'booth_items': [
            'ライブデモ：STA-100 PAAでSHIMANO STEPSナレッジベースを10分で構築',
            'AI bike-fit推奨エンジン（Canyon / Rose / Cubeサイジング）',
            '日本自転車小売ROI計算機（中規模店で年間52K EUR削減）',
            '日本販売代理店プログラム（10–49台：359 USD · 50–99：319 USD · 100+：279 USD）',
            '2年保証 + 24/7日本語サポート',
        ],
        'cta_label': 'STRATRONIXブースで1対1デモを予約',
        'cta_text': '創業者Wang Jie（汪杰）とエンジニアリングチームに直接連絡。24時間以内に返信。',
        'cta_email1_label': '日本営業', 'cta_email1': 'sales@stratronix.ai',
        'cta_email2_label': '自転車OEM', 'cta_email2': 'cycling@stratronix.ai',
        'company_text': 'STRATRONIX（鼎图太易）は2026年に深圳で設立されたAIハードウェア企業です。STA-100 PAA Private AI-Agent Appliance — 厳格なデータプライバシーとコンプライアンス要件を持つ産業向けのクラウドベースAIサービスのグローバル代替品を開発しています。コアオープンソース製品：OpenClaw（BSD-3-Clause、GitHub 8K+スター）。',
    },
    'kr': {
        'lang': 'ko-KR', 'locale': 'ko_KR', 'country_code': 'kr',
        'country_name': '한국', 'flag': '🇰🇷',
        'city_focus': '한국 시장',
        'page_slug': 'cbm-2026-09-korea',
        'title': 'STRATRONIX @ CBM 2026 · 중국 아웃도어·자전거 업계 AI 에이전트 박람회 · 2026년 9월 9일',
        'desc': 'STRATRONIX는 2026년 9월 9일 중국에서 개최되는 CBM 2026(중국 아웃도어·자전거 업계 AI 에이전트 박람회)에 STA-100 PAA Private AI-Agent Appliance을展出합니다. 9평 표준 부스. 자전거 업계용 AI 업무 어시스턴트. 세계 통일 가이드 가격 399 USD.',
        'kw': 'CBM 2026, 중국 자전거 박람회, 자전거 AI, STA-100, PAA, STRATRONIX, 프라이빗 AI, e-bike, 자전거 소매',
        'hero_h1': 'STRATRONIX @ CBM 2026 — 중국 아웃도어·자전거 업계 AI 에이전트 박람회',
        'hero_sub': '2026년 9월 9일 · 09:00–17:00 (수) · 9평 표준 부스',
        'apac_note': 'CBM 2026은 중국·유럽·APAC에서 30,000명 이상의 바이어가 참가하는 <strong>중국 업계 전문 박람회</strong>입니다.',
        'intro': 'STRATRONIX는 <strong>한국 시장</strong> 파트너 (삼천리자전거, 알톤스포츠, BIKE24, 셔플, Giant Korea, Trek Korea, Shimano Korea)를 환영합니다. STA-100 PAA는 자전거 소매점, 수리 공방, e-bike 브랜드, DTC를 위한 한국어 AI 업무 어시스턴트입니다.',
        'compliance_label': '개인정보보호법·GDPR 컴플라이언스',
        'compliance_text': 'STA-100 PAA는 <strong>개인정보보호법</strong>, <strong>GDPR</strong>, <strong>EU AI Act</strong>의 요구사항을 충족합니다. 로컬 LLM 추론, 데이터 유출 없음, 완전한 감사 추적. Shimano STEPS, Yamaha PW, Bosch eBike Systems 호환.',
        'why_now_label': '한국 자전거 소매상이 중국을 방문해야 하는 이유',
        'why_now_text': 'CBM 2026은 2027년 한국 바이어를 위한 가장 효율적인 소싱 여행입니다. <strong>30,000명 이상의 바이어</strong> (30개국 이상), 2,000개 이상의 전시업체, 모든 주요 중국 자전거 브랜드 — Giant, Merida, Trinx, XDS, Forever 및 1,000개 이상의 부품 공급업체. 창업자 Wang Jie (汪杰) 및 엔지니어링 팀과의 직접 미팅.',
        'product_label': '한국 자전거 AI 기능',
        'product_items': [
            '🔧 <strong>공방 AI</strong> — Shimano STEPS, Yamaha PW, Bosch eBike Systems, Panasonic, Bafang, Brose',
            '🛒 <strong>소매 AI 어시스턴트</strong> — 삼천리자전거, 알톤스포츠, BIKE24, 셔플, Giant Korea, Trek Korea',
            '📦 <strong>DTC E-커머스 AI</strong> — Shopify, WooCommerce, 네이버 스마트스토어, 쿠팡 자동 상품 설명',
            '🇰🇷 <strong>한국어 UI</strong> — 부가세, 사업자등록번호, 세금계산서 발행',
            '🌍 <strong>8개 언어 UI</strong> — KO / EN / DE / FR / ES / IT / NL / 中文',
        ],
        'booth_label': '9평 부스에서 만나보실 수 있는 것',
        'booth_items': [
            '라이브 데모: STA-100 PAA로 Shimano STEPS 지식 베이스를 10분 만에 구축',
            'AI bike-fit 추천 엔진 (Canyon / Rose / Cube 사이징)',
            '한국 자전거 소매 ROI 계산기 (중규모 매장 연간 52K EUR 절감)',
            '한국 유통 프로그램 (10–49대: 359 USD · 50–99: 319 USD · 100+: 279 USD)',
            '2년 보증 + 24/7 한국어 지원',
        ],
        'cta_label': 'STRATRONIX 부스에서 1:1 데모 예약',
        'cta_text': '창업자 Wang Jie (汪杰) 및 엔지니어링 팀과 직접 연락. 24시간 이내에 회신.',
        'cta_email1_label': '한국 영업', 'cta_email1': 'sales@stratronix.ai',
        'cta_email2_label': '자전거 OEM', 'cta_email2': 'cycling@stratronix.ai',
        'company_text': 'STRATRONIX (鼎图太易)는 2026년에 선전에서 설립된 AI 하드웨어 회사입니다. 엄격한 데이터 프라이버시 및 컴플라이언스 요구사항이 있는 산업을 위한 클라우드 기반 AI 서비스의 글로벌 대안인 STA-100 PAA Private AI-Agent Appliance를 개발합니다. 핵심 오픈소스 제품: OpenClaw (BSD-3-Clause, GitHub 8K+ 스타).',
    },
    'au': {
        'lang': 'en-AU', 'locale': 'en_AU', 'country_code': 'au',
        'country_name': 'Australia', 'flag': '🇦🇺',
        'city_focus': 'Australia & New Zealand',
        'page_slug': 'cbm-2026-09-australia',
        'title': 'STRATRONIX @ CBM 2026 · China Outdoor & Cycling AI-Agent Expo · 9 September 2026 · ANZ Partners Invited',
        'desc': 'STRATRONIX invites Australia & New Zealand cycling retailers, distributors, and e-bike brands to CBM 2026 (China Outdoor & Cycling Industry AI Agent Expo) on 9 September 2026. STA-100 PAA — local AI for ANZ cycling retail, repair, and DTC trade.',
        'kw': 'CBM 2026, ANZ cycling, Australia cycling, NZ cycling, STA-100, PAA, STRATRONIX, Privacy Act 1988, cycling retail AI',
        'hero_h1': 'STRATRONIX @ CBM 2026 — China Outdoor & Cycling AI-Agent Expo · ANZ Edition',
        'hero_sub': '9 September 2026 · 09:00–17:00 (Wed) · 9 m² Standard Booth · ANZ Partners Welcome',
        'apac_note': 'CBM 2026 is a <strong>China-focused industry trade show</strong> with 30,000+ buyers from cycling, outdoor, fitness, and e-commerce channels across China, ANZ, and APAC.',
        'intro': 'STRATRONIX welcomes our <strong>Australia & New Zealand</strong> cycling retail, repair, e-bike, and D2C partners. The STA-100 PAA delivers an ANZ-localised AI Work Assistant built for 99 Bikes, Reid Cycles, JetBlack Products, Bicycling Australia, Avanti, and DTC brands (BikesOnline, Pushys, Chain Reaction Cycles).',
        'compliance_label': 'Privacy Act 1988 & AUPrivacy Principles compliant',
        'compliance_text': 'STA-100 PAA meets the requirements of <strong>Privacy Act 1988</strong> and the 13 Australian Privacy Principles (APPs). All inference local, no data exfiltration, full audit trail. Compatible with Shimano STEPS, Yamaha PW, Bosch eBike Systems, Bafang.',
        'why_now_label': 'Why ANZ cycling retailers should source from China',
        'why_now_text': 'CBM 2026 is the most efficient 2027 sourcing trip for ANZ cycling buyers. <strong>30,000+ buyers</strong> from 30+ countries, 2,000+ exhibitors, all major Chinese cycling brands — Giant, Merida, Trinx, XDS, Forever and 1,000+ component suppliers. Direct contact with our founder Wang Jie (汪杰) and engineering team.',
        'product_label': 'ANZ cycling AI features',
        'product_items': [
            '🔧 <strong>Workshop AI</strong> — Shimano, SRAM, Campagnolo, Hope, Brooks, Chris King, ANZ IBD brands',
            '🛒 <strong>Retail AI Assistant</strong> — 99 Bikes, Reid Cycles, JetBlack, Avanti, Mal Star, Modus, Faction',
            '📦 <strong>DTC E-commerce AI</strong> — Shopify, BigCommerce, Australia Post, NZ Post integration',
            '🇦🇺 <strong>ANZ English UI</strong> — AUD/NZD pricing, GST, and ANZ consumer law compliance',
            '🌍 <strong>8-language UI</strong> — EN / DE / FR / ES / IT / NL / PL / 中文 (CN)',
        ],
        'booth_label': 'What you’ll see at our 9 m² booth',
        'booth_items': [
            'Live demo: STA-100 PAA running ANZ IBD knowledge base in 10 minutes',
            'AI bike-fit recommendation engine (Canyon / Rose / Cube sizing)',
            'ANZ cycling retail ROI calculator (saves AUD 90K/year for mid-size store)',
            'ANZ distributor partnership program (10–49 units: AUD 550 · 50–99: AUD 490 · 100+: AUD 430)',
            '2-year warranty + 24/7 ANZ English support',
        ],
        'cta_label': 'Book a 1-on-1 demo at STRATRONIX booth',
        'cta_text': 'Direct contact with founder Wang Jie (汪杰) and engineering team. Reply within 24 hours.',
        'cta_email1_label': 'ANZ Sales', 'cta_email1': 'sales@stratronix.ai',
        'cta_email2_label': 'Cycling OEM', 'cta_email2': 'cycling@stratronix.ai',
        'company_text': 'STRATRONIX (鼎图太易) is a 2026-founded AI hardware company in Shenzhen. We develop the STA-100 PAA Private AI-Agent Appliance — the global alternative to cloud-based AI services for industries with strict data privacy and compliance requirements. Core open-source product: OpenClaw (BSD-3-Clause, GitHub 8K+ stars).',
    },
    'ca': {
        'lang': 'en-CA', 'locale': 'en_CA', 'country_code': 'ca',
        'country_name': 'Canada', 'flag': '🇨🇦',
        'city_focus': 'Canada & North America',
        'page_slug': 'cbm-2026-09-canada',
        'title': 'STRATRONIX @ CBM 2026 · China Outdoor & Cycling AI-Agent Expo · 9 September 2026 · Canadian Partners Invited',
        'desc': 'STRATRONIX invites Canadian cycling retailers, distributors, and e-bike brands to CBM 2026 (China Outdoor & Cycling Industry AI Agent Expo) on 9 September 2026. STA-100 PAA — local AI for Canadian cycling retail, repair, and DTC trade.',
        'kw': 'CBM 2026, Canada cycling, Canadian cycling, STA-100, PAA, STRATRONIX, PIPEDA, Quebec Law 25, cycling retail AI',
        'hero_h1': 'STRATRONIX @ CBM 2026 — China Outdoor & Cycling AI-Agent Expo · Canada Edition',
        'hero_sub': '9 September 2026 · 09:00–17:00 (Wed) · 9 m² Standard Booth · Canadian Partners Welcome',
        'apac_note': 'CBM 2026 is a <strong>China-focused industry trade show</strong> with 30,000+ buyers from cycling, outdoor, fitness, and e-commerce channels across China, North America, and APAC.',
        'intro': 'STRATRONIX welcomes our <strong>Canadian</strong> cycling retail, repair, e-bike, and D2C partners. The STA-100 PAA delivers a Canada-localised AI Work Assistant built for Canadian Tire, Sport Chek, MEC, Bike Vancouver, and DTC brands (Rapha, Knog, Mission Cycles, Argon 18).',
        'compliance_label': 'PIPEDA & Quebec Law 25 compliant',
        'compliance_text': 'STA-100 PAA meets the requirements of <strong>PIPEDA</strong> (Personal Information Protection and Electronic Documents Act) and <strong>Quebec Law 25</strong> (modernizing privacy rules). All inference local, no data exfiltration, full audit trail. Compatible with Shimano STEPS, Yamaha PW, Bosch eBike Systems, Bafang.',
        'why_now_label': 'Why Canadian cycling retailers should source from China',
        'why_now_text': 'CBM 2026 is the most efficient 2027 sourcing trip for Canadian cycling buyers. <strong>30,000+ buyers</strong> from 30+ countries, 2,000+ exhibitors, all major Chinese cycling brands — Giant, Merida, Trinx, XDS, Forever and 1,000+ component suppliers. Direct contact with our founder Wang Jie (汪杰) and engineering team.',
        'product_label': 'Canadian cycling AI features',
        'product_items': [
            '🔧 <strong>Workshop AI</strong> — Shimano, SRAM, Campagnolo, Hope, Brooks, Chris King, North American IBD brands',
            '🛒 <strong>Retail AI Assistant</strong> — Canadian Tire, Sport Chek, MEC, Bike Vancouver, Argon 18, Louis Garneau',
            '📦 <strong>DTC E-commerce AI</strong> — Shopify, BigCommerce, Canada Post, Purolator integration',
            '🇨🇦 <strong>Canadian English/French UI</strong> — CAD/USD pricing, GST/HST/QST, Canadian consumer law',
            '🌍 <strong>8-language UI</strong> — EN/FR / DE / ES / IT / NL / PL / 中文 (CN)',
        ],
        'booth_label': 'What you’ll see at our 9 m² booth',
        'booth_items': [
            'Live demo: STA-100 PAA running Canadian IBD knowledge base in 10 minutes',
            'AI bike-fit recommendation engine (Canyon / Rose / Cube sizing)',
            'Canadian cycling retail ROI calculator (saves CAD 78K/year for mid-size store)',
            'Canadian distributor partnership program (10–49 units: CAD 490 · 50–99: CAD 430 · 100+: CAD 380)',
            '2-year warranty + 24/7 Canadian English/French support',
        ],
        'cta_label': 'Book a 1-on-1 demo at STRATRONIX booth',
        'cta_text': 'Direct contact with founder Wang Jie (汪杰) and engineering team. Reply within 24 hours.',
        'cta_email1_label': 'Canada Sales', 'cta_email1': 'sales@stratronix.ai',
        'cta_email2_label': 'Cycling OEM', 'cta_email2': 'cycling@stratronix.ai',
        'company_text': 'STRATRONIX (鼎图太易) is a 2026-founded AI hardware company in Shenzhen. We develop the STA-100 PAA Private AI-Agent Appliance — the global alternative to cloud-based AI services for industries with strict data privacy and compliance requirements. Core open-source product: OpenClaw (BSD-3-Clause, GitHub 8K+ stars).',
    },
    'mx': {
        'lang': 'es-MX', 'locale': 'es_MX', 'country_code': 'mx',
        'country_name': 'México', 'flag': '🇲🇽',
        'city_focus': 'México y mercado latinoamericano',
        'page_slug': 'cbm-2026-09-mexico',
        'title': 'STRATRONIX @ CBM 2026 · Exposición IA Ciclismo & Outdoor China · 9 septiembre 2026',
        'desc': 'STRATRONIX presenta STA-100 PAA Private AI-Agent Appliance en CBM 2026 (Exposición IA Ciclismo & Outdoor de China) el 9 de septiembre de 2026. Stand 9 m². Asistente IA para industria ciclista. Precio mundial 399 USD.',
        'kw': 'CBM 2026, exposición ciclismo China, IA ciclismo, STA-100, PAA, STRATRONIX, LFPDPPP, e-bike, retail ciclista',
        'hero_h1': 'STRATRONIX @ CBM 2026 — Exposición IA Ciclismo & Outdoor China',
        'hero_sub': '9 septiembre 2026 · 09:00–17:00 (mié) · Pabellón TBD · Stand 9 m²',
        'apac_note': 'CBM 2026 es una <strong>feria profesional china</strong> con más de 30 000 compradores de los sectores de ciclismo, outdoor, fitness y e-commerce en China, Latinoamérica y APAC.',
        'intro': 'STRATRONIX da la bienvenida a nuestros socios <strong>latinoamericanos</strong> de México, Colombia, Argentina, Chile, Perú, Brasil. El STA-100 PAA es un asistente IA local para el comercio minorista ciclista, talleres, marcas de e-bike y DTC compatible con Shimano, SRAM, Bafang, Bosch, Yamaha, Giant, Trek, Specialized, BH, Orbea, Scott.',
        'compliance_label': 'Cumple LFPDPPP y estándares globales',
        'compliance_text': 'STA-100 PAA cumple los requisitos de la <strong>LFPDPPP</strong> (Ley Federal de Protección de Datos Personales en Posesión de los Particulares) y estándares globales como RGPD. Inferencia LLM local, sin exfiltración de datos, pistas de auditoría completas. Compatible con Bosch eBike Systems, Shimano STEPS, Bafang, Yamaha PW.',
        'why_now_label': 'Por qué los minoristas ciclistas latinos deberían visitar China',
        'why_now_text': 'CBM 2026 es el viaje de aprovisionamiento 2027 más eficiente para compradores ciclistas latinos. <strong>30 000+ compradores</strong> de 30+ países, 2 000+ expositores, todas las grandes marcas chinas — Giant, Merida, Trinx, XDS, Eternal y 1 000+ proveedores de componentes. Contacto directo con nuestro fundador Wang Jie (汪杰) y el equipo de ingeniería.',
        'product_label': 'Funciones IA ciclismo en español latino',
        'product_items': [
            '🔧 <strong>IA de taller</strong> — Bosch eBike Systems, Shimano STEPS, Bafang, Yamaha, Brose, SRAM, Shimano',
            '🛒 <strong>Asistente IA retail</strong> — Specialized, Trek, Giant, BH, Orbea, Scott, Cervélo, Conor, Mérida',
            '📦 <strong>IA e-commerce DTC</strong> — Shopify, WooCommerce, Mercado Libre, Amazon LATAM, Clip, Mercado Pago',
            '🇲🇽 <strong>Interfaz español latino</strong> — IVA, RFC, facturación electrónica CFDI 4.0',
            '🌍 <strong>Interfaz 8 idiomas</strong> — ES / EN / DE / FR / IT / NL / PL / 中文 (CN)',
        ],
        'booth_label': 'Qué le espera en nuestro stand de 9 m²',
        'booth_items': [
            'Demo en vivo: STA-100 PAA con base de conocimientos Bosch eBike en 10 minutos',
            'Motor de recomendación IA bike-fit (Canyon / Rose / Cube tallaje)',
            'Calculadora ROI retail ciclista (ahorra 52K EUR/año para tienda mediana)',
            'Programa de distribución LATAM (10–49 unidades: 359 USD · 50–99: 319 USD · 100+: 279 USD)',
            'Garantía 2 años + soporte 24/7 en español latino',
        ],
        'cta_label': 'Reserve una demo 1-a-1 en el stand de STRATRONIX',
        'cta_text': 'Contacto directo con el fundador Wang Jie (汪杰) y el equipo de ingeniería. Respuesta en 24 horas.',
        'cta_email1_label': 'Ventas LATAM', 'cta_email1': 'sales@stratronix.ai',
        'cta_email2_label': 'OEM Ciclismo', 'cta_email2': 'cycling@stratronix.ai',
        'company_text': 'STRATRONIX (鼎图太易) es una empresa de hardware AI fundada en Shenzhen en 2026. Desarrollamos el STA-100 PAA Private AI-Agent Appliance — la alternativa mundial a los servicios AI cloud para industrias con requisitos estrictos de privacidad y cumplimiento. Producto open-source principal: OpenClaw (BSD-3-Clause, GitHub 8K+ estrellas).',
    },
    'in': {
        'lang': 'hi-IN', 'locale': 'hi_IN', 'country_code': 'in',
        'country_name': 'भारत', 'flag': '🇮🇳',
        'city_focus': 'भारत और दक्षिण एशिया',
        'page_slug': 'cbm-2026-09-india',
        'title': 'STRATRONIX @ CBM 2026 · चीन आउटडोर और साइकिलिंग AI एजेंट एक्सपो · 9 सितंबर 2026',
        'desc': 'STRATRONIX 9 सितंबर 2026 को CBM 2026 (चीन आउटडोर और साइकिलिंग उद्योग AI एजेंट एक्सपो) में STA-100 PAA Private AI-Agent Appliance का अनावरण करेगा। 9 वर्ग मीटर मानक बूथ। साइकिलिंग उद्योग AI कार्य सहायक। वैश्विक सूची मूल्य 399 USD।',
        'kw': 'CBM 2026, चीन साइकिलिंग एक्सपो, साइकिलिंग AI, STA-100, PAA, STRATRONIX, DPDP, e-bike, साइकिलिंग रिटेल',
        'hero_h1': 'STRATRONIX @ CBM 2026 — चीन आउटडोर और साइकिलिंग AI एजेंट एक्सपो',
        'hero_sub': '9 सितंबर 2026 · 09:00–17:00 (बुध) · 9 वर्ग मीटर मानक बूथ',
        'apac_note': 'CBM 2026 एक <strong>चीन-केंद्रित उद्योग व्यापार शो</strong> है जिसमें चीन, भारत, दक्षिण पूर्व एशिया से 30,000+ खरीदार शामिल हैं।',
        'intro': 'STRATRONIX अपने <strong>भारतीय</strong> साइकिलिंग, आउटडोर, और e-bike भागीदारों का स्वागत करता है। STA-100 PAA एक स्थानीय AI कार्य सहायक है जो BSA, Firefox, Hero Cycles, Atlas Cycles, Avon Cycles, और Ti Cycles जैसे भारतीय साइकिलिंग ब्रांडों के लिए बनाया गया है।',
        'compliance_label': 'DPDP और वैश्विक मानकों के अनुरूप',
        'compliance_text': 'STA-100 PAA <strong>DPDP Act 2023</strong> (Digital Personal Data Protection Act) और अंतरराष्ट्रीय मानकों की आवश्यकताओं को पूरा करता है। सभी अनुमान स्थानीय, कोई डेटा रिसाव नहीं, पूर्ण ऑडिट ट्रेल। Shimano STEPS, Yamaha PW, Bosch eBike Systems, Bafang के साथ संगत।',
        'why_now_label': 'भारतीय साइकिलिंग खुदरा विक्रेताओं को चीन क्यों जाना चाहिए',
        'why_now_text': 'CBM 2026 भारतीय साइकिलिंग खरीदारों के लिए 2027 का सबसे कुशल सोर्सिंग ट्रिप है। <strong>30,000+ खरीदार</strong> 30+ देशों से, 2,000+ प्रदर्शक, सभी प्रमुख चीनी साइकिलिंग ब्रांड — Giant, Merida, Trinx, XDS, Forever और 1,000+ घटक आपूर्तिकर्ता। संस्थापक Wang Jie (汪杰) और इंजीनियरिंग टीम के साथ सीधा संपर्क।',
        'product_label': 'भारतीय साइकिलिंग AI सुविधाएँ',
        'product_items': [
            '🔧 <strong>वर्कशॉप AI</strong> — BSA, Firefox, Hero Cycles, Atlas Cycles, Avon Cycles, Ti Cycles, Trinx',
            '🛒 <strong>रिटेल AI सहायक</strong> — BSA, Firefox, Hero Cycles, Avon, Atlas, कस्टम डीलर नेटवर्क',
            '📦 <strong>DTC ई-कॉमर्स AI</strong> — Shopify, WooCommerce, Flipkart, Amazon India, Razorpay, UPI',
            '🇮🇳 <strong>हिंदी UI</strong> — GST, PAN, भारतीय बिलिंग और इनवॉइसिंग',
            '🌍 <strong>8-भाषा UI</strong> — HI / EN / DE / FR / ES / IT / NL / 中文 (CN)',
        ],
        'booth_label': 'हमारे 9 वर्ग मीटर बूथ पर आप क्या देखेंगे',
        'booth_items': [
            'लाइव डेमो: STA-100 PAA 10 मिनट में BSA/विश्वकर्मा ज्ञानकोष चला रहा है',
            'AI bike-fit अनुशंसा इंजन (ग्राहक आकार, आराम, सड़क बनाम ग्रेवल)',
            'भारतीय साइकिलिंग रिटेल ROI कैलकुलेटर (मध्यम आकार की दुकान के लिए 52K EUR/वर्ष बचत)',
            'भारतीय वितरक भागीदारी कार्यक्रम (10–49 यूनिट: 359 USD · 50–99: 319 USD · 100+: 279 USD)',
            '2 साल वारंटी + 24/7 हिंदी / अंग्रेजी सहायता',
        ],
        'cta_label': 'STRATRONIX बूथ पर 1-ऑन-1 डेमो बुक करें',
        'cta_text': 'संस्थापक Wang Jie (汪杰) और इंजीनियरिंग टीम से सीधा संपर्क। 24 घंटे के भीतर उत्तर।',
        'cta_email1_label': 'भारत बिक्री', 'cta_email1': 'sales@stratronix.ai',
        'cta_email2_label': 'साइकिलिंग OEM', 'cta_email2': 'cycling@stratronix.ai',
        'company_text': 'STRATRONIX (鼎图太易) 2026 में शेन्ज़ेन में स्थापित एक AI हार्डवेयर कंपनी है। हम STA-100 PAA Private AI-Agent Appliance विकसित करते हैं — सख्त डेटा गोपनीयता और अनुपालन आवश्यकताओं वाले उद्योगों के लिए क्लाउड-आधारित AI सेवाओं का वैश्विक विकल्प। मुख्य ओपन-सोर्स उत्पाद: OpenClaw (BSD-3-Clause, GitHub 8K+ स्टार)।',
    },
    'th': {
        'lang': 'th-TH', 'locale': 'th_TH', 'country_code': 'th',
        'country_name': 'ประเทศไทย', 'flag': '🇹🇭',
        'city_focus': 'ประเทศไทยและอาเซียน',
        'page_slug': 'cbm-2026-09-thailand',
        'title': 'STRATRONIX @ CBM 2026 · งานจัดแสดง AI จักรยานและกลางแจ้งของจีน · 9 กันยายน 2026',
        'desc': 'STRATRONIX จะเปิดตัว STA-100 PAA Private AI-Agent Appliance ที่งาน CBM 2026 (งานจัดแสดง AI จักรยานและกลางแจ้งของจีน) ในวันที่ 9 กันยายน 2026 บูธมาตรฐาน 9 ตร.ม. ผู้ช่วย AI สำหรับอุตสาหกรรมจักรยาน ราคาสากล 399 USD',
        'kw': 'CBM 2026, งานจักรยานจีน, จักรยาน AI, STA-100, PAA, STRATRONIX, PDPA, e-bike, ร้านจักรยาน',
        'hero_h1': 'STRATRONIX @ CBM 2026 — งานจัดแสดง AI จักรยานและกลางแจ้งของจีน',
        'hero_sub': '9 กันยายน 2026 · 09:00–17:00 (พ) · บูธมาตรฐาน 9 ตร.ม.',
        'apac_note': 'CBM 2026 เป็น<strong>งานแสดงสินค้าอุตสาหกรรมของจีน</strong>ที่มีผู้ซื้อมากกว่า 30,000 รายจากอุตสาหกรรมจักรยาน กลางแจ้ง ฟิตเนส และอีคอมเมิร์ซ',
        'intro': 'STRATRONIX ขอต้อนรับพันธมิตร<strong>ชาวไทยและอาเซียน</strong>ด้านจักรยานและ e-bike ของเรา STA-100 PAA เป็นผู้ช่วย AI ทำงานในพื้นที่สำหรับร้านค้าปลีกจักรยาน อู่ซ่อม แบรนด์ e-bike และ DTC ที่สร้างขึ้นสำหรับ Bangkok Cycle, Pai & Co, Rudy Project, และ Bangkok-area bike shops',
        'compliance_label': 'สอดคล้องกับ PDPA และมาตรฐานสากล',
        'compliance_text': 'STA-100 PAA ตรงตามข้อกำหนดของ<strong>PDPA</strong> (พ.ร.บ. คุ้มครองข้อมูลส่วนบุคคล) และ PDPA ของไทย การอนุมานทั้งหมดเป็นแบบโลคัล ไม่มีการรั่วไหลของข้อมูล มี audit trail ครบถ้วน เข้ากันได้กับ Shimano STEPS, Yamaha PW, Bosch eBike Systems, Bafang',
        'why_now_label': 'เหตุผลที่ร้านค้าปลีกจักรยานไทยควรไปจีน',
        'why_now_text': 'CBM 2026 เป็นทริปจัดซื้อปี 2027 ที่มีประสิทธิภาพที่สุดสำหรับผู้ซื้อจักรยานไทย <strong>ผู้ซื้อ 30,000+ ราย</strong>จาก 30+ ประเทศ ผู้แสดงสินค้า 2,000+ ราย แบรนด์จักรยานจีนชั้นนำทั้งหมด — Giant, Merida, Trinx, XDS, Forever และซัพพลายเออร์ชิ้นส่วน 1,000+ ราย ติดต่อโดยตรงกับผู้ก่อตั้ง Wang Jie (汪杰) และทีมวิศวกรรม',
        'product_label': 'คุณสมบัติ AI จักรยานไทย',
        'product_items': [
            '🔧 <strong>AI อู่ซ่อม</strong> — Shimano STEPS, Yamaha PW, Bosch eBike Systems, Bafang, Brose',
            '🛒 <strong>ผู้ช่วย AI ค้าปลีก</strong> — Bangkok Cycle, Pai & Co, ร้านจักรยานท้องถิ่นในกรุงเทพฯ, เชียงใหม่, ภูเก็ต',
            '📦 <strong>AI DTC E-commerce</strong> — Shopify, Lazada, Shopee, LINE MyShop, คำอธิบายสินค้าอัตโนมัติภาษาไทย',
            '🇹🇭 <strong>UI ภาษาไทย</strong> — ระบบ VAT 7%, ใบกำกับภาษี, ระบบชำระเงิน PromptPay',
            '🌍 <strong>UI 8 ภาษา</strong> — TH / EN / DE / FR / ES / IT / NL / 中文 (CN)',
        ],
        'booth_label': 'สิ่งที่คุณจะเห็นที่บูธ 9 ตร.ม. ของเรา',
        'booth_items': [
            'เดโมสด: STA-100 PAA รันฐานความรู้ Bosch eBike ใน 10 นาที',
            'เครื่องมือแนะนำ AI bike-fit (ขนาด Canyon / Rose / Cube)',
            'เครื่องคำนวณ ROI ร้านค้าปลีกจักรยานไทย (ประหยัด 52K EUR/ปี)',
            'โปรแกรมผู้จัดจำหน่ายไทย (10–49 หน่วย: 359 USD · 50–99: 319 USD · 100+: 279 USD)',
            'รับประกัน 2 ปี + สนับสนุน 24/7 ภาษาไทย',
        ],
        'cta_label': 'จองเดโม 1-ต่อ-1 ที่บูธ STRATRONIX',
        'cta_text': 'ติดต่อโดยตรงกับผู้ก่อตั้ง Wang Jie (汪杰) และทีมวิศวกรรม ตอบกลับภายใน 24 ชั่วโมง',
        'cta_email1_label': 'ฝ่ายขายไทย', 'cta_email1': 'sales@stratronix.ai',
        'cta_email2_label': 'OEM จักรยาน', 'cta_email2': 'cycling@stratronix.ai',
        'company_text': 'STRATRONIX (鼎图太易) เป็นบริษัทฮาร์ดแวร์ AI ที่ก่อตั้งในปี 2026 ในเซินเจิ้น เราพัฒนา STA-100 PAA Private AI-Agent Appliance — ทางเลือกระดับโลกแทนบริการ AI บนคลาวด์สำหรับอุตสาหกรรมที่มีข้อกำหนดด้านความเป็นส่วนตัวของข้อมูลและการปฏิบัติตามข้อกำหนดที่เข้มงวด ผลิตภัณฑ์โอเพนซอร์สหลัก: OpenClaw (BSD-3-Clause, GitHub 8K+ ดาว)',
    },
    'za': {
        'lang': 'en-ZA', 'locale': 'en_ZA', 'country_code': 'za',
        'country_name': 'South Africa', 'flag': '🇿🇦',
        'city_focus': 'South Africa & Sub-Saharan Africa',
        'page_slug': 'cbm-2026-09-south-africa',
        'title': 'STRATRONIX @ CBM 2026 · China Outdoor & Cycling AI-Agent Expo · 9 September 2026 · SA Partners Invited',
        'desc': 'STRATRONIX invites South African cycling retailers, distributors, and e-bike brands to CBM 2026 (China Outdoor & Cycling Industry AI Agent Expo) on 9 September 2026. STA-100 PAA — local AI for SA cycling retail, repair, and DTC trade.',
        'kw': 'CBM 2026, South Africa cycling, SA cycling, STA-100, PAA, STRATRONIX, POPIA, e-bike, cycling retail AI',
        'hero_h1': 'STRATRONIX @ CBM 2026 — China Outdoor & Cycling AI-Agent Expo · South Africa Edition',
        'hero_sub': '9 September 2026 · 09:00–17:00 (Wed) · 9 m² Standard Booth · SA Partners Welcome',
        'apac_note': 'CBM 2026 is a <strong>China-focused industry trade show</strong> with 30,000+ buyers from cycling, outdoor, fitness, and e-commerce channels across China, Africa, and APAC.',
        'intro': 'STRATRONIX welcomes our <strong>South African and Sub-Saharan African</strong> cycling retail, repair, e-bike, and D2C partners. The STA-100 PAA delivers an SA-localised AI Work Assistant built for Game, Cycle Lab, Sportsmans Warehouse, and DTC brands (Leatt, Lezyne, Spinner).',
        'compliance_label': 'POPIA compliant',
        'compliance_text': 'STA-100 PAA meets the requirements of <strong>POPIA</strong> (Protection of Personal Information Act). All inference local, no data exfiltration, full audit trail. Compatible with Shimano STEPS, Yamaha PW, Bosch eBike Systems, Bafang.',
        'why_now_label': 'Why SA cycling retailers should source from China',
        'why_now_text': 'CBM 2026 is the most efficient 2027 sourcing trip for South African cycling buyers. <strong>30,000+ buyers</strong> from 30+ countries, 2,000+ exhibitors, all major Chinese cycling brands — Giant, Merida, Trinx, XDS, Forever and 1,000+ component suppliers. Direct contact with our founder Wang Jie (汪杰) and engineering team.',
        'product_label': 'SA cycling AI features',
        'product_items': [
            '🔧 <strong>Workshop AI</strong> — Shimano, SRAM, Campagnolo, Hope, Brooks, Chris King, SA IBD brands',
            '🛒 <strong>Retail AI Assistant</strong> — Game, Cycle Lab, Sportsmans Warehouse, Cape Cycle, The Bike Shop',
            '📦 <strong>DTC E-commerce AI</strong> — Shopify, WooCommerce, Takealot, Payfast integration',
            '🇿🇦 <strong>SA English UI</strong> — ZAR pricing, VAT 15%, SA consumer law',
            '🌍 <strong>8-language UI</strong> — EN / DE / FR / ES / IT / NL / PL / 中文 (CN)',
        ],
        'booth_label': 'What you’ll see at our 9 m² booth',
        'booth_items': [
            'Live demo: STA-100 PAA running SA IBD knowledge base in 10 minutes',
            'AI bike-fit recommendation engine (Canyon / Rose / Cube sizing)',
            'SA cycling retail ROI calculator (saves ZAR 1.1M/year for mid-size store)',
            'SA distributor partnership program (10–49 units: ZAR 6,500 · 50–99: ZAR 5,800 · 100+: ZAR 5,100)',
            '2-year warranty + 24/7 SA English support',
        ],
        'cta_label': 'Book a 1-on-1 demo at STRATRONIX booth',
        'cta_text': 'Direct contact with founder Wang Jie (汪杰) and engineering team. Reply within 24 hours.',
        'cta_email1_label': 'SA Sales', 'cta_email1': 'sales@stratronix.ai',
        'cta_email2_label': 'Cycling OEM', 'cta_email2': 'cycling@stratronix.ai',
        'company_text': 'STRATRONIX (鼎图太易) is a 2026-founded AI hardware company in Shenzhen. We develop the STA-100 PAA Private AI-Agent Appliance — the global alternative to cloud-based AI services for industries with strict data privacy and compliance requirements. Core open-source product: OpenClaw (BSD-3-Clause, GitHub 8K+ stars).',
    },
    'nz': {
        'lang': 'en-NZ', 'locale': 'en_NZ', 'country_code': 'nz',
        'country_name': 'New Zealand', 'flag': '🇳🇿',
        'city_focus': 'New Zealand & Pacific Islands',
        'page_slug': 'cbm-2026-09-new-zealand',
        'title': 'STRATRONIX @ CBM 2026 · China Outdoor & Cycling AI-Agent Expo · 9 September 2026 · NZ Partners Invited',
        'desc': 'STRATRONIX invites New Zealand cycling retailers, distributors, and e-bike brands to CBM 2026 (China Outdoor & Cycling Industry AI Agent Expo) on 9 September 2026. STA-100 PAA — local AI for NZ cycling retail, repair, and DTC trade.',
        'kw': 'CBM 2026, New Zealand cycling, NZ cycling, STA-100, PAA, STRATRONIX, NZ Privacy Act 2020, e-bike, cycling retail AI',
        'hero_h1': 'STRATRONIX @ CBM 2026 — China Outdoor & Cycling AI-Agent Expo · NZ Edition',
        'hero_sub': '9 September 2026 · 09:00–17:00 (Wed) · 9 m² Standard Booth · NZ Partners Welcome',
        'apac_note': 'CBM 2026 is a <strong>China-focused industry trade show</strong> with 30,000+ buyers from cycling, outdoor, fitness, and e-commerce channels across China, NZ, and APAC.',
        'intro': 'STRATRONIX welcomes our <strong>New Zealand</strong> cycling retail, repair, e-bike, and D2C partners. The STA-100 PAA delivers an NZ-localised AI Work Assistant built for Evo Cycles, Cycle Trading Post, Torpedo7, and DTC brands (Bikesonline NZ, Paddy, NZ Cycle Trail).',
        'compliance_label': 'NZ Privacy Act 2020 compliant',
        'compliance_text': 'STA-100 PAA meets the requirements of <strong>NZ Privacy Act 2020</strong>. All inference local, no data exfiltration, full audit trail. Compatible with Shimano STEPS, Yamaha PW, Bosch eBike Systems, Bafang.',
        'why_now_label': 'Why NZ cycling retailers should source from China',
        'why_now_text': 'CBM 2026 is the most efficient 2027 sourcing trip for NZ cycling buyers. <strong>30,000+ buyers</strong> from 30+ countries, 2,000+ exhibitors, all major Chinese cycling brands — Giant, Merida, Trinx, XDS, Forever and 1,000+ component suppliers. Direct contact with our founder Wang Jie (汪杰) and engineering team.',
        'product_label': 'NZ cycling AI features',
        'product_items': [
            '🔧 <strong>Workshop AI</strong> — Shimano, SRAM, Campagnolo, Hope, Brooks, Chris King, NZ IBD brands',
            '🛒 <strong>Retail AI Assistant</strong> — Evo Cycles, Cycle Trading Post, Torpedo7, NZ Bike, Avanti',
            '📦 <strong>DTC E-commerce AI</strong> — Shopify, WooCommerce, NZ Post, NZ Couriers integration',
            '🇳🇿 <strong>NZ English UI</strong> — NZD pricing, GST 15%, NZ consumer law',
            '🌍 <strong>8-language UI</strong> — EN / DE / FR / ES / IT / NL / PL / 中文 (CN)',
        ],
        'booth_label': 'What you’ll see at our 9 m² booth',
        'booth_items': [
            'Live demo: STA-100 PAA running NZ IBD knowledge base in 10 minutes',
            'AI bike-fit recommendation engine (Canyon / Rose / Cube sizing)',
            'NZ cycling retail ROI calculator (saves NZD 95K/year for mid-size store)',
            'NZ distributor partnership program (10–49 units: NZD 580 · 50–99: NZD 520 · 100+: NZD 460)',
            '2-year warranty + 24/7 NZ English support',
        ],
        'cta_label': 'Book a 1-on-1 demo at STRATRONIX booth',
        'cta_text': 'Direct contact with founder Wang Jie (汪杰) and engineering team. Reply within 24 hours.',
        'cta_email1_label': 'NZ Sales', 'cta_email1': 'sales@stratronix.ai',
        'cta_email2_label': 'Cycling OEM', 'cta_email2': 'cycling@stratronix.ai',
        'company_text': 'STRATRONIX (鼎图太易) is a 2026-founded AI hardware company in Shenzhen. We develop the STA-100 PAA Private AI-Agent Appliance — the global alternative to cloud-based AI services for industries with strict data privacy and compliance requirements. Core open-source product: OpenClaw (BSD-3-Clause, GitHub 8K+ stars).',
    },
    'ie': {
        'lang': 'en-IE', 'locale': 'en_IE', 'country_code': 'ie',
        'country_name': 'Ireland', 'flag': '🇮🇪',
        'city_focus': 'Ireland & European English-speaking markets',
        'page_slug': 'cbm-2026-09-ireland',
        'title': 'STRATRONIX @ CBM 2026 · China Outdoor & Cycling AI-Agent Expo · 9 September 2026 · Irish Partners Invited',
        'desc': 'STRATRONIX invites Irish cycling retailers, distributors, and e-bike brands to CBM 2026 (China Outdoor & Cycling Industry AI Agent Expo) on 9 September 2026. STA-100 PAA — local AI for IE cycling retail, repair, and DTC trade.',
        'kw': 'CBM 2026, Ireland cycling, Irish cycling, STA-100, PAA, STRATRONIX, GDPR, HSE, e-bike, cycling retail AI',
        'hero_h1': 'STRATRONIX @ CBM 2026 — China Outdoor & Cycling AI-Agent Expo · Ireland Edition',
        'hero_sub': '9 September 2026 · 09:00–17:00 (Wed) · 9 m² Standard Booth · Irish Partners Welcome',
        'apac_note': 'CBM 2026 is a <strong>China-focused industry trade show</strong> with 30,000+ buyers from cycling, outdoor, fitness, and e-commerce channels across China, Ireland, EU, and APAC.',
        'intro': 'STRATRONIX welcomes our <strong>Irish</strong> cycling retail, repair, e-bike, and D2C partners. The STA-100 PAA delivers an IE-localised AI Work Assistant built for Halfords Ireland, Bikeworld, The Bike Shop, Cycle SuperStore, and DTC brands (Ribble, Watt, Bikes.ie).',
        'compliance_label': 'GDPR & HSE compliant',
        'compliance_text': 'STA-100 PAA meets the requirements of <strong>GDPR</strong> (EU/EEA). All inference local, no data exfiltration, full audit trail. Compatible with Shimano STEPS, Yamaha PW, Bosch eBike Systems, Bafang.',
        'why_now_label': 'Why Irish cycling retailers should source from China',
        'why_now_text': 'CBM 2026 is the most efficient 2027 sourcing trip for Irish cycling buyers. <strong>30,000+ buyers</strong> from 30+ countries, 2,000+ exhibitors, all major Chinese cycling brands — Giant, Merida, Trinx, XDS, Forever and 1,000+ component suppliers. Direct contact with our founder Wang Jie (汪杰) and engineering team.',
        'product_label': 'IE cycling AI features',
        'product_items': [
            '🔧 <strong>Workshop AI</strong> — Shimano, SRAM, Campagnolo, Hope, Brooks, Chris King, IE IBD brands',
            '🛒 <strong>Retail AI Assistant</strong> — Halfords Ireland, Bikeworld, The Bike Shop, Cycle SuperStore',
            '📦 <strong>DTC E-commerce AI</strong> — Shopify, WooCommerce, An Post, DPD Ireland integration',
            '🇮🇪 <strong>IE English UI</strong> — EUR pricing, VAT 23%, Irish consumer law',
            '🌍 <strong>8-language UI</strong> — EN / DE / FR / ES / IT / NL / PL / 中文 (CN)',
        ],
        'booth_label': 'What you’ll see at our 9 m² booth',
        'booth_items': [
            'Live demo: STA-100 PAA running IE IBD knowledge base in 10 minutes',
            'AI bike-fit recommendation engine (Canyon / Rose / Cube sizing)',
            'IE cycling retail ROI calculator (saves EUR 52K/year for mid-size store)',
            'IE distributor partnership program (10–49 units: EUR 290 · 50–99: EUR 260 · 100+: EUR 230)',
            '2-year warranty + 24/7 IE English support',
        ],
        'cta_label': 'Book a 1-on-1 demo at STRATRONIX booth',
        'cta_text': 'Direct contact with founder Wang Jie (汪杰) and engineering team. Reply within 24 hours.',
        'cta_email1_label': 'IE Sales', 'cta_email1': 'sales@stratronix.ai',
        'cta_email2_label': 'Cycling OEM', 'cta_email2': 'cycling@stratronix.ai',
        'company_text': 'STRATRONIX (鼎图太易) is a 2026-founded AI hardware company in Shenzhen. We develop the STA-100 PAA Private AI-Agent Appliance — the global alternative to cloud-based AI services for industries with strict data privacy and compliance requirements. Core open-source product: OpenClaw (BSD-3-Clause, GitHub 8K+ stars).',
    },
}

print(f"Total countries: {len(COUNTRIES)}")
print(f"Countries: {', '.join(COUNTRIES.keys())}")

# ============== HTML Generation ==============

HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="{lang}">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="keywords" content="{kw}">
<meta name="robots" content="index, follow, max-snippet:-1">
<meta name="author" content="STRATRONIX 鼎图太易信息技术（深圳）有限公司">
<link rel="canonical" href="{canonical}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{canonical}">
<meta property="og:image" content="{OG_IMAGE}">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:type" content="event">
<meta property="og:locale" content="{locale}">
<meta property="event:start_time" content="2026-09-09T09:00:00+08:00">
<meta property="event:end_time" content="2026-09-09T17:00:00+08:00">
<meta property="event:location" content="STRATRONIX 9 平米标准展位（展位号详见官方邀请函）">
<script type="application/ld+json">
{jsonld}
</script>
<style>
* {{ box-sizing: border-box; margin: 0; padding: 0; }}
body {{ font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Microsoft YaHei', sans-serif; line-height: 1.85; color: #1a1a1a; background: #fafafa; padding: 20px; }}
header {{ background: linear-gradient(135deg, #E6417F 0%, #c9296c 100%); color: white; padding: 50px 24px; text-align: center; border-radius: 12px; }}
header h1 {{ font-size: 2.2rem; max-width: 1000px; margin: 0 auto 16px; line-height: 1.4; }}
header p {{ opacity: 0.95; font-size: 1.1rem; max-width: 1000px; margin: 0 auto; }}
.booth {{ display: inline-block; background: white; color: #E6417F; padding: 12px 28px; border-radius: 30px; font-weight: 700; font-size: 1.3rem; margin-top: 20px; }}
.main {{ max-width: 1000px; margin: 30px auto; background: white; padding: 35px; border-radius: 12px; }}
h2 {{ font-size: 1.6rem; color: #E6417F; margin: 30px 0 14px; border-left: 5px solid #E6417F; padding-left: 12px; }}
.kw {{ font-weight: 700; }}
.callout {{ background: #fff5f9; border-left: 5px solid #E6417F; padding: 22px; margin: 24px 0; border-radius: 0 8px 8px 0; }}
.eu {{ background: linear-gradient(135deg, #fff5f9 0%, #e8f4ff 100%); border-left: 5px solid #1e6fd9; padding: 22px; border-radius: 8px; margin: 24px 0; }}
.cta {{ background: linear-gradient(135deg, #E6417F 0%, #c9296c 100%); color: white; padding: 36px; text-align: center; border-radius: 12px; margin: 36px 0; }}
.cta a {{ background: white; color: #E6417F; padding: 12px 32px; border-radius: 8px; text-decoration: none; font-weight: 600; display: inline-block; margin: 6px; }}
.cta a:hover {{ transform: translateY(-2px); box-shadow: 0 4px 12px rgba(0,0,0,0.15); }}
.event-meta {{ display: flex; flex-wrap: wrap; gap: 16px; margin: 26px 0; padding: 18px; background: #1a1a1a; color: white; border-radius: 12px; }}
.event-meta div {{ flex: 1; min-width: 180px; }}
.event-meta strong {{ color: #E6417F; display: block; margin-bottom: 4px; font-size: 0.85rem; }}
ul {{ margin: 12px 0 16px 24px; }}
li {{ margin-bottom: 6px; }}
.lang-switch {{ text-align: center; margin: 20px 0; padding: 16px; background: white; border-radius: 8px; }}
.lang-switch a {{ display: inline-block; margin: 4px; padding: 6px 14px; border-radius: 16px; background: #fafafa; color: #E6417F; text-decoration: none; font-size: 0.9em; border: 1px solid #E6417F; }}
.lang-switch a:hover {{ background: #E6417F; color: white; }}
.lang-switch a.current {{ background: #E6417F; color: white; }}
footer {{ text-align: center; color: #666; font-size: 0.85em; margin-top: 32px; padding-top: 16px; border-top: 1px solid #eee; }}
@media (max-width: 640px) {{ header h1 {{ font-size: 1.6rem; }} .main {{ padding: 20px; }} }}
</style>
</head>
<body>

<div style="background: linear-gradient(135deg, #fff5f9 0%, #ffe6f0 100%); border-left: 5px solid #E6417F; margin: 16px 0; padding: 18px 24px; border-radius: 8px;">
  <strong style="color: #E6417F; font-size: 1.1rem;">📩 {cta_label}</strong>
  <p style="margin: 6px 0 0 0; color: #333; font-size: 0.95rem;">
    {cta_text}
    <a href="{BASE}/events/cbm-2026-09/invitation.html" style="display:inline-block;background:#E6417F;color:white;padding:8px 18px;border-radius:6px;text-decoration:none;font-weight:600;margin-left:8px;">🎯 Full Invitation Portal</a>
  </p>
</div>

<header>
<h1>{hero_h1}</h1>
<p>{hero_sub}</p>
<div class="booth">📍 9 m² Standard Booth</div>
</header>

<div class="main">

<div class="lang-switch">
  <a href="{BASE}/events/cbm-2026-09/zh.html">🇨🇳 中文</a>
  <a href="{BASE}/events/cbm-2026-09/en.html">🇺🇸 English</a>
  <a href="{BASE}/events/{country_code}/{page_slug}.html" class="current">{flag} {country_name}</a>
</div>

<div class="eu">
<strong style="color:#1e6fd9;font-size:1.15rem;">🌍 Focus: {city_focus}</strong>
<p style="margin:10px 0 0 0;font-size:1.02rem;">{apac_note}</p>
<p style="margin:8px 0 0 0;font-size:1.0rem;">{intro}</p>
</div>

<div class="event-meta">
<div><strong>📅 Date</strong>September 9, 2026 (Wed)</div>
<div><strong>⏰ Hours</strong>09:00 - 17:00</div>
<div><strong>📍 Venue</strong>9 m² Standard Booth (Hall TBD per official invitation)</div>
<div><strong>🌐 Theme</strong>AI Work Assistant for Cycling Industry</div>
</div>

<div class="callout">
<strong>World Premiere</strong>: STRATRONIX unveils the <strong class="kw">STA-100 PAA Private AI-Agent Appliance</strong> at CBM 2026 (China Outdoor & Cycling Industry AI-Agent Expo).<br>
<strong>8-10 minute</strong> setup · <strong>On-device LLM inference</strong> · <strong>Complete data sovereignty</strong> · <strong>Global list price USD 399</strong>
</div>

<h2>1. {product_label}</h2>
<ul>
{product_items_html}
</ul>

<h2>2. {compliance_label}</h2>
<div class="eu">
<p>{compliance_text}</p>
</div>

<h2>3. {why_now_label}</h2>
<p>{why_now_text}</p>

<h2>4. {booth_label}</h2>
<ul>
{booth_items_html}
</ul>

<div class="cta">
<h2 style="color:white;border:none;padding:0;margin:0 0 12px;">📩 {cta_label}</h2>
<p style="margin:0 0 16px;font-size:1.05em;">{cta_text}</p>
<a href="mailto:{cta_email1}?subject=CBM 2026 Booth Visit ({country_name})">📧 {cta_email1_label}: {cta_email1}</a>
<a href="mailto:{cta_email2}?subject=CBM 2026 Cycling OEM">📧 {cta_email2_label}: {cta_email2}</a>
</div>

<div class="eu">
<h2 style="font-size:1.4rem;">About STRATRONIX</h2>
<p>{company_text}</p>
<p style="font-size:0.9rem;margin-top:12px;color:#666;">📍 深圳市宝安区航城街道洲石路 739 号恒丰工业 C6 栋 1203D · 统一社会信用代码: 91440300MAKD20DT6F</p>
</div>

<footer>
<p>© 2026 STRATRONIX 鼎图太易信息技术（深圳）有限公司 · Stratronix Technology (Shenzhen) Company, Limited · All rights reserved.</p>
<p>Global list price USD 399 · Volume distributor pricing available · 2-year warranty · 24/7 multilingual support</p>
</footer>

</div>
</body>
</html>"""

def make_jsonld(c, country_name):
    return json.dumps({
        "@context": "https://schema.org",
        "@type": "Event",
        "name": "STRATRONIX @ CBM 2026 — China Outdoor & Cycling Industry AI-Agent Expo",
        "description": c['desc'],
        "startDate": "2026-09-09T09:00:00+08:00",
        "endDate": "2026-09-09T17:00:00+08:00",
        "eventAttendanceMode": "https://schema.org/OfflineEventAttendanceMode",
        "eventStatus": "https://schema.org/EventScheduled",
        "location": {
            "@type": "Place",
            "name": f"STRATRONIX 9 m² Standard Booth at CBM 2026 ({country_name} partners welcome)",
            "address": {
                "@type": "PostalAddress",
                "addressCountry": "CN"
            }
        },
        "organizer": {
            "@type": "Organization",
            "name": "STRATRONIX",
            "alternateName": "Stratronix Technology (Shenzhen) Company, Limited",
            "url": "https://www.stratronix.ai",
            "email": "sales@stratronix.ai"
        },
        "offers": {
            "@type": "Offer",
            "price": "399",
            "priceCurrency": "USD",
            "availability": "https://schema.org/InStock",
            "url": f"{BASE}/buy/"
        }
    }, indent=2, ensure_ascii=False)


for cc, c in COUNTRIES.items():
    out_dir = f'{ROOT}/events/cbm-2026-09/{cc}'
    os.makedirs(out_dir, exist_ok=True)

    product_items_html = '\n'.join(f'<li>{item}</li>' for item in c['product_items'])
    booth_items_html = '\n'.join(f'<li>{item}</li>' for item in c['booth_items'])

    canonical = f"{BASE}/events/cbm-2026-09/{cc}/{c['page_slug']}.html"
    jsonld = make_jsonld(c, c['country_name'])

    html = HTML_TEMPLATE.format(
        lang=c['lang'],
        locale=c['locale'],
        country_code=c['country_code'],
        country_name=c['country_name'],
        flag=c['flag'],
        page_slug=c['page_slug'],
        title=c['title'],
        desc=c['desc'],
        kw=c['kw'],
        canonical=canonical,
        OG_IMAGE=OG_IMAGE,
        jsonld=jsonld,
        cta_label=c['cta_label'],
        cta_text=c['cta_text'],
        cta_email1=c['cta_email1'],
        cta_email1_label=c['cta_email1_label'],
        cta_email2=c['cta_email2'],
        cta_email2_label=c['cta_email2_label'],
        hero_h1=c['hero_h1'],
        hero_sub=c['hero_sub'],
        city_focus=c['city_focus'],
        apac_note=c['apac_note'],
        intro=c['intro'],
        product_label=c['product_label'],
        product_items_html=product_items_html,
        booth_label=c['booth_label'],
        booth_items_html=booth_items_html,
        compliance_label=c['compliance_label'],
        compliance_text=c['compliance_text'],
        why_now_label=c['why_now_label'],
        why_now_text=c['why_now_text'],
        company_text=c['company_text'],
        BASE=BASE,
    )

    html_path = f'{out_dir}/{c["page_slug"]}.html'
    gz_path = f'{html_path}.gz'

    with open(html_path, 'w', encoding='utf-8') as f:
        f.write(html)
    with open(gz_path, 'wb') as f:
        f.write(gzip.compress(html.encode('utf-8'), compresslevel=9))

    print(f'✓ {cc} → {c["page_slug"]}.html ({len(html)} bytes, {os.path.getsize(gz_path)} gz)')

print(f'\nGenerated {len(COUNTRIES)} country pages for CBM 2026-09')

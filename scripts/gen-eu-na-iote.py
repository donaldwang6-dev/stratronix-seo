#!/usr/bin/env python3
"""
生成 IOTE 2026 邀请函页面 — 欧洲 + 北美 9 国 native 语言
- 欧洲 6 国：de / fr / es / it / nl / pl
- 北美 3 国：us / ca / mx（us + ca 用 en, mx 用 es-MX）
- 100% native 语言（铁律 15.1）
- Schema.org Event JSON-LD
- Open Graph 完整
"""
import os, gzip, shutil

ROOT = '/home/donald/.openclaw/workspace/stratronix-seo'
BASE = 'https://donaldwang6-dev.github.io/stratronix-seo'
OG_IMAGE = f'{BASE}/og-images/og-image-iot-2026.png'

# 每个国家的完整 native 语言文案（人工翻译）
COUNTRIES = {
    'de': {
        'lang': 'de-DE',
        'locale': 'de_DE',
        'country_code': 'de',
        'country_name': 'Deutschland',
        'city_focus': 'DACH-Region (Deutschland / Österreich / Schweiz)',
        'page_slug': 'iote-2026-deutschland',
        'title': 'STRATRONIX IOTE 2026 Shenzhen IoT-Messe Einladung · 26.-28. August 2026',
        'desc': 'STRATRONIX stellt auf der IOTE 2026 (25. Internationale IoT-Messe, Shenzhen, 26.-28. August 2026) den STA-100 PAA Private AI-Agent Appliance vor. Stand 12B62-1. Eingeladen sind DACH-Partner, Distributoren und Systemintegratoren.',
        'kw': 'IOTE 2026, Shenzhen IoT, STA-100, PAA, STRATRONIX, Private AI, DSGVO, EU AI Act, Stand 12B62-1, August 2026',
        'hero_h1': 'STRATRONIX lädt zur IOTE 2026 Shenzhen IoT-Messe ein',
        'hero_sub': '25. Internationale IoT-Messe · AGIC AI-Messe · ISVE Smart Business Expo<br>26.-28. August 2026 · Shenzhen World Exhibition & Convention Center, Hallen 9-12',
        'booth': 'Stand 12B62-1',
        'apac_note': 'Bitte beachten Sie: IOTE 2026 ist eine <strong>Asien-Pazifik fokussierte Messe</strong> mit Besuchern aus über 30 Ländern, insbesondere China, Japan, Korea, Indien und Südostasien.',
        'eu_intro': 'STRATRONIX heißt unsere <strong>DACH-Partner</strong> aus Deutschland, Österreich und der Schweiz am Stand 12B62-1 willkommen. Entdecken Sie den STA-100 PAA und diskutieren Sie Vertriebs-, OEM- und Integrationsmöglichkeiten.',
        'compliance_label': 'DSGVO- & EU-AI-Act-konform',
        'compliance_text': 'STA-100 PAA erfüllt die strengen Anforderungen der <strong>DSGVO</strong> (Art. 9 besondere Kategorien personenbezogener Daten) sowie die Pflichten des <strong>EU AI Act</strong> für Hochrisiko-Systeme. Datenhoheit garantiert: Keine Cloud-Abhängigkeit, alle Inferenz auf dem Gerät, menschliche Aufsicht (Human-in-the-Loop) durchsetzbar.',
        'why_now_label': 'Warum jetzt nach Shenzhen reisen?',
        'why_now_text': 'China ist 2026 der größte IoT-Markt der Welt. Die IOTE 2026 bringt <strong>50.000+ Fachbesucher</strong> aus 30+ Ländern zusammen — die einzige Messe, auf der Sie das gesamte APAC-Ökosystem an einem Ort treffen. Direkter Kontakt mit unserem Gründer Wang Jie (汪杰) und dem STRATRONIX-Engineering-Team.',
        'product_label': 'Produkt-Highlights',
        'product_items': [
            '🔒 <strong>Privat & Sicher</strong>: Alle Daten bleiben auf dem Gerät — keine Cloud-Übertragung',
            '⚡ <strong>8-10 Minuten Setup</strong>: Vom Einschalten bis zur produktiven Nutzung in unter 10 Minuten',
            '🧠 <strong>OpenClaw integriert</strong>: Open-Source AI-Agent-Framework (BSD-3-Clause, GitHub 8K+ Stars)',
            '💼 <strong>8 Branchen-Workflows</strong>: Gesundheit · Finanzen · Recht · Fertigung · Bildung · Behörden · SaaS · Cross-Border-E-Commerce',
            '🌍 <strong>Globaler Listenpreis 399 USD</strong> (Mengenrabatt verfügbar)',
        ],
        'eu_specific_label': 'Vorteile für den DACH-Markt',
        'eu_specific_text': 'Der STA-100 PAA erfüllt die Anforderungen der <strong>DSGVO</strong>, des <strong>EU AI Act</strong> und der <strong>BaFin AI-Guidance</strong>. Lokale LLM-Inferenz (Qwen3, Llama 3.3, Mistral), keine Datenexfiltration, vollständige Audit-Trails. Mehrsprachige UI (DE / EN / FR / IT / ES / NL / PL) standardmäßig enthalten.',
        'booth_label': 'Was Sie am Stand 12B62-1 erwartet',
        'booth_items': [
            'Live-Demo: STA-100 PAA in 10 Minuten produktiv',
            'Privater LLM + RAG auf Deutsch (Live-Test Ihrer eigenen Dokumente)',
            '7 Branchen-ROI-Rechner (Healthcare 52K EUR · Finance 68K · Legal 74K · Manufacturing 61K EUR)',
            'DSGVO- & EU-AI-Act-Compliance-Checkliste',
            'Vertriebs- & OEM-Partnerprogramm (10-49 Stück: 359 USD · 50-99: 319 USD · 100+: 279 USD)',
            '2 Jahre Garantie + 24/7-Support auf Deutsch',
        ],
        'cta_label': 'Vereinbaren Sie jetzt Ihren Standbesuch',
        'cta_text': 'Direkter Draht zum Gründer Wang Jie (汪杰) und dem Engineering-Team. Antwort innerhalb von 24 Stunden.',
        'cta_email1_label': 'Europa-Vertrieb',
        'cta_email1': 'sales@stratronix.ai',
        'cta_email2_label': 'APAC-Partner',
        'cta_email2': 'apac@stratronix.ai',
        'company_label': 'Über STRATRONIX',
        'company_text': 'STRATRONIX (鼎图太易) ist ein 2026 in Shenzhen gegründetes AI-Hardware-Unternehmen. Wir entwickeln den STA-100 PAA Private AI-Agent Appliance — die globale Alternative zu cloud-basierten AI-Diensten für Branchen mit hohen Datenschutz- und Compliance-Anforderungen. Hauptprodukt: OpenClaw, unser Open-Source AI-Agent-Framework (BSD-3-Clause, GitHub 8K+ Stars).',
        'company_addr': 'Anschrift:深圳市宝安区航城街道洲石路 739 号恒丰工业 C6 栋 1203D · Handelsregister: 91440300MAKD20DT6F',
    },
    'fr': {
        'lang': 'fr-FR',
        'locale': 'fr_FR',
        'country_code': 'fr',
        'country_name': 'France',
        'city_focus': 'France / Belgique / Suisse / Luxembourg',
        'page_slug': 'iote-2026-france',
        'title': 'STRATRONIX IOTE 2026 Salon IoT Shenzhen Invitation · 26-28 août 2026',
        'desc': "STRATRONIX présente le STA-100 PAA Private AI-Agent Appliance à l'IOTE 2026 (25e Salon International IoT, Shenzhen, 26-28 août 2026). Stand 12B62-1. Distributeurs et intégrateurs francophones invités.",
        'kw': 'IOTE 2026, Salon IoT Shenzhen, STA-100, PAA, STRATRONIX, AI privé, RGPD, EU AI Act, Stand 12B62-1, août 2026',
        'hero_h1': "STRATRONIX vous invite à l'IOTE 2026 Shenzhen",
        'hero_sub': "25e Salon International IoT · Salon AGIC AI · Salon ISVE Smart Business<br>26-28 août 2026 · Centre mondial des expositions de Shenzhen, halls 9-12",
        'booth': 'Stand 12B62-1',
        'apac_note': "À noter : l'IOTE 2026 est un salon <strong>focalisé sur l'Asie-Pacifique</strong> avec des visiteurs de plus de 30 pays, notamment la Chine, le Japon, la Corée, l'Inde et l'Asie du Sud-Est.",
        'eu_intro': "STRATRONIX accueille chaleureusement nos partenaires <strong>francophones</strong> de France, Belgique, Suisse et Luxembourg au stand 12B62-1. Découvrez le STA-100 PAA et discutez des opportunités de distribution, OEM et d'intégration.",
        'compliance_label': 'Conforme RGPD & EU AI Act',
        'compliance_text': "STA-100 PAA satisfait aux exigences strictes du <strong>RGPD</strong> (art. 9 catégories particulières de données) et aux obligations de l'<strong>EU AI Act</strong> pour les systèmes à haut risque. Souveraineté des données garantie : aucune dépendance au cloud, toute l'inférence sur l'appareil, supervision humaine (Human-in-the-Loop) applicable.",
        'why_now_label': "Pourquoi se rendre à Shenzhen maintenant ?",
        'why_now_text': "La Chine est en 2026 le plus grand marché IoT au monde. L'IOTE 2026 réunit <strong>50 000+ visiteurs professionnels</strong> de 30+ pays — le seul salon où vous rencontrez tout l'écosystème APAC en un seul endroit. Contact direct avec notre fondateur Wang Jie (汪杰) et l'équipe d'ingénierie STRATRONIX.",
        'product_label': 'Points forts du produit',
        'product_items': [
            "🔒 <strong>Privé & Sécurisé</strong> : toutes les données restent sur l'appareil — aucune transmission cloud",
            "� <strong>Installation en 8-10 minutes</strong> : de la mise sous tension à l'utilisation productive en moins de 10 minutes",
            "🧠 <strong>OpenClaw intégré</strong> : framework open-source d'agents AI (BSD-3-Clause, GitHub 8K+ étoiles)",
            "💼 <strong>8 workflows sectoriels</strong> : santé · finance · juridique · industrie · éducation · secteur public · SaaS · e-commerce transfrontalier",
            "🌍 <strong>Prix catalogue mondial 399 USD</strong> (remises volume disponibles)",
        ],
        'eu_specific_label': 'Avantages pour le marché francophone',
        'eu_specific_text': "Le STA-100 PAA satisfait aux exigences du <strong>RGPD</strong>, de l'<strong>EU AI Act</strong> et des orientations <strong>AMF / ACPR</strong> sur l'IA. Inférence LLM locale (Qwen3, Llama 3.3, Mistral), aucune exfiltration de données, pistes d'audit complètes. Interface multilingue (FR / EN / DE / IT / ES / NL / PL) incluse en standard.",
        'booth_label': 'Ce qui vous attend au stand 12B62-1',
        'booth_items': [
            "Démo live : STA-100 PAA productif en 10 minutes",
            "LLM privé + RAG en français (test live de vos propres documents)",
            "Calculateur ROI 7 secteurs (Santé 52K EUR · Finance 68K · Juridique 74K · Industrie 61K EUR)",
            "Checklist de conformité RGPD & EU AI Act",
            "Programme partenaires distribution & OEM (10-49 unités : 359 USD · 50-99 : 319 USD · 100+ : 279 USD)",
            "Garantie 2 ans + support 24/7 en français",
        ],
        'cta_label': "Réservez votre visite au stand dès maintenant",
        'cta_text': "Contact direct avec le fondateur Wang Jie (汪杰) et l'équipe d'ingénierie. Réponse sous 24 heures.",
        'cta_email1_label': 'Ventes Europe',
        'cta_email1': 'sales@stratronix.ai',
        'cta_email2_label': 'Partenaires APAC',
        'cta_email2': 'apac@stratronix.ai',
        'company_label': 'À propos de STRATRONIX',
        'company_text': "STRATRONIX (鼎图太易) est une entreprise de matériel IA fondée en 2026 à Shenzhen. Nous développons le STA-100 PAA Private AI-Agent Appliance — l'alternative mondiale aux services AI cloud pour les industries ayant des exigences élevées en matière de protection des données et de conformité. Produit phare : OpenClaw, notre framework open-source d'agents AI (BSD-3-Clause, GitHub 8K+ étoiles).",
        'company_addr': "Adresse : 深圳市宝安区航城街道洲石路 739 号恒丰工业 C6 栋 1203D · Registre du commerce : 91440300MAKD20DT6F",
    },
    'es': {
        'lang': 'es-ES',
        'locale': 'es_ES',
        'country_code': 'es',
        'country_name': 'España',
        'city_focus': 'España / Latinoamérica',
        'page_slug': 'iote-2026-espana',
        'title': 'STRATRONIX IOTE 2026 Feria IoT Shenzhen Invitación · 26-28 agosto 2026',
        'desc': 'STRATRONIX presenta el STA-100 PAA Private AI-Agent Appliance en IOTE 2026 (25ª Feria Internacional IoT, Shenzhen, 26-28 agosto 2026). Stand 12B62-1. Distribuidores e integradores hispanohablantes invitados.',
        'kw': 'IOTE 2026, Feria IoT Shenzhen, STA-100, PAA, STRATRONIX, AI privado, RGPD, EU AI Act, Stand 12B62-1, agosto 2026',
        'hero_h1': 'STRATRONIX le invita a IOTE 2026 Shenzhen',
        'hero_sub': '25ª Feria Internacional IoT · Feria AGIC AI · Feria ISVE Smart Business<br>26-28 agosto 2026 · Centro Mundial de Exposiciones de Shenzhen, pabellones 9-12',
        'booth': 'Stand 12B62-1',
        'apac_note': 'Nota: IOTE 2026 es una feria <strong>enfocada en Asia-Pacífico</strong> con visitantes de más de 30 países, especialmente China, Japón, Corea, India y el sudeste asiático.',
        'eu_intro': 'STRATRONIX da una cálida bienvenida a nuestros <strong>socios hispanohablantes</strong> de España, Latinoamérica y mercados de habla hispana en el stand 12B62-1. Descubra el STA-100 PAA y discuta oportunidades de distribución, OEM e integración.',
        'compliance_label': 'Cumple RGPD y EU AI Act',
        'compliance_text': 'STA-100 PAA cumple los estrictos requisitos del <strong>RGPD</strong> (art. 9 categorías especiales de datos personales) y las obligaciones de la <strong>EU AI Act</strong> para sistemas de alto riesgo. Soberanía de datos garantizada: sin dependencia de la nube, toda la inferencia en el dispositivo, supervisión humana (Human-in-the-Loop) aplicable.',
        'why_now_label': '¿Por qué viajar a Shenzhen ahora?',
        'why_now_text': 'China es en 2026 el mayor mercado IoT del mundo. IOTE 2026 reúne <strong>50.000+ visitantes profesionales</strong> de más de 30 países — la única feria donde se encuentra todo el ecosistema APAC en un solo lugar. Contacto directo con nuestro fundador Wang Jie (汪杰) y el equipo de ingeniería de STRATRONIX.',
        'product_label': 'Características del producto',
        'product_items': [
            '🔒 <strong>Privado y seguro</strong>: todos los datos permanecen en el dispositivo — sin transmisión a la nube',
            '⚡ <strong>Configuración en 8-10 minutos</strong>: del encendido al uso productivo en menos de 10 minutos',
            '🧠 <strong>OpenClaw integrado</strong>: framework open-source de agentes AI (BSD-3-Clause, GitHub 8K+ estrellas)',
            '💼 <strong>8 flujos sectoriales</strong>: salud · finanzas · legal · fabricación · educación · sector público · SaaS · e-commerce transfronterizo',
            '🌍 <strong>Precio de lista global 399 USD</strong> (descuentos por volumen disponibles)',
        ],
        'eu_specific_label': 'Ventajas para el mercado hispanohablante',
        'eu_specific_text': 'El STA-100 PAA cumple los requisitos del <strong>RGPD</strong>, la <strong>EU AI Act</strong> y las directrices de la <strong>CNMV / Banco de España</strong> sobre IA. Inferencia LLM local (Qwen3, Llama 3.3, Mistral), sin exfiltración de datos, auditorías completas. Interfaz multilingüe (ES / EN / FR / IT / DE / NL / PL) incluida de serie.',
        'booth_label': 'Qué le espera en el stand 12B62-1',
        'booth_items': [
            'Demo en vivo: STA-100 PAA productivo en 10 minutos',
            'LLM privado + RAG en español (prueba en vivo de sus propios documentos)',
            'Calculadora ROI 7 sectores (Salud 52K EUR · Finanzas 68K · Legal 74K · Fabricación 61K EUR)',
            'Lista de verificación de cumplimiento RGPD y EU AI Act',
            'Programa de socios de distribución y OEM (10-49 unidades: 359 USD · 50-99: 319 USD · 100+: 279 USD)',
            '2 años de garantía + soporte 24/7 en español',
        ],
        'cta_label': 'Reserve su visita al stand ahora',
        'cta_text': 'Línea directa con el fundador Wang Jie (汪杰) y el equipo de ingeniería. Respuesta en 24 horas.',
        'cta_email1_label': 'Ventas Europa',
        'cta_email1': 'sales@stratronix.ai',
        'cta_email2_label': 'Socios APAC',
        'cta_email2': 'apac@stratronix.ai',
        'company_label': 'Acerca de STRATRONIX',
        'company_text': 'STRATRONIX (鼎图太易) es una empresa de hardware de IA fundada en 2026 en Shenzhen. Desarrollamos el STA-100 PAA Private AI-Agent Appliance — la alternativa global a los servicios AI en la nube para industrias con altos requisitos de protección de datos y cumplimiento normativo. Producto estrella: OpenClaw, nuestro framework open-source de agentes AI (BSD-3-Clause, GitHub 8K+ estrellas).',
        'company_addr': 'Dirección: 深圳市宝安区航城街道洲石路 739 号恒丰工业 C6 栋 1203D · Registro mercantil: 91440300MAKD20DT6F',
    },
    'it': {
        'lang': 'it-IT',
        'locale': 'it_IT',
        'country_code': 'it',
        'country_name': 'Italia',
        'city_focus': 'Italia / Europa meridionale',
        'page_slug': 'iote-2026-italia',
        'title': 'STRATRONIX IOTE 2026 Fiera IoT Shenzhen Invito · 26-28 agosto 2026',
        'desc': "STRATRONIX presenta lo STA-100 PAA Private AI-Agent Appliance all'IOTE 2026 (25ª Fiera Internazionale IoT, Shenzhen, 26-28 agosto 2026). Stand 12B62-1. Distributori e integratori italiani invitati.",
        'kw': 'IOTE 2026, Fiera IoT Shenzhen, STA-100, PAA, STRATRONIX, AI privato, GDPR, EU AI Act, Stand 12B62-1, agosto 2026',
        'hero_h1': "STRATRONIX ti invita all'IOTE 2026 Shenzhen",
        'hero_sub': '25ª Fiera Internazionale IoT · Fiera AGIC AI · Fiera ISVE Smart Business<br>26-28 agosto 2026 · Shenzhen World Exhibition & Convention Center, padiglioni 9-12',
        'booth': 'Stand 12B62-1',
        'apac_note': "Nota: l'IOTE 2026 è una fiera <strong>con focus Asia-Pacifico</strong> con visitatori da oltre 30 paesi, in particolare Cina, Giappone, Corea, India e Sud-Est asiatico.",
        'eu_intro': "STRATRONIX dà un caloroso benvenuto ai nostri <strong>partner italiani</strong> d'Italia e dell'Europa meridionale allo stand 12B62-1. Scopri lo STA-100 PAA e discutete opportunità di distribuzione, OEM e integrazione.",
        'compliance_label': 'Conforme GDPR e EU AI Act',
        'compliance_text': "STA-100 PAA soddisfa i requisiti rigorosi del <strong>GDPR</strong> (art. 9 categorie particolari di dati personali) e gli obblighi dell'<strong>EU AI Act</strong> per i sistemi ad alto rischio. Sovranità dei dati garantita: nessuna dipendenza dal cloud, tutta l'inferenza sul dispositivo, supervisione umana (Human-in-the-Loop) applicabile.",
        'why_now_label': 'Perché recarsi a Shenzhen adesso?',
        'why_now_text': "La Cina è nel 2026 il più grande mercato IoT al mondo. L'IOTE 2026 riunisce <strong>50.000+ visitatori professionali</strong> da oltre 30 paesi — l'unica fiera dove incontri tutto l'ecosistema APAC in un unico posto. Contatto diretto con il nostro fondatore Wang Jie (汪杰) e il team di ingegneria STRATRONIX.",
        'product_label': 'Caratteristiche del prodotto',
        'product_items': [
            "🔒 <strong>Privato e sicuro</strong>: tutti i dati rimangono sul dispositivo — nessuna trasmissione cloud",
            "⚡ <strong>Configurazione in 8-10 minuti</strong>: dall'accensione all'uso produttivo in meno di 10 minuti",
            "🧠 <strong>OpenClaw integrato</strong>: framework open-source di agenti AI (BSD-3-Clause, GitHub 8K+ stelle)",
            "💼 <strong>8 workflow settoriali</strong>: sanità · finanza · legale · manifattura · istruzione · pubblica amministrazione · SaaS · e-commerce transfrontaliero",
            "🌍 <strong>Prezzo di listino globale 399 USD</strong> (sconti volume disponibili)",
        ],
        'eu_specific_label': 'Vantaggi per il mercato italiano',
        'eu_specific_text': "Lo STA-100 PAA soddisfa i requisiti del <strong>GDPR</strong>, dell'<strong>EU AI Act</strong> e delle linee guida <strong>AGCM / Banca d'Italia</strong> sull'IA. Inferenza LLM locale (Qwen3, Llama 3.3, Mistral), nessuna esfiltrazione di dati, audit trail completi. Interfaccia multilingue (IT / EN / DE / FR / ES / NL / PL) inclusa di serie.",
        'booth_label': "Cosa vi aspetta allo stand 12B62-1",
        'booth_items': [
            "Demo live: STA-100 PAA produttivo in 10 minuti",
            "LLM privato + RAG in italiano (test live dei vostri documenti)",
            "Calcolatore ROI 7 settori (Sanità 52K EUR · Finanza 68K · Legale 74K · Manifattura 61K EUR)",
            "Checklist conformità GDPR e EU AI Act",
            "Programma partner distribuzione & OEM (10-49 unità: 359 USD · 50-99: 319 USD · 100+: 279 USD)",
            "2 anni di garanzia + supporto 24/7 in italiano",
        ],
        'cta_label': "Prenota subito la tua visita allo stand",
        'cta_text': "Linea diretta con il fondatore Wang Jie (汪杰) e il team di ingegneria. Risposta entro 24 ore.",
        'cta_email1_label': 'Vendite Europa',
        'cta_email1': 'sales@stratronix.ai',
        'cta_email2_label': 'Partner APAC',
        'cta_email2': 'apac@stratronix.ai',
        'company_label': 'Informazioni su STRATRONIX',
        'company_text': "STRATRONIX (鼎图太易) è un'azienda di hardware IA fondata nel 2026 a Shenzhen. Sviluppiamo lo STA-100 PAA Private AI-Agent Appliance — l'alternativa globale ai servizi AI cloud per industrie con elevati requisiti di protezione dei dati e conformità. Prodotto di punta: OpenClaw, il nostro framework open-source di agenti AI (BSD-3-Clause, GitHub 8K+ stelle).",
        'company_addr': 'Indirizzo: 深圳市宝安区航城街道洲石路 739 号恒丰工业 C6 栋 1203D · Registro imprese: 91440300MAKD20DT6F',
    },
    'nl': {
        'lang': 'nl-NL',
        'locale': 'nl_NL',
        'country_code': 'nl',
        'country_name': 'Nederland',
        'city_focus': 'Nederland / België',
        'page_slug': 'iote-2026-nederland',
        'title': 'STRATRONIX IOTE 2026 Shenzhen IoT-beurs Uitnodiging · 26-28 augustus 2026',
        'desc': 'STRATRONIX presenteert de STA-100 PAA Private AI-Agent Appliance op IOTE 2026 (25e Internationale IoT-beurs, Shenzhen, 26-28 augustus 2026). Stand 12B62-1. Distributeurs en integratoren uit de Benelux uitgenodigd.',
        'kw': 'IOTE 2026, Shenzhen IoT-beurs, STA-100, PAA, STRATRONIX, Privé AI, AVG, EU AI Act, Stand 12B62-1, augustus 2026',
        'hero_h1': 'STRATRONIX nodigt u uit voor IOTE 2026 Shenzhen',
        'hero_sub': '25e Internationale IoT-beurs · AGIC AI-beurs · ISVE Smart Business Expo<br>26-28 augustus 2026 · Shenzhen World Exhibition & Convention Center, hallen 9-12',
        'booth': 'Stand 12B62-1',
        'apac_note': 'Let op: IOTE 2026 is een <strong>Aziatisch-Pacific gerichte beurs</strong> met bezoekers uit meer dan 30 landen, met name China, Japan, Korea, India en Zuidoost-Azië.',
        'eu_intro': 'STRATRONIX verwelkomt van harte onze <strong>Benelux-partners</strong> uit Nederland, België en Luxemburg op stand 12B62-1. Ontdek de STA-100 PAA en bespreek distributie-, OEM- en integratiemogelijkheden.',
        'compliance_label': 'AVG- & EU AI Act-conform',
        'compliance_text': 'STA-100 PAA voldoet aan de strenge eisen van de <strong>AVG</strong> (art. 9 bijzondere categorieën van persoonsgegevens) en de verplichtingen van de <strong>EU AI Act</strong> voor hoog-risicosystemen. Datsoevereiniteit gegarandeerd: geen cloud-afhankelijkheid, alle inferentie op het apparaat, menselijke supervisie (Human-in-the-Loop) afdwingbaar.',
        'why_now_label': 'Waarom nu naar Shenzhen reizen?',
        'why_now_text': 'China is in 2026 de grootste IoT-markt ter wereld. IOTE 2026 brengt <strong>50.000+ professionele bezoekers</strong> uit 30+ landen samen — de enige beurs waar u het hele APAC-ecosysteem op één plek ontmoet. Direct contact met onze oprichter Wang Jie (汪杰) en het STRATRONIX engineeringteam.',
        'product_label': 'Producthoogtepunten',
        'product_items': [
            '🔒 <strong>Privé & veilig</strong>: alle data blijft op het apparaat — geen cloud-transmissie',
            '⚡ <strong>8-10 minuten setup</strong>: van opstarten tot productief gebruik in minder dan 10 minuten',
            '🧠 <strong>OpenClaw geïntegreerd</strong>: open-source AI-agent framework (BSD-3-Clause, GitHub 8K+ sterren)',
            '💼 <strong>8 sector-workflows</strong>: zorg · financiën · juridisch · productie · onderwijs · overheid · SaaS · grensoverschrijdende e-commerce',
            '🌍 <strong>Wereldwijde adviesprijs 399 USD</strong> (volumekorting beschikbaar)',
        ],
        'eu_specific_label': 'Voordelen voor de Benelux-markt',
        'eu_specific_text': 'STA-100 PAA voldoet aan de vereisten van de <strong>AVG</strong>, de <strong>EU AI Act</strong> en de <strong>DNB / AFM AI-richtlijnen</strong>. Lokale LLM-inferentie (Qwen3, Llama 3.3, Mistral), geen data-exfiltratie, volledige audit-trails. Meertalige UI (NL / EN / DE / FR / IT / ES / PL) standaard inbegrepen.',
        'booth_label': 'Wat u kunt verwachten op stand 12B62-1',
        'booth_items': [
            'Live demo: STA-100 PAA in 10 minuten productief',
            'Privé LLM + RAG in het Nederlands (live test van uw eigen documenten)',
            'ROI-calculator 7 sectoren (Zorg 52K EUR · Financiën 68K · Juridisch 74K · Productie 61K EUR)',
            'AVG- & EU AI Act-compliance checklist',
            'Distributie- & OEM-partnerprogramma (10-49 stuks: 359 USD · 50-99: 319 USD · 100+: 279 USD)',
            '2 jaar garantie + 24/7 ondersteuning in het Nederlands',
        ],
        'cta_label': 'Boek nu uw standbezoek',
        'cta_text': 'Directe lijn naar oprichter Wang Jie (汪杰) en het engineeringteam. Antwoord binnen 24 uur.',
        'cta_email1_label': 'Europa-verkoop',
        'cta_email1': 'sales@stratronix.ai',
        'cta_email2_label': 'APAC-partners',
        'cta_email2': 'apac@stratronix.ai',
        'company_label': 'Over STRATRONIX',
        'company_text': 'STRATRONIX (鼎图太易) is een in 2026 in Shenzhen opgericht AI-hardwarebedrijf. We ontwikkelen de STA-100 PAA Private AI-Agent Appliance — het wereldwijde alternatief voor cloud-AI-diensten voor industrieën met hoge eisen op het gebied van gegevensbescherming en compliance. Vlaggenschipproduct: OpenClaw, ons open-source AI-agent framework (BSD-3-Clause, GitHub 8K+ sterren).',
        'company_addr': 'Adres: 深圳市宝安区航城街道洲石路 739 号恒丰工业 C6 栋 1203D · Handelsregister: 91440300MAKD20DT6F',
    },
    'pl': {
        'lang': 'pl-PL',
        'locale': 'pl_PL',
        'country_code': 'pl',
        'country_name': 'Polska',
        'city_focus': 'Polska / Europa Środkowo-Wschodnia',
        'page_slug': 'iote-2026-polska',
        'title': 'STRATRONIX IOTE 2026 Targi IoT Shenzhen Zaproszenie · 26-28 sierpnia 2026',
        'desc': 'STRATRONIX prezentuje STA-100 PAA Private AI-Agent Appliance na IOTE 2026 (25. Międzynarodowe Targi IoT, Shenzhen, 26-28 sierpnia 2026). Stoisko 12B62-1. Dystrybutorzy i integratorzy z Polski zaproszeni.',
        'kw': 'IOTE 2026, Targi IoT Shenzhen, STA-100, PAA, STRATRONIX, Prywatne AI, RODO, EU AI Act, Stoisko 12B62-1, sierpień 2026',
        'hero_h1': 'STRATRONIX zaprasza na IOTE 2026 Shenzhen',
        'hero_sub': '25. Międzynarodowe Targi IoT · Targi AGIC AI · Targi ISVE Smart Business<br>26-28 sierpnia 2026 · Shenzhen World Exhibition & Convention Center, hale 9-12',
        'booth': 'Stoisko 12B62-1',
        'apac_note': 'Uwaga: IOTE 2026 to targi <strong>skoncentrowane na regionie Azji i Pacyfiku</strong> z odwiedzającymi z ponad 30 krajów, zwłaszcza z Chin, Japonii, Korei, Indii i Azji Południowo-Wschodniej.',
        'eu_intro': 'STRATRONIX serdecznie zaprasza naszych <strong>partnerów z Polski i Europy Środkowo-Wschodniej</strong> na stoisko 12B62-1. Odkryj STA-100 PAA i omów możliwości dystrybucji, OEM i integracji.',
        'compliance_label': 'Zgodne z RODO i EU AI Act',
        'compliance_text': 'STA-100 PAA spełnia surowe wymogi <strong>RODO</strong> (art. 9 szczególne kategorie danych osobowych) oraz obowiązki <strong>EU AI Act</strong> dla systemów wysokiego ryzyka. Suwerenność danych gwarantowana: brak zależności od chmury, całe wnioskowanie na urządzeniu, nadzór człowieka (Human-in-the-Loop) możliwy do wdrożenia.',
        'why_now_label': 'Dlaczego warto teraz pojechać do Shenzhen?',
        'why_now_text': 'Chiny są w 2026 największym rynkiem IoT na świecie. IOTE 2026 gromadzi <strong>50 000+ profesjonalnych odwiedzających</strong> z ponad 30 krajów — jedyne targi, na których spotkasz cały ekosystem APAC w jednym miejscu. Bezpośredni kontakt z naszym założycielem Wang Jie (汪杰) i zespołem inżynierów STRATRONIX.',
        'product_label': 'Najważniejsze cechy produktu',
        'product_items': [
            '🔒 <strong>Prywatny i bezpieczny</strong>: wszystkie dane pozostają na urządzeniu — brak transmisji do chmury',
            '⚡ <strong>Konfiguracja w 8-10 minut</strong>: od włączenia do użytku produkcyjnego w mniej niż 10 minut',
            '🧠 <strong>OpenClaw zintegrowany</strong>: open-source framework agentów AI (BSD-3-Clause, GitHub 8K+ gwiazdek)',
            '� <strong>8 przepływów branżowych</strong>: opieka zdrowotna · finanse · prawo · produkcja · edukacja · administracja publiczna · SaaS · e-commerce transgraniczny',
            '🌍 <strong>Globalna cena katalogowa 399 USD</strong> (rabaty ilościowe dostępne)',
        ],
        'eu_specific_label': 'Korzyści dla rynku polskiego',
        'eu_specific_text': 'STA-100 PAA spełnia wymogi <strong>RODO</strong>, <strong>EU AI Act</strong> oraz wytycznych <strong>KNF / UODO</strong> dotyczących AI. Lokalne wnioskowanie LLM (Qwen3, Llama 3.3, Mistral), brak eksfiltracji danych, pełne ścieżki audytu. Wielojęzyczny interfejs (PL / EN / DE / FR / IT / ES / NL) w zestawie.',
        'booth_label': 'Co czeka Cię na stoisku 12B62-1',
        'booth_items': [
            'Demo na żywo: STA-100 PAA produkcyjny w 10 minut',
            'Prywatny LLM + RAG po polsku (test na żywo Twoich własnych dokumentów)',
            'Kalkulator ROI dla 7 branż (Zdrowie 52K EUR · Finanse 68K · Prawo 74K · Produkcja 61K EUR)',
            'Lista kontrolna zgodności RODO i EU AI Act',
            'Program partnerski dystrybucji i OEM (10-49 szt.: 359 USD · 50-99: 319 USD · 100+: 279 USD)',
            '2 lata gwarancji + wsparcie 24/7 po polsku',
        ],
        'cta_label': 'Zarezerwuj wizytę na stoisku już teraz',
        'cta_text': 'Bezpośrednia linia do założyciela Wang Jie (汪杰) i zespołu inżynierów. Odpowiedź w ciągu 24 godzin.',
        'cta_email1_label': 'Sprzedaż Europa',
        'cta_email1': 'sales@stratronix.ai',
        'cta_email2_label': 'Partnerzy APAC',
        'cta_email2': 'apac@stratronix.ai',
        'company_label': 'O STRATRONIX',
        'company_text': 'STRATRONIX (鼎图太易) to firma sprzętowa AI założona w 2026 roku w Shenzhen. Opracowujemy STA-100 PAA Private AI-Agent Appliance — globalną alternatywę dla usług AI w chmurze dla branż o wysokich wymagach ochrony danych i zgodności z przepisami. Flagowy produkt: OpenClaw, nasz open-source framework agentów AI (BSD-3-Clause, GitHub 8K+ gwiazdek).',
        'company_addr': 'Adres: 深圳市宝安区航城街道洲石路 739 号恒丰工业 C6 栋 1203D · Rejestr handlowy: 91440300MAKD20DT6F',
    },
    'us': {
        'lang': 'en-US',
        'locale': 'en_US',
        'country_code': 'us',
        'country_name': 'United States',
        'city_focus': 'North America (USA / Canada / Mexico)',
        'page_slug': 'iote-2026-united-states',
        'title': 'STRATRONIX IOTE 2026 Shenzhen IoT Exhibition Invitation · Aug 26-28 2026',
        'desc': 'STRATRONIX premieres the STA-100 PAA Private AI-Agent Appliance at IOTE 2026 (25th International IoT Exhibition, Shenzhen, Aug 26-28 2026). Booth 12B62-1. US distributors, system integrators and enterprise customers invited.',
        'kw': 'IOTE 2026, Shenzhen IoT exhibition, STA-100, PAA, STRATRONIX, private AI, on-prem AI, GDPR, Booth 12B62-1, August 2026',
        'hero_h1': 'STRATRONIX Invites You to IOTE 2026 Shenzhen',
        'hero_sub': '25th International IoT Exhibition · AGIC AI Exhibition · ISVE Smart Business Expo<br>August 26-28, 2026 · Shenzhen World Exhibition & Convention Center, Halls 9-12',
        'booth': 'Booth 12B62-1',
        'apac_note': 'Note: IOTE 2026 is an <strong>Asia-Pacific focused exhibition</strong> with visitors from 30+ countries, primarily China, Japan, Korea, India, and Southeast Asia.',
        'eu_intro': 'STRATRONIX welcomes our <strong>North American partners</strong> from the USA, Canada, and Mexico to Booth 12B62-1. Discover the STA-100 PAA and explore distribution, OEM, and integration opportunities for the Americas market.',
        'compliance_label': 'GDPR + EU AI Act + HIPAA-ready',
        'compliance_text': 'STA-100 PAA is built to meet <strong>GDPR</strong> (Art. 9 special categories of personal data), <strong>EU AI Act</strong> high-risk system obligations, and is <strong>HIPAA-ready</strong> for US healthcare workflows. Complete data sovereignty: no cloud dependency, all inference on-device, human-in-the-loop supervision enforceable.',
        'why_now_label': 'Why travel to Shenzhen now?',
        'why_now_text': 'China is the largest IoT market in the world in 2026. IOTE 2026 brings together <strong>50,000+ professional visitors</strong> from 30+ countries — the only exhibition where you meet the entire APAC ecosystem in one place. Direct contact with our founder Wang Jie (汪杰) and the STRATRONIX engineering team.',
        'product_label': 'Product highlights',
        'product_items': [
            '🔒 <strong>Private & secure</strong>: all data stays on the device — zero cloud transmission',
            '⚡ <strong>8-10 minute setup</strong>: from power-on to productive use in under 10 minutes',
            '🧠 <strong>OpenClaw integrated</strong>: open-source AI-agent framework (BSD-3-Clause, GitHub 8K+ stars)',
            '💼 <strong>8 industry workflows</strong>: healthcare · finance · legal · manufacturing · education · public sector · SaaS · cross-border e-commerce',
            '🌍 <strong>Global list price USD 399</strong> (volume discounts available)',
        ],
        'eu_specific_label': 'Advantages for the North American market',
        'eu_specific_text': 'The STA-100 PAA meets <strong>GDPR</strong>, <strong>EU AI Act</strong>, and is <strong>HIPAA-ready</strong> for US healthcare. Local LLM inference (Qwen3, Llama 3.3, Mistral), no data exfiltration, complete audit trails. Multilingual UI (EN / ES / FR / DE / IT / NL / PL) included by default. NA pricing: 1 unit $399 · 10-49 units $359 · 50-99 units $319 · 100+ units $279.',
        'booth_label': 'What to expect at Booth 12B62-1',
        'booth_items': [
            'Live demo: STA-100 PAA productive in 10 minutes',
            'Private LLM + RAG in English (live test on your own documents)',
            '7-industry ROI calculator (Healthcare $52K · Finance $68K · Legal $74K · Manufacturing $61K)',
            'HIPAA + GDPR + EU AI Act compliance checklist',
            'Distribution & OEM partner program (10-49 units: $359 · 50-99: $319 · 100+: $279)',
            '2-year warranty + 24/7 English support',
        ],
        'cta_label': 'Book your booth visit now',
        'cta_text': 'Direct line to founder Wang Jie (汪杰) and the engineering team. Reply within 24 hours.',
        'cta_email1_label': 'North America Sales',
        'cta_email1': 'sales@stratronix.ai',
        'cta_email2_label': 'APAC Partners',
        'cta_email2': 'apac@stratronix.ai',
        'company_label': 'About STRATRONIX',
        'company_text': 'STRATRONIX (鼎图太易) is an AI hardware company founded in 2026 in Shenzhen. We develop the STA-100 PAA Private AI-Agent Appliance — the global alternative to cloud-based AI services for industries with high data-protection and compliance requirements. Flagship product: OpenClaw, our open-source AI-agent framework (BSD-3-Clause, GitHub 8K+ stars).',
        'company_addr': 'Address: 深圳市宝安区航城街道洲石路 739 号恒丰工业 C6 栋 1203D · Business Registration: 91440300MAKD20DT6F',
    },
    'ca': {
        'lang': 'en-CA',
        'locale': 'en_CA',
        'country_code': 'ca',
        'country_name': 'Canada',
        'city_focus': 'Canada / North America',
        'page_slug': 'iote-2026-canada',
        'title': 'STRATRONIX IOTE 2026 Shenzhen IoT Exhibition Invitation · Aug 26-28 2026',
        'desc': 'STRATRONIX launches the STA-100 PAA Private AI-Agent Appliance at IOTE 2026 (25th International IoT Exhibition, Shenzhen, Aug 26-28 2026). Booth 12B62-1. Canadian distributors, system integrators and enterprise customers invited.',
        'kw': 'IOTE 2026, Shenzhen IoT exhibition, STA-100, PAA, STRATRONIX, private AI, PIPEDA, GDPR, Booth 12B62-1, August 2026',
        'hero_h1': 'STRATRONIX Invites You to IOTE 2026 Shenzhen',
        'hero_sub': '25th International IoT Exhibition · AGIC AI Exhibition · ISVE Smart Business Expo<br>August 26-28, 2026 · Shenzhen World Exhibition & Convention Center, Halls 9-12',
        'booth': 'Booth 12B62-1',
        'apac_note': 'Note: IOTE 2026 is an <strong>Asia-Pacific focused exhibition</strong> with visitors from 30+ countries, primarily China, Japan, Korea, India, and Southeast Asia.',
        'eu_intro': 'STRATRONIX welcomes our <strong>Canadian partners</strong> from Canada to Booth 12B62-1. Discover the STA-100 PAA and explore distribution, OEM, and integration opportunities for the Canadian market.',
        'compliance_label': 'PIPEDA + GDPR + HIPAA-ready',
        'compliance_text': 'STA-100 PAA is built to meet <strong>PIPEDA</strong> (Personal Information Protection and Electronic Documents Act), <strong>GDPR</strong>, and is <strong>HIPAA-ready</strong> for cross-border healthcare workflows. Complete data sovereignty: no cloud dependency, all inference on-device, human-in-the-loop supervision enforceable.',
        'why_now_label': 'Why travel to Shenzhen now?',
        'why_now_text': 'China is the largest IoT market in the world in 2026. IOTE 2026 brings together <strong>50,000+ professional visitors</strong> from 30+ countries — the only exhibition where you meet the entire APAC ecosystem in one place. Direct contact with our founder Wang Jie (汪杰) and the STRATRONIX engineering team.',
        'product_label': 'Product highlights',
        'product_items': [
            '🔒 <strong>Private & secure</strong>: all data stays on the device — zero cloud transmission',
            '⚡ <strong>8-10 minute setup</strong>: from power-on to productive use in under 10 minutes',
            '🧠 <strong>OpenClaw integrated</strong>: open-source AI-agent framework (BSD-3-Clause, GitHub 8K+ stars)',
            '💼 <strong>8 industry workflows</strong>: healthcare · finance · legal · manufacturing · education · public sector · SaaS · cross-border e-commerce',
            '🌍 <strong>Global list price USD 399</strong> (CAD pricing available via distributors)',
        ],
        'eu_specific_label': 'Advantages for the Canadian market',
        'eu_specific_text': 'The STA-100 PAA meets <strong>PIPEDA</strong>, <strong>GDPR</strong>, and is <strong>HIPAA-ready</strong> for cross-border healthcare. Local LLM inference (Qwen3, Llama 3.3, Mistral), no data exfiltration, complete audit trails. Multilingual UI (EN / FR / ES) included by default. NA pricing: 1 unit $399 · 10-49 units $359 · 50-99 units $319 · 100+ units $279.',
        'booth_label': 'What to expect at Booth 12B62-1',
        'booth_items': [
            'Live demo: STA-100 PAA productive in 10 minutes',
            'Private LLM + RAG in English / French (live test on your own documents)',
            '7-industry ROI calculator (Healthcare $52K · Finance $68K · Legal $74K · Manufacturing $61K)',
            'PIPEDA + GDPR + HIPAA compliance checklist',
            'Distribution & OEM partner program (10-49 units: $359 · 50-99: $319 · 100+: $279)',
            '2-year warranty + 24/7 English/French support',
        ],
        'cta_label': 'Book your booth visit now',
        'cta_text': 'Direct line to founder Wang Jie (汪杰) and the engineering team. Reply within 24 hours.',
        'cta_email1_label': 'Canada Sales',
        'cta_email1': 'sales@stratronix.ai',
        'cta_email2_label': 'APAC Partners',
        'cta_email2': 'apac@stratronix.ai',
        'company_label': 'About STRATRONIX',
        'company_text': 'STRATRONIX (鼎图太易) is an AI hardware company founded in 2026 in Shenzhen. We develop the STA-100 PAA Private AI-Agent Appliance — the global alternative to cloud-based AI services for industries with high data-protection and compliance requirements. Flagship product: OpenClaw, our open-source AI-agent framework (BSD-3-Clause, GitHub 8K+ stars).',
        'company_addr': 'Address: 深圳市宝安区航城街道洲石路 739 号恒丰工业 C6 栋 1203D · Business Registration: 91440300MAKD20DT6F',
    },
    'mx': {
        'lang': 'es-MX',
        'locale': 'es_MX',
        'country_code': 'mx',
        'country_name': 'México',
        'city_focus': 'México / Latinoamérica',
        'page_slug': 'iote-2026-mexico',
        'title': 'STRATRONIX IOTE 2026 Feria IoT Shenzhen Invitación · 26-28 agosto 2026',
        'desc': 'STRATRONIX presenta el STA-100 PAA Private AI-Agent Appliance en IOTE 2026 (25ª Feria Internacional IoT, Shenzhen, 26-28 agosto 2026). Stand 12B62-1. Distribuidores e integradores de México y Latinoamérica invitados.',
        'kw': 'IOTE 2026, Feria IoT Shenzhen, STA-100, PAA, STRATRONIX, AI privado, LFPDPPP, RGPD, Stand 12B62-1, agosto 2026',
        'hero_h1': 'STRATRONIX le invita a IOTE 2026 Shenzhen',
        'hero_sub': '25ª Feria Internacional IoT · Feria AGIC AI · Feria ISVE Smart Business<br>26-28 agosto 2026 · Centro Mundial de Exposiciones de Shenzhen, pabellones 9-12',
        'booth': 'Stand 12B62-1',
        'apac_note': 'Nota: IOTE 2026 es una feria <strong>enfocada en Asia-Pacífico</strong> con visitantes de más de 30 países, especialmente China, Japón, Corea, India y el sudeste asiático.',
        'eu_intro': 'STRATRONIX da una cálida bienvenida a nuestros <strong>socios de México y Latinoamérica</strong> en el stand 12B62-1. Descubra el STA-100 PAA y discuta oportunidades de distribución, OEM e integración para el mercado latinoamericano.',
        'compliance_label': 'Cumple LFPDPPP + RGPD',
        'compliance_text': 'STA-100 PAA cumple con los requisitos de la <strong>LFPDPPP</strong> (Ley Federal de Protección de Datos Personales en Posesión de los Particulares), <strong>RGPD</strong> y el marco de la <strong>CNMV / Banco de México</strong> sobre IA. Soberanía de datos garantizada: sin dependencia de la nube, toda la inferencia en el dispositivo, supervisión humana (Human-in-the-Loop) aplicable.',
        'why_now_label': '¿Por qué viajar a Shenzhen ahora?',
        'why_now_text': 'China es en 2026 el mayor mercado IoT del mundo. IOTE 2026 reúne <strong>50.000+ visitantes profesionales</strong> de más de 30 países — la única feria donde se encuentra todo el ecosistema APAC en un solo lugar. Contacto directo con nuestro fundador Wang Jie (汪杰) y el equipo de ingeniería de STRATRONIX.',
        'product_label': 'Características del producto',
        'product_items': [
            '🔒 <strong>Privado y seguro</strong>: todos los datos permanecen en el dispositivo — sin transmisión a la nube',
            '⚡ <strong>Configuración en 8-10 minutos</strong>: del encendido al uso productivo en menos de 10 minutos',
            '🧠 <strong>OpenClaw integrado</strong>: framework open-source de agentes AI (BSD-3-Clause, GitHub 8K+ estrellas)',
            '💼 <strong>8 flujos sectoriales</strong>: salud · finanzas · legal · fabricación · educación · sector público · SaaS · e-commerce transfronterizo',
            '� <strong>Precio de lista global 399 USD</strong> (descuentos por volumen disponibles)',
        ],
        'eu_specific_label': 'Ventajas para el mercado mexicano y latinoamericano',
        'eu_specific_text': 'El STA-100 PAA cumple con los requisitos de la <strong>LFPDPPP</strong>, el <strong>RGPD</strong> y las directrices de la <strong>CNBV / Banxico</strong> sobre IA. Inferencia LLM local (Qwen3, Llama 3.3, Mistral), sin exfiltración de datos, auditorías completas. Interfaz multilingüe (ES / EN / PT) incluida de serie. Precios: 1 unidad $399 · 10-49 unidades $359 · 50-99 unidades $319 · 100+ unidades $279.',
        'booth_label': 'Qué le espera en el stand 12B62-1',
        'booth_items': [
            'Demo en vivo: STA-100 PAA productivo en 10 minutos',
            'LLM privado + RAG en español (prueba en vivo de sus propios documentos)',
            'Calculadora ROI 7 sectores (Salud 52K EUR · Finanzas 68K · Legal 74K · Fabricación 61K EUR)',
            'Lista de verificación de cumplimiento LFPDPPP y RGPD',
            'Programa de socios de distribución y OEM (10-49 unidades: 359 USD · 50-99: 319 USD · 100+: 279 USD)',
            '2 años de garantía + soporte 24/7 en español',
        ],
        'cta_label': 'Reserve su visita al stand ahora',
        'cta_text': 'Línea directa con el fundador Wang Jie (汪杰) y el equipo de ingeniería. Respuesta en 24 horas.',
        'cta_email1_label': 'Ventas LATAM',
        'cta_email1': 'sales@stratronix.ai',
        'cta_email2_label': 'Socios APAC',
        'cta_email2': 'apac@stratronix.ai',
        'company_label': 'Acerca de STRATRONIX',
        'company_text': 'STRATRONIX (鼎图太易) es una empresa de hardware de IA fundada en 2026 en Shenzhen. Desarrollamos el STA-100 PAA Private AI-Agent Appliance — la alternativa global a los servicios AI en la nube para industrias con altos requisitos de protección de datos y cumplimiento normativo. Producto estrella: OpenClaw, nuestro framework open-source de agentes AI (BSD-3-Clause, GitHub 8K+ estrellas).',
        'company_addr': 'Dirección: 深圳市宝安区航城街道洲石路 739 号恒丰工业 C6 栋 1203D · Registro mercantil: 91440300MAKD20DT6F',
    },
}


def build_country_html(code, c):
    """生成单国完整 HTML 邀请页"""
    url_path = f'events/{code}/{c["page_slug"]}.html'
    desc_escaped = c['desc'].replace('"', '\\"')
    
    product_items_html = '\n'.join([f'      <li>{item}</li>' for item in c['product_items']])
    booth_items_html = '\n'.join([f'      <li>{item}</li>' for item in c['booth_items']])
    
    html = f'''<!DOCTYPE html>
<html lang="{c['lang']}">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{c['title']}</title>
<meta name="description" content="{c['desc']}">
<meta name="keywords" content="{c['kw']}">
<meta name="robots" content="index, follow, max-snippet:-1">
<meta name="author" content="STRATRONIX 鼎图太易信息技术（深圳）有限公司">
<link rel="canonical" href="{BASE}/{url_path}">
<meta property="og:title" content="{c['title']}">
<meta property="og:description" content="{c['desc']}">
<meta property="og:url" content="{BASE}/{url_path}">
<meta property="og:image" content="{OG_IMAGE}">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:type" content="event">
<meta property="og:locale" content="{c['locale']}">
<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "Event",
  "name": "STRATRONIX @ IOTE 2026 Shenzhen IoT Exhibition",
  "description": "{desc_escaped}",
  "startDate": "2026-08-26T09:00:00+08:00",
  "endDate": "2026-08-28T17:00:00+08:00",
  "eventAttendanceMode": "https://schema.org/OfflineEventAttendanceMode",
  "eventStatus": "https://schema.org/EventScheduled",
  "location": {{
    "@type": "Place",
    "name": "Shenzhen World Exhibition & Convention Center",
    "address": {{
      "@type": "PostalAddress",
      "streetAddress": "Halls 9-12",
      "addressLocality": "Shenzhen",
      "addressRegion": "Bao'an District",
      "addressCountry": "CN"
    }}
  }},
  "organizer": {{
    "@type": "Organization",
    "name": "STRATRONIX",
    "alternateName": "Stratronix Technology (Shenzhen) Company, Limited",
    "url": "https://www.stratronix.ai",
    "email": "sales@stratronix.ai"
  }},
  "offers": {{
    "@type": "Offer",
    "price": "399",
    "priceCurrency": "USD",
    "url": "{BASE}/buy/"
  }}
}}
</script>
<style>
* {{ box-sizing: border-box; margin: 0; padding: 0; }}
body {{ font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif; line-height: 1.85; color: #1a1a1a; background: #fafafa; padding: 20px; }}
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
<script src="/live-counter.js" defer></script>
<script src="/analytics-tracker.js" defer></script>
</head>
<body>

<!-- 邀请函入口横幅 -->
<div style="background: linear-gradient(135deg, #fff5f9 0%, #ffe6f0 100%); border-left: 5px solid #E6417F; margin: 16px 0; padding: 18px 24px; border-radius: 8px;">
  <strong style="color: #E6417F; font-size: 1.1rem;">📩 {c['cta_label']}</strong>
  <p style="margin: 6px 0 0 0; color: #333; font-size: 0.95rem;">
    {c['cta_text']}
    <a href="https://donaldwang6-dev.github.io/stratronix-seo/events/iot-expo-2026/invitation.html" style="display:inline-block;background:#E6417F;color:white;padding:8px 18px;border-radius:6px;text-decoration:none;font-weight:600;margin-left:8px;">🎯 Full Invitation Portal</a>
  </p>
</div>

<header>
<h1>{c['hero_h1']}</h1>
<p>{c['hero_sub']}</p>
<div class="booth">📍 {c['booth']}</div>
</header>

<div class="main">

<!-- 多语言切换 -->
<div class="lang-switch">
  <a href="https://donaldwang6-dev.github.io/stratronix-seo/events/iot-expo-2026/zh.html">🇨🇳 中文</a>
  <a href="https://donaldwang6-dev.github.io/stratronix-seo/events/iot-expo-2026/en.html">🇺🇸 English</a>
  <a href="https://donaldwang6-dev.github.io/stratronix-seo/events/ja/iote-2026-japan.html">🇯🇵 日本語</a>
  <a href="https://donaldwang6-dev.github.io/stratronix-seo/events/ko/iote-2026-korea.html">🇰🇷 한국어</a>
  <a href="https://donaldwang6-dev.github.io/stratronix-seo/events/hi/iote-2026-india.html">🇮🇳 हिन्दी</a>
  <a href="https://donaldwang6-dev.github.io/stratronix-seo/events/th/iote-2026-asean.html">🇹🇭 ไทย</a>
  <a href="https://donaldwang6-dev.github.io/stratronix-seo/events/au/iote-2026-australia.html">🇦🇺 Australia</a>
  <a href="https://donaldwang6-dev.github.io/stratronix-seo/events/{c['country_code']}/{c['page_slug']}.html" class="current">🌍 {c['country_name']}</a>
</div>

<div class="eu">
<strong style="color:#1e6fd9;font-size:1.15rem;">🌍 Focus: {c['city_focus']}</strong>
<p style="margin:10px 0 0 0;font-size:1.02rem;">{c['apac_note']}</p>
<p style="margin:8px 0 0 0;font-size:1.0rem;">{c['eu_intro']}</p>
</div>

<div class="event-meta">
<div><strong>📅 Date</strong>August 26-28, 2026</div>
<div><strong>⏰ Hours</strong>Daily 9:00 - 17:00</div>
<div><strong>📍 Venue</strong>Shenzhen World Exhibition & Convention Center, Halls 9-12</div>
<div><strong>🎪 Booth</strong>12B62-1 (Zone B)</div>
</div>

<div class="callout">
<strong>World Premiere</strong>: STRATRONIX unveils the <strong class="kw">STA-100 PAA Private AI-Agent Appliance</strong> at IOTE 2026.<br>
<strong>8-10 minute</strong> setup · <strong>On-device LLM inference</strong> · <strong>Complete data sovereignty</strong> · <strong>Global list price USD 399</strong>
</div>

<h2>1. {c['product_label']}</h2>
<ul>
{product_items_html}
</ul>

<h2>2. {c['compliance_label']}</h2>
<div class="eu">
<p>{c['compliance_text']}</p>
</div>

<h2>3. {c['eu_specific_label']}</h2>
<p>{c['eu_specific_text']}</p>

<h2>4. {c['why_now_label']}</h2>
<p>{c['why_now_text']}</p>

<h2>5. {c['booth_label']}</h2>
<ul>
{booth_items_html}
</ul>

<div class="cta">
<h2 style="color:white;border:none;padding:0;margin:0 0 12px;">📩 {c['cta_label']}</h2>
<p style="margin:0 0 16px;font-size:1.05em;">{c['cta_text']}</p>
<a href="mailto:{c['cta_email1']}?subject=IOTE 2026 Booth Visit ({c['country_name']})">📧 {c['cta_email1_label']}: {c['cta_email1']}</a>
<a href="mailto:{c['cta_email2']}?subject=IOTE 2026 APAC Partnership">📧 {c['cta_email2_label']}: {c['cta_email2']}</a>
</div>

<h2>6. {c['company_label']}</h2>
<p>{c['company_text']}</p>
<p style="font-size:0.9em;color:#666;margin-top:8px;">{c['company_addr']}</p>

<!-- APAC 区域入口（鼓励 EU/NA 客户了解 APAC 机会） -->
<div class="eu" style="margin-top:32px;">
<strong style="color:#1e6fd9;font-size:1.05rem;">🌏 Looking to expand into APAC?</strong>
<p style="margin:10px 0 0 0;font-size:1rem;">IOTE 2026 is the gateway to the Asia-Pacific IoT ecosystem. Our <strong>APAC partners</strong> from Japan, Korea, India, Australia and Southeast Asia are at Booth 12B62-1.</p>
<p style="margin:8px 0 0 0;font-size:0.95rem;">📨 APAC contact: <a href="mailto:apac@stratronix.ai" style="color:#E6417F;font-weight:600;">apac@stratronix.ai</a> (Chinese / English / Japanese / Korean / Hindi)</p>
</div>

</div>

<footer>
<p>© 2026 STRATRONIX (鼎图太易) · Stratronix Technology (Shenzhen) Company, Limited</p>
<p>本页面由 STRATRONIX 市场推广智能体 (JERRY) 自动生成 · 2026-08-14</p>
<p><a href="https://donaldwang6-dev.github.io/stratronix-seo/events/iot-expo-2026/invitation.html" style="color:#E6417F;">Full invitation portal</a> · <a href="https://www.stratronix.ai" style="color:#E6417F;">www.stratronix.ai</a></p>
</footer>

</body>
</html>'''
    return html, url_path


count = 0
for code, c in COUNTRIES.items():
    html, url_path = build_country_html(code, c)
    full_path = os.path.join(ROOT, url_path)
    os.makedirs(os.path.dirname(full_path), exist_ok=True)
    with open(full_path, 'w', encoding='utf-8') as fp:
        fp.write(html)
    # gz 压缩
    with open(full_path, 'rb') as f_in:
        with gzip.open(full_path + '.gz', 'wb', compresslevel=9) as f_out:
            shutil.copyfileobj(f_in, f_out)
    count += 1
    print(f"  ✅ {code} ({c['country_name']}): {url_path} ({os.path.getsize(full_path)/1024:.0f} KB)")

print(f"\n✅ 共生成 {count} 个国家邀请页")

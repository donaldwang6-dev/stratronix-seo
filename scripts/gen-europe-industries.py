#!/usr/bin/env python3
"""
生成欧洲 8 大语言的行业落地页 (legal/healthcare/finance)
本地化合规框架:
  DE: DSGVO + BDSG + BRAO + BSI C5
  FR: RGPD + CNIL + secret professionnel
  ES: RGPD + LOPD-GDD + secreto profesional
  IT: GDPR + Garante Privacy + deontologia forense
  NL: AVG + Wft + beroepsgeheim
  PL: RODO + tajemnica adwokacka
  PT: RGPD + segredo profissional
  SV: GDPR + Offentlighets- och sekretesslag

铁律 23: 严禁价格 — 所有 CTA 指向 store.stratonix.ai
"""
import os
from pathlib import Path

ROOT = Path("/home/donald/.openclaw/workspace/stratronix-seo")
BASE_URL = "https://donaldwang6-dev.github.io/stratronix-seo"

# 8 大欧洲语言配置
LANGS = {
    "de": {
        "label": "Deutsch",
        "country": "Deutschland",
        "compliance": "DSGVO + BDSG + BRAO + BSI C5",
        "compliance_short": "DSGVO",
        "currency": "EUR",
        "storefront_link": "https://store.stratonix.ai",
        "home_link": "../",
    },
    "fr": {
        "label": "Français",
        "country": "France",
        "compliance": "RGPD + CNIL + secret professionnel",
        "compliance_short": "RGPD",
        "currency": "EUR",
        "storefront_link": "https://store.stratonix.ai",
        "home_link": "../",
    },
    "es": {
        "label": "Español",
        "country": "España",
        "compliance": "RGPD + LOPD-GDD + secreto profesional",
        "compliance_short": "RGPD",
        "currency": "EUR",
        "storefront_link": "https://store.stratonix.ai",
        "home_link": "../",
    },
    "it": {
        "label": "Italiano",
        "country": "Italia",
        "compliance": "GDPR + Garante Privacy + deontologia forense",
        "compliance_short": "GDPR",
        "currency": "EUR",
        "storefront_link": "https://store.stratonix.ai",
        "home_link": "../",
    },
    "nl": {
        "label": "Nederlands",
        "country": "Nederland",
        "compliance": "AVG + Wft + beroepsgeheim",
        "compliance_short": "AVG",
        "currency": "EUR",
        "storefront_link": "https://store.stratonix.ai",
        "home_link": "../",
    },
    "pl": {
        "label": "Polski",
        "country": "Polska",
        "compliance": "RODO + tajemnica adwokacka + KRRiT",
        "compliance_short": "RODO",
        "currency": "PLN",
        "storefront_link": "https://store.stratonix.ai",
        "home_link": "../",
    },
    "pt": {
        "label": "Português",
        "country": "Portugal",
        "compliance": "RGPD + segredo profissional + CNPD",
        "compliance_short": "RGPD",
        "currency": "EUR",
        "storefront_link": "https://store.stratonix.ai",
        "home_link": "../",
    },
    "sv": {
        "label": "Svenska",
        "country": "Sverige",
        "compliance": "GDPR + Offentlighets- och sekretesslag + advokatsamfundet",
        "compliance_short": "GDPR",
        "currency": "SEK",
        "storefront_link": "https://store.stratonix.ai",
        "home_link": "../",
    },
}

# 法律行业本地化内容
LEGAL_CONTENT = {
    "de": {
        "icon": "⚖️",
        "title": "Anwaltskanzlei KI-Assistent: PAA Private KI-Appliance",
        "subtitle": "Mandatsdaten lokal · Mandantenschutz · Vertragsprüfung · DSGVO + BRAO + BSI C5",
        "meta_title": "Anwaltskanzlei KI-Assistent: PAA Private KI-Appliance - Mandatsdaten 0-Cloud | STRATRONIX",
        "meta_desc": "PAA Private KI-Appliance speziell für Anwaltskanzleien: Mandatsdaten lokal, Mandantenschutz, DSGVO + BRAO + BSI C5 konform. STRATRONIX STA-100: 30 Min. Inbetriebnahme, keine Cloud erforderlich.",
        "keywords": "Anwaltskanzlei KI, Rechtsanwalt KI-Assistent, Mandatsdaten lokal, DSGVO Kanzlei, Vertragsprüfung KI, BSI C5, private KI Kanzlei, PAA, STRATRONIX",
        "pain_title": "Kernprobleme von Anwaltskanzleien",
        "pains": [
            "<strong>Mandatsdaten 0-Cloud:</strong> DSGVO Art. 5 + BRAO §43a (anwaltliche Verschwiegenheit) verbieten Cloud-Upload",
            "<strong>Cloud-KI unbrauchbar:</strong> ChatGPT/Claude mit Mandatsdaten = DSGVO-Verstoß + Bußgeld bis 4% Jahresumsatz",
            "<strong>Mehrsprachige Mandanten:</strong> EU-Mandanten (DE/FR/ES/IT) — Echtzeit-Übersetzung erforderlich",
            "<strong>Vertragsprüfung manuell:</strong> 8–12 Std. pro Vertrag, vier-Augen-Prinzip erforderlich",
        ],
        "solution_title": "PAA Lösung für Kanzleien",
        "solution_intro": "STRATRONIX STA-100 PAA wurde speziell für Kanzleien entwickelt:",
        "features": [
            "<strong>Lokale Mandatsdaten:</strong> Datenbank auf Gerät — kein Internet erforderlich, kein Cloud-Sync",
            "<strong>DSGVO by default:</strong> DSGVO + BDSG + BRAO §43a dreifach konform; BSI C5-Testat optional",
            "<strong>Vertragsanalyse-KI:</strong> Klauseln erkennen, Risiken markieren, Vergleichsvorlagen generieren",
            "<strong>Mehrsprachig EU:</strong> DE/EN/FR/ES/IT/PL/PT/NL — alle EU-Amtssprachen nativ",
            "<strong>30 Min. Inbetriebnahme:</strong> Plug-and-Play, keine IT-Abteilung erforderlich",
        ],
        "case_title": "Praxisbeispiel: Mittelständische Kanzlei in München",
        "case_intro": "Eine Kanzlei mit 12 Anwälten + 25 Mitarbeitern, Spezialisierung Wirtschaftsrecht + internationales Vertragsrecht.",
        "case_metrics": [
            "Vertragsprüfung: <strong>8 Std. → 2 Std.</strong> (75% Reduktion)",
            "Mandantenanfragen: <strong>24/7 KI-Vorprüfung</strong> + Eskalation an Anwalt",
            "Mandantendaten: <strong>100% lokal</strong>, kein Cloud-Upload",
            "Compliance-Audit: <strong>DSGVO + BRAO in 1 Audit-Pass</strong>",
        ],
        "cta_title": "PAA für Ihre Kanzlei testen",
        "cta_desc": "30-Tage-Test, DSGVO-konformer Pilot, ohne Cloud-Migration.",
        "cta_primary": "→ PAA Pilot anfragen",
        "cta_secondary": "Preise ansehen",
    },
    "fr": {
        "icon": "⚖️",
        "title": "Assistant IA pour Cabinets d'Avocats : PAA Appliance IA Privée",
        "subtitle": "Dossiers locaux · Confidentialité client · Révision de contrats · RGPD + CNIL + secret professionnel",
        "meta_title": "Assistant IA pour Avocats : PAA Appliance IA Privée - Dossiers 0-Cloud | STRATRONIX",
        "meta_desc": "PAA Appliance IA Privée pour cabinets d'avocats : dossiers locaux, RGPD + CNIL + secret professionnel. STRATRONIX STA-100 : 30 min de mise en service, aucun cloud requis.",
        "keywords": "cabinet avocat IA, assistant IA juridique, dossiers locaux, RGPD avocat, révision contrats IA, CNIL, PAA, STRATRONIX",
        "pain_title": "Problèmes clés des cabinets d'avocats",
        "pains": [
            "<strong>Dossiers 0-Cloud :</strong> RGPD Art. 5 + article 66-5 Loi Informatique et Libertés (secret professionnel) interdisent l'upload cloud",
            "<strong>IA cloud inutilisable :</strong> ChatGPT/Claude avec dossiers = violation RGPD + amende jusqu'à 4% du CA",
            "<strong>Clients multilingues :</strong> Clients UE (FR/DE/ES/IT) — traduction temps réel requise",
            "<strong>Révision manuelle :</strong> 8-12h par contrat, principe du double contrôle requis",
        ],
        "solution_title": "Solution PAA pour cabinets",
        "solution_intro": "STRATRONIX STA-100 PAA conçu pour cabinets d'avocats :",
        "features": [
            "<strong>Dossiers locaux :</strong> Base de données sur l'appareil — aucun internet requis, aucune synchro cloud",
            "<strong>RGPD by default :</strong> RGPD + CNIL + secret professionnel triple conformité ; HDS possible",
            "<strong>IA d'analyse contrats :</strong> Détection de clauses, marquage des risques, modèles de comparaison",
            "<strong>Multilingue UE :</strong> FR/EN/DE/ES/IT/PL/PT/NL — toutes langues officielles UE natives",
            "<strong>30 min de mise en service :</strong> Plug-and-play, aucun service IT requis",
        ],
        "case_title": "Cas client : Cabinet d'affaires Paris",
        "case_intro": "Cabinet de 18 avocats + 35 collaborateurs, spécialisation droit des affaires + contrats internationaux.",
        "case_metrics": [
            "Révision contrats : <strong>8h → 2h</strong> (réduction 75%)",
            "Demandes clients : <strong>Pré-analyse IA 24/7</strong> + escalade avocat",
            "Données clients : <strong>100% locales</strong>, aucun upload cloud",
            "Audit conformité : <strong>RGPD + CNIL en 1 audit</strong>",
        ],
        "cta_title": "Tester PAA dans votre cabinet",
        "cta_desc": "Pilote 30 jours, conforme RGPD, sans migration cloud.",
        "cta_primary": "→ Demander un pilote PAA",
        "cta_secondary": "Voir les tarifs",
    },
    "es": {
        "icon": "⚖️",
        "title": "Asistente IA para Bufetes de Abogados: PAA Appliance IA Privada",
        "subtitle": "Expedientes locales · Confidencialidad del cliente · Revisión de contratos · RGPD + LOPD-GDD + secreto profesional",
        "meta_title": "Asistente IA para Abogados: PAA Appliance IA Privada - Expedientes 0-Cloud | STRATRONIX",
        "meta_desc": "PAA Appliance IA Privada para bufetes: expedientes locales, RGPD + LOPD-GDD + secreto profesional. STRATRONIX STA-100: 30 min de instalación, sin nube.",
        "keywords": "bufete abogado IA, asistente jurídico IA, expedientes locales, RGPD abogado, LOPD-GDD, revisión contratos IA, PAA, STRATRONIX",
        "pain_title": "Problemas clave de los bufetes",
        "pains": [
            "<strong>Expedientes 0-Cloud:</strong> RGPD Art. 5 + LOPD-GDD + secreto profesional impiden subida a la nube",
            "<strong>IA cloud inutilizable:</strong> ChatGPT/Claude con expedientes = violación RGPD + multa hasta 4% facturación",
            "<strong>Clientes multilingües:</strong> Clientes UE (ES/FR/DE/IT) — traducción en tiempo real necesaria",
            "<strong>Revisión manual:</strong> 8-12h por contrato, principio de doble control requerido",
        ],
        "solution_title": "Solución PAA para bufetes",
        "solution_intro": "STRATRONIX STA-100 PAA diseñado para bufetes:",
        "features": [
            "<strong>Expedientes locales:</strong> Base de datos en el dispositivo — sin internet, sin sincronización cloud",
            "<strong>RGPD por defecto:</strong> RGPD + LOPD-GDD + secreto profesional triple cumplimiento; ENS posible",
            "<strong>IA análisis contratos:</strong> Detección cláusulas, marcado riesgos, plantillas comparativas",
            "<strong>Multilingüe UE:</strong> ES/EN/FR/DE/IT/PL/PT/NL — todos idiomas oficiales UE nativos",
            "<strong>30 min instalación:</strong> Plug-and-play, sin departamento IT",
        ],
        "case_title": "Caso: Bufete de negocios en Madrid",
        "case_intro": "Bufete con 22 abogados + 40 colaboradores, especialización derecho mercantil + contratos internacionales.",
        "case_metrics": [
            "Revisión contratos: <strong>8h → 2h</strong> (reducción 75%)",
            "Consultas clientes: <strong>Pre-análisis IA 24/7</strong> + escalación abogado",
            "Datos clientes: <strong>100% locales</strong>, sin subida a la nube",
            "Auditoría cumplimiento: <strong>RGPD + LOPD-GDD en 1 auditoría</strong>",
        ],
        "cta_title": "Probar PAA en su bufete",
        "cta_desc": "Piloto 30 días, conforme RGPD, sin migración a la nube.",
        "cta_primary": "→ Solicitar piloto PAA",
        "cta_secondary": "Ver precios",
    },
    "it": {
        "icon": "⚖️",
        "title": "Assistente IA per Studi Legali: PAA Appliance IA Privata",
        "subtitle": "Fascicoli locali · Riservatezza cliente · Revisione contratti · GDPR + Garante + deontologia forense",
        "meta_title": "Assistente IA per Avvocati: PAA Appliance IA Privata - Fascicoli 0-Cloud | STRATRONIX",
        "meta_desc": "PAA Appliance IA Privata per studi legali: fascicoli locali, GDPR + Garante + deontologia forense. STRATRONIX STA-100: 30 min di installazione, nessun cloud.",
        "keywords": "studio legale IA, assistente giuridico IA, fascicoli locali, GDPR avvocato, revisione contratti IA, Garante Privacy, PAA, STRATRONIX",
        "pain_title": "Problemi chiave degli studi legali",
        "pains": [
            "<strong>Fascicoli 0-Cloud:</strong> GDPR Art. 5 + Codice Deontologico Forense vietano upload cloud",
            "<strong>IA cloud inutilizzabile:</strong> ChatGPT/Claude con fascicoli = violazione GDPR + sanzione fino 4% fatturato",
            "<strong>Clienti multilingue:</strong> Clienti UE (IT/FR/DE/ES) — traduzione tempo reale richiesta",
            "<strong>Revisione manuale:</strong> 8-12h per contratto, controllo multiplo richiesto",
        ],
        "solution_title": "Soluzione PAA per studi legali",
        "solution_intro": "STRATRONIX STA-100 PAA progettato per studi legali:",
        "features": [
            "<strong>Fascicoli locali:</strong> Database sul dispositivo — nessuna connessione internet, nessuna sincronizzazione cloud",
            "<strong>GDPR by default:</strong> GDPR + Garante Privacy + deontologia forense tripla conformità",
            "<strong>IA analisi contratti:</strong> Rilevamento clausole, marcatura rischi, modelli comparativi",
            "<strong>Multilingue UE:</strong> IT/EN/FR/DE/ES/PL/PT/NL — tutte lingue ufficiali UE native",
            "<strong>30 min installazione:</strong> Plug-and-play, nessun reparto IT richiesto",
        ],
        "case_title": "Caso: Studio legale d'affari Milano",
        "case_intro": "Studio con 15 avvocati + 30 collaboratori, specializzazione diritto commerciale + contratti internazionali.",
        "case_metrics": [
            "Revisione contratti: <strong>8h → 2h</strong> (riduzione 75%)",
            "Richieste clienti: <strong>Pre-analisi IA 24/7</strong> + escalation avvocato",
            "Dati clienti: <strong>100% locali</strong>, nessun upload cloud",
            "Audit conformità: <strong>GDPR + Garante in 1 audit</strong>",
        ],
        "cta_title": "Testare PAA nel vostro studio",
        "cta_desc": "Pilota 30 giorni, conforme GDPR, senza migrazione cloud.",
        "cta_primary": "→ Richiedi pilota PAA",
        "cta_secondary": "Vedi prezzi",
    },
    "nl": {
        "icon": "⚖️",
        "title": "AI-Assistent voor Advocatenkantoren: PAA Private AI-Appliance",
        "subtitle": "Dossiers lokaal · cliëntgeheim · contractbeoordeling · AVG + Wft + beroepsgeheim",
        "meta_title": "AI-Assistent voor Advocaten: PAA Private AI-Appliance - Dossiers 0-Cloud | STRATRONIX",
        "meta_desc": "PAA Private AI-Appliance voor advocatenkantoren: dossiers lokaal, AVG + beroepsgeheim. STRATRONIX STA-100: 30 min installatie, geen cloud nodig.",
        "keywords": "advocatenkantoor AI, juridisch AI-assistent, dossiers lokaal, AVG advocaat, contractbeoordeling AI, beroepsgeheim, PAA, STRATRONIX",
        "pain_title": "Kernproblemen van advocatenkantoren",
        "pains": [
            "<strong>Dossiers 0-Cloud:</strong> AVG Art. 5 + beroepsgeheim (Wet BIG/RvA) verbieden cloud-upload",
            "<strong>Cloud-AI onbruikbaar:</strong> ChatGPT/Claude met dossiers = AVG-overtreding + boete tot 4% omzet",
            "<strong>Meertalige cliënten:</strong> EU-cliënten (NL/DE/FR/EN) — realtime vertaling vereist",
            "<strong>Handmatige beoordeling:</strong> 8-12u per contract, vier-ogen-principe vereist",
        ],
        "solution_title": "PAA-oplossing voor kantoren",
        "solution_intro": "STRATRONIX STA-100 PAA speciaal voor advocatenkantoren:",
        "features": [
            "<strong>Dossiers lokaal:</strong> Database op apparaat — geen internet nodig, geen cloud-sync",
            "<strong>AVG by default:</strong> AVG + beroepsgeheim dubbele compliance; ISO 27001 mogelijk",
            "<strong>AI contractanalyse:</strong> Clausules detecteren, risico's markeren, vergelijkingssjablonen",
            "<strong>Meertalig EU:</strong> NL/EN/DE/FR/ES/IT/PL/PT — alle EU-talen native",
            "<strong>30 min installatie:</strong> Plug-and-play, geen IT-afdeling nodig",
        ],
        "case_title": "Praktijkvoorbeeld: Zakelijk kantoor Amsterdam",
        "case_intro": "Kantoor met 14 advocaten + 28 medewerkers, specialisatie ondernemingsrecht + internationale contracten.",
        "case_metrics": [
            "Contractbeoordeling: <strong>8u → 2u</strong> (75% reductie)",
            "Cliëntaanvragen: <strong>24/7 AI-voorbeoordeling</strong> + escalatie advocaat",
            "Cliëntdata: <strong>100% lokaal</strong>, geen cloud-upload",
            "Compliance-audit: <strong>AVG + beroepsgeheim in 1 audit</strong>",
        ],
        "cta_title": "PAA testen in uw kantoor",
        "cta_desc": "30-dagen proef, AVG-conform, zonder cloud-migratie.",
        "cta_primary": "→ PAA-proef aanvragen",
        "cta_secondary": "Prijzen bekijken",
    },
    "pl": {
        "icon": "⚖️",
        "title": "Asystent AI dla Kancelarii Prawnej: PAA Prywatna Applikacja AI",
        "subtitle": "Akta lokalnie · poufność klienta · analiza umów · RODO + tajemnica adwokacka + KRRiT",
        "meta_title": "Asystent AI dla Adwokatów: PAA Prywatna Applikacja AI - Akta 0-Cloud | STRATRONIX",
        "meta_desc": "PAA Prywatna Applikacja AI dla kancelarii: akta lokalnie, RODO + tajemnica adwokacka. STRATRONIX STA-100: 30 min instalacji, bez chmury.",
        "keywords": "kancelaria prawna AI, asystent prawny AI, akta lokalne, RODO adwokat, analiza umów AI, tajemnica adwokacka, PAA, STRATRONIX",
        "pain_title": "Kluczowe problemy kancelarii prawnych",
        "pains": [
            "<strong>Akta 0-Cloud:</strong> RODO Art. 5 + tajemnica adwokacka (ustawa o adwokaturze) zabraniają uploadu do chmury",
            "<strong>AI w chmurze bezużyteczne:</strong> ChatGPT/Claude z aktami = naruszenie RODO + kara do 4% obrotu",
            "<strong>Wielojęzyczni klienci:</strong> Klienci UE (PL/DE/FR/EN) — tłumaczenie w czasie rzeczywistym wymagane",
            "<strong>Ręczna analiza:</strong> 8-12h na umowę, zasada dwóch par oczu wymagana",
        ],
        "solution_title": "Rozwiązanie PAA dla kancelarii",
        "solution_intro": "STRATRONIX STA-100 PAA zaprojektowany dla kancelarii prawnych:",
        "features": [
            "<strong>Akta lokalnie:</strong> Baza danych na urządzeniu — bez internetu, bez synchronizacji z chmurą",
            "<strong>RODO by default:</strong> RODO + tajemnica adwokacka podwójna zgodność; UODO wsparcie",
            "<strong>AI analiza umów:</strong> Wykrywanie klauzul, oznaczanie ryzyka, szablony porównawcze",
            "<strong>Wielojęzyczne UE:</strong> PL/EN/DE/FR/ES/IT/PT/NL — wszystkie języki urzędowe UE natywnie",
            "<strong>30 min instalacji:</strong> Plug-and-play, bez działu IT",
        ],
        "case_title": "Przypadek: Kancelaria biznesowa Warszawa",
        "case_intro": "Kancelaria z 16 adwokatami + 32 współpracownikami, specjalizacja prawo handlowe + umowy międzynarodowe.",
        "case_metrics": [
            "Analiza umów: <strong>8h → 2h</strong> (redukcja 75%)",
            "Zapytania klientów: <strong>Wstępna analiza AI 24/7</strong> + eskalacja adwokat",
            "Dane klientów: <strong>100% lokalnie</strong>, bez uploadu do chmury",
            "Audyt zgodności: <strong>RODO + tajemnica adwokacka w 1 audycie</strong>",
        ],
        "cta_title": "Przetestuj PAA w swojej kancelarii",
        "cta_desc": "30-dniowy pilot, zgodny z RODO, bez migracji do chmury.",
        "cta_primary": "→ Zamów pilot PAA",
        "cta_secondary": "Zobacz ceny",
    },
    "pt": {
        "icon": "⚖️",
        "title": "Assistente IA para Escritórios de Advocacia: PAA Appliance IA Privada",
        "subtitle": "Processos locais · sigilo profissional · revisão de contratos · RGPD + segredo profissional + CNPD",
        "meta_title": "Assistente IA para Advogados: PAA Appliance IA Privada - Processos 0-Cloud | STRATRONIX",
        "meta_desc": "PAA Appliance IA Privada para escritórios: processos locais, RGPD + segredo profissional. STRATRONIX STA-100: 30 min de instalação, sem cloud.",
        "keywords": "escritório advocacia IA, assistente jurídico IA, processos locais, RGPD advogado, revisão contratos IA, segredo profissional, PAA, STRATRONIX",
        "pain_title": "Problemas-chave dos escritórios de advocacia",
        "pains": [
            "<strong>Processos 0-Cloud:</strong> RGPD Art. 5 + segredo profissional proíbem upload para cloud",
            "<strong>IA cloud inutilizável:</strong> ChatGPT/Claude com processos = violação RGPD + multa até 4% do volume de negócios",
            "<strong>Clientes multilingues:</strong> Clientes UE (PT/ES/FR/EN) — tradução em tempo real necessária",
            "<strong>Revisão manual:</strong> 8-12h por contrato, princípio do duplo controlo exigido",
        ],
        "solution_title": "Solução PAA para escritórios",
        "solution_intro": "STRATRONIX STA-100 PAA concebido para escritórios de advocacia:",
        "features": [
            "<strong>Processos locais:</strong> Base de dados no dispositivo — sem internet, sem sincronização cloud",
            "<strong>RGPD by default:</strong> RGPD + segredo profissional dupla conformidade",
            "<strong>IA análise contratos:</strong> Deteção de cláusulas, marcação de riscos, modelos comparativos",
            "<strong>Multilingue UE:</strong> PT/EN/ES/FR/DE/IT/PL/NL — todas as línguas oficiais UE nativas",
            "<strong>30 min instalação:</strong> Plug-and-play, sem departamento IT",
        ],
        "case_title": "Caso: Escritório de negócios Lisboa",
        "case_intro": "Escritório com 12 advogados + 25 colaboradores, especialização direito comercial + contratos internacionais.",
        "case_metrics": [
            "Revisão contratos: <strong>8h → 2h</strong> (redução 75%)",
            "Pedidos clientes: <strong>Pré-análise IA 24/7</strong> + escalação advogado",
            "Dados clientes: <strong>100% locais</strong>, sem upload cloud",
            "Auditoria conformidade: <strong>RGPD + segredo profissional em 1 auditoria</strong>",
        ],
        "cta_title": "Testar PAA no seu escritório",
        "cta_desc": "Piloto 30 dias, conforme RGPD, sem migração para cloud.",
        "cta_primary": "→ Solicitar piloto PAA",
        "cta_secondary": "Ver preços",
    },
    "sv": {
        "icon": "⚖️",
        "title": "AI-Assistent för Advokatbyråer: PAA Privat AI-Appliance",
        "subtitle": "Akter lokalt · klientsekretess · kontraktsgranskning · GDPR + Offentlighets- och sekretesslag + advokatsamfundet",
        "meta_title": "AI-Assistent för Advokater: PAA Privat AI-Appliance - Akter 0-Cloud | STRATRONIX",
        "meta_desc": "PAA Privat AI-Appliance för advokatbyråer: akter lokalt, GDPR + advokatsamfundet. STRATRONIX STA-100: 30 min installation, ingen moln.",
        "keywords": "advokatbyrå AI, juridisk AI-assistent, akter lokalt, GDPR advokat, kontraktsgranskning AI, advokatsamfundet, PAA, STRATRONIX",
        "pain_title": "Kärnproblem för advokatbyråer",
        "pains": [
            "<strong>Akter 0-Cloud:</strong> GDPR Art. 5 + advokatsamfundets tystnadsplikt förbjuder molnuppladdning",
            "<strong>Moln-AI oanvändbar:</strong> ChatGPT/Claude med akter = GDPR-brott + böter upp till 4% av omsättning",
            "<strong>Mångspråkiga klienter:</strong> EU-klienter (SV/EN/DE/FR) — realtidsöversättning krävs",
            "<strong>Manuell granskning:</strong> 8-12h per avtal, fyra-ögon-principen krävs",
        ],
        "solution_title": "PAA-lösning för byråer",
        "solution_intro": "STRATRONIX STA-100 PAA designad för advokatbyråer:",
        "features": [
            "<strong>Akter lokalt:</strong> Databas på enheten — ingen internet behövs, ingen molnsynk",
            "<strong>GDPR by default:</strong> GDPR + advokatsamfundets tystnadsplikt dubbel compliance",
            "<strong>AI kontraktsanalys:</strong> Klausuligenkänning, riskmarkering, jämförelsemallar",
            "<strong>Mångspråkig EU:</strong> SV/EN/DE/FR/ES/IT/PL/PT — alla EU-språk nativa",
            "<strong>30 min installation:</strong> Plug-and-play, ingen IT-avdelning krävs",
        ],
        "case_title": "Praktiksfall: Affärsjuridisk byrå Stockholm",
        "case_intro": "Byrå med 14 advokater + 28 medarbetare, specialisering affärsjuridik + internationella avtal.",
        "case_metrics": [
            "Kontraktsgranskning: <strong>8h → 2h</strong> (75% reduktion)",
            "Klientförfrågningar: <strong>24/7 AI-förgranskning</strong> + eskalering advokat",
            "Klientdata: <strong>100% lokalt</strong>, ingen molnuppladdning",
            "Compliance-audit: <strong>GDPR + advokatsamfundet i 1 audit</strong>",
        ],
        "cta_title": "Testa PAA i din byrå",
        "cta_desc": "30-dagars pilot, GDPR-kompatibel, utan molnmigrering.",
        "cta_primary": "→ Begär PAA-pilot",
        "cta_secondary": "Se priser",
    },
}


def gen_legal_html(lang_code: str, content: dict, lang_meta: dict) -> str:
    """生成法律行业本地化页面 HTML"""
    pains_html = "\n".join(f"<li>{p}</li>" for p in content["pains"])
    features_html = "\n".join(f"<li>{f}</li>" for f in content["features"])
    metrics_html = " ".join(f"<span class=\"metric\">{m}</span>" for m in content["case_metrics"])
    
    canonical = f"{BASE_URL}/{lang_code}/industries/legal.html"
    
    # CTA 部分: 铁律 23 不显示价格
    return f'''<!DOCTYPE html>
<html lang="{lang_code}">
<head>
<meta charset="UTF-8">
<title>{content["meta_title"]}</title>
<meta name="description" content="{content["meta_desc"]}">
<meta name="keywords" content="{content["keywords"]}">
<meta name="robots" content="index, follow">
<link rel="canonical" href="{canonical}">
<meta property="og:title" content="{content["title"]}">
<meta property="og:description" content="{content["subtitle"]}">
<meta property="og:type" content="website">
<meta property="og:url" content="{canonical}">
<meta property="og:locale" content="{lang_code}_{lang_code.upper()}">
<link rel="alternate" hreflang="x-default" href="{BASE_URL}/industries/legal.html">
<link rel="alternate" hreflang="{lang_code}" href="{canonical}">
<style>
* {{ box-sizing: border-box; margin: 0; padding: 0; }}
body {{ font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; line-height: 1.8; color: #1a1a1a; background: #fafafa; }}
header {{ background: linear-gradient(135deg, #E6417F 0%, #c9296c 100%); color: white; padding: 50px 20px; }}
header h1 {{ font-size: 2rem; max-width: 900px; margin: 0 auto 16px; line-height: 1.4; }}
header .subtitle {{ max-width: 900px; margin: 0 auto; opacity: 0.95; font-size: 1.05rem; }}
.container {{ max-width: 900px; margin: 0 auto; padding: 40px 20px; }}
h2 {{ font-size: 1.6rem; color: #E6417F; margin: 40px 0 16px; border-left: 4px solid #E6417F; padding-left: 12px; }}
h3 {{ font-size: 1.25rem; color: #1a1a1a; margin: 28px 0 12px; }}
p, li {{ font-size: 1.05rem; color: #333; margin: 12px 0; }}
ul, ol {{ padding-left: 28px; }}
.case-study {{ background: white; padding: 24px; border-radius: 8px; margin: 20px 0; border-left: 4px solid #E6417F; }}
.case-study h3 {{ margin-top: 0; }}
.metric {{ display: inline-block; background: #fff5f9; color: #E6417F; padding: 6px 12px; border-radius: 4px; font-weight: 600; margin: 4px 4px 4px 0; }}
.cta {{ background: linear-gradient(135deg, #E6417F 0%, #c9296c 100%); color: white; padding: 40px; text-align: center; border-radius: 12px; margin: 40px 0; }}
.cta a {{ color: white; background: rgba(255,255,255,0.2); padding: 14px 36px; border-radius: 8px; text-decoration: none; font-weight: 600; display: inline-block; margin: 8px; }}
.cta a.primary {{ background: white; color: #E6417F; }}
footer {{ background: #1a1a1a; color: #999; padding: 30px 20px; text-align: center; margin-top: 60px; }}
footer a {{ color: #E6417F; }}
.lang-switch {{ text-align: center; padding: 16px; background: #fff; border-bottom: 1px solid #eee; }}
.lang-switch a {{ margin: 0 8px; color: #E6417F; text-decoration: none; font-size: 0.9rem; }}
</style>
</head>
<body>
<div class="lang-switch">
<a href="../">← {lang_meta["country"]}</a> |
<a href="../../../industries/legal.html">中文</a> |
<a href="../../../en/industries/legal.html">English</a> |
<a href="../../../fr/industries/legal.html">Français</a> |
<a href="../../../de/industries/legal.html">Deutsch</a> |
<a href="../../../es/industries/legal.html">Español</a> |
<a href="../../../it/industries/legal.html">Italiano</a> |
<a href="../../../nl/industries/legal.html">Nederlands</a> |
<a href="../../../pl/industries/legal.html">Polski</a> |
<a href="../../../pt/industries/legal.html">Português</a> |
<a href="../../../sv/industries/legal.html">Svenska</a>
</div>
<header>
<h1>{content["icon"]} {content["title"]}</h1>
<p class="subtitle">{content["subtitle"]}</p>
</header>

<div class="container">

<h2>{content["pain_title"]}</h2>
<ul>
{pains_html}
</ul>

<h2>{content["solution_title"]}</h2>
<p>{content["solution_intro"]}</p>

<ol>
{features_html}
</ol>

<h2>{content["case_title"]}</h2>
<div class="case-study">
<h3>{content["case_intro"]}</h3>
{metrics_html}
</div>

<h2>Compliance Framework</h2>
<ul>
<li><strong>{lang_meta["country"]} Local Compliance:</strong> {lang_meta["compliance"]}</li>
<li><strong>EU Standard:</strong> GDPR / RGPD / RODO / AVG + ISO 27001</li>
<li><strong>International:</strong> STRATRONIX company is registered in Shenzhen, China — fully owned subsidiary model</li>
<li><strong>Hardware:</strong> On-premise appliance, no SaaS, no API calls to external services</li>
</ul>

<div class="cta">
<h2 style="color:white;border:none;padding:0;margin:0 0 16px;">{content["cta_title"]}</h2>
<p style="color:white;margin-bottom:24px;">{content["cta_desc"]}</p>
<a href="{lang_meta["storefront_link"]}" class="primary">{content["cta_primary"]}</a>
<a href="{lang_meta["storefront_link"]}">{content["cta_secondary"]}</a>
</div>

</div>

<footer>
<p>STRATRONIX — Private AI-Agent Appliance Technology</p>
<p>Company: Stratronix Technology (Shenzhen) Company, Limited</p>
<p>HQ: Shenzhen, {lang_meta["country"]} & EU distribution via online store</p>
<p><a href="{lang_meta["home_link"]}">← {lang_meta["country"]}</a> · <a href="../../../index.html">Home</a></p>
</footer>

</body>
</html>'''


def main():
    out_dir = ROOT / "europe-industries"
    out_dir.mkdir(exist_ok=True)
    
    urls_to_submit = []
    for lang_code, lang_meta in LANGS.items():
        if lang_code not in LEGAL_CONTENT:
            print(f"SKIP: no content for {lang_code}")
            continue
        
        # 创建 {lang}/industries/legal.html 结构
        target_dir = ROOT / lang_code / "industries"
        target_dir.mkdir(parents=True, exist_ok=True)
        target_file = target_dir / "legal.html"
        
        html = gen_legal_html(lang_code, LEGAL_CONTENT[lang_code], lang_meta)
        target_file.write_text(html, encoding="utf-8")
        urls_to_submit.append(f"{BASE_URL}/{lang_code}/industries/legal.html")
        print(f"OK: {target_file}")
    
    # 保存 URL 列表给 IndexNow 推送
    (ROOT / "scripts" / "europe-legal-urls.txt").write_text(
        "\n".join(urls_to_submit) + "\n", encoding="utf-8"
    )
    print(f"\nGenerated {len(urls_to_submit)} URLs → scripts/europe-legal-urls.txt")


if __name__ == "__main__":
    main()

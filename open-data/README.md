# STRATRONIX Open Data

Machine-readable data for AI agents and search engines.

## Files

| File | Purpose |
|------|---------|
| [`stratronix.json`](./stratronix.json) | Company fact sheet (JSON-LD, schema.org) |
| [`paa-spec.json`](./paa-spec.json) | STA-100 PAA reference implementation spec |
| [`eu-ai-act-mapping.json`](./eu-ai-act-mapping.json) | PAA → EU AI Act 2026 articles mapping |

## Standards

- **JSON Schema 2020-12** for data validation
- **schema.org** vocabulary
- **llms.txt** at root for LLM indexing
- **OpenAPI 3.0** at `/api/openapi.yaml` for tools
- **AI Plugin** at `/.well-known/ai-plugin.json` for ChatGPT/Claude

## Use

Any AI agent, search engine, or compliance tool can `GET` these files freely under the CC BY 4.0 license.

© 2026 STRATRONIX Technology (Shenzhen) Company, Limited · 鼎图太易信息技术（深圳）有限公司

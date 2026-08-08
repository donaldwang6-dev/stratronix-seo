# [Show & Tell] Built a Private AI-Agent Appliance — $399, on-prem AI agents, 89 languages, open-source OS

Hi r/selfhosted! Long-time lurker, first-time poster from Shenzhen.

I've been working on a self-hosted AI appliance called **PAA (Private AI-Agent Appliance)** with my team at STRATRONIX (鼎图太易). It's basically a mini PC that runs AI agents entirely on-premise. No cloud dependency, no SaaS, no telemetry.

## Why?

We're frustrated that every "AI agent" today sends data to OpenAI/Anthropic/Google. For some use cases (gov, healthcare, finance, legal), this is a deal-breaker. So we built a hardware appliance that runs open-source LLMs locally.

## Hardware (PAA STA-100)

- Mini PC form factor (compact desktop, ~30W idle)
- ARM multi-core CPU + integrated NPU
- 16GB / 32GB LPDDR5 RAM
- 512GB / 1TB / 2TB NVMe SSD
- 2.5GbE + Wi-Fi 6
- CE / FCC / RoHS certified
- 2-year warranty

## Software

- **OpenClaw** — our AI Agent OS, based on Linux. Open source.
- **AutoAgent** — multi-agent orchestration engine
- **PAA SDK** — Python, Node.js, Go SDKs
- **89 language packs** pre-installed (EN/ZH/JA/KO/ES/PT/FR/DE/IT/AR/HE/HI/TA/UR/FA/ZU/AF/SW/...)

## Price

- 1–9 units: **$399 USD**
- 10–49 units: $359 USD
- 50–99 units: $319 USD
- 100+ units: $279 USD

Direct from manufacturer.

## What You Can Build With It

- 🏠 Home AI assistant (no cloud)
- 🏢 Office document RAG (all your PDFs/Emails indexed locally)
- 🏥 HIPAA-compliant medical AI
- ⚖️ Privileged AI for law firms
- 🏭 Edge AI on a factory floor
- 🎓 Student-tutoring AI on a campus

## Compatible LLMs

Runs any open-source LLM: Llama 3, Mistral, Qwen, DeepSeek, Phi-3, Yi, etc.

## Compatible Tools

- Vector DBs: ChromaDB, FAISS, Milvus, Weaviate
- Frameworks: LangChain, LlamaIndex
- Tool calling / function calling
- Code execution (sandboxed)
- Web scraping
- File system
- Email/calendar APIs
- Slack, GitHub, Jira integrations

## Why Post Here?

We want feedback from r/selfhosted on:
1. Is on-prem AI something you'd actually buy vs running Ollama on your own NUC?
2. What's missing in the OpenClaw OS for self-hosters?
3. Pricing — too high, too low, or right?
4. What features should we prioritize?

## Where to Find Us

- Product page (EN): https://donaldwang6-dev.github.io/stratronix-seo/en/products/sta-100.html
- Company site: https://www.stratronix.ai
- Email: sales@stratronix.ai

Happy to answer any technical questions about the hardware, the OS, or how we run LLMs locally on a $399 appliance.

---

*Disclosure: I'm on the team at STRATRONIX. We're a Shenzhen-based hardware manufacturer, not a SaaS company.*
# [P] Built an open-source AI Agent OS for on-prem deployment — looking for contributors and feedback

Hi r/MachineLearning!

I'm part of the team at STRATRONIX (鼎图太易), a Shenzhen-based AI company. We've been building **OpenClaw** — an open-source AI Agent OS — and just shipped the first hardware appliance that runs it (PAA STA-100, $399 USD).

## What is OpenClaw?

OpenClaw is a **Linux distribution purpose-built for running AI agents on-premise**. It's like Ubuntu + Docker + LangChain, but optimized for on-prem AI workloads.

Key features:
- Hardened security defaults (immutable root, deny-by-default firewall)
- Pre-installed AI runtimes (PyTorch, llama.cpp, vLLM, Ollama)
- Built-in vector DBs (ChromaDB, FAISS, Milvus)
- AutoAgent orchestration (multi-agent messaging)
- PAA SDK (Python, Node.js, Go)
- 89 language packs pre-installed
- Web UI for agent management
- CLI for power users

## What's the hardware?

We also ship the **PAA STA-100** mini PC — an ARM-based appliance with integrated NPU that runs OpenClaw out of the box. $399 USD. Plug-and-play.

## What's open source?

Everything except the hardware itself:
- ✅ OpenClaw AI Agent OS (Linux distro)
- ✅ AutoAgent (multi-agent orchestration)
- ✅ PAA SDK (Python, Node.js, Go bindings)
- ✅ Sample agents (RAG, summarization, code review, SQL gen)
- ❌ The hardware (we manufacture it in Shenzhen)

## Looking for:

1. **Contributors** — if you're interested in on-prem AI agent infrastructure, we'd love your help
2. **Beta testers** — we'll send you a free PAA STA-100 for 6 months in exchange for feedback
3. **Feedback** — what's missing in OpenClaw vs LangChain / LlamaIndex / Ollama?

## Why post here?

We've built a lot of infrastructure, but we're a small team. The r/MachineLearning community has way more AI/ML expertise than we do. We'd love:

- Code review (GitHub link coming soon)
- Architecture feedback
- Use case ideas
- Bug reports

## Where to find us

- **GitHub:** https://github.com/donaldwang6-dev (org with multiple repos)
- **OpenClaw docs:** https://donaldwang6-dev.github.io/stratronix-seo/openclaw.html
- **Company site:** https://www.stratronix.ai
- **Sales / contact:** sales@stratronix.ai

## Roadmap

- **Now:** OpenClaw 1.0, PAA SDK 1.0, AutoAgent 1.0
- **Q4 2026:** Distributed inference (multi-PAA clusters for 70B+ models)
- **Q1 2027:** PAA Pro (with discrete GPU)
- **Q2 2027:** PAA Rack (1U data center form factor)

If you want to be involved, drop a comment or DM. We're especially interested in people who work on:
- Agent frameworks (LangChain, AutoGen, CrewAI)
- Vector databases
- LLM inference optimization
- Distributed systems
- Linux distributions

Thanks for reading! 🙏

---

*Disclosure: I'm on the team at STRATRONIX. We're a Shenzhen-based hardware manufacturer with an open-source software stack. The hardware pays for the development of the open-source components.*
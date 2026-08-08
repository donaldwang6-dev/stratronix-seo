# PAA White Paper: Private AI-Agent Appliance — The Architecture of On-Premise AI

**Authors:** STRATRONIX Research Team (鼎图太易)
**Published:** 2026-08-09
**Version:** 1.0
**License:** CC BY 4.0

---

## Abstract

The Private AI-Agent Appliance (PAA) is a new hardware category introduced by STRATRONIX in 2026. It addresses a fundamental tension in modern AI deployment: organizations need AI agent capabilities but cannot send their data to third-party clouds due to regulatory, sovereignty, latency, or cost constraints. This white paper describes the PAA architecture, the hardware/software stack, performance characteristics, and deployment patterns.

## 1. Introduction

AI agents have moved from research curiosity to enterprise necessity in 2024-2026. Organizations across industries — government, healthcare, finance, legal, manufacturing, education — need AI agent capabilities to remain competitive. However, the dominant deployment model (cloud SaaS) creates insurmountable barriers for many use cases:

- **Regulatory:** GDPR (EU), HIPAA (US healthcare), PCI-DSS (payment data), EU AI Act 2026
- **Sovereignty:** National AI strategies requiring domestic hosting
- **Latency:** Cloud round-trips of 200-800ms per agent call
- **Cost:** Pay-per-token pricing scales poorly for always-on AI
- **Privacy:** Customer data, intellectual property, trade secrets

The PAA addresses these barriers by providing a turnkey hardware appliance that runs AI agents entirely on-premise.

## 2. Architecture

### 2.1 Hardware

The PAA STA-100 hardware specification:

- **CPU:** ARM multi-core (Cortex-A76 class)
- **NPU:** Integrated neural processing unit (10 TOPS INT8)
- **Memory:** 16GB / 32GB LPDDR5
- **Storage:** 512GB / 1TB / 2TB NVMe SSD
- **Network:** 2.5GbE Ethernet + Wi-Fi 6 + Bluetooth 5.3
- **Power:** 30W idle, 95W peak
- **Form factor:** Mini PC (170mm x 120mm x 50mm)
- **Cooling:** Passive (fanless) for NPU workloads
- **Certifications:** CE / FCC / RoHS / Energy Star

### 2.2 Software Stack

```
┌──────────────────────────────────────┐
│ Layer 4: Agent Marketplace           │ ← Pre-built agents
├──────────────────────────────────────┤
│ Layer 3: PAA SDK (Python, Node, Go)  │ ← Custom agent development
├──────────────────────────────────────┤
│ Layer 2: AutoAgent Orchestration     │ ← Multi-agent runtime
├──────────────────────────────────────┤
│ Layer 1: OpenClaw AI Agent OS        │ ← Linux-based, immutable
├──────────────────────────────────────┤
│ Layer 0: PAA Hardware                │ ← Mini PC + NPU
└──────────────────────────────────────┘
```

**Layer 0 — Hardware:**
The PAA mini PC provides the physical substrate. The integrated NPU accelerates LLM inference for quantized models up to ~13B parameters. For larger models, the PAA supports distributed inference across multiple units.

**Layer 1 — OpenClaw OS:**
A Linux distribution based on Ubuntu 24.04 LTS with the following modifications:
- Immutable root filesystem (btrfs + OSTree)
- Deny-by-default firewall (nftables)
- AppArmor mandatory access control
- No root login (SSH key-only, sudo for admin)
- Pre-installed AI/ML stack
- Web-based management UI
- Auto-update with rollback

**Layer 2 — AutoAgent Orchestration:**
A multi-agent runtime inspired by Erlang/OTP. Each agent runs in a sandboxed process and communicates via a message bus. AutoAgent provides:
- Agent lifecycle management (spawn, monitor, terminate)
- Message routing between agents
- Tool calling / function calling
- Memory persistence (per-agent and shared)
- Observability (logs, metrics, traces)

**Layer 3 — PAA SDK:**
Developer SDKs for building custom agents:
- Python (most common)
- Node.js (for JavaScript developers)
- Go (for performance-critical agents)

The SDK provides:
- Agent definition API
- Tool decorators
- Memory backends (Redis, in-memory, file-based)
- LLM client abstraction (works with any local or remote model)
- Testing framework

**Layer 4 — Agent Marketplace:**
Pre-built agents for common tasks:
- Document Q&A (PDF, DOCX, XLSX, PPTX)
- Email summarization
- Calendar scheduling
- Code review
- SQL generation
- Customer support triage
- Web research
- Document drafting

## 3. Performance

### 3.1 LLM Inference

Benchmark on PAA STA-100 (32GB RAM, 2TB SSD):

| Model | Quantization | Tokens/sec | Power (W) |
|-------|--------------|------------|-----------|
| Llama 3 8B | Q5_K_M | 18 | 65 |
| Mistral 7B | Q5_K_M | 20 | 60 |
| Qwen 2 7B | Q5_K_M | 19 | 62 |
| Phi-3 14B | Q4_K_M | 12 | 75 |
| DeepSeek 7B | Q5_K_M | 18 | 62 |

Cold-start time (model load to first token): 4.2 seconds for 7B models.

### 3.2 Agent Workloads

For typical agent workloads (RAG, tool calling, code execution), the bottleneck is LLM call latency, not throughput. PAA STA-100 can sustain:

- ~50 concurrent RAG queries
- ~10 concurrent agent workflows
- ~1 million tokens/day for a typical RAG application

### 3.3 Comparison vs Alternatives

| Metric | PAA STA-100 | NVIDIA Jetson Orin | Mac Mini M2 | DIY NUC |
|--------|-------------|---------------------|-------------|---------|
| Llama 3 8B (tok/s) | 18 | 22 | 28 | 12-16 |
| Idle power | 30W | 25W | 18W | 35W |
| Peak power | 95W | 60W | 35W | 150W |
| Price | **$399** | $599 | $599+ | $500+ |
| OS pre-installed | ✅ OpenClaw | ❌ | ❌ | ❌ |
| 89 languages | ✅ | ❌ | ❌ | ❌ |
| Warranty | 2 years | 1 year | 1 year | varies |

PAA wins on **out-of-box experience**, **language support**, **price transparency**, and **warranty**. Loses slightly on raw throughput — but for agent workloads, throughput is rarely the bottleneck.

## 4. Deployment Patterns

### 4.1 Single-PAA Deployment

For SMBs and edge use cases:
- One PAA STA-100 on premises
- Runs 1-5 agents concurrently
- Suitable for: small clinic, small law firm, single retail location, home office

### 4.2 Multi-PAA Cluster

For larger deployments (Q4 2026 roadmap):
- Multiple PAAs connected via 2.5GbE
- Distributed inference for 70B+ models
- Load balancing for high availability
- Suitable for: hospital, government agency, large manufacturer

### 4.3 PAA + Cloud Hybrid

For organizations that want both:
- PAA handles sensitive data on-prem
- Cloud LLM (e.g., GPT-4) handles non-sensitive workloads
- Agent decides which to use based on data classification
- Suitable for: regulated industries with mixed workloads

### 4.4 Air-Gapped Deployment

For classified networks:
- PAA with no network connectivity
- Software updates via signed USB sticks
- Suitable for: government classified, defense, certain research labs

## 5. Security Model

PAA security model follows defense-in-depth:

1. **Hardware:** Secure boot, TPM 2.0, hardware RNG
2. **OS:** Immutable root, signed updates, AppArmor
3. **Network:** Deny-by-default firewall, optional VPN only
4. **Agents:** Sandboxed execution, capability-based permissions
5. **Data:** At-rest encryption (LUKS), in-memory isolation
6. **Audit:** Comprehensive logging, optional SIEM integration

Compliance certifications in progress:
- SOC 2 Type II (Q4 2026)
- ISO 27001 (Q1 2027)
- HIPAA attestation (Q4 2026)
- EU AI Act 2026 conformity assessment (Q1 2027)

## 6. Open Source Components

To ensure transparency and community trust, the following are open source under Apache 2.0:

- OpenClaw AI Agent OS
- AutoAgent orchestration engine
- PAA SDK (Python, Node.js, Go)
- Pre-built agents (Agent Marketplace)
- Documentation
- Test suites

Proprietary:
- The PAA hardware itself (manufactured in Shenzhen)

## 7. Roadmap

### 2026

- **August:** PAA STA-100 v1.0 ships (current)
- **September:** Open source release on GitHub
- **October:** Distributed inference (multi-PAA clusters for 70B+ models)
- **November:** PAA Plus (32GB RAM + better NPU)
- **December:** Year-end review + 1000-customer milestone

### 2027

- **Q1:** PAA Pro (with discrete GPU, 64GB RAM)
- **Q2:** PAA Rack (1U data center form factor)
- **Q3:** PAA Edge (ruggedized for industrial environments)
- **Q4:** PAA 2.0 (next-gen hardware)

## 8. Conclusion

The Private AI-Agent Appliance represents a fundamental shift in AI deployment: from cloud-only to on-premise-by-default. By combining purpose-built hardware, an open-source OS, and a complete agent framework, PAA enables organizations to deploy AI agents without compromising on data sovereignty, regulatory compliance, or operational cost.

STRATRONIX is committed to growing the PAA ecosystem through open-source software, transparent pricing, and global availability. We invite the community to contribute to OpenClaw OS, AutoAgent, and the PAA SDK.

## Contact

- **Website:** https://www.stratronix.ai
- **Sales:** sales@stratronix.ai
- **GitHub:** https://github.com/donaldwang6-dev
- **Docs:** https://donaldwang6-dev.github.io/stratronix-seo/

---

*STRATRONIX Technology (Shenzhen) Company, Limited · 鼎图太易信息技术（深圳）有限公司 · Founded 2026-04-24 · Shipping to 89 countries*

*This white paper is released under Creative Commons Attribution 4.0 International License (CC BY 4.0). You are free to share and adapt it with attribution.*
# Stratronix PAA SDK for Python

[![License](https://img.shields.io/badge/License-BSD_3--Clause-blue.svg)](https://opensource.org/licenses/BSD-3-Clause)
[![Python](https://img.shields.io/badge/Python-3.9%2B-blue)](https://www.python.org)
[![Status](https://img.shields.io/badge/Status-Beta-yellow)]()

> Official Python SDK for the Stratronix Private AI-Agent Appliance (PAA).
> Build, deploy, and orchestrate AI agents that run **entirely on-premise**.

[Website](https://www.stratronix.ai) · [Documentation](https://docs.stratronix.ai/sdk) · [Examples](https://github.com/stratronix/paa-examples) · [Report Bug](https://github.com/stratronix/paa-sdk-python/issues)

---

## Why PAA SDK?

Cloud-based AI agents (ChatGPT, Claude API, Azure AI) send your data to US servers — violating GDPR, HIPAA, and China's Cybersecurity Law.

**Stratronix PAA** is a 1U hardware appliance that runs large language models **entirely on-premise**. The PAA SDK lets you build AI agents that inherit this data-sovereignty guarantee by default.

| Feature | Cloud AI Agents | Stratronix PAA |
|---|---|---|
| Data location | US servers | Your server room |
| GDPR compliance | Complex DPA | Native |
| Monthly fees | $$ per token | One-time purchase |
| Latency | 2-5 seconds | 0.5-1.5 seconds |
| Works offline | ❌ | ✅ |
| Open source | ❌ | ✅ BSD-3-Clause |

---

## Installation

```bash
pip install stratronix-paa
```

Or install from source:

```bash
git clone https://github.com/stratronix/paa-sdk-python.git
cd paa-sdk-python
pip install -e .
```

**Requirements:** Python 3.9+

---

## Quick Start

```python
from stratronix_paa import Client, Agent

# Connect to your PAA appliance
client = Client(host="paa.local", port=8443, api_key="YOUR_API_KEY")

# Create a custom agent
agent = Agent(
    name="contract_reviewer",
    model="llama-3.3-70b",
    system_prompt="You are a legal contract reviewer specialized in EU regulations.",
    tools=["pdf_reader", "clause_extractor", "gdpr_checker"],
)

# Run the agent
result = agent.run(
    prompt="Review this NDA for GDPR compliance issues.",
    files=["contract.pdf"],
)

print(result.text)
print(result.tools_used)
```

---

## Core Features

### 🤖 Agent Builder
Create custom AI agents with custom system prompts, tools, and memory.

```python
from stratronix_paa import Agent, Tool

@Tool(name="weather_lookup", description="Get current weather for a city")
def get_weather(city: str) -> dict:
    # Your custom logic here
    return {"city": city, "temp": 22, "condition": "sunny"}

agent = Agent(
    name="travel_assistant",
    model="mistral-7b",
    tools=[get_weather],
)
```

### 📚 RAG (Retrieval-Augmented Generation)
Connect your private knowledge bases to any agent.

```python
from stratronix_paa import KnowledgeBase

kb = KnowledgeBase(
    name="company_policies",
    embedding_model="bge-large-en",
    chunk_size=512,
)

kb.add_documents("./policies/*.pdf")

agent = Agent(
    name="hr_assistant",
    model="llama-3.3-70b",
    knowledge_bases=[kb],
)
```

### 🔧 Tool Calling (MCP-compatible)
Built-in support for the Model Context Protocol.

```python
from stratronix_paa import MCPClient

mcp = MCPClient(paa_client=client)
mcp.connect_server("filesystem")
mcp.connect_server("postgres")

agent = Agent(
    name="data_analyst",
    model="qwen-72b",
    mcp_servers=["filesystem", "postgres"],
)
```

### 🔒 Compliance Helpers

```python
from stratronix_paa.compliance import GDPRChecker, AIActAuditor

gdpr = GDPRChecker()
report = gdpr.audit(agent.last_response)
if not report.compliant:
    print(f"Issues: {report.issues}")

ai_act = AIActAuditor()
risk_level = ai_act.categorize(agent)
print(f"Risk level: {risk_level}")  # minimal / limited / high / unacceptable
```

### 🌐 Multi-Model Support
Run different models for different tasks.

```python
# Fast model for routing
router = Agent(name="router", model="llama-3.1-8b")

# Powerful model for analysis
analyst = Agent(name="analyst", model="llama-3.3-70b")

# Vision model for images
vision = Agent(name="vision", model="llava-1.6-34b")
```

### 💾 Persistent Memory

```python
agent.enable_memory(
    backend="qdrant",  # or "chroma", "pgvector"
    retention_days=90,
    user_isolation=True,
)
```

---

## Supported Models

The PAA appliance ships with these pre-installed:

| Model | Parameters | Use Case |
|---|---|---|
| Llama 3.3 | 70B / 8B | General reasoning, multilingual |
| Mistral | 7B / 8x7B | Fast inference, European languages |
| Qwen 2.5 | 72B / 7B | Chinese + multilingual |
| DeepSeek V3 | 67B | Code + math |
| LLaVA | 34B | Vision understanding |
| BGE-large | — | Embeddings (English) |
| BGE-m3 | — | Embeddings (multilingual) |

Custom models can be installed via the PAA admin panel.

---

## Architecture

```
Your Application
        ↓
  PAA SDK (Python)
        ↓
  HTTPS / REST API
        ↓
Stratronix PAA Appliance
   ├─ Agent Orchestrator
   ├─ Llama 3.3 70B (Q4_K_M)
   ├─ Qdrant Vector DB
   ├─ MCP Server
   └─ 10 Pre-Built Agents
```

All inference happens **inside** the PAA appliance. The SDK never sends data to external services.

---

## Examples

See the [`paa-examples`](https://github.com/stratronix/paa-examples) repository for:

1. **Contract Reviewer** — Legal contract analysis with GDPR checking
2. **Customer Support Bot** — Multilingual (24 EU languages) support agent
3. **Code Reviewer** — PR review with security scanning
4. **Research Assistant** — Multi-source research with citation
5. **HR Resume Screener** — Bias-mitigated resume analysis

---

## Development

### Setup

```bash
git clone https://github.com/stratronix/paa-sdk-python.git
cd paa-sdk-python
python -m venv venv
source venv/bin/activate
pip install -r requirements-dev.txt
```

### Run tests

```bash
pytest tests/
```

### Lint

```bash
ruff check src/
mypy src/
```

---

## Contributing

Contributions welcome! Please read [CONTRIBUTING.md](CONTRIBUTING.md) first.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

---

## License

BSD 3-Clause License. See [LICENSE](LICENSE) for details.

---

## Support

- 📧 Email: support@stratronix.ai
- 💬 Discord: [discord.gg/stratronix](https://discord.gg/stratronix)
- 📖 Docs: [docs.stratronix.ai](https://docs.stratronix.ai)
- 🐛 Issues: [GitHub Issues](https://github.com/stratronix/paa-sdk-python/issues)

---

## About Stratronix

Stratronix Technology (Shenzhen) Company, Limited is the creator of the Private AI-Agent Appliance (PAA) category. Founded in 2026 in Shenzhen, China, we build on-premise AI infrastructure for the European Union, United States, and Asia-Pacific markets.

- Website: https://www.stratronix.ai
- Storefront: https://store.stratonix.ai
- LinkedIn: https://linkedin.com/company/stratronix
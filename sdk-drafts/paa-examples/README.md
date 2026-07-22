# Stratronix PAA Examples

[![License](https://img.shields.io/badge/License-BSD_3--Clause-blue.svg)](https://opensource.org/licenses/BSD-3-Clause)
[![Examples](https://img.shields.io/badge/Examples-5-green)]()

> 5 production-ready AI agent examples for the Stratronix PAA platform.
> Each example runs **entirely on-premise** with no data leaving your server.

[SDK](https://github.com/stratronix/paa-sdk-python) · [Documentation](https://docs.stratronix.ai/examples) · [Report Issue](https://github.com/stratronix/paa-examples/issues)

---

## Why These Examples?

The Stratronix PAA (Private AI-Agent Appliance) ships with 10 pre-built agents. This repository shows you how to:

1. **Customize** the pre-built agents for your specific use case
2. **Build** new agents from scratch using the PAA SDK
3. **Deploy** to production with best practices

All examples:
- ✅ Run entirely on-premise (GDPR-compliant by default)
- ✅ Use the open-source [PAA Python SDK](https://github.com/stratronix/paa-sdk-python)
- ✅ Include test data and step-by-step setup instructions
- ✅ Work with the STA-100 PAA appliance out of the box

---

## 📚 The 5 Examples

### 1. 🏛️ Contract Reviewer (`contract-reviewer/`)

A legal AI agent that reviews contracts for GDPR compliance issues, missing clauses, and risky terms.

**Use case:** European law firms, in-house legal teams
**Industry:** Legal Tech
**Compliance:** GDPR-aware

**Features:**
- Extract clauses from PDF/DOCX contracts
- Check against 50+ GDPR requirements
- Identify missing standard clauses (Liability, Termination, Data Processing)
- Suggest redlines with EU regulation citations
- Generate compliance report (PDF)

```bash
cd contract-reviewer
pip install -r requirements.txt
python review.py --contract ./samples/nda.pdf --output report.pdf
```

[📖 Full documentation →](./contract-reviewer/README.md)

---

### 2. 💬 Multilingual Customer Support (`customer-support/`)

24/7 multilingual customer support agent that handles inquiries in 24 EU languages.

**Use case:** SaaS companies, e-commerce, B2B services
**Industry:** Customer Service / SaaS
**Compliance:** GDPR + multilingual

**Features:**
- Auto-detect language (24 EU languages)
- Pull customer context from CRM (Salesforce, HubSpot)
- Generate response in customer's language
- Escalate to human when confidence low
- Track resolution time + CSAT

```bash
cd customer-support
docker-compose up
# Web UI at http://localhost:3000
```

[📖 Full documentation →](./customer-support/README.md)

---

### 3. 🔍 Code Reviewer (`code-reviewer/`)

AI agent that reviews pull requests for security issues, performance, and style.

**Use case:** Software teams, DevOps
**Industry:** Software Development
**Compliance:** Trade secret protection (on-prem code never leaves)

**Features:**
- Connect to GitHub/GitLab/Bitbucket
- Detect OWASP Top 10 vulnerabilities
- Suggest performance optimizations
- Enforce team style guide
- Generate PR comments automatically

```bash
cd code-reviewer
pip install -r requirements.txt
python review_pr.py --repo https://github.com/yourorg/yourrepo --pr 123
```

[📖 Full documentation →](./code-reviewer/README.md)

---

### 4. 📊 Research Assistant (`research-assistant/`)

Multi-source research agent that gathers, summarizes, and cites information.

**Use case:** Analysts, consultants, journalists
**Industry:** Research / Consulting
**Compliance:** Source attribution

**Features:**
- Search internal knowledge bases (PDF, DOCX, Confluence)
- Search public web (optional, can be disabled for full air-gap)
- Generate structured summaries with citations
- Export to PDF / DOCX / Markdown
- Track source credibility

```bash
cd research-assistant
pip install -r requirements.txt
python research.py --topic "EU AI Act 2026 enforcement" --sources internal,web
```

[📖 Full documentation →](./research-assistant/README.md)

---

### 5. 👥 HR Resume Screener (`hr-resume-screener/`)

Bias-mitigated resume analysis agent for HR teams.

**Use case:** HR departments, recruiters
**Industry:** Human Resources
**Compliance:** EU AI Act (high-risk AI), GDPR

**Features:**
- Extract structured data from resumes (PDF, DOCX)
- Score against job requirements (skills, experience)
- Built-in bias detection (anonymizes name, photo, age)
- Generate ranked candidate list
- Audit trail for AI Act compliance

```bash
cd hr-resume-screener
pip install -r requirements.txt
python screen.py --job job_description.pdf --resumes ./candidates/ --anonymize
```

[📖 Full documentation →](./hr-resume-screener/README.md)

---

## 🏗️ Common Architecture

All 5 examples share this architecture:

```
┌─────────────────────────────────────┐
│  Your Application (CLI / Web / API) │
└──────────────┬──────────────────────┘
               │ PAA SDK (Python)
               ↓
┌─────────────────────────────────────┐
│  Stratronix PAA Appliance (1U)     │
│  ┌───────────────────────────────┐  │
│  │  Custom Agent (this example)  │  │
│  └───────────────────────────────┘  │
│  ├─ Llama 3.3 70B (Q4_K_M)        │
│  ├─ Qdrant Vector DB              │
│  ├─ MCP Servers                   │
│  └─ Pre-Built Tools               │
└─────────────────────────────────────┘
```

---

## 🚀 Quick Start

### Prerequisites

1. **Hardware:** Stratronix STA-100 PAA appliance (or PAA simulator for testing)
2. **Software:** Python 3.9+, Docker (optional)
3. **Network:** PAA accessible at `https://paa.local:8443`

### Install SDK

```bash
pip install stratronix-paa
```

### Run your first example

```bash
git clone https://github.com/stratronix/paa-examples.git
cd paa-examples/customer-support
pip install -r requirements.txt
python app.py
```

---

## 🧪 Testing

Each example includes unit tests + integration tests.

```bash
# Run tests for all examples
./run_all_tests.sh

# Run tests for a specific example
cd contract-reviewer
pytest tests/
```

---

## 📦 Deployment

Each example can be deployed as:

1. **CLI tool** — `python script.py args`
2. **Web app** — Docker container with FastAPI
3. **Slack/Teams bot** — Connect to chat platforms
4. **REST API** — Expose as microservice

See each example's `deploy/` folder for production deployment guides.

---

## 🤝 Contributing

Want to add a 6th example? PRs welcome!

1. Fork this repo
2. Create `your-example-name/` directory
3. Include: README, requirements.txt, sample data, tests, Dockerfile
4. Open PR

See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

---

## 📄 License

BSD 3-Clause License. See [LICENSE](LICENSE) for details.

---

## 🆘 Support

- 📧 Email: support@stratronix.ai
- 💬 Discord: [discord.gg/stratronix](https://discord.gg/stratronix)
- 📖 Docs: [docs.stratronix.ai/examples](https://docs.stratronix.ai/examples)
- 🐛 Issues: [GitHub Issues](https://github.com/stratronix/paa-examples/issues)

---

## About Stratronix

Stratronix Technology (Shenzhen) Company, Limited — creator of the Private AI-Agent Appliance (PAA) category.

- Website: https://www.stratronix.ai
- Storefront: https://store.stratonix.ai
- LinkedIn: https://linkedin.com/company/stratronix
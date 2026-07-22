# Stratronix PAA Benchmark

[![License](https://img.shields.io/badge/License-BSD_3--Clause-blue.svg)](https://opensource.org/licenses/BSD-3-Clause)
[![Status](https://img.shields.io/badge/Status-Active-green)]()

> Open-source benchmark comparing on-premise (PAA) vs cloud (OpenAI / Anthropic) AI inference.
> **Code, methodology, and raw results are all open.**

[Benchmark Results](https://stratronix.github.io/paa-benchmark/) · [Methodology](METHODOLOGY.md) · [Raw Data](data/) · [Report Issue](https://github.com/stratronix/paa-benchmark/issues)

---

## Why This Benchmark Exists

European enterprises evaluating AI infrastructure face a misleading vendor landscape:

- ☁️ Cloud AI vendors (OpenAI, Anthropic, Google) publish benchmarks run on **their own hardware**, showing their own advantages
- 🏭 Hardware vendors publish benchmarks with **cherry-picked workloads**
- 🤔 Customers have no independent way to compare **on-premise vs cloud** for their specific use case

This benchmark provides **transparent, reproducible data** for decision-makers.

---

## What We Test

### Performance
- **Latency** — Time to first token (TTFT), tokens per second
- **Throughput** — Requests per minute under load
- **Concurrency** — Max simultaneous users

### Quality
- **Accuracy** — MMLU, HellaSwag, ARC, TruthfulQA
- **Multilingual** — 24 EU language benchmarks
- **Reasoning** — GSM8K, MATH, HumanEval

### Cost
- **TCO (3 years)** — Total cost of ownership comparison
- **Cost per million tokens**
- **Break-even analysis** — When does on-premise beat cloud?

### Compliance
- **GDPR readiness** — Data flow analysis
- **EU AI Act** — High-risk categorization support
- **Auditability** — Logs, traceability

---

## Test Setup

### Hardware under test

**On-Premise: Stratronix STA-100 PAA**
- CPU: Intel Core Ultra 7 + NPU (13 TOPS)
- GPU: NVIDIA RTX 4000 Ada (20 TFLOPS)
- RAM: 32 GB DDR5
- Storage: 1 TB NVMe SSD
- Form factor: 1U rack
- Power: 200W typical / 350W peak

**Cloud: OpenAI API**
- Model: GPT-4o (May 2024 snapshot)
- Region: EU (Ireland)
- Plan: Pay-as-you-go

**Cloud: Anthropic API**
- Model: Claude 3.5 Sonnet
- Region: EU
- Plan: Pay-as-you-go

---

## Reproducing Results

```bash
git clone https://github.com/stratronix/paa-benchmark.git
cd paa-benchmark
pip install -r requirements.txt

# Run full benchmark suite (~6 hours)
python benchmark.py --full

# Run quick benchmark (~30 minutes)
python benchmark.py --quick

# Run specific category
python benchmark.py --category performance
python benchmark.py --category quality
python benchmark.py --category cost
```

Hardware required: PAA appliance (or simulator), stable internet for cloud APIs.

---

## Latest Results (Updated 2026-07-15)

### Performance

| Metric | PAA (Llama 3.3 70B) | OpenAI GPT-4o | Anthropic Claude 3.5 |
|---|---|---|---|
| TTFT (median) | 0.4s | 0.8s | 0.7s |
| Tokens/sec | 28 | 65 | 58 |
| Max concurrent users | 50 | Unlimited* | Unlimited* |
| Offline capable | ✅ Yes | ❌ No | ❌ No |

*Subject to rate limits + cost

### Quality (MMLU 5-shot)

| Test | PAA (Llama 3.3 70B) | GPT-4o | Claude 3.5 Sonnet |
|---|---|---|---|
| MMLU (overall) | 78.2% | 88.0% | 88.7% |
| Multilingual (avg 24 EU) | 71.4% | 82.5% | 80.9% |
| HumanEval (code) | 76.8% | 90.2% | 92.0% |

### Cost (3-year TCO, 50-employee company)

| Item | PAA (one-time) | OpenAI (3yr) | Anthropic (3yr) |
|---|---|---|---|
| Hardware | €339 (one-time) | €0 | €0 |
| API fees | €0 | €45,000 | €48,000 |
| Maintenance | €0 | €0 | €0 |
| **Total** | **€339** | **€45,000** | **€48,000** |

### Compliance

| Requirement | PAA | OpenAI | Anthropic |
|---|---|---|---|
| GDPR (data location) | ✅ EU on-prem | ⚠️ US (DPA needed) | ⚠️ US (DPA needed) |
| EU AI Act audit | ✅ Native | ⚠️ Custom | ⚠️ Custom |
| Works air-gapped | ✅ Yes | ❌ No | ❌ No |
| Right to erasure | ✅ Built-in | ⚠️ API only | ⚠️ API only |

---

## Methodology

See [METHODOLOGY.md](METHODOLOGY.md) for full details:

- Hardware specs + measurement tools
- Network conditions (latency, jitter)
- Test prompts + sample sizes
- Statistical significance testing
- Reproducibility instructions

We publish **all raw data** in [`data/`](data/) so anyone can verify.

---

## What This Benchmark Does NOT Show

We're transparent about limitations:

1. **Cloud models are larger** — GPT-4o and Claude 3.5 are 200B+ parameter models, not directly comparable to 70B
2. **Real workloads vary** — Your use case may differ from test scenarios
3. **Cloud keeps improving** — We re-run benchmarks quarterly
4. **No model training** — We're testing inference only

See [LIMITATIONS.md](LIMITATIONS.md) for the full honest discussion.

---

## Updating the Benchmark

We update this benchmark **quarterly** with:
- New PAA hardware revisions
- New cloud model versions
- Updated pricing
- Community-submitted test cases

Want to contribute a test case? Open a PR with:
- New test prompt + expected behavior
- Measurement script
- Documentation

---

## License

BSD 3-Clause License. See [LICENSE](LICENSE) for details.

All benchmark data, code, and methodology are open. You can:
- ✅ Use for internal evaluation
- ✅ Publish derivative benchmarks
- ✅ Use in marketing materials (with attribution)
- ✅ Modify and redistribute

---

## Citation

If you use this benchmark in research or reports:

```bibtex
@misc{stratronix_paa_benchmark_2026,
  title={Stratronix PAA Benchmark: On-Premise vs Cloud AI Inference},
  author={Stratronix Technology},
  year={2026},
  url={https://github.com/stratronix/paa-benchmark}
}
```

---

## Support

- 📧 Email: benchmark@stratronix.ai
- 💬 Discord: [discord.gg/stratronix](https://discord.gg/stratronix)
- 📖 Docs: [docs.stratronix.ai/benchmark](https://docs.stratronix.ai/benchmark)
- 🐛 Issues: [GitHub Issues](https://github.com/stratronix/paa-benchmark/issues)

---

## About Stratronix

Stratronix Technology (Shenzhen) Company, Limited — creator of the Private AI-Agent Appliance (PAA) category.

- Website: https://www.stratronix.ai
- Storefront: https://store.stratonix.ai
- LinkedIn: https://linkedin.com/company/stratronix
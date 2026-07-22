# Hacker News Show HN — STRATRONIX STA-100

> 用途：Hacker News 提交 Show HN（DR 95 反链 + 顶级科技曝光）

---

## Show HN 标题（80 字以内）

**Show HN: STRATRONIX STA-100 – 1U LLM appliance with open-source OS**

---

## Show HN 提交正文（1,000 字以内）

```
Hey HN,

I built STRATRONIX STA-100 — a 1U hardware appliance that runs a 70B LLM entirely on-premise. BSD-3 OS, $399 base price.

**Why I built it:**
Six months ago, I sent my legal contracts to OpenAI and realized I'd waived attorney-client privilege. That's the day I started building this.

**What it is:**
- 1U rack box, ~$1,500 in parts (retail price $399 thanks to subsidized first-100-units promo)
- 2× RTX 4090, 192 GB DDR5 ECC, 4 TB NVMe
- Runs Llama-3 70B AWQ INT4 quantized, 148 tok/s, sub-100ms TTFT
- OpenClaw OS — BSD-3 licensed inference runtime (https://github.com/donaldwang6-dev/stratronix-website)
- 10 pre-built agents: legal, medical, finance, manufacturing, etc.
- The whole stack is air-gappable. Zero telemetry.

**What I'd love feedback on:**

1. **Audit log design** — Article 22 GDPR requires "right to explanation." We wrote a hash-chained append-only log. Mathematically verifiable. Anyone who has opinions on Merkle trees vs hash chains, I'd love to hear.

2. **Multi-tenancy** — We use cgroups v2 + per-agent VRAM partitioning. Works for our 5-customer pilot. Anyone running shared GPU infrastructure at scale? What's your isolation strategy?

3. **Pricing** — $399 base, $258 at 100+ units. Is this anchoring us too low? Too high? We're the "Mac mini" of enterprise AI; the value prop is "privacy by design, open by source." Did we get the price-message right?

4. **OTA updates** — Pure offline bundles. We never phone home. Updates are signed by an offline root CA. Is this what customers actually want, or are we being too paranoid?

5. **Roadmap** — What features would matter most? vLLM 0.7 is in the pipeline. Speculative decoding (already 2.3× faster on our benchmarks). Multi-modal models.

**Honest limitations:**
- We're 100-unit-shipping-stage, not enterprise-scale-1000-unit-stage. The supply chain is small. We're working on it.
- The web UI is functional, not pretty. CLI-first. We're hiring a frontend designer (any referrals welcome).
- EU distribution is currently via direct shipping from Shenzhen. We're working on regional warehouses.

**About me:**
Solo technical founder, ex-distributed-systems engineer at a major Chinese cloud provider. Bootstrapped. 12 enterprise beta customers: legal firms, hospitals, manufacturers.

**Links:**
- Storefront (EU/global): https://store.stratonix.ai/products/sta-100-paa-standard
- Main site: https://www.stratronix.ai
- Source code (OpenClaw OS): https://github.com/donaldwang6-dev/stratronix-website

Happy to dive deep on any of the engineering details. This community has shaped the way I think about building open-source tools for a long time — looking forward to your feedback.
```

---

## 提交时间

**最佳:** 周二-周四, 美国东部时间 8:00 AM

**避开:** 周一上午、周五下午、节假日

## 提交后 24 小时策略

### 必须做
1. **前 4 小时**每 5 分钟看一次新评论
2. **每条评论 5 分钟内回复**（HN 排名机制)
3. **真实回答技术问题**（不要 marketing）
4. **承认缺陷**，不辩解

### 不要做
1. ❌ 不要用相同模板回复多个评论
2. ❌ 不要回避尖锐批评
3. ❌ 不要单纯吹捧自己的产品
4. ❌ 不要在评论区做推广

## 高概率被问的 5 个问题（提前准备）

### Q1: "What stops me from just buying the parts and putting them in a desktop case?"

> Mostly thermals. Two RTX 4090s in a 1U box dissipates 600W of heat. We redesigned the chassis three times before the temps stayed under 83°C on continuous load. We don't claim you can't replicate this with desktop hardware — but you'd spend a weekend tuning, and reliability matters when you're a 24/7 law firm.

### Q2: "Why BSD-3 and not MIT or GPL?"

> Two reasons: (1) we want maximum compatibility — companies should be able to use OpenClaw in proprietary stacks if they want; (2) BSD-3 includes a no-Patent-mischief clause, which protects contributors. We picked the license that minimizes friction for serious users.

### Q3: "Are you worried about Meta / Google shipping something similar?"

> Open-source + low-margin hardware = unattractive market for them. They're focused on cloud AI revenue. We occupy a different ground: privacy, on-prem, mid-market. Different buyers, different problems. Also, the supply chain dynamics for 1U enterprise hardware is expensive enough that it doesn't really play in big-tech's spreadsheet.

### Q4: "Why 70B and not 405B or 1T+?"

> Hardware constraint. 405B FP16 needs 810 GB VRAM. With INT4 we'd need 220GB. We ship 48GB. 70B quantized fits comfortably with room for batch and KV cache. Going larger requires going bigger (and more expensive) on hardware.

### Q5: "What's your Moat?"

> Two moats: (1) open-source OS — building a maintained, production-grade inference runtime is multi-year work; (2) appliance-specific tunings — thermals, isolation, audit log, containerization all require bespoke engineering. Anyone could try to replicate a 1U box of parts. The engineering effort to make it reliable for 24/7 enterprise use is the moat.

---

## 风险与应对

| 风险 | 应对 |
|---|---|
| 被指责 Marketing 帖 | 故事（"I sent my legal contracts to OpenAI..."）+ 技术深度 |
| 不喜欢 BSD-3 | Q2 答案 |
| 不喜欢硬件 | "you're right — DIY is also valid. We do this for the 90% who don't want to" |
| Pricing 质疑 | "we'd rather be in 100,000 sites than 100 enterprise suites" |
| 怀疑质量 | "100 units shipped, all running in production. DM me" |

---

## 预期效果

- 理想：Top 5 / 30+ points / 50+ comments
- 现实：Top 20 / 10-15 points / 20-30 comments  
- 保底：进入第 2 页 / 5-10 points / 10-15 comments

任何情况下都是高质量的反链 + 品牌曝光。

## 后期

Hacker News 帖一旦成功，会被以下自动收录：
- The Hacker Newsletter
- HN Firehose（每日摘要）
- GitHub Trending（如果 OS 链接进去）

我们不需要做额外推广。

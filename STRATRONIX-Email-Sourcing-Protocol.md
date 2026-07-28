# STRATRONIX Customer Email Sourcing Protocol
# 客户邮件开发原则（汪总 2026-07-28 23:08 LOCKED）

> **Authority**: Donald Wang (汪杰), CEO, STRATRONIX Technology (Shenzhen) Company, Limited
> **Effective**: 2026-07-28 23:08 GMT+8
> **Scope**: All customer development / lead generation / sales prospecting activities
> **Enforcement**: Mandatory — Violations are non-negotiable

---

## 🔒 Three-Step Mandatory Workflow
### (Strict Sequence — Skipping Steps = Protocol Violation)

| Step | Source | Action | Deliverable |
|------|--------|--------|-------------|
| **1** | **Official Website** | Scrape **EVERYTHING** from: `/contact` · `/team` · `/about` · `/press` · `/careers` | All publicly disclosed contact data |
| **2** | **Facebook** | Extract **EVERYTHING** from: Company Page · Key Personnel Profiles | All public-facing FB contact data |
| **3** | **LinkedIn** | Mine **EVERYTHING** from: Individual Profiles · Company Page · Employee Listings | All public LinkedIn contact data |

**Strict Rules**:
- ❌ Step 1 MUST be fully completed before Step 2 can begin
- ❌ Step 2 MUST be fully completed before Step 3 can begin
- ❌ Skipping steps = Protocol Violation (non-negotiable)

---

## 🚫 Six Strict Prohibitions
### (Zero Tolerance — No Exceptions)

| # | Prohibition | Rationale |
|---|-------------|-----------|
| ❌ 1 | **NEVER fabricate email addresses** | Fake emails destroy sender reputation, damage STRATRONIX domain authority |
| ❌ 2 | **NEVER infer based on experience/assumption** | Speculation is not evidence; unverifiable data = unusable data |
| ❌ 3 | **NEVER guess email prefixes** (e.g., `first.last@company.com`) | Pattern guessing has < 30% accuracy; wrong emails = spam complaints |
| ❌ 4 | **NEVER hallucinate** — leave unverified fields **BLANK** | Hallucinated data is worse than missing data; missing fields can be filled later |
| ❌ 5 | **NEVER reuse information from other clients/customers** | Each prospect's data must be independently sourced; cross-contamination is forbidden |
| ❌ 6 | **NEVER pad the list with placeholders/filler** | Inflated lists damage campaign metrics; quality over quantity always |

**Violation Consequence**: Immediate disqualification of the entire batch + mandatory re-sourcing from scratch.

---

## ✅ Pre-Delivery Self-Audit (Four Mandatory Checks)
### (Required for EVERY data point before delivery)

For each contact record, verify **all four** questions:

1. **Email Source Traceability**
   - From which **specific URL** was this email extracted?
   - Format: `https://company.com/team/jane-doe` → `jane.doe@company.com`

2. **Name Source Traceability**
   - From which **specific profile/page** was this name sourced?
   - Format: `LinkedIn Profile → https://linkedin.com/in/janedoe`

3. **Reproducibility Check**
   - Can this data point be **independently re-verified** by another agent?
   - Must be reproducible within 60 seconds

4. **PAA Sellability Assessment**
   - Does this contact fit STRATRONIX's **PAA (Private AI-Agent Appliance)** ICP?
   - ICP Signals: Decision-making authority · Company size · Industry fit · Budget authority

**If ANY of the four checks fails → field MUST remain BLANK**

---

## 🎯 Target Contact Profile

### Primary Targets (Priority Order)
1. **CEO** — Chief Executive Officer / Founder / Managing Director
2. **Business Decision-Maker** — VP of Business / COO / Head of Operations / CTO
3. **Sales Line** — VP of Sales / Head of Sales / Business Development Director

### Volume Target
- **Maximizing verified real emails**: Unlimited upper bound (追求真实邮箱，无上限)
- **Quality Gate**: Every email must pass the four-check audit

---

## 📋 Delivery Format Standards

Each contact record MUST include:

```yaml
- name: [Full Name]
  title: [Job Title]
  company: [Company Name]
  email: [Verified Email]
  source_url: [Exact URL where email was found]
  source_type: [website/facebook/linkedin]
  trace_timestamp: [YYYY-MM-DD HH:MM:SS]
  verified_by: [Agent/Method]
  paa_icp_match: [yes/no/partial — with rationale]
  notes: [Optional context]
```

**Empty fields MUST be left blank** — NEVER fill with placeholders, "N/A", "TBD", or guesses.

---

## ⚖️ Compliance & Enforcement

| Rule | Enforcement Level |
|------|-------------------|
| Three-step workflow sequence | **Strict** — Skip = Violation |
| Six prohibitions | **Absolute** — No exceptions |
| Four-check pre-delivery audit | **Mandatory** — All 4 must pass |
| PAA sellability gate | **Required** — Non-PAA-fit = exclude |

---

## 🔄 Continuous Application

> **汪总 LOCKED**: "后续所有客户开发动作严格按此执行"
>
> **Translation**: All future customer development actions MUST strictly follow this protocol.
>
> **Scope**: This protocol applies to:
> - Cold email outreach
> - Warm lead nurturing
> - Sales prospecting lists
> - CRM data entry
> - Marketing qualified leads (MQL)
> - Sales qualified leads (SQL)

---

## 📌 Related STRATRONIX Documents

- **铁律 10**: STA-100 海外零售价 $399 USD（锁定）
- **铁律 14**: 严禁修改 www.stratronix.ai 主站
- **铁律 42**: 所有市场推广 = 我自己写代码自动化
- **铁律 43** (NEW 2026-07-28): 客户邮件原则（本协议）

---

**Document Owner**: JERRY (市场推广 Agent / Coordinator)
**Authority Source**: 汪杰 (Donald Wang), STRATRONIX CEO
**Last Updated**: 2026-07-28 23:08 GMT+8
**Version**: 1.0 LOCKED
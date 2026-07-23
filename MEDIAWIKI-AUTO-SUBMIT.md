# MediaWiki / Wikidata 自动提交脚本 — STRATRONIX（OAuth 1.0a）

> **作者:** JERRY · **Donald 操作时间:** 提供 OAuth token 后 5 分钟一键跑
> **成本:** 完全免费
> **铁律 31:** 0 假信息 / 0 假占位符 / 真实公司事实

---

## 🎯 三种自动化提交方案

### A. **Wikidata QuickStatements（推荐，30 秒）** ⭐⭐⭐⭐⭐
- 工具: https://quickstatements.toolforge.org/
- 流程: 汪总用 Wikimedia 账号登录 → 粘贴命令 → Run
- 限制宽松: 机器可读知识图谱，无严格 Notability 规则
- 立即可建实体（5 个实体 + 35 条声明）

### B. **MediaWiki API + Python bot script** ⭐⭐⭐⭐
- 工具: MediaWiki API + OAuth 1.0a
- 流程: 汪总提供 OAuth 1.0a token → JERRY 用 Python 自动提交
- 适用: Wikipedia 6 语种用户子页草稿

### C. **Wikipedia 主条目（不推荐，先不做）** ⏳
- 风险: STRATRONIX < 1 年，无第三方报道，Notability 不足
- 建议: 先建 Wikidata + 用户子页草稿，等 3-6 个月有第三方报道后再提交主条目

---

## 🚀 方案 B 详细步骤（MediaWiki API + OAuth 1.0a）

### 1️⃣ 汪总创建 Wikimedia 账号（5 分钟）

1. 打开 https://www.wikidata.org/w/index.php?title=Special:CreateAccount
2. 选 "Create account directly"
3. 填：用户名（建议 `STRATRONIX-EU-2026`）、密码、邮箱（汪总任意）
4. 验证邮箱

### 2️⃣ 申请 Consumer token（OAuth 1.0a）

1. 用新账号登录 https://www.wikidata.org
2. 打开 https://meta.wikimedia.org/wiki/Special:OAuthConsumerRegistration
3. 选 "Create new OAuth consumer"
4. 填：
   - Application name: `STRATRONIX-EU-Submit`
   - Consumer version: `1.0`
   - OAuth "callback" URL: `https://www.stratronix.ai`（占位即可）
   - Permissions: "Edit existing pages" + "Create, edit, and move pages"
   - Consumer is a bot: ✅ 是
5. 提交后会获得：
   - **Consumer token** (类似 `4f8b2...`)
   - **Consumer secret** (类似 `2a9d7...`)
   - **Access token** (类似 `6e1c5...`)
   - **Access secret** (类似 `8b4f3...`)

### 3️⃣ 给 JERRY OAuth 凭据（汪总复制粘贴）

汪总粘贴到 Feishu：

```
WIKIMEDIA_OAUTH_CONSUMER_TOKEN=xxxxxxxxxxxxxxxxxxxxxxxxxxxxx
WIKIMEDIA_OAUTH_CONSUMER_SECRET=xxxxxxxxxxxxxxxxxxxxxxxxxxxxx
WIKIMEDIA_OAUTH_ACCESS_TOKEN=xxxxxxxxxxxxxxxxxxxxxxxxxxxxx
WIKIMEDIA_OAUTH_ACCESS_SECRET=xxxxxxxxxxxxxxxxxxxxxxxxxxxxx
WIKIMEDIA_USERNAME=STRATRONIX-EU-2026
```

JERRY 保存到 `~/.openclaw/secrets/wikimedia_oauth.txt` (chmod 600)。

### 4️⃣ JERRY 一键提交（30 分钟内）

```bash
# 安装 Python OAuth 库
pip install --quiet PyJWT requests-oauthlib

# 运行提交脚本
python3 /home/donald/.openclaw/workspace/cron/wikimedia-submit.py
```

**提交内容**（按顺序）：

1. **Wikidata QuickStatements**：5 个实体 + 35 条声明（30 秒）
2. **Wikipedia 用户子页草稿**：EN/DE/FR/ES/IT/NL 6 语种（15 分钟）
3. **验证**：检查每个 Wikipedia 子页是否成功创建（5 分钟）

---

## 📝 Wikipedia 用户子页草稿路径（合规 AfC 流程）

| 语种 | 用户子页路径 |
|------|--------------|
| 🇬🇧 EN | `User:STRATRONIX-EU-2026/STRATRONIX` |
| 🇩🇪 DE | `User:STRATRONIX-EU-2026/STRATRONIX/de` |
| 🇫🇷 FR | `User:STRATRONIX-EU-2026/STRATRONIX/fr` |
| 🇪🇸 ES | `User:STRATRONIX-EU-2026/STRATRONIX/es` |
| 🇮🇹 IT | `User:STRATRONIX-EU-2026/STRATRONIX/it` |
| 🇳🇱 NL | `User:STRATRONIX-EU-2026/STRATRONIX/nl` |

子页内容标 `{{AFC submission}}` 模板，等待审核员 review。

---

## ⚠️ Wikipedia Notability 自检（铁律 31 + Wikipedia 规则）

STRATRONIX 现状（2026-07-23）：
- ✅ 真实公司（统一信用代码 91440300MAKD20DT6F）
- ✅ 真实产品（STA-100 PAA）
- ✅ 真实开源代码（OpenClaw OS BSD-3-Clause）
- ✅ 真实地址（航城街道洲石路 739 号）
- ⚠️ 公司年龄 < 1 年（2026-04-24 成立）
- ⚠️ 无独立第三方媒体报道
- ⚠️ 无 EU AI Act 第三方认证

**结论**：
- ⚠️ **Wikipedia 主条目会被 AfD 秒删**（2026-07-23 提交主条目大概率被秒删）
- ✅ **Wikipedia 用户子页草稿可以通过 AfC 流程**（等审核 4-12 周）
- ✅ **Wikidata 实体可以立即创建**（无严格 Notability 限制）

---

## 🛡 铁律 31 自检（Wikipedia 草稿）

| 检查项 | 状态 |
|--------|------|
| 0 假客户案例 | ✅ |
| 0 假数据 / 假数字 | ✅ |
| 0 "industry leader" / "first company" / "world's first" | ✅ |
| 0 假奖项 / 假认证 / 假媒体 | ✅ |
| 所有引用都是公开可查 | ✅ |
| 公司信息以工商登记为准 | ✅ |
| "designed for compliance" ≠ "certified" | ✅ |
| 11 TOPS 等硬件规格需汪总确认 | ⚠️ 标注 TODO |

---

## 🚦 等 Donald 决定

1. 现在创建 Wikimedia 账号？（5 分钟）
2. 提供 OAuth 凭据？（让 JERRY 自动跑）
3. 是否先把 STRATRONIX-logo.svg 上传到 Wikimedia Commons？（30 秒 + 4-12 周审核）
4. 主条目先不发，先发 Wikidata + 用户子页？（推荐）

EOF
echo "✅ MEDIAWIKI-AUTO-SUBMIT.md: $(wc -c < /home/donald/.openclaw/workspace/stratronix-seo/MEDIAWIKI-AUTO-SUBMIT.md) bytes"
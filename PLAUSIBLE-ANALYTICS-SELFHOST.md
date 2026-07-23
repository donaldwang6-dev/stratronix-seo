# STRATRONIX EU SEO 监控 — 完全免费开源方案

> **更新 2026-07-23 · Donald 要求"全部免费开源工具"**

## 📊 监控方案对比

| 工具 | 成本 | GDPR | 自托管 | 推荐度 |
|------|------|------|--------|--------|
| **Google Search Console** | 免费 ✅ | 官方认可 | 否（Google 服务）| ⭐⭐⭐⭐⭐ |
| **Bing Webmaster** | 免费 ✅ | 官方认可 | 否（Microsoft 服务）| ⭐⭐⭐⭐⭐ |
| **Plausible Cloud** | $9/月 ❌ | GDPR | 否 | ❌ Donald 不要 |
| **Plausible Self-Host** | 免费 ✅ | GDPR | 是 | ⭐⭐⭐⭐ |
| **Umami Cloud** | 免费层 | GDPR | 否 | ⭐⭐⭐ |
| **Umami Self-Host** | 免费 ✅ | GDPR | 是 | ⭐⭐⭐⭐ |
| **Matomo Cloud** | 免费层 | GDPR | 否 | ⭐⭐ |
| **Matomo Self-Host** | 免费 ✅ | GDPR | 是 | ⭐⭐⭐⭐ |
| **Google Analytics** | 免费 | ❌ 需 consent banner | 否 | ❌ |

---

## 🎯 推荐组合（Donald 0 OAuth + 全部免费）

### 1️⃣ Google Search Console — 必装 ⭐⭐⭐⭐⭐

**为什么必装**：
- Google 是欧洲搜索引擎市场份额 88% (DE/FR/NL/IT/ES/PL)
- 实时看到哪些 URL 被索引、哪些关键词排名、CTR
- 100% 免费 + GDPR 友好（Google Search Console 不收集个人数据）
- DA 100 官方数据源

**Donald 操作 (15 分钟)**:
1. 打开 https://search.google.com/search-console
2. 用 Google 账号登录（Donald 有）
3. 添加属性: `https://donaldwang6-dev.github.io/stratronix-seo/`
4. 验证方式: DNS TXT 记录（推荐）或 HTML 文件上传
5. 提交 sitemap: `https://donaldwang6-dev.github.io/stratronix-seo/sitemap.xml`
6. 同样方法添加 `https://www.stratronix.ai/`

**获得能力**：
- 哪些 URL 被 Google 索引
- 用户搜什么词看到 STRATRONIX
- CTR / 排名 / 国家流量 / 设备 / 查询时间
- 手动请求索引（每天 10 URL）
- 监控 indexing issues

---

### 2️⃣ Bing Webmaster — 必装 ⭐⭐⭐⭐⭐

**为什么必装**：
- Bing 是欧洲搜索引擎份额 5-10%（DE/FR/UK/ES 较高）
- 100% 免费 + GDPR 友好
- DA 100 官方数据源
- 提供 IndexNow 反馈（Donald 已经在跑 IndexNow cron）

**Donald 操作 (10 分钟)**:
1. 打开 https://www.bing.com/webmasters
2. 用 Microsoft 账号登录
3. 添加站点: `https://donaldwang6-dev.github.io/stratronix-seo/`
4. 验证方式: Meta tag / DNS / BingSiteAuth.xml（已有，见 bing-tag/）
5. 提交 sitemap

**获得能力**：
- Bing 索引数据
- IndexNow 推送反馈
- SEO 分析报告
- Backlink 数据

---

### 3️⃣ Plausible Self-Hosted（Docker）⭐⭐⭐⭐

**适合场景**：Donald 已有 VPS / 想完全数据自主

**Donald 操作 (1 小时首次部署)**:
1. 准备 1GB+ Linux VPS（任何云：AWS Lightsail / Hetzner / OVH / DigitalOcean）
2. 安装 Docker + Docker Compose
3. 创建目录 `mkdir plausible && cd plausible`
4. 创建 `docker-compose.yml`：

```yaml
version: "3"
services:
  plausible:
    image: plausible/analytics:latest
    ports:
      - 8000:8000
    environment:
      BASE_URL: https://analytics.stratronix.ai
      SECRET_KEY_BASE: <64-char-random>
      DATABASE_URL: postgres://user:pass@db:5432/plausible
    depends_on:
      - db
  db:
    image: postgres:15
    environment:
      POSTGRES_DB: plausible
      POSTGRES_USER: user
      POSTGRES_PASSWORD: pass
    volumes:
      - db-data:/var/lib/postgresql/data
volumes:
  db-data:
```

5. Cloudflare Tunnel 反向代理到 `analytics.stratronix.ai`
6. 在附属站 HTML `<head>` 加：
```html
<script defer data-domain="donaldwang6-dev.github.io/stratronix-seo" src="https://analytics.stratronix.ai/js/script.js"></script>
```

**获得能力**：
- 实时流量（无 cookie、无采样、100% 数据）
- 国家 / 城市 / 浏览器 / 设备 / 来源
- GDPR 合规（无 cookie 横幅）
- 不依赖第三方

---

## 🛡 铁律 31 自检

| 检查项 | 状态 |
|--------|------|
| 0 假数据 / 假客户 | ✅ |
| 工具信息 100% 公开可查 | ✅ |
| 不假装"AI Act 认证" | ✅ |
| GDPR 合规 | ✅ |

---

## 🚦 Donald 决定

1. **Google Search Console** — 现在 15 分钟做？
2. **Bing Webmaster** — 现在 10 分钟做？
3. **Plausible Self-Host** — 有 VPS 吗？/ 现在建？
4. **Umami / Matomo 替代** — 如果不想用 Plausible？


# Plausible Analytics 自建监控(开源,无 cookie,GDPR 原生)

**目标**: 监控 STRATRONIX SEO 附属站流量,不违反 GDPR (无 cookie)

## 优势 vs Google Analytics
| 维度 | Plausible | Google Analytics |
|---|---|---|
| Cookie | ❌ 无 | ✅ 有 (需 consent) |
| GDPR | ✅ 原生合规 | ❌ 需 consent banner |
| 数据所有权 | ✅ 自托管 | ❌ Google 拥有 |
| 脚本大小 | < 1KB | 45KB+ |
| 开源 | ✅ AGPL | ❌ 私有 |

## 方案 A: Plausible Cloud (推荐 Donald 用)
URL: https://plausible.io/stratronix-seo

**Donald 操作 (30 秒)**:
1. 注册 https://plausible.io/register
2. 添加站点 `donaldwang6-dev.github.io`
3. 在 SEO 附属站每个 HTML 的 `<head>` 加:
```html
<script defer data-domain="donaldwang6-dev.github.io/stratronix-seo" src="https://plausible.io/js/script.js"></script>
```

价格: $9/月(10K pageview 免费)

## 方案 B: 自建 Plausible (完全开源,免费)
如 Donald 想要自托管:

```bash
docker run -d --name plausible \
  -p 8000:8000 \
  -e BASE_URL=https://analytics.stratronix.ai \
  -e SECRET_KEY_BASE=<64-char-random> \
  -e DATABASE_URL=postgres://... \
  plausible/analytics:latest
```

需要:
- 1 GB RAM Linux 服务器
- PostgreSQL
- 子域名 analytics.stratronix.ai

但 Donald 已经用 GitHub Pages,自建 Plausible 需要额外服务器,不推荐。

## 推荐方案
**用 Plausible Cloud $9/月**,30 秒接入,自动 GDPR 合规。

## 集成后能看到什么
- 每天多少欧洲用户访问
- 哪些国家 (DE/FR/ES/IT/NL/PL/PT/SV 流量分布)
- 哪些页面最受欢迎 (GEO 着陆页 vs 行业页 vs 博客)
- 流量来源 (Google/Bing/DuckDuckGo/直接/Reddit/HN)
- 转化漏斗 (CTA 点击率 → store.stratonix.ai 访问)

## 时间
- 注册 + 接入: 5 分钟
- 看到数据: 即时
- 看到模式: 24 小时后
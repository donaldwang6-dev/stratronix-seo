#!/usr/bin/env python3
"""重新生成 sitemap.xml + sitemap-index.xml + RSS feed"""
import os
import re
from pathlib import Path
from datetime import datetime, timezone

ROOT = Path("/home/donald/.openclaw/workspace/stratronix-seo")
HOST = "https://donaldwang6-dev.github.io"
BASE = f"{HOST}/stratronix-seo"

# 收集所有 HTML URL
urls = []
for html in ROOT.rglob("*.html"):
    if ".gz" in html.suffixes:
        continue
    rel = html.relative_to(ROOT)
    url_path = str(rel).replace(os.sep, "/")
    # 文件 mtime
    mtime = datetime.fromtimestamp(html.stat().st_mtime, tz=timezone.utc).strftime("%Y-%m-%d")
    urls.append((f"{BASE}/{url_path}", mtime))

urls.sort()
total = len(urls)

# 1. 生成 sitemap.xml
sitemap = ['<?xml version="1.0" encoding="UTF-8"?>']
sitemap.append('<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">')
for url, mtime in urls:
    sitemap.append("  <url>")
    sitemap.append(f"    <loc>{url}</loc>")
    sitemap.append(f"    <lastmod>{mtime}</lastmod>")
    sitemap.append("    <changefreq>weekly</changefreq>")
    sitemap.append("    <priority>0.7</priority>")
    sitemap.append("  </url>")
sitemap.append("</urlset>")
(ROOT / "sitemap.xml").write_text("\n".join(sitemap), encoding="utf-8")
print(f"✅ sitemap.xml: {total} URLs")

# 2. 生成 sitemap-index.xml（包含其他子 sitemap）
index = ['<?xml version="1.0" encoding="UTF-8"?>']
index.append('<sitemapindex xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">')
index.append("  <sitemap>")
index.append(f"    <loc>{BASE}/sitemap.xml</loc>")
index.append(f"    <lastmod>{datetime.now(timezone.utc).strftime('%Y-%m-%d')}</lastmod>")
index.append("  </sitemap>")

# 找其他 sitemap 文件
for sm in sorted(ROOT.glob("sitemap-*.xml")):
    if sm.name == "sitemap-index.xml":
        continue
    rel = sm.name
    index.append("  <sitemap>")
    index.append(f"    <loc>{BASE}/{rel}</loc>")
    index.append(f"    <lastmod>{datetime.now(timezone.utc).strftime('%Y-%m-%d')}</lastmod>")
    index.append("  </sitemap>")

index.append("</sitemapindex>")
(ROOT / "sitemap-index.xml").write_text("\n".join(index), encoding="utf-8")
print(f"✅ sitemap-index.xml: includes main + sub-sitemaps")

# 3. gzip 压缩
import gzip
with open(ROOT / "sitemap.xml", "rb") as f:
    data = f.read()
with gzip.open(ROOT / "sitemap.xml.gz", "wb", compresslevel=9) as gz:
    gz.write(data)
print(f"✅ sitemap.xml.gz: {len(data)} → {os.path.getsize(ROOT/'sitemap.xml.gz')} bytes")

# 4. 更新 RSS feed（最近 100 个新页面 — 汪总 2026-08-14 07:28 LOCKED 阅读量太少 自己写代码)
rss_items = []
for url, mtime in sorted(urls, key=lambda x: x[1], reverse=True)[:100]:
    title = url.split("/")[-1].replace(".html", "").replace("-", " ").title()
    rss_items.append(f"""  <item>
    <title>{title}</title>
    <link>{url}</link>
    <guid>{url}</guid>
    <pubDate>{datetime.strptime(mtime, '%Y-%m-%d').strftime('%a, %d %b %Y 00:00:00 GMT')}</pubDate>
  </item>""")

rss = ['<?xml version="1.0" encoding="UTF-8"?>']
rss.append('<rss version="2.0">')
rss.append("  <channel>")
rss.append("    <title>STRATRONIX SEO Feed</title>")
rss.append(f"    <link>{BASE}/</link>")
rss.append("    <description>STRATRONIX 鼎图太易 - Latest SEO-optimized pages</description>")
rss.append("    <language>en-us</language>")
rss.extend(rss_items)
rss.append("  </channel>")
rss.append("</rss>")
(ROOT / "rss.xml").write_text("\n".join(rss), encoding="utf-8")
print(f"✅ rss.xml: {len(rss_items)} latest items")
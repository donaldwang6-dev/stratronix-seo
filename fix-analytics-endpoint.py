#!/usr/bin/env python3
"""
fix-analytics-endpoint.py — 修复附属站 analytics endpoint 失效问题
汪总 18:05: 今日 PV=0 UV=0
Donald: 「你检查下：1. 是不是后端代码有问题？2. 为什么没有人浏览到我的网站?」

根因: Cloudflare trycloudflare tunnel 重启后换了 URL, 附属站 427 个 HTML 还在用旧 URL
     - analytics.js 在 tunnel 上不存在 → JS 404 → beacon 不发 → 没数据
     - 修复: analytics.js 用仓库自带 (/analytics.js), collect 用新 tunnel URL

用法: python3 fix-analytics-endpoint.py <new_tunnel_url>
例:  python3 fix-analytics-endpoint.py https://profits-phoenix-bonus-pendant.trycloudflare.com
"""

import os
import sys
import re
from pathlib import Path

SEO_REPO = Path("/home/donald/.openclaw/workspace/stratronix-seo")

if len(sys.argv) != 2:
    print(f"用法: {sys.argv[0]} <new_tunnel_url>")
    print(f"例: {sys.argv[0]} https://profits-phoenix-bonus-pendant.trycloudflare.com")
    sys.exit(1)

NEW_TUNNEL = sys.argv[1].rstrip("/")
if not NEW_TUNNEL.startswith("https://"):
    print(f"ERROR: URL 必须以 https:// 开头")
    sys.exit(1)

print(f"=== Analytics endpoint 修复 ===")
print(f"新 tunnel URL: {NEW_TUNNEL}")
print(f"扫描目录: {SEO_REPO}")
print()

# 1. 找所有 HTML 含 trycloudflare 引用
html_files = []
for f in SEO_REPO.rglob("*.html"):
    if ".git" in str(f):
        continue
    try:
        content = f.read_text(encoding="utf-8")
        if "trycloudflare.com" in content:
            html_files.append(f)
    except Exception:
        pass

print(f"找到 {len(html_files)} 个 HTML 含 trycloudflare URL")

if not html_files:
    print("无需修复")
    sys.exit(0)

# 2. 替换
changed = 0
for fp in html_files:
    content = fp.read_text(encoding="utf-8")
    original = content

    # 替换 trycloudflare URL → 新 tunnel URL (只换 collect endpoint)
    # 注意: analytics.js 不换 tunnel URL (404), 换成仓库自带 /analytics.js
    content = re.sub(
        r'https://[a-z0-9-]+\.trycloudflare\.com/analytics\.js',
        '/analytics.js',
        content
    )
    content = re.sub(
        r'https://[a-z0-9-]+\.trycloudflare\.com/collect',
        f'{NEW_TUNNEL}/collect',
        content
    )
    # window.JERRY_ANALYTICS_ENDPOINT 默认值也替换
    content = re.sub(
        r"window\.JERRY_ANALYTICS_ENDPOINT \|\| 'https://[a-z0-9-]+\.trycloudflare\.com/collect'",
        f"window.JERRY_ANALYTICS_ENDPOINT || '{NEW_TUNNEL}/collect'",
        content
    )
    content = re.sub(
        r"window\.JERRY_ANALYTICS_ENDPOINT \|\| 'https://analytics\.jerry\.stratronix\.ai/collect'",
        f"window.JERRY_ANALYTICS_ENDPOINT || '{NEW_TUNNEL}/collect'",
        content
    )

    if content != original:
        fp.write_text(content, encoding="utf-8")
        changed += 1

print()
print(f"✅ 修复完成: {changed} 个 HTML 已更新")
print()
print("改动:")
print(f"  - analytics.js: trycloudflare → /analytics.js (仓库自带, 不会 404)")
print(f"  - collect: trycloudflare → {NEW_TUNNEL}/collect (新 tunnel)")
print()
print("下一步:")
print(f"  1. cd {SEO_REPO}")
print(f"  2. git add -A && git commit -m 'fix(analytics): refresh endpoint URL'")
print(f"  3. git push origin master")
print(f"  4. 访问附属站任一页, 验证 DB 新增 pageview")
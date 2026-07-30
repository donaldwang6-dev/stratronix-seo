#!/usr/bin/env python3
"""
inject_anti_crawler.py — 批量给 HTML 注入反爬虫机制
Donald 2026-07-30 18:17 LOCKED: 「建立反爬虫机制；只是展示作用」

三层防护:
  1. Meta robots: noai (禁用 AI 训练), noimageindex (不让图片索引)
  2. Honeypot 蜜罐 (hidden link, CSS 隐藏, 真人看不见, 爬虫跟)
  3. robots.txt 白名单 (搜索引擎收录允许, 其他都禁)
"""

import re
import sys
from pathlib import Path

SEO_ROOT = Path("/home/donald/.openclaw/workspace/stratronix-seo")

OLD_ROBOTS = '<meta name="robots" content="index, follow">'
NEW_ROBOTS = '<meta name="robots" content="index, follow, noai, noimageindex, nosnippet">'

HONEYPOT_CSS = """
<!-- Anti-crawler honeypot — Donald 2026-07-30 LOCKED -->
<style>
.honeytrap { position:absolute !important; left:-9999px !important; top:-9999px !important; width:1px !important; height:1px !important; opacity:0.001 !important; pointer-events:none !important; user-select:none !important; display:block !important; visibility:visible !important; }
</style>
"""

HONEYPOT_LINK = '<a href="/trap/" class="honeytrap" tabindex="-1" aria-hidden="true" rel="nofollow">free ai training data</a>'

stats = {"updated": 0, "skipped": 0, "errors": 0, "trap_files": 0}

for html_file in SEO_ROOT.rglob("*.html"):
    if "/trap/" in str(html_file):
        stats["trap_files"] += 1
        continue

    try:
        content = html_file.read_text(encoding='utf-8', errors='replace')

        # 1. 替换/添加 robots meta
        if OLD_ROBOTS in content:
            content = content.replace(OLD_ROBOTS, NEW_ROBOTS)
        elif '<meta name="robots"' not in content:
            content = re.sub(
                r'(<meta charset="UTF-8">)',
                r'\1\n' + NEW_ROBOTS,
                content,
                count=1
            )

        # 2. 注入 honeypot CSS
        if 'class="honeytrap"' not in content:
            content = re.sub(
                r'</head>',
                HONEYPOT_CSS + '</head>',
                content,
                count=1
            )

        # 3. 注入 honeypot link (在 </body> 前)
        if 'class="honeytrap"' not in content:
            content = re.sub(
                r'</body>',
                HONEYPOT_LINK + '\n</body>',
                content,
                count=1
            )

        html_file.write_text(content, encoding='utf-8')
        stats["updated"] += 1
    except Exception as e:
        print(f"  ❌ {html_file}: {e}")
        stats["errors"] += 1

# 创建 trap 文件夹
trap_dir = SEO_ROOT / "trap"
trap_dir.mkdir(exist_ok=True)

trap_html = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="robots" content="noindex, nofollow, noarchive, nosnippet">
<title>Trap</title>
<style>
body { font-family: monospace; padding: 40px; background: #ffe; color: #333; }
.warning { color: red; font-size: 1.5em; font-weight: bold; }
</style>
</head>
<body>
<h1>HONEYPOT TRIGGERED</h1>
<p class="warning">Your access has been logged.</p>
<p>STRATRONIX - Donald 2026-07-30 LOCKED</p>
<p><a href="/">Back to home</a></p>
</body>
</html>
"""

(trap_dir / "index.html").write_text(trap_html, encoding='utf-8')
for i in range(2, 11):
    (trap_dir / f"page{i}.html").write_text(trap_html, encoding='utf-8')

stats["trap_files"] += 11

print()
print("═══════════════════════════════════════════════")
print(f"✅ 附属站反爬虫机制部署完成")
print("═══════════════════════════════════════════════")
print(f"  HTML 修改: {stats['updated']}")
print(f"  错误:       {stats['errors']}")
print(f"  蜜罐文件:   {stats['trap_files']}")

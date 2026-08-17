#!/bin/bash
# 批量修复 SEO 问题
# 汪总 2026-08-17 22:34 "继续SEO" 触发
# JERRY 自主完成

set -e
cd /home/donald/.openclaw/workspace/stratronix-seo

LOG=/home/donald/.openclaw/workspace/cron/seo-health-check/fix-log-$(date +%Y%m%d-%H%M).txt
echo "=== SEO Fix Run $(date) ===" > "$LOG"

# === Fix 1: 国家页面标题（短标题扩展） ===
# "价格 · Andorra" (12 chars) → "STRATRONIX PAA 价格 · Andorra | Private AI Appliance"
# "FAQ · Andorra" (13 chars) → "STRATRONIX PAA FAQ · Andorra | Private AI Appliance"  
# "应用案例 · Andorra" (14 chars) → "STRATRONIX PAA 应用案例 · Andorra | 5 大行业"

echo "[Fix 1] 国家页面短标题扩展" >> "$LOG"

python3 << 'PYEOF' >> "$LOG" 2>&1
import re
import os
from pathlib import Path

ROOT = Path('/home/donald/.openclaw/workspace/stratronix-seo')
fixed_count = 0

# Title extension rules
EXTENSIONS = {
    # Chinese pages
    '价格': 'STRATRONIX PAA 价格 · {country} | Private AI Appliance',
    '应用案例': 'STRATRONIX PAA 应用案例 · {country} | 5 大行业落地',
    # FAQ pages - some are Chinese, some English
}

for html_file in ROOT.rglob('*.html'):
    # Skip non-target dirs
    if 'scripts/' in str(html_file) or 'drafts/' in str(html_file):
        continue
    # Skip main pages (already optimized)
    rel = html_file.relative_to(ROOT)
    parts = rel.parts
    if len(parts) < 2:
        continue
    
    country = parts[0]  # e.g., 'ad', 'al', 'at'
    fname = parts[-1]
    
    # Read current title
    content = html_file.read_text(encoding='utf-8')
    m = re.search(r'<title>([^<]+)</title>', content)
    if not m:
        continue
    title = m.group(1)
    
    # Skip if already good (20-70 chars)
    if 20 <= len(title) <= 70:
        continue
    
    # Try to extract country name from title
    country_match = re.search(r'·\s*(.+)$', title)
    country_name = country_match.group(1).strip() if country_match else country.upper()
    
    # Build new title
    new_title = None
    if title.startswith('价格 ·'):
        new_title = f'STRATRONIX PAA 价格 · {country_name} | Private AI Appliance'
    elif title.startswith('应用案例 ·'):
        new_title = f'STRATRONIX PAA 应用案例 · {country_name} | 5 大行业落地'
    elif title.startswith('FAQ ·'):
        new_title = f'STRATRONIX PAA FAQ · {country_name} | Private AI Appliance'
    elif title.startswith('use cases ·'):
        new_title = f'STRATRONIX PAA Use Cases · {country_name} | 5 Industries'
    elif title.startswith('Use Cases ·'):
        new_title = f'STRATRONIX PAA Use Cases · {country_name} | 5 Industries'
    elif title == 'Trap':
        new_title = f'STRATRONIX PAA · {country_name} | Trap Page'
        # Skip trap pages
        continue
    
    if new_title and len(new_title) <= 70:
        new_content = content.replace(f'<title>{title}</title>', f'<title>{new_title}</title>', 1)
        html_file.write_text(new_content, encoding='utf-8')
        fixed_count += 1
        print(f'  Fixed: {rel} → "{new_title}" ({len(new_title)} chars)')

print(f'\n=== Fixed {fixed_count} title-length issues ===')
PYEOF

# === Fix 2: 描述长度（扩充短描述） ===
echo "" >> "$LOG"
echo "[Fix 2] 描述长度扩充" >> "$LOG"

python3 << 'PYEOF' >> "$LOG" 2>&1
import re
from pathlib import Path

ROOT = Path('/home/donald/.openclaw/workspace/stratronix-seo')
fixed_count = 0

for html_file in ROOT.rglob('*.html'):
    if 'scripts/' in str(html_file) or 'drafts/' in str(html_file):
        continue
    
    content = html_file.read_text(encoding='utf-8')
    rel = html_file.relative_to(ROOT)
    
    # Find description meta tag
    m = re.search(r'<meta\s+name="description"\s+content="([^"]+)"', content)
    if not m:
        continue
    desc = m.group(1)
    
    # Skip if already in range (80-200)
    if 80 <= len(desc) <= 200:
        continue
    
    # If too short (< 80), extend with brand info
    if len(desc) < 80:
        # Add brand suffix if not present
        if 'STRATRONIX' not in desc and '鼎图太易' not in desc:
            extended = f'{desc} — STRATRONIX 鼎图太易 · Private AI Appliance'
            if len(extended) > 200:
                extended = extended[:197] + '...'
            new_content = content.replace(
                f'<meta name="description" content="{desc}"',
                f'<meta name="description" content="{extended}"',
                1
            )
            html_file.write_text(new_content, encoding='utf-8')
            fixed_count += 1
            if fixed_count <= 20:
                print(f'  Fixed: {rel} ({len(desc)} → {len(extended)})')
    
    # If too long (> 200), trim
    elif len(desc) > 200:
        # Trim at sentence boundary
        trimmed = desc[:197] + '...'
        new_content = content.replace(
            f'<meta name="description" content="{desc}"',
            f'<meta name="description" content="{trimmed}"',
            1
        )
        html_file.write_text(new_content, encoding='utf-8')
        fixed_count += 1
        print(f'  Trimmed: {rel} ({len(desc)} → {len(trimmed)})')

print(f'\n=== Fixed {fixed_count} description-length issues ===')
PYEOF

echo "" >> "$LOG"
echo "[Done] All SEO fixes applied. Re-run health check to verify." >> "$LOG"
echo "Log: $LOG"
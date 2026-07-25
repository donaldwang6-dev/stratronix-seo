#!/bin/bash
# Inject JERRY analytics beacon into all HTML files (HEAD only)
# 铁律 33.1: 仅修改 <head> 区域, 不动 <body> 显示内容

set -e
SEO_REPO="/home/donald/.openclaw/workspace/stratronix-seo"
ANALYTICS_JS="https://analytics.jerry.stratronix.ai/analytics.js"
SITE_NAME="stratronix-seo"

COUNT=0
SKIP=0

# 注入模板 - 加在 <head> 末尾 </head> 前
INJECT='\n<!-- JERRY Analytics (汪总 13:09 LOCKED) -->\n<script async src="'$ANALYTICS_JS'" data-site="'$SITE_NAME'"></script>\n<noscript><img src="https://analytics.jerry.stratronix.ai/collect?site='$SITE_NAME'&p='$SITE_NAME'" width="1" height="1" alt="" /></noscript>'

for f in $(find "$SEO_REPO" -name "*.html" -type f); do
    # 跳过已注入
    if grep -q "JERRY Analytics" "$f"; then
        SKIP=$((SKIP+1))
        continue
    fi
    
    # 用 python 安全注入 (避免 sed 转义问题)
    python3 << PYEOF
import sys
fn = "$f"
with open(fn, 'r', encoding='utf-8') as fp:
    content = fp.read()

inject = '''<!-- JERRY Analytics (汪总 13:09 LOCKED) -->
<script async src="$ANALYTICS_JS" data-site="$SITE_NAME"></script>
<noscript><img src="https://analytics.jerry.stratronix.ai/collect?site=$SITE_NAME" width="1" height="1" alt="" /></noscript>
'''
if '</head>' in content.lower():
    # 找到第一个 </head> 大小写不敏感位置
    idx = content.lower().find('</head>')
    new_content = content[:idx] + inject + '\n' + content[idx:]
    with open(fn, 'w', encoding='utf-8') as fp:
        fp.write(new_content)
    print(f"OK: {fn}")
PYEOF
    COUNT=$((COUNT+1))
done

echo "注入完成: $COUNT 文件, 跳过: $SKIP"

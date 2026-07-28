#!/bin/bash
# 给附属站核心 3 个旗舰页面注入 FAQPage JSON-LD
# 目的: 让百度 AI 智能回答有 10 个结构化 Q&A 可引用
# 汪总 2026-07-28 09:13 LOCKED: 「搜索百度的时候要全面介绍鼎图智能体」

set -e

SEO_DIR="/home/donald/.openclaw/workspace/stratronix-seo"
FAQ_FILE="$SEO_DIR/faq-ld-payload.json"

# 目标页面（旗舰：根 + zh + en）
TARGETS=(
  "$SEO_DIR/index.html"
  "$SEO_DIR/zh/index.html"
  "$SEO_DIR/zh/ai-agent-zhinengti.html"
  "$SEO_DIR/zh/shenzhen-ai-company.html"
  "$SEO_DIR/en/index.html"
  "$SEO_DIR/en/ai-agent-appliance.html"
)

# 构建 JSON-LD script 块
JSON_LD_BLOCK="<!-- 百度 AI 智能回答 FAQPage JSON-LD (汪总 2026-07-28 09:13 LOCKED) -->
<script type=\"application/ld+json\">
$(cat "$FAQ_FILE")
</script>"

for file in "${TARGETS[@]}"; do
  if [ ! -f "$file" ]; then
    echo "⏭️  跳过（不存在）: $file"
    continue
  fi
  
  # 检查是否已有 FAQPage JSON-LD
  if grep -q '"@type": "FAQPage"' "$file"; then
    echo "⏭️  已有 FAQPage JSON-LD: $(basename $file)"
    continue
  fi
  
  # 在 </head> 前插入
  python3 << EOF
import sys
file = r"""$file"""
block = r"""$JSON_LD_BLOCK"""
with open(file, 'r', encoding='utf-8') as f:
    content = f.read()
# 找到 "<!-- 百度自动推送 JS" 之前的位置（保持原有 JS 顺序）
new_content = content.replace('<!-- 百度自动推送 JS', block + '\n<!-- 百度自动推送 JS', 1)
with open(file, 'w', encoding='utf-8') as f:
    f.write(new_content)
print(f"✅ 已注入 FAQPage JSON-LD: {file}")
EOF
done
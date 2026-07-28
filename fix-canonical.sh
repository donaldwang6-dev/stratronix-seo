#!/bin/bash
# 修复附属站 1092 个页面的 canonical URL
# 原因: 之前 canonical 全部指向主站 www.stratronix.ai/zh/...
#       但主站铁律 14 禁改, 这些 URL 实际 404
#       百度爬虫跳过 → AI 智能回答没有素材
# 修复: 全部改为附属站实际部署 URL
# 汪总 2026-07-28 09:13 LOCKED: 「搜索百度的时候要全面介绍鼎图智能体」

set -e

SEO_DIR="/home/donald/.openclaw/workspace/stratronix-seo"
SITE_BASE="https://donaldwang6-dev.github.io/stratronix-seo"

cd "$SEO_DIR"

echo "🔍 扫描需要修复 canonical 的页面..."

# 找出所有 canonical 指向 www.stratronix.ai 的 HTML
mapfile -t FILES < <(grep -rl "canonical.*stratronix\.ai" --include="*.html" . 2>/dev/null | grep -v "\.git/")

TOTAL=${#FILES[@]}
echo "📊 共找到 $TOTAL 个页面需要修复"
echo ""

COUNT_FIXED=0
COUNT_SKIP=0

for file in "${FILES[@]}"; do
  # 跳过主站目录的页面
  if [[ "$file" == "./stratronix-website"* ]]; then
    COUNT_SKIP=$((COUNT_SKIP + 1))
    continue
  fi

  # 提取文件相对路径（去掉 ./ 前缀）
  rel_path="${file#./}"

  # 计算正确的 canonical URL
  # 例如: zh/ai-agent-zhinengti.html -> https://donaldwang6-dev.github.io/stratronix-seo/zh/ai-agent-zhinengti.html
  #       en/index.html -> https://donaldwang6-dev.github.io/stratronix-seo/en/index.html
  #       index.html -> https://donaldwang6-dev.github.io/stratronix-seo/
  if [[ "$rel_path" == "index.html" ]]; then
    new_canonical="${SITE_BASE}/"
  else
    new_canonical="${SITE_BASE}/${rel_path}"
  fi

  # 用 python 替换（更精确）
  python3 -c "
import sys, re
file = sys.argv[1]
new_canonical = sys.argv[2]
with open(file, 'r', encoding='utf-8') as f:
    content = f.read()
# 替换 canonical 行
new_content = re.sub(
    r'<link rel=\"canonical\" href=\"[^\"]*\">',
    f'<link rel=\"canonical\" href=\"{new_canonical}\">',
    content,
    count=1
)
if new_content != content:
    with open(file, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print('fixed')
else:
    print('skip')
" "$file" "$new_canonical" > /dev/null

  if grep -q "canonical.*$new_canonical" "$file" 2>/dev/null; then
    COUNT_FIXED=$((COUNT_FIXED + 1))
  fi
done

echo ""
echo "═══════════════════════════════════════════════"
echo "📊 Canonical 修复结果:"
echo "  ✅ 已修复: $COUNT_FIXED"
echo "  ⏭️  跳过: $COUNT_SKIP"
echo "═══════════════════════════════════════════════"
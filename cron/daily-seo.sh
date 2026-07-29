#!/bin/bash
# STRATRONIX Daily AI Crawler & Search Engine Diagnostic
# 诊断 AI 爬虫 + 搜索引擎能否发现/收录我们
# Last updated: 2026-07-29

set -e

SITE_BASE="https://donaldwang6-dev.github.io/stratonix-seo"
MAIN_SITE="https://www.stratronix.ai"

LOG_FILE="/home/donald/.openclaw/workspace/stratronix-seo/cron/daily-seo-$(date +%Y%m%d).log"

mkdir -p "$(dirname "$LOG_FILE")"

echo "===========================================" | tee -a "$LOG_FILE"
echo "STRATRONIX Daily SEO Diagnostic" | tee -a "$LOG_FILE"
echo "Date: $(date '+%Y-%m-%d %H:%M:%S')" | tee -a "$LOG_FILE"
echo "===========================================" | tee -a "$LOG_FILE"

# 测试每个 AI 爬虫/搜索引擎的可达性
echo "" | tee -a "$LOG_FILE"
echo "[1] AI 时代文件可访问性测试:" | tee -a "$LOG_FILE"

declare -a AI_FILES=(
  "llms.txt"
  "robots.txt"
  "ai-plugin.json"
  ".well-known/ai.txt"
  "sitemap.xml"
)

for f in "${AI_FILES[@]}"; do
  url="$SITE_BASE/$f"
  code=$(curl -s -o /dev/null -w "%{http_code}" -m 10 "$url")
  size=$(curl -s -m 10 "$url" | wc -c)
  echo "  HTTP $code  $url (${size} bytes)" | tee -a "$LOG_FILE"
done

# 测试主要语言页面
echo "" | tee -a "$LOG_FILE"
echo "[2] 主要语言页面测试:" | tee -a "$LOG_FILE"

declare -a LANG_DIRS=(
  "zh"
  "en"
  "es"
  "fr"
  "de"
  "it"
  "pt"
  "nl"
  "ru"
  "ja"
  "ko"
  "ar"
  "he"
  "vi"
  "uk"
  "sr"
  "ch"
  "cs"
  "pl"
  "sv"
  "ro"
  "hu"
  "fi"
  "no"
)

LANG_OK=0
LANG_FAIL=0
for lang in "${LANG_DIRS[@]}"; do
  code=$(curl -s -o /dev/null -w "%{http_code}" -m 5 "$SITE_BASE/$lang/index.html")
  if [[ "$code" == "200" ]]; then
    LANG_OK=$((LANG_OK+1))
  else
    LANG_FAIL=$((LANG_FAIL+1))
  fi
done

echo "  可访问语言: $LANG_OK / 失败: $LANG_FAIL / 总: ${#LANG_DIRS[@]}" | tee -a "$LOG_FILE"

# 检查 Pages 是否启用
echo "" | tee -a "$LOG_FILE"
echo "[3] Pages 启用状态:" | tee -a "$LOG_FILE"
HOME_CODE=$(curl -s -o /dev/null -w "%{http_code}" -m 5 "$SITE_BASE/")
if [[ "$HOME_CODE" == "200" ]]; then
  echo "  ✅ GitHub Pages 已启用" | tee -a "$LOG_FILE"
else
  echo "  ❌ GitHub Pages 未启用 (HTTP $HOME_CODE)" | tee -a "$LOG_FILE"
  echo "  必须 Donald 操作: https://github.com/donaldwang6-dev/stratonix-seo/settings/pages" | tee -a "$LOG_FILE"
fi

# 决策
echo "" | tee -a "$LOG_FILE"
echo "===========================================" | tee -a "$LOG_FILE"
echo "决策:" | tee -a "$LOG_FILE"
if [[ "$HOME_CODE" != "200" ]]; then
  echo "  ⚠️  Pages 未启用 — 所有 SEO 推送无效" | tee -a "$LOG_FILE"
  echo "  P0: Donald 必须启用 Pages (1 分钟操作)" | tee -a "$LOG_FILE"
  echo "  P1: 继续生产 PAA 内容 (不依赖 Pages)" | tee -a "$LOG_FILE"
else
  echo "  ✅ Pages 健康 — 立即批量推送" | tee -a "$LOG_FILE"
  echo "  P0: 批量 IndexNow 推送所有 URL" | tee -a "$LOG_FILE"
  echo "  P1: 推送 sitemap 至 Bing/Yandex/百度" | tee -a "$LOG_FILE"
fi
echo "===========================================" | tee -a "$LOG_FILE"
#!/usr/bin/env python3
"""
将 11 个 .md 平台内容生成可索引的 HTML 页面（用于 SEO 反链）
"""
import os, re, gzip, shutil

ROOT = '/home/donald/.openclaw/workspace/stratronix-seo'
BASE_URL = 'https://donaldwang6-dev.github.io/stratronix-seo'

PLATFORMS = {
    'zhihu': {
        'name': '知乎专栏',
        'name_en': 'Zhihu Column',
        'title': 'PAA 私有 AI 智能体深度解析 · STRATRONIX 鼎图太易',
        'desc': '深度技术文章：PAA 私有 AI 智能体的架构、隐私保护、与云端 AI 对比、ROI 测算。STRATRONIX 鼎图太易原创。',
        'icon': '📘',
        'color': '#0084ff'
    },
    'wechat': {
        'name': '微信公众号',
        'name_en': 'WeChat Official Account',
        'title': 'STRATRONIX 服务号官方文章 · 邀请莅临 IOTE 2026 展位 12B62-1',
        'desc': 'STRATRONIX 微信公众号官方文章：IOTE 2026 深圳物联网展邀请函 + STA-100 PAA 全球首发。',
        'icon': '💬',
        'color': '#07c160'
    },
    'baijiahao': {
        'name': '百家号',
        'name_en': 'Baijiahao',
        'title': '深圳 AI 公司 STRATRONIX 鼎图太易 · IOTE 2026 邀您莅临 12B62-1',
        'desc': '深圳 AI 公司鼎图太易 IOTE 2026 邀请函：8/26-28 深圳国际会展中心 12 号馆展位 12B62-1，全球首发 STA-100 PAA 私有 AI 智能体设备。',
        'icon': '📰',
        'color': '#e02e24'
    },
    'baidu-tieba': {
        'name': '百度贴吧',
        'name_en': 'Baidu Tieba',
        'title': '深圳 IoT 公司 IOTE 2026 现场求围观 · 12B62-1 展位送设备',
        'desc': '百度贴吧 IoT 吧互动短帖：深圳 AI 创业公司 STRATRONIX 全球首发 STA-100 PAA 私有 AI 智能体设备，8/26-28 IOTE 2026 现场送样机。',
        'icon': '💭',
        'color': '#3385ff'
    },
    'douyin': {
        'name': '抖音',
        'name_en': 'Douyin TikTok',
        'title': '60 秒看懂 STRATRONIX PAA 私有 AI 智能体设备 · IOTE 2026',
        'desc': '抖音 60 秒视频脚本：PAA 私有 AI 智能体设备的核心价值、隐私保护优势、IOTE 2026 展位信息。',
        'icon': '🎵',
        'color': '#000'
    },
    'csdnbbs': {
        'name': 'CSDN 论坛',
        'name_en': 'CSDN Developer Forum',
        'title': 'OpenClaw 开源 AI 智能体框架介绍 · STRATRONIX STA-100 PAA',
        'desc': 'CSDN 开发者向技术文：OpenClaw BSD-3-Clause 开源 AI 智能体框架架构、自学习自演化机制、与传统 chatbot 对比。',
        'icon': '💻',
        'color': '#c00'
    },
    'baidu-zhidao': {
        'name': '百度知道',
        'name_en': 'Baidu Zhidao',
        'title': 'PAA 私有 AI 智能体是什么？STRATRONIX 鼎图太易 Q&A',
        'desc': '百度知道 Q&A 软植入：5 组问答覆盖 PAA 定义、隐私保护、与云端 AI 对比、$399 价格、IOTE 2026 展位。',
        'icon': '❓',
        'color': '#2450fb'
    },
    'kol-invitation': {
        'name': 'KOL / 媒体邀请函',
        'name_en': 'KOL Media Invitation',
        'title': 'IOTE 2026 KOL 邀请函 · STRATRONIX 站台嘉宾/联合直播/内容共创',
        'desc': 'IOTE 2026 KOL/媒体邀请函：3 种合作形式（站台嘉宾/联合直播/内容共创）、47 位 KOL 邀请名单、20 家媒体 PR 计划。',
        'icon': '🎤',
        'color': '#E6417F'
    },
    'openclaw-intro': {
        'name': 'OpenClaw 介绍',
        'name_en': 'OpenClaw Introduction',
        'title': 'OpenClaw 开源 AI 智能体框架 · STRATRONIX STA-100 内置',
        'desc': 'OpenClaw BSD-3-Clause 开源 AI 智能体框架介绍：自学习自演化、多平台集成、隐私保护架构。STRATRONIX STA-100 PAA 内置。',
        'icon': '🐾',
        'color': '#1E6FD9'
    },
}

def md_to_html(md_content, platform_key, meta):
    """将 markdown 内容转成 HTML（基础转义）"""
    # 简单转换：转义 HTML 特殊字符
    html = md_content
    # 保留 code blocks
    code_blocks = []
    def save_code(m):
        code_blocks.append(m.group(1))
        return f'\n<<<CODE_{len(code_blocks)-1}>>>\n'
    html = re.sub(r'```\n(.*?)\n```', save_code, html, flags=re.DOTALL)
    # 转义
    html = html.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
    # 标题
    html = re.sub(r'^# (.+)$', r'<h1>\1</h1>', html, flags=re.MULTILINE)
    html = re.sub(r'^## (.+)$', r'<h2>\1</h2>', html, flags=re.MULTILINE)
    html = re.sub(r'^### (.+)$', r'<h3>\1</h3>', html, flags=re.MULTILINE)
    # 粗体/斜体
    html = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', html)
    html = re.sub(r'\*(.+?)\*', r'<em>\1</em>', html)
    # 列表
    html = re.sub(r'^- (.+)$', r'<li>\1</li>', html, flags=re.MULTILINE)
    html = re.sub(r'(<li>.*?</li>\n?)+', lambda m: '<ul>' + m.group(0) + '</ul>', html, flags=re.DOTALL)
    # 段落
    paragraphs = []
    for line in html.split('\n'):
        if line.strip() and not line.startswith('<'):
            paragraphs.append(f'<p>{line}</p>')
        else:
            paragraphs.append(line)
    html = '\n'.join(paragraphs)
    # 恢复 code blocks
    for i, code in enumerate(code_blocks):
        html = html.replace(f'&lt;&lt;&lt;CODE_{i}&gt;&gt;&gt;', f'<pre><code>{code.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")}</code></pre>')
    return html


def md_to_html_simple(md_content):
    """极简 markdown 转 HTML（保留段落）"""
    html = md_content
    code_blocks = []
    def save_code(m):
        code_blocks.append(m.group(1))
        return f'\n<<<CODE_{len(code_blocks)-1}>>>\n'
    html = re.sub(r'```\n(.*?)\n```', save_code, html, flags=re.DOTALL)
    html = html.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
    html = re.sub(r'^# (.+)$', r'<h1>\1</h1>', html, flags=re.MULTILINE)
    html = re.sub(r'^## (.+)$', r'<h2>\1</h2>', html, flags=re.MULTILINE)
    html = re.sub(r'^### (.+)$', r'<h3>\1</h3>', html, flags=re.MULTILINE)
    html = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', html)
    html = re.sub(r'\*(.+?)\*', r'<em>\1</em>', html)
    paragraphs = []
    in_list = False
    for line in html.split('\n'):
        s = line.strip()
        if s.startswith('- '):
            if not in_list:
                paragraphs.append('<ul>')
                in_list = True
            paragraphs.append(f'<li>{s[2:]}</li>')
        elif s.startswith('---'):
            paragraphs.append('<hr>')
        elif s.startswith('|'):
            paragraphs.append(f'<p>{s}</p>')
        elif s and not s.startswith('<'):
            if in_list:
                paragraphs.append('</ul>')
                in_list = False
            paragraphs.append(f'<p>{s}</p>')
        elif s == '':
            if in_list:
                paragraphs.append('</ul>')
                in_list = False
        else:
            paragraphs.append(line)
    if in_list:
        paragraphs.append('</ul>')
    html = '\n'.join(paragraphs)
    for i, code in enumerate(code_blocks):
        safe = code.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
        html = html.replace(f'&lt;&lt;&lt;CODE_{i}&gt;&gt;&gt;', f'<pre><code>{safe}</code></pre>')
    return html


# 平台内容映射（一个平台多个文件 → 合并到一个 HTML）
PLATFORM_FILES = {
    'zhihu': ['events/iot-expo-2026/zh-content/zhihu/article-01-paa-explained.md'],
    'wechat': ['events/iot-expo-2026/zh-content/wechat/official-account-article-01.md'],
    'baijiahao': ['events/iot-expo-2026/zh-content/baijiahao/seo-article-01.md'],
    'baidu-tieba': ['events/iot-expo-2026/zh-content/baidu-tieba/post-01.md'],
    'douyin': ['events/iot-expo-2026/zh-content/douyin/video-script-60s.md'],
    'csdnbbs': ['events/iot-expo-2026/zh-content/csdnbbs/developer-forum-post-01.md'],
    'baidu-zhidao': ['events/iot-expo-2026/zh-content/baidu-zhidao/qa-pairs.md'],
    'kol-invitation': ['events/iot-expo-2026/zh-content/kol-invitation.md'],
    'openclaw-intro': [
        'events/iot-expo-2026/zh-content/openclaw-intro/short-zh.md',
        'events/iot-expo-2026/zh-content/openclaw-intro/full-zh.md',
        'events/iot-expo-2026/zh-content/openclaw-intro/short-en.md',
    ],
}


def make_platform_html(platform_key, meta, files):
    """为单个平台生成完整 HTML"""
    combined_md = ''
    for f in files:
        if os.path.exists(f):
            with open(f, 'r', encoding='utf-8') as fp:
                combined_md += '\n\n---\n\n' + fp.read()
    body = md_to_html_simple(combined_md)
    
    slug = platform_key.replace('-', '-')
    url_path = f'events/iot-expo-2026/zh-content/{slug}.html'
    
    html = f'''<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{meta["title"]} | STRATRONIX IOTE 2026</title>
<meta name="description" content="{meta["desc"]}">
<meta name="keywords" content="IOTE 2026, STRATRONIX, {meta["name"]}, 鼎图太易, STA-100, PAA, 私有 AI, AI 智能体, 展位 12B62-1">
<meta name="robots" content="index, follow, max-snippet:-1">
<meta name="author" content="STRATRONIX 鼎图太易信息技术（深圳）有限公司">
<link rel="canonical" href="{BASE_URL}/{url_path}">
<meta property="og:title" content="{meta["title"]}">
<meta property="og:description" content="{meta["desc"]}">
<meta property="og:url" content="{BASE_URL}/{url_path}">
<meta property="og:image" content="{BASE_URL}/og-images/og-image-iot-2026.png">
<meta property="og:type" content="article">
<style>
:root{{--pink:#E6417F;--pink-dark:#C9296C;--gray:#666;--bg:#fafafa}}
*{{box-sizing:border-box;margin:0;padding:0}}
body{{font-family:-apple-system,BlinkMacSystemFont,"PingFang SC","Microsoft YaHei",sans-serif;line-height:1.8;color:#222;background:var(--bg);padding:24px 20px}}
.wrap{{max-width:860px;margin:0 auto;background:#fff;padding:32px;border-radius:12px;box-shadow:0 2px 12px rgba(0,0,0,0.06)}}
.platform-badge{{display:inline-block;background:{meta["color"]};color:#fff;padding:8px 18px;border-radius:20px;font-size:0.95em;font-weight:600;margin-bottom:20px}}
.platform-badge .icon{{font-size:1.2em;margin-right:8px}}
h1{{color:var(--pink);font-size:2em;margin:16px 0 12px;padding-bottom:12px;border-bottom:3px solid var(--pink)}}
h2{{color:var(--pink-dark);font-size:1.4em;margin:28px 0 12px;padding-left:12px;border-left:4px solid var(--pink)}}
h3{{color:#222;font-size:1.15em;margin:20px 0 8px}}
p{{margin-bottom:14px;color:#333}}
ul{{margin:12px 0 16px 24px}}
li{{margin-bottom:6px}}
strong{{color:var(--pink-dark)}}
em{{color:#555}}
pre{{background:#1e1e1e;color:#d4d4d4;padding:16px;border-radius:8px;overflow-x:auto;margin:14px 0}}
code{{font-family:"SF Mono","Consolas","Monaco",monospace;font-size:0.92em}}
hr{{border:none;border-top:2px dashed #eee;margin:24px 0}}
.cta-block{{background:linear-gradient(135deg,var(--pink) 0%,var(--pink-dark) 100%);color:#fff;padding:24px;border-radius:8px;margin-top:32px;text-align:center}}
.cta-block h2{{color:#fff;border:none;padding:0;margin:0 0 12px}}
.cta-block a{{color:#fff;text-decoration:underline;font-weight:600}}
.cta-block .email{{font-size:1.15em;font-weight:700;display:inline-block;background:rgba(255,255,255,0.2);padding:6px 14px;border-radius:6px;margin:4px}}
footer{{margin-top:32px;padding-top:16px;border-top:1px solid #eee;color:var(--gray);font-size:0.85em;text-align:center}}
</style>
</head>
<body>
<div class="wrap">
<div class="platform-badge"><span class="icon">{meta["icon"]}</span>{meta["name"]} · {meta["name_en"]}</div>
{body}

<div class="cta-block">
<h2>🎯 邀请您莅临 IOTE 2026</h2>
<p style="margin:0 0 8px;color:#fff">8 月 26-28 日 · 深圳国际会展中心 12 号馆 · 展位 12B62-1</p>
<a href="mailto:sales@stratronix.ai" class="email">📧 sales@stratronix.ai</a>
<a href="mailto:apac@stratronix.ai" class="email">📧 apac@stratronix.ai</a>
<p style="margin-top:14px;font-size:0.9em"><a href="https://www.stratronix.ai">www.stratronix.ai</a> · 鼎图太易信息技术（深圳）有限公司</p>
</div>
</div>
<footer>
<p>STRATRONIX IOTE 2026 · 全球首发 STA-100 PAA 私有 AI 智能体设备</p>
<p>本页面由 STRATRONIX 市场推广智能体 (JERRY) 自动从 {meta["name"]} 发布稿生成 · 2026-08-14</p>
</footer>
</body>
</html>'''
    return html, url_path


count = 0
for key, meta in PLATFORMS.items():
    files = PLATFORM_FILES[key]
    html, url_path = make_platform_html(key, meta, files)
    full_path = os.path.join(ROOT, url_path)
    os.makedirs(os.path.dirname(full_path), exist_ok=True)
    with open(full_path, 'w', encoding='utf-8') as fp:
        fp.write(html)
    # gz 压缩
    with open(full_path, 'rb') as f_in:
        with gzip.open(full_path + '.gz', 'wb', compresslevel=9) as f_out:
            shutil.copyfileobj(f_in, f_out)
    count += 1
    print(f"  ✅ {key}: {url_path} ({os.path.getsize(full_path)/1024:.0f} KB)")

print(f"\n✅ 共生成 {count} 个平台 HTML 反链页")

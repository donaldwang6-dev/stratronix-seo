#!/usr/bin/env python3
"""
批量修复 stratronix-seo 附属站 SEO 问题
- 补 viewport meta（375 页）
- 补 canonical（19 页）
- 补 og:title/og:description/og:image（382 页）
- 缩短过长 title（646 页）
- 缩短过长 description（391 页）
- 补缺失 H1（10 页）
- 补缺失 description（16 页）
"""
import os, re, sys
from pathlib import Path

BASE_URL = "https://donaldwang6-dev.github.io/stratronix-seo"
DEFAULT_OG_IMAGE = "https://donaldwang6-dev.github.io/stratronix-seo/og-images/og-image-sta-100.png"

# 统计
stats = {
    'viewport_added': 0,
    'canonical_added': 0,
    'og_added': 0,
    'title_shortened': 0,
    'title_extended': 0,
    'desc_shortened': 0,
    'desc_extended': 0,
    'desc_added': 0,
    'h1_added': 0,
    'lang_added': 0,
    'files_modified': 0,
}

# 语言推断（从路径）
def infer_lang(path):
    """从 URL 路径推断语言代码"""
    p = path.lstrip('./').lstrip('/')
    # 第一段是语言目录
    first = p.split('/')[0] if '/' in p else p.replace('.html', '')
    lang_map = {
        'zh': 'zh-CN', 'en': 'en-US', 'ja': 'ja-JP', 'ko': 'ko-KR',
        'es': 'es-ES', 'fr': 'fr-FR', 'de': 'de-DE', 'it': 'it-IT',
        'pt': 'pt-PT', 'ru': 'ru-RU', 'ar': 'ar-SA', 'th': 'th-TH',
        'vi': 'vi-VN', 'id': 'id-ID', 'ms': 'ms-MY', 'hi': 'hi-IN',
        'tr': 'tr-TR', 'pl': 'pl-PL', 'nl': 'nl-NL', 'sv': 'sv-SE',
        'no': 'no-NO', 'da': 'da-DK', 'fi': 'fi-FI', 'cs': 'cs-CZ',
        'hu': 'hu-HU', 'ro': 'ro-RO', 'el': 'el-GR', 'he': 'he-IL',
        'bn': 'bn-BD', 'ta': 'ta-IN', 'si': 'si-LK', 'ne': 'ne-NP',
        'uk': 'uk-UA', 'bg': 'bg-BG', 'hr': 'hr-HR', 'sk': 'sk-SK',
        'sl': 'sl-SI', 'sr': 'sr-RS', 'lt': 'lt-LT', 'lv': 'lv-LV',
        'et': 'et-EE', 'is': 'is-IS', 'ga': 'ga-IE', 'mt': 'mt-MT',
        'eu': 'eu-ES', 'ca': 'ca-ES', 'gl': 'gl-ES', 'cy': 'cy-GB',
        'af': 'af-ZA', 'sw': 'sw-KE', 'zu': 'zu-ZA', 'xh': 'xh-ZA',
        'am': 'am-ET', 'ha': 'ha-NG', 'ig': 'ig-NG', 'yo': 'yo-NG',
        'so': 'so-SO', 'mg': 'mg-MG', 'sn': 'sn-ZW', 'st': 'st-ZA',
        'tn': 'tn-ZA', 'ts': 'ts-ZA', 've': 've-ZA', 'ss': 'ss-ZA',
        'nr': 'nr-ZA', 'nd': 'nd-ZW', 'be': 'be-BY', 'bs': 'bs-BA',
        'mk': 'mk-MK', 'sq': 'sq-AL', 'az': 'az-AZ', 'hy': 'hy-AM',
        'ka': 'ka-GE', 'kk': 'kk-KZ', 'ky': 'ky-KG', 'lo': 'lo-LA',
        'mn': 'mn-MN', 'my': 'my-MM', 'ps': 'ps-AF', 'fa': 'fa-IR',
        'sd': 'sd-PK', 'ur': 'ur-PK', 'uz': 'uz-UZ', 'yi': 'yi',
        'jv': 'jv-ID', 'su': 'su-ID', 'ceb': 'ceb-PH', 'tl': 'tl-PH',
        'haw': 'haw-US', 'sm': 'sm-WS', 'mi': 'mi-NZ', 'fo': 'fo-FO',
        'lb': 'lb-LU', 'rm': 'rm-CH', 'gd': 'gd-GB', 'br': 'br-FR',
        'fur': 'fur-IT', 'sc': 'sc-IT', 'vec': 'vec-IT', 'lmo': 'lmo',
        'nap': 'nap-IT', 'pms': 'pms-IT', 'co': 'co-FR', 'oc': 'oc-FR',
        'ba': 'ba-RU', 'kv': 'kv-RU', 'mhr': 'mhr-RU', 'mrj': 'mrj-RU',
        'udm': 'udm-RU', 'koi': 'koi-RU', 'kv': 'kv-RU',
        # 国家/地区目录映射
        'au': 'en-AU', 'ca': 'en-CA', 'gb': 'en-GB', 'ie': 'en-IE',
        'nz': 'en-NZ', 'sg': 'en-SG', 'in': 'hi-IN', 'ph': 'en-PH',
        'id': 'id-ID', 'my': 'ms-MY', 'th': 'th-TH', 'vn': 'vi-VN',
        'jp': 'ja-JP', 'kr': 'ko-KR', 'cn': 'zh-CN', 'tw': 'zh-TW',
        'hk': 'zh-HK', 'mo': 'zh-MO', 'mx': 'es-MX', 'br': 'pt-BR',
        'ar': 'es-AR', 'cl': 'es-CL', 'co': 'es-CO', 'pe': 'es-PE',
        've': 'es-VE', 'uy': 'es-UY', 'py': 'es-PY', 'bo': 'es-BO',
        'ec': 'es-EC', 'cr': 'es-CR', 'pa': 'es-PA', 'do': 'es-DO',
        'gt': 'es-GT', 'hn': 'es-HN', 'ni': 'es-NI', 'sv': 'es-SV',
        'pr': 'es-PR', 'cu': 'es-CU', 'us': 'en-US', 'na': 'en-US',
        'eu': 'en-GB', 'mena': 'ar-SA', 'sea': 'en-SG', 'sa': 'ar-SA',
        'ae': 'ar-AE', 'eg': 'ar-EG', 'qa': 'ar-QA', 'kw': 'ar-KW',
        'sa': 'ar-SA', 'om': 'ar-OM', 'bh': 'ar-BH', 'lb': 'ar-LB',
        'jo': 'ar-JO', 'iq': 'ar-IQ', 'ye': 'ar-YE', 'tr': 'tr-TR',
        'pk': 'ur-PK', 'bd': 'bn-BD', 'lk': 'si-LK', 'np': 'ne-NP',
        'mm': 'my-MM', 'kh': 'km-KH', 'la': 'lo-LA', 'mn': 'mn-MN',
        'kz': 'kk-KZ', 'uz': 'uz-UZ', 'kg': 'ky-KG', 'tj': 'tg-TJ',
        'tm': 'tk-TM', 'az': 'az-AZ', 'ge': 'ka-GE', 'am': 'hy-AM',
        'by': 'be-BY', 'ua': 'uk-UA', 'md': 'ro-MD', 'rs': 'sr-RS',
        'hr': 'hr-HR', 'ba': 'bs-BA', 'me': 'sr-ME', 'xk': 'sq-XK',
        'mk': 'mk-MK', 'al': 'sq-AL', 'gr': 'el-GR', 'cy': 'el-CY',
        'mt': 'mt-MT', 'is': 'is-IS', 'fo': 'fo-FO', 'gl': 'gl-ES',
        'lu': 'lb-LU', 'be': 'nl-BE', 'ch': 'de-CH', 'at': 'de-AT',
        'li': 'de-LI', 'mc': 'fr-MC', 'ad': 'ca-AD', 'sm': 'it-SM',
        'va': 'it-VA', 'it': 'it-IT', 'si': 'sl-SI', 'cz': 'cs-CZ',
        'sk': 'sk-SK', 'pl': 'pl-PL', 'hu': 'hu-HU', 'ro': 'ro-RO',
        'bg': 'bg-BG', 'ee': 'et-EE', 'lv': 'lv-LV', 'lt': 'lt-LT',
        'fi': 'fi-FI', 'se': 'sv-SE', 'no': 'no-NO', 'dk': 'da-DK',
        'is': 'is-IS', 'ie': 'ga-IE', 'cy': 'el-CY',
    }
    # 先尝试作为语言代码
    if first in lang_map:
        return lang_map[first]
    # 默认英文
    return 'en-US'


def truncate_title(title, max_len=60):
    """智能截断 title，保留品牌"""
    if len(title) <= max_len:
        return title
    # 尝试在分隔符处截断
    for sep in [' | ', ' - ', ' — ', ' · ', ' / ', ' : ']:
        if sep in title:
            parts = title.split(sep)
            for i in range(len(parts)-1, 0, -1):
                truncated = sep.join(parts[:i]).strip()
                if 20 <= len(truncated) <= max_len:
                    return truncated
    # 最后按字符截断
    return title[:max_len-3].rstrip() + '...'


def shorten_description(desc, max_len=160):
    """智能缩短 description"""
    if len(desc) <= max_len:
        return desc
    # 在句末标点截断
    truncated = desc[:max_len]
    for sep in ['. ', '。 ', '! ', '！ ', '? ', '？ ', '; ', '； ', ', ', '， ']:
        idx = truncated.rfind(sep)
        if idx >= 80:
            return truncated[:idx+1].strip()
    return truncated.rstrip() + '...'


def process_file(path):
    """处理单个文件"""
    try:
        with open(path, 'r', encoding='utf-8') as fp:
            content = fp.read()
    except Exception:
        return False
    
    original = content
    modified = False
    
    # 1. 补 viewport meta
    if not re.search(r'<meta\s+name=["\']viewport["\']', content, re.I):
        viewport_tag = '<meta name="viewport" content="width=device-width, initial-scale=1.0">'
        # 在 charset 后面插入
        content = re.sub(
            r'(<meta\s+charset=["\'][^"\']*["\']>)',
            r'\1\n    ' + viewport_tag,
            content,
            count=1
        )
        if viewport_tag in content:
            stats['viewport_added'] += 1
            modified = True
    
    # 2. 补 canonical
    canonical_match = re.search(r'<link\s+rel=["\']canonical["\']\s+href=["\']([^"\']*)["\']', content, re.I)
    if not canonical_match:
        # 计算 canonical URL（去掉 ./ 和 .html 可选）
        url_path = path.lstrip('./').lstrip('/')
        if url_path == 'index.html':
            url_path = ''
        elif url_path.endswith('/index.html'):
            url_path = url_path[:-11]
        canonical_url = f"{BASE_URL}/{url_path}" if url_path else f"{BASE_URL}/"
        canonical_tag = f'<link rel="canonical" href="{canonical_url}">'
        # 在 viewport 后插入
        content = re.sub(
            r'(<meta\s+name=["\']viewport["\'][^>]*>)',
            r'\1\n    ' + canonical_tag,
            content,
            count=1
        )
        if canonical_tag in content:
            stats['canonical_added'] += 1
            modified = True
    
    # 3. 补 og:title, og:description, og:image
    og_title_match = re.search(r'<meta\s+(?:property|name)=["\']og:title["\']\s+content=["\']([^"\']*)["\']', content, re.I)
    og_desc_match = re.search(r'<meta\s+(?:property|name)=["\']og:description["\']\s+content=["\']([^"\']*)["\']', content, re.I)
    og_image_match = re.search(r'<meta\s+(?:property|name)=["\']og:image["\']\s+content=["\']([^"\']*)["\']', content, re.I)
    
    if not og_title_match or not og_desc_match or not og_image_match:
        title_match = re.search(r'<title>(.*?)</title>', content, re.DOTALL)
        desc_match = re.search(r'<meta\s+name=["\']description["\']\s+content=["\']([^"\']*)["\']', content, re.I)
        title = title_match.group(1).strip() if title_match else 'STRATRONIX'
        desc = desc_match.group(1) if desc_match else 'Private AI Appliance by STRATRONIX'
        
        og_tags = []
        if not og_title_match:
            og_tags.append(f'<meta property="og:title" content="{title[:200]}">')
        if not og_desc_match:
            og_tags.append(f'<meta property="og:description" content="{desc[:300]}">')
        if not og_image_match:
            og_tags.append(f'<meta property="og:image" content="{DEFAULT_OG_IMAGE}">')
        # 补 og:type
        if not re.search(r'og:type', content, re.I):
            og_tags.append('<meta property="og:type" content="website">')
        # 补 og:url
        url_path = path.lstrip('./').lstrip('/')
        if url_path == 'index.html':
            url_path = ''
        elif url_path.endswith('/index.html'):
            url_path = url_path[:-11]
        page_url = f"{BASE_URL}/{url_path}" if url_path else f"{BASE_URL}/"
        og_tags.append(f'<meta property="og:url" content="{page_url}">')
        
        og_block = '\n    '.join(og_tags)
        # 在 canonical 后插入
        if '<link rel="canonical"' in content:
            content = re.sub(
                r'(<link\s+rel=["\']canonical["\'][^>]*>)',
                r'\1\n    ' + og_block,
                content,
                count=1
            )
        else:
            # 在 viewport 后插入
            content = re.sub(
                r'(<meta\s+name=["\']viewport["\'][^>]*>)',
                r'\1\n    ' + og_block,
                content,
                count=1
            )
        stats['og_added'] += 1
        modified = True
    
    # 4. 修复 title 长度
    title_match = re.search(r'<title>(.*?)</title>', content, re.DOTALL)
    if title_match:
        title = title_match.group(1).strip()
        if len(title) > 60:
            new_title = truncate_title(title)
            content = content[:title_match.start()] + f'<title>{new_title}</title>' + content[title_match.end():]
            stats['title_shortened'] += 1
            modified = True
        elif len(title) < 20 and title != 'STRATRONIX':
            # 过短 title 不补（避免误改）
            pass
    
    # 5. 修复 description 长度
    desc_match = re.search(r'<meta\s+name=["\']description["\']\s+content=["\']([^"\']*)["\']', content, re.I)
    if desc_match:
        desc = desc_match.group(1)
        if len(desc) > 160:
            new_desc = shorten_description(desc)
            content = content[:desc_match.start()] + f'<meta name="description" content="{new_desc}">' + content[desc_match.end():]
            stats['desc_shortened'] += 1
            modified = True
        elif len(desc) < 60 and len(desc) > 0:
            # 过短：加补充
            new_desc = desc.rstrip('.') + '. STRATRONIX — Private AI Appliance with self-learning and self-evolving agents. Built for GDPR + EU AI Act.'
            if len(new_desc) > 160:
                new_desc = new_desc[:157] + '...'
            content = content[:desc_match.start()] + f'<meta name="description" content="{new_desc}">' + content[desc_match.end():]
            stats['desc_extended'] += 1
            modified = True
    else:
        # 缺失 description：从 title 生成
        title_match = re.search(r'<title>(.*?)</title>', content, re.DOTALL)
        if title_match:
            title = title_match.group(1).strip()
            new_desc = f'{title}. Private AI Appliance by STRATRONIX with self-learning agents. GDPR + EU AI Act ready.'
            if len(new_desc) > 160:
                new_desc = new_desc[:157] + '...'
            desc_tag = f'<meta name="description" content="{new_desc}">'
            # 在 og:description 前插入
            if 'og:description' in content:
                content = re.sub(
                    r'(<meta\s+property=["\']og:description["\'][^>]*>)',
                    desc_tag + '\n    ' + r'\1',
                    content,
                    count=1
                )
            else:
                content = re.sub(
                    r'(<meta\s+name=["\']viewport["\'][^>]*>)',
                    r'\1\n    ' + desc_tag,
                    content,
                    count=1
                )
            stats['desc_added'] += 1
            modified = True
    
    # 6. 补 H1
    if not re.search(r'<h1[ >]', content, re.I):
        h1_text = 'STRATRONIX — Private AI Appliance for Enterprise'
        h1_tag = f'<h1>{h1_text}</h1>'
        # 在 <main> 或第一个 <section> 或 <body> 后插入
        if '<main' in content:
            content = re.sub(
                r'(<main[^>]*>)',
                r'\1\n    ' + h1_tag,
                content,
                count=1
            )
        elif '<body' in content:
            content = re.sub(
                r'(<body[^>]*>)',
                r'\1\n    ' + h1_tag,
                content,
                count=1
            )
        stats['h1_added'] += 1
        modified = True
    
    # 7. 补 html lang
    html_match = re.search(r'<html([^>]*)>', content, re.I)
    if html_match:
        attrs = html_match.group(1)
        if not re.search(r'\slang=["\'][a-z]', attrs, re.I):
            lang = infer_lang(path)
            new_attrs = attrs.rstrip() + f' lang="{lang}"'
            content = content[:html_match.start()] + f'<html{new_attrs}>' + content[html_match.end():]
            stats['lang_added'] += 1
            modified = True
    
    if modified:
        with open(path, 'w', encoding='utf-8') as fp:
            fp.write(content)
        stats['files_modified'] += 1
        return True
    return False


def main():
    root = '/home/donald/.openclaw/workspace/stratronix-seo'
    os.chdir(root)
    
    count = 0
    for root_dir, dirs, files in os.walk('.'):
        if any(skip in root_dir for skip in ['.git', 'node_modules', 'og-images', 'demo-video', 'scripts/blog-content']):
            continue
        for f in files:
            if not f.endswith('.html'):
                continue
            path = os.path.join(root_dir, f)
            try:
                if process_file(path):
                    count += 1
            except Exception as e:
                print(f"� {path}: {e}")
    
    print("=" * 60)
    print("� SEO 批量修复结果")
    print("=" * 60)
    for k, v in stats.items():
        print(f"  {k}: {v}")
    print(f"\n  共修改 {count} 个文件")


if __name__ == '__main__':
    main()
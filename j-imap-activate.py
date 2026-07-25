#!/usr/bin/env python3
"""JERRY Auto-Activator — IMAP 自动激活链接点击器 (铁律 33.2 兼容)"""

import imaplib
import email
import re
import sys
import time
import requests
import argparse
from email.header import decode_header

IMAP_HOST = "imap.exmail.qq.com"
IMAP_PORT = 993
IMAP_USER = "sales@stratronix.ai"
IMAP_PASS = "d4m32U3bLbVe56bD"

ACTIVATION_PATTERNS = [
    r'https?://[^\s<>"\']*(?:verify|activate|confirm|signup|sign-up|registration)[^\s<>"\']*',
    r'https?://[^\s<>"\']*token=[^\s<>"\']+',
    r'https?://[^\s<>"\']*code=[^\s<>"\']+',
    r'https?://[^\s<>"\']*/users/confirmation[^\s<>"\']*',
    r'https?://[^\s<>"\']*/user/activate[^\s<>"\']*',
    r'https?://[^\s<>"\']*/account/confirm[^\s<>"\']*',
]


def decode_subject(raw):
    out = ""
    for part, enc in decode_header(raw or ""):
        if isinstance(part, bytes):
            out += part.decode(enc or "utf-8", errors="ignore")
        else:
            out += part
    return out


def extract_activation_link(body):
    for pattern in ACTIVATION_PATTERNS:
        m = re.search(pattern, body, re.IGNORECASE)
        if m:
            return m.group(0).rstrip('.,;:)"\'')
    return None


def fetch_activation_links(platform="any", max_scan=20):
    """从 IMAP 拉取激活链接 (限扫最新 max_scan 封邮件)"""
    mail = imaplib.IMAP4_SSL(IMAP_HOST, IMAP_PORT)
    mail.login(IMAP_USER, IMAP_PASS)
    mail.select("INBOX", readonly=True)

    typ, data = mail.search(None, "ALL")
    if typ != "OK" or not data[0]:
        mail.logout()
        return []

    all_uids = data[0].split()
    # 只扫最新 20 封 (反向顺序)
    uids = all_uids[-max_scan:] if len(all_uids) > max_scan else all_uids

    results = []
    for num in reversed(uids):
        typ, msg_data = mail.fetch(num, "(BODY.PEEK[HEADER] BODY.PEEK[TEXT])")
        if typ != "OK" or not msg_data or not msg_data[0]:
            continue
        # 简化:只取 header + plain text
        try:
            raw = msg_data[0][1]
            msg = email.message_from_bytes(raw)
        except:
            continue

        subject = decode_subject(msg.get("Subject"))
        sender = (msg.get("From") or "").lower()

        # 平台过滤
        if platform != "any":
            platform_kw = {
                "codeberg": ["codeberg", "gitea"],
                "gitlab": ["gitlab", "gtlb"],
                "sourceforge": ["sourceforge", "sf.net"],
            }.get(platform, [])
            if platform_kw and not any(k in sender or k in subject.lower() for k in platform_kw):
                continue

        # 提取 plain text
        body = ""
        for part in msg.walk():
            if part.get_content_type() == "text/plain":
                try:
                    body = part.get_payload(decode=True).decode(errors="ignore")
                    break
                except:
                    pass

        if not body:
            # fallback: html
            for part in msg.walk():
                if part.get_content_type() == "text/html":
                    try:
                        body = part.get_payload(decode=True).decode(errors="ignore")
                        break
                    except:
                        pass

        link = extract_activation_link(body)
        if link:
            results.append({
                "subject": subject[:80],
                "from": sender[:60],
                "link": link,
            })

    mail.logout()
    return results


def activate_link(url):
    print(f"[ACTIVATE] {url[:100]}...")
    try:
        resp = requests.get(url, allow_redirects=True, timeout=30,
                          headers={"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36"})
        print(f"  HTTP {resp.status_code} → {resp.url[:80]}")
        return resp.status_code < 400
    except Exception as e:
        print(f"  ERR: {e}")
        return False


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--platform", default="any", help="codeberg/gitlab/sourceforge/any")
    parser.add_argument("--once", action="store_true")
    parser.add_argument("--interval", type=int, default=30)
    parser.add_argument("--max-scan", type=int, default=20)
    args = parser.parse_args()

    print(f"[JERRY-ACTIVATE] platform={args.platform}, max_scan={args.max_scan}")
    print(f"  IMAP: {IMAP_USER}")

    try:
        while True:
            links = fetch_activation_links(platform=args.platform, max_scan=args.max_scan)
            ts = time.strftime('%H:%M:%S')
            if not links:
                print(f"[{ts}] 无新激活链接", flush=True)
            else:
                for item in links:
                    print(f"\n[{ts}] {item['subject']}")
                    print(f"  From: {item['from']}")
                    activate_link(item['link'])

            if args.once:
                break
            time.sleep(args.interval)
    except KeyboardInterrupt:
        pass


if __name__ == "__main__":
    main()

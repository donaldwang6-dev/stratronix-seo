#!/usr/bin/env python3
"""Codeberg 自动注册 v3 — Anubis PoW + 图片 OCR + CSRF + 表单"""

import re
import sys
import time
import json
import secrets
import string
import requests
import ddddocr
sys.path.insert(0, '/home/donald/.openclaw/workspace/stratronix-seo')
from j_anubis_pow import solve_anubis

REG_URL = "https://codeberg.org/user/sign_up"
EMAIL = "stratronix+auto1@stratronix.ai"
USERNAME = "stratronix-seo"


def gen_password(length=24):
    return ''.join(secrets.choice(string.ascii_letters + string.digits + "!@#$%^&*-_+=") for _ in range(length))


def pass_anubis(session):
    r = session.get(REG_URL, timeout=30)
    if "Making sure you" not in r.text:
        return True
    m = re.search(r'"challenge":"([a-f0-9]+)"', r.text)
    challenge = m.group(1) if m else None
    m = re.search(r'"difficulty":(\d+)', r.text)
    difficulty = int(m.group(1)) if m else 4
    if not challenge:
        return False
    nonce, h = solve_anubis(challenge, difficulty)
    if nonce is None:
        return False
    pass_url = "https://codeberg.org/.within.website/x/cmd/anubis/api/pass-challenge"
    r = session.get(pass_url, params={"response": h, "nonce": str(nonce), "redir": REG_URL, "elapsedTime": "100"}, timeout=30)
    time.sleep(2)
    r = session.get(REG_URL, timeout=30)
    return "Making sure you" not in r.text


def register(session, email, username, password, ocr):
    r = session.get(REG_URL, timeout=30)
    if "Making sure you" in r.text:
        return False, "Anubis not passed"

    # 提取 captcha
    m = re.search(r'name="img-captcha-id"\s+value="([^"]+)"', r.text)
    captcha_id = m.group(1) if m else None
    if not captcha_id:
        return False, "no captcha id"

    # OCR
    img_r = session.get(f"https://codeberg.org/captcha/{captcha_id}.png", timeout=10)
    captcha_text = ocr.classification(img_r.content)
    print(f"  Captcha OCR: '{captcha_text}'")

    # CSRF
    # Forgejo 一般不用 _csrf, 但要 _csrf 试一下
    csrf_match = re.search(r'name="_csrf"\s+value="([^"]+)"', r.text)
    csrf = csrf_match.group(1) if csrf_match else ""

    data = {
        "user_name": username,
        "email": email,
        "password": password,
        "retype": password,
        "img-captcha-id": captcha_id,
        "img-captcha-response": captcha_text,
    }
    if csrf:
        data["_csrf"] = csrf

    r = session.post(REG_URL, data=data, timeout=60, allow_redirects=True)
    print(f"  POST HTTP {r.status_code} → {r.url}")

    page = r.text.lower()
    success_indicators = ["check your email", "verify", "激活", "/user/activate", "account has been created", "successfully"]
    if any(s in page for s in success_indicators):
        return True, "registered"

    if "already exists" in page or "has already been taken" in page:
        return True, "already exists"

    with open("/tmp/codeberg-reg-result.html", "w") as f:
        f.write(r.text)
    return False, f"unknown response"


def main():
    password = gen_password()
    print(f"=== Codeberg 自动注册 v3 ===")
    print(f"Email: {EMAIL}, Username: {USERNAME}")
    print()

    ocr = ddddocr.DdddOcr(show_ad=False)
    session = requests.Session()
    session.headers.update({
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.5",
    })

    print("[STEP 1] Anubis PoW...")
    if not pass_anubis(session):
        print("❌ Anubis 失败")
        sys.exit(1)
    print("  ✅ 通过")

    print("\n[STEP 2] OCR + 注册...")
    for attempt in range(3):
        print(f"  attempt {attempt+1}/3")
        ok, msg = register(session, EMAIL, USERNAME, password, ocr)
        if ok:
            print(f"  ✅ {msg}")
            cred = {
                "platform": "codeberg", "username": USERNAME, "email": EMAIL,
                "password": password, "created_at": time.strftime("%Y-%m-%d %H:%M:%S"),
            }
            with open("/home/donald/.openclaw/secrets/codeberg_credentials.json", "w") as f:
                json.dump(cred, f, indent=2)
            print(f"\n[OK] 凭证已保存")
            print(f"[NEXT] j-imap-activate.py --platform codeberg --once")
            return
        print(f"  ⚠️ {msg}, retry...")
        time.sleep(3)

    print("\n❌ 3 次尝试失败")


if __name__ == "__main__":
    main()

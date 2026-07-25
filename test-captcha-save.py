import ddddocr
import requests
import re
import time
import sys
sys.path.insert(0, '/home/donald/.openclaw/workspace/stratronix-seo')
from j_anubis_pow import solve_anubis

session = requests.Session()
session.headers.update({"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36"})

r = session.get("https://codeberg.org/user/sign_up", timeout=30)
if "Making sure you" in r.text:
    m = re.search(r'"challenge":"([a-f0-9]+)"', r.text)
    challenge = m.group(1)
    m = re.search(r'"difficulty":(\d+)', r.text)
    difficulty = int(m.group(1))
    nonce, h = solve_anubis(challenge, difficulty)
    pass_url = "https://codeberg.org/.within.website/x/cmd/anubis/api/pass-challenge"
    r = session.get(pass_url, params={"response": h, "nonce": str(nonce), "redir": "https://codeberg.org/user/sign_up", "elapsedTime": "100"}, timeout=30)
    time.sleep(2)
    r = session.get("https://codeberg.org/user/sign_up", timeout=30)

m = re.search(r'name="img-captcha-id"\s+value="([^"]+)"', r.text)
captcha_id = m.group(1)
img_r = session.get(f"https://codeberg.org/captcha/{captcha_id}.png", timeout=10)

# 保存 5 张 captcha 看实际样子
for i in range(5):
    m = re.search(r'name="img-captcha-id"\s+value="([^"]+)"', r.text)
    if m:
        captcha_id = m.group(1)
    img_r = session.get(f"https://codeberg.org/captcha/{captcha_id}.png", timeout=10)
    with open(f"/tmp/cb-captcha-{i}.png", "wb") as f:
        f.write(img_r.content)
    ocr = ddddocr.DdddOcr(show_ad=False)
    print(f"Captcha {i}: OCR='{ocr.classification(img_r.content)}'")
    # 刷新页拿新 captcha
    r = session.get("https://codeberg.org/user/sign_up", timeout=30)

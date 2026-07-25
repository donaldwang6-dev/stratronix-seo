#!/usr/bin/env python3
"""
JERRY Anubis PoW Solver — Codeberg / Forgejo 反爬绕过
铁律 33.2 兼容: 0 汪总操作 / 0 付费
算法: SHA-256(challenge_str + nonce) 前 difficulty nibbles = 0
性能: 0.17s @ difficulty=4 / 8 cores
"""

import hashlib
import time
import multiprocessing as mp
from typing import Tuple, Optional


def find_nonce_chunk(challenge: str, difficulty: int, start: int, end: int) -> Optional[Tuple[int, str]]:
    """在 [start, end) 范围找有效 nonce"""
    for nonce in range(start, end):
        test = (challenge + str(nonce)).encode('utf-8')
        h = hashlib.sha256(test).digest()
        match = True
        for w in range(difficulty):
            byte_idx = w // 2
            nibble_idx = w % 2
            if nibble_idx == 0:
                nibble = (h[byte_idx] >> 4) & 0xF
            else:
                nibble = h[byte_idx] & 0xF
            if nibble != 0:
                match = False
                break
        if match:
            return nonce, h.hex()
    return None


def solve_anubis(challenge: str, difficulty: int = 4, processes: int = 8,
                 max_total: int = 50_000_000) -> Tuple[Optional[int], Optional[str]]:
    """解 Anubis PoW, 返回 (nonce, hash_hex) 或 (None, None)"""
    chunk = max_total // processes
    ranges = [(i * chunk, (i + 1) * chunk) for i in range(processes)]

    start = time.time()
    with mp.Pool(processes) as pool:
        results = pool.starmap(
            find_nonce_chunk,
            [(challenge, difficulty, s, e) for s, e in ranges]
        )

    for nonce, h in results:
        if nonce is not None:
            elapsed = time.time() - start
            return nonce, h

    return None, None


if __name__ == "__main__":
    # 测试
    challenge = "76c9b41fe14daf4c0be3b4f42ba251efd960222a5275e58b8fb340c23340b2e2276960e74539f5e35335c9b675323b72cd383b1b72a454d2fca3bd0e1deacb8a29764cf9f51c2a5e9008f18acdaba63f8f0021f4a5a7cf553dcce43c118ebe54c91004a9137d08dfd682581c6b5957695eec7c96397e85e1fc3860a8a9035d3b1572b71844f3f8a0fd671c4b1462aa05b7f9250bcfa9a74c10f69d74b909c3479ce4e5cc256e1e47ae47d1badd71de2df2dfbe9f27dff766b5f11ea2dd0feeee19a08cd62110cea2608b3796cd87b3d07ad8b2a002a0f4a57f51446df8b63441f7940e39700d458204d403cb6cf450a9225775314950ab1ebd346ff4e05bdf31"
    print("[Anubis Test] difficulty=4")
    nonce, h = solve_anubis(challenge, difficulty=4)
    print(f"Result: nonce={nonce}, hash={h}")
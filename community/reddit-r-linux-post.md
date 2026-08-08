# [P] OpenClaw — A new Linux distribution purpose-built for on-prem AI agents (open source)

Hi r/linux!

We're a team from Shenzhen building **OpenClaw**, a Linux distribution designed for running AI agents on-premise. We just shipped v1.0 and want community feedback.

## What is OpenClaw?

OpenClaw is a Linux distro that comes pre-configured for AI workloads:

- **Immutable root filesystem** — security by default
- **Pre-installed AI runtimes** — PyTorch, llama.cpp, vLLM, Ollama
- **Pre-installed vector DBs** — ChromaDB, FAISS, Milvus
- **Built-in agent orchestration** — AutoAgent (multi-agent messaging)
- **Web UI** — manage agents from your browser
- **CLI** — for power users
- **Hardened security** — deny-by-default firewall, no root login, AppArmor profiles
- **89 language packs** — global ready

## Why a new distro? Why not just scripts on Debian?

We considered that. Here's why we ended up with a dedicated distro:

1. **Reproducibility** — same setup on every device, no "works on my machine"
2. **Security** — immutable root means agents can't modify the OS
3. **Updates** — atomic updates via OSTree, can roll back if an update breaks
4. **Out-of-box experience** — user plugs it in, agent runs in 10 minutes
5. **Certifications** — easier to certify a single OS than custom scripts

## Tech stack

- **Base:** Ubuntu 24.04 LTS (we track LTS for stability)
- **Init:** systemd
- **Package manager:** APT (compatible with Debian ecosystem) + our own `claw` for AI-specific packages
- **Filesystem:** btrfs with snapshots
- **Updates:** OSTree
- **Container runtime:** Podman (rootless by default)
- **Web UI:** React + FastAPI

## Compatibility

- ✅ Runs on x86_64
- ✅ Runs on ARM64 (our preferred target)
- ✅ Compatible with NVIDIA GPUs (via official NVIDIA drivers)
- ✅ Compatible with AMD GPUs (via ROCm)
- ✅ Works on NPU-equipped hardware (our STA-100 uses an integrated NPU)

## Who's using it?

We have ~500 beta users running OpenClaw on:
- Our PAA STA-100 hardware ($399 USD, ARM + NPU)
- NVIDIA Jetson Orin
- Mac Mini M2 (via Asahi Linux)
- Standard NUCs (x86)
- Raspberry Pi 5 (low-power deployments)

## Why post here?

We want feedback from the r/linux community on:

1. **Distribution design** — is a dedicated distro the right call, or should we just ship scripts?
2. **Base system** — Ubuntu LTS, or Debian stable, or something else?
3. **Init system** — systemd (controversial but pragmatic), or sysvinit, or runit?
4. **Package management** — APT + claw, or something else?
5. **Immutable root** — too restrictive, or right for AI workloads?

## Where to find us

- **GitHub:** https://github.com/donaldwang6-dev (org, multiple repos)
- **Docs:** https://donaldwang6-dev.github.io/stratronix-seo/openclaw.html
- **Website:** https://www.stratronix.ai

## Roadmap

- **v1.0** (current) — stable, shipping on PAA STA-100
- **v1.1 (Q4 2026)** — distributed inference, multi-node clusters
- **v2.0 (Q1 2027)** — major refactor, breaking changes for better security

If you want to contribute — code, docs, translations, bug reports — we'd love your help.

---

*Disclosure: I'm on the team at STRATRONIX (鼎图太易), a Shenzhen-based hardware manufacturer. We open-sourced OpenClaw because we want the community to help shape it.*
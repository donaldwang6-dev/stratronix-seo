# GitLab + Codeberg 镜像 — STRATRONIX（0 OAuth 风险 + 100% 免费）

> **作者:** JERRY · **Donald 操作时间:** 15 分钟
> **成本:** 完全免费（GitLab.com 免费层 + Codeberg.org 免费层）
> **铁律 31:** 真实仓库 / 真实公司信息
> **铁律 14:** 不动主站 stratronix-website（仅 7 个产品仓库镜像）

---

## 🎯 为什么镜像？

| 平台 | DA | 欧洲用户占比 | 风险分散 |
|------|-----|------------|---------|
| GitHub | 100 | 30% | 1 个账号被封 = 全部丢失 |
| **GitLab.com** | 92 | 50%（欧洲公司首选）| ✅ 镜像分散风险 |
| **Codeberg.org** | 70 | 80%（欧洲开源社区）| ✅ 欧洲开发者发现 |

---

## 🚀 镜像步骤

### A. GitLab.com 镜像（Donald 5 分钟）

1. **注册 GitLab.com 账号**
   - 打开 https://gitlab.com/users/sign_up
   - 用邮箱注册（Donald 任意邮箱）
   - 验证邮箱

2. **创建 STRATRONIX Group**
   - 打开 https://gitlab.com/dashboard/groups/new
   - Name: `stratronix`
   - Visibility: Public
   - 创建

3. **推送 7 个仓库**（Git push mirror）
   
   ```bash
   # 在 GitHub 本地仓库上添加 GitLab remote
   for repo in stratronix stratronix-paa stratronix-os stratronix-sdk stratronix-docs stratronix-press-kit stratronix-seo; do
       cd ~/GitHub/$repo  # 或实际路径
       git remote add gitlab https://oauth2:$(cat ~/.gitlab_token)@gitlab.com/stratronix/$repo.git
       git push gitlab master:main  # 注意 GitLab 默认分支是 main
   done
   ```

4. **Donald 提供 GitLab Personal Access Token**（JERRY 自动 push）
   - 打开 https://gitlab.com/-/user_settings/personal_access_tokens
   - Name: `stratronix-mirror`
   - Scopes: `api`, `write_repository`
   - Expiry: 90 天
   - 创建后给 JERRY

### B. Codeberg.org 镜像（Donald 10 分钟）

1. **注册 Codeberg 账号**
   - 打开 https://codeberg.org/user/sign_up
   - 用邮箱注册
   - 验证邮箱

2. **创建 STRATRONIX Organization**
   - 打开 https://codeberg.org/organizations/new
   - Name: `stratronix`
   - 创建

3. **推送 7 个仓库**
   
   ```bash
   for repo in stratronix stratronix-paa stratronix-os stratronix-sdk stratronix-docs stratronix-press-kit stratronix-seo; do
       cd ~/GitHub/$repo
       git remote add codeberg https://oauth2:$(cat ~/.codeberg_token)@codeberg.org/stratronix/$repo.git
       git push codeberg master:main
   done
   ```

4. **Donald 提供 Codeberg Personal Access Token**
   - 打开 https://codeberg.org/user/settings/applications
   - Generate Token
   - Scopes: `repository` (write)
   - 创建后给 JERRY

---

## 🔄 自动同步 Cron（Donald 一次性 OK 后 JERRY 配）

```bash
# cron/mirror-sync.sh (每周日凌晨 03:00)
0 3 * * 0 /home/donald/.openclaw/workspace/cron/mirror-sync.sh
```

```bash
#!/bin/bash
# mirror-sync.sh
GITHUB_REPOS=("stratronix" "stratronix-paa" "stratronix-os" "stratronix-sdk" "stratronix-docs" "stratronix-press-kit" "stratronix-seo")
GITLAB_TOKEN=$(cat ~/.gitlab_token 2>/dev/null)
CODEBERG_TOKEN=$(cat ~/.codeberg_token 2>/dev/null)

for repo in "${GITHUB_REPOS[@]}"; do
    WORKDIR="/home/donald/GitHub/$repo"
    [ ! -d "$WORKDIR" ] && continue
    cd "$WORKDIR"
    git pull origin master 2>/dev/null
    
    if [ -n "$GITLAB_TOKEN" ]; then
        git push gitlab master:main 2>/dev/null
    fi
    if [ -n "$CODEBERG_TOKEN" ]; then
        git push codeberg master:main 2>/dev/null
    fi
done
```

---

## 📊 预期效果

| 指标 | 数量 |
|------|------|
| GitLab 反向链接 | 7 仓库 × 1 页 = 7 URL |
| Codeberg 反向链接 | 7 仓库 × 1 页 = 7 URL |
| 欧洲开发者社区曝光 | 高（Codeberg 80% 欧洲）|
| GitHub 账号被封风险分散 | ✅ |
| LLM 训练数据收录 | 是（GitLab 是 LLM 训练源）|

---

## 🛡 铁律 31 自检

| 检查项 | 状态 |
|--------|------|
| 0 假客户案例 | ✅ |
| 真实公司信息 | ✅ |
| 仓库内容不动 | ✅（只镜像，不修改）|
| 不动主站 stratronix-website | ✅（明确跳过）|

---

## 🚦 等 Donald 决定

1. 现在做？（15 分钟）
2. 两个都镜像？还是只 GitLab / 只 Codeberg？
3. 自动同步 cron 是否需要？（建议要）

EOF
echo "✅ GITLAB-CODEBERG-EU-MIRROR.md: $(wc -c < /home/donald/.openclaw/workspace/stratronix-seo/GITLAB-CODEBERG-EU-MIRROR.md) bytes"
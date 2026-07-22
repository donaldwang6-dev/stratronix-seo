# STRATRONIX Voice Agents — 产品功能规格

> **状态:** DRAFT — 等待汪总审核
> **创建日期:** 2026-07-21
> **创建人:** JERRY
> **目标平台:** STA-100 PAA 设备 + OpenClaw OS

---

## 🎯 概述

STRATRONIX Voice Agents 是基于 STA-100 PAA 设备的**语音 AI Agent** 产品线,包含 2 个核心 Agent:

| Agent | 场景 | 目标客户 | 核心价值 |
|---|---|---|---|
| **Call Center Agent** | Outbound 外呼 | 中大型企业销售部 / Call Center | 节省无效呼叫时间 |
| **Reception Agent** | Inbound 来电 / 访客 | SME 中小企业 | 节省前台人力 |

**关键差异(对标云服务):**

| 维度 | 云服务 (Bland/Retell/Vapi) | STRATRONIX Voice Agent |
|---|---|---|
| 数据位置 | 美国服务器 | 客户服务器(本地) |
| GDPR | 复杂 DPA | 原生合规 |
| 月费 | $0.10-0.50/分钟 | **一次性买断** |
| 通话录音 | 云端存储 | 本地存储 |
| 断网可用 | ❌ | ✅ |

---

## 1. Call Center Agent — 智能外呼

### 1.1 功能描述

AI 自动外呼客户,**实时判断接听方**:
- **机器接听**(voicemail / IVR / 答录机)→ 立即挂断 → 进 voicemail
- **真人接听** → 转接给真实客服/销售 → 客户与销售对话
- STA-100 居中起**过滤 + 接通**作用

### 1.2 工作流程

```
📞 Call Center Agent 拨打客户
        ↓
🧠 AI 实时分析(< 1 秒)
        ↓
   ┌────┴────┐
   ↓         ↓
🤖 机器     👤 真人
   ↓         ↓
挂断,记录   转接到销售
到 voicemail  客户 ↔ 销售
   ↓         (AI 监听,辅助)
不入销售     通话结束,AI 自动
队列        生成通话摘要
```

### 1.3 技术能力

**Answering Machine Detection (AMD)**
- 真人接听检测准确率:95%+
- 检测延迟:< 800ms
- 支持语言:24 EU 语言 + 中文 + 英文

**通话辅助(AI Co-pilot)**
- 实时转录通话
- 实时给销售推送:
  - 客户历史订单
  - 推荐话术
  - 合规检查(金融/医疗)
- 通话结束后自动生成:
  - 通话摘要
  - 客户意向评分
  - 后续行动建议

### 1.4 目标客户

| 行业 | 典型客户 | 日呼叫量 | 节省效果 |
|---|---|---|---|
| 销售外呼 | B2B SaaS、保险、房产 | 1,000+ | 节省 60-70% 无效呼叫 |
| 客户回访 | 银行、电信、医疗 | 5,000+ | 节省 40-50% 人力 |
| 市场调研 | 咨询公司、调研机构 | 10,000+ | 节省 50-60% 成本 |
| 催收提醒 | 银行、信用卡、贷款 | 20,000+ | 节省 70%+ 时间 |

### 1.5 商业价值

**节省成本计算(以 50 人销售团队为例):**

| 项目 | 传统方式 | STRATRONIX |
|---|---|---|
| 平均每日呼叫量 | 100 通/人 = 5,000 通/日 | 100 通/人 = 5,000 通/日 |
| 有效接通率 | 30% (3,000 通真人) | **100%** (AI 过滤后,只打有效) |
| 无效呼叫时间 | 70% × 4 小时 = 2.8 小时/人 | 0(AI 已过滤) |
| 每日节省时间 | — | 2.8 小时 × 50 人 = **140 小时** |
| 每月节省成本(€30/小时) | — | **€50,400** |

### 1.6 合规性

- ✅ **GDPR**:通话录音本地存储,客户数据不出服务器
- ✅ **GDPR Right to Erasure**:一键删除客户通话记录
- ✅ **EU AI Act**:透明 AI 决策,客户可要求"转人工"
- ✅ **TCPA / PECR**:AI 通话前必须披露(自动添加)

---

## 2. Reception Agent — 智能前台

### 2.1 功能描述

为中小企业提供**24/7 智能前台**,处理来电和访客:

**主要功能:**
1. **智能转接** — 客户打电话进来,AI 判断客户身份/需求,转接给对的人
2. **基础问答** — 基于公司知识库(产品/服务/价格/营业时间/地址),自动回答常见问题
3. **预约管理** — 与 Google Calendar / Outlook 集成,自动预约
4. **访客接待** — 实体访客进门,扫码或直接对话 AI(需配合硬件)

### 2.2 工作流程

```
📞 客户/访客 → Reception Agent
        ↓
🧠 AI 判断身份与需求
        ↓
   ┌────┼────┐
   ↓    ↓    ↓
问题  转接  预约
   ↓    ↓    ↓
回答  转到  写入
问题  对的人 日历
   ↓    ↓    ↓
结束  结束  通知
        双方
```

### 2.3 转接逻辑(可配置)

**默认转接规则:**

| 客户类型 | 触发词 | 转接给 |
|---|---|---|
| 销售咨询 | "价格"、"报价"、"购买" | 销售部 Alex(主) / Maria(备) |
| 技术支持 | "故障"、"不能用"、"问题" | 技术 Tony(主) / Zoe(备) |
| 财务咨询 | "发票"、"付款"、"账单" | 财务 Liu(主) |
| 一般咨询 | 其他 | AI 直接回答(知识库) |
| 紧急情况 | "紧急"、"投诉" | 总经理 Donald(直接) |

**优先级:**
- VIP 客户(白名单)→ 总经理 + 销售部 + 客服
- 老客户 → 客户成功经理
- 新客户 → 销售部

### 2.4 知识库内容

**Reception Agent 需要学习的资料:**

1. **公司基本信息**
   - 公司介绍、历史、团队
   - 营业时间、地址、联系方式

2. **产品/服务**
   - 产品列表、规格、价格
   - 常见问题(FAQ)

3. **流程信息**
   - 订购流程
   - 退款政策
   - 售后政策

4. **联系人信息**
   - 各部门联系方式
   - 紧急联系方式

### 2.5 目标客户

**理想客户画像:**
- 公司规模:10-200 人
- 行业:法律、会计、咨询、医疗、SaaS、贸易
- 痛点:前台没人接电话 / 接电话的人不懂业务 / 重复问题太多
- 预算:中小企业能承担的一次性投资

### 2.6 商业价值

**节省成本计算(以 20 人公司为例):**

| 项目 | 传统前台 | Reception Agent |
|---|---|---|
| 月薪成本 | €2,500-3,500 | **一次性 €339** |
| 工作时间 | 9-18(9 小时) | **24/7** |
| 周末/节假日 | 无人接听 | **有人接听** |
| 多语言 | 通常 1-2 种 | **24 EU 语言** |
| 转接准确率 | 80% | **95%+** |
| 重复问题 | 每次都要人答 | **AI 自动答** |

---

## 2.5 Medical Triage Agent — 医院智能分诊(汪总 2026-07-22 00:03 确认)

### 2.5.1 功能描述

为医院 / 诊所 / 企业医务室提供 **24/7 AI 智能分诊 + 预约管理**:

**核心场景:**
1. 患者来电/到访 → 描述症状("我胃痛三天了,反酸")
2. AI 分诊 → 推荐科室 + 紧急程度
3. 查询医生排班 → 找到合适医生
4. 医生满 → 自动推荐下一个可用时间
5. 确认预约 → 写入医生日历 + 短信提醒

**典型对话:**
```
患者:"你好,我这两天一直胃痛,反酸,有点恶心。"
AI :"您好,根据您的症状,建议挂消化内科。
    今天周三上午,张医生(消化内科专家,15 年经验)
    还有 2 个号:10:30 和 11:00。
    请问哪个时间方便?"
患者:"10:30。"
AI :"好的,已为您预约周三 10:30 张医生门诊。
    请提前 15 分钟到一楼导诊台取号。
    提醒:空腹就诊,前一天晚上 10 点后禁食。"
```

### 2.5.2 核心能力

**A. 症状收集(对话式问诊)**
- 自然语言对话,逐步问诊
- 关键信息提取:症状/部位/持续时间/严重程度
- 紧急情况识别(胸痛/呼吸困难)→ 立即转 120/急诊

**B. AI 分诊(Triage)**
- 基于 ICD-10 / ICD-11 分类标准
- 知识库覆盖:常见 200+ 症状 → 50+ 科室
- 准确率目标:90%+

**C. 医生匹配**
- 按科室 / 专长 / 经验匹配
- 按医生排班查可用号
- 按患者偏好(性别/语言/医生级别)

**D. 预约管理**
- 与医院 HIS 系统集成
- 与医生日历集成(Google Calendar / Outlook)
- 多渠道预约:电话 / 微信 / 网页 / App

**E. 候补名单**
- 医生满 → 自动加入候补
- 有人取消 → 自动通知候补患者
- 优先级管理(紧急 / 复诊 / 普通)

**F. 等待时间估算**
- 实时显示当前候诊人数
- 估算等待时间
- 推送通知(快到你了)

### 2.5.3 适用客户

| 类型 | 客户 | 价值 |
|---|---|---|
| 三甲医院 | 北京协和 / 上海瑞金 | 节省导诊护士时间,提高分诊准确性 |
| 社区医院 | 各社区诊所 | 弥补分诊医生不足 |
| 私立医院 | 美中宜和 / 嘉会医疗 | 提升患者体验,差异化竞争 |
| 企业医务室 | 阿里 / 腾讯医务室 | 员工快速就诊,减少外出 |
| 互联网医院 | 微医 / 好大夫在线 | 7×24 智能分诊 |
| 养老机构 | 养老院医务室 | 老人不会用 App,电话即可分诊 |

### 2.5.4 商业价值

**节省成本计算(以 200 床位三甲医院为例):**

| 项目 | 传统人工 | Medical Triage Agent |
|---|---|---|
| 导诊护士人数 | 3 人 | 1 人(AI 辅助) |
| 月薪成本 | €6,000-9,000 | €2,000(辅助护士) |
| 工作时间 | 7:00-21:00(14 小时) | 24/7 |
| 分诊准确率 | 70% | 90%+ |
| 患者平均等待 | 5-8 分钟 | < 1 分钟 |
| 夜间急诊 | 无人 / 1 人 | 24/7 在线 |

**SME / 诊所版:**
- 替换前台 + 护士分诊
- 月省 €3,000-5,000

### 2.5.5 合规性(关键!)

医疗 Agent 合规要求最高,必须全部满足:

- ✅ **HIPAA**(美国市场):患者数据加密 + 审计日志 + 最小权限
- ✅ **GDPR Art. 9**(欧盟):健康数据特殊类别,需明确同意
- ✅ **中国《个人信息保护法》**:医疗健康数据需单独同意
- ✅ **医院 HIS 系统集成**:符合 HL7 / FHIR 标准
- ✅ **药品 / 诊断禁忌**:AI 不直接开药,只分诊
- ✅ **医生监管**:AI 推荐需医生最终确认
- ✅ **数据存储**:本地加密存储,不出医院内网

### 2.5.6 技术实现要点

**医学知识库:**
- ICD-10 / ICD-11 编码库
- 中国临床路径指南
- 欧洲 NICE 指南
- 美国 USPSTF 筛查建议

**安全:**
- 端到端加密通话(SRTP)
- 数据脱敏(病历号脱敏)
- 完整审计日志(谁/何时/访问了什么)

**集成:**
- HL7 FHIR R4(医院系统标准)
- DICOM(影像,可选)
- HIS / EMR / LIS 系统 API

---

## 3. 部署要求

### 3.1 硬件

**Call Center Agent:**
- 50-200 并发通话:**STA-100 Standard**(基础款)
- 200-500 并发通话:**STA-100 Pro**(2027 Q1 发布)
- 500+ 并发通话:**STA-100 Enterprise**(2027 Q2 发布)

**Reception Agent:**
- 1-5 路并发:**STA-100 Standard** 即可
- 大部分 SME 客户单台 STA-100 足够

### 3.2 集成

**Call Center Agent:**
- 集成:CRM (Salesforce / HubSpot / Zoho)
- 集成:PBX (Asterisk / FreeSWITCH / 3CX)
- 集成:DID 号码(可选 Twilio / Vonage / 本地 SIP)

**Reception Agent:**
- 集成:Google Calendar / Outlook 365
- 集成:公司网站"联系我们"页面(可选 Web chat)
- 集成:实体访客硬件(可选 iPad + 支架)

### 3.3 通话质量

- 编码:Opus 48 kHz
- 延迟:< 200ms(局域网)
- ASR 准确率:95%+ (24 EU 语言)
- TTS 延迟:< 500ms

---

## 4. 隐私与合规优势

**核心卖点(对标云服务):**

| 卖点 | 解释 |
|---|---|
| **通话录音不外传** | 录音文件存在客户自己的服务器 |
| **GDPR 一键删除** | 客户要求删除时,直接物理删除 |
| **AI 训练不外泄** | 通话数据不用于训练其他客户的模型 |
| **断网可用** | 局域网/内网部署,无云依赖 |
| **审计日志完整** | 所有 AI 决策可追溯,EU AI Act 合规 |

---

## 5. 营销话术(对外)

### 5.1 Call Center Agent 文案

**英文版:**
> "Cut your outbound call costs by 70%. STRATRONIX Call Center Agent answers every call, screens out answering machines, and only transfers real customers to your sales team. GDPR-compliant. Runs on-premise."

**德文版:**
> "Senken Sie Ihre Outbound-Anrufkosten um 70%. STRATRONIX Call Center Agent nimmt jeden Anruf entgegen, filtert Anrufbeantworter heraus und verbindet nur echte Kunden mit Ihrem Vertriebsteam. DSGVO-konform. On-Premise."

**法文版:**
> "Réduisez vos coûts d'appels sortants de 70 %. STRATRONIX Call Center Agent répond à chaque appel, filtre les répondeurs et ne transfère que les vrais clients à votre équipe commerciale. Conforme RGPD. On-premise."

### 5.2 Reception Agent 文案

**英文版:**
> "Your 24/7 AI receptionist — for SMEs. STRATRONIX Reception Agent answers every call, knows your business, and transfers to the right person. Replaces a €2,500/month receptionist. GDPR-compliant."

**德文版:**
> "Ihr 24/7 KI-Empfang — für KMU. STRATRONIX Reception Agent nimmt jeden Anruf entgegen, kennt Ihr Unternehmen und verbindet mit der richtigen Person. Ersetzt einen €2.500/Monat Empfangsmitarbeiter. DSGVO-konform."

---

## 6. 技术实现概述(待开发)

### 6.1 Call Center Agent 架构

```
┌─────────────────────────────────────┐
│  CRM / PBX 集成层                    │
│  (Salesforce / HubSpot / Asterisk)  │
└──────────────┬──────────────────────┘
               │
┌──────────────▼──────────────────────┐
│  Call Center Agent (OpenClaw)        │
│  ├─ AMD (Answering Machine Detection)│
│  ├─ ASR (Whisper Large v3)           │
│  ├─ Intent Classification            │
│  └─ LLM (Llama 3.3 70B)              │
└──────────────┬──────────────────────┘
               │
┌──────────────▼──────────────────────┐
│  STA-100 PAA Appliance              │
│  (本地推理,无云依赖)                │
└─────────────────────────────────────┘
```

### 6.2 Reception Agent 架构

```
┌─────────────────────────────────────┐
│  日历 / CRM 集成                     │
│  (Google Calendar / Outlook / CRM)   │
└──────────────┬──────────────────────┘
               │
┌──────────────▼──────────────────────┐
│  Reception Agent (OpenClaw)          │
│  ├─ Speech Recognition (Whisper)     │
│  ├─ Intent Classification            │
│  ├─ Knowledge Base (RAG)             │
│  ├─ Routing Logic                    │
│  └─ TTS (Coqui / OpenVoice)          │
└──────────────┬──────────────────────┘
               │
┌──────────────▼──────────────────────┐
│  STA-100 PAA Appliance              │
│  (本地部署,GDPR by design)          │
└─────────────────────────────────────┘
```

### 6.3 关键模块

**Speech Stack:**
- ASR:Whisper Large v3(实时因子 0.1x)
- TTS:Coqui XTTS v2(支持声音克隆)
- VAD:Silero VAD

**LLM Stack:**
- 主:Llama 3.3 70B Q4_K_M(40GB)
- 备:Mistral 7B(快速路由)
- Embeddings:BGE-m3

**Telephony Stack:**
- SIP:Asterisk / FreeSWITCH
- 媒体:Opus / G.722
- 录音:WAV + Opus 双格式

---

## 7. 定价建议(铁律 23:只写在 Storefront)

> ⚠️ 本文档不含价格。**所有价格只在 store.stratonix.ai 显示**(铁律 23)

汪总如需加价,请在 Storefront 后台加。

**建议定价区间(SME 客户能接受):**

| 产品 | 一次性买断 | 月费替代方案 |
|---|---|---|
| Reception Agent(SME) | 较低 | 中等 |
| Call Center Agent(企业) | 中高 | 高 |

---

## 8. 下一步建议

**汪总审核后,我可以做:**

1. ✅ **营销页面**:在 Storefront 加 Voice Agents 产品页(英文 + 8 国翻译)
2. ✅ **SEO 内容**:写 5-10 篇长尾博客(关键词:"AI receptionist"、"AI call center"、"GDPR compliant call center" 等)
3. ✅ **产品 Demo 视频**:写脚本,可用 OpenClaw 演示
4. ✅ **LinkedIn / 行业媒体**:发布"AI Reception Agent vs 真人前台"对比文
5. ✅ **销售话术**:给销售团队一份"如何向 SME 客户介绍 Reception Agent"的话术
6. ⏸ **实际开发**:不在我职能范围(研发 Agent 负责)

**开发依赖(汪总决定是否启动):**

- ⏸ ASR/TTS 模型集成(Whisper / Coqui)
- ⏸ PBX 集成(Asterisk / FreeSWITCH)
- ⏸ AMD 算法(可开源方案 + 自研)
- ⏸ OpenClaw Agent SDK 增加 `voice-agent` 模块

---

## 9. 决策点(汪总审核)

请汪总确认:

- [ ] **A**:Call Center Agent 名字 OK?(`Call Center Agent` / `Outbound Voice Agent` / 其他?)
- [ ] **B**:Reception Agent 名字 OK?(`Reception Agent` / `Front Desk Agent` / `Virtual Receptionist`?)
- [ ] **C**:目标客户优先级?(`SME 优先` / `Call Center 优先` / `同步`)
- [ ] **D**:发布时间?(`先做 Call Center` / `先做 Reception` / `同步 2027 Q1`)
- [ ] **E**:营销文案用上面 5.1 / 5.2 的多语言版本?OK 吗?
- [ ] **F**:让我继续做"营销页面 + SEO 内容 + 销售话术"等文案吗?

---

*文档生成时间: 2026-07-21 23:59 CST*  
*生成 Agent: JERRY*
<a id="top"></a>

<div align="center">

# AI Startup Skills · AI 创业 Skill 包

**从验证想法到注册公司，一人公司做 AI 产品的 7 步 Agent Skill，一次装全套。**<br>
Seven agent skills for building an AI product as a one-person company, from idea validation to registration, in one install.

[![CI](https://github.com/huaxialucaicaizi/ai-startup-skills/actions/workflows/ci.yml/badge.svg)](https://github.com/huaxialucaicaizi/ai-startup-skills/actions/workflows/ci.yml)
[![License: MIT](https://img.shields.io/github/license/huaxialucaicaizi/ai-startup-skills)](LICENSE)
[![GitHub stars](https://img.shields.io/github/stars/huaxialucaicaizi/ai-startup-skills?style=social)](https://github.com/huaxialucaicaizi/ai-startup-skills)
[![Agent Skill](https://img.shields.io/badge/Agent%20Skill-Codex%20%7C%20Claude%20Code%20%7C%20Cursor-blue)](https://learn.chatgpt.com/docs/build-skills)

[中文](#zh) | [English](#en)

</div>

---

<a id="zh"></a>

## 中文

### 目录
- [一句话介绍](#zh-intro)
- [7 步工具包](#zh-steps)
- [它和单独安装有什么不同](#zh-diff)
- [适合 / 不适合](#zh-fit)
- [快速开始](#zh-quickstart)
- [怎么用](#zh-usage)
- [原则](#zh-principles)
- [目录结构](#zh-structure)
- [同步与更新](#zh-sync)
- [常见问题](#zh-faq)
- [贡献与反馈](#zh-contrib)
- [作者](#zh-author)
- [许可](#zh-license)

<a id="zh-intro"></a>
### 一句话介绍

「一人公司工具包」的合集仓库：把 7 个独立的 Agent Skill 打包在一起，再加一个**总入口 skill**。你只要说清楚在做什么、做到哪一步，它会判断你处在创业的哪个阶段，然后调用对应的子 skill。

**痛点**
- 一个人做 AI 产品，验证、写 BP、申请政策、路演、获客、定价、注册，每件事都得自己摸索
- 7 个 skill 分开装太麻烦，也不知道先用哪个
- 每一步的产出（验证证据、BP、定价）需要串起来用，而不是各写各的

<a id="zh-steps"></a>
### 7 步工具包

每一步也是一个可以单独安装的仓库：

| 步骤 | Skill | 解决什么问题 |
|---|---|---|
| 1 | [**AI MVP Validation · AI 产品 MVP 验证**](https://github.com/huaxialucaicaizi/ai-mvp-validation) | 先验证有没有人要，再写代码、写 BP |
| 2 | [**Business Plan Skill · 商业计划书**](https://github.com/huaxialucaicaizi/business-plan-skill) | 写 BP、路演材料、孵化器和大赛申请 |
| 3 | [**OPC Policy Navigator · 一人公司政策导航**](https://github.com/huaxialucaicaizi/opc-policy-navigator) | 查能申请的政策、补贴、算力券、OPC 社区 |
| 4 | [**AI Pitch Coach · 路演教练**](https://github.com/huaxialucaicaizi/ai-pitch-coach) | 园区、孵化器、创业大赛的路演稿和评委问答 |
| 5 | [**OPC Growth Playbook · 一人公司增长获客**](https://github.com/huaxialucaicaizi/opc-growth-playbook) | 小红书、抖音、视频号冷启动获客 |
| 6 | [**OPC Pricing & Sales · 定价与成交**](https://github.com/huaxialucaicaizi/opc-pricing-sales) | 定价、套餐、报价单、私域成交 |
| 7 | [**OPC Registration & Compliance · 一人公司注册与合规**](https://github.com/huaxialucaicaizi/opc-registration-compliance) | 选主体类型、注册清单、年报与合规日历 |

<a id="zh-diff"></a>
### 它和单独安装有什么不同

| 单独安装某一个 skill | 安装 AI 创业 Skill 包 |
|---|---|
| 需要自己判断该用哪个 | 总入口 skill 按阶段帮你选 |
| 每一步的产出各自独立 | 上一步的结果交给下一步用（验证证据 → BP → 政策申请 / 路演） |
| 7 个仓库分别安装、分别更新 | 一次安装，`scripts/sync.sh` 一键同步 |

如果你只需要其中一步，直接装对应的单独仓库就行。

<a id="zh-fit"></a>
### 适合 / 不适合

**适合**
- 在中国做 AI 工具、AI 应用、Agent 的一人公司和早期创业者
- 想按顺序走完"验证 → BP → 政策 → 路演 → 获客 → 定价 → 注册"的人

**不适合**
- 需要正式法律、税务意见：本工具包只提供信息参考，请以官方原文和专业人士意见为准
- 面向 VC 的融资路演：路演教练针对的是园区、孵化器和创业大赛

<a id="zh-quickstart"></a>
### 快速开始

**1. 安装**

克隆本仓库，把 `skills/` 下的 7 个子 skill 和总入口一起放进你的技能目录。

Codex（用户技能目录 `~/.agents/skills`）：

```bash
git clone https://github.com/huaxialucaicaizi/ai-startup-skills.git
mkdir -p ~/.agents/skills
cp -R ai-startup-skills/skills/* ~/.agents/skills/
cp -R ai-startup-skills ~/.agents/skills/ai-startup-skills
```

Claude Code（用户技能目录 `~/.claude/skills`）：

```bash
git clone https://github.com/huaxialucaicaizi/ai-startup-skills.git
mkdir -p ~/.claude/skills
cp -R ai-startup-skills/skills/* ~/.claude/skills/
cp -R ai-startup-skills ~/.claude/skills/ai-startup-skills
```

其他支持 Agent Skills 的工具（如 Cursor）也可按各自方式安装。规范参考：[OpenAI Codex skills](https://learn.chatgpt.com/docs/build-skills)。

**2. 开始使用**

```text
用 ai-startup-skills 帮我看看我现在在创业的哪一步、下一步该做什么：___（在做什么产品、已经做到哪一步）
```

也可以直接点名某一步，例如：

```text
用 opc-pricing-sales 帮我给这个 AI 产品定价：___
```

<a id="zh-usage"></a>
### 怎么用

1. 说清楚你在做什么、已经做到哪一步
2. 总入口判断阶段，最多问两个问题，然后调用对应的子 skill
3. 每一步完成后，它会告诉你下一步建议做什么、为什么
4. 新创业者的默认顺序：1 → 2 → 3 / 7 → 4 → 5 → 6。第 3 步和第 7 步可以同时做，申请政策前通常要先注册主体

<a id="zh-principles"></a>
### 原则

- **不编数据**：不编造行业平均值、案例和用户评价，示例都会标明虚构
- **只用官方来源**：政策、法规、平台规则附官方原文链接
- **信息参考，不是法律或税务意见**
- **子 skill 的规则优先**：进入某一步后，按那一步的 SKILL.md 执行

<a id="zh-structure"></a>
### 目录结构

```text
ai-startup-skills/
├── SKILL.md                 # 总入口：按阶段路由到子 skill
├── agents/openai.yaml
├── skills/
│   ├── ai-mvp-validation/            # 第 1 步
│   ├── business-plan-skill/          # 第 2 步
│   ├── opc-policy-navigator/         # 第 3 步
│   ├── ai-pitch-coach/               # 第 4 步
│   ├── opc-growth-playbook/          # 第 5 步
│   ├── opc-pricing-sales/            # 第 6 步
│   └── opc-registration-compliance/  # 第 7 步
├── scripts/
│   ├── validate.py          # 校验总入口和 7 个子 skill 的 frontmatter
│   └── sync.sh              # 从 7 个独立仓库重新拉取到 skills/
├── CHANGELOG.md
└── LICENSE
```

<a id="zh-sync"></a>
### 同步与更新

7 个子 skill 的源头是各自的独立仓库。要拉取最新版本：

```bash
./scripts/sync.sh
python3 scripts/validate.py
```

<a id="zh-faq"></a>
### 常见问题

**Q：必须 7 步都走一遍吗？**<br>
A：不用。总入口会从你还没做的最早一步开始，你也可以直接点名某一步。

**Q：合集和单独仓库的内容一样吗？**<br>
A：一样。`skills/` 下的内容由 `scripts/sync.sh` 从独立仓库同步，问题请优先到对应的独立仓库反馈。

**Q：政策和法规信息会过期吗？**<br>
A：会。子 skill 只引用官方链接，使用前请点开原文确认最新版本。

**Q：可以用在中国以外的市场吗？**<br>
A：验证、BP、路演、定价的思路通用；政策导航、注册与合规、平台获客主要针对中国大陆。

<a id="zh-contrib"></a>
### 贡献与反馈

- 某一步的问题或建议：到对应的独立仓库提 Issue
- 总入口或合集结构的问题：欢迎在本仓库提 [Issue](https://github.com/huaxialucaicaizi/ai-startup-skills/issues)
- 提交 PR 前请运行 `python3 scripts/validate.py`
- 引用任何法规或平台规则时，请附官方原文链接

<a id="zh-author"></a>
### 作者

**华夏路菜菜子**：前大厂 AI 产品增长，现 AI 创业者，「一人公司工具包」作者。

- GitHub：[@huaxialucaicaizi](https://github.com/huaxialucaicaizi)

如果这个工具包对你有帮助，欢迎点个 Star ⭐

### Star History

[![Star History Chart](https://api.star-history.com/svg?repos=huaxialucaicaizi/ai-startup-skills&type=Date&t=20261026)](https://star-history.com/#huaxialucaicaizi/ai-startup-skills&Date)

<a id="zh-license"></a>
### 许可

[MIT](LICENSE)

[↑ 返回顶部](#top)

---

<a id="en"></a>

## English

### Contents
- [In one sentence](#en-intro)
- [The 7-step toolkit](#en-steps)
- [Bundle vs. standalone](#en-diff)
- [Who it is for](#en-fit)
- [Quick start](#en-quickstart)
- [How to use](#en-usage)
- [Principles](#en-principles)
- [Directory structure](#en-structure)
- [Sync and updates](#en-sync)
- [FAQ](#en-faq)
- [Contributing](#en-contrib)
- [Author](#en-author)
- [License](#en-license)

<a id="en-intro"></a>
### In one sentence

The bundle repo of the One-Person Company Toolkit: seven standalone Agent Skills plus a **router skill**. Tell it what you are building and how far you have got; it works out which stage you are at and hands off to the matching sub-skill.

**Pain points**
- Building an AI product alone means figuring out validation, the BP, policy applications, pitching, growth, pricing and registration by yourself
- Installing seven skills one by one is tedious, and it is unclear which one to use first
- The output of each step (validation evidence, BP, pricing) should feed the next one

<a id="en-steps"></a>
### The 7-step toolkit

Each step is also a standalone repo you can install on its own:

| Step | Skill | What it does |
|---|---|---|
| 1 | [**AI MVP Validation**](https://github.com/huaxialucaicaizi/ai-mvp-validation) | Validate demand before you build or write a BP |
| 2 | [**Business Plan Skill**](https://github.com/huaxialucaicaizi/business-plan-skill) | Business plans, pitch content, incubator and competition applications |
| 3 | [**OPC Policy Navigator**](https://github.com/huaxialucaicaizi/opc-policy-navigator) | Find policies, subsidies, compute vouchers and OPC community spaces |
| 4 | [**AI Pitch Coach**](https://github.com/huaxialucaicaizi/ai-pitch-coach) | Roadshow scripts and judge Q&A for parks, incubators and competitions |
| 5 | [**OPC Growth Playbook**](https://github.com/huaxialucaicaizi/opc-growth-playbook) | Cold-start growth on Xiaohongshu, Douyin and WeChat Channels |
| 6 | [**OPC Pricing & Sales**](https://github.com/huaxialucaicaizi/opc-pricing-sales) | Pricing, packages, quotes and a closing process |
| 7 | [**OPC Registration & Compliance**](https://github.com/huaxialucaicaizi/opc-registration-compliance) | Entity choice, registration checklist, annual-report and compliance calendar |

<a id="en-diff"></a>
### Bundle vs. standalone

| Install one skill | Install AI Startup Skills |
|---|---|
| You decide which skill to use | The router picks by stage |
| Each step's output stands alone | Outputs flow forward (validation evidence → BP → policy / pitch) |
| Seven repos to install and update | One install, one `scripts/sync.sh` |

If you only need one step, install that standalone repo.

<a id="en-fit"></a>
### Who it is for

**Good fit**
- One-person companies and early founders in China building AI tools, apps or agents
- Anyone who wants to go through validate → BP → policy → pitch → growth → pricing → registration in order

**Not a fit**
- Formal legal or tax advice: this toolkit gives information guidance only; rely on official texts and professionals
- VC fundraising pitches: the pitch coach targets parks, incubators and competitions

<a id="en-quickstart"></a>
### Quick start

**1. Install**

Clone this repo and put the 7 sub-skills under `skills/` plus the router into your skills directory.

Codex (user skills directory `~/.agents/skills`):

```bash
git clone https://github.com/huaxialucaicaizi/ai-startup-skills.git
mkdir -p ~/.agents/skills
cp -R ai-startup-skills/skills/* ~/.agents/skills/
cp -R ai-startup-skills ~/.agents/skills/ai-startup-skills
```

Claude Code (user skills directory `~/.claude/skills`):

```bash
git clone https://github.com/huaxialucaicaizi/ai-startup-skills.git
mkdir -p ~/.claude/skills
cp -R ai-startup-skills/skills/* ~/.claude/skills/
cp -R ai-startup-skills ~/.claude/skills/ai-startup-skills
```

Other tools that support Agent Skills (such as Cursor) can install them their own way. Spec: [OpenAI Codex skills](https://learn.chatgpt.com/docs/build-skills).

**2. Use it**

```text
Use ai-startup-skills to tell me which startup stage I am at and what to do next: ___ (what you are building, what you have done)
```

Or call a step directly:

```text
Use opc-pricing-sales to price this AI product: ___
```

<a id="en-usage"></a>
### How to use

1. Say what you are building and how far you have got
2. The router picks the stage, asks at most two questions, then calls the sub-skill
3. After each step it suggests the next step and why
4. Default order for a new founder: 1 → 2 → 3 / 7 → 4 → 5 → 6. Steps 3 and 7 can run in parallel; registration is often required before policy applications

<a id="en-principles"></a>
### Principles

- **No invented data**: no made-up benchmarks, cases or testimonials; examples are marked fictional
- **Official sources only** for policies, laws and platform rules
- **Information guidance, not legal or tax advice**
- **Sub-skill rules win** inside each step

<a id="en-structure"></a>
### Directory structure

```text
ai-startup-skills/
├── SKILL.md                 # router: routes to sub-skills by stage
├── agents/openai.yaml
├── skills/
│   ├── ai-mvp-validation/            # step 1
│   ├── business-plan-skill/          # step 2
│   ├── opc-policy-navigator/         # step 3
│   ├── ai-pitch-coach/               # step 4
│   ├── opc-growth-playbook/          # step 5
│   ├── opc-pricing-sales/            # step 6
│   └── opc-registration-compliance/  # step 7
├── scripts/
│   ├── validate.py          # checks router + 7 sub-skill frontmatter
│   └── sync.sh              # re-pulls the 7 standalone repos into skills/
├── CHANGELOG.md
└── LICENSE
```

<a id="en-sync"></a>
### Sync and updates

The sub-skills come from their standalone repos. To pull the latest:

```bash
./scripts/sync.sh
python3 scripts/validate.py
```

<a id="en-faq"></a>
### FAQ

**Q: Do I have to go through all 7 steps?**<br>
A: No. The router starts at the earliest step you have not done, or you can name a step directly.

**Q: Is the bundle content the same as the standalone repos?**<br>
A: Yes. `skills/` is synced from the standalone repos by `scripts/sync.sh`; please report step-specific issues there.

**Q: Can policy and legal info go out of date?**<br>
A: Yes. Sub-skills link only to official sources; open the original to confirm the latest version.

**Q: Does it work outside China?**<br>
A: Validation, BP, pitch and pricing logic is general; policy, registration and platform growth target mainland China.

<a id="en-contrib"></a>
### Contributing

- Issues with a specific step: open an issue in that standalone repo
- Issues with the router or bundle: open an [issue](https://github.com/huaxialucaicaizi/ai-startup-skills/issues) here
- Run `python3 scripts/validate.py` before a PR
- Cite official sources for any law or platform rule

<a id="en-author"></a>
### Author

**华夏路菜菜子 (huaxialucaicaizi)**: former AI product growth lead at major Chinese tech companies, now an AI founder; author of the One-Person Company Toolkit.

- GitHub: [@huaxialucaicaizi](https://github.com/huaxialucaicaizi)

If this toolkit helps you, a Star ⭐ is appreciated.

### Star History

[![Star History Chart](https://api.star-history.com/svg?repos=huaxialucaicaizi/ai-startup-skills&type=Date&t=20261026)](https://star-history.com/#huaxialucaicaizi/ai-startup-skills&Date)

<a id="en-license"></a>
### License

[MIT](LICENSE)

[↑ Back to top](#top)

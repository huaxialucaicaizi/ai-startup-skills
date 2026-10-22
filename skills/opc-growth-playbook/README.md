<a id="top"></a>

<div align="center">

# OPC Growth Playbook · 一人公司增长获客 Skill

**小红书 / 抖音 / 视频号冷启动：漏斗、实验、内容日历、口播脚本，只用你自己的数据。**<br>
Cold-start growth on Xiaohongshu, Douyin and WeChat Channels — funnel, experiments, content calendar, scripts, using only your own data.

[![CI](https://github.com/huaxialucaicaizi/opc-growth-playbook/actions/workflows/ci.yml/badge.svg)](https://github.com/huaxialucaicaizi/opc-growth-playbook/actions/workflows/ci.yml)
[![License: MIT](https://img.shields.io/github/license/huaxialucaicaizi/opc-growth-playbook)](LICENSE)
[![GitHub stars](https://img.shields.io/github/stars/huaxialucaicaizi/opc-growth-playbook?style=social)](https://github.com/huaxialucaicaizi/opc-growth-playbook)
[![Agent Skill](https://img.shields.io/badge/Agent%20Skill-Codex%20%7C%20Cursor-blue)](https://learn.chatgpt.com/docs/build-skills)

[中文](#zh) | [English](#en)

<!-- 头图 / 演示截图：待 rui 确认是否添加，例如 assets/banner.png -->

</div>

---

<a id="zh"></a>

## 中文

### 目录
- [一句话介绍](#zh-intro)
- [它和直接问 AI 有什么不同](#zh-diff)
- [适合 / 不适合](#zh-fit)
- [快速开始](#zh-quickstart)
- [示例对话与输出节选](#zh-example)
- [工作流](#zh-workflow)
- [原则](#zh-principles)
- [目录结构](#zh-structure)
- [一人公司工具包](#zh-kit)
- [常见问题](#zh-faq)
- [贡献与反馈](#zh-contrib)
- [作者](#zh-author)
- [许可](#zh-license)

<a id="zh-intro"></a>
### 一句话介绍

一个帮一人公司在**小红书、抖音、视频号**冷启动的 Agent Skill：确认定位，搭增长漏斗并定义指标，用 ICE 排增长实验，排出 2–4 周内容日历和口播脚本，检查广告标识等合规事项，再按真实数据每周复盘。

> 这是「一人公司工具包」的第 5 步。下一步定价与成交即将推出。

**痛点**
- 发了很多内容，不知道哪里出问题：没曝光、没互动，还是没人咨询
- 想做增长实验，但不知道先做哪个、怎么判断有没有效
- 内容想到哪发到哪，没有日历和节奏
- 怕踩广告标识、AI 生成内容标识等合规问题

<a id="zh-diff"></a>
### 它和直接问 AI 有什么不同

| 直接问 AI | 用 opc-growth-playbook |
|---|---|
| 给你一堆"爆款技巧"和看起来很像真的行业数据 | 不提供行业基准，首周跑自己的基线，之后和自己比 |
| 想法一大堆，没有优先级 | 实验卡 + ICE 排序，每周只跑少量实验，一次只改一个变量 |
| 脚本里编案例、编效果 | 证据只用真实素材，没有就写"待补充" |
| 不提合规 | 逐项检查广告标识、AI 生成内容标识，附官方原文链接 |

<a id="zh-fit"></a>
### 适合 / 不适合

**适合**
- 在小红书、抖音、视频号做冷启动的一人公司、独立开发者、知识服务者
- 有产品或服务、想把内容变成咨询和付费
- 愿意每周记录数据并复盘

**不适合**
- 想刷量、买粉、搬运或做虚假测评
- 只做海外平台（本 skill 以国内平台为主）
- 已有成熟投放团队、需要精细化投放优化

<a id="zh-quickstart"></a>
### 快速开始

**1. 安装**（Codex 内置安装器）

```bash
$skill-installer huaxialucaicaizi/opc-growth-playbook
```

或手动克隆到用户技能目录：

```bash
mkdir -p ~/.agents/skills
cd ~/.agents/skills
git clone https://github.com/huaxialucaicaizi/opc-growth-playbook.git
```

其他支持 Agent Skills 的工具（如 Cursor）也可按各自方式安装。规范参考：[OpenAI Codex skills](https://learn.chatgpt.com/docs/build-skills)。

**2. 开始使用**

```text
用 opc-growth-playbook 帮我做冷启动计划：产品 ___，目标用户 ___，平台 ___，每周可投入 ___ 小时，能否出镜 ___，转化路径 ___
```

<a id="zh-example"></a>
### 示例对话与输出节选

> ⚠️ 以下案例**全部虚构**，仅用于展示输出格式和判断逻辑。

**你：**
```text
我做 AI 简历优化工具，目标用户是应届生。想做小红书，每周 6 小时，不出镜，转化是私信领取免费诊断。账号刚注册，没有数据。
```

**输出节选：**

| 层级 | 指标 | 数据来源 | 当前数据 | 本周目标 |
|---|---|---|---|---|
| 曝光 | 笔记曝光 | 平台后台 | 无（新账号） | 首周跑基线 |
| 留资 | 私信领取诊断人数 | 私信记录 | 无 | 首周跑基线 |
| 付费 | 付费人数 | 收款记录 | 无 | 首周跑基线 |

| 编号 | 假设 | 做法 | 主指标 | ICE（用户自评） |
|---|---|---|---|---|
| E1 | 如果标题直接写出应届生的具体场景，曝光会提高 | 同一内容做两版标题，各发 1 条 | 曝光 | 4 / 3 / 5 |

> 本周没有数据可比，结论写"首周跑基线"；不引用任何行业平均值。

<a id="zh-workflow"></a>
### 工作流

1. **定位确认**：一句话定位、目标用户、3 个内容支柱、人设、转化路径
2. **漏斗与指标**：曝光 → 互动 → 关注 / 留资 → 咨询 → 付费 → 复购，找出最弱的一层
3. **实验池**：假设 → 做法 → 指标 → 判断标准 → 周期，ICE 排序
4. **内容日历与口播脚本**：2–4 周排期；脚本结构"钩子 → 痛点 → 方案 → 证据 → 行动引导"
5. **合规检查**：广告标识、AI 生成内容标识、如实宣传
6. **周复盘**：真实数据、实验结论、下周计划

<a id="zh-principles"></a>
### 原则

- **不编数据**：粉丝、播放、互动、转化只用你的真实数据；不提供行业基准
- **阈值可调**：频率、实验数量、判断标准都标"建议值，可自行调整"
- **不刷量、不搬运、不做虚假测评**
- **推广内容按规定标识**；平台规则以各平台官方规则为准；不构成法律意见

<a id="zh-structure"></a>
### 目录结构

```text
SKILL.md                          # 主流程
references/
  positioning-check.md            # 定位确认
  growth-funnel.md                # 漏斗与指标
  experiment-pool.md              # 实验卡与 ICE 排序
  content-calendar.md             # 内容日历
  video-script.md                 # 口播脚本结构
  compliance.md                   # 合规检查（广告标识、AI 生成内容标识）
templates/
  growth-plan.md                  # 增长计划输出模板
  weekly-review.md                # 周复盘模板
agents/openai.yaml
scripts/validate.py
```

<a id="zh-kit"></a>
### 一人公司工具包

| 步骤 | 仓库 |
|---|---|
| 1. AI 产品 MVP 验证 | [ai-mvp-validation](https://github.com/huaxialucaicaizi/ai-mvp-validation) |
| 2. 商业计划书 | [business-plan-skill](https://github.com/huaxialucaicaizi/business-plan-skill) |
| 3. 政策与补贴 | [opc-policy-navigator](https://github.com/huaxialucaicaizi/opc-policy-navigator) |
| 4. 路演教练 | [ai-pitch-coach](https://github.com/huaxialucaicaizi/ai-pitch-coach) |
| 5. 增长获客 | [opc-growth-playbook](https://github.com/huaxialucaicaizi/opc-growth-playbook)（本仓库） |
| 6. 定价与成交 | [opc-pricing-sales](https://github.com/huaxialucaicaizi/opc-pricing-sales) |
| 7. 注册与合规 | [opc-registration-compliance](https://github.com/huaxialucaicaizi/opc-registration-compliance) |
| 串联大仓库 | 即将推出 |

<a id="zh-faq"></a>
### 常见问题

**Q：为什么不告诉我"小红书平均互动率"？**<br>
A：没有可靠出处的基准容易误导判断。本 skill 让你先跑一周基线，再和自己比。

**Q：不出镜能做吗？**<br>
A：可以，内容日历和脚本会按"不出镜"（录屏、图文、配音）来设计。

**Q：要不要投流？**<br>
A：可选。不投流就只做自然流量；投流时预算由你定，并按实验卡记录效果。

**Q：支持海外平台吗？**<br>
A：本 skill 以小红书、抖音、视频号为主；海外广告测试可参考 ai-mvp-validation 中的 Meta 广告验证。

**Q：平台规则会变怎么办？**<br>
A：本 skill 不复述未核实的平台规则，请以各平台官方规则为准。

<a id="zh-contrib"></a>
### 贡献与反馈

- 发现问题或有补充：欢迎提 [Issue](https://github.com/huaxialucaicaizi/opc-growth-playbook/issues)
- 提交 PR 前请运行 `python3 scripts/validate.py`
- 引用任何法规、政策或平台规则时，请附官方原文链接

<a id="zh-author"></a>
### 作者

**华夏路菜菜子**：前大厂 AI 产品增长，现 AI 创业者，「一人公司工具包」作者。

- GitHub：[@huaxialucaicaizi](https://github.com/huaxialucaicaizi)

如果这个 skill 对你有帮助，欢迎点个 Star ⭐

### Star History

[![Star History Chart](https://api.star-history.com/svg?repos=huaxialucaicaizi/opc-growth-playbook&type=Date)](https://star-history.com/#huaxialucaicaizi/opc-growth-playbook&Date)

<a id="zh-license"></a>
### 许可

[MIT](LICENSE)

[↑ 返回顶部](#top)

---

<a id="en"></a>

## English

### Contents
- [What It Is](#en-intro)
- [How It Differs from Just Asking an AI](#en-diff)
- [Good Fit / Not a Fit](#en-fit)
- [Quick Start](#en-quickstart)
- [Example Conversation and Output Excerpt](#en-example)
- [Workflow](#en-workflow)
- [Principles](#en-principles)
- [Structure](#en-structure)
- [One-Person Company Toolkit](#en-kit)
- [FAQ](#en-faq)
- [Contributing & Feedback](#en-contrib)
- [Author](#en-author)
- [License](#en-license)

<a id="en-intro"></a>
### What It Is

An Agent Skill that helps one-person companies cold-start on **Xiaohongshu, Douyin and WeChat Channels**: confirm positioning, build a growth funnel with defined metrics, prioritize experiments with ICE, plan a 2–4 week content calendar and short-video scripts, check ad-labeling compliance, and review weekly with real data.

> Step 5 of the "One-Person Company Toolkit". Next step (pricing & closing) is coming soon.

**The problem**
- Posting a lot but not knowing where it breaks: reach, engagement or inquiries
- Unsure which experiment to run first or how to judge it
- No calendar or rhythm
- Worried about ad-labeling and AI-content labeling rules

<a id="en-diff"></a>
### How It Differs from Just Asking an AI

| Just asking an AI | Using opc-growth-playbook |
|---|---|
| A pile of "viral tricks" and plausible-looking benchmarks | No benchmarks: run your own baseline in week 1, then compare with yourself |
| Lots of ideas, no priority | Experiment cards + ICE, few experiments at a time, one variable each |
| Scripts with invented cases | Evidence only from real material, otherwise "TBD" |
| No compliance | Checks ad labeling and AI-content labeling with official sources |

<a id="en-fit"></a>
### Good Fit / Not a Fit

**Good fit**
- Solo founders, indie developers and knowledge workers cold-starting on Chinese platforms
- Have a product or service and want content to drive inquiries and sales
- Willing to log data and review weekly

**Not a fit**
- Fake engagement, bought followers, reposting or fake reviews
- Overseas-only platforms (this skill focuses on China)
- Mature paid-media teams needing fine-grained optimization

<a id="en-quickstart"></a>
### Quick Start

**1. Install** (Codex built-in installer)

```bash
$skill-installer huaxialucaicaizi/opc-growth-playbook
```

Or clone into your user skills directory:

```bash
mkdir -p ~/.agents/skills
cd ~/.agents/skills
git clone https://github.com/huaxialucaicaizi/opc-growth-playbook.git
```

Other Agent Skills-compatible tools (e.g. Cursor) can install it in their own way. Spec: [OpenAI Codex skills](https://learn.chatgpt.com/docs/build-skills).

**2. Use it**

```text
Use opc-growth-playbook to build a cold-start plan: product ___, target users ___, platforms ___, ___ hours/week, on camera? ___, conversion path ___
```

<a id="en-example"></a>
### Example Conversation and Output Excerpt

> ⚠️ The case below is **entirely fictional**, shown only to illustrate the output format and decision logic.

**You:**
```text
AI resume tool for new graduates. Xiaohongshu, 6 hours/week, no on-camera, conversion via DM for a free review. New account, no data.
```

**Output excerpt:**

| Layer | Metric | Source | Current | This week's target |
|---|---|---|---|---|
| Reach | Note impressions | Platform dashboard | None (new account) | Run baseline |
| Leads | DMs requesting a review | DM log | None | Run baseline |
| Paid | Paying users | Payment records | None | Run baseline |

| ID | Hypothesis | Action | Metric | ICE (self-rated) |
|---|---|---|---|---|
| E1 | Titles naming a specific graduate scenario raise reach | Two title versions, one post each | Impressions | 4 / 3 / 5 |

> No data to compare yet, so the verdict is "run baseline"; no industry averages are cited.

<a id="en-workflow"></a>
### Workflow

1. **Positioning**
2. **Funnel & metrics**: reach → engagement → follow / lead → inquiry → paid → repeat; find the weakest layer
3. **Experiment pool** with ICE
4. **Content calendar & scripts**: hook → pain → solution → proof → call to action
5. **Compliance check**
6. **Weekly review** with real data

<a id="en-principles"></a>
### Principles

- **No invented data or benchmarks**
- **Adjustable thresholds**
- **No fake engagement, reposting or fake reviews**
- **Label promotional content**; platform rules per each platform; not legal advice

<a id="en-structure"></a>
### Structure

```text
SKILL.md
references/
  positioning-check.md
  growth-funnel.md
  experiment-pool.md
  content-calendar.md
  video-script.md
  compliance.md
templates/
  growth-plan.md
  weekly-review.md
agents/openai.yaml
scripts/validate.py
```

<a id="en-kit"></a>
### One-Person Company Toolkit

| Step | Repository |
|---|---|
| 1. AI MVP Validation | [ai-mvp-validation](https://github.com/huaxialucaicaizi/ai-mvp-validation) |
| 2. Business Plan | [business-plan-skill](https://github.com/huaxialucaicaizi/business-plan-skill) |
| 3. Policy & Subsidies | [opc-policy-navigator](https://github.com/huaxialucaicaizi/opc-policy-navigator) |
| 4. Roadshow Coach | [ai-pitch-coach](https://github.com/huaxialucaicaizi/ai-pitch-coach) |
| 5. Growth | [opc-growth-playbook](https://github.com/huaxialucaicaizi/opc-growth-playbook) (this repo) |
| 6. Pricing & Closing | [opc-pricing-sales](https://github.com/huaxialucaicaizi/opc-pricing-sales) |
| 7. Registration & Compliance | [opc-registration-compliance](https://github.com/huaxialucaicaizi/opc-registration-compliance) |
| Full toolkit repo | Coming soon |

<a id="en-faq"></a>
### FAQ

**Q: Why no "average engagement rate"?**<br>
A: Unsourced benchmarks mislead; you run your own baseline first.

**Q: Can I do it without appearing on camera?**<br>
A: Yes, plans can use screen recordings, image posts and voice-over.

**Q: Paid promotion?**<br>
A: Optional; you set the budget and log results with experiment cards.

**Q: Overseas platforms?**<br>
A: Focus is China; for Meta ad tests see ai-mvp-validation.

**Q: Platform rules change?**<br>
A: Not restated here; follow the official rules of each platform.

<a id="en-contrib"></a>
### Contributing & Feedback

- Found a problem or have something to add? Open an [Issue](https://github.com/huaxialucaicaizi/opc-growth-playbook/issues)
- Run `python3 scripts/validate.py` before submitting a PR
- Cite official sources for any regulation, policy or platform rule

<a id="en-author"></a>
### Author

**华夏路菜菜子 (huaxialucaicaizi)**: former AI product growth lead at major Chinese tech companies, now an AI founder; author of the One-Person Company Toolkit.

- GitHub: [@huaxialucaicaizi](https://github.com/huaxialucaicaizi)

If this skill helps you, a Star ⭐ is appreciated.

### Star History

[![Star History Chart](https://api.star-history.com/svg?repos=huaxialucaicaizi/opc-growth-playbook&type=Date)](https://star-history.com/#huaxialucaicaizi/opc-growth-playbook&Date)

<a id="en-license"></a>
### License

[MIT](LICENSE)

[↑ Back to top](#top)

<a id="top"></a>

<div align="center">

# AI MVP Validation · AI 产品 MVP 验证 Skill

**先验证有没有人要，再写代码、写 BP。**<br>
Validate demand before you build or write a business plan.

[![CI](https://github.com/huaxialucaicaizi/ai-mvp-validation/actions/workflows/ci.yml/badge.svg)](https://github.com/huaxialucaicaizi/ai-mvp-validation/actions/workflows/ci.yml)
[![License: MIT](https://img.shields.io/github/license/huaxialucaicaizi/ai-mvp-validation)](LICENSE)
[![GitHub stars](https://img.shields.io/github/stars/huaxialucaicaizi/ai-mvp-validation?style=social)](https://github.com/huaxialucaicaizi/ai-mvp-validation)
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

一个面向 **AI 工具、AI 应用、Agent** 的 Agent Skill：用**桌面调研 + 用户访谈 + 小预算 Meta（Facebook / Instagram）广告测试**验证 AI 产品想法，最后给出"继续 / 调整 / 放弃"的结论，并把过程整理成写 BP、申请园区、找投资时可以引用的证据。

> 这是「一人公司工具包」的第 1 步。下一步写 BP 可用第 2 步 [**Business Plan Skill · 商业计划书**](https://github.com/huaxialucaicaizi/business-plan-skill)。

**痛点**
- 做 AI 产品很快，但做完才发现没人用、没人付钱
- 不确定通用大模型会不会让你的产品变得多余
- 模型调用成本算不清，定价心里没底
- 想投广告测需求，但不知道测什么、花多少、看哪些指标、怎样算通过
- 写 BP 或申请园区时，拿不出"市场验证"证据

<a id="zh-diff"></a>
### 它和直接问 AI 有什么不同

| 直接问"我的想法好不好" | 用 ai-mvp-validation |
|---|---|
| 得到一段泛泛的鼓励或 SWOT | 按固定五步走，每一步有表格和判断标准 |
| 容易给出看起来很像真的市场数据 | 没有来源的数据一律写"待补充"，不提供"行业平均" |
| 不会追问"通用 AI 能不能直接做到" | 专门评估大模型原生功能覆盖、推理成本、数据合规 |
| 没有可执行的测试方案 | 给出落地页 / 等待名单 + A/B 广告测试方案、指标公式、止损 |
| 结论模糊 | 组合公式 + "已验证 X，下一步验证 Y" + 继续 / 调整 / 放弃 |

<a id="zh-fit"></a>
### 适合 / 不适合

**适合**
- 一人公司、独立开发者、小团队，正在做或打算做 AI 工具、AI 应用、Agent
- 面向海外（Meta 广告）或国内（可换小红书聚光、巨量引擎）
- 需要把验证过程变成评委、投资人看得懂的证据

**不适合**
- 已有稳定付费用户、需要做规模化增长的产品（这是工具包第 5 步的事，见 [**OPC Growth Playbook · 一人公司增长获客**](https://github.com/huaxialucaicaizi/opc-growth-playbook)）
- 需要法律意见的合规问题（本 skill 只提示风险并给官方原文链接）
- 想要现成"行业基准数据"的人（本 skill 不提供，阈值请自行设定）

<a id="zh-quickstart"></a>
### 快速开始

**1. 安装**（Codex 内置安装器）

```bash
$skill-installer huaxialucaicaizi/ai-mvp-validation
```

或手动克隆到用户技能目录：

```bash
mkdir -p ~/.agents/skills
cd ~/.agents/skills
git clone https://github.com/huaxialucaicaizi/ai-mvp-validation.git
```

其他支持 Agent Skills 的工具（如 Cursor）也可按各自方式安装。规范参考：[OpenAI Codex skills](https://learn.chatgpt.com/docs/build-skills)。

**2. 开始使用**

```text
用 ai-mvp-validation 帮我验证这个想法：___（产品是什么、给谁用、目标市场、广告预算）
```

<a id="zh-example"></a>
### 示例对话与输出节选

> ⚠️ 以下案例、访谈和广告数据**全部虚构**，仅用于展示输出格式和判断逻辑。

**你：**
```text
用 ai-mvp-validation 验证：一个帮海外独立站小卖家自动起草售后邮件回复的 Agent。
访谈了 6 个卖家，投了 10 天 Meta 广告，3 个卖点版本，数据在附件。
```

**输出节选：**

| 版本（卖点） | 落地页访问 | 留资 | 落地页转化率 | 单线索成本 | 付费意向（表单） | 实际预付 |
|---|---|---|---|---|---|---|
| A 每天省 2 小时 | 210 | 17 | 8.1% | $5.88 | 2 | 0 |
| B 提升好评 | 130 | 4 | 3.1% | $25.00 | 0 | 0 |
| C 24 小时回复 | 160 | 9 | 5.6% | $11.11 | 1 | 0 |

| 给谁 | 解决什么 | 卖点（胜出版本） | 付多少钱 |
|---|---|---|---|
| 海外独立站小卖家（已验证，样本不足） | 售后邮件回复耗时（已验证） | 每天省 2 小时（已验证） | 每月 19 美元（待验证） |

> 已验证的是：人群痛点和"省时间"卖点更能吸引留资；下一步要验证的是：A 版留资用户中能否有真实预付，以及通用 AI 能否直接替代。
>
> **结论：调整**。原因：实际预付为 0；"会不会被大模型原生功能覆盖"未评估，按高风险处理；售价未定，单线索成本无法判断。

<a id="zh-workflow"></a>
### 工作流

1. **调研**：桌面调研（竞品、搜索热度、社区讨论）+ 用户访谈
2. **痛点 + AI 产品判断**：大模型原生功能覆盖风险、模型 / 推理成本、数据与合规
3. **一人能否做**：时间、钱（含广告费和模型调用费）、技能、AI 工具分工
4. **Meta 广告投放验证**：多卖点 × 多受众 A/B 测试，记录 CTR、CPC、落地页转化率、单线索成本、付费意向、实际预付
5. **结论**：组合公式（给谁 / 解决什么 / 卖点 / 付多少钱）+ 继续 / 调整 / 放弃

辅助方法：小红书笔记测反应、预售、人工模拟交付。

<a id="zh-principles"></a>
### 原则

- **不编数据**：没有的写"待补充"；不提供"行业平均"基准
- **阈值可调**：所有判断标准都标"建议值，可自行调整"
- **如实宣传**：未上线产品只能以"等待名单 / 内测预约"呈现
- **只引用已核实的官方链接**：法规、平台规则以官方原文为准；本 skill 不构成法律意见

<a id="zh-structure"></a>
### 目录结构

```text
SKILL.md                         # 主流程
references/
  desk-research.md               # 桌面调研
  interview-guide.md             # 用户访谈指南
  pain-and-feasibility.md        # 痛点、AI 产品判断、一人可行性
  meta-ads-validation.md         # Meta 广告投放验证（核心）
  validation-methods.md          # 辅助方法：小红书、预售、人工交付
  validation-log.md              # 验证记录表
agents/openai.yaml
scripts/validate.py
```

<a id="zh-kit"></a>
### 一人公司工具包

| 步骤 | 仓库 |
|---|---|
| 1. AI 产品 MVP 验证 | [**AI MVP Validation · AI 产品 MVP 验证**](https://github.com/huaxialucaicaizi/ai-mvp-validation)（本仓库） |
| 2. 商业计划书 | [**Business Plan Skill · 商业计划书**](https://github.com/huaxialucaicaizi/business-plan-skill) |
| 3. 政策与补贴 | [**OPC Policy Navigator · 一人公司政策导航**](https://github.com/huaxialucaicaizi/opc-policy-navigator) |
| 4. 路演教练 | [**AI Pitch Coach · 路演教练**](https://github.com/huaxialucaicaizi/ai-pitch-coach) |
| 5. 增长获客 | [**OPC Growth Playbook · 一人公司增长获客**](https://github.com/huaxialucaicaizi/opc-growth-playbook) |
| 6. 定价与成交 | [**OPC Pricing & Sales · 定价与成交**](https://github.com/huaxialucaicaizi/opc-pricing-sales) |
| 7. 注册与合规 | [**OPC Registration & Compliance · 一人公司注册与合规**](https://github.com/huaxialucaicaizi/opc-registration-compliance) |
| AI 创业 Skill 包（全套 7 步） | [**AI Startup Skills · AI 创业 Skill 包**](https://github.com/huaxialucaicaizi/ai-startup-skills) |

<a id="zh-faq"></a>
### 常见问题

**Q：广告预算要多少？**<br>
A：本 skill 不给固定金额，按"版本数 × 每版本达到足够访问量"的思路帮你估算，并设止损。所有数值都是建议值，可自行调整。

**Q：产品还没做出来，可以投广告吗？**<br>
A：可以，但落地页必须如实说明是"等待名单 / 内测预约"，不能暗示已经可用。

**Q：我做国内市场，不用 Meta 怎么办？**<br>
A：思路相同，平台换成小红书聚光或巨量引擎即可。

**Q：为什么不给"行业平均 CTR"？**<br>
A：没有可靠出处的基准容易误导判断。本 skill 用 CTR、CPC 比较你自己的版本，用你自己的商业模式倒推单线索成本上限。

**Q：一定要先用这个 skill 才能用 business-plan-skill 吗？**<br>
A：不需要，两者都可单独使用。验证结论为"继续"时，可输出 BP 素材包作为可选衔接。

**Q：支持哪些工具？**<br>
A：遵循 Agent Skills 规范（SKILL.md），可在 Codex 中用 `$skill-installer` 安装；其他支持 Agent Skills 的工具（如 Cursor）可按各自方式安装。

<a id="zh-contrib"></a>
### 贡献与反馈

- 发现问题、想补充新的验证方法或国内投放平台经验：欢迎提 [Issue](https://github.com/huaxialucaicaizi/ai-mvp-validation/issues)
- 提交 PR 前请运行 `python3 scripts/validate.py`
- 引用任何法规或平台规则时，请附官方原文链接

<a id="zh-author"></a>
### 作者

**华夏路菜菜子**：前大厂 AI 产品增长，现 AI 创业者，「一人公司工具包」作者。

- GitHub：[@huaxialucaicaizi](https://github.com/huaxialucaicaizi)

如果这个 skill 对你有帮助，欢迎点个 Star ⭐

### Star History

[![Star History Chart](https://api.star-history.com/svg?repos=huaxialucaicaizi/ai-mvp-validation&type=Date)](https://star-history.com/#huaxialucaicaizi/ai-mvp-validation&Date)

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

An Agent Skill for **AI tools, AI apps and Agents**: validate your AI product idea with **desk research + user interviews + small-budget Meta (Facebook / Instagram) ad tests**, get a continue / adjust / stop verdict, and turn the process into evidence you can cite in a business plan, incubator application or investor conversation.

> Step 1 of the "One-Person Company Toolkit". Next step: write your BP with step 2, [**Business Plan Skill**](https://github.com/huaxialucaicaizi/business-plan-skill).

**The problem**
- Building an AI product is fast; finding out nobody uses or pays for it comes later and costs more
- Unsure whether general-purpose LLMs make your product redundant
- Unclear inference cost, so pricing is guesswork
- Want to run ad tests but don't know what to test, how much to spend, which metrics to watch, or what "pass" looks like
- No market validation evidence for your BP or incubator application

<a id="en-diff"></a>
### How It Differs from Just Asking an AI

| Asking "Is my idea good?" | Using ai-mvp-validation |
|---|---|
| Generic encouragement or a SWOT | A fixed five-step process with tables and decision criteria |
| Plausible-looking market numbers | Anything without a source is marked "TBD"; no "industry averages" |
| Rarely asks "can a general AI already do this?" | Explicitly checks native-LLM overlap, inference cost, data compliance |
| No runnable test plan | Landing page / waitlist + A/B ad test plan, metric formulas, stop-loss |
| Vague conclusion | Combination formula + "Validated X, next validate Y" + continue / adjust / stop |

<a id="en-fit"></a>
### Good Fit / Not a Fit

**Good fit**
- Solo founders, indie hackers and small teams building (or planning) AI tools, AI apps or Agents
- Targeting overseas markets (Meta ads) or China (swap in Xiaohongshu Juguang or Ocean Engine)
- Need validation evidence that judges and investors can understand

**Not a fit**
- Products with steady paying users that need to scale (that is step 5 of the toolkit: see [**OPC Growth Playbook**](https://github.com/huaxialucaicaizi/opc-growth-playbook))
- Compliance questions that need legal advice (this skill only flags risks and links official sources)
- Anyone looking for ready-made industry benchmarks (not provided; set your own thresholds)

<a id="en-quickstart"></a>
### Quick Start

**1. Install** (Codex built-in installer)

```bash
$skill-installer huaxialucaicaizi/ai-mvp-validation
```

Or clone into your user skills directory:

```bash
mkdir -p ~/.agents/skills
cd ~/.agents/skills
git clone https://github.com/huaxialucaicaizi/ai-mvp-validation.git
```

Other Agent Skills-compatible tools (e.g. Cursor) can install it in their own way. Spec: [OpenAI Codex skills](https://learn.chatgpt.com/docs/build-skills).

**2. Use it**

```text
Use ai-mvp-validation to validate this idea: ___ (what it is, who it's for, target market, ad budget)
```

<a id="en-example"></a>
### Example Conversation and Output Excerpt

> ⚠️ The case, interviews and ad data below are **entirely fictional**, shown only to illustrate the output format and decision logic.

**You:**
```text
Use ai-mvp-validation to validate: an Agent that drafts after-sales email replies for small overseas e-commerce sellers.
I interviewed 6 sellers and ran Meta ads for 10 days with 3 selling-point versions; data attached.
```

**Output excerpt:**

| Version (selling point) | Visits | Leads | Conversion | Cost per lead | Payment intent (form) | Actual prepay |
|---|---|---|---|---|---|---|
| A Save 2 hours a day | 210 | 17 | 8.1% | $5.88 | 2 | 0 |
| B More good reviews | 130 | 4 | 3.1% | $25.00 | 0 | 0 |
| C 24h replies | 160 | 9 | 5.6% | $11.11 | 1 | 0 |

| For whom | Solving what | Selling point (winner) | Price |
|---|---|---|---|
| Small overseas e-commerce sellers (validated, small sample) | Time spent on after-sales emails (validated) | Save 2 hours a day (validated) | $19/month (to be validated) |

> Validated: the pain point and that "save time" attracts the most sign-ups. Next to validate: whether A's leads will actually prepay, and whether a general AI can already do this.
>
> **Verdict: Adjust.** Reasons: zero actual prepayments; native-LLM overlap not assessed (treated as high risk); price undecided, so cost per lead can't be judged.

<a id="en-workflow"></a>
### Workflow

1. **Research**: desk research (competitors, search trends, community discussions) + user interviews
2. **Pain + AI product assessment**: native-LLM overlap risk, model / inference cost, data and compliance
3. **Can one person do it**: time, money (incl. ad spend and model API costs), skills, division of work with AI tools
4. **Meta ad validation**: multi-selling-point × multi-audience A/B tests, tracking CTR, CPC, landing page conversion, cost per lead, payment intent, actual prepayments
5. **Conclusion**: combination formula (for whom / solving what / selling point / price) + continue / adjust / stop

Supplementary methods: Xiaohongshu posts, pre-sales, manual (concierge) delivery.

<a id="en-principles"></a>
### Principles

- **No fabricated data**: write "TBD" for anything missing; no "industry average" benchmarks
- **Adjustable thresholds**: every criterion is marked "suggested value, adjust as needed"
- **Honest promotion**: unlaunched products may only be presented as "waitlist / beta sign-up"
- **Only cite verified official links**: regulations and platform rules follow official sources; this skill is not legal advice

<a id="en-structure"></a>
### Structure

```text
SKILL.md                         # main workflow
references/
  desk-research.md               # desk research
  interview-guide.md             # user interview guide
  pain-and-feasibility.md        # pain, AI product assessment, solo feasibility
  meta-ads-validation.md         # Meta ad validation (core)
  validation-methods.md          # supplementary methods
  validation-log.md              # validation log template
agents/openai.yaml
scripts/validate.py
```

<a id="en-kit"></a>
### One-Person Company Toolkit

| Step | Repository |
|---|---|
| 1. AI MVP Validation | [**AI MVP Validation**](https://github.com/huaxialucaicaizi/ai-mvp-validation) (this repo) |
| 2. Business Plan | [**Business Plan Skill**](https://github.com/huaxialucaicaizi/business-plan-skill) |
| 3. Policy & Subsidies | [**OPC Policy Navigator**](https://github.com/huaxialucaicaizi/opc-policy-navigator) |
| 4. Roadshow Coach | [**AI Pitch Coach**](https://github.com/huaxialucaicaizi/ai-pitch-coach) |
| 5. Growth | [**OPC Growth Playbook**](https://github.com/huaxialucaicaizi/opc-growth-playbook) |
| 6. Pricing & Closing | [**OPC Pricing & Sales**](https://github.com/huaxialucaicaizi/opc-pricing-sales) |
| 7. Registration & Compliance | [**OPC Registration & Compliance**](https://github.com/huaxialucaicaizi/opc-registration-compliance) |
| AI Startup Skills (all 7 steps) | [**AI Startup Skills**](https://github.com/huaxialucaicaizi/ai-startup-skills) |

<a id="en-faq"></a>
### FAQ

**Q: How much ad budget do I need?**<br>
A: No fixed amount. The skill helps you estimate it from "number of versions × enough visits per version" and sets a stop-loss. All values are suggestions you can adjust.

**Q: Can I run ads before the product exists?**<br>
A: Yes, but the landing page must honestly say "waitlist / beta sign-up" and must not imply the product is available.

**Q: I'm targeting China, not Meta. What then?**<br>
A: Same approach; use Xiaohongshu Juguang or Ocean Engine instead.

**Q: Why no "industry average CTR"?**<br>
A: Benchmarks without a reliable source mislead. CTR and CPC are used to compare your own versions; the cost-per-lead ceiling is derived from your own business model.

**Q: Do I need this skill before using business-plan-skill?**<br>
A: No, both work standalone. When the verdict is "continue", you can optionally export a BP material pack.

**Q: Which tools are supported?**<br>
A: It follows the Agent Skills format (SKILL.md). Install in Codex with `$skill-installer`; other Agent Skills-compatible tools (e.g. Cursor) can install it their own way.

<a id="en-contrib"></a>
### Contributing & Feedback

- Found a problem, or want to add a validation method or ad platform experience? Open an [Issue](https://github.com/huaxialucaicaizi/ai-mvp-validation/issues)
- Run `python3 scripts/validate.py` before submitting a PR
- Cite official sources for any regulation or platform rule

<a id="en-author"></a>
### Author

**华夏路菜菜子 (huaxialucaicaizi)**: former AI product growth lead at major Chinese tech companies, now an AI founder; author of the One-Person Company Toolkit.

- GitHub: [@huaxialucaicaizi](https://github.com/huaxialucaicaizi)

If this skill helps you, a Star ⭐ is appreciated.

### Star History

[![Star History Chart](https://api.star-history.com/svg?repos=huaxialucaicaizi/ai-mvp-validation&type=Date)](https://star-history.com/#huaxialucaicaizi/ai-mvp-validation&Date)

<a id="en-license"></a>
### License

[MIT](LICENSE)

[↑ Back to top](#top)

<a id="top"></a>

<div align="center">

# AI Pricing & Closing · 定价与成交 Skill

**卖多少钱、怎么分套餐、咨询来了怎么成交——底价算清楚，价格写合规。**<br>
Price your AI product or service, design packages, write quotes and close deals — with real costs and compliant price marking.

[![CI](https://github.com/huaxialucaicaizi/opc-pricing-sales/actions/workflows/ci.yml/badge.svg)](https://github.com/huaxialucaicaizi/opc-pricing-sales/actions/workflows/ci.yml)
[![License: MIT](https://img.shields.io/github/license/huaxialucaicaizi/opc-pricing-sales)](LICENSE)
[![GitHub stars](https://img.shields.io/github/stars/huaxialucaicaizi/opc-pricing-sales?style=social)](https://github.com/huaxialucaicaizi/opc-pricing-sales)
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

一个帮卖 AI 产品或服务的一人公司**定价和成交**的 Agent Skill：用成本法（含模型 / API 调用费）算底价，结合竞品和客户价值定价格区间，设计 2–3 档套餐，生成报价单，给出私域成交流程和异议处理，并按《明码标价和禁止价格欺诈规定》检查价格写法。

> 这是「一人公司工具包」的第 6 步。下一步注册与合规可用 [opc-registration-compliance](https://github.com/huaxialucaicaizi/opc-registration-compliance)。

**痛点**
- 不敢定价，或者随便定了个数，算下来其实在亏
- 模型调用费会不会吃掉利润，心里没底
- 套餐分不清，客户不知道选哪个
- 咨询很多、成交很少，被问"太贵了""我用通用 AI 就行"不知道怎么回

<a id="zh-diff"></a>
### 它和直接问 AI 有什么不同

| 直接问 AI | 用 opc-pricing-sales |
|---|---|
| 给一个"市场价一般是……"的数字 | 底价 / 建议价 / 上限参考三个数，每个都写依据，缺数据写"待补充" |
| 忽略模型调用费和自己的时间 | 成本法计入模型 / API 费（来自官方价格页）、工具、外包和时间成本 |
| 教你"原价 999 现价 199" | 按明码标价规定检查划线价、折扣基准和促销写法 |
| 话术夸大效果 | 异议处理只用真实案例，承诺必须能兑现 |

<a id="zh-fit"></a>
### 适合 / 不适合

**适合**
- 卖 AI 工具、AI 应用、Agent 或 AI 相关服务（咨询、代运营、陪跑）的一人公司
- 需要定价、设计套餐、写报价单、提高私域成交
- 在中国境内销售、需要注意明码标价

**不适合**
- 大型企业的复杂招投标定价
- 需要合同、发票、税务等专业意见（请咨询专业人士）
- 想用虚假促销提高成交

<a id="zh-quickstart"></a>
### 快速开始

**1. 安装**（Codex 内置安装器）

```bash
$skill-installer huaxialucaicaizi/opc-pricing-sales
```

或手动克隆到用户技能目录：

```bash
mkdir -p ~/.agents/skills
cd ~/.agents/skills
git clone https://github.com/huaxialucaicaizi/opc-pricing-sales.git
```

其他支持 Agent Skills 的工具（如 Cursor）也可按各自方式安装。规范参考：[OpenAI Codex skills](https://learn.chatgpt.com/docs/build-skills)。

**2. 开始使用**

```text
用 opc-pricing-sales 帮我定价：产品 / 服务 ___，交付方式 ___，成本（模型费、工具、时间）___，竞品价格（附链接）___，客户能省多少 ___
```

<a id="zh-example"></a>
### 示例对话与输出节选

> ⚠️ 以下案例**全部虚构**，仅用于展示输出格式和判断逻辑。

**你：**
```text
我给小微企业做 AI 合同初审（AI 先审、我再人工复核），每份大约花我 1 小时，模型费每份约 2 元（官方价格页估算）。期望时薪 200 元。竞品价格还没查。
```

**输出节选：**

| 成本项 | 数值 | 来源 |
|---|---|---|
| 模型费 | 约 2 元 / 份 | 用户按官方价格页估算（查询日期：待补充） |
| 时间成本 | 1 小时 × 200 元 = 200 元 | 用户自定 |
| 单位成本 | 约 202 元 / 份 | |

| 底价 | 建议价 | 上限参考 | 依据 |
|---|---|---|---|
| 202 ÷（1 − 目标毛利率）；毛利率待用户设定 | 待补充 | 待补充 | 竞品价格、客户价值估算均未提供 |

> 结论：先补竞品公开价格（附链接）和 3 位客户的价值估算，再定建议价。主要成本是你的时间，不是模型费，套餐设计应控制人工复核的范围。

<a id="zh-workflow"></a>
### 工作流

1. **算底价**：模型 / API 费 + 工具 + 外包 + 时间成本，按目标毛利率算底价
2. **定价格区间**：竞品法（附来源）+ 价值法（客户自己估算）
3. **设计套餐**：2–3 档，写清包含 / 不包含 / 交付时间
4. **报价单**：内容、交付物、价格、付款、退款、有效期
5. **成交流程与异议处理**：线索 → 需求 → 方案 → 报价 → 异议 → 成交 → 交付 → 回访
6. **价格合规检查**：明码标价、划线价、促销

<a id="zh-principles"></a>
### 原则

- **不编造竞品价格、行业毛利率、转化率**；没有来源写"待补充"
- **模型价格来自服务商官方价格页并注明查询日期**
- **不做虚假原价、虚假限时、虚假名额**
- **承诺必须能兑现**；不构成法律或财税意见

<a id="zh-structure"></a>
### 目录结构

```text
SKILL.md                          # 主流程
references/
  pricing-methods.md              # 成本法 / 竞品法 / 价值法 / 价格区间
  packages.md                     # 套餐设计
  closing-sop.md                  # 成交流程
  objection-handling.md           # 异议处理
  price-compliance.md             # 价格合规检查（明码标价规定）
templates/
  pricing-plan.md                 # 定价与成交方案输出模板
  quote.md                        # 报价单模板
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
| 5. 增长获客 | [opc-growth-playbook](https://github.com/huaxialucaicaizi/opc-growth-playbook) |
| 6. 定价与成交 | [opc-pricing-sales](https://github.com/huaxialucaicaizi/opc-pricing-sales)（本仓库） |
| 7. 注册与合规 | [opc-registration-compliance](https://github.com/huaxialucaicaizi/opc-registration-compliance) |
| AI 创业 Skill 包（全套 7 步） | [ai-startup-skills](https://github.com/huaxialucaicaizi/ai-startup-skills) |

<a id="zh-faq"></a>
### 常见问题

**Q：能直接告诉我该卖多少钱吗？**<br>
A：只能在你提供成本、竞品和客户价值后给出区间；缺数据的部分会写"待补充"。

**Q：目标毛利率定多少？**<br>
A：由你自己定，本 skill 只标"建议值，可自行调整"，不提供行业毛利率。

**Q：可以用划线价吗？**<br>
A：可以，但被比较价格要真实准确，按明码标价规定检查（附原文链接）。

**Q：订阅制怎么算模型成本？**<br>
A：按普通用户和重度用户的调用量各算一遍，确认重度用户不亏钱。

**Q：合同和发票怎么处理？**<br>
A：本 skill 不提供法律或财税意见，请咨询专业人士或主管部门。

<a id="zh-contrib"></a>
### 贡献与反馈

- 发现问题或有补充：欢迎提 [Issue](https://github.com/huaxialucaicaizi/opc-pricing-sales/issues)
- 提交 PR 前请运行 `python3 scripts/validate.py`
- 引用任何法规、政策或平台规则时，请附官方原文链接

<a id="zh-author"></a>
### 作者

**华夏路菜菜子**：前大厂 AI 产品增长，现 AI 创业者，「一人公司工具包」作者。

- GitHub：[@huaxialucaicaizi](https://github.com/huaxialucaicaizi)

如果这个 skill 对你有帮助，欢迎点个 Star ⭐

### Star History

[![Star History Chart](https://api.star-history.com/svg?repos=huaxialucaicaizi/opc-pricing-sales&type=Date)](https://star-history.com/#huaxialucaicaizi/opc-pricing-sales&Date)

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

An Agent Skill for one-person companies selling AI products or services: compute a price floor from real costs (including model/API fees), set a range using competitors and customer value, design 2–3 tiers, draft a quote, follow a closing SOP with objection handling, and check price marking against China rules.

> Step 6 of the "One-Person Company Toolkit". Next step: register and stay compliant with [opc-registration-compliance](https://github.com/huaxialucaicaizi/opc-registration-compliance).

**The problem**
- Afraid to set a price, or picked one that actually loses money
- Unsure if model/API costs eat the margin
- Confusing packages
- Many inquiries, few sales; stuck on "too expensive" or "I'll just use ChatGPT"

<a id="en-diff"></a>
### How It Differs from Just Asking an AI

| Just asking an AI | Using opc-pricing-sales |
|---|---|
| A "typical market price" with no source | Floor / suggested / ceiling, each with its basis; missing data is "TBD" |
| Ignores model costs and your time | Includes model/API fees from official pricing pages, tools, outsourcing and time |
| Fake "was 999, now 199" tactics | Checks strikethrough prices and discounts against China price-marking rules |
| Overpromising scripts | Objection handling with real cases only; promises must be deliverable |

<a id="en-fit"></a>
### Good Fit / Not a Fit

**Good fit**
- One-person companies selling AI tools, apps, agents or AI services
- Need pricing, packages, quotes and better one-to-one closing
- Selling in China and need compliant price marking

**Not a fit**
- Complex enterprise tenders
- Contract, invoice or tax advice (consult professionals)
- Fake promotions

<a id="en-quickstart"></a>
### Quick Start

**1. Install** (Codex built-in installer)

```bash
$skill-installer huaxialucaicaizi/opc-pricing-sales
```

Or clone into your user skills directory:

```bash
mkdir -p ~/.agents/skills
cd ~/.agents/skills
git clone https://github.com/huaxialucaicaizi/opc-pricing-sales.git
```

Other Agent Skills-compatible tools (e.g. Cursor) can install it in their own way. Spec: [OpenAI Codex skills](https://learn.chatgpt.com/docs/build-skills).

**2. Use it**

```text
Use opc-pricing-sales to price my offer: product ___, delivery ___, costs ___, competitor prices (with links) ___, customer value ___
```

<a id="en-example"></a>
### Example Conversation and Output Excerpt

> ⚠️ The case below is **entirely fictional**, shown only to illustrate the output format and decision logic.

**You:**
```text
AI-assisted contract pre-review for small businesses (AI first, then my manual check). ~1 hour per contract, ~RMB 2 model cost per contract (from the official pricing page). Target hourly rate RMB 200. Competitor prices not checked yet.
```

**Output excerpt:**

| Cost item | Value | Source |
|---|---|---|
| Model cost | ~RMB 2 / contract | User estimate from official pricing page (date: TBD) |
| Time | 1 h × RMB 200 = RMB 200 | User-defined |
| Unit cost | ~RMB 202 / contract | |

| Floor | Suggested | Ceiling | Basis |
|---|---|---|---|
| 202 ÷ (1 − target margin); margin TBD | TBD | TBD | No competitor prices or customer value estimates yet |

> Verdict: collect sourced competitor prices and value estimates from 3 customers first. Your time, not the model, is the main cost, so packages should limit manual review.

<a id="en-workflow"></a>
### Workflow

1. **Price floor** from real costs and target margin
2. **Price range**: competitors (sourced) + customer value
3. **Packages**: 2–3 tiers with inclusions, exclusions and timing
4. **Quote**
5. **Closing SOP & objections**
6. **Price-marking compliance check**

<a id="en-principles"></a>
### Principles

- **No invented competitor prices, margins or conversion rates**
- **Model prices from official pricing pages with dates**
- **No fake list prices, deadlines or scarcity**
- **Only promise what you can deliver**; not legal or tax advice

<a id="en-structure"></a>
### Structure

```text
SKILL.md
references/
  pricing-methods.md
  packages.md
  closing-sop.md
  objection-handling.md
  price-compliance.md
templates/
  pricing-plan.md
  quote.md
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
| 5. Growth | [opc-growth-playbook](https://github.com/huaxialucaicaizi/opc-growth-playbook) |
| 6. Pricing & Closing | [opc-pricing-sales](https://github.com/huaxialucaicaizi/opc-pricing-sales) (this repo) |
| 7. Registration & Compliance | [opc-registration-compliance](https://github.com/huaxialucaicaizi/opc-registration-compliance) |
| AI Startup Skills (all 7 steps) | [ai-startup-skills](https://github.com/huaxialucaicaizi/ai-startup-skills) |

<a id="en-faq"></a>
### FAQ

**Q: Can it just tell me the price?**<br>
A: It gives a range once you provide costs, competitors and customer value; missing parts are "TBD".

**Q: What margin should I target?**<br>
A: You decide; no industry margins are provided.

**Q: Strikethrough prices?**<br>
A: Allowed if the compared price is real; checked against the price-marking rules.

**Q: Model cost for subscriptions?**<br>
A: Calculate for typical and heavy users.

**Q: Contracts and invoices?**<br>
A: Not legal or tax advice; consult professionals.

<a id="en-contrib"></a>
### Contributing & Feedback

- Found a problem or have something to add? Open an [Issue](https://github.com/huaxialucaicaizi/opc-pricing-sales/issues)
- Run `python3 scripts/validate.py` before submitting a PR
- Cite official sources for any regulation, policy or platform rule

<a id="en-author"></a>
### Author

**华夏路菜菜子 (huaxialucaicaizi)**: former AI product growth lead at major Chinese tech companies, now an AI founder; author of the One-Person Company Toolkit.

- GitHub: [@huaxialucaicaizi](https://github.com/huaxialucaicaizi)

If this skill helps you, a Star ⭐ is appreciated.

### Star History

[![Star History Chart](https://api.star-history.com/svg?repos=huaxialucaicaizi/opc-pricing-sales&type=Date)](https://star-history.com/#huaxialucaicaizi/opc-pricing-sales&Date)

<a id="en-license"></a>
### License

[MIT](LICENSE)

[↑ Back to top](#top)

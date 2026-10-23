<a id="top"></a>

<div align="center">

# OPC Company Registration (China) · 一人公司注册与合规 Skill

**个体户、个人独资企业、一人有限公司怎么选？怎么注册？注册后守哪些规矩？——只引官方原文，非法律意见。**<br>
Sole proprietorship, individual business or one-shareholder company? How to register in China and stay compliant — official sources only, not legal advice.

[![CI](https://github.com/huaxialucaicaizi/opc-registration-compliance/actions/workflows/ci.yml/badge.svg)](https://github.com/huaxialucaicaizi/opc-registration-compliance/actions/workflows/ci.yml)
[![License: MIT](https://img.shields.io/github/license/huaxialucaicaizi/opc-registration-compliance)](LICENSE)
[![GitHub stars](https://img.shields.io/github/stars/huaxialucaicaizi/opc-registration-compliance?style=social)](https://github.com/huaxialucaicaizi/opc-registration-compliance)
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

一个帮中国大陆一人创业者**选主体、办注册、守合规**的 Agent Skill：按责任承担、组织机构、出资对比个体工商户、个人独资企业和一人有限公司（每条附法律条款出处），生成登记事项和材料清单，再给出年报、变更登记、财产独立等注册后合规日历。只做信息指引，不构成法律或财税意见。

> 这是「一人公司工具包」的第 7 步。这是工具包的最后一步；串联全部 7 步的合集见 [AI 创业 Skill 包 ai-startup-skills](https://github.com/huaxialucaicaizi/ai-startup-skills)。

**痛点**
- 个体户、个人独资、有限公司分不清，网上说法互相矛盾
- 不知道一人有限公司的"财产混同"风险具体指什么
- 注册要准备什么、经营范围怎么填、地址能不能用园区工位
- 注册后忘了年报、变更登记，被列入异常

<a id="zh-diff"></a>
### 它和直接问 AI 有什么不同

| 直接问 AI | 用 opc-registration-compliance |
|---|---|
| 凭印象说"有限公司更好""个体户税更低" | 只按已核实的法律条款对比，没收录的方面写"以主管部门最新规定为准" |
| 编出办理天数、费用、税率 | 只引用条例原文中的时限；不给未核实的数字 |
| 推荐挂靠地址等灰色做法 | 地址必须真实合法，便利政策只引用官方原文 |
| 没有注册后的提醒 | 生成年报、变更登记、出资期限等合规日历 |

<a id="zh-fit"></a>
### 适合 / 不适合

**适合**
- 准备在中国大陆注册的一人创业者、自由职业者、独立开发者
- 在个体工商户、个人独资企业、一人有限公司之间犹豫
- 已注册、想理清年报、变更、财产独立等合规事项

**不适合**
- 需要律师或会计师出具专业意见
- 外商投资、港澳台及境外主体注册（本 skill 未覆盖）
- 需要税负测算或筹划

<a id="zh-quickstart"></a>
### 快速开始

**1. 安装**（Codex 内置安装器）

```bash
$skill-installer huaxialucaicaizi/opc-registration-compliance
```

或手动克隆到用户技能目录：

```bash
mkdir -p ~/.agents/skills
cd ~/.agents/skills
git clone https://github.com/huaxialucaicaizi/opc-registration-compliance.git
```

其他支持 Agent Skills 的工具（如 Cursor）也可按各自方式安装。规范参考：[OpenAI Codex skills](https://learn.chatgpt.com/docs/build-skills)。

**2. 开始使用**

```text
用 opc-registration-compliance 帮我看看注册成什么：城市 ___，业务 ___，是否有合伙人 / 投资人 ___，是否打算申请政策 ___，注册地址情况 ___
```

<a id="zh-example"></a>
### 示例对话与输出节选

> ⚠️ 以下案例**全部虚构**，仅用于展示输出格式和判断逻辑。

**你：**
```text
我在广州，一个人接 AI 设计外包，客户多是企业。以后可能申请 OPC 社区入驻。注册个体户还是一人有限公司？
```

**输出节选：**

| 方面 | 个体工商户 | 一人有限公司 |
|---|---|---|
| 责任承担 | 本 skill 未收录原文，待核实 | 以认缴出资额为限（公司法第四条）；不能证明财产独立的，对公司债务承担连带责任（第二十三条第三款） |
| 组织机构 | — | 不设股东会，股东决定书面化（第六十条） |
| 出资 | — | 五年内缴足认缴出资（第四十七条） |
| 税负 | 以税务机关最新规定为准 | 以税务机关最新规定为准 |

需要你确认：
1. 打算申请的 OPC 社区政策是否要求企业法人？（以政策原文为准，可用 opc-policy-navigator 查询）
2. 能否做到公司收支全部走公司账户？

> 以上为信息指引，不构成法律或财税意见，具体以主管部门最新规定为准。信息核实日期：2026-10-22。

<a id="zh-workflow"></a>
### 工作流

1. **主体形式对比**：责任承担、组织机构、出资、转型，每条附条款出处
2. **注册步骤与材料清单**：登记事项、备案事项、申请材料、办理时限、办理入口
3. **注册后合规日历**：年报、变更登记、歇业、财产独立、出资期限
4. **风险提示**：一人公司财产独立，以及广告、标价、AI 服务等经营中常见规定

<a id="zh-principles"></a>
### 原则

- **只引用已核实的官方原文**（中国政府网、中国人大网、国家市场监督管理总局、国家税务总局等）
- **不给未核实的数字**：税率、费用、办理天数一律不写，时限只引用条例原文
- **地址真实合法**，不推荐挂靠等做法
- **非法律意见**：具体以主管部门最新规定为准

<a id="zh-structure"></a>
### 目录结构

```text
SKILL.md                              # 主流程
references/
  entity-comparison.md                # 主体形式对比（附条款）
  registration-steps.md               # 注册步骤与材料清单
  post-registration-compliance.md     # 注册后合规日历
templates/registration-plan.md        # 输出模板
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
| 6. 定价与成交 | [opc-pricing-sales](https://github.com/huaxialucaicaizi/opc-pricing-sales) |
| 7. 注册与合规 | [opc-registration-compliance](https://github.com/huaxialucaicaizi/opc-registration-compliance)（本仓库） |
| AI 创业 Skill 包（全套 7 步） | [ai-startup-skills](https://github.com/huaxialucaicaizi/ai-startup-skills) |

<a id="zh-faq"></a>
### 常见问题

**Q：能直接告诉我选哪个吗？**<br>
A：不能替你决定。会给出带条款出处的对比和需要你确认的问题，由你选择。

**Q：哪个税更低？**<br>
A：本 skill 不做税负比较，请以税务机关最新规定为准，必要时咨询专业人士。

**Q：可以用园区工位注册吗？**<br>
A：条例允许省级政府作出更便利的住所规定；具体以当地官方政策为准，可用 opc-policy-navigator 查询。

**Q：注册要多少天？**<br>
A：条例规定：材料齐全的当场登记，不能当场登记的 3 个工作日内登记，情形复杂可再延长 3 个工作日。实际以当地为准。

**Q：支持外资或港澳台主体吗？**<br>
A：暂不覆盖。

<a id="zh-contrib"></a>
### 贡献与反馈

- 发现问题或有补充：欢迎提 [Issue](https://github.com/huaxialucaicaizi/opc-registration-compliance/issues)
- 提交 PR 前请运行 `python3 scripts/validate.py`
- 补充或更新条款时，必须附中国政府网、中国人大网或主管部门官方原文链接，并写核实日期

<a id="zh-author"></a>
### 作者

**华夏路菜菜子**：前大厂 AI 产品增长，现 AI 创业者，「一人公司工具包」作者。

- GitHub：[@huaxialucaicaizi](https://github.com/huaxialucaicaizi)

如果这个 skill 对你有帮助，欢迎点个 Star ⭐

### Star History

[![Star History Chart](https://api.star-history.com/svg?repos=huaxialucaicaizi/opc-registration-compliance&type=Date)](https://star-history.com/#huaxialucaicaizi/opc-registration-compliance&Date)

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

An Agent Skill that helps solo founders in mainland China choose an entity, register and stay compliant: compares individual businesses, sole proprietorships and one-shareholder limited companies by liability, governance and capital (each with the legal article), builds a registration checklist, and creates a post-registration compliance calendar (annual reports, change filings, asset separation). Information only, not legal or tax advice.

> Step 7 of the "One-Person Company Toolkit". This is the last step; the full bundle of all 7 steps is at [AI Startup Skills – ai-startup-skills](https://github.com/huaxialucaicaizi/ai-startup-skills).

**The problem**
- Confused between entity types; online advice contradicts itself
- Unclear what the one-shareholder "asset commingling" risk means
- Unsure what registration needs, how to fill business scope, whether a park desk address works
- Forgetting annual reports or change filings after registration

<a id="en-diff"></a>
### How It Differs from Just Asking an AI

| Just asking an AI | Using opc-registration-compliance |
|---|---|
| "Companies are better", "individual businesses pay less tax" from memory | Compares only verified legal articles; everything else defers to authorities |
| Invents processing days, fees or tax rates | Only time limits stated in the regulation; no unverified numbers |
| Suggests nominee addresses | Address must be real and lawful; local facilitation only from official texts |
| No post-registration reminders | Compliance calendar for annual reports, changes and capital deadlines |

<a id="en-fit"></a>
### Good Fit / Not a Fit

**Good fit**
- Solo founders, freelancers and indie developers registering in mainland China
- Choosing between individual business, sole proprietorship and one-shareholder company
- Already registered and organizing ongoing compliance

**Not a fit**
- Formal legal or accounting opinions
- Foreign-invested, Hong Kong/Macau/Taiwan or overseas entities (not covered)
- Tax calculations or planning

<a id="en-quickstart"></a>
### Quick Start

**1. Install** (Codex built-in installer)

```bash
$skill-installer huaxialucaicaizi/opc-registration-compliance
```

Or clone into your user skills directory:

```bash
mkdir -p ~/.agents/skills
cd ~/.agents/skills
git clone https://github.com/huaxialucaicaizi/opc-registration-compliance.git
```

Other Agent Skills-compatible tools (e.g. Cursor) can install it in their own way. Spec: [OpenAI Codex skills](https://learn.chatgpt.com/docs/build-skills).

**2. Use it**

```text
Use opc-registration-compliance to help me choose an entity: city ___, business ___, partners/investors ___, policy plans ___, address ___
```

<a id="en-example"></a>
### Example Conversation and Output Excerpt

> ⚠️ The case below is **entirely fictional**, shown only to illustrate the output format and decision logic.

**You:**
```text
I'm in Guangzhou doing AI design outsourcing alone, mostly for companies. May apply to an OPC community later. Individual business or one-shareholder company?
```

**Output excerpt:**

| Aspect | Individual business | One-shareholder company |
|---|---|---|
| Liability | Not in this skill's verified sources (TBD) | Limited to subscribed capital (Company Law Art. 4); joint liability if asset independence can't be proven (Art. 23(3)) |
| Governance | — | No shareholders' meeting; written decisions (Art. 60) |
| Capital | — | Subscribed capital paid within 5 years (Art. 47) |
| Tax | Per tax authority | Per tax authority |

To confirm:
1. Does the OPC community policy require a legal-person entity? (check the policy text)
2. Can all company income and expenses go through a company account?

> Information only, not legal or tax advice. Verified: 2026-10-22.

<a id="en-workflow"></a>
### Workflow

1. **Entity comparison** with legal articles
2. **Registration checklist**: items, filings, documents, time limits, portal
3. **Compliance calendar**: annual report, changes, suspension, asset separation, capital deadline
4. **Risk notes**

<a id="en-principles"></a>
### Principles

- **Official sources only**
- **No unverified numbers**: no tax rates, fees or processing days beyond the regulation
- **Real, lawful addresses only**
- **Not legal advice**; defer to the latest official rules

<a id="en-structure"></a>
### Structure

```text
SKILL.md
references/
  entity-comparison.md
  registration-steps.md
  post-registration-compliance.md
templates/registration-plan.md
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
| 6. Pricing & Closing | [opc-pricing-sales](https://github.com/huaxialucaicaizi/opc-pricing-sales) |
| 7. Registration & Compliance | [opc-registration-compliance](https://github.com/huaxialucaicaizi/opc-registration-compliance) (this repo) |
| AI Startup Skills (all 7 steps) | [ai-startup-skills](https://github.com/huaxialucaicaizi/ai-startup-skills) |

<a id="en-faq"></a>
### FAQ

**Q: Can it choose for me?**<br>
A: No. You get a sourced comparison and questions to decide.

**Q: Which pays less tax?**<br>
A: No tax comparisons; check with the tax authority.

**Q: Can I use a park desk address?**<br>
A: The regulation allows provincial facilitation; check local official policies.

**Q: How long does registration take?**<br>
A: Per the regulation: same day if complete, otherwise within 3 working days, extendable by 3 in complex cases. Local practice may vary.

**Q: Foreign or HK/Macau/Taiwan entities?**<br>
A: Not covered.

<a id="en-contrib"></a>
### Contributing & Feedback

- Found a problem or have something to add? Open an [Issue](https://github.com/huaxialucaicaizi/opc-registration-compliance/issues)
- Run `python3 scripts/validate.py` before submitting a PR
- Any added or updated article must link to the official source and include a verification date

<a id="en-author"></a>
### Author

**华夏路菜菜子 (huaxialucaicaizi)**: former AI product growth lead at major Chinese tech companies, now an AI founder; author of the One-Person Company Toolkit.

- GitHub: [@huaxialucaicaizi](https://github.com/huaxialucaicaizi)

If this skill helps you, a Star ⭐ is appreciated.

### Star History

[![Star History Chart](https://api.star-history.com/svg?repos=huaxialucaicaizi/opc-registration-compliance&type=Date)](https://star-history.com/#huaxialucaicaizi/opc-registration-compliance&Date)

<a id="en-license"></a>
### License

[MIT](LICENSE)

[↑ Back to top](#top)

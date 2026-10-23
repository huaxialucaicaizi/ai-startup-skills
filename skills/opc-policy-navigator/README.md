<a id="top"></a>

<div align="center">

# OPC Policy Navigator · 一人公司政策导航 Skill

**我能申什么？要准备什么？文案怎么写？——只引用已核实的官方政策原文。**<br>
Find China startup policies, subsidies and OPC community support you can apply for — official sources only.

[![CI](https://github.com/huaxialucaicaizi/opc-policy-navigator/actions/workflows/ci.yml/badge.svg)](https://github.com/huaxialucaicaizi/opc-policy-navigator/actions/workflows/ci.yml)
[![License: MIT](https://img.shields.io/github/license/huaxialucaicaizi/opc-policy-navigator)](LICENSE)
[![GitHub stars](https://img.shields.io/github/stars/huaxialucaicaizi/opc-policy-navigator?style=social)](https://github.com/huaxialucaicaizi/opc-policy-navigator)
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

一个面向中国一人公司（OPC）和早期创业者的 Agent Skill：按**城市 / 区 + 赛道 + 阶段**，先比对国家级政策、再比对地方政策（北京、上海、广州、深圳及杭州），把结果分成"大概率可申 / 需确认条件 / 暂不适用"三档，并给出官方链接、材料清单和申报文案框架。

> 这是「一人公司工具包」的第 3 步。上一步写 BP 可用 [business-plan-skill](https://github.com/huaxialucaicaizi/business-plan-skill)；下一步路演可用 [ai-pitch-coach](https://github.com/huaxialucaicaizi/ai-pitch-coach)。

**痛点**
- 政策文件多、分散在各级政府网站，不知道哪些和自己有关
- 网上二手解读常把"最高 X 万元"说成"能拿 X 万元"
- 不清楚自己卡在哪个门槛（年龄、社保、注册地、成立年限）
- 材料和申报文案不知道从哪写起

<a id="zh-diff"></a>
### 它和直接问 AI 有什么不同

| 直接问 AI | 用 opc-policy-navigator |
|---|---|
| 可能凭印象编出政策名、金额、截止日期 | 只引用政策库中已核实的政策，每条附官方链接和核实日期 |
| 不区分国家级和地方政策 | 先国家、再省市区，城市未收录时如实说明并给官方查询入口 |
| 笼统地说"你可以申请" | 三档分类，并列出缺哪项信息、向谁确认 |
| 没有材料清单 | 材料清单分"已有证明 / 用户自述 / 待补充"三种状态 |

<a id="zh-fit"></a>
### 适合 / 不适合

**适合**
- 在北京、上海、广州、深圳（或杭州）注册或打算注册的一人公司、早期团队
- 想申请 OPC 社区入驻、算力券 / 模型券、创业担保贷款、小微企业税费优惠等
- 需要一份有官方出处的政策清单和申报文案框架

**不适合**
- 政策库未收录城市的地方政策（只能给国家级结果和官方查询入口）
- 需要代办申报或法律、财税意见
- 想要"保证能拿到"的承诺

<a id="zh-quickstart"></a>
### 快速开始

**1. 安装**（Codex 内置安装器）

```bash
$skill-installer huaxialucaicaizi/opc-policy-navigator
```

或手动克隆到用户技能目录：

```bash
mkdir -p ~/.agents/skills
cd ~/.agents/skills
git clone https://github.com/huaxialucaicaizi/opc-policy-navigator.git
```

其他支持 Agent Skills 的工具（如 Cursor）也可按各自方式安装。规范参考：[OpenAI Codex skills](https://learn.chatgpt.com/docs/build-skills)。

**2. 开始使用**

```text
用 opc-policy-navigator 帮我看看能申什么：城市/区 ___，赛道 ___，阶段 ___（是否注册、成立多久、是否入驻园区），创始人情况 ___
```

<a id="zh-example"></a>
### 示例对话与输出节选

> ⚠️ 以下案例**全部虚构**，仅用于展示输出格式和判断逻辑。

**你：**
```text
我在上海杨浦，做 AI 简历优化工具，一个人，还没注册公司，打算入驻 OPC 社区。能申什么？
```

**输出节选：**

| 档位 | 政策 | 与你相关的要点 | 为什么在这一档 |
|---|---|---|---|
| 需确认条件 | 杨浦区《关于支持打造 OPC 超级个体社区的若干措施》（杨府发〔2026〕4号） | 入驻经认定 OPC 社区的 OPC 企业首年全额减免房租及物业费；创新券最高 50%、每年最高 20 万元 | 尚未注册企业、尚未入驻经认定社区，需先完成注册和入驻 |
| 需确认条件 | 小微企业和个体工商户税费政策（国家级） | 以公告原文为准 | 注册后按主体类型和纳税情况确认 |
| 只用于文案"政策契合" | 上海市 2026 年度 OPC 社区申报通知 | 市级 OPC 定义：以人工智能驱动经营活动、员工 10 人及以下 | 面向社区运营方，不是对企业的直接资助 |

> 以上信息以主管部门最新政策和申报通知为准。信息核实日期：2026-10-22。

<a id="zh-workflow"></a>
### 工作流

1. **收集信息**：城市 / 区、赛道、阶段、创始人情况（缺的标"待补充"）
2. **先国家、再地方**：国家级政策库 → 省 / 市 / 区政策库；未收录城市如实告知
3. **三档分类**：大概率可申 / 需确认条件 / 暂不适用，并写明理由
4. **材料清单**：已有证明 / 用户自述 / 待补充
5. **申报文案框架**：按模板输出，正文可用已有 BP

<a id="zh-principles"></a>
### 原则

- **不编造政策、金额、条件、截止日期**：政策库没有的回答"未收录"
- **"最高 X 万元"不写成"可获得 X 万元"**
- **每条政策附官方链接和核实日期**；政策会调整，以主管部门最新通知为准
- **不构成法律或财税意见，不代办申报**

<a id="zh-structure"></a>
### 目录结构

```text
SKILL.md                              # 主流程
references/
  policy-db-national.md               # 国家级政策库
  policy-db-beijing.md                # 北京（含海淀）
  policy-db-shanghai.md               # 上海（含杨浦、徐汇）
  policy-db-guangzhou.md              # 广东省级 + 广州（含海珠、白云）
  policy-db-shenzhen.md               # 深圳（含南山）
  policy-db-other-cities.md           # 杭州
  materials-checklist.md              # 材料清单
  application-copy-framework.md       # 申报文案框架
templates/policy-match-report.md      # 输出模板
agents/openai.yaml
scripts/validate.py
```

<a id="zh-kit"></a>
### 一人公司工具包

| 步骤 | 仓库 |
|---|---|
| 1. AI 产品 MVP 验证 | [ai-mvp-validation](https://github.com/huaxialucaicaizi/ai-mvp-validation) |
| 2. 商业计划书 | [business-plan-skill](https://github.com/huaxialucaicaizi/business-plan-skill) |
| 3. 政策与补贴 | [opc-policy-navigator](https://github.com/huaxialucaicaizi/opc-policy-navigator)（本仓库） |
| 4. 路演教练 | [ai-pitch-coach](https://github.com/huaxialucaicaizi/ai-pitch-coach) |
| 5. 增长获客 | [opc-growth-playbook](https://github.com/huaxialucaicaizi/opc-growth-playbook) |
| 6. 定价与成交 | [opc-pricing-sales](https://github.com/huaxialucaicaizi/opc-pricing-sales) |
| 7. 注册与合规 | [opc-registration-compliance](https://github.com/huaxialucaicaizi/opc-registration-compliance) |
| AI 创业 Skill 包（全套 7 步） | [ai-startup-skills](https://github.com/huaxialucaicaizi/ai-startup-skills) |

<a id="zh-faq"></a>
### 常见问题

**Q：政策库多久更新？**<br>
A：政策库标注了信息核实日期（当前为 2026-10-22）。政策会调整，使用前请到官方链接确认最新版本。

**Q：我的城市没有收录怎么办？**<br>
A：skill 会如实告知，只给国家级结果，并给出中国政府网政策文件库、国家政务服务平台等官方查询入口。

**Q：能帮我直接提交申报吗？**<br>
A：不能。本 skill 只做信息整理和文案辅助。

**Q："已截止"的政策还会显示吗？**<br>
A：会归入"需确认条件"，提示关注下一批次通知。

**Q：想补充新的城市政策？**<br>
A：欢迎提 Issue 或 PR，并附政策原文的官方政府网站链接。

<a id="zh-contrib"></a>
### 贡献与反馈

- 发现问题或有补充：欢迎提 [Issue](https://github.com/huaxialucaicaizi/opc-policy-navigator/issues)
- 提交 PR 前请运行 `python3 scripts/validate.py`
- 新增或更新政策时，必须附政策原文的官方政府网站链接、文号和核实日期

<a id="zh-author"></a>
### 作者

**华夏路菜菜子**：前大厂 AI 产品增长，现 AI 创业者，「一人公司工具包」作者。

- GitHub：[@huaxialucaicaizi](https://github.com/huaxialucaicaizi)

如果这个 skill 对你有帮助，欢迎点个 Star ⭐

### Star History

[![Star History Chart](https://api.star-history.com/svg?repos=huaxialucaicaizi/opc-policy-navigator&type=Date)](https://star-history.com/#huaxialucaicaizi/opc-policy-navigator&Date)

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

An Agent Skill for one-person companies (OPC) and early-stage founders in China: given city / district, industry and stage, it matches national policies first, then local ones (Beijing, Shanghai, Guangzhou, Shenzhen, plus Hangzhou), sorts them into "likely eligible / needs confirmation / not applicable", and outputs official links, a materials checklist and an application outline.

> Step 3 of the "One-Person Company Toolkit". Previous step: [business-plan-skill](https://github.com/huaxialucaicaizi/business-plan-skill). Next step: rehearse your pitch with [ai-pitch-coach](https://github.com/huaxialucaicaizi/ai-pitch-coach).

**The problem**
- Policies are scattered across many government sites
- Second-hand summaries turn "up to X" into "you get X"
- Unclear which threshold blocks you (age, social insurance, registration, company age)
- No idea how to start the materials and application text

<a id="en-diff"></a>
### How It Differs from Just Asking an AI

| Just asking an AI | Using opc-policy-navigator |
|---|---|
| May invent policy names, amounts or deadlines | Only cites verified policies, each with an official link and date |
| Mixes national and local policies | National first, then province / city / district; says so honestly when a city is not covered |
| Vague "you can apply" | Three tiers, listing what is missing and whom to ask |
| No materials list | Checklist marked "proven / self-reported / to be added" |

<a id="en-fit"></a>
### Good Fit / Not a Fit

**Good fit**
- One-person companies and early teams in Beijing, Shanghai, Guangzhou, Shenzhen (or Hangzhou)
- Applying for OPC community admission, compute / model vouchers, startup guarantee loans, small-business tax relief
- Need a policy list with official sources and an application outline

**Not a fit**
- Local policies for cities not in the database (national results and official search portals only)
- Filing on your behalf, or legal / tax advice
- Anyone wanting a guarantee of approval

<a id="en-quickstart"></a>
### Quick Start

**1. Install** (Codex built-in installer)

```bash
$skill-installer huaxialucaicaizi/opc-policy-navigator
```

Or clone into your user skills directory:

```bash
mkdir -p ~/.agents/skills
cd ~/.agents/skills
git clone https://github.com/huaxialucaicaizi/opc-policy-navigator.git
```

Other Agent Skills-compatible tools (e.g. Cursor) can install it in their own way. Spec: [OpenAI Codex skills](https://learn.chatgpt.com/docs/build-skills).

**2. Use it**

```text
Use opc-policy-navigator to find policies I can apply for: city/district ___, industry ___, stage ___, founder profile ___
```

<a id="en-example"></a>
### Example Conversation and Output Excerpt

> ⚠️ The case below is **entirely fictional**, shown only to illustrate the output format and decision logic.

**You:**
```text
I'm in Yangpu, Shanghai, building an AI resume tool alone, not yet registered, planning to join an OPC community. What can I apply for?
```

**Output excerpt:**

| Tier | Policy | Relevant points | Why |
|---|---|---|---|
| Needs confirmation | Yangpu District OPC community measures (杨府发〔2026〕4号) | First-year rent and property fee waiver for OPC companies in certified communities; innovation vouchers up to 50%, up to RMB 200k per year | Not yet registered and not yet in a certified community |
| Needs confirmation | National small-business tax relief | Per the official announcement | Confirm after registration, by entity type |
| For "policy fit" text only | Shanghai 2026 OPC community notice | City-level OPC definition: AI-driven, 10 or fewer employees | Targets community operators, not direct funding |

> Subject to the latest official policies and notices. Verified: 2026-10-22.

<a id="en-workflow"></a>
### Workflow

1. **Collect**: city / district, industry, stage, founder profile (missing items marked "TBD")
2. **National first, then local**; uncovered cities are stated honestly
3. **Three tiers** with reasons
4. **Materials checklist**
5. **Application outline** from the template

<a id="en-principles"></a>
### Principles

- **No invented policies, amounts, conditions or deadlines**
- **"Up to X" is never written as "you get X"**
- **Every policy has an official link and verification date**; always defer to the latest official notice
- **Not legal or tax advice; does not file on your behalf**

<a id="en-structure"></a>
### Structure

```text
SKILL.md                              # main workflow
references/
  policy-db-national.md               # national policies
  policy-db-beijing.md                # Beijing (incl. Haidian)
  policy-db-shanghai.md               # Shanghai (incl. Yangpu, Xuhui)
  policy-db-guangzhou.md              # Guangdong + Guangzhou
  policy-db-shenzhen.md               # Shenzhen (incl. Nanshan)
  policy-db-other-cities.md           # Hangzhou
  materials-checklist.md
  application-copy-framework.md
templates/policy-match-report.md      # output template
agents/openai.yaml
scripts/validate.py
```

<a id="en-kit"></a>
### One-Person Company Toolkit

| Step | Repository |
|---|---|
| 1. AI MVP Validation | [ai-mvp-validation](https://github.com/huaxialucaicaizi/ai-mvp-validation) |
| 2. Business Plan | [business-plan-skill](https://github.com/huaxialucaicaizi/business-plan-skill) |
| 3. Policy & Subsidies | [opc-policy-navigator](https://github.com/huaxialucaicaizi/opc-policy-navigator) (this repo) |
| 4. Roadshow Coach | [ai-pitch-coach](https://github.com/huaxialucaicaizi/ai-pitch-coach) |
| 5. Growth | [opc-growth-playbook](https://github.com/huaxialucaicaizi/opc-growth-playbook) |
| 6. Pricing & Closing | [opc-pricing-sales](https://github.com/huaxialucaicaizi/opc-pricing-sales) |
| 7. Registration & Compliance | [opc-registration-compliance](https://github.com/huaxialucaicaizi/opc-registration-compliance) |
| AI Startup Skills (all 7 steps) | [ai-startup-skills](https://github.com/huaxialucaicaizi/ai-startup-skills) |

<a id="en-faq"></a>
### FAQ

**Q: How current is the database?**<br>
A: Each file has a verification date (currently 2026-10-22). Always check the official link for the latest version.

**Q: My city is not covered?**<br>
A: You get national results plus official search portals; no local policies are made up.

**Q: Can it file the application for me?**<br>
A: No. It only organizes information and drafts text.

**Q: What about closed batches?**<br>
A: They go under "needs confirmation", with a reminder to watch for the next batch.

**Q: Want to add a city?**<br>
A: Open an Issue or PR with the official government source link.

<a id="en-contrib"></a>
### Contributing & Feedback

- Found a problem or have something to add? Open an [Issue](https://github.com/huaxialucaicaizi/opc-policy-navigator/issues)
- Run `python3 scripts/validate.py` before submitting a PR
- New or updated policies must include the official government link, document number and verification date

<a id="en-author"></a>
### Author

**华夏路菜菜子 (huaxialucaicaizi)**: former AI product growth lead at major Chinese tech companies, now an AI founder; author of the One-Person Company Toolkit.

- GitHub: [@huaxialucaicaizi](https://github.com/huaxialucaicaizi)

If this skill helps you, a Star ⭐ is appreciated.

### Star History

[![Star History Chart](https://api.star-history.com/svg?repos=huaxialucaicaizi/opc-policy-navigator&type=Date)](https://star-history.com/#huaxialucaicaizi/opc-policy-navigator&Date)

<a id="en-license"></a>
### License

[MIT](LICENSE)

[↑ Back to top](#top)

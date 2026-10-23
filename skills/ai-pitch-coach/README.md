<a id="top"></a>

<div align="center">

# Roadshow Pitch Coach · 园区路演教练 Skill

**为政府园区、OPC 社区和创业大赛准备 3 / 5 分钟路演与答辩，不夸大、不编数据。**<br>
Prepare 3- and 5-minute pitches and judge Q&A for China government parks, OPC communities and startup competitions.

[![CI](https://github.com/huaxialucaicaizi/ai-pitch-coach/actions/workflows/ci.yml/badge.svg)](https://github.com/huaxialucaicaizi/ai-pitch-coach/actions/workflows/ci.yml)
[![License: MIT](https://img.shields.io/github/license/huaxialucaicaizi/ai-pitch-coach)](LICENSE)
[![GitHub stars](https://img.shields.io/github/stars/huaxialucaicaizi/ai-pitch-coach?style=social)](https://github.com/huaxialucaicaizi/ai-pitch-coach)
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

一个专做**政府园区、OPC 社区入驻、孵化器、创业大赛**现场路演和答辩的 Agent Skill：生成带时间分配的 3 / 5 分钟逐字稿，按场合从评委题库中挑题并写回答要点，模拟答辩，再给出排练清单。面向风险投资人的融资路演不是本 skill 的重点。

> 这是「一人公司工具包」的第 4 步。下一步：[增长获客 opc-growth-playbook](https://github.com/huaxialucaicaizi/opc-growth-playbook)。

**痛点**
- 3 分钟讲不完，或者讲完评委还是不知道你做什么
- 园区评委常问落地、纳税、就业、"一个人怎么交付"，不知道怎么答
- 被问到短板时容易夸大或回避
- 照着 BP 念稿，没有排练和计时

<a id="zh-diff"></a>
### 它和直接问 AI 有什么不同

| 直接问 AI | 用 ai-pitch-coach |
|---|---|
| 给一份通用的融资路演结构 | 针对园区 / OPC 社区 / 大赛评委的 3 / 5 分钟结构 |
| 讲稿里容易出现编出来的数字和客户 | 数字、客户、奖项只能来自你的材料，没有就写"待补充" |
| 不会模拟评委追问 | 从分类题库挑题，一次问一题并点评 |
| 回避短板 | 短板按"承认 + 已有应对 + 下一步计划"诚实回答 |

<a id="zh-fit"></a>
### 适合 / 不适合

**适合**
- 参加园区入驻评审、OPC 社区入驻、孵化器面试、创业大赛的一人公司或小团队
- 需要 3 分钟或 5 分钟版本的逐字稿和答辩准备

**不适合**
- 面向风险投资人的融资路演（可参考，但不是重点）
- 需要设计 PPT 视觉稿（本 skill 只做讲稿和问答）
- 希望把没做到的事讲成已做到

<a id="zh-quickstart"></a>
### 快速开始

**1. 安装**（Codex 内置安装器）

```bash
$skill-installer huaxialucaicaizi/ai-pitch-coach
```

或手动克隆到用户技能目录：

```bash
mkdir -p ~/.agents/skills
cd ~/.agents/skills
git clone https://github.com/huaxialucaicaizi/ai-pitch-coach.git
```

其他支持 Agent Skills 的工具（如 Cursor）也可按各自方式安装。规范参考：[OpenAI Codex skills](https://learn.chatgpt.com/docs/build-skills)。

**2. 开始使用**

```text
用 ai-pitch-coach 帮我准备 ___ 分钟路演，场合：___（园区入驻 / OPC 社区 / 创业大赛），这是我的 BP / 项目介绍：___
```

<a id="zh-example"></a>
### 示例对话与输出节选

> ⚠️ 以下案例**全部虚构**，仅用于展示输出格式和判断逻辑。

**你：**
```text
下周要参加上海杨浦 OPC 社区入驻评审，3 分钟。我一个人做 AI 简历优化工具，有 2 个付费用户（有付款记录），还没注册公司。
```

**输出节选：**

| 段落 | 时间 | 逐字稿（节选） |
|---|---|---|
| 开场 | 0:00–0:20 | 我是 ___，一个人用 AI 工作流做"简历优化工具"，帮求职者 ___。 |
| 进展 | 1:50–2:30 | 目前有 2 位付费用户，付款记录可现场出示；更多用户数据：待补充。 |
| 诉求与落地 | 2:30–3:00 | 希望入驻社区；入驻后 ___ 内完成在杨浦注册（时间：待补充）。 |

| 类别 | 问题（题号） | 回答要点 |
|---|---|---|
| 落地与政策 | 公司注册在哪里？多久内完成？（A1） | 目前未注册；计划时间：待补充，不要临场承诺做不到的时间 |
| 一人公司 | 只有你一个人，怎么保证交付？（B7） | 说明 AI 工具分工和需要人工的环节；外部合作方：待补充 |

<a id="zh-workflow"></a>
### 工作流

1. **选结构**：3 分钟或 5 分钟，生成逐字稿，标注每段时间和 PPT 页
2. **计时校准**：按你的实测语速估算字数，超时就删内容
3. **问答准备**：按场合从题库挑题（3 分钟版 8–10 题，5 分钟版 10–15 题），写回答要点
4. **模拟答辩**：一次一题，点评是否答到点、是否超时、是否有无法核实的说法
5. **叙事模块（可选）**：验证进度页、分阶段路线页、先本地验证→区域复制
6. **排练清单**

<a id="zh-principles"></a>
### 原则

- **数字、客户、奖项、融资只来自你的材料**，没有就写"待补充"
- **不夸大、不回避**：短板用"承认 + 已有应对 + 下一步计划"
- **政策说法必须有官方出处**
- **时间以主办方规定和实际计时为准**

<a id="zh-structure"></a>
### 目录结构

```text
SKILL.md                          # 主流程
references/
  speech-templates.md             # 3 / 5 分钟讲稿结构 + 排练清单
  judge-qa-bank.md                # 评委问答题库（分类）
  story-modules.md                # 叙事模块：验证进度、分阶段路线、本地验证→区域复制
templates/roadshow-output.md      # 输出模板
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
| 4. 路演教练 | [ai-pitch-coach](https://github.com/huaxialucaicaizi/ai-pitch-coach)（本仓库） |
| 5. 增长获客 | [opc-growth-playbook](https://github.com/huaxialucaicaizi/opc-growth-playbook) |
| 6. 定价与成交 | [opc-pricing-sales](https://github.com/huaxialucaicaizi/opc-pricing-sales) |
| 7. 注册与合规 | [opc-registration-compliance](https://github.com/huaxialucaicaizi/opc-registration-compliance) |
| AI 创业 Skill 包（全套 7 步） | [ai-startup-skills](https://github.com/huaxialucaicaizi/ai-startup-skills) |

<a id="zh-faq"></a>
### 常见问题

**Q：主办方要求 8 分钟怎么办？**<br>
A：按比例调整 5 分钟结构，并以主办方规定为准。

**Q：没有 BP 能用吗？**<br>
A：可以，先口头介绍项目，缺的内容会标"待补充"。有 BP 效果更好。

**Q：题库里的题是真题吗？**<br>
A：不是，是常见提问方向的归纳，不代表某个具体评审的真实题目。

**Q：可以用于融资路演吗？**<br>
A：可以参考，但本 skill 的结构和题库是按政府园区、OPC 社区、大赛设计的。

**Q：讲稿里的政策从哪来？**<br>
A：只用你提供的、带官方链接的政策原文；可以先用 opc-policy-navigator 查询。

<a id="zh-contrib"></a>
### 贡献与反馈

- 发现问题或有补充：欢迎提 [Issue](https://github.com/huaxialucaicaizi/ai-pitch-coach/issues)
- 提交 PR 前请运行 `python3 scripts/validate.py`
- 补充题库时请注明适用场合，只写提问方向，不写某个具体评审的未公开题目

<a id="zh-author"></a>
### 作者

**华夏路菜菜子**：前大厂 AI 产品增长，现 AI 创业者，「一人公司工具包」作者。

- GitHub：[@huaxialucaicaizi](https://github.com/huaxialucaicaizi)

如果这个 skill 对你有帮助，欢迎点个 Star ⭐

### Star History

[![Star History Chart](https://api.star-history.com/svg?repos=huaxialucaicaizi/ai-pitch-coach&type=Date)](https://star-history.com/#huaxialucaicaizi/ai-pitch-coach&Date)

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

An Agent Skill for live pitches and defenses at **China government parks, OPC communities, incubators and startup competitions**: 3- and 5-minute scripts with timing, judge Q&A picked from a categorized bank, mock defense and a rehearsal checklist. Not focused on VC fundraising pitches.

> Step 4 of the "One-Person Company Toolkit". Next step: [Growth – opc-growth-playbook](https://github.com/huaxialucaicaizi/opc-growth-playbook).

**The problem**
- Running out of time in 3 minutes, or judges still unsure what you do
- Park judges ask about local commitment, tax, jobs and "how can one person deliver?"
- Tempted to exaggerate or dodge weak points
- Reading the BP aloud without timed rehearsal

<a id="en-diff"></a>
### How It Differs from Just Asking an AI

| Just asking an AI | Using ai-pitch-coach |
|---|---|
| Generic VC pitch structure | 3/5-minute structures for park, OPC and competition judges |
| Made-up numbers and customers | Numbers, customers and awards come only from your materials; otherwise "TBD" |
| No mock Q&A | Picks questions from a categorized bank, one at a time, with feedback |
| Dodges weak points | Honest answers: admit + current mitigation + next step |

<a id="en-fit"></a>
### Good Fit / Not a Fit

**Good fit**
- Solo founders and small teams pitching to parks, OPC communities, incubators or competitions
- Need a 3- or 5-minute script and Q&A prep

**Not a fit**
- VC fundraising pitches (usable, but not the focus)
- Slide visual design (scripts and Q&A only)
- Presenting unfinished work as done

<a id="en-quickstart"></a>
### Quick Start

**1. Install** (Codex built-in installer)

```bash
$skill-installer huaxialucaicaizi/ai-pitch-coach
```

Or clone into your user skills directory:

```bash
mkdir -p ~/.agents/skills
cd ~/.agents/skills
git clone https://github.com/huaxialucaicaizi/ai-pitch-coach.git
```

Other Agent Skills-compatible tools (e.g. Cursor) can install it in their own way. Spec: [OpenAI Codex skills](https://learn.chatgpt.com/docs/build-skills).

**2. Use it**

```text
Use ai-pitch-coach to prepare a ___-minute pitch for ___ (park / OPC community / competition). Here is my BP or project summary: ___
```

<a id="en-example"></a>
### Example Conversation and Output Excerpt

> ⚠️ The case below is **entirely fictional**, shown only to illustrate the output format and decision logic.

**You:**
```text
Next week I pitch for a Yangpu (Shanghai) OPC community, 3 minutes. Solo AI resume tool, 2 paying users (with payment records), company not yet registered.
```

**Output excerpt:**

| Section | Time | Script (excerpt) |
|---|---|---|
| Opening | 0:00–0:20 | I'm ___, running an AI resume tool alone with an AI workflow, helping job seekers ___. |
| Traction | 1:50–2:30 | 2 paying users so far, payment records available; further data: TBD. |
| Ask & commitment | 2:30–3:00 | We'd like to join the community and register in Yangpu within ___ (timeline: TBD). |

| Category | Question (ID) | Answer points |
|---|---|---|
| Local commitment | Where will you register, and when? (A1) | Not yet registered; timeline TBD — don't promise what you can't do |
| One-person company | How can one person deliver? (B7) | Explain AI tool roles and human steps; partners: TBD |

<a id="en-workflow"></a>
### Workflow

1. **Pick a structure** (3 or 5 minutes), script with timing and slide numbers
2. **Calibrate** word count to your measured pace; cut content if over time
3. **Q&A prep** from the question bank, with answer points
4. **Mock defense**, one question at a time
5. **Optional story modules**: validation progress, staged roadmap, local-first then regional
6. **Rehearsal checklist**

<a id="en-principles"></a>
### Principles

- **Numbers, customers, awards and funding only from your materials**
- **No exaggeration, no dodging**
- **Policy claims need official sources**
- **Timing follows the organizer and your measured pace**

<a id="en-structure"></a>
### Structure

```text
SKILL.md                          # main workflow
references/
  speech-templates.md             # 3/5-minute structures + rehearsal checklist
  judge-qa-bank.md                # categorized judge Q&A bank
  story-modules.md                # story modules
templates/roadshow-output.md      # output template
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
| 4. Roadshow Coach | [ai-pitch-coach](https://github.com/huaxialucaicaizi/ai-pitch-coach) (this repo) |
| 5. Growth | [opc-growth-playbook](https://github.com/huaxialucaicaizi/opc-growth-playbook) |
| 6. Pricing & Closing | [opc-pricing-sales](https://github.com/huaxialucaicaizi/opc-pricing-sales) |
| 7. Registration & Compliance | [opc-registration-compliance](https://github.com/huaxialucaicaizi/opc-registration-compliance) |
| AI Startup Skills (all 7 steps) | [ai-startup-skills](https://github.com/huaxialucaicaizi/ai-startup-skills) |

<a id="en-faq"></a>
### FAQ

**Q: The organizer wants 8 minutes?**<br>
A: Scale the 5-minute structure and follow the organizer.

**Q: No BP?**<br>
A: Describe your project; missing parts are marked "TBD".

**Q: Are these real judge questions?**<br>
A: No, they summarize common question directions.

**Q: Usable for VC pitches?**<br>
A: As a reference; the structure targets parks, OPC communities and competitions.

**Q: Where do policy statements come from?**<br>
A: Only official policy texts you provide, e.g. found via opc-policy-navigator.

<a id="en-contrib"></a>
### Contributing & Feedback

- Found a problem or have something to add? Open an [Issue](https://github.com/huaxialucaicaizi/ai-pitch-coach/issues)
- Run `python3 scripts/validate.py` before submitting a PR
- When adding questions, note the setting; describe question directions, not unpublished questions from a specific panel

<a id="en-author"></a>
### Author

**华夏路菜菜子 (huaxialucaicaizi)**: former AI product growth lead at major Chinese tech companies, now an AI founder; author of the One-Person Company Toolkit.

- GitHub: [@huaxialucaicaizi](https://github.com/huaxialucaicaizi)

If this skill helps you, a Star ⭐ is appreciated.

### Star History

[![Star History Chart](https://api.star-history.com/svg?repos=huaxialucaicaizi/ai-pitch-coach&type=Date)](https://star-history.com/#huaxialucaicaizi/ai-pitch-coach&Date)

<a id="en-license"></a>
### License

[MIT](LICENSE)

[↑ Back to top](#top)

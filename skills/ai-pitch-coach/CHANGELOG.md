# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Changed
- SKILL.md 触发描述补齐中文关键词（路演稿、逐字稿、评委问答、模拟答辩、园区入驻、OPC社区、孵化器、政府项目答辩）；输入场合、题库场合优先级、README 快速开始与 agents/openai.yaml 同步加上「孵化器」
- SKILL.md description: add Chinese trigger phrases (script, verbatim draft, judge Q&A, mock defense, park admission, OPC community, incubator, government project defense); add incubator to input settings, question-bank occasion priorities, README quick start, and agents/openai.yaml
- README 中文工作流补齐问答准备规则：优先使用已有 BP 评审追问，再按题库场合优先级补足 3 分钟版 8–10 题或 5 分钟版 10–15 题（与英文工作流、SKILL.md 对齐）
- README Chinese workflow now prioritizes questions from existing BP review feedback, then follows the question bank's setting priorities to reach 8–10 questions for 3 minutes or 10–15 for 5 minutes (aligned with the English workflow and SKILL.md)
- README 英文工作流补齐问答准备规则：优先使用已有 BP 评审追问，再按场合补足 3 分钟版 8–10 题或 5 分钟版 10–15 题
- README English workflow now prioritizes questions from existing BP review feedback, then follows setting priorities to reach 8–10 questions for 3 minutes or 10–15 for 5 minutes
- 评委题库补上题号格式（A1、B7）和按场合优先类别；SKILL.md 第 3 步改为按该文首选题，与 README 示例对齐
- Judge Q&A bank: add IDs (A1, B7) and occasion-priority categories; SKILL.md step 3 now follows that intro, matching the README examples
- SKILL.md 新增「可选衔接」：有第 1 / 2 / 3 步产出时，分别用于验证进度、讲稿材料和「诉求与落地」；硬性规则里的政策查询补上 opc-policy-navigator 链接
- SKILL.md: add optional companion-step section (steps 1–3 feed validation progress, script materials, and the ask/commitment close); link opc-policy-navigator in the policy rule
- LICENSE / README：新增未经许可不得上架第三方 AI 产品、Skill 商店的条款；授权联系仍为 @huaxialucaicaizi
- LICENSE / README: added a clause forbidding listing on third-party AI products or skill stores without prior author permission; contact remains @huaxialucaicaizi
- 许可证由 MIT 改为非商业许可；转载或商用需联系 @huaxialucaicaizi
- License changed from MIT to a non-commercial license; republication or commercial use requires contacting @huaxialucaicaizi
- README「一人公司工具包」表格：每个仓库链接后附加粗的英文名 · 中文名，命名与 ai-startup-skills 合集一致
- README "One-Person Company Toolkit" table: each repository link now shows its bold English name, matching the ai-startup-skills bundle
- README「一人公司工具包」表格：去掉重复的仓库短名链接，改为直接用加粗名称作链接，与 opc-policy-navigator、ai-startup-skills 写法一致
- README "One-Person Company Toolkit" table: the bold repository name is now the link itself (duplicate slug link removed), matching opc-policy-navigator and ai-startup-skills
- README 常见问题「讲稿里的政策从哪来」：提到的第 3 步改为加粗名称链接 **OPC Policy Navigator · 一人公司政策导航**
- README FAQ "Where do policy statements come from?": the step 3 mention is now a bold link to **OPC Policy Navigator**

### Fixed
- 输出模板排练清单原先只有空白勾选，现与 `references/speech-templates.md` 末尾 6 项对齐
- Output template rehearsal checklist was a blank stub; now matches the 6 items at the end of `references/speech-templates.md`

## [1.0.0] - 2026-10-22

### Added
- 首个独立版本：政府园区、OPC 社区、孵化器、创业大赛路演教练 skill
- 3 / 5 分钟讲稿结构、分类评委问答题库、模拟答辩、排练清单
- 叙事模块：验证进度页、分阶段路线页、先本地验证→区域复制
- 输出模板（templates/）
- 与 BP 评审、政策导航、想法验证的衔接改为可选
- First standalone release of the roadshow pitch coach

# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- `scripts/validate.py` 新增检查：`references/` 和 `templates/` 中的链接必须指向政府官方域名（`*.gov.cn`），否则校验失败
- `scripts/validate.py` now fails if any link in `references/` or `templates/` is not an official government domain (`*.gov.cn`)

### Changed
- SKILL.md 主体对比维度与 `references/entity-comparison.md` 对齐（去掉未收录的「适合场景」），并明确领照后事项须标「待核实」；`templates/registration-plan.md` 补全对比表、登记事项、领照后与合规日历占位行；README 中英工作流说明同步
- SKILL.md entity-comparison dimensions now match `references/entity-comparison.md` (dropped the unlisted "suitable scenarios" axis) and post-license items must stay "待核实"; `templates/registration-plan.md` fills in placeholder rows for comparison, registration items, post-license follow-ups, and the compliance calendar; README ZH/EN workflow notes aligned
- 输出免责声明不再使用与新近核验条款矛盾的固定核实日期，改为提示查阅 `references/` 中各来源的逐条核实日期；README 示例与输出模板同步
- Output disclaimers now point to per-source verification dates in `references/` instead of a stale fixed date; README examples and the output template are aligned
- 主体对比表：「是否法人」由「待核实」改为摘录《民法典》第五十四条（个体工商户）、第一百零二条（个人独资企业为非法人组织）；国家市场监督管理总局网站原文，2026-11-06 核验；README 中英示例表同步补上该行
- Entity comparison: legal-person row now cites Civil Code Art. 54 (individual business) and Art. 102 (sole proprietorship as an unincorporated organization); SAMR official text, verified 2026-11-06; README example tables updated to match
- 主体对比表：个体工商户「责任承担」由「待核实」改为摘录《民法典》第五十六条（国家市场监督管理总局网站原文，2026-11-05 核验）；README 中英示例表同步
- Entity comparison: individual-business liability now cites Civil Code Art. 56 (SAMR official text, verified 2026-11-05); README example tables updated to match
- SKILL.md「可选衔接」：为第 2 步商业计划书、第 3 步政策导航补上步骤编号和仓库链接；正文中的政策导航引用同步加上链接
- SKILL.md optional hand-offs: added step numbers and GitHub links for business-plan-skill and opc-policy-navigator
- 许可补充：未经作者事先书面许可，不得将本项目上架、收录或分发到第三方 AI 产品、Skill 商店或类似渠道；授权联系仍为 @huaxialucaicaizi
- License: listing this project on third-party AI products, skill stores, or similar channels requires prior written permission from the author; contact remains @huaxialucaicaizi
- 许可证由 MIT 改为非商业许可；转载或商用须联系 @huaxialucaicaizi
- License changed from MIT to non-commercial; republication or commercial use requires contacting @huaxialucaicaizi
- README「一人公司工具包」表格：仓库链接改为加粗的「英文名 · 中文名」（与合集 ai-startup-skills 一致），英文版用加粗英文名
- README toolkit tables: repo links now use bold "English name · Chinese name" (matching the ai-startup-skills bundle); the English section uses bold English names
- README 开头的第 7 步提示和「园区工位注册」FAQ 中提到的姐妹仓库改为可点击、加粗的「英文名 · 中文名」链接；英文 FAQ 补上与中文版一致的政策导航指引
- README step-7 note and park-desk FAQ now link sister repos with bold names; the English FAQ now points to OPC Policy Navigator like the Chinese one

## [1.0.0] - 2026-10-22

### Added
- 首个独立版本：中国大陆一人公司注册与合规 skill
- 个体工商户 / 个人独资企业 / 一人有限公司对比，每条附公司法、个人独资企业法、促进个体工商户发展条例等官方原文条款
- 注册步骤与材料清单（市场主体登记管理条例）
- 注册后合规日历：年报（企业信息公示暂行条例）、变更登记、歇业、财产独立、出资期限
- 注明"非法律意见"；不提供未核实的税率、费用、办理天数
- First standalone release of OPC company registration (China)

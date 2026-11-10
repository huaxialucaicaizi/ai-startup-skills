# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Changed
- 漏斗判断补充：没有历史数据或关键层级尚未记录时，最弱层写「待基线」，避免在数据不足时凭空判断
- Funnel guidance: write "awaiting baseline" instead of guessing the weakest layer when historical or key-stage data is missing
- templates/weekly-review.md 漏斗表补上「复购 / 转介绍」行，与 SKILL 工作流、references/growth-funnel.md 对齐（没有数据仍写「未记录」）
- templates/weekly-review.md funnel table: added the "repeat / referral" row to match the SKILL workflow and growth-funnel.md (still write "not recorded" when there is no data)
- SKILL.md 开篇「只做五件事」漏了合规检查；改为与工作流一致的六件事（定位确认、漏斗与指标、实验池、内容日历与脚本、合规检查、周复盘）
- SKILL.md intro listed five tasks and omitted the compliance check; now six tasks, matching the workflow (positioning, funnel, experiments, calendar & scripts, compliance, weekly review)
- SKILL.md「可选衔接」：为已提到的想法验证、商业计划书补上第 1 步 ai-mvp-validation、第 2 步 business-plan-skill 仓库链接
- SKILL.md "Optional hand-offs": the already-mentioned validation and BP notes now link to step 1 ai-mvp-validation and step 2 business-plan-skill
- 许可证补充：未经作者事先书面许可，不得将本项目上架到第三方 AI 产品、Skill 商店或类似分发渠道；授权联系 @huaxialucaicaizi
- License: added a clause forbidding listing this project on third-party AI products, skill stores, or similar channels without prior written permission from the author (@huaxialucaicaizi)
- 许可证由 MIT 改为非商业许可；转载或商用需联系 @huaxialucaicaizi
- License changed from MIT to a non-commercial license; republication or commercial use requires contacting @huaxialucaicaizi
- SKILL.md「可选衔接」：定价与成交步骤已上线，去掉"即将推出"，改为链接第 6 步 opc-pricing-sales
- SKILL.md: the pricing & closing step is live; replaced "coming soon" with a link to step 6, opc-pricing-sales
- README「一人公司工具包」表格：仓库链接统一为加粗的“英文名 · 中文名”（英文版只加粗英文名），与 ai-mvp-validation 写法一致
- README toolkit tables: repository links now use bold names ("English name · 中文名" in the Chinese section, English name only in the English section), matching ai-mvp-validation
- README 常见问题「支持海外平台吗？」：给提到的 ai-mvp-validation 加上链接（加粗“英文名 · 中文名”，注明第 1 步）
- README FAQ "Overseas platforms?": the ai-mvp-validation mention now links to the repo (step 1)

## [1.0.0] - 2026-10-22

### Added
- 首个独立版本：一人公司小红书 / 抖音 / 视频号冷启动增长 skill
- 定位确认、增长漏斗与指标、实验池（ICE）、内容日历、口播脚本结构
- 合规检查：广告标识（互联网广告管理办法）、AI 生成内容标识，附官方原文链接
- 增长计划与周复盘模板（templates/）
- 不提供行业基准，所有阈值标"建议值，可自行调整"
- First standalone release of the OPC growth playbook

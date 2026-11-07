# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Changed
- 许可证补充：未经作者事先书面许可，不得将本项目上架到第三方 AI 产品、Skill 商店或类似分发渠道；授权联系 @huaxialucaicaizi
- License: added a clause forbidding listing this project on third-party AI products, skill stores, or similar channels without prior written permission from the author (@huaxialucaicaizi)
- 许可证由 MIT 改为非商业许可；转载或商用须通过 GitHub 联系作者 @huaxialucaicaizi
- License changed from MIT to non-commercial; republication or commercial use requires contacting @huaxialucaicaizi
- README「一人公司工具包」表格：仓库链接改为加粗"英文名 · 中文名"（英文版只用英文名），与姐妹仓库写法一致
- README "One-Person Company Toolkit" table: repo links now use bold names, matching sister repos
- README「一句话介绍」中的"下一步"链接改为加粗"英文名 · 中文名"（英文版只用英文名），与工具包表格一致
- README intro "next step" link to step 7 now uses the bold repo name, matching the toolkit table

### Fixed
- 输出模板「价格合规检查」原先只有 4 项，漏了服务标价、折扣基准、网页一致；现与 `references/price-compliance.md` 的 7 项及官方依据对齐
- Output template compliance checklist had 4 items and omitted service price marking, discount base, and page consistency; now matches the 7 checks in `references/price-compliance.md`
- SKILL.md「可选衔接」：第 5 步增长获客已上线，去掉"即将推出"，并为第 1、2、5 步补上仓库链接
- SKILL.md "Optional hand-offs": step 5 (growth) is live; replaced "coming soon" and linked steps 1, 2 and 5
- SKILL.md「可选衔接」补上第 7 步注册与合规链接（README 已写「下一步」，skill 正文此前未衔接）
- SKILL.md "Optional hand-offs": link step 7 (registration & compliance), which README already names as the next step

## [1.0.0] - 2026-10-22

### Added
- 首个独立版本：AI 产品 / 服务定价与成交 skill
- 成本法（含模型 / API 费）、竞品法、价值法，输出底价 / 建议价 / 上限参考
- 套餐设计、报价单、私域成交流程、异议处理
- 价格合规检查：《明码标价和禁止价格欺诈规定》，附官方原文链接
- 输出模板（templates/）；不提供行业基准
- First standalone release of AI pricing & closing

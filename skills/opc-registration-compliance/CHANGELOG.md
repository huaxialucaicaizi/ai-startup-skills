# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- `scripts/validate.py` 新增检查：`references/` 和 `templates/` 中的链接必须指向政府官方域名（`*.gov.cn`），否则校验失败
- `scripts/validate.py` now fails if any link in `references/` or `templates/` is not an official government domain (`*.gov.cn`)

### Changed
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

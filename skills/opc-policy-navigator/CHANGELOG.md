# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Fixed
- 上海政策库 SH-XH-02：补上官方页面标注的文号「徐市监营商〔2026〕91号」（原写“页面未标注文号”），2026-10-26 在徐汇区政府官网原文页核对
- Shanghai DB SH-XH-02: added the document number shown on the official Xuhui District page (previously listed as "not shown")
- CI 链接检查：排除 star-history 统计图接口（第三方服务间歇性返回 403，曾导致 main 分支 CI 失败）；政府官方链接仍照常检查
- CI link check: excluded the star-history chart API (third-party, intermittently returns 403 and failed CI on main); official government links are still checked

### Changed
- README「一人公司工具包」表格：仓库链接改为加粗的中英文名（如 **AI Pitch Coach · 路演教练**），与 ai-startup-skills 合集一致；英文表格只用英文名
- README toolkit tables: repo links now use bold project names, matching the ai-startup-skills bundle (English table uses English names only)

## [1.0.0] - 2026-10-22

### Added
- 首个独立版本：中国一人公司（OPC）政策导航 skill
- 国家级 + 北京、上海、广州、深圳（及杭州）政策库，每条附官方链接
- 三档匹配：大概率可申 / 需确认条件 / 暂不适用
- 材料清单、申报文案框架、输出模板（templates/）
- 2026-10-22 逐条复核全部官方链接
- 与其他步骤的衔接改为可选，不依赖其他 skill
- First standalone release of the China OPC policy navigator

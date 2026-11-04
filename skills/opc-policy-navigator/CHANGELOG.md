# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- 2026-11-01 月度复核：国家级 CN-06（《关于健全创业支持体系提升创业质量的意见》）、上海临港 SH-LG-01、北京朝阳 BJ-CY-01 由「已核查但未收录」升为正式条目；补上 BJ-01「OPC 专项服务券」申报入口
- 2026-11-01 monthly review: promoted national CN-06, Lingang SH-LG-01 and Chaoyang BJ-CY-01 from "checked but not included" to formal entries; added BJ-01 "OPC special service voucher" application path

### Changed
- 许可证补充：未经作者事先书面许可，不得将本项目上架、收录或分发到第三方 AI 产品、Skill 商店或类似渠道；许可联系 GitHub @huaxialucaicaizi
- License: added a clause forbidding listing this project on third-party AI products / skill stores without prior written permission; contact GitHub @huaxialucaicaizi
- 许可证由 MIT 改为非商业许可；转载或商用须通过 GitHub 联系 @huaxialucaicaizi
- License changed from MIT to non-commercial; republication or commercial use requires contacting @huaxialucaicaizi
- 广州南沙区 OPC 服务专区：补充区政府网站说明页和市场监管局清单链接，仍因无资金条款和文号暂不收录
- Guangzhou Nansha OPC service zone: added district government page and market-regulation list links; still not catalogued (no funding terms or document number)
- 政策库信息核实日期更新为 2026-11-01
- Policy database verification date updated to 2026-11-01

### Fixed
- CI 链接检查：排除海淀区政务网站 zyk.bjhd.gov.cn（GitHub runner 上偶发网络错误，本地 curl 仍为 200）；政策条目本身未改
- CI link check: excluded Haidian government host zyk.bjhd.gov.cn (intermittent network errors on GitHub runners; local curl still returns 200)
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

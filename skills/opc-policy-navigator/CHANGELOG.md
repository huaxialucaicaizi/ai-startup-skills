# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- 2026-11-01 月度复核：国家级 CN-06（《关于健全创业支持体系提升创业质量的意见》）、上海临港 SH-LG-01、北京朝阳 BJ-CY-01 由「已核查但未收录」升为正式条目；补上 BJ-01「OPC 专项服务券」申报入口
- 2026-11-01 monthly review: promoted national CN-06, Lingang SH-LG-01 and Chaoyang BJ-CY-01 from "checked but not included" to formal entries; added BJ-01 "OPC special service voucher" application path

### Changed
- SKILL.md / README / 输出模板：澄清「只用于文案政策契合」的判定——除方向性文件外，不含资金条款、以登记监管便利为主、以及适用对象不是 OPC 企业本人（如社区运营方）的条目也不进三档；模板该栏改为表格；顺带统一深圳 / 广东行的 `references/` 路径前缀，并补齐英文工作流的材料三种状态
- SKILL.md / README / output template: clarify "policy-fit text only" — besides directional docs, no-funding / registration-convenience items and policies not aimed at the OPC company itself (e.g. community operators) stay out of the three tiers; that template section is now a table; also unify `references/` path prefixes for Shenzhen / Guangdong rows and complete the English workflow materials states
- 输出模板与 SKILL.md 工作流对齐：需确认条件 / 暂不适用改为表格并补上文号和官方链接；材料清单补上「用户自述、待提供证明」
- Output template aligned with SKILL.md: needs-confirmation and not-applicable sections are tables with document numbers and official links; materials checklist adds the self-reported state
- SKILL.md 工作流与 README 工作流 / 原则：补上「方向性文件只列入文案『政策契合』、不作为可申资金」，与输出模板和示例表一致
- SKILL.md workflow and README workflow / principles: directional documents go under "policy-fit text only", not as fundable items, matching the output template and example table
- 许可证补充：未经作者事先书面许可，不得将本项目上架、收录或分发到第三方 AI 产品、Skill 商店或类似渠道；许可联系 GitHub @huaxialucaicaizi
- License: added a clause forbidding listing this project on third-party AI products / skill stores without prior written permission; contact GitHub @huaxialucaicaizi
- 许可证由 MIT 改为非商业许可；转载或商用须通过 GitHub 联系 @huaxialucaicaizi
- License changed from MIT to non-commercial; republication or commercial use requires contacting @huaxialucaicaizi
- 广州南沙区 OPC 服务专区：补充区政府网站说明页和市场监管局清单链接，仍因无资金条款和文号暂不收录
- Guangzhou Nansha OPC service zone: added district government page and market-regulation list links; still not catalogued (no funding terms or document number)
- 政策库信息核实日期更新为 2026-11-01
- Policy database verification date updated to 2026-11-01

### Fixed
- CI 链接检查：排除朝阳区政府网站 bjchy.gov.cn（GitHub Actions 上 Network error，本地 curl 仍为 200）；BJ-CY-01 条目保留原链接，正式印发通知仍以 ncsti.gov.cn 为准
- CI link check: excluded Chaoyang government host bjchy.gov.cn (Network error on GitHub Actions; local curl still returns 200); BJ-CY-01 keeps the original link, with the formal notice still pointing to ncsti.gov.cn
- CI 链接检查：限制并发请求数，避免同一批上海市政府官方链接因并发访问超时；链接仍保留在检查范围内
- CI link check: limited concurrent requests to avoid timeouts when checking Shanghai government links in the same batch; the links remain covered
- CI 链接检查：排除海淀区政务网站 zyk.bjhd.gov.cn（GitHub runner 上偶发网络错误，本地 curl 仍为 200）；政策条目本身未改
- CI link check: excluded Haidian government host zyk.bjhd.gov.cn (intermittent network errors on GitHub runners; local curl still returns 200)
- 上海政策库 SH-XH-02：补上官方页面标注的文号「徐市监营商〔2026〕91号」（原写“页面未标注文号”），2026-10-26 在徐汇区政府官网原文页核对
- Shanghai DB SH-XH-02: added the document number shown on the official Xuhui District page (previously listed as "not shown")
- CI 链接检查：排除 star-history 统计图接口（第三方服务间歇性返回 403，曾导致 main 分支 CI 失败）；政府官方链接仍照常检查
- CI link check: excluded the star-history chart API (third-party, intermittently returns 403 and failed CI on main); official government links are still checked

### Changed
- SKILL.md「可选衔接」与 README 开篇：补上第 7 步注册与合规（可与本步并行），并为路演教练补上仓库链接；README 开篇的工具包链接改为加粗项目名，与表格一致
- SKILL.md optional handoff and README intro: added step 7 registration (can run in parallel) and a link to the pitch coach; README intro toolkit links now use bold names, matching the tables
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

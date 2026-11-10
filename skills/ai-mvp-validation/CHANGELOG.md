# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Changed
- CI 链接检查忽略偶发返回 503 的 Star History 动态图片接口，避免外部服务波动导致误报
- CI link checking now ignores the Star History image API, whose intermittent 503 responses caused false failures
- `references/pain-and-feasibility.md`：为「AI 产品特有判断」补上自查清单（三项风险等级、未评估按高风险且无应对、合规只引用已核实链接）
- `references/pain-and-feasibility.md`: add a self-check for the AI-product assessment section (risk levels, unevaluated overlap treated as high risk, official-link-only compliance)
- `references/pain-and-feasibility.md`：标识办法链接从网信办「发布说明」改为含办法全文的官方通知原文
- `references/pain-and-feasibility.md`: the 标识办法 link now points to the CAC notice with the full official text, not the press release
- 许可证补充：未经作者事先书面许可，不得将本项目上架、收录或分发到第三方 AI 产品、Skill 商店或类似渠道
- License: added a clause forbidding listing this project on third-party AI products / skill stores without prior written permission
- 许可证由 MIT 改为非商业许可；转载或商用须联系 @huaxialucaicaizi
- License changed from MIT to non-commercial; republication or commercial use requires contacting @huaxialucaicaizi
- SKILL.md「可选衔接」：标明本仓库是工具包第 1 步；第 2 步链接改为加粗中英文名 **Business Plan Skill · 商业计划书**；补上第 3 步政策导航、第 4 步路演教练和合集 **AI Startup Skills · AI 创业 Skill 包**（均为可选配套，非依赖）
- SKILL.md optional handoff: mark this repo as toolkit step 1; step 2 now uses the bold bilingual name **Business Plan Skill**; add optional links to step 3 (policy), step 4 (pitch coach), and the **AI Startup Skills** bundle
- README「一人公司工具包」表格：仓库链接改为加粗的中英文名（如 **AI Pitch Coach · 路演教练**），与 ai-startup-skills 合集一致；英文版只用英文名
- README toolkit tables: repo links now show bold display names, matching the ai-startup-skills bundle
- README「不适合」：把"之后的增长步骤"改为链接到第 5 步 **OPC Growth Playbook · 一人公司增长获客**
- README "Not a fit": the "later growth step" now links to step 5, OPC Growth Playbook
- README 开头「下一步」提示：`business-plan-skill` 改为加粗的第 2 步 **Business Plan Skill · 商业计划书**，与工具包表格写法一致
- README intro "next step" note: now shows step 2 as **Business Plan Skill** instead of the raw repo slug

## [1.0.0] - 2026-10-22

### Added
- 首个独立版本：AI 产品（AI 工具、AI 应用、Agent）MVP 验证 skill
- 桌面调研（竞品、搜索热度、社区讨论）+ 用户访谈指南
- AI 产品特有判断：是否被大模型原生功能覆盖、模型 / 推理成本、数据与合规（引用网信办官方链接）
- 核心方法 Meta 广告投放验证：落地页 / 等待名单、A/B 测试、CTR / CPC / 落地页转化率 / 单线索成本 / 付费意向 / 实际预付；国内可换小红书聚光、巨量引擎
- 组合公式（给谁 / 解决什么 / 卖点 / 付多少钱）与固定结论句式"已验证的是 X，下一步要验证 Y"
- 辅助方法：小红书笔记、预售、人工模拟交付；验证记录表
- 所有阈值标"建议值，可自行调整"，不提供行业基准数据
- 与写 BP 的衔接改为可选，不依赖其他 skill
- First standalone release: AI product MVP validation with desk research, interviews and Meta ad tests

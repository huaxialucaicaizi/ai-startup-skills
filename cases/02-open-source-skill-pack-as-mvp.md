# 把「一人公司工具包」开源，当作 MVP 和分发渠道

> **真实案例（作者经历）** · 作者：华夏路菜菜子
> 本文的事实来自本仓库和作者 GitHub 的公开信息（仓库、提交记录、创建时间）。使用量、Star 数、收入等未写入：Star 数以 README 顶部实时徽章为准，其余未公开。

## 对应步骤

- 主要：第 1 步 MVP 验证 → [`skills/ai-mvp-validation/SKILL.md`](../skills/ai-mvp-validation/SKILL.md)
- 关联：第 5 步 增长获客 → [`skills/opc-growth-playbook/SKILL.md`](../skills/opc-growth-playbook/SKILL.md)（开源仓库本身是分发渠道）
- 关联：第 6 步 定价与成交 → [`skills/opc-pricing-sales/SKILL.md`](../skills/opc-pricing-sales/SKILL.md)（免费开源和后续商业化的关系）

## 背景

- 目标用户：在中国做 AI 产品的一人公司（OPC）和早期创业者。
- 他们的问题：验证、写 BP、申请政策、路演、获客、定价、注册，每件事都要自己摸索。
- 作者自己就在走这条路，所以把每一步的方法写成 Agent Skill（可以装进 Codex、Claude Code、Cursor 等工具，让 AI 按步骤带着做）。

## 做了什么

以下事实都可以在 GitHub 上查到：

1. **先发一个，再扩成一套**：[business-plan-skill](https://github.com/huaxialucaicaizi/business-plan-skill) 是最早的一个（GitHub 显示创建于 2026-06-04）。另外 6 个 skill 和本合集仓库都创建于 2026-10-22。
2. **每一步一个独立仓库**：7 个仓库都用 MIT 许可，可以单独安装，也可以通过本合集一次装全。
3. **合集只加一层"路由"**：本仓库的 `SKILL.md` 不做具体工作，只判断用户在哪一步，再交给对应子 skill。子 skill 由 `scripts/sync.sh` 从独立仓库同步，不在合集里另改一份。
4. **把原则写进规则**：「不编数据」「只用官方来源」「信息参考，不是法律或税务意见」写进 README 和每个 SKILL.md 的硬性规则；示例统一标注「虚构」（见 `skills/business-plan-skill/examples/`）。
5. **用 CI 守住质量**：`scripts/validate.py` 校验 frontmatter 和路由，lychee 检查文档里的链接（见 `.github/workflows/ci.yml`）。
6. **安装路径写到能直接复制**：README 给出 Codex 和 Claude Code 的命令，其他工具按各自方式安装。

还不知道的：有多少人实际安装和使用、使用后的反馈、是否带来咨询或付费。这些作者没有公开，本文不写。

## 可复用动作清单

把"开源一个工具"当作 MVP 验证，可以对照 `skills/ai-mvp-validation` 这样做：

1. **最小可用单元先发**：先发一个能独立解决一个问题的 skill（或模板、脚本），而不是一次做完整套。等第一个有了反馈，再决定扩不扩。
2. **把验证信号定义清楚，再看数据**：开源项目能看到的信号包括 Star、Fork、Issue、PR、安装后的提问。先在 `references/validation-log.md` 里写下"什么信号算继续 / 调整 / 停止"，再去看数据；判断标准是你自己定的建议值，不是行业基准。
3. **Star 不等于需求**：Star 只说明有人感兴趣。更强的信号是有人提 Issue 描述自己的真实场景，或者主动来问能不能付费帮做。记录时按 `已验证（有记录）` / `用户自述、未验证` 标注。
4. **开源仓库也是内容**：每个仓库的 README 都是一篇可以被搜到、被转发的内容。发布时配合第 5 步的内容日历（`skills/opc-growth-playbook/references/content-calendar.md`），而不是只发仓库。
5. **免费和付费分开想**：MIT 开源意味着任何人都可以免费用、改、商用。如果之后要商业化，可以收费的是"人"的部分（陪跑、咨询、定制），而不是代码本身。具体怎么定价，走第 6 步；本案例的商业化结果未公开。
6. **合集和独立仓库保持单一来源**：如果你也做多个工具的合集，内容只在一个地方改，用脚本同步，避免两边版本不一致。

## 风险 / 注意

- **"开源 = 获客"不是必然的**：发布本身不会带来用户，需要配合内容分发；没有分发，开源仓库和没发布差别不大。
- **不要用 Star 数做宣传数据**：在 BP 或路演里引用时，写查询日期和来源，并说明它只代表关注度。
- **MIT 许可的含义**：别人可以合法地复制和商用你的内容。如果有不想公开的部分（例如付费交付物），不要放进开源仓库。
- **规则会过期**：工具包里的政策、法规、平台规则需要定期核对官方原文。开源后别人会按你写的去做，过期信息的影响比私下用更大。

## English summary

**Real case (author's own experience).** The author open-sourced the One-Person Company Toolkit as both an MVP and a distribution channel: first one skill (`business-plan-skill`, repo created 2026-06-04), then six more standalone MIT repos plus this bundle (all created 2026-10-22), with a thin router, `sync.sh` as the single source of truth, a no-invented-data rule, and CI validation. It maps to step 1 (validation), step 5 (growth) and step 6 (pricing). Reusable lessons: ship the smallest useful unit first, define validation signals before reading them, treat Stars as interest not demand, pair releases with content, and monetize the human part (coaching/consulting) rather than MIT code. Install counts, feedback and revenue are not public and are not stated.

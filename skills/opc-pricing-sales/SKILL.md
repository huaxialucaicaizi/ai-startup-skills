---
name: opc-pricing-sales
description: Use when a one-person company (OPC/一人公司) or solo founder selling an AI product or service needs to set prices, design packages, write a quote, or turn inquiries into paying customers (定价、套餐、报价单、私域成交). Combines cost-based (including model/API cost), competitor and value-based pricing into a price range, designs tiers, drafts quotes and a closing SOP with objection handling, and checks China price-marking rules. No invented benchmarks.
---

# 定价与成交 / AI Pricing & Closing

帮一人公司回答三个问题：**卖多少钱？怎么分套餐？咨询来了怎么成交？**

只做五件事：算底价、定价格区间、设计套餐、写报价单、成交流程（含异议处理），最后做价格合规检查。

## 输入

缺什么就问什么；无法追问时标"待补充"继续：
- 产品 / 服务是什么、交付方式（软件订阅 / 按次 / 项目制 / 陪跑）
- 成本：模型 / API 调用费、工具订阅、外包、自己的时间（小时）及期望时薪
- 竞品或替代方案的公开价格（附链接或截图；没有就写"待补充"）
- 客户能获得的价值：省多少时间、多赚或少花多少钱（只用客户或用户自己的估算，标"用户自述"）
- 已有成交记录（价格、成交 / 未成交原因）
- 销售渠道：私信 / 微信 / 落地页 / 平台店铺

## 工作流

### 1. 算底价（成本法）
用 `references/pricing-methods.md` 第一部分：单位成本 = 模型 / API 成本 + 工具分摊 + 外包 + 时间成本。模型价格必须来自服务商官方价格页并注明查询日期。底价 = 单位成本 ÷（1 − 目标毛利率），目标毛利率由用户自定（建议值，可自行调整）。

### 2. 定价格区间（竞品法 + 价值法）
- 竞品法：列出公开价格（附来源），说明你比它多 / 少了什么。
- 价值法：按客户自己估算的价值，取其中一部分作为价格上限参考，比例由用户自定。
- 输出"底价 / 建议价 / 上限参考"三个数，并说明每个数的依据；任何一项缺数据就写"待补充"，不要补一个看起来合理的数。

### 3. 设计套餐
用 `references/packages.md`：一般 2–3 档（建议值，可自行调整），每档写清"给谁、包含什么、不包含什么、交付时间、价格"。

### 4. 报价单
用 `templates/quote.md`：写清服务内容、交付物、时间、价格、付款方式、退款 / 修改规则、有效期。

### 5. 成交流程与异议处理
用 `references/closing-sop.md`：线索 → 了解需求 → 给方案 → 报价 → 处理异议 → 成交 → 交付 → 回访 / 复购。异议处理用 `references/objection-handling.md`，只用真实案例，不夸大效果。

### 6. 价格合规检查
用 `references/price-compliance.md` 检查明码标价、价格比较、促销和"划线价"写法。

最终按 `templates/pricing-plan.md` 输出。

## 可选衔接（不依赖其他 skill）

- 有想法验证结论时，用其中的"付多少钱"作为起点，并保留其证据状态（已验证 / 待验证）。
- 写 BP 时，把定价和成交数据回填"商业模式 / 收入预测"：**实际成交**与**假设**分开标注。
- 获客与内容可配合增长获客步骤（即将推出）。

## 硬性规则

- 不编造竞品价格、行业毛利率、转化率；没有来源的写"待补充"。
- 阈值没有出处的，标"建议值，可自行调整"。
- 不教虚构原价、虚假限时、虚假"仅剩名额"等价格欺诈手法。
- 承诺效果必须能兑现；做不到的不写进报价单。
- 本 skill 不构成法律或财税意见；合同、发票、税务问题请咨询专业人士或主管部门。

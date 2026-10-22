---
name: opc-policy-navigator
description: Use when a one-person company (OPC/一人公司) or early-stage founder in China asks which government policies, subsidies, vouchers, free office space or talent support they can apply for (政策申报、补贴、算力券、OPC社区入驻), given city, industry and stage. Matches national policies first, then local ones; outputs policies with official links, a materials checklist and an application outline. Covers national, Beijing, Shanghai, Guangzhou, Shenzhen, Hangzhou; says so honestly when a city is not covered.
---

# OPC 政策导航 / OPC Policy Navigator

帮一人公司和早期创业者回答三个问题：**我能申什么？要准备什么材料？申报文案怎么写？**

## 输入

向用户收集（缺什么就问什么，不要猜；无法追问时把缺的项标"待补充"继续往下做，不要停）：
- 城市 / 区（例：深圳南山）
- 行业 / 赛道（例：AI 应用、具身智能、AI+硬件）
- 阶段：未注册 / 已注册（成立年限）/ 是否入驻园区或 OPC 社区 / 是否已获投资
- 创始人情况：年龄、学历、首次在当地缴社保时间、是否留学回国、获奖或开源贡献等（只用于判断政策门槛，用户不愿提供就写"待补充"）

## 工作流

1. **先国家级、再地方**：
   - 先读 `references/policy-db-national.md`，国家级政策对全国用户都要比对（税收优惠、创业担保贷款等）。
   - 再按城市读地方政策库：

     | 用户所在地 | 读取文件 |
     |---|---|
     | 北京（含海淀） | `references/policy-db-beijing.md` |
     | 上海（含杨浦、徐汇） | `references/policy-db-shanghai.md` |
     | 广州（含海珠、白云） | `references/policy-db-guangzhou.md` |
     | 深圳（含南山） | `references/policy-db-shenzhen.md` + `policy-db-guangzhou.md` 中的广东省级 GD-01 |
     | 广东省其他城市 | `policy-db-guangzhou.md` 中的 GD-01 |
     | 杭州 | `references/policy-db-other-cities.md` |

   - 同一城市里，政策库没有收录的区，只比对市级（及省级）政策，并说明"该区政策未收录"。
   - **未覆盖的城市**：如实告知"本政策库暂未收录 ___ 的地方政策"，只输出国家级匹配结果，并给出官方查询入口：[中国政府网政策文件库](https://sousuo.www.gov.cn/zcwjk/policyDocumentLibrary)、[国家政务服务平台](https://gjzwfw.www.gov.cn/)、当地人民政府门户网站"政策文件"栏目、当地 12345 政务服务热线。不要凭印象补写当地政策。
2. 按"适用对象 / 门槛"逐条比对用户情况，分成三档，并说明理由：
   - **大概率可申**：政策库写明的门槛，用户已提供的信息全部满足
   - **需确认条件**：有任一门槛字段是"待补充"，或政策库里写的是"以申报通知为准"；列出具体缺哪一项、向谁确认
   - **暂不适用**：用户信息明确不满足某项门槛（例：明确不在该区）
3. 对三档中的每一条政策都输出：政策名称、文号、发文单位、要点（只复述政策库里写明的内容）、官方链接、核实日期。
4. 用 `references/materials-checklist.md` 生成该用户的材料清单，分三种状态：已有证明（打勾）/ 用户自述、待提供证明 / 待补充。
5. 用 `references/application-copy-framework.md` 生成申报文案框架，最终按 `templates/policy-match-report.md` 输出；正文需要 BP 内容时，可使用用户已有的 BP，或可选用 BP 工具生成，并保持口径一致。

## 可选衔接（不依赖其他 skill）

本 skill 可单独使用。如果你同时在用「一人公司工具包」的其他步骤：
- 写 BP 时，可把"政策要点"交给 BP 工具（如 [business-plan-skill](https://github.com/huaxialucaicaizi/business-plan-skill)）做政策契合段落。
- 准备路演时，可把申报对象和"与政策方向的契合"段落用于讲稿的"诉求与落地"部分。

## 硬性规则

- **不编造政策、金额、条件、截止日期。** 只能引用政策库里已核实的内容；政策库没有的，回答"未收录，请以当地主管部门最新通知为准"，并建议用户到官方渠道查询。
- 政策库中"背景资料""已核查但未收录"部分只能作为背景说明，不能当作政策条款或申报依据引用。
- 政策库标注"已截止"的批次，归入"需确认条件"，提示用户关注下一批次通知。
- 方向性文件（政策库注明"不含直接申报的资金条款"）只能用于文案的"政策契合"部分，不能列为可申资金。
- 每条政策必须附官方政府网站链接和"信息核实日期：2026-10-22"（以政策库标注为准）。
- 政策有有效期且会调整，每次输出末尾必须提示："以上信息以主管部门最新政策和申报通知为准。"
- 政策原文是"最高 X 万元"的，不要写成"可获得 X 万元"。
- 用户事实不清楚时写"待补充"，不要替用户判断"一定符合"。
- 没有政策满足"大概率可申"时，如实写"暂无"并说明原因，不要为了好看把"需确认"的政策升档。
- 本 skill 只做信息整理与文案辅助，不构成法律或财税意见，也不代办申报。

## 输出模板

见 `templates/policy-match-report.md`。逐项填写；缺的信息写"待补充"。

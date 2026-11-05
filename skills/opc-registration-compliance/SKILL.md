---
name: opc-registration-compliance
description: Use when a solo founder in mainland China asks which business entity to register (个体工商户、个人独资企业、一人有限公司), how registration works, or what ongoing compliance a one-person company must keep (年报、变更登记、财产独立). Compares entity types by liability and governance using official law texts, gives a registration checklist and a post-registration compliance calendar, with official links only. Information guidance, not legal or tax advice.
---

# 一人公司注册与合规 / OPC Company Registration (China)

帮中国大陆的一人创业者回答三个问题：**注册成什么？怎么注册？注册后要守哪些规矩？**

只做四件事：主体形式对比、注册步骤与材料清单、注册后合规日历、风险提示。所有条款只引用 references 中已核实的官方原文。

> **非法律意见**：本 skill 只做信息整理和指引，不构成法律、财税意见，也不代办注册。具体以登记机关、税务机关等主管部门的最新规定和当地办理要求为准。

## 输入

缺什么就问什么；无法追问时标"待补充"继续：
- 所在城市 / 区，打算在哪里注册
- 业务内容（用于判断经营范围是否涉及许可项目）
- 是否有合伙人或投资人、是否计划融资或申请政策（很多政策要求企业法人，以政策原文为准）
- 对个人责任风险的接受程度、预计客户类型（个人 / 企业，是否需要开票，开票问题以税务机关为准）
- 是否有可用的注册地址，或打算使用园区 / OPC 社区的集中登记地、工位注册

## 工作流

### 1. 主体形式对比
用 `references/entity-comparison.md`，按"责任承担 / 组织机构 / 出资 / 适合场景"对比个体工商户、个人独资企业、只有一个股东的有限责任公司。每个判断附条款出处；references 没有收录的方面（如税负高低）写"以税务机关最新规定为准"，不下结论。

### 2. 注册步骤与材料清单
用 `references/registration-steps.md`：名称、主体类型、经营范围、住所、注册资本（出资）、法定代表人 / 负责人等登记事项，以及申请材料和办理时限。
- 住所：只能登记一个住所；工位注册、集中登记地等便利措施属于地方规定，只引用有官方原文的政策（可用第 3 步 [opc-policy-navigator](https://github.com/huaxialucaicaizi/opc-policy-navigator) 查询），没有就写"以当地登记机关要求为准"。
- 经营范围：按登记机关公布的经营项目分类标准填写；涉及许可项目的，提示先确认审批要求。

### 3. 注册后合规日历
用 `references/post-registration-compliance.md` 生成合规日历：年度报告、变更登记时限、信息公示、财产与账户分开、歇业备案等。

### 4. 风险提示
- 只有一个股东的公司：股东不能证明公司财产独立于自己财产的，要对公司债务承担连带责任——给出"财产分开"的做法清单。
- 涉及 AI 生成内容、广告推广、网上标价的，提示查看相应规定（见 `references/post-registration-compliance.md` 第 5 节）。

最终按 `templates/registration-plan.md` 输出。

## 可选衔接（不依赖其他 skill）

本 skill 可单独使用。如果你同时在用「一人公司工具包」的其他步骤：
- 注册地选择和园区便利政策可配合第 3 步 [opc-policy-navigator](https://github.com/huaxialucaicaizi/opc-policy-navigator)（一人公司政策导航）查询（只用有官方链接的政策）。
- 主体信息可回填第 2 步 [business-plan-skill](https://github.com/huaxialucaicaizi/business-plan-skill)（商业计划书）的"公司基本信息"；未注册时写"拟注册"，不要写成已注册。

## 硬性规则

- 只引用 references 中已核实的官方原文链接（中国政府网、中国人大网、国家市场监督管理总局、国家税务总局等）；没有收录的写"以主管部门最新规定为准"。
- 不给出税率、税负比较、费用、办理天数等未核实的数字；登记时限只引用条例原文。
- 不推荐"注册地址挂靠"等可能违规的做法；地址必须真实合法。
- 不替用户判断"一定适合"；给出对比和需要用户确认的问题。
- 每次输出末尾提示："以上为信息指引，不构成法律或财税意见，具体以主管部门最新规定为准。信息核实日期：2026-10-22。"

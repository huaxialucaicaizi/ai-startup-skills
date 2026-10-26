---
name: ai-startup-skills
description: Use when a founder or one-person company (一人公司/OPC) building an AI product in China needs end-to-end startup help and it is unclear which step they are on. Routes by stage through a 7-step journey - MVP validation, business plan, policy and subsidies, roadshow, growth, pricing and sales, registration and compliance - to the matching sub-skill in skills/.
---

# AI 创业 Skill 包 · Router

This is the entry skill for a 7-step toolkit. It does not do the work itself: it figures out which stage the user is at and hands off to the matching sub-skill under `skills/`.

## The 7 steps

| Step | Sub-skill | Use when the user... |
|---|---|---|
| 1 | `skills/ai-mvp-validation/SKILL.md` | has an AI product idea/MVP and does not yet know if anyone wants it |
| 2 | `skills/business-plan-skill/SKILL.md` | needs a business plan / BP, deck content or application materials |
| 3 | `skills/opc-policy-navigator/SKILL.md` | asks which policies, subsidies, vouchers or OPC community spaces they can apply for |
| 4 | `skills/ai-pitch-coach/SKILL.md` | prepares a live roadshow or defense for a park, incubator or competition |
| 5 | `skills/opc-growth-playbook/SKILL.md` | needs cold-start growth on Xiaohongshu, Douyin or WeChat Channels |
| 6 | `skills/opc-pricing-sales/SKILL.md` | needs prices, packages, quotes or a closing process |
| 7 | `skills/opc-registration-compliance/SKILL.md` | asks which entity to register or what ongoing compliance applies |

## Routing

1. If the request clearly matches one step, read that sub-skill's `SKILL.md` and follow it. Do not ask extra questions first.
2. If it is unclear, ask at most two short questions: what they are building, and what they have already done (validated? BP written? registered?). Then pick the earliest step not yet done.
3. Default order for a new founder is 1 → 2 → 3/7 → 4 → 5 → 6. Steps 3 and 7 can run in parallel; step 7 is often required before applying in step 3.
4. Pass outputs forward: validation evidence from step 1 feeds the BP in step 2; the BP feeds policy applications (3) and the roadshow (4); pricing (6) uses the funnel data from growth (5).
5. When a step finishes, say in one line which step is a sensible next one, and why.

## Real cases

`cases/` holds short real cases from the author's own experience (真实案例), each mapped to steps. When the user asks for a real example, or seems unsure how a step plays out in practice, point them to the matching case alongside the sub-skill. Do not add numbers or outcomes that the case does not state.

| Case | Steps |
|---|---|
| `cases/01-big-tech-ai-growth-to-content.md` | 5 growth (also 6) |
| `cases/02-open-source-skill-pack-as-mvp.md` | 1 validation, 5, 6 |
| `cases/03-campus-talk-career-narrative.md` | 4 pitch, 2 BP founder section |

## Rules

- Each sub-skill's own rules win inside that step (official links only, no invented benchmarks, compliance flags).
- Never invent numbers, policies, cases or testimonials. Mark any example as fictional.
- Policy, legal and tax content is information guidance, not professional advice; point to official sources.

# Changelog

## Unreleased

- Remove the author's personal real cases (`cases/`) and every reference to them, at the author's request (应作者要求删除个人真实案例及全部引用). This reverts the unreleased cases addition: README (中文 + English), router `SKILL.md` and `scripts/validate.py` no longer mention `cases/`.

## v1.0.0 - 2026-10-22

- First release of AI 创业 Skill 包 (AI Startup Skills)
- Router skill `SKILL.md` that routes by stage across the 7-step journey
- Bundles 7 sub-skills under `skills/`: ai-mvp-validation, business-plan-skill, opc-policy-navigator, ai-pitch-coach, opc-growth-playbook, opc-pricing-sales, opc-registration-compliance
- `scripts/validate.py` checks the router and every sub-skill's frontmatter
- `scripts/sync.sh` re-pulls the 7 standalone repos into `skills/`
- CI: validator + lychee link check

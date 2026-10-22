# Changelog

## v1.0.0 - 2026-10-22

- First release of AI 创业 Skill 包 (AI Startup Skills)
- Router skill `SKILL.md` that routes by stage across the 7-step journey
- Bundles 7 sub-skills under `skills/`: ai-mvp-validation, business-plan-skill, opc-policy-navigator, ai-pitch-coach, opc-growth-playbook, opc-pricing-sales, opc-registration-compliance
- `scripts/validate.py` checks the router and every sub-skill's frontmatter
- `scripts/sync.sh` re-pulls the 7 standalone repos into `skills/`
- CI: validator + lychee link check

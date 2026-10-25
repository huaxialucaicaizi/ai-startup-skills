# Changelog

## Unreleased

- Add `cases/`: 3 real cases from the author's own experience (真实案例), each mapped to toolkit steps — big-tech AI growth → solo content growth (step 5), open-sourcing this toolkit as MVP + distribution (steps 1/5/6), campus-talk career narrative (steps 4/2). No invented metrics; unknowns marked 未公开.
- Router `SKILL.md` points to the matching case when a user wants a real example
- `scripts/validate.py` also checks that `cases/*.md` files referenced by the router exist
- README links the cases (中文 + English)

## v1.0.0 - 2026-10-22

- First release of AI 创业 Skill 包 (AI Startup Skills)
- Router skill `SKILL.md` that routes by stage across the 7-step journey
- Bundles 7 sub-skills under `skills/`: ai-mvp-validation, business-plan-skill, opc-policy-navigator, ai-pitch-coach, opc-growth-playbook, opc-pricing-sales, opc-registration-compliance
- `scripts/validate.py` checks the router and every sub-skill's frontmatter
- `scripts/sync.sh` re-pulls the 7 standalone repos into `skills/`
- CI: validator + lychee link check

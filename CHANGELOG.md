# Changelog

## Unreleased

- Sync all 7 `skills/` copies with their standalone repos' `main` via `scripts/sync.sh` (2026-10-28): README next-step / FAQ links now use bold bilingual names (ai-mvp-validation #8, ai-pitch-coach #7, opc-growth-playbook #5, opc-pricing-sales #7); business-plan-skill #10 adds a "所属工具包" section listing all 7 steps plus this bundle and updates the file-structure tree; opc-registration-compliance #7 makes `scripts/validate.py` require `*.gov.cn` sources in references/templates; opc-policy-navigator #7 is CHANGELOG-only here (CI ignore file is not copied by sync).
- Sync all 7 `skills/` copies with their standalone repos' `main` via `scripts/sync.sh` (用 sync.sh 同步 7 个子 skill 副本): bold bilingual repo names in toolkit tables, business-plan-skill Validation Evidence section + fictional financial/validation example + Final Delivery Check, opc-policy-navigator SH-XH-02 document number, and stale "coming soon" hand-offs replaced with links.
- Remove the author's personal real cases (`cases/`) and every reference to them, at the author's request (应作者要求删除个人真实案例及全部引用). This reverts the unreleased cases addition: README (中文 + English), router `SKILL.md` and `scripts/validate.py` no longer mention `cases/`.

## v1.0.0 - 2026-10-22

- First release of AI 创业 Skill 包 (AI Startup Skills)
- Router skill `SKILL.md` that routes by stage across the 7-step journey
- Bundles 7 sub-skills under `skills/`: ai-mvp-validation, business-plan-skill, opc-policy-navigator, ai-pitch-coach, opc-growth-playbook, opc-pricing-sales, opc-registration-compliance
- `scripts/validate.py` checks the router and every sub-skill's frontmatter
- `scripts/sync.sh` re-pulls the 7 standalone repos into `skills/`
- CI: validator + lychee link check

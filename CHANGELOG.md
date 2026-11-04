# Changelog

## Unreleased

- Add Japanese README (`README.ja.md`) and a language switcher link in the root README (新增日文 README，并在根 README 语言切换中加入日本語链接)
- Sync all 7 `skills/` copies with their standalone repos' `main` via `scripts/sync.sh` (2026-11-04): README and CHANGELOG catch up the standalone license-docs follow-ups after this bundle's LICENSE-only copy in #11 (`business-plan-skill` CONTRIBUTING.md also moved). Source: `ai-mvp-validation` `239c395` (#11), `business-plan-skill` `50a07ca` → `564d63b` (#16), `opc-policy-navigator` `3000a33` (#11), `ai-pitch-coach` `4255a12` (#10), `opc-growth-playbook` `2c8a57c` (#8), `opc-pricing-sales` `bbbd69d` (#10), `opc-registration-compliance` `5accfb2` (#10). LICENSE files already matched; `.github/` and `.lycheeignore` are not copied by sync.
- License now also forbids listing this project (or derivative works) on third-party AI products, Skill stores, plugin marketplaces, or similar channels without prior written permission from @huaxialucaicaizi (许可证新增：未经作者事先书面许可，不得将本项目上架到第三方 AI 产品、Skill 商店等分发渠道)
- License changed from MIT to a non-commercial license; republication or commercial use requires contacting @huaxialucaicaizi (许可证由 MIT 改为非商业许可；转载或商用需联系 @huaxialucaicaizi)
- Sync `skills/` copies with their standalone repos' `main` via `scripts/sync.sh` (2026-11-03): only `business-plan-skill` moved (`c0159f3` → `50a07ca`, source PR #12) — added fictional `examples/team-and-competitive-advantage.md` plus `examples/README.md`, README, and CHANGELOG; the other 6 copies already matched current `main`.
- Sync `skills/` copies with their standalone repos' `main` via `scripts/sync.sh` (2026-11-02): only `opc-policy-navigator` moved (`32217e3` → `c28e608`, source PR #9) — policy DB adds CN-06 / SH-LG-01 / BJ-CY-01, BJ-01 申报入口, README/SKILL/CHANGELOG/template date updates to 2026-11-01, and BJ-01 全角括号链接拆分; source-repo CI ignore files are not copied by sync; the other 6 copies already matched current `main`.
- Sync `skills/` copies with their standalone repos' `main` via `scripts/sync.sh` (2026-10-31): only `business-plan-skill` moved (`e0ae907` → `c0159f3`, source PR #11) — expanded fictional `examples/incubator-application-summary.md` plus `examples/README.md`, README, and CHANGELOG; the other 6 copies already matched current `main`.
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

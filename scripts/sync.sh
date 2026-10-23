#!/usr/bin/env bash
# Re-pull the 7 standalone repos' main branch into skills/<name>/ (skips .git, .github, .lycheeignore).
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
OWNER="huaxialucaicaizi"
BRANCH="main"
REPOS=(ai-mvp-validation business-plan-skill opc-policy-navigator ai-pitch-coach opc-growth-playbook opc-pricing-sales opc-registration-compliance)
TMP="$(mktemp -d)"; trap 'rm -rf "$TMP"' EXIT
mkdir -p "$ROOT/skills"
for r in "${REPOS[@]}"; do
  echo "→ $r"
  git clone -q --depth 1 --single-branch --branch "$BRANCH" "https://github.com/$OWNER/$r.git" "$TMP/$r"
  rm -rf "$ROOT/skills/$r"; mkdir -p "$ROOT/skills/$r"
  tar -C "$TMP/$r" --exclude=.git --exclude=.github --exclude=.lycheeignore -cf - . | tar -C "$ROOT/skills/$r" -xf -
  echo "  $BRANCH@$(git -C "$TMP/$r" rev-parse --short HEAD)"
done
echo "Done. Run: python3 scripts/validate.py"

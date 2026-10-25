#!/usr/bin/env python3
"""Validate the router SKILL.md and every skills/<name>/SKILL.md frontmatter."""
import re, sys, pathlib, yaml
root = pathlib.Path(__file__).resolve().parent.parent
EXPECTED = ["ai-mvp-validation", "business-plan-skill", "opc-policy-navigator", "ai-pitch-coach",
            "opc-growth-playbook", "opc-pricing-sales", "opc-registration-compliance"]
err = []
def check(path, want):
    rel = path.relative_to(root)
    if not path.exists():
        err.append(f"{rel}: missing"); return ""
    text = path.read_text(encoding="utf-8")
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if not m:
        err.append(f"{rel}: missing YAML frontmatter"); return text
    fm = yaml.safe_load(m.group(1)) or {}
    name, desc = str(fm.get("name", "")), fm.get("description", "")
    if not re.fullmatch(r"[a-z0-9]+(-[a-z0-9]+)*", name):
        err.append(f"{rel}: invalid name {name!r}")
    elif name != want:
        err.append(f"{rel}: name {name!r} != folder {want!r}")
    if not desc:
        err.append(f"{rel}: missing description")
    elif len(desc) > 1024:
        err.append(f"{rel}: description {len(desc)} chars (>1024)")
    else:
        print(f"✅ {rel}: {name} ({len(desc)} chars)")
    base = path.parent
    for ref in re.findall(r"`((?:references|templates|cases)/[^`]+\.md)`", text):
        if not (base / ref).exists():
            err.append(f"{rel}: missing {ref}")
    return text
router = check(root / "SKILL.md", "ai-startup-skills")
for n in EXPECTED:
    check(root / "skills" / n / "SKILL.md", n)
    if f"skills/{n}/SKILL.md" not in router:
        err.append(f"SKILL.md: router does not route to skills/{n}/SKILL.md")
extra = sorted(p.name for p in (root / "skills").iterdir() if p.is_dir() and p.name not in EXPECTED)
if extra:
    err.append(f"skills/: unexpected folders {extra}")
if err:
    print("\n".join("❌ " + e for e in err)); sys.exit(1)
print(f"✅ router + {len(EXPECTED)} sub-skills valid")

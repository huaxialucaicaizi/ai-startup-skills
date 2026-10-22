#!/usr/bin/env python3
"""Validate SKILL.md frontmatter, agents/openai.yaml and references links."""
import re, sys, pathlib, yaml
root = pathlib.Path(__file__).resolve().parent.parent
err = []
text = (root / "SKILL.md").read_text(encoding="utf-8")
m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
if not m:
    err.append("SKILL.md: missing YAML frontmatter")
else:
    fm = yaml.safe_load(m.group(1)) or {}
    name, desc = fm.get("name", ""), fm.get("description", "")
    if not re.fullmatch(r"[a-z0-9]+(-[a-z0-9]+)*", str(name)):
        err.append(f"SKILL.md: invalid name {name!r}")
    if not desc:
        err.append("SKILL.md: missing description")
    elif len(desc) > 500:
        err.append(f"SKILL.md: description {len(desc)} chars (>500)")
    else:
        print(f"✅ SKILL.md: {name} ({len(desc)} chars)")
for ref in re.findall(r"`((?:references|templates)/[^`]+\.md)`", text):
    if not (root / ref).exists():
        err.append(f"SKILL.md: missing {ref}")
oa = yaml.safe_load((root / "agents/openai.yaml").read_text(encoding="utf-8")) or {}
iface = oa.get("interface", {})
for k in ("display_name", "short_description", "default_prompt"):
    if not iface.get(k):
        err.append(f"agents/openai.yaml: missing interface.{k}")
if err:
    print("\n".join("❌ " + e for e in err)); sys.exit(1)
print("✅ agents/openai.yaml valid")

#!/usr/bin/env python3
"""Structural verification for author-toolkit: JSON validity + SKILL.md frontmatter."""
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
errors = []

json_files = [
    ROOT / ".claude-plugin" / "plugin.json",
    ROOT / ".claude-plugin" / "marketplace.json",
    ROOT / "references" / "finding-schema.json",
]
for f in json_files:
    if not f.exists():
        errors.append(f"missing: {f.relative_to(ROOT)}")
        continue
    try:
        json.loads(f.read_text())
    except json.JSONDecodeError as e:
        errors.append(f"invalid JSON in {f.relative_to(ROOT)}: {e}")

skills_dir = ROOT / "skills"
skill_dirs = sorted(d for d in skills_dir.iterdir() if d.is_dir()) if skills_dir.exists() else []
if not skill_dirs:
    errors.append("no skill directories found under skills/")

for d in skill_dirs:
    skill_md = d / "SKILL.md"
    if not skill_md.exists():
        errors.append(f"{d.name}: missing SKILL.md")
        continue
    text = skill_md.read_text()
    if not text.startswith("---"):
        errors.append(f"{d.name}/SKILL.md: missing YAML frontmatter block")
        continue
    end = text.find("\n---", 3)
    if end == -1:
        errors.append(f"{d.name}/SKILL.md: unterminated frontmatter block")
        continue
    frontmatter = text[3:end]
    if "name:" not in frontmatter:
        errors.append(f"{d.name}/SKILL.md: frontmatter missing 'name:'")
    if "description:" not in frontmatter:
        errors.append(f"{d.name}/SKILL.md: frontmatter missing 'description:'")

if errors:
    print(f"FAIL: {len(errors)} issue(s) found")
    for e in errors:
        print(f"  - {e}")
    sys.exit(1)

print(f"OK: {len(json_files)} JSON file(s) valid, {len(skill_dirs)} skill(s) have valid SKILL.md frontmatter")
sys.exit(0)

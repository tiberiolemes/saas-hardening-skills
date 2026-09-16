#!/usr/bin/env python3
"""Validate the public structure of the SaaS Hardening Skills framework."""

from __future__ import annotations

import re
import sys
from pathlib import Path


EXPECTED = {
    "saas-hardening-orchestrator",
    "saas-baseline",
    "appsec-auditor",
    "tenant-isolation-auditor",
    "database-integrity-auditor",
    "code-health-auditor",
    "performance-auditor",
    "ux-accessibility-auditor",
    "production-readiness-auditor",
}
NAME_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
PLACEHOLDER_RE = re.compile(r"(?:TODO|FIXME|<skill-name>|<description>)")


def frontmatter(text: str, path: Path) -> tuple[str, str]:
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        raise ValueError(f"{path}: SKILL.md must start with YAML frontmatter")
    try:
        end = lines.index("---", 1)
    except ValueError as exc:
        raise ValueError(f"{path}: frontmatter is not closed") from exc
    fields: dict[str, str] = {}
    for line in lines[1:end]:
        if not line.strip():
            continue
        if ":" not in line or line.startswith((" ", "\t")):
            continue
        key, value = line.split(":", 1)
        fields[key.strip()] = value.strip().strip('"\'')
    if not fields.get("name") or not fields.get("description"):
        raise ValueError(f"{path}: frontmatter needs name and description")
    return fields["name"], fields["description"]


def validate_yaml(path: Path) -> None:
    text = path.read_text(encoding="utf-8")
    if "interface:" not in text:
        raise ValueError(f"{path}: missing interface section")
    for key in ("display_name", "short_description", "default_prompt"):
        match = re.search(rf"^  {key}: (.+)$", text, re.MULTILINE)
        if not match or not (
            match.group(1).startswith('"') and match.group(1).endswith('"')
        ):
            raise ValueError(f"{path}: {key} must be a quoted string")
    prompt = re.search(r'^  default_prompt: "([^"]+)"$', text, re.MULTILINE)
    if not prompt or "$" not in prompt.group(1):
        raise ValueError(f"{path}: default_prompt must mention the Skill explicitly")


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    skills_root = root / "skills"
    actual = (
        {p.name for p in skills_root.iterdir() if p.is_dir()}
        if skills_root.exists()
        else set()
    )
    errors: list[str] = []

    if actual != EXPECTED:
        errors.append(f"skills/: expected {sorted(EXPECTED)}, found {sorted(actual)}")

    for name in sorted(actual):
        skill_dir = skills_root / name
        skill_path = skill_dir / "SKILL.md"
        try:
            skill_text = skill_path.read_text(encoding="utf-8")
            skill_name, description = frontmatter(skill_text, skill_path)
            if skill_name != name:
                raise ValueError(f"{skill_path}: name {skill_name!r} does not match folder")
            if not NAME_RE.fullmatch(skill_name):
                raise ValueError(f"{skill_path}: invalid skill name")
            if len(description) < 20:
                raise ValueError(f"{skill_path}: description is too short")
            if PLACEHOLDER_RE.search(skill_text):
                raise ValueError(f"{skill_path}: unfinished placeholder found")
            yaml_path = skill_dir / "agents" / "openai.yaml"
            if yaml_path.exists():
                validate_yaml(yaml_path)
        except (OSError, ValueError) as exc:
            errors.append(str(exc))

    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1
    print(f"Validated {len(actual)} Skills and their optional UI metadata.")
    return 0


if __name__ == "__main__":
    sys.exit(main())

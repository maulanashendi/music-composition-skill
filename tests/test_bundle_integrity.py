"""
Bundle integrity tests for music-composition-skill.

Catches silent discovery failures:
- Skill directories without SKILL.md
- Missing frontmatter in SKILL.md files
- Broken path references in markdown
- Registry/template inconsistencies
"""

import json
import os
import re
from pathlib import Path


# Root of the skill bundle (repo root)
BUNDLE_ROOT = Path(__file__).parent.parent
SKILLS_DIR = BUNDLE_ROOT / "skills"


def test_setiap_direktori_skill_punya_skill_md():
    """
    Setiap subdirektori di skills/ harus punya SKILL.md.
    Lewati direktori yang namanya diawali titik dan direktori 'templates'.
    """
    failed = []

    if not SKILLS_DIR.exists():
        raise AssertionError(f"skills/ directory not found at {SKILLS_DIR}")

    for item in SKILLS_DIR.iterdir():
        if not item.is_dir():
            continue

        dirname = item.name

        # Skip dot directories
        if dirname.startswith("."):
            continue

        # Skip templates directory
        if dirname == "templates":
            continue

        skill_md = item / "SKILL.md"
        if not skill_md.exists():
            failed.append(dirname)

    assert not failed, (
        f"The following skill directories are missing SKILL.md: {', '.join(failed)}"
    )


def test_setiap_skill_md_punya_frontmatter_name_dan_description():
    """
    Setiap skills/*/SKILL.md harus punya frontmatter dengan 'name:' dan 'description:'.
    Baris pertama harus '---', dan blok frontmatter harus berisi kedua field itu.
    """
    failed = []

    for skill_dir in SKILLS_DIR.iterdir():
        if not skill_dir.is_dir():
            continue

        dirname = skill_dir.name

        # Skip dot directories and templates
        if dirname.startswith(".") or dirname == "templates":
            continue

        skill_md = skill_dir / "SKILL.md"
        if not skill_md.exists():
            # Already caught by test 1, skip here
            continue

        content = skill_md.read_text(encoding="utf-8")
        lines = content.split("\n")

        # Check first line is '---'
        if not lines or lines[0] != "---":
            failed.append((dirname, "First line is not '---'"))
            continue

        # Find closing '---'
        closing_idx = None
        for i in range(1, len(lines)):
            if lines[i] == "---":
                closing_idx = i
                break

        if closing_idx is None:
            failed.append((dirname, "No closing '---' found"))
            continue

        # Extract frontmatter lines
        frontmatter = lines[1:closing_idx]
        frontmatter_text = "\n".join(frontmatter)

        # Check for 'name:' field
        has_name = any(line.startswith("name:") for line in frontmatter)
        has_description = any(line.startswith("description:") for line in frontmatter)

        if not has_name:
            failed.append((dirname, "Missing 'name:' field in frontmatter"))

        if not has_description:
            failed.append((dirname, "Missing 'description:' field in frontmatter"))

    assert not failed, (
        f"Frontmatter issues in SKILL.md files:\n" +
        "\n".join(f"  {d}: {msg}" for d, msg in failed)
    )


def test_rujukan_path_relatif_di_markdown_bundle_resolve():
    """Setiap rujukan EKSPLISIT RELATIF (./ atau ../) di markdown bundle harus resolve.

    Sengaja HANYA yang eksplisit relatif: nama berkas polos seperti `plan.json`,
    `notes.md`, `project.json` adalah artefak yang AGEN BUAT saat runtime, bukan
    rujukan ke berkas bundle -- memeriksanya menghasilkan merah palsu.

    Bug nyata yang jadi alasan test ini ada tetap tertangkap: schema.md pernah
    merujuk `../assets/composition-plan-template.json` yang tak pernah ada.
    """
    known_broken_file = BUNDLE_ROOT / "tests" / "known_broken_refs.txt"
    known_broken = set()
    if known_broken_file.exists():
        for line in known_broken_file.read_text(encoding="utf-8").splitlines():
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            parts = line.split(" :: ")
            known_broken.add((parts[0], parts[1]))

    ref_re = re.compile(r"`(\.{1,2}/[.\w/-]+\.(?:md|json))`")
    broken = []
    for path in sorted(BUNDLE_ROOT.glob('skills/**/*.md')):
        text = path.read_text(encoding="utf-8")
        base = str(path.parent)
        for ref in set(ref_re.findall(text)):
            if "*" in ref or "<" in ref:
                continue
            target = os.path.normpath(os.path.join(base, ref))
            if not os.path.exists(target):
                src = str(path.relative_to(BUNDLE_ROOT))
                if (src, ref) in known_broken:
                    continue
                broken.append((src, ref))

    assert not broken, "Rujukan path relatif yang menggantung:\n" + "\n".join(
        f"  {src}: {ref}" for src, ref in sorted(broken))

    stale = []
    for src, ref in sorted(known_broken):
        target = os.path.normpath(os.path.join(BUNDLE_ROOT, os.path.dirname(src), ref))
        if os.path.exists(target):
            stale.append((src, ref))

    assert not stale, "entri known_broken_refs.txt sudah tak berlaku, hapus:\n" + "\n".join(
        f"  {src}: {ref}" for src, ref in stale)

def test_registry_dan_template_konsisten():
    """
    Baca skills/jazz-composition/templates/registry.md. Ambil baris tabel yang
    sel pertamanya berisi id ber-backtick (regex '^\\|\\s*`([a-z0-9-]+)`\\s*\\|').
    Untuk tiap id:
      - Berkas templates/<id>.json harus ada
      - 'when_to_use' di dalamnya harus SAMA PERSIS (setelah strip) dengan sel ketiga
    Sebaliknya, setiap templates/*.json harus punya baris di registry.
    """
    templates_dir = SKILLS_DIR / "jazz-composing" / "templates"
    registry_file = templates_dir / "registry.md"

    if not templates_dir.exists():
        raise AssertionError(f"templates/ directory not found at {templates_dir}")

    if not registry_file.exists():
        raise AssertionError(f"registry.md not found at {registry_file}")

    registry_content = registry_file.read_text(encoding="utf-8")

    # Extract table rows: pattern ^\|\s*`([a-z0-9-]+)`\s*\|...\|
    # The third column (when_to_use) is what we need to match
    table_pattern = r"^\|\s*`([a-z0-9-]+)`\s*\|[^|]*\|([^|]+)\|"

    registry_entries = {}
    for line in registry_content.split("\n"):
        match = re.match(table_pattern, line)
        if match:
            template_id = match.group(1)
            when_to_use_from_registry = match.group(2).strip()
            registry_entries[template_id] = when_to_use_from_registry

    failed = []

    # Check each registry entry has a corresponding template file
    # and the when_to_use field matches
    for template_id, when_to_use_registry in registry_entries.items():
        template_file = templates_dir / f"{template_id}.json"

        if not template_file.exists():
            failed.append((template_id, f"Template file {template_id}.json not found"))
            continue

        # Load the template JSON
        try:
            template_data = json.loads(template_file.read_text(encoding="utf-8"))
        except json.JSONDecodeError as e:
            failed.append((template_id, f"Invalid JSON in {template_id}.json: {e}"))
            continue

        # Check for when_to_use field
        if "when_to_use" not in template_data:
            failed.append((template_id, f"Missing 'when_to_use' field in {template_id}.json"))
            continue

        when_to_use_file = template_data["when_to_use"].strip()

        # Compare
        if when_to_use_file != when_to_use_registry:
            failed.append((
                template_id,
                f"'when_to_use' mismatch: "
                f"registry='{when_to_use_registry}' vs "
                f"file='{when_to_use_file}'"
            ))

    # Check each template file has a registry entry
    for template_file in templates_dir.glob("*.json"):
        template_id = template_file.stem

        if template_id not in registry_entries:
            failed.append((
                template_id,
                f"Template {template_id}.json exists but has no entry in registry.md"
            ))

    assert not failed, (
        f"Registry and template inconsistencies:\n" +
        "\n".join(f"  {tid}: {msg}" for tid, msg in failed)
    )

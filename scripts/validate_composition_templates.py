#!/usr/bin/env python3
"""Validate style templates at the composition level, without using the engine."""

from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

REQUIRED_OUTLINE_HEADINGS = (
    "Tempo",
    "Key",
    "Form",
    "Harmony",
    "Hook",
    "Bass behavior",
    "Drum intent",
    "Arrangement development",
    "Ending",
)


@dataclass
class Finding:
    template_id: str
    severity: str
    message: str


@dataclass
class TemplateResult:
    template_id: str
    passed: bool = True
    checks: dict[str, bool] = field(default_factory=dict)
    findings: list[Finding] = field(default_factory=list)

    def check(self, name: str, condition: bool, message: str) -> None:
        self.checks[name] = condition
        if not condition:
            self.passed = False
            self.findings.append(Finding(self.template_id, "error", message))


def find_repo_root(start: Path) -> Path:
    for candidate in (start, *start.parents):
        if (candidate / "skills/jazz-composing/templates").exists():
            return candidate
    raise FileNotFoundError("Could not locate skills/jazz-composing/templates")


def load_registry(path: Path) -> dict[str, str]:
    entries: dict[str, str] = {}
    pattern = re.compile(r"^\|\s*`([a-z0-9-]+)`\s*\|[^|]*\|([^|]+)\|")
    for line in path.read_text(encoding="utf-8").splitlines():
        match = pattern.match(line)
        if match:
            entries[match.group(1)] = match.group(2).strip()
    return entries


def contains_number(value: Any, number: int) -> bool:
    if isinstance(value, dict):
        return any(contains_number(item, number) for item in value.values())
    if isinstance(value, list):
        return any(contains_number(item, number) for item in value)
    return str(number) in str(value)


def validate_template(template: dict[str, Any], path: Path, outlines_dir: Path, known_ids: set[str], registry: dict[str, str]) -> TemplateResult:
    template_id = template.get("id", path.stem)
    result = TemplateResult(template_id)

    result.check("id_matches_filename", template_id == path.stem, "id must match the JSON filename")
    result.check("registered", template_id in registry, "template must have a registry entry")
    result.check(
        "when_to_use_matches_registry",
        template_id in registry and template.get("when_to_use", "").strip() == registry[template_id],
        "when_to_use must exactly match registry.md",
    )

    defaults = template.get("defaults", {})
    harmony = template.get("harmony_palette", {})
    hooks = template.get("hook_archetypes", [])
    melody = template.get("melody_phrasing", {})
    drums = template.get("drum_skeleton", {})
    arrangement = template.get("arrangement_defaults", {})
    bass = template.get("bass_behavior", {})
    groove = template.get("groove_intent", {})
    differentiation = template.get("differentiation", {})
    status = template.get("composition_status", {})
    form = template.get("form_archetype", [])

    result.check("genre_identity", bool(template.get("style")) and bool(template.get("when_to_use")), "style and when_to_use must define a genre identity")
    result.check("harmony_language", len(harmony.get("diatonic_core", [])) >= 4 and len(harmony.get("signature_moves", [])) >= 2 and bool(harmony.get("avoid")), "harmony palette needs core chords, signature moves, and avoid rules")
    result.check("melodic_language", len(hooks) >= 1 and len(melody) >= 3 and all({"note_lengths", "contour", "placement"}.issubset(v) for v in melody.values()), "hooks and phase-specific melody phrasing must be complete")
    result.check("form_development", isinstance(form, list) and len(form) >= 5 and len(set(form)) >= 4, "form_archetype must describe a developed multi-section form")
    result.check("groove_intent", {"feel", "kick", "snare", "hihat", "ensemble_relationship"}.issubset(groove), "groove_intent must specify feel and role relationships")
    result.check("bass_behavior", {"role", "rhythmic_relationship", "density", "articulation"}.issubset(bass), "bass_behavior must define role, rhythm, density, and articulation")
    result.check("instrument_behavior", len(arrangement.get("entrance_order", [])) >= 3 and bool(arrangement.get("layout_rules")) and {"low_energy", "mid_energy", "high_energy"}.issubset(drums), "arrangement and drum roles must be behavioral, not a bare instrument list")
    result.check("reference_key", template.get("palette_reference_key") in defaults.get("key_options", []), "palette_reference_key must be one of defaults.key_options")
    result.check("anti_boredom", len(template.get("anti_boredom_rules", [])) >= 3, "anti_boredom_rules must define variation constraints")

    nearest = differentiation.get("nearest_templates", [])
    traits = differentiation.get("distinguishing_traits", [])
    result.check("differentiation", len(nearest) >= 1 and all(item in known_ids and item != template_id for item in nearest) and len(traits) >= 3 and len(set(traits)) == len(traits), "differentiation must identify nearby templates and at least three unique distinguishing traits")

    expected_status = {
        "defined": True,
        "outline_validated": True,
        "desk_reviewed": True,
        "listening_reviewed": False,
    }
    result.check("composition_status", status == expected_status, "composition_status must reflect desk validation without claiming listening validation")

    outline_path = outlines_dir / f"{template_id}.md"
    result.check("outline_exists", outline_path.exists(), "canonical composition outline is missing")
    if outline_path.exists():
        outline = outline_path.read_text(encoding="utf-8")
        headings_present = all(re.search(rf"\*\*{re.escape(heading)}:\*\*", outline) for heading in REQUIRED_OUTLINE_HEADINGS)
        result.check("outline_complete", headings_present, "outline must contain all required composition headings")
        result.check("outline_substantive", len(outline.split()) >= 110, "outline must be substantive enough to demonstrate the template")

    # Targeted regression checks for the two contradictions found during desk review.
    if template_id == "cool-modal-quintet":
        tempo_range = defaults.get("tempo_range")
        result.check("cool_tempo_range", tempo_range == [100, 125], "cool-modal-quintet must use the selected 100-125 BPM design center")
        result.check("cool_no_stale_fast_range", not contains_number(template, 140) and not contains_number(template, 175), "cool-modal-quintet still contains the stale 140-175 BPM range")
        identity_text = " ".join([template.get("when_to_use", ""), template.get("style", "")]).lower()
        result.check("cool_no_competing_identity", "west coast" not in identity_text, "the pianoless west-coast quartet must not be presented as a second competing primary identity")
        pianoless_mentions = [v for v in json.dumps(template).lower().split('"') if "pianoless" in v]
        result.check("cool_primary_identity", bool(pianoless_mentions) and any("optional" in v for v in pianoless_mentions), "pianoless counterpoint must be explicitly framed as optional somewhere in the template")

    if template_id == "hiphop-jazz-boombap":
        low = drums.get("low_energy", "").lower()
        optional = drums.get("optional_half_time_variant", "").lower()
        result.check("boombap_regular_backbeat", "beats 2 and 4" in low, "regular-time boom-bap must place the snare on beats 2 and 4")
        result.check("boombap_half_time_explicit", "half-time" in optional and "beat 3" in optional, "beat-3 snare must be isolated as an explicitly labeled half-time option")

    return result


def validate(root: Path) -> tuple[list[TemplateResult], list[Finding]]:
    templates_dir = root / "skills/jazz-composing/templates"
    outlines_dir = root / "skills/jazz-composing/examples/composition-outlines"
    registry = load_registry(templates_dir / "registry.md")

    paths = sorted(templates_dir.glob("*.json"))
    data = [json.loads(path.read_text(encoding="utf-8")) for path in paths]
    known_ids = {template.get("id", path.stem) for template, path in zip(data, paths)}

    global_findings: list[Finding] = []
    if len(paths) != 10:
        global_findings.append(Finding("GLOBAL", "error", f"expected 10 templates, found {len(paths)}"))
    if len(known_ids) != len(paths):
        global_findings.append(Finding("GLOBAL", "error", "template ids must be unique"))
    if set(registry) != known_ids:
        global_findings.append(Finding("GLOBAL", "error", "registry ids and template ids differ"))

    results = [validate_template(template, path, outlines_dir, known_ids, registry) for template, path in zip(data, paths)]

    # Pairwise structural differentiation: no two templates may share the same
    # form, groove feel, bass role, and harmony signature set.
    fingerprints: dict[str, str] = {}
    for template in data:
        fingerprint = json.dumps({
            "form": template["form_archetype"],
            "groove": template["groove_intent"]["feel"],
            "bass": template["bass_behavior"]["role"],
            "signature_moves": template["harmony_palette"]["signature_moves"],
        }, sort_keys=True)
        other = fingerprints.get(fingerprint)
        if other:
            global_findings.append(Finding("GLOBAL", "error", f"{template['id']} is structurally indistinguishable from {other}"))
        fingerprints[fingerprint] = template["id"]

    return results, global_findings


def report_markdown(results: list[TemplateResult], global_findings: list[Finding]) -> str:
    lines = [
        "# Composition Template Validation Report",
        "",
        "Scope: composition-level structure and musical intent only. Engine, MIDI, audio, and listening tests are excluded.",
        "",
        "| Template | Result | Checks passed |",
        "|---|---:|---:|",
    ]
    for result in sorted(results, key=lambda item: item.template_id):
        passed_count = sum(result.checks.values())
        lines.append(f"| `{result.template_id}` | {'PASS' if result.passed else 'FAIL'} | {passed_count}/{len(result.checks)} |")

    total_passed = sum(result.passed for result in results)
    lines.extend([
        "",
        "## Summary",
        "",
        f"- Templates found: {len(results)}",
        f"- Composition desk-validated: {total_passed}/{len(results)}",
        f"- Canonical outlines complete: {sum(result.checks.get('outline_complete', False) for result in results)}/{len(results)}",
        f"- Global findings: {len(global_findings)}",
        "- Listening validation: not claimed",
        "- Engine validation: not performed",
    ])

    all_findings = global_findings + [finding for result in results for finding in result.findings]
    if all_findings:
        lines.extend(["", "## Findings", ""])
        for finding in all_findings:
            lines.append(f"- **{finding.severity.upper()} — {finding.template_id}:** {finding.message}")
    else:
        lines.extend(["", "## Findings", "", "No composition-level validation errors found."])

    lines.extend([
        "",
        "## Completion criteria",
        "",
        "Each passing template has a clear genre identity, appropriate harmonic and melodic language, developed form, musician-readable groove intent, behavioral instrument roles, explicit differentiation, no known internal contradiction, and a complete canonical outline.",
        "",
    ])
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve())
    parser.add_argument("--report", type=Path)
    args = parser.parse_args()

    root = find_repo_root(args.root.resolve())
    results, global_findings = validate(root)
    report = report_markdown(results, global_findings)
    print(report)
    if args.report:
        args.report.parent.mkdir(parents=True, exist_ok=True)
        args.report.write_text(report + "\n", encoding="utf-8")

    return 0 if all(result.passed for result in results) and not global_findings else 1


if __name__ == "__main__":
    sys.exit(main())

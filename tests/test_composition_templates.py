"""Composition-level validation for jazz-composing style templates."""

from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
VALIDATOR_PATH = ROOT / "scripts/validate_composition_templates.py"
SPEC = importlib.util.spec_from_file_location("composition_validator", VALIDATOR_PATH)
assert SPEC and SPEC.loader
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


def test_all_ten_templates_are_composition_validated():
    results, global_findings = MODULE.validate(ROOT)

    assert len(results) == 10
    assert not global_findings, "\n".join(f"{item.template_id}: {item.message}" for item in global_findings)

    failed = [result for result in results if not result.passed]
    assert not failed, "\n".join(
        f"{result.template_id}: " + "; ".join(item.message for item in result.findings)
        for result in failed
    )

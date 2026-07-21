from __future__ import annotations

import importlib.util
import json
import os
import subprocess
import sys
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent
MODULE_PATH = HERE / "validate_composition.py"
spec = importlib.util.spec_from_file_location("validate_composition", MODULE_PATH)
assert spec and spec.loader
validator = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = validator
spec.loader.exec_module(validator)


def load(rel):
    with open(HERE / "fixtures" / rel, encoding="utf-8") as f:
        return json.load(f)


class ValidateCompositionTests(unittest.TestCase):
    def test_valid_minimal_passes(self):
        self.assertEqual(validator.validate_composition(load("valid/minimal.json")), [])

    def test_bad_instrument_flagged(self):
        v = validator.validate_composition(load("invalid/bad-instrument.json"))
        self.assertTrue(any("instrument" in x for x in v), v)

    def test_bar_overflow_flagged(self):
        v = validator.validate_composition(load("invalid/bar-overflow.json"))
        self.assertTrue(any("melewati bar" in x for x in v), v)

    def test_bad_drum_flagged(self):
        v = validator.validate_composition(load("invalid/bad-drum.json"))
        self.assertTrue(any("drum" in x for x in v), v)

    def test_missing_meta_collects_multiple(self):
        v = validator.validate_composition(load("invalid/missing-meta.json"))
        self.assertGreater(len(v), 1)

    def test_cli_exit_codes(self):
        ok = subprocess.run(
            [sys.executable, str(MODULE_PATH), str(HERE / "fixtures/valid/minimal.json")],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
        self.assertEqual(ok.returncode, 0)
        bad = subprocess.run(
            [sys.executable, str(MODULE_PATH), str(HERE / "fixtures/invalid/bad-drum.json")],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
        self.assertEqual(bad.returncode, 1)


if __name__ == "__main__":
    unittest.main()

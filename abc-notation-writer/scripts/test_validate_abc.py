from __future__ import annotations

import importlib.util
import sys
import tempfile
import unittest
from pathlib import Path
from types import SimpleNamespace

MODULE_PATH = Path(__file__).resolve().parents[0] / "validate_abc.py"
spec = importlib.util.spec_from_file_location("jazz_validate_abc", MODULE_PATH)
assert spec and spec.loader
validator = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = validator
spec.loader.exec_module(validator)

HEADER = """X:1
T:Test
M:4/4
L:1/8
Q:1/4=120
K:C
V:Melody clef=treble
"""


def run_abc(body: str, header: str = HEADER):
    with tempfile.TemporaryDirectory() as tmp:
        path = Path(tmp) / "test.abc"
        path.write_text(header + body, encoding="utf-8")
        errors, warnings = validator.validate(path)
        return SimpleNamespace(ok=not errors, errors=errors, warnings=warnings)


class ABCValidatorTests(unittest.TestCase):
    def test_simple_bars(self):
        result = run_abc('V:Melody\n"Cmaj7"C2 E2 G2 B2 | c8 |]\n')
        self.assertTrue(result.ok, result.errors)

    def test_pickup_and_complement(self):
        result = run_abc("V:Melody\nG A | c4 B2 A2 | G2 F2 E2 D2 | C6 |]\n")
        self.assertTrue(result.ok, result.errors)
        self.assertTrue(any("pickup" in item for item in result.warnings))

    def test_pickup_without_short_final_is_warning_not_error(self):
        result = run_abc("V:Melody\nG A | c4 B2 A2 | G2 F2 E2 D2 | C8 |]\n")
        self.assertTrue(result.ok, result.errors)
        self.assertTrue(any("without a complementary" in item for item in result.warnings))

    def test_triplet(self):
        result = run_abc("V:Melody\n(3CDE F2 G2 A2 | B8 |]\n")
        self.assertTrue(result.ok, result.errors)

    def test_bracketed_chords_are_simultaneous(self):
        result = run_abc("V:Melody\n[CEG]2 [DFA]2 [EGB]2 [FAC]2 | [CEGc]8 |]\n")
        self.assertTrue(result.ok, result.errors)

    def test_broken_rhythm(self):
        result = run_abc("V:Melody\nC>D E>F G>A B>c | c<B A<G F>E D>C |]\n")
        self.assertTrue(result.ok, result.errors)

    def test_multiple_voices(self):
        header = HEADER.replace(
            "V:Melody clef=treble\n",
            "V:Melody clef=treble\nV:Riff clef=treble\n",
        )
        body = "[V:Melody] C2 E2 G2 c2 | d8 |]\n[V:Riff] z8 | G2 A2 B2 c2 |]\n"
        result = run_abc(body, header)
        self.assertTrue(result.ok, result.errors)

    def test_inline_meter_changes(self):
        result = run_abc(
            "V:Melody\nC2 E2 G2 c2 | [M:3/4] d2 c2 B2 | [M:5/4] A2 B2 c2 d2 e2 |]\n"
        )
        self.assertTrue(result.ok, result.errors)

    def test_overlay_uses_longest_layer(self):
        result = run_abc("V:Melody\nC2 E2 G2 c2 & G,2 B,2 D2 G2 |]\n")
        self.assertTrue(result.ok, result.errors)
        self.assertTrue(any("overlay" in item for item in result.warnings))

    def test_multimeasure_rest(self):
        result = run_abc("V:Melody\nZ4 | C2 E2 G2 c2 |]\n")
        self.assertTrue(result.ok, result.errors)

    def test_invalid_single_partial_bar_fails(self):
        result = run_abc("V:Melody\nC2 E2 G2 |]\n")
        self.assertFalse(result.ok)
        self.assertTrue(any("duration" in item for item in result.errors))

    def test_invalid_interior_bar_fails(self):
        result = run_abc("V:Melody\nC8 | C2 E2 G2 | C8 |]\n")
        self.assertFalse(result.ok)
        self.assertTrue(any("bar 2" in item for item in result.errors))


if __name__ == "__main__":
    unittest.main()

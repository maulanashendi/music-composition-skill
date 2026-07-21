from __future__ import annotations

import contextlib
import importlib.util
import io
import json
import sys
import unittest
from pathlib import Path

SCRIPTS_DIR = Path(__file__).resolve().parents[0]
TEMPLATE_PATH = SCRIPTS_DIR.parent / "assets" / "drum-grid-template.json"


def _load(module_name: str, filename: str):
    module_path = SCRIPTS_DIR / filename
    spec = importlib.util.spec_from_file_location(module_name, module_path)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


drums_to_engine = _load("jazz_drums_to_engine", "drums_to_engine.py")

BAR_A = {"kick": "x.......", "chh": "x.x.x.x."}
BAR_B = {"kick": "x...x...", "chh": "x.x.x.x."}
BAR_C = {"kick": "....x...", "snare": "....x..."}


def make_spec(sections) -> dict:
    return {
        "steps_per_bar": 8,
        "gm_map": {"kick": 36, "snare": 38, "chh": 42},
        "base_velocity": {"kick": 96, "snare": 82, "chh": 58},
        "swing": 0.56,
        "sections": sections,
    }


def convert_quiet(spec):
    """Jalankan convert() sambil menangkap stderr (warning) untuk di-assert."""
    stderr = io.StringIO()
    with contextlib.redirect_stderr(stderr):
        engine = drums_to_engine.convert(spec)
    return engine, stderr.getvalue()


class V2MergeTests(unittest.TestCase):
    def test_v2_four_bars_two_identical_then_two_distinct_gives_three_sections(self):
        # Test wajib spec E2 #1: 4 bar (2 identik berurutan + 2 beda)
        # -> sections [{bars:2}, {bars:1}, {bars:1}]
        spec = make_spec([{"bars": 4, "pattern": [BAR_A, BAR_A, BAR_B, BAR_C]}])
        engine, _ = convert_quiet(spec)
        self.assertEqual([s["bars"] for s in engine["sections"]], [2, 1, 1])
        self.assertEqual(engine["sections"][0]["pattern"], BAR_A)
        self.assertEqual(engine["sections"][1]["pattern"], BAR_B)
        self.assertEqual(engine["sections"][2]["pattern"], BAR_C)


class V1PassthroughTests(unittest.TestCase):
    def test_v1_dict_pattern_passes_through_as_single_section(self):
        # Test wajib spec E2 #2: v1 pattern-dict -> passthrough satu section.
        spec = make_spec([{"bars": 4, "pattern": BAR_A}])
        engine, _ = convert_quiet(spec)
        self.assertEqual(engine["sections"], [{"bars": 4, "pattern": BAR_A}])
        self.assertEqual(engine["steps_per_bar"], 8)
        self.assertEqual(engine["swing"], 0.56)
        self.assertEqual(
            set(engine),
            {"steps_per_bar", "gm_map", "base_velocity", "swing", "sections"},
        )


class ForeignFieldTests(unittest.TestCase):
    def test_foreign_fields_dropped_and_warned_by_name(self):
        # Test wajib spec E2 #3: field asing dibuang + warning menyebut namanya.
        spec = make_spec(
            [{"bars": 1, "pattern": BAR_A, "label": "Intro",
              "phrase_velocity": [1.0]}])
        spec["tempo_bpm"] = 90
        spec["beats_per_bar"] = 4
        spec["humanize_velocity"] = 6
        spec["timing"] = {"kick": 0}
        spec["title"] = "T"
        spec["_comment"] = "c"
        engine, warnings = convert_quiet(spec)
        for field in ("tempo_bpm", "beats_per_bar", "humanize_velocity",
                      "timing", "title", "_comment"):
            self.assertNotIn(field, engine)
            self.assertIn(field, warnings)
        self.assertEqual(set(engine["sections"][0]), {"bars", "pattern"})
        self.assertIn("phrase_velocity", warnings)
        self.assertIn("label", warnings)
        self.assertIn("WARNING", warnings)


class ValidationTests(unittest.TestCase):
    def test_invalid_steps_per_bar_raises_with_clear_message(self):
        # Test wajib spec E2 #4: steps_per_bar di luar {8,12,16} -> error jelas.
        spec = make_spec([{"bars": 1, "pattern": BAR_A}])
        spec["steps_per_bar"] = 10
        with self.assertRaises(ValueError) as ctx:
            convert_quiet(spec)
        self.assertIn("steps_per_bar", str(ctx.exception))
        self.assertIn("10", str(ctx.exception))

    def test_invalid_pattern_char_raises(self):
        spec = make_spec([{"bars": 1, "pattern": {"kick": "x..?...."}}])
        with self.assertRaises(ValueError) as ctx:
            convert_quiet(spec)
        self.assertIn("kick", str(ctx.exception))

    def test_gm_map_out_of_range_raises(self):
        spec = make_spec([{"bars": 1, "pattern": BAR_A}])
        spec["gm_map"]["kick"] = 90  # > 81
        with self.assertRaises(ValueError) as ctx:
            convert_quiet(spec)
        self.assertIn("gm_map", str(ctx.exception))

    def test_base_velocity_out_of_range_raises(self):
        spec = make_spec([{"bars": 1, "pattern": BAR_A}])
        spec["base_velocity"]["kick"] = 0
        with self.assertRaises(ValueError) as ctx:
            convert_quiet(spec)
        self.assertIn("base_velocity", str(ctx.exception))

    def test_base_velocity_bool_raises(self):
        """bool adalah subclass int di Python — True == 1 tak boleh lolos
        sebagai velocity valid."""
        spec = make_spec([{"bars": 1, "pattern": BAR_A}])
        spec["base_velocity"]["kick"] = True
        with self.assertRaises(ValueError) as ctx:
            convert_quiet(spec)
        self.assertIn("base_velocity", str(ctx.exception))

    def test_gm_map_bool_raises(self):
        """bool adalah subclass int di Python — True == 1 tak boleh lolos
        sebagai note GM valid."""
        spec = make_spec([{"bars": 1, "pattern": BAR_A}])
        spec["gm_map"]["kick"] = True
        with self.assertRaises(ValueError) as ctx:
            convert_quiet(spec)
        self.assertIn("gm_map", str(ctx.exception))

    def test_v2_pattern_list_length_mismatch_raises(self):
        spec = make_spec([{"bars": 3, "pattern": [BAR_A]}])
        with self.assertRaises(ValueError):
            convert_quiet(spec)

    def test_v1_row_length_mismatch_steps_per_bar_raises_with_clear_message(self):
        # steps_per_bar: 16 tapi baris voice cuma 8 char -> engine /api/render
        # akan menolak dengan 422; konverter harus fail-fast di sini dulu.
        spec = make_spec([{"bars": 1, "pattern": {"kick": "x......."}}])
        spec["steps_per_bar"] = 16
        with self.assertRaises(ValueError) as ctx:
            convert_quiet(spec)
        message = str(ctx.exception)
        self.assertIn("kick", message)
        self.assertIn("8", message)
        self.assertIn("16", message)

    def test_v2_bar_row_length_mismatch_steps_per_bar_raises(self):
        # v2 list: satu bar punya baris voice dengan panjang salah.
        bad_bar = {"kick": "x.......", "chh": "x.x.x.x."}  # 8 char, harus 16
        spec = make_spec([{"bars": 1, "pattern": [bad_bar]}])
        spec["steps_per_bar"] = 16
        with self.assertRaises(ValueError) as ctx:
            convert_quiet(spec)
        message = str(ctx.exception)
        self.assertIn("kick", message)
        self.assertIn("16", message)


class TemplateRegressionTests(unittest.TestCase):
    def test_current_template_asset_converts_to_valid_engine_schema(self):
        # Test wajib spec E2 #5: template asset SAAT INI sebagai regression
        # fixture (bukan fixture buatan sendiri).
        spec = json.loads(TEMPLATE_PATH.read_text(encoding="utf-8"))
        engine, _ = convert_quiet(spec)
        self.assertEqual(
            set(engine),
            {"steps_per_bar", "gm_map", "base_velocity", "swing", "sections"},
        )
        self.assertIn(engine["steps_per_bar"], (8, 12, 16))
        for note in engine["gm_map"].values():
            self.assertTrue(35 <= note <= 81)
        for vel in engine["base_velocity"].values():
            self.assertTrue(1 <= vel <= 127)
        # Template: intro 2 bar (dict) + A 4 bar (list, semua bar beda karena
        # rimshot bar-2 beda) + B 4 bar (bar 1-2 identik -> merge) + outro 2
        # bar (dict) = total 12 bar, 9 section engine.
        self.assertEqual(sum(s["bars"] for s in engine["sections"]), 12)
        self.assertEqual(len(engine["sections"]), 9)
        for section in engine["sections"]:
            self.assertEqual(set(section), {"bars", "pattern"})
            self.assertGreaterEqual(section["bars"], 1)
            for row in section["pattern"].values():
                self.assertTrue(set(row) <= set("xXg."))


if __name__ == "__main__":
    unittest.main()

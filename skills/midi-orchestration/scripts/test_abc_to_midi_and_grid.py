from __future__ import annotations

import importlib.util
import json
import sys
import tempfile
import unittest
from pathlib import Path

import pretty_midi

SCRIPTS_DIR = Path(__file__).resolve().parents[0]


def _load(module_name: str, filename: str):
    module_path = SCRIPTS_DIR / filename
    spec = importlib.util.spec_from_file_location(module_name, module_path)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


abc_to_midi = _load("jazz_abc_to_midi", "abc_to_midi.py")
grid_to_midi = _load("jazz_grid_to_midi", "grid_to_midi.py")

ABC_WITH_TEMPO_AND_METER = """X:1
T:TempoMeterTest
M:7/8
L:1/8
Q:1/8=160
K:C
V:Lead name="Lead" clef=treble
[V:Lead] CDEFGAB |]
"""

ABC_WITHOUT_TEMPO_OR_METER = """X:1
T:NoHeaderTest
L:1/8
K:C
V:Lead name="Lead" clef=treble
[V:Lead] CDEFGABc |]
"""


def render_abc(abc_text: str) -> pretty_midi.PrettyMIDI:
    with tempfile.TemporaryDirectory() as tmp:
        abc_path = Path(tmp) / "test.abc"
        abc_path.write_text(abc_text, encoding="utf-8")
        out_path = Path(tmp) / "out.mid"
        abc_to_midi.render(str(abc_path), str(out_path))
        return pretty_midi.PrettyMIDI(str(out_path))


def make_drum_spec(beats_per_bar=None) -> dict:
    """Minimal 2-bar, single-voice spec with one hit on step 0 of each bar."""
    spec = {
        "tempo_bpm": 120,
        "steps_per_bar": 4,
        "swing": 0.5,  # straight, no swing offset
        "humanize_velocity": 0,
        "gm_map": {"kick": 36},
        "base_velocity": {"kick": 100},
        "sections": [
            {"bars": 2, "pattern": {"kick": ["x", "", "", ""]}},
        ],
    }
    if beats_per_bar is not None:
        spec["beats_per_bar"] = beats_per_bar
    return spec


def build_drums(spec: dict) -> pretty_midi.PrettyMIDI:
    with tempfile.TemporaryDirectory() as tmp:
        spec_path = Path(tmp) / "spec.json"
        spec_path.write_text(json.dumps(spec), encoding="utf-8")
        out_path = Path(tmp) / "drums.mid"
        grid_to_midi.build_drums(str(spec_path), str(out_path))
        return pretty_midi.PrettyMIDI(str(out_path))


class AbcToMidiTempoMeterTests(unittest.TestCase):
    def test_tempo_and_meter_parsed_from_header(self):
        pm = render_abc(ABC_WITH_TEMPO_AND_METER)

        _, tempi = pm.get_tempo_changes()
        self.assertEqual(len(tempi), 1)
        self.assertAlmostEqual(tempi[0], 80.0, delta=0.5)

        self.assertEqual(len(pm.time_signature_changes), 1)
        ts = pm.time_signature_changes[0]
        self.assertEqual(ts.numerator, 7)
        self.assertEqual(ts.denominator, 8)

    def test_missing_headers_fall_back_to_default_without_raising(self):
        pm = render_abc(ABC_WITHOUT_TEMPO_OR_METER)

        _, tempi = pm.get_tempo_changes()
        self.assertEqual(len(tempi), 1)
        self.assertAlmostEqual(tempi[0], 120.0, delta=0.5)

        self.assertEqual(len(pm.time_signature_changes), 1)
        ts = pm.time_signature_changes[0]
        self.assertEqual(ts.numerator, 4)
        self.assertEqual(ts.denominator, 4)


class GridToMidiBeatsPerBarTests(unittest.TestCase):
    def test_custom_beats_per_bar_sets_sec_per_bar(self):
        # tempo 120 -> sec_per_beat = 0.5; beats_per_bar 3.5 -> sec_per_bar = 1.75
        pm = build_drums(make_drum_spec(beats_per_bar=3.5))
        notes = sorted(pm.instruments[0].notes, key=lambda n: n.start)
        self.assertEqual(len(notes), 2)
        self.assertAlmostEqual(notes[0].start, 0.0, places=3)
        self.assertAlmostEqual(notes[1].start, 1.75, places=3)

    def test_missing_beats_per_bar_defaults_to_four(self):
        # No beats_per_bar key at all: must behave exactly like an explicit 4.
        pm_default = build_drums(make_drum_spec(beats_per_bar=None))
        pm_explicit = build_drums(make_drum_spec(beats_per_bar=4))

        notes_default = sorted(pm_default.instruments[0].notes, key=lambda n: n.start)
        notes_explicit = sorted(pm_explicit.instruments[0].notes, key=lambda n: n.start)

        self.assertEqual(len(notes_default), 2)
        starts_default = [round(n.start, 3) for n in notes_default]
        starts_explicit = [round(n.start, 3) for n in notes_explicit]
        self.assertEqual(starts_default, starts_explicit)

        # tempo 120 -> sec_per_beat = 0.5; beats_per_bar 4 -> sec_per_bar = 2.0
        self.assertAlmostEqual(notes_default[0].start, 0.0, places=3)
        self.assertAlmostEqual(notes_default[1].start, 2.0, places=3)


def make_accent_ghost_spec(ch: str) -> dict:
    """Single-hit spec whose one step uses the given pattern character."""
    spec = make_drum_spec()
    spec["sections"] = [{"bars": 1, "pattern": {"kick": [ch, "", "", ""]}}]
    return spec


class GridToMidiAccentGhostTests(unittest.TestCase):
    def test_accent_X_has_higher_velocity_than_normal_x(self):
        pm_normal = build_drums(make_accent_ghost_spec("x"))
        pm_accent = build_drums(make_accent_ghost_spec("X"))

        normal_notes = pm_normal.instruments[0].notes
        accent_notes = pm_accent.instruments[0].notes

        self.assertEqual(len(normal_notes), 1)
        self.assertEqual(len(accent_notes), 1)
        self.assertGreater(accent_notes[0].velocity, normal_notes[0].velocity)

    def test_ghost_g_has_lower_velocity_than_normal_x(self):
        pm_normal = build_drums(make_accent_ghost_spec("x"))
        pm_ghost = build_drums(make_accent_ghost_spec("g"))

        normal_notes = pm_normal.instruments[0].notes
        ghost_notes = pm_ghost.instruments[0].notes

        self.assertEqual(len(normal_notes), 1)
        self.assertEqual(len(ghost_notes), 1)
        self.assertLess(ghost_notes[0].velocity, normal_notes[0].velocity)


if __name__ == "__main__":
    unittest.main()

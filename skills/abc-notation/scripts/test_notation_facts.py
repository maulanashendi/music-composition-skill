from __future__ import annotations

import importlib.util
import sys
import unittest
from pathlib import Path

SCRIPTS_DIR = Path(__file__).resolve().parents[0]


def _load(module_name: str, filename: str):
    module_path = SCRIPTS_DIR / filename
    spec = importlib.util.spec_from_file_location(module_name, module_path)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


nf = _load("notation_facts", "notation_facts.py")


def _abc(body: str, key: str = "Cm", voice: str = "Lead") -> str:
    return (
        "X:1\nT:t\nM:4/4\nL:1/8\nQ:1/4=120\n"
        f"K:{key}\nV:{voice}\n[V:{voice}] {body} |]\n"
    )


class NotationFactsTests(unittest.TestCase):
    def test_key_signature_makes_written_E_sound_Eb(self):
        data = nf.analyze(_abc("z C E2 A4"))["Lead"]
        names = [(n["name"], n["octave"]) for bar in data["bars"] for n in bar["notes"]]
        # rest z is NOT a pitch; C sounds C4, E sounds Eb (E-4), A sounds Ab (A-4)
        self.assertEqual(names, [("C", 4), ("E-", 4), ("A-", 4)])

    def test_intervals_are_plus3_then_plus5(self):
        data = nf.analyze(_abc("z C E2 A4"))["Lead"]
        semis = [iv["semitones"] for iv in data["intervals"]]
        dirs = [iv["direction"] for iv in data["intervals"]]
        self.assertEqual(semis, [3, 5])          # minor 3rd up, then perfect 4th up
        self.assertEqual(dirs, ["naik", "naik"])
        self.assertIn("Third", data["intervals"][0]["name"])
        self.assertIn("Fourth", data["intervals"][1]["name"])

    def test_ebmaj7_notes_are_all_chord_tones(self):
        # written e/g/b under K:Cm sound Eb/G/Bb -- all chord tones of Ebmaj7
        data = nf.analyze(_abc('"Ebmaj7" z e g2 b4'))["Lead"]
        classes = [n["cls"] for bar in data["bars"] for n in bar["notes"]]
        self.assertTrue(classes)
        self.assertTrue(all(c == "chord-tone" for c in classes), classes)

    def test_abmaj7_and_ebmaj7_are_diatonic_in_Cm(self):
        data = nf.analyze(_abc('"Abmaj7" A,2C2E2G2 | "Ebmaj7" E,2G,2B,2D2', voice="Keys"), voice="Keys")["Keys"]
        verdicts = [bar["chord_vs_key"] for bar in data["bars"] if bar["chord"]]
        self.assertEqual(verdicts, ["diatonik", "diatonik"])

    def test_voicing_top_note_is_G(self):
        # [A,CEG] = A3,C4,E4,G4 -> highest sounding pitch is G (see plan note on [ACEG])
        data = nf.analyze(_abc("[A,CEG]8", key="C", voice="Keys"), voice="Keys")["Keys"]
        self.assertEqual(data["bars"][0]["top_note"], "G")

    def test_unknown_chord_symbol_is_unparsed_no_crash(self):
        self.assertIsNone(nf.parse_chord_symbol("Wackadoo"))
        data = nf.analyze(_abc('"Wackadoo" C2 E2 G2 z2', key="C"))["Lead"]
        self.assertIsNone(data["bars"][0]["chord_pcs"])
        classes = [n["cls"] for bar in data["bars"] for n in bar["notes"]]
        self.assertTrue(all(c == "unparsed" for c in classes), classes)

    def test_multi_bar_notes_land_in_the_correct_bar(self):
        # Two whole-bar rests followed by a note reproduces a real bug found
        # via the CLI smoke test on runs/2026-07-14-doubt-to-acceptance/song.abc:
        # music21's ABC importer gives each element's .offset relative to its
        # own Measure (always 0.0 for a whole-bar rest), so bucketing bars by
        # `el.offset // bar_ql` via s.recurse() silently collapsed every bar
        # into "bar 1". s.flatten() restores absolute offsets across bars.
        abc = (
            "X:1\nT:t\nM:4/4\nL:1/8\nQ:1/4=120\nK:C\nV:Lead\n"
            '[V:Lead] "Cm9" z8 | "Cm9" z8 | "Cm9" C8 |]\n'
        )
        data = nf.analyze(abc)["Lead"]
        self.assertEqual(len(data["bars"]), 3)
        self.assertEqual(data["bars"][0]["notes"], [])
        self.assertEqual(data["bars"][1]["notes"], [])
        self.assertEqual([n["name"] for n in data["bars"][2]["notes"]], ["C"])


if __name__ == "__main__":
    unittest.main()

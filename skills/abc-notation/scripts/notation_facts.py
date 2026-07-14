#!/usr/bin/env python3
"""Report objective facts about the pitches actually written in an ABC file.

This is a FACT GENERATOR, not a claim checker: it reports the notes that
actually sound (after the key signature), the intervals between them, how each
note relates to the bar's chord symbol, the top note of each voicing, and how
each chord relates to the key. The skill instructions (Level 3/4/7 DoD) are
what compare these facts against the prose claims in an artifact.

Pitch parsing reuses abc_to_midi.py's music21 path (split_voices +
music21.converter.parse) rather than a second hand-written ABC parser. Chord
symbols are extracted from the raw ABC text (music21 silently drops unknown
symbols on parse) and classified by a minimal chord parser built on
music21.harmony.ChordSymbol.
"""
from __future__ import annotations

import argparse
import importlib.util as _ilu
import re
import sys
from pathlib import Path

from music21 import converter, harmony, note, chord, key, interval

# --- reuse abc_to_midi.py's voice splitting (single ABC parsing path) ---
_ABC_PATH = (
    Path(__file__).resolve().parents[2]
    / "midi-orchestration" / "scripts" / "abc_to_midi.py"
)
_spec = _ilu.spec_from_file_location("abc_to_midi", _ABC_PATH)
abcmod = _ilu.module_from_spec(_spec)
sys.modules["abc_to_midi"] = abcmod
_spec.loader.exec_module(abcmod)

# --- chord-symbol normalization + minimal parser ---
_FLAT_ROOT_RE = re.compile(r"\b([A-G])b")
_FLAT_BASS_RE = re.compile(r"/([A-G])b")
_ALT_RE = re.compile(r"(?:7)?alt")


def normalize_chord_symbol(sym: str) -> str:
    """ABC/pop chord spelling -> music21 ChordSymbol spelling.

    'Eb'/'Ab'/'Bb' (root or slash bass) -> 'E-'/'A-'/'B-'; '7alt'/'alt' ->
    '7b9#5' (music21 has no 'alt' abbreviation).
    """
    sym = _FLAT_ROOT_RE.sub(r"\1-", sym)
    sym = _FLAT_BASS_RE.sub(r"/\1-", sym)
    sym = _ALT_RE.sub("7b9#5", sym)
    return sym


def parse_chord_symbol(sym: str):
    """Return the chord's pitch-class names, or None if the symbol is unknown.

    Never raises: an unrecognized/eXotic/typo'd symbol yields None ('unparsed').
    """
    try:
        cs = harmony.ChordSymbol(normalize_chord_symbol(sym))
        return [p.name for p in cs.pitches]
    except Exception:
        return None


def extract_bar_chords(body: str):
    """Chord-symbol strings per written bar, split on barlines.

    Only quoted tokens starting with A-G are treated as chord symbols;
    text-placement annotations ('^text', etc.) are ignored. Repeats are NOT
    expanded -- these are facts about the written notation.
    """
    bars = []
    for seg in re.split(r"\|", body):
        seg = seg.strip().strip(":").strip("]").strip("[")
        if seg == "":
            continue
        chords = [q for q in re.findall(r'"([^"]*)"', seg) if re.match(r"^[A-G]", q)]
        bars.append(chords)
    return bars


def _scale_pcs(k):
    return set(p.name for p in k.pitches) if k else set()


def classify_note(pc_name, chord_pcs, scale_pcs):
    if chord_pcs is None:
        return "unparsed"
    if pc_name in chord_pcs:
        return "chord-tone"
    if scale_pcs and pc_name in scale_pcs:
        return "tension-diatonik"
    return "outside"


def chord_vs_key(chord_pcs, scale_pcs):
    if chord_pcs is None:
        return "unparsed"
    if not scale_pcs:
        return "unknown-key"
    if all(pc in scale_pcs for pc in chord_pcs):
        return "diatonik"
    if chord_pcs[0] in scale_pcs:
        return "borrowed"
    return "luar-key"


def _interval_fact(p1, p2):
    iv = interval.Interval(noteStart=note.Note(p1), noteEnd=note.Note(p2))
    semi = iv.semitones
    direction = "naik" if semi > 0 else ("turun" if semi < 0 else "unison")
    return {"semitones": semi, "name": iv.niceName, "direction": direction}


def analyze(abc_text: str, voice: str | None = None) -> dict:
    lines = abc_text.splitlines()
    header, _vnames, body = abcmod.split_voices(lines)
    result: dict = {}
    target_voices = [voice] if voice else list(body.keys())
    for vid in target_voices:
        if vid not in body:
            continue
        joined = " ".join(body[vid])
        stub = "\n".join(header) + f"\nV:{vid}\n" + joined
        s = converter.parse(stub, format="abc")

        k = next(iter(s.recurse().getElementsByClass(key.Key)), None)
        scale_pcs = _scale_pcs(k)
        ts = next(iter(s.recurse().getElementsByClass("TimeSignature")), None)
        bar_ql = float(ts.barDuration.quarterLength) if ts else 4.0
        bar_chords = extract_bar_chords(joined)

        # NOTE: must use s.flatten(), not s.recurse() -- .offset on a recursed
        # element is relative to its immediate parent Measure (always 0.0 for
        # a whole-bar rest), which silently collapses every bar into "bar 1"
        # for any ABC with >1 measure. flatten() restores absolute offsets.
        elems = [(int(float(el.offset) // bar_ql), el) for el in s.flatten().notesAndRests]
        max_bar = max((b for b, _ in elems), default=-1)

        notes_seq = []      # ordered Pitch objects for melodic intervals
        bars_report = []
        note_count = rest_count = 0
        durations = []
        for b in range(max_bar + 1):
            chords_here = bar_chords[b] if b < len(bar_chords) else []
            sym = chords_here[0] if chords_here else None
            chord_pcs = parse_chord_symbol(sym) if sym else None
            bar_notes = []
            top = None
            for bar_idx, el in elems:
                if bar_idx != b:
                    continue
                if isinstance(el, note.Rest):
                    rest_count += 1
                    durations.append(float(el.quarterLength))
                    continue
                if isinstance(el, harmony.ChordSymbol):
                    continue
                if isinstance(el, chord.Chord):
                    ps = sorted(el.pitches, key=lambda p: p.midi)
                    top = ps[-1].name
                    for p in ps:
                        note_count += 1
                        durations.append(float(el.quarterLength))
                        bar_notes.append({
                            "name": p.name, "octave": p.octave, "midi": p.midi,
                            "cls": classify_note(p.name, chord_pcs, scale_pcs),
                            "in_chord": True,
                        })
                        notes_seq.append(p)
                elif isinstance(el, note.Note):
                    note_count += 1
                    durations.append(float(el.quarterLength))
                    bar_notes.append({
                        "name": el.pitch.name, "octave": el.pitch.octave,
                        "midi": el.pitch.midi,
                        "cls": classify_note(el.pitch.name, chord_pcs, scale_pcs),
                        "in_chord": False,
                    })
                    notes_seq.append(el.pitch)
            bars_report.append({
                "bar": b + 1, "chord": sym, "chord_pcs": chord_pcs,
                "chord_vs_key": chord_vs_key(chord_pcs, scale_pcs) if sym else None,
                "notes": bar_notes, "top_note": top,
            })

        intervals = [
            _interval_fact(notes_seq[i], notes_seq[i + 1])
            for i in range(len(notes_seq) - 1)
        ]
        total = note_count + rest_count
        result[vid] = {
            "key": str(k) if k else None,
            "bars": bars_report,
            "intervals": intervals,
            "summary": {
                "notes": note_count, "rests": rest_count,
                "rest_ratio": round(rest_count / total, 3) if total else 0,
                "shortest_ql": min(durations) if durations else None,
                "longest_ql": max(durations) if durations else None,
            },
        }
    return result


def format_report(analysis: dict) -> str:
    out = []
    for vid, data in analysis.items():
        out.append(f"# Voice: {vid}")
        out.append(f"Key: {data['key']}")
        s = data["summary"]
        out.append(
            f"Notes: {s['notes']}  Rests: {s['rests']}  Rest-ratio: {s['rest_ratio']}  "
            f"Shortest(ql): {s['shortest_ql']}  Longest(ql): {s['longest_ql']}"
        )
        out.append("")
        for bar in data["bars"]:
            out.append(
                f"## Bar {bar['bar']}  chord={bar['chord']}  "
                f"chord-vs-key={bar['chord_vs_key']}  top-note={bar['top_note']}"
            )
            if bar["chord_pcs"]:
                out.append(f"   chord tones: {', '.join(bar['chord_pcs'])}")
            elif bar["chord"]:
                out.append("   chord tones: UNPARSED (simbol tak dikenal)")
            for n in bar["notes"]:
                out.append(f"   {n['name']}{n['octave']} (midi {n['midi']}) -> {n['cls']}")
        out.append("")
        out.append("Intervals (nada melodi berurutan):")
        for iv in data["intervals"]:
            sign = "+" if iv["semitones"] > 0 else ""
            out.append(f"   {sign}{iv['semitones']} {iv['name']} {iv['direction']}")
        out.append("")
    return "\n".join(out)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("abc_file", type=Path)
    parser.add_argument("--voice", default=None, help="voice id to analyze (default: all)")
    args = parser.parse_args()
    text = args.abc_file.read_text(encoding="utf-8")
    print(format_report(analyze(text, args.voice)))
    return 0


if __name__ == "__main__":
    sys.exit(main())

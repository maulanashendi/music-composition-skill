#!/usr/bin/env python3
"""Convert a drum step-grid JSON into a MIDI drum track (GM channel 10).

Applies swing (delay off-beat 16th steps), per-role phrase velocity, a small
final velocity humanization, and deterministic per-role timing offsets for a
natural lofi/funk feel. Output is a single-track MIDI on the drum channel,
ready to merge with the pitched MIDI rendered from ABC.

Grid v2 (backward compatible with v1):
- section.pattern may be a dict (legacy: tiled identically across every bar of
  the section) or a list of dicts (one pattern per bar; the list length MUST
  equal section["bars"]).
- section.phrase_velocity (optional): list of float multipliers, one per bar
  (length must equal section["bars"]), applied to every hit's velocity in that
  bar after accent/ghost. Absent -> 1.0 for every bar (no-op, identical to v1).
- top-level "timing" (optional): map role -> offset in milliseconds, added
  deterministically to each onset of that role (clamped so onset >= 0). Absent
  -> no per-role offset (identical to v1).

Velocity order: base -> accent X / ghost g -> phrase_velocity -> humanize.
"""
import json
import random
import sys
import pretty_midi


def _resolve_bar_patterns(section):
    """Return a list of per-bar pattern dicts for a section.

    Legacy dict -> tiled identically across all bars. New list -> returned
    as-is, but its length must match section["bars"] exactly (no silent
    truncate/pad).
    """
    pattern = section["pattern"]
    bars = section["bars"]
    if isinstance(pattern, list):
        if len(pattern) != bars:
            raise ValueError(
                f"section pattern list has {len(pattern)} bars but section['bars'] "
                f"is {bars}; per-bar pattern lists must match the bar count exactly"
            )
        return pattern
    return [pattern] * bars


def lint_sections(spec):
    """Warn (not error) when a section > 2 bars has every bar identical.

    Applies to both pattern forms: a legacy dict is identical-by-tiling, and a
    list whose entries are all equal. Purely informational -- does not change
    the rendered MIDI.
    """
    warnings = []
    for idx, section in enumerate(spec["sections"]):
        bars = section["bars"]
        if bars <= 2:
            continue
        patterns = _resolve_bar_patterns(section)
        first = patterns[0]
        if all(p == first for p in patterns):
            label = section.get("label", f"section {idx}")
            warnings.append(
                f"section {idx} ({label!r}) has {bars} bars but every bar is "
                "identical; add a 2-bar base + variation + transition per "
                "level-09-drum.md"
            )
    return warnings


def build_drums(spec_path: str, out_path: str, seed: int = 7):
    random.seed(seed)
    spec = json.load(open(spec_path))

    tempo = spec["tempo_bpm"]
    spb = spec["steps_per_bar"]
    swing = spec.get("swing", 0.5)          # 0.5 = straight; >0.5 pushes off-beats late
    hum = spec.get("humanize_velocity", 0)
    gm = spec["gm_map"]
    basevel = spec["base_velocity"]
    timing = spec.get("timing", {})         # role -> ms offset (deterministic)

    sec_per_beat = 60.0 / tempo
    # Bar length in quarter-note-equivalents: 4 for 4/4, 3.5 for 7/8 (at eighth-
    # note subdivision), 3 for 3/4, etc. -- numerator * 4/denominator. Defaults
    # to 4 so every existing 4/4 spec that doesn't set this field is unaffected.
    beats_per_bar = spec.get("beats_per_bar", 4)
    sec_per_bar = sec_per_beat * beats_per_bar
    sec_per_step = sec_per_bar / spb

    warnings = lint_sections(spec)
    for w in warnings:
        print(f"WARNING: {w}", file=sys.stderr)

    pm = pretty_midi.PrettyMIDI(initial_tempo=tempo)
    drum = pretty_midi.Instrument(program=0, is_drum=True, name="Drums")

    bar_cursor = 0
    for section in spec["sections"]:
        patterns = _resolve_bar_patterns(section)
        phrase = section.get("phrase_velocity")
        if phrase is not None and len(phrase) != section["bars"]:
            raise ValueError(
                f"phrase_velocity has {len(phrase)} entries but section['bars'] "
                f"is {section['bars']}; they must match"
            )
        for bar_index in range(section["bars"]):
            bar_start = bar_cursor * sec_per_bar
            pat = patterns[bar_index]
            pmult = phrase[bar_index] if phrase is not None else 1.0
            for voice, row in pat.items():
                note = gm[voice]
                bv = basevel[voice]
                for i, ch in enumerate(row):
                    if ch == "x":
                        hit_vel = bv
                    elif ch == "X":
                        hit_vel = bv * 1.2  # accent: ~+20% of normal
                    elif ch == "g":
                        hit_vel = bv * 0.45  # ghost: ~45% of normal
                    else:
                        continue
                    hit_vel *= pmult  # phrase-shaped velocity (directional, not jitter)
                    t = bar_start + i * sec_per_step
                    # swing: push the second 16th of each 8th-note pair later
                    if i % 2 == 1:
                        t += (swing - 0.5) * 2 * sec_per_step
                    # deterministic per-role timing offset; clamp onset >= 0
                    t = max(0.0, t + timing.get(voice, 0) / 1000.0)
                    vel = max(1, min(127, round(hit_vel) + random.randint(-hum, hum)))
                    drum.notes.append(pretty_midi.Note(
                        velocity=vel, pitch=note,
                        start=t, end=t + sec_per_step * 0.9))
            bar_cursor += 1

    pm.instruments.append(drum)
    pm.write(out_path)
    total = len(drum.notes)
    print(f"wrote {out_path}: {total} drum hits across {bar_cursor} bars")
    return warnings


if __name__ == "__main__":
    spec = sys.argv[1] if len(sys.argv) > 1 else "backstep_drums.json"
    out = sys.argv[2] if len(sys.argv) > 2 else "backstep_drums.mid"
    build_drums(spec, out)

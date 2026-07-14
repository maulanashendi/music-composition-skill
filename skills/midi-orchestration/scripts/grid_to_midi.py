#!/usr/bin/env python3
"""Convert a drum step-grid JSON into a MIDI drum track (GM channel 10).

Applies swing (delay off-beat 16th steps) and velocity humanization for a
natural lofi/funk feel. Output is a single-track MIDI on the drum channel,
ready to merge with the pitched MIDI rendered from ABC.
"""
import json
import random
import sys
import pretty_midi


def build_drums(spec_path: str, out_path: str, seed: int = 7):
    random.seed(seed)
    spec = json.load(open(spec_path))

    tempo = spec["tempo_bpm"]
    spb = spec["steps_per_bar"]
    swing = spec.get("swing", 0.5)          # 0.5 = straight; >0.5 pushes off-beats late
    hum = spec.get("humanize_velocity", 0)
    gm = spec["gm_map"]
    basevel = spec["base_velocity"]

    sec_per_beat = 60.0 / tempo
    # Bar length in quarter-note-equivalents: 4 for 4/4, 3.5 for 7/8 (at eighth-
    # note subdivision), 3 for 3/4, etc. -- numerator * 4/denominator. Defaults
    # to 4 so every existing 4/4 spec that doesn't set this field is unaffected.
    beats_per_bar = spec.get("beats_per_bar", 4)
    sec_per_bar = sec_per_beat * beats_per_bar
    sec_per_step = sec_per_bar / spb

    pm = pretty_midi.PrettyMIDI(initial_tempo=tempo)
    drum = pretty_midi.Instrument(program=0, is_drum=True, name="Drums")

    bar_cursor = 0
    for section in spec["sections"]:
        for _ in range(section["bars"]):
            bar_start = bar_cursor * sec_per_bar
            for voice, row in section["pattern"].items():
                note = gm[voice]
                bv = basevel[voice]
                for i, ch in enumerate(row):
                    if ch != "x":
                        continue
                    t = bar_start + i * sec_per_step
                    # swing: push the second 16th of each 8th-note pair later
                    if i % 2 == 1:
                        t += (swing - 0.5) * 2 * sec_per_step
                    vel = max(1, min(127, bv + random.randint(-hum, hum)))
                    drum.notes.append(pretty_midi.Note(
                        velocity=vel, pitch=note,
                        start=t, end=t + sec_per_step * 0.9))
            bar_cursor += 1

    pm.instruments.append(drum)
    pm.write(out_path)
    total = len(drum.notes)
    print(f"wrote {out_path}: {total} drum hits across {bar_cursor} bars")


if __name__ == "__main__":
    spec = sys.argv[1] if len(sys.argv) > 1 else "backstep_drums.json"
    out = sys.argv[2] if len(sys.argv) > 2 else "backstep_drums.mid"
    build_drums(spec, out)

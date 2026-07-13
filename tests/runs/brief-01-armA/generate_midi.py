#!/usr/bin/env python3
"""
From-scratch MIDI generator for "Settling In" (baseline draft, no specialized
tooling). Encodes, by hand, the same bar-by-bar note data as song.abc (Lead,
Rhodes, Bass) plus the drum grooves described in drums.json, at 78 BPM / 4/4,
20 bars. Adds light, deterministic humanization (micro-timing + a per-section
dynamic arc) to avoid a completely robotic/quantized feel. Uses only
pretty_midi (a generic library available in the eval venv), no specialized
composition tooling.

Run with the venv python, e.g.:
    .venv-eval/bin/python3 generate_midi.py
"""
import json
import os
import pretty_midi

HERE = os.path.dirname(os.path.abspath(__file__))

TEMPO_BPM = 78
SEC_PER_BEAT = 60.0 / TEMPO_BPM
SEC_PER_16TH = SEC_PER_BEAT / 4.0
BEATS_PER_BAR = 4
N_BARS = 20

# ---------------------------------------------------------------------------
# Pitched voice data: one list per bar of (offset_in_beats, duration_in_beats,
# pitch_or_None) tuples. Matches song.abc bar-for-bar (hand cross-checked).
# ---------------------------------------------------------------------------

lead_bars = [
    [(0, 1, None), (1, 1, 75), (2, 1, 72), (3, 1, None)],          # b1  Cm7
    [(0, 1, None), (1, 1, 79), (2, 1, 75), (3, 1, 72)],            # b2  Cm7
    [(0, 1, None), (1, 1, 80), (2, 1, 77), (3, 1, None)],          # b3  Fm7
    [(0, 1, 72), (1, 1, 58), (2, 2, None)],                        # b4  Fm7
    [(0, 1, None), (1, 1, 77), (2, 1, 80), (3, 1, None)],          # b5  Dm7b5
    [(0, 1, None), (1, 1, 71), (2, 1, 80), (3, 1, 79)],            # b6  G7b9
    [(0, 1, None), (1, 1, 75), (2, 1, 72), (3, 1, None)],          # b7  Cm7
    [(0, 1, 80), (1, 1, 79), (2, 1, 75), (3, 1, None)],            # b8  Abmaj7
    [(0, 1, 77), (1, 1, 79), (2, 1, 80), (3, 1, 84)],              # b9  Fm7
    [(0, 1, 84), (1, 1, 80), (2, 1, 79), (3, 1, None)],            # b10 Bb7
    [(0, 1, 79), (1, 1, 77), (2, 1, 75), (3, 1, None)],            # b11 Ebmaj7
    [(0, 1, 80), (1, 1, 79), (2, 1, 77), (3, 1, None)],            # b12 Abmaj7
    [(0, 1, None), (1, 1, 77), (2, 1, 80), (3, 1, None)],          # b13 Dm7b5
    [(0, 2, None), (2, 1, 71), (3, 1, 72)],                        # b14 G7
    [(0, 1, 72), (1, 1, None), (2, 1, 75), (3, 1, None)],          # b15 Cm7
    [(0, 2, None), (2, 1, 75), (3, 1, None)],                      # b16 Cm7/Eb
    [(0, 1, None), (1, 2, 77), (3, 1, None)],                      # b17 Fm7
    [(0, 1, None), (1, 2, 75), (3, 1, None)],                      # b18 Abmaj7
    [(0, 1, 74), (1, 2, 72), (3, 1, None)],                        # b19 Fm7
    [(0, 4, 75)],                                                  # b20 Cm(add9)
]

rhodes_bars = [
    [63, 67, 70, 74],  # b1  Cm9 shell
    [63, 67, 70, 74],  # b2
    [68, 72, 75, 79],  # b3  Fm9 shell
    [68, 72, 75, 79],  # b4
    [65, 68, 72],       # b5  Dm7b5 shell (3-b5-b7)
    [71, 77, 80],       # b6  G7b9 shell (3-b7-b9)
    [63, 67, 70, 74],  # b7
    [72, 75, 79],       # b8  Abmaj7 shell (3-5-7)
    [68, 72, 75, 79],  # b9
    [62, 68, 72],       # b10 Bb7 shell (3-b7-9)
    [67, 70, 74],       # b11 Ebmaj7 shell (3-5-7)
    [72, 75, 79],       # b12
    [65, 68, 72],       # b13
    [71, 74, 77],       # b14 G7 shell, no b9 this time
    [63, 67, 70, 74],  # b15
    [63, 67, 70, 74],  # b16 (Cm7/Eb, bass carries inversion)
    [68, 72, 75, 79],  # b17
    [72, 75, 79],       # b18
    [68, 72, 75, 79],  # b19
    [60, 63, 67, 74],  # b20 Cm(add9)
]

bass_bars = [
    [(0, 2, 48), (2, 1, 51), (3, 1, 55)],   # b1
    [(0, 2, 48), (2, 2, None)],             # b2
    [(0, 2, 53), (2, 1, 56), (3, 1, 60)],   # b3
    [(0, 2, 53), (2, 2, None)],             # b4
    [(0, 2, 50), (2, 1, 53), (3, 1, 56)],   # b5
    [(0, 2, 55), (2, 1, 59), (3, 1, 53)],   # b6
    [(0, 2, 48), (2, 1, 51), (3, 1, 55)],   # b7
    [(0, 2, 56), (2, 1, 60), (3, 1, 63)],   # b8
    [(0, 2, 53), (2, 1, 56), (3, 1, 60)],   # b9
    [(0, 2, 58), (2, 1, 62), (3, 1, 65)],   # b10
    [(0, 2, 51), (2, 1, 55), (3, 1, 58)],   # b11
    [(0, 2, 56), (2, 1, 60), (3, 1, 63)],   # b12
    [(0, 2, 50), (2, 1, 53), (3, 1, 56)],   # b13
    [(0, 2, 55), (2, 1, 59), (3, 1, 62)],   # b14
    [(0, 2, 48), (2, 2, None)],             # b15
    [(0, 2, 51), (2, 2, None)],             # b16
    [(0, 2, 53), (2, 2, None)],             # b17
    [(0, 2, 56), (2, 2, None)],             # b18
    [(0, 2, 53), (2, 2, None)],             # b19
    [(0, 4, 48)],                           # b20
]

assert len(lead_bars) == N_BARS and len(rhodes_bars) == N_BARS and len(bass_bars) == N_BARS
for name, bars in (("lead", lead_bars), ("bass", bass_bars)):
    for i, b in enumerate(bars, 1):
        total = sum(d for (_, d, _) in b)
        assert total == BEATS_PER_BAR, f"{name} bar {i} sums to {total} beats, expected {BEATS_PER_BAR}"


def bar_dynamic_delta(bar_1indexed):
    """Per-section dynamic arc: quieter at the start (self-doubt), a bit more
    present in section B (searching), softer again through the outro
    (settling), quietest of all on the final held chord."""
    if bar_1indexed <= 8:
        return -8
    if bar_1indexed <= 12:
        return +5
    if bar_1indexed <= 14:
        return 0
    if bar_1indexed <= 16:
        return -5
    if bar_1indexed <= 19:
        return -12
    return -18  # bar 20


def humanize_pitched_offset(offset_in_bar_beats):
    """Small laid-back push for anything not landing on beat 1 of the bar."""
    if offset_in_bar_beats == 0:
        return 0.0
    return 0.03 * SEC_PER_BEAT


def clamp_vel(v):
    return max(1, min(120, int(round(v))))


pm = pretty_midi.PrettyMIDI(initial_tempo=TEMPO_BPM)

lead_inst = pretty_midi.Instrument(program=65, name="Lead (Alto Sax)")     # GM Alto Sax
rhodes_inst = pretty_midi.Instrument(program=4, name="Rhodes")            # GM Electric Piano 1
bass_inst = pretty_midi.Instrument(program=33, name="Bass (Fingered)")     # GM Electric Bass (finger)
drum_inst = pretty_midi.Instrument(program=0, is_drum=True, name="Drums")

LEAD_BASE_VEL = 78
RHODES_BASE_VEL = 60
BASS_BASE_VEL = 74

for bar_idx in range(N_BARS):
    bar_1 = bar_idx + 1
    bar_start_beat = bar_idx * BEATS_PER_BAR
    dyn = bar_dynamic_delta(bar_1)

    # --- Lead ---
    for offset, dur, pitch in lead_bars[bar_idx]:
        if pitch is None:
            continue
        start = (bar_start_beat + offset) * SEC_PER_BEAT + humanize_pitched_offset(offset)
        extra = 1.6 if bar_1 == N_BARS else 0.0  # let the final note ring a bit past the bar
        end = (bar_start_beat + offset + dur) * SEC_PER_BEAT + extra
        vel = clamp_vel(LEAD_BASE_VEL + dyn)
        lead_inst.notes.append(pretty_midi.Note(velocity=vel, pitch=pitch, start=start, end=end))

    # --- Rhodes (one chord per bar) ---
    chord = rhodes_bars[bar_idx]
    start = bar_start_beat * SEC_PER_BEAT
    extra = 1.6 if bar_1 == N_BARS else 0.0
    end = (bar_start_beat + BEATS_PER_BAR) * SEC_PER_BEAT + extra
    for pitch in chord:
        vel = clamp_vel(RHODES_BASE_VEL + dyn)
        rhodes_inst.notes.append(pretty_midi.Note(velocity=vel, pitch=pitch, start=start, end=end))

    # --- Bass ---
    for offset, dur, pitch in bass_bars[bar_idx]:
        if pitch is None:
            continue
        start = (bar_start_beat + offset) * SEC_PER_BEAT + humanize_pitched_offset(offset)
        extra = 1.6 if bar_1 == N_BARS else 0.0
        end = (bar_start_beat + offset + dur) * SEC_PER_BEAT + extra
        vel = clamp_vel(BASS_BASE_VEL + dyn)
        bass_inst.notes.append(pretty_midi.Note(velocity=vel, pitch=pitch, start=start, end=end))

# ---------------------------------------------------------------------------
# Drums: read the pattern from drums.json, apply it per bar via bar_map, with
# a bit of swing/laid-back micro-timing on off-grid 16th steps.
# ---------------------------------------------------------------------------

with open(os.path.join(HERE, "drums.json")) as f:
    drum_data = json.load(f)

gm_notes = drum_data["gm_drum_notes"]
grooves = drum_data["grooves"]
bar_map = drum_data["bar_map"]


def step_humanize_delay(step):
    """Laid-back swing: notes on the beat are on-grid, 8th 'ands' get a small
    push, 16th 'e'/'a' subdivisions get a slightly bigger push."""
    pos_in_beat = step % 4
    if pos_in_beat == 0:
        return 0.0
    if pos_in_beat == 2:
        return 0.15 * SEC_PER_16TH
    return 0.25 * SEC_PER_16TH


for bar_idx in range(N_BARS):
    bar_1 = bar_idx + 1
    bar_start_beat = bar_idx * BEATS_PER_BAR
    groove_name = bar_map[str(bar_1)]
    groove = grooves[groove_name]
    for inst_name, hits in groove.items():
        if inst_name.startswith("_"):
            continue
        note_num = gm_notes[inst_name]
        for hit in hits:
            step = hit["step"]
            vel = hit["vel"]
            extra_drag = 0.3 * SEC_PER_16TH if inst_name == "ghost_snare" else 0.0
            start = (bar_start_beat * SEC_PER_BEAT
                      + step * SEC_PER_16TH
                      + step_humanize_delay(step)
                      + extra_drag)
            end = start + 0.12  # short drum hit
            drum_inst.notes.append(pretty_midi.Note(velocity=vel, pitch=note_num, start=start, end=end))

pm.instruments.append(lead_inst)
pm.instruments.append(rhodes_inst)
pm.instruments.append(bass_inst)
pm.instruments.append(drum_inst)

out_path = os.path.join(HERE, "song.mid")
pm.write(out_path)
print(f"Wrote {out_path}")
print(f"Total duration: {pm.get_end_time():.2f}s across {len(pm.instruments)} instruments")
for inst in pm.instruments:
    print(f"  {inst.name}: {len(inst.notes)} notes")

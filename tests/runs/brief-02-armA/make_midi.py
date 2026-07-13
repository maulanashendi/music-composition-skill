#!/usr/bin/env python3
"""
Build song.mid for "Restless Seven" from scratch.

Approach (written from scratch for this baseline test, no project-specific
tooling): parse the hand-written song.abc with music21 to get exact Lead and
Bass note events (pitch + timing), then programmatically generate a Keys
comping track and a Drums track from an explicit per-bar chord/event table
that mirrors notes.md / drums.md, and merge everything into one multi-track
MIDI file with pretty_midi.

Tempo: ABC says Q:1/8=160 (eighth note = 160 bpm) -> quarter note = 80 bpm.
Bar = 7 eighths = 2.625 seconds at this tempo.
"""

import music21 as m21
import pretty_midi as pm

ABC_PATH = "song.abc"
OUT_PATH = "song.mid"

SEC_PER_QUARTER = 60.0 / 80.0   # quarter = 80 bpm  (== eighth = 160 bpm)
SEC_PER_EIGHTH = SEC_PER_QUARTER / 2.0
BAR_SEC = 7 * SEC_PER_EIGHTH    # 2.625s
N_BARS = 20

# ---------------------------------------------------------------------------
# 1. Lead + Bass from the hand-written ABC (ground truth for pitched parts)
# ---------------------------------------------------------------------------

score = m21.converter.parse(ABC_PATH)

real_parts = [p for p in score.parts if p.duration.quarterLength > 0]
if len(real_parts) != 2:
    raise RuntimeError(f"expected 2 non-empty parts, got {len(real_parts)}")

# distinguish by average pitch (lead sits higher than bass)
def avg_pitch(part):
    ps = [n.pitch.midi for n in part.flatten().notes if n.isNote]
    return sum(ps) / len(ps)

real_parts.sort(key=avg_pitch, reverse=True)
lead_part, bass_part = real_parts

midi = pm.PrettyMIDI(initial_tempo=80.0)
midi.time_signature_changes.append(pm.TimeSignature(7, 8, 0.0))

lead_inst = pm.Instrument(program=66, name="Lead (Tenor Sax)")   # GM 67, 1-idx
bass_inst = pm.Instrument(program=35, name="Bass (Fretless)")    # GM 36, 1-idx

CLIMAX_START_Q = 56.0  # bar 17 starts at quarterLength offset 56 (see parse dump)

for n in lead_part.flatten().notes:
    if not n.isNote:
        continue
    start = float(n.offset) * SEC_PER_QUARTER
    end = start + float(n.quarterLength) * SEC_PER_QUARTER
    vel = 100 if float(n.offset) >= CLIMAX_START_Q else 92
    lead_inst.notes.append(pm.Note(velocity=vel, pitch=n.pitch.midi, start=start, end=end))

for n in bass_part.flatten().notes:
    if not n.isNote:
        continue
    start = float(n.offset) * SEC_PER_QUARTER
    end = start + float(n.quarterLength) * SEC_PER_QUARTER
    vel = 105 if float(n.offset) >= CLIMAX_START_Q else 98
    bass_inst.notes.append(pm.Note(velocity=vel, pitch=n.pitch.midi, start=start, end=end))

# ---------------------------------------------------------------------------
# 2. Keys comping — programmatic, from the same chord chart as song.abc
# ---------------------------------------------------------------------------

CHORD_PER_BAR = [
    "Dm7", "Dm7", "Ebmaj7#11", "Dm7",
    "Dm7", "Ebmaj7#11", "Dm7", "C7#9",
    "Bbmaj7#11", "A7alt", "Dm7", "Ebmaj7#11",
    "Em7b5", "A7alt", "Fmaj7#11", "G7#9",
    "D", "Gmaj7#11", "Bm7", "Dmaj7#11",
]
assert len(CHORD_PER_BAR) == N_BARS

VOICINGS = {
    "Dm7":          [62, 65, 69, 72],
    "Ebmaj7#11":    [63, 67, 70, 74, 81],
    "C7#9":         [60, 64, 67, 70, 75],
    "Bbmaj7#11":    [58, 62, 65, 69, 76],
    "A7alt":        [57, 61, 64, 67, 70],
    "Em7b5":        [64, 67, 70, 74],
    "Fmaj7#11":     [65, 69, 72, 76, 83],
    "G7#9":         [55, 59, 62, 65, 70],
    "D":            [62, 66, 69, 74],
    "Gmaj7#11":     [67, 71, 74, 78, 85],
    "Bm7":          [59, 62, 66, 69],
    "Dmaj7#11":     [62, 66, 69, 73, 80],
}

keys_inst = pm.Instrument(program=4, name="Keys (Rhodes)")  # GM 5, 1-idx

for bar_idx, chord_name in enumerate(CHORD_PER_BAR, start=1):
    bar_start = (bar_idx - 1) * BAR_SEC
    voicing = VOICINGS[chord_name]
    is_climax = bar_idx >= 17
    vel = 92 if is_climax else 78
    # stab 1: slots 1-4 (4 eighths), stab 2: slots 5-7 (3 eighths)
    stab1_start = bar_start
    stab1_end = bar_start + 4 * SEC_PER_EIGHTH
    stab2_start = stab1_end
    stab2_end = bar_start + 7 * SEC_PER_EIGHTH
    for pitch in voicing:
        keys_inst.notes.append(pm.Note(velocity=vel, pitch=pitch, start=stab1_start, end=stab1_end))
        keys_inst.notes.append(pm.Note(velocity=vel - 8, pitch=pitch, start=stab2_start, end=stab2_end))

# ---------------------------------------------------------------------------
# 3. Drums — programmatic, from the per-bar event table in drums.md
# ---------------------------------------------------------------------------

KICK, SNARE, HHC, HHO, CRASH, RIDE = 36, 38, 42, 46, 49, 51
TOM_HI, TOM_MID, TOM_LO = 50, 47, 45

drum_inst = pm.Instrument(program=0, is_drum=True, name="Drums")

def hit(bar_idx, slot, note, vel):
    """slot is 1..7 (eighth-note position within the bar)."""
    bar_start = (bar_idx - 1) * BAR_SEC
    t = bar_start + (slot - 1) * SEC_PER_EIGHTH
    drum_inst.notes.append(pm.Note(velocity=vel, pitch=note, start=t, end=t + SEC_PER_EIGHTH * 0.9))

for bar_idx in range(1, N_BARS + 1):
    if 1 <= bar_idx <= 4:
        # Section 1: intro, 2+2+3, sparse
        for s in (1, 3, 5):
            hit(bar_idx, s, KICK, 105)
        hit(bar_idx, 6, SNARE, 100)
        for s in range(1, 8):
            hit(bar_idx, s, HHC, 70)
        if bar_idx == 1:
            hit(bar_idx, 1, CRASH, 110)

    elif 5 <= bar_idx <= 10:
        # Section 2: A theme, 2+2+3, restless build
        for s in (1, 3, 5):
            hit(bar_idx, s, KICK, 108)
        hit(bar_idx, 2, SNARE, 50)   # ghost
        hit(bar_idx, 6, SNARE, 102)  # accent
        for s in range(1, 8):
            v = 82 if s in (1, 3, 5) else 68
            hit(bar_idx, s, HHC, v)

    elif 11 <= bar_idx <= 16:
        # Section 3: B/development, 3+2+2, groove displaced ("unsettled")
        for s in (1, 4, 6):
            hit(bar_idx, s, KICK, 110)
        hit(bar_idx, 3, SNARE, 55)   # ghost
        hit(bar_idx, 7, SNARE, 108)  # accent, lands "wrong side" of bar
        if bar_idx != 16:
            for s in (1, 2, 3, 5, 6):
                hit(bar_idx, s, HHC, 74)
            for s in (4, 7):
                hit(bar_idx, s, HHO, 90)
        else:
            # bar 16: drop snare/hihat for a tom fill into the climax
            hit(bar_idx, 5, TOM_HI, 100)
            hit(bar_idx, 6, TOM_MID, 105)
            hit(bar_idx, 7, TOM_LO, 112)
            # (kick on 1,4 and no snare already handled above; remove the
            # bar-16 snare ghost/accent added above since the fill replaces it)
            drum_inst.notes = [nn for nn in drum_inst.notes
                                if not (nn.pitch == SNARE and
                                        abs(nn.start - ((bar_idx - 1) * BAR_SEC + 2 * SEC_PER_EIGHTH)) < 1e-6)
                                and not (nn.pitch == SNARE and
                                         abs(nn.start - ((bar_idx - 1) * BAR_SEC + 6 * SEC_PER_EIGHTH)) < 1e-6)]

    else:
        # Section 4: climax, bars 17-20, back to steady 2+2+3, released/confident
        if bar_idx != N_BARS:
            for s in (1, 3, 5):
                hit(bar_idx, s, KICK, 115)
            hit(bar_idx, 1, SNARE, 112)
            hit(bar_idx, 6, SNARE, 108)
            for s in range(1, 8):
                hit(bar_idx, s, RIDE, 95)
            if bar_idx == 17:
                hit(bar_idx, 1, CRASH, 120)
        else:
            # final bar: one big hit, then let the ride ring out
            hit(bar_idx, 1, KICK, 120)
            hit(bar_idx, 1, SNARE, 118)
            hit(bar_idx, 1, CRASH, 127)
            for s in range(2, 8):
                hit(bar_idx, s, RIDE, 90)

# ---------------------------------------------------------------------------
# 4. Assemble + write
# ---------------------------------------------------------------------------

midi.instruments.extend([lead_inst, keys_inst, bass_inst, drum_inst])
midi.write(OUT_PATH)

total_bars_sec = N_BARS * BAR_SEC
print(f"Wrote {OUT_PATH}")
print(f"Lead notes: {len(lead_inst.notes)}  Bass notes: {len(bass_inst.notes)}  "
      f"Keys notes: {len(keys_inst.notes)}  Drum hits: {len(drum_inst.notes)}")
print(f"Expected length: {total_bars_sec:.3f}s for {N_BARS} bars of 7/8 @ eighth=160bpm")

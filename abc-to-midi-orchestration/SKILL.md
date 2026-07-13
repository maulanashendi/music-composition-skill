---
name: abc-to-midi-orchestration
description: Turn a validated ABC composition into a finished multi-track MIDI ready for a DAW like BandLab — designing a bar-by-bar interaction map (who leads, who supports, who answers, who stays silent) that serves the piece's dramatic arc, handling drums as a separate step-grid, and converting everything to clean per-instrument MIDI. Use whenever someone has ABC notation (or a composition-plan.json plus ABC) and wants it rendered to MIDI, wants an arrangement built from it, asks how instruments should interact across sections, or wants a DAW-ready multi-track file with drums. Trigger on "turn this ABC into MIDI," "arrange this for full band," "make a BandLab-ready file," "who should play when," or handing over validated ABC for production.
---

# ABC to MIDI Orchestration

Take a **validated** ABC composition and produce a **DAW-ready multi-track MIDI**: one clean track per instrument, plus a drum track on channel 10. Along the way, design the **interaction map** — which instrument leads, supports, answers, or stays silent, bar by bar — so the arrangement breathes instead of everyone playing all the time.

This skill assumes the musical ideas are decided (by `jazz-idea-generator`) and the ABC is written and validated (by `abc-notation-writer`). It does not invent chords or melodies. Its job is arrangement + conversion.

## The rule that keeps arrangements from sounding cluttered

**The dramatic arc (from the composition plan) is the master; the interaction map serves it.** The map is not a chance to make everyone busy — it's how you translate the arc's emotional journey into "who plays when." A section that should feel lonely has one or two voices and lots of silence; a section that should feel full has the ensemble together. Do not add activity that doesn't serve the arc. Subtraction (dropping a voice) is as powerful as addition — often more.

## Workflow

### Step 1 — Read the plan and the arc

If a `composition-plan.json` is available, read its `arc`, `ensemble`, and per-section `phrasing`/`tension`. The arc tells you the density and interaction each section needs. If only ABC is provided, infer the sections and ask the person for the emotional shape if it isn't obvious — the interaction map is meaningless without knowing what each section should feel like.

### Step 2 — Design the interaction map (serving the arc)

Read `references/interaction-map.md`. For each section, decide per instrument: **lead / support / answer / silent**, and mark where call-and-response, subtraction, and density changes happen. Density must track the arc — sparse where the arc is quiet, full where it peaks. Produce a concrete bar-or-section table, not a vague sentence. Then apply the quality gate: does each section feel different, following the arc? Is any voice active only to fill space rather than serve the moment? If so, silence it.

The map drives how you write or adjust the ABC voices (a "silent" instrument gets rests; an "answer" instrument plays in the gaps the lead leaves) and how you shape the drum grid (drums also follow the arc — near-absent when lonely, full when warm).

### Step 3 — Prepare the pitched ABC

Ensure the ABC reflects the interaction map: silent voices have rests for those bars, answering voices play in the lead's gaps, and the density matches each section's role. If the ABC needs changes, that's an `abc-notation-writer` task — keep it validated (`validate_abc.py`) before converting. Every voice needs a `V:` header with a `name="..."` so the converter can map it to an instrument.

### Step 4 — Design the drum grid (also serving the arc)

Drums stay out of ABC (they're not pitched). Write them as a step-grid JSON — see `assets/drum-grid-template.json`. Critical: **the grid's total bars must match the ABC's total bars**, section for section, or the drums and the band drift out of sync. Build the grid section-by-section from the same plan so the bar counts line up. Let the drums follow the arc: minimal in quiet sections, full in the peak, fading at the end.

### Step 5 — Convert and merge

Read `references/midi-conversion.md` for the two bug-fixes that are mandatory (they were found by actually importing to a DAW):

1. **Strip chord symbols before rendering.** ABC chord symbols in quotes (`"Cm9"`) will otherwise be sounded as chord notes, piling up into a drone on every track. The converter removes them; never render raw.
2. **Force the lead voice monophonic.** A melody voice should be one note at a time; keep the top note if any chord slips through.

Run the converters:

```bash
python3 scripts/abc_to_midi.py <file.abc> pitched.mid      # per-voice pitched tracks
python3 scripts/grid_to_midi.py <drums.json> drums.mid      # channel-10 drum track w/ swing + humanize
```

Then merge (append the drum track to the pitched PrettyMIDI object and write once). Verify: each track's end time is roughly equal (sync check), the lead track's max polyphony is 1 (mono check), and total bars match the plan. If the lead runs long-note drones, the chord-strip step was skipped — fix and re-render.

### Step 6 — Deliver

Output the single merged `.mid`. Tell the person it imports to BandLab (or any DAW) as separate tracks they can voice, mute, or edit — the drum track lands on channel 10 so the DAW treats it as a kit. Note what serves the arc (where the subtraction is, where the peak is) so they hear the intent. Instrument sounds come from the DAW's patches; this is MIDI data, not finished audio.

## References

- `references/interaction-map.md` — how to design lead/support/answer/silent per section, call-and-response, subtraction, and density that tracks the arc; includes the quality gate.
- `references/midi-conversion.md` — how the converters work, the two mandatory bug-fixes, GM program mapping, swing/humanization, and the sync/mono verification checks.
- `scripts/abc_to_midi.py` — multi-voice ABC → per-track MIDI (strips chord symbols, forces mono lead).
- `scripts/grid_to_midi.py` — drum step-grid → channel-10 MIDI with swing and velocity humanization.
- `assets/drum-grid-template.json` — starting point for a drum grid; match its bar counts to the ABC.

## Dependencies

Requires `music21` and `pretty_midi` (`pip install music21 pretty_midi`). Both are pure-Python and install from PyPI.

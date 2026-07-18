---
name: midi-orchestration
description: Design a bar-by-bar interaction map (who leads, who supports, who answers, who stays silent) that serves the piece's dramatic arc, and realize it as a finished multi-track composition JSON — drums as a `role:"drums"` voice — ready for the `daw_generative` render engine. ABC→MIDI conversion (drums as a separate step-grid, per-instrument MIDI tracks for BandLab or any DAW) is supported as a legacy path. Use whenever someone has a decided composition (JSON or ABC) and wants an arrangement built from it, asks how instruments should interact across sections, wants the interaction map realized into JSON voices, or wants a DAW-ready multi-track file with drums. Trigger on "design the interaction map," "arrange this for full band," "realize this into composition JSON," "turn this ABC into MIDI," "make a BandLab-ready file," "who should play when," or handing over a decided composition for production.
---

# ABC to MIDI Orchestration

Take the **decided** composition and produce a **DAW-ready multi-track result**. Primarily this means realizing it as a composition JSON (written via `../json-composition/SKILL.md`): one voice per instrument plus a `role:"drums"` voice. The legacy alternative is a validated ABC composition converted to a multi-track MIDI (one clean track per instrument, plus a drum track on channel 10). Either way, the core craft is the same: design the **interaction map** — which instrument leads, supports, answers, or stays silent, bar by bar — so the arrangement breathes instead of everyone playing all the time.

This skill assumes the musical ideas are decided (by `jazz-composition`) and the composition is written and validated — as JSON (by `json-composition`), or, on the legacy path, as ABC (by `abc-notation`). It does not invent chords or melodies. Its job is arrangement + realization/conversion.

## The rule that keeps arrangements from sounding cluttered

**The dramatic arc (from the composition plan) is the master; the interaction map serves it.** The map is not a chance to make everyone busy — it's how you translate the arc's emotional journey into "who plays when." A section that should feel lonely has one or two voices and lots of silence; a section that should feel full has the ensemble together. Do not add activity that doesn't serve the arc. Subtraction (dropping a voice) is as powerful as addition — often more.

See `../RED-FLAGS.md` for common excuse-vs-reality failure patterns in this domain.

## Primary path: JSON

The **primary** output path is now composition JSON, written by `../json-composition/SKILL.md`. The interaction map below (lead/support/answer/silent per section) is still designed exactly the same way — it just gets *realized* differently: by **which notes/rests are written into the composition JSON voices**, not by editing ABC or running `abc_to_midi.py`. Concretely:

- **Exact voicing**: those exact pitches are now **written directly into the JSON `chords` voice**, per `../json-composition/references/schema.md` — the LLM writes the voicing itself, rather than converting scientific pitch notation into ABC octave marks.
- **Drums** are no longer a separate `drums.json` step-grid — they are a `role:"drums"` voice in the same composition JSON, alongside the pitched voices. The pocket/feel that `%%pocket` plus the engine's `realize()` used to add automatically is now **baked into the explicit notes** the JSON writer produces — see `../json-composition/references/baking-feel.md`.
- The ABC-conversion steps in this file (Step 5, and the `abc_to_midi.py`/`grid_to_midi.py` references below) remain for the **legacy ABC path** — kept, not deleted, for when ABC is the artifact in hand.

## Workflow

### Step 1 — Read the plan and the arc

If a `composition-plan.json` is available, read its `arc`, `ensemble`, and per-section `phrasing`/`tension`. The arc tells you the density and interaction each section needs. If only ABC is provided, infer the sections and ask the person for the emotional shape if it isn't obvious — the interaction map is meaningless without knowing what each section should feel like.

### Step 2 — Design the interaction map (serving the arc)

Read `references/interaction-map.md`. For each section, decide per instrument: **lead / support / answer / silent**, and mark where call-and-response, subtraction, and density changes happen. Density must track the arc — sparse where the arc is quiet, full where it peaks. Produce a concrete bar-or-section table, not a vague sentence. Then apply the quality gate: does each section feel different, following the arc? Is any voice active only to fill space rather than serve the moment? If so, silence it.

For an ensemble or style that needs more than the four-role map (big band, duo/trio conventions, trading, cue systems, backgrounds), read the deeper `references/ensemble-interaction.md` — then reduce the decisions back to the map's table format. Where a section boundary needs more than a bare cut, `references/instrumental-transitions.md` catalogs transition families (rhythmic, harmonic, melodic, bass, textural, negative-space) and how to size the transition to the size of the change.

The map drives how you write or adjust the ABC voices (a "silent" instrument gets rests; an "answer" instrument plays in the gaps the lead leaves) and how you shape the drum grid (drums also follow the arc — near-absent when lonely, full when warm).

### Step 3 — Prepare the pitched ABC (legacy — jalur ABC saja)

On the JSON path, this step's decisions — silent voices get rests, answering voices play in the lead's gaps, density matching each section's role, exact voicing — are written directly as notes/rests into the composition JSON's pitched voices, per `../json-composition/SKILL.md` and `../json-composition/references/schema.md`. The rest of this step describes the legacy ABC equivalent.

Ensure the ABC reflects the interaction map: silent voices have rests for those bars, answering voices play in the lead's gaps, and the density matches each section's role. If the ABC needs changes, that's an `abc-notation` task — keep it validated (`validate_abc.py`) before converting. Every voice needs a `V:` header with a `name="..."` so the converter can map it to an instrument. When the ABC needs exact register/attack/voice-leading detail (lofi, neo-soul, smooth jazz, production-ready harmony), read `references/exact-voicing.md` — it uses scientific pitch notation (`C4` = middle C), so convert explicitly to ABC's octave marks before writing (see the note at the top of that file).

### Step 4 — Design the drum grid (also serving the arc) (legacy — jalur ABC saja)

On the JSON path, drums are written directly as notes in a `role:"drums"` voice in the composition JSON, following the same arc-driven density logic below, with feel baked into the explicit notes per `../json-composition/references/baking-feel.md` (not a separate step-grid). The rest of this step describes the legacy ABC/step-grid equivalent.

Drums stay out of ABC (they're not pitched). Write them as a step-grid JSON — see `assets/drum-grid-template.json`. Critical: **the grid's total bars must match the ABC's total bars**, section for section, or the drums and the band drift out of sync. Build the grid section-by-section from the same plan so the bar counts line up. Let the drums follow the arc: minimal in quiet sections, full in the peak, fading at the end.

For the actual pocket (per-role tick offsets, gate ratios) instead of inventing numbers ad hoc, read `references/groove-profiles.md` — it distills `references/advanced-microtiming.md` into a named, reusable profile (`neo-soul-core`) that both this grid and the downstream engine can implement consistently. Pick a profile; don't re-derive ticks per song. Declare the choice in the ABC itself as a directive, `%%pocket <id>` (e.g. `%%pocket neo-soul-core`) in the tune header before the first voice, so the downstream engine picks the matching groove profile — the brain's job is to *pick* a profile by name, never to write per-note tick numbers into the ABC.

### Step 5 — Convert and merge (legacy — jalur ABC saja)

Read `references/midi-conversion.md` for the two bug-fixes that are mandatory (they were found by actually importing to a DAW):

1. **Strip chord symbols before rendering.** ABC chord symbols in quotes (`"Cm9"`) will otherwise be sounded as chord notes, piling up into a drone on every track. The converter removes them; never render raw.
2. **Force the lead voice monophonic.** A melody voice should be one note at a time; keep the top note if any chord slips through.

Run the converters:

```bash
python3 scripts/abc_to_midi.py <file.abc> pitched.mid      # per-voice pitched tracks
python3 scripts/grid_to_midi.py <drums.json> drums.mid      # channel-10 drum track w/ swing + humanize
```

Then merge (append the drum track to the pitched PrettyMIDI object and write once). Verify: each track's end time is roughly equal (sync check), the lead track's max polyphony is 1 (mono check), and total bars match the plan. If the lead runs long-note drones, the chord-strip step was skipped — fix and re-render. If the meter, subdivision, or swing feel itself is in question (odd meter, clave, shuffle vs. straight-16th, etc.), `../groove-rhythm/references/groove-meter.md` is the deeper reference; for a full pre-delivery audit across form, transitions, groove, harmony, voicing, melody, and more, run this module's `references/rubric.md` (plus the sibling `rubric.md` in each other module) before Step 6.

### Step 6 — Deliver

Output the single merged `.mid`. Tell the person it imports to BandLab (or any DAW) as separate tracks they can voice, mute, or edit — the drum track lands on channel 10 so the DAW treats it as a kit. Note what serves the arc (where the subtraction is, where the peak is) so they hear the intent. Instrument sounds come from the DAW's patches; this is MIDI data, not finished audio.

This package's converters (BandLab or any external DAW) are the **alternative** downstream path. The **primary** downstream for this whole package is the `daw_generative` engine, consumed as an external HTTP contract — `POST /api/render`. On the JSON path (primary), the request body **is the composition JSON itself** (voices, including the `role:"drums"` voice, already carrying baked-in feel). The legacy alternative is the ABC body, `{abc, drums?, mastering?}`, for the ABC path described in Step 5 above. Say which path the delivered artifact targets; either way the engine realizes it (FluidSynth rendering, mastering) and returns audio.

## References

- `references/interaction-map.md` — how to design lead/support/answer/silent per section, call-and-response, subtraction, and density that tracks the arc; includes the quality gate.
- `references/ensemble-interaction.md` — deeper jazz performance-practice reference (duo/trio/big band conventions, call-and-response, trading, cue systems) for when the four-role map needs more nuance.
- `references/instrumental-transitions.md` — transition families, durations, and source-target analysis for section boundaries.
- `references/exact-voicing.md` — exact pitch/register/attack/voice-leading detail, in scientific pitch notation; convert to ABC octave marks when writing.
- `references/advanced-microtiming.md` — the principles behind pocket, velocity, and note-length design (reference layer, bounded offsets, instrument relationships, microtiming profiles).
- `references/groove-profiles.md` — the numeric distillation of the above into a named, shared pocket table (`neo-soul-core`: per-role tick offsets and gate ratios); pick a profile instead of inventing numbers.
- `../groove-rhythm/references/groove-meter.md` — meter, subdivision, and feel reference (swing, clave, odd meter, polyrhythm) beyond straightforward 4/4.
- `references/rubric.md` — this module's scoring rubric (production/DAW-first, plus the DAW-plan validation row); run before Step 6 alongside the other modules' `references/rubric.md` and `skills/jazz-composition/references/scorecard-template.md` for the full cross-module audit.
- `references/midi-conversion.md` — how the converters work, the two mandatory bug-fixes, GM program mapping, swing/humanization, and the sync/mono verification checks.
- `scripts/abc_to_midi.py` — multi-voice ABC → per-track MIDI (strips chord symbols, forces mono lead). (legacy — jalur ABC saja)
- `scripts/grid_to_midi.py` — drum step-grid → channel-10 MIDI with swing and velocity humanization. (legacy — jalur ABC saja)
- `assets/drum-grid-template.json` — starting point for a drum grid; match its bar counts to the ABC.

## Dependencies

Requires `music21` and `pretty_midi` (`pip install music21 pretty_midi`). Both are pure-Python and install from PyPI.

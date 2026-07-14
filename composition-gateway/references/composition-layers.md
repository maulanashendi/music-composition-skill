# The fourteen-layer composition map

This is the big-picture method behind the gateway: a strong jazz piece is
**not** built by picking chords at random and draping a melody over them. It
is built in layers, top-down — high layers set direction, low layers decide
how every note, chord, accent, and texture actually works.

**Read this as an index, not as a workflow to run here.** Each layer names
the concern *and the skill that already executes it*. When someone asks
"where does X get decided?", this tells you which skill and reference owns it.
The gateway routes; the owning skill does the work.

The layers follow the macro → meso → micro doctrine in
`../jazz-idea-generator/references/reasoning-theory.md` (Module 5): big
decisions constrain medium ones, medium constrain small. Work big-first.

---

## MACRO — direction and shape

### Layer 1 — Artistic concept
The song's identity before a single note: style family, character/mood,
energy direction, target ensemble, harmonic complexity.
**→ `jazz-idea-generator`, Step 1** (lock the brief and the emotional
journey). See also `references/reasoning-theory.md` Module 1 (mood → the
seven musical parameters).

### Layer 2 — Song architecture
The overall form (AABA, ABAC, blues, through-composed) and the full
performance structure (intro, head, solos, interlude, shout chorus, head
out, coda) — with a *function* for each section.
**→ `jazz-idea-generator`, Step 2** (design the arc as sections). Deeper
form mechanics in `references/form-and-dramaturgy.md`.

### Layer 13 — Dynamics and dramaturgy
The energy curve across the whole piece — not just volume, but register,
density, articulation, harmonic tension, rhythmic activity, instrument
count, note duration, and silence.
**→ designed as intent in `jazz-idea-generator`** (the arc and per-section
tension) **and realized in `abc-to-midi-orchestration`** (interaction map,
dynamics). ⚠️ **Known gap:** the converter currently emits flat velocity=90
— microtiming/velocity groove profiles are documented in
`../abc-to-midi-orchestration/references/groove-profiles.md` but not yet
applied in `grid_to_midi.py`/`abc_to_midi.py`. Treat dynamics as a
hand-finished step in a DAW until that is fixed.

---

## MESO — harmony, melody, groove, arrangement

### Layer 3 — Harmony map
Tonal center, harmonic rhythm, a functional skeleton, then color/extensions
and a tension map. Harmony as *direction*, not just chord choice.
**→ `jazz-idea-generator`, Step 3** (bar-by-bar chords per section, tension
plan). Vocabulary in `references/ideation-theory.md`; device catalog in
`references/reasoning-theory.md` Modules 2–3.

### Layer 4 — Melody design
Core motif, contour, target tones, connecting the guide tones, conscious
interval choice, broken-chord lines, chromatic vocabulary, and *planned*
outside playing tied to the tension map. The theme and the improv vocabulary
are kept distinct.
**→ intent in `jazz-idea-generator`, Step 3** (hook + per-section phrasing);
**exact notes encoded in `abc-notation-writer`**. Design intent vs. exact
spelling is a deliberate split — don't collapse it.

### Layer 5 — Rhythm and groove
Feel (swing, straight, bossa, funk, odd meter, rubato…), rhythmic identity,
syncopation, anticipation, displacement, augmentation/diminution,
polyrhythm.
**→ feel/bass-character in `jazz-idea-generator`; groove realized in
`abc-to-midi-orchestration`.** See `references/groove-profiles.md` and
`references/groove-meter.md`.

### Layer 6 — Instrument arrangement
Give each instrument a role; vary texture and density (sparse → medium →
dense → sparse); avoid everyone playing full all the time.
**→ `abc-to-midi-orchestration`** (the bar-by-bar interaction map: who
leads / supports / answers / is silent). See `references/interaction-map.md`
and `references/ensemble-interaction.md`.

---

## MICRO — voicing, bass, drums, and the note-level detail

### Layer 7 — Comping and voicing
Move away from static block chords: shell, rootless, quartal, spread, upper
structure, drop, cluster, moving inner voices — voicing as motion, with
voice-leading.
**→ `abc-to-midi-orchestration`.** Exact voicings in
`references/exact-voicing.md`.

### Layer 8 — Bass line
Walking, two-feel, pedal, ostinato, counterline — with its own contour, not
just roots.
**→ bass character decided in `jazz-idea-generator`; the line built in
`abc-notation-writer` (pitched voice) and shaped in
`abc-to-midi-orchestration`.**

### Layer 9 — Drum design
Ride/hi-hat/snare/bass-drum comping, fills, setups, accents, form cues — as
a roadmap that follows the form.
**→ `abc-to-midi-orchestration`**, always as a **step-grid JSON**
(`drums.json`), never as an ABC drummap voice. Template:
`../abc-to-midi-orchestration/assets/drum-grid-template.json`.

### Layer 10 — Improvisation design
Solo form, harmonic freedom, solo development across choruses, background
figures.
**→ planned as section function in `jazz-idea-generator` (form) and staged
in `abc-to-midi-orchestration` (who plays under the solo).** ⚠️ **Known thin
spot:** improvisation is the least-developed area in the package today —
it is currently handled only as "solo" leadership in the interaction map.
When a piece leans heavily on blown solos, say so explicitly and expect to
hand-finish that section.

### Layer 11 — Interlude, shout chorus, transitions
Keep the form from being just theme → solo → theme: interludes reset or
modulate; shout choruses build the climax; transitions (fills, pedals,
breakdowns, fermatas) connect sections.
**→ form intent in `jazz-idea-generator`; executed in
`abc-to-midi-orchestration`.** See `references/instrumental-transitions.md`.

### Layer 12 — Intro and ending
An intro that opens the song's world (vamp, rubato, pedal, motif preview)
and an ending tied to the main motif (tag, ritard, fermata, vamp, final
hit).
**→ `jazz-idea-generator` decides the strategy (`ending` field in the
plan); `abc-notation-writer` + `abc-to-midi-orchestration` realize it.**

### Layer 14 — Low-level detail and review
The final pass over exact target tones, intervals, phrasing, articulation,
register, chord spelling, extensions, voice-leading, spacing, and
orchestration — then a whole-piece review by ear before fixing individual
notes.
**→ `abc-to-midi-orchestration`'s quality-control audit**
(`references/quality-control.md`, the /64 rubric). Remember the package
rule: a high rubric score is a **floor, not a ceiling**, and a clean
`validate_abc.py` pass does **not** mean the MIDI rendered correctly —
always check the actual rendered MIDI (track count, notes per track,
tempo/time-signature).

---

## The order, in one line

```
concept → architecture → harmony → motif → melody → rhythm →
arrangement → improvisation → detail → review
```

Which, in this package's pipeline, is:

```
composition-gateway   →  jazz-idea-generator  →  abc-notation-writer  →  abc-to-midi-orchestration
   (route here)           (concept → plan)        (plan → valid ABC)      (ABC → arranged MIDI, QC)
```

Built this way, intervals, broken chords, chromaticism, and outside playing
stop being random ornaments — each one lands as part of the melody design,
the tension map, and the development of the form.

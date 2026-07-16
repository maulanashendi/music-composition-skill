# Authoring JSON schema — field contract

This is the full field contract for the authoring JSON this skill writes
(spec: `docs/superpowers/specs/2026-07-16-json-composition-architecture-design.md`
§4, in the `daw_generative` repo). It's the same contract `scripts/validate_composition.py`
enforces — read this before writing, not after the validator complains.

## Shape

```json
{
  "schemaVersion": 1,
  "meta": { "title": "Contoh Neo-Soul", "key": "F major", "tempo": 72, "meter": "4/4" },
  "sections": [{
    "name": "A", "bars": 2,
    "harmony": [
      { "bar": 1, "beat": 1, "symbol": "Fmaj9" },
      { "bar": 2, "beat": 1, "symbol": "Dm9" }
    ],
    "voices": [
      { "role": "lead", "instrument": "rhodes", "notes": [
        { "bar": 1, "beat": 1,    "pitch": "A4", "dur": 1,   "vel": 68, "artic": "legato" },
        { "bar": 1, "beat": 2.52, "pitch": "C5", "dur": 0.5, "vel": 76, "artic": "accent" },
        { "bar": 1, "beat": 3,    "pitch": "F5", "dur": 1.5, "vel": 80, "artic": "legato" },
        { "bar": 2, "beat": 1,    "pitch": "E5", "dur": 1,   "vel": 70, "artic": "legato" },
        { "bar": 2, "beat": 2,    "pitch": "D5", "dur": 2,   "vel": 66, "artic": "legato" }
      ] },
      { "role": "chords", "instrument": "rhodes", "notes": [
        { "bar": 1, "beat": 1, "pitch": "A3", "dur": 4, "vel": 52, "artic": "legato" },
        { "bar": 1, "beat": 1, "pitch": "C4", "dur": 4, "vel": 52, "artic": "legato" },
        { "bar": 1, "beat": 1, "pitch": "E4", "dur": 4, "vel": 52, "artic": "legato" },
        { "bar": 1, "beat": 1, "pitch": "G4", "dur": 4, "vel": 52, "artic": "legato" },
        { "bar": 2, "beat": 1, "pitch": "F3", "dur": 4, "vel": 52, "artic": "legato" },
        { "bar": 2, "beat": 1, "pitch": "A3", "dur": 4, "vel": 52, "artic": "legato" },
        { "bar": 2, "beat": 1, "pitch": "C4", "dur": 4, "vel": 52, "artic": "legato" },
        { "bar": 2, "beat": 1, "pitch": "E4", "dur": 4, "vel": 52, "artic": "legato" }
      ] },
      { "role": "bass", "instrument": "bass", "notes": [
        { "bar": 1, "beat": 1, "pitch": "F2", "dur": 1, "vel": 84, "artic": "legato" },
        { "bar": 1, "beat": 3, "pitch": "C3", "dur": 1, "vel": 78, "artic": "legato" },
        { "bar": 2, "beat": 1, "pitch": "D2", "dur": 1, "vel": 84, "artic": "legato" },
        { "bar": 2, "beat": 3, "pitch": "A2", "dur": 1, "vel": 78, "artic": "legato" }
      ] },
      { "role": "drums", "instrument": "jazz-kit", "notes": [
        { "bar": 1, "beat": 1,    "pitch": "kick",  "dur": 0.5, "vel": 100, "artic": "normal" },
        { "bar": 1, "beat": 2.02, "pitch": "snare", "dur": 0.5, "vel": 88,  "artic": "normal" },
        { "bar": 1, "beat": 3,    "pitch": "kick",  "dur": 0.5, "vel": 92,  "artic": "normal" },
        { "bar": 1, "beat": 4.02, "pitch": "snare", "dur": 0.5, "vel": 90,  "artic": "normal" },
        { "bar": 2, "beat": 1,    "pitch": "kick",  "dur": 0.5, "vel": 100, "artic": "normal" },
        { "bar": 2, "beat": 2.02, "pitch": "snare", "dur": 0.5, "vel": 88,  "artic": "normal" },
        { "bar": 2, "beat": 3,    "pitch": "kick",  "dur": 0.5, "vel": 92,  "artic": "normal" },
        { "bar": 2, "beat": 4.02, "pitch": "snare", "dur": 0.5, "vel": 90,  "artic": "normal" }
      ] }
    ]
  }]
}
```

This exact object is `assets/song-template.json` — copy its shape, not its
notes, for a new song.

## Field contract

- `schemaVersion` — int, required. Currently always `1`.
- `meta.title` — string.
- `meta.key` — string `"<tonic> <mode>"`, e.g. `"F major"`, `"C# minor"`,
  `"Bb dorian"`. The importer parses this into `{tonic, mode}` downstream;
  authoring stays in the human-readable string form.
- `meta.tempo` — BPM, int > 0. Single global tempo — no ramps, no rubato,
  no per-section tempo change (out of scope; see spec §11).
- `meta.meter` — `"n/d"`, the default meter for every section.
- `sections[].name` — string label (e.g. `"A"`, `"Verse"`, `"Bridge"`).
- `sections[].bars` — int > 0, the section length in bars.
- `sections[].meter` — optional. Overrides `meta.meter` for this section
  only (e.g. a bridge that switches to 3/4). Omit when the section follows
  the global meter.
- `sections[].harmony` — an array of **positioned** chord events
  `{bar, beat, symbol}`, not one chord symbol per bar implicitly. This is
  deliberate: it kills the "1 chord/bar, cyclic" assumption that breaks the
  moment a tune has two harmonic rhythms per bar or a chord that holds for
  three bars. `symbol` is a standard chord symbol (`Fmaj9`, `Dm7b5`, `C7#9`,
  …) — write the actual harmony, not a Roman numeral.
- `sections[].voices[].role` — one of `lead | bass | chords | pad | drums`.
- `sections[].voices[].instrument` — a **registry id** (mirrors
  `src/instruments/registry.js` in the `daw_generative` engine). Known ids at
  the time of writing: `sax, piano, guitar, bass, rhodes, trumpet,
  vibraphone, jazz-kit, guitar-clean, bass-finger, synth-bass, synth-lead`,
  plus a small set of aliases (`electric-piano`/`ep`/`keys` → `rhodes`-style,
  `acoustic-bass`/`upright-bass` → `bass`, etc. — see
  `scripts/validate_composition.py`'s `INSTRUMENT_ALIASES` for the current
  list). An unrecognized instrument name is a **hard validation failure**,
  never a silent fallback to a default sound — the point of a registry is
  that "unknown instrument" is always visible, not swallowed.
- `sections[].voices[].notes[]` — the actual note events for that voice.

### Note fields

- `note.bar` — int, 1-indexed, relative to the section (bar 1 of section
  "B" is not bar 9 of the tune — it's bar 1 of that section).
- `note.beat` — float, 1-indexed (`1.0` is the first beat of the bar).
  Fractional beats place a note off the main pulse — `2.52` is a hair after
  beat 2.5, useful for baking feel (see `baking-feel.md`).
- `note.pitch` — for pitched voices (`lead`, `bass`, `chords`, `pad`), a note
  name like `"A4"` (`C4` = MIDI 60). For `role: "drums"`, a GM drum name —
  currently **`kick | snare | hihat | ride`** only (mirrors `DRUM_NOTES` in
  the engine's `src/playback/midi.js`); extending the drum vocabulary beyond
  these four is a separate, not-yet-made decision, not something to
  freelance in a composition.
- `note.dur` — duration in beats (float). **There is no tie mechanism.**
  Because every note's position is an absolute `(bar, beat)` pair rather
  than a chain of linked segments, a note that needs to ring across a
  barline is written as a single note whose `dur` simply extends past the
  current bar's beat count — e.g. a whole note starting on bar 1 beat 4 in
  4/4 just has `dur: 4`, ending at bar 2 beat 4, with nothing written on
  bar 2 for that voice. This is the practical payoff of absolute
  positioning: no `-` tie glyphs to open and forget to close.
- `note.vel` — velocity, int **1..127**. This is not decorative — see
  `baking-feel.md` and `rubric.md` on why a flat velocity value across every
  note reads as mechanical.
- `note.artic` — one of `legato | staccato | accent | normal`. Controls
  gate length (how much of the nominal duration actually sounds) downstream,
  not pitch or timing.

## What the validator checks (`scripts/validate_composition.py`)

All violations are collected and reported together — the validator does not
stop at the first error, so a self-heal pass can fix everything it finds in
one read instead of playing whack-a-mole:

- `bar` is within `1..sections[].bars`; `beat ≥ 1`; `dur > 0`.
- `(beat − 1 + dur)` does not overflow past the bar's length for the
  section's meter (reported, not silently clamped).
- No voice is declared with an empty `notes: []` — a 0-note voice is always
  a bug, never a legitimate "intentionally silent" voice (if a voice should
  be silent for a whole section, omit the voice entirely for that section).
- `instrument` is in the registry (aliases included); drum `pitch` is in the
  GM drum vocabulary.

A clean validator run means the file is structurally sound. It does **not**
mean the music is good — chord-scale conformance, voice-leading, dynamics
spread, and range are evaluated separately downstream (Gate A, spec §7) and
are not this skill's job to compute by hand.

## See also

- `../abc-notation/references/abc-syntax.md` — the equivalent contract for
  the older ABC path, useful only for contrast; do not mix the two formats
  in one deliverable.
- `baking-feel.md` — how to use `beat` offsets and `vel` deliberately so the
  performance doesn't sound quantized.
- `rubric.md` — how a finished authoring JSON gets scored.

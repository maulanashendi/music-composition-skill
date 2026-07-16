---
name: json-composition
description: Encode a decided musical idea as authoring JSON and validate it before hand-off to the engine. Use whenever someone has a locked composition idea — a composition-plan.json, a chord progression, a bassline, or a melody they've decided on — and wants it written as the JSON authoring format (schemaVersion 1: meta + sections + harmony + voices + notes), or when authoring JSON keeps failing validation (bar/beat overflow, unknown instrument, empty voice) and needs fixing. Trigger on "write this as JSON," "turn this progression into composition JSON," "my composition JSON won't validate," "validate this composition JSON," or handing over a composition plan to notate for `/api/render`. This skill does the encoding, feel-baking, and validation; it does not brainstorm musical ideas (that's jazz-composition) or render MIDI.
---

# JSON Composition Writer

Encode a **decided** musical idea into the authoring JSON contract (§4 of
`docs/superpowers/specs/2026-07-16-json-composition-architecture-design.md`
in the `daw_generative` repo) that validates cleanly and carries real
performance feel, not just correct pitches. This skill is the primary
notation-encoder in this package — it supersedes `abc-notation` as the
default output path; the ABC path is kept only for backward compatibility,
not for new compositions.

This skill does **not** invent musical content. If the idea isn't decided
yet — vibe, form, harmony, melody, arrangement — that's `jazz-composition`'s
job — stop and say so rather than guessing chords, melodies, or voicings.

## Input

Best input is a filled `composition-plan.json` (produced by
`jazz-composition`). This skill also accepts a raw progression, bassline, or
melody the person already committed to (from jamming, a reference, or
another session). If a critical field is missing — key, tempo, meter, or the
actual notes/chords per bar — **ask; do not guess.** Guessing here produces
a file that validates but plays the wrong music.

## Workflow

### Step 1 — Gather essentials

Confirm you have, before writing anything: `key`, `tempo`, `meter`, the
section layout (names + bar counts), the harmony (bar/beat-positioned chord
symbols, not one implicit chord per bar), and which voices exist for each
section (`lead`/`bass`/`chords`/`pad`/`drums`) with their instrument. Map
each `composition-plan.json` field to the authoring JSON's `meta`/
`sections` fields. If a section's meter differs from the global one (e.g. a
3/4 bridge), note the override explicitly rather than letting it default
silently.

### Step 2 — Write the authoring JSON with every voice explicit

Read `references/schema.md` for the full field contract before writing —
`schemaVersion`, `meta`, `sections[].harmony` (positioned `{bar, beat,
symbol}` events, not per-bar-implicit), `sections[].voices[].role`/
`instrument`/`notes`. Write **every declared voice's notes explicitly**,
including chord voicings (each chord tone as its own note event at the same
`bar`/`beat`, not a shorthand chord symbol standing in for actual pitches)
and drums (a `role: "drums"` voice using GM names `kick`/`snare`/`hihat`/
`ride` — never pitched notes standing in for percussion). A voice that's
declared but left with `notes: []` is always a bug, never an intentional
silence — omit the voice for a section instead of declaring it empty.

### Step 3 — Bake the feel

Read `references/baking-feel.md`. The engine does **not** humanize this
path — whatever pocket the piece needs must be written into the JSON
itself: dynamic `vel` (ghost notes low, accents high — never one repeated
velocity across a voice), `beat` nudged off-grid (snare/keys laid back a
touch behind the grid, bass pickups sitting ahead of it, lead phrase notes
nudged for lay-back), and `artic` for note length (`legato`/`staccato`/
`accent`/`normal`). Translate `../groove-rhythm/references/groove-profiles.md`'s
`neo-soul-core` numbers into concrete beat/vel/artic values rather than
inventing a feel from scratch or leaving everything dead-on-grid.

### Step 4 — Realize the interaction map through what's written and left out

The arrangement's interaction map (who leads, who lays out, where the space
is) is not a separate document in this format — it's realized entirely
through which notes are written and which beats are left as rests per
voice. A voice that should sit out for a section is simply omitted from
that section's `voices` array; a voice that should thin out for a bridge
gets fewer/sparser notes there, not a flag. Cross-check the written notes
against the interaction map decided upstream (in `jazz-composition`/
`arrangement`) before moving to validation — a voice with the right pitches
but wrong density silently breaks the arrangement even though it validates.

### Step 5 — Validate, and self-heal on failure

Run the validator:

```bash
python3 scripts/validate_composition.py <file.json>
```

It checks `schemaVersion`/`meta` presence, bar/beat/dur bounds and overflow,
empty voices, and instrument/drum-name validity against the registry — and
collects **all** violations rather than stopping at the first one. If it
reports errors:

1. Read every reported violation, not just the first.
2. Fix each one at its source (an out-of-range `bar`, an unrecognized
   `instrument` id, an empty `notes: []`, a `beat`+`dur` that overflows the
   bar).
3. Re-run. Repeat until it prints `valid`.

This is the same self-healing retry loop `abc-notation` uses for ABC: feed
the validator's own error back into a targeted fix rather than rewriting
the whole file. Don't declare success until it passes with 0 violations —
and remember a clean validator pass is a structural floor, not a quality
signal (see `references/rubric.md` for what it doesn't catch).

### Step 6 — Deliver

Output the validated JSON file. The body is the composition JSON itself,
sent as-is to `POST /api/render` (the engine's canonical render endpoint —
no wrapping, no sidecar). Note the validator result and flag anything a
human should double-check (an unusual instrument choice, a section meter
override, a deliberately sparse voice). Say it's ready for `/api/render` —
importer enrichment (authoring → canonical, tick math, id generation) and
MIDI rendering happen downstream in the engine, not in this skill.

## References

- `references/schema.md` — the full §4 field contract: types, bounds, what
  the validator enforces, the template as worked example. The syntax
  authority for this format.
- `references/baking-feel.md` — how to bake pocket (velocity, off-grid
  `beat`, `artic`) without relying on engine humanization, which does not
  exist on this path.
- `references/rubric.md` — scoring rubric: schema-valid, every voice
  non-empty, dynamics not flat, feel baked, drums as a valid GM voice.
- `assets/song-template.json` — a complete, validated 2-bar neo-soul example
  (lead/chords/bass/drums) to copy the shape of.
- `scripts/validate_composition.py` — the schema/bounds/registry validator.
  Run on every file before hand-off.

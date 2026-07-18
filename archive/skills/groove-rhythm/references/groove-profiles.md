# Groove profiles — the shared pocket table

This is the numeric distillation of `advanced-microtiming.md` §4 (instrument
relationships) and §9 (microtiming profiles), cross-checked against an
applied case study (`neo-soul-core`, derived from a full DAW-plan blueprint
built and validated against this same craft). It exists so the **composing
brain only has to name a profile** ("use `neo-soul-core`") — the numbers
themselves live here once, and the downstream engine that actually renders
timing (this package's `grid_to_midi.py`/`abc_to_midi.py`, or the
`daw_generative` engine on `POST /api/render`) implements them consistently.
Do not re-derive or restate per-note tick offsets in a composition plan or in
prose — reference the profile name.

## Why a shared table, not per-note numbers

`advanced-microtiming.md` §1 already establishes the principle: microtiming
is a *bounded, relational* offset around a reference layer, not
per-note randomization. A shared table turns that principle into something
both a reasoning brain (this package, or `compose-song`-style skills) and a
rendering engine can point to by name, so "elastic neo-soul pocket" means the
same bar-for-bar ticks everywhere it's used, instead of drifting composition
to composition.

## `neo-soul-core` profile

Reference layer: **hi-hat sixteenth grid**, with quarter-note accents sitting
close to the grid (the anchor). Tempo/PPQ examples below assume 96 BPM at 960
PPQ (quarter note = 625 ms, 1 tick ≈ 0.65 ms) — recompute ms from the actual
tempo using `advanced-microtiming.md` §2; the tick ranges themselves do not
change with tempo.

| Role | Offset (ticks) | Approx ms @ 96 BPM/960 PPQ | Notes |
|---|---:|---:|---|
| Kick | 0 to +4 | ~0 to +2.6 | Anchor — stays essentially on the grid; this is what the other roles are relative to. |
| Snare / backbeat | +18 to +24 | ~+11.7 to +15.6 | Consistently behind the grid — the main source of the "laid-back" feel. |
| Bass, arrivals (chord-change downbeats) | +2 to +7 | ~+1.3 to +4.6 | Close to the kick — locks the low end. |
| Bass, pickups (approach notes into an arrival) | −12 to −6 | ~−7.8 to −3.9 | Ahead of the grid — the anticipation that makes the arrival land. |
| Keys / Rhodes, chord attacks | +16 to +22 | ~+10.4 to +14.3 | Behind the grid, similar to snare — comping breathes with the backbeat, not against it. |
| Lead, target/structural notes | +3 to +10 | ~+2 to +6.5 | Close to the grid, slightly behind — keeps structural targets intelligible. |
| Lead, pickups | earlier than the target's offset | — | Pickups anticipate; exact amount is phrase-level push/pull (`advanced-microtiming.md` §4, lead melody), not a fixed tick. |

**Hi-hat**, tiered rather than a single offset class:
- quarter-note hits: strong, close to the grid (they *are* the reference layer);
- off-beat/in-between hits: ghost-level, velocity below 45 (out of 127)  — dynamic variation, not clutter (`advanced-microtiming.md` §6).

**Gate (note-off / sustain ratio, as a fraction of the nominal note length)**:

| Role | Gate ratio | Notes |
|---|---:|---|
| Bass | ~0.78–0.90 | Short of full sustain — leaves room for the kick and for syncopated silence. |
| Keys / Rhodes | ~0.62–0.86 | Wider range because comping density varies most by section — sparse comping can gate as low as 0.62; sustained pad-like voicings sit near 0.86. |
| Lead | ~0.86–0.96 | Closest to full sustain — the lead should not sound clipped; use the lower end only for deliberately detached/staccato phrasing. |

**Ready-to-paste `drums.json` `timing` map (ms offsets, derived from the tick table above).** Convert the tick ranges to ms at 96 BPM/960 PPQ and round to a single per-role value the drum grid can use directly (kick as anchor at 0; snare/rimshot laid-back behind the grid; hi-hat a touch ahead). The composing brain copies this block into `drums.json` under top-level `timing` — do not re-derive per song:

```json
"timing": { "kick": 0, "snare": 15, "rimshot": 25, "chh": -3 }
```

`grid_to_midi.py` applies these deterministically per role (see `../../midi-orchestration/references/midi-conversion.md`, `timing` field). Ride/open-hat, if used, sit near the hi-hat/anchor range; add them only when the kit uses them, keeping kick at 0 as the reference.

## How this maps to this package's artifacts

- **Pitched voices (ABC).** `advanced-microtiming.md` distinguishes *notated
  displacement* (written rhythm) from *performance placement* (the offsets
  above). ABC written by the `abc-notation` module (dulu `abc-notation-writer`)
  stays on notated rhythm;
  performance placement is not written into the ABC itself — state the
  chosen profile as a **directive**, not a comment: `%%pocket neo-soul-core`
  on its own line in the tune header, before the first `V:` voice. That is a
  real ABC directive (`%%`, two percent signs), not a `%` comment — the
  `daw_generative` engine's `src/abc/midi-directives.js` parses `%%pocket` to
  select which named profile's per-role tick offsets and gate ratios to
  apply at render time. As of this package's writing, that parsing is
  planned for Task 7 of the daw_generative 2-tools architecture initiative
  and is not yet implemented — writing `%%pocket neo-soul-core` today is
  forward-compat/declarative: it costs nothing (the directive is inert to
  any consumer that doesn't look for it) and means the ABC is already
  correct once Task 7 ships. Until then, treat it the same as the fallback
  below: left to the renderer/performer, or applied downstream at the MIDI
  stage if the target pipeline supports per-note offset (this package's
  `abc_to_midi.py` does not currently apply per-note micro-offset; state the
  profile as intent for a human or downstream DAW to apply).
- **Drums (step-grid JSON).** `grid_to_midi.py` already implements swing and
  velocity humanization at the grid level (`references/midi-conversion.md`).
  The kick/snare/hi-hat rows above describe the *intended* relationship this
  swing-and-humanize step should approximate; when a grid's `swing` value and
  per-hit velocity are tuned, tune them toward this table rather than an
  arbitrary feel.
- **`daw_generative` engine (`POST /api/render`).** When the ultimate
  consumer is the `daw_generative` engine rather than this package's own
  converters, the engine owns the actual micro-timing implementation. This
  table is the contract both sides read from — the composing brain picks
  `neo-soul-core` (or names a deviation and why), the engine renders it the
  same way every time.

## Choosing vs. deriving

The composing brain (`jazz-composition`/`vibes-mood` at idea stage — dulu
`jazz-idea-generator` — or a human directing the `midi-orchestration`
module, dulu `abc-to-midi-orchestration`) should **select** a named profile —
currently only `neo-soul-core` is defined here — rather than invent new
per-role tick numbers ad hoc. A genuinely different pocket (e.g. a tight
acoustic-swing profile, per `advanced-microtiming.md` §9 "Tight acoustic or
ensemble profile") is a candidate for a *new* named profile added to this
file, not a one-off number set buried in a single composition's notes. Adding
a profile means adding a new table section here (same shape: reference
layer, per-role offset table, gate table), so it stays a shared, reusable
contract instead of drifting per song.

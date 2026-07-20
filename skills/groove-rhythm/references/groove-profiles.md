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

## `fusion-tight` profile

The opposite pocket to `neo-soul-core`: a **tight 16th funk** feel where the
backbeat sits *on* the grid, not behind it, and the whole band locks hard to a
riff. Use for jazz-funk / fusion vamps (`style-cheatsheets.md` "Jazz-funk /
fusion") where identity comes from the bass-and-drum riff lock, not from a
laid-back drag. Tempo/PPQ examples below assume 108 BPM at 960 PPQ; the tick
ranges do not change with tempo (recompute ms via `advanced-microtiming.md` §2).

Reference layer: **hi-hat/16th grid**, with the kick and snare both anchored
essentially on the grid — the "tight" character is *small* offsets everywhere,
not a laid-back backbeat.

| Role | Offset (ticks) | Approx ms @ 108 BPM/960 PPQ | Notes |
|---|---:|---:|---|
| Kick | 0 to +3 | ~0 to +1.7 | Anchor — dead on the grid; drives the riff. |
| Snare / backbeat | 0 to +6 | ~0 to +3.5 | On the grid, *not* behind it — this is what makes it "tight," the opposite of `neo-soul-core`'s +18..+24. |
| Bass, riff notes (locked to kick) | −2 to +4 | ~−1.2 to +2.3 | Sits right on/around the kick — the low-end lock is the whole point. |
| Bass, pickups (approach into a downbeat) | −8 to −3 | ~−4.6 to −1.7 | A little ahead — the push into the "1," smaller than neo-soul's pickup drag. |
| Keys / clav, stabs | 0 to +5 | ~0 to +2.9 | Close to the grid; punchy comping locks with the backbeat rather than dragging. |
| Lead, target/structural notes | 0 to +6 | ~0 to +3.5 | On the grid — clarity and drive over lay-back. |
| Lead, pickups | earlier than the target's offset | — | Phrase-level push (`advanced-microtiming.md` §4), not a fixed tick. |

**Hi-hat**, tiered: quarter/eighth accents strong and on the grid; in-between
16ths ghost-level (velocity below 45), driving but not cluttered.

**Gate (note-off / sustain ratio, fraction of nominal note length):**

| Role | Gate ratio | Notes |
|---|---:|---|
| Bass | ~0.55–0.75 | Shorter/punchier than neo-soul — funk bass is detached, leaves gaps for the kick. |
| Keys / clav | ~0.40–0.65 | Short stabs; the tightness is in the silence between hits. |
| Lead | ~0.80–0.95 | Still mostly sustained; use the low end for staccato riff-doubling. |

**Ready-to-paste `drums.json` `timing` map** (single per-role ms value; kick as
anchor at 0, snare on the grid, hi-hat a hair ahead for drive):

```json
"timing": { "kick": 0, "snare": 3, "rimshot": 3, "chh": -2 }
```

## `classic-jazz-swing` profile

The acoustic-ensemble pocket for classic jazz (`vibes-mood/references/classic-jazz-genre.md`
§7) — a straight-ahead 4-beat swing where the **ride cymbal's swung 8ths**
are the reference layer, not a 16th grid, and attacks sit close to that grid
rather than laid back. This is this package's applied case of
`advanced-microtiming.md` §9 "Tight acoustic or ensemble profile": major
attacks near the grid, articulation (mutes, growls, glissandi — see the
genre file §7) carries the feel more than timing offset does. Tempo/PPQ
examples below assume 132 BPM (medium swing) at 960 PPQ (quarter note ≈
454.5 ms, 1 tick ≈ 0.47 ms); the tick ranges do not change with tempo
(recompute ms via `advanced-microtiming.md` §2).

Reference layer: **ride cymbal swung-8th pattern** (`1, 2-and, 3, 4-and`),
triplet-subdivided; the walking bass and comping lock tightly to it rather
than dragging behind.

| Role | Offset (ticks) | Approx ms @ 132 BPM/960 PPQ | Notes |
|---|---:|---:|---|
| Ride (swung 8th pattern) | 0 to +4 | ~0 to +1.9 | Anchor — defines the swing subdivision everything else locks to. |
| Kick (feathering, all 4 beats) | −2 to +2 | ~−0.9 to +0.9 | Barely audible — a felt pulse, not a hit; stays essentially on the grid. |
| Hi-hat (chick on 2 & 4) | −3 to +3 | ~−1.4 to +1.4 | Tight, near the grid — this era does not lay the backbeat back. |
| Bass, walking quarter notes | −6 to 0 | ~−2.8 to 0 | Slightly ahead of the grid — upright bass characteristically pushes the band forward, the opposite of `neo-soul-core`'s drag. |
| Bass, chromatic approach tone | −10 to −4 | ~−4.7 to −1.9 | The anticipation into the next chord's downbeat. |
| Piano stride (LH bass note, beats 1 & 3) | −4 to +2 | ~−1.9 to +0.9 | Locked close to the kick/bass. |
| Guitar/piano comping chunk (Freddie Green, every beat) | −2 to +4 | ~−0.9 to +1.9 | Tight and percussive — the short gate (below) does more work than the offset. |
| Horn section ensemble hits (shout-chorus stabs, block chords) | −2 to +5 | ~−0.9 to +2.4 | Section unity matters more than individual offset — tight as one voice. |
| Lead, structural/target notes | 0 to +6 | ~0 to +2.8 | Close to the grid, articulation (fall-off, doit, shake) carries expression. |
| Lead, pickups | earlier than the target's offset | — | Phrase-level push, not a fixed tick (`advanced-microtiming.md` §4). |

**Gate (note-off / sustain ratio, fraction of nominal note length):**

| Role | Gate ratio | Notes |
|---|---:|---|
| Bass | ~0.55–0.75 | Detached "boom" articulation — short of full sustain keeps walking lines clear. |
| Piano/guitar comping chunk | ~0.25–0.45 | Very short and percussive — the Freddie Green/stride-chord "chunk" character lives in the silence between hits. |
| Piano stride bass note | ~0.65–0.85 | Longer than the chunk — the left-hand bass note rings more than the chord it alternates with. |
| Horns, legato phrasing | ~0.80–0.95 | Solo lines and soli sections — sustained. |
| Horns, shout-chorus/staccato hits | ~0.45–0.65 | Ensemble punches — short and accented, not sustained. |

**Ready-to-paste `drums.json` `timing` map** (kick near-silent anchor, hi-hat
chick tight on the grid, snare/rimshot used for backbeat accents rather than
a laid-back feel):

```json
"timing": { "kick": 0, "snare": 2, "rimshot": 2, "chh": -1 }
```

Set the grid's `swing` field high (~0.62–0.67) relative to
`neo-soul-core`/`fusion-tight` — classic jazz's triplet swing is more
pronounced than a lightly-swung 16th feel. The ride pattern itself is not
one of the four standard drum-grid roles (`kick`/`snare`/`rimshot`/`chh`);
program it as `ride` hits on the swung-8th steps per
`../../midi-orchestration/references/midi-conversion.md`, with `swing`
driving the "and" displacement.

## `bossa-nova-straight` profile

The pocket for bossa nova (`vibes-mood/references/bossa-nova-genre.md` §2,
§8) — a **straight, unswung 16th grid** carried by the guitar batida,
shaker, and cross-stick, with only the lead/vocal laid back or rubato on
top. This is the genre's defining contrast and the thing most likely to get
flattened into another profile by mistake: do not swing the rhythm section
(that drifts toward `classic-jazz-swing`), and do not drag the *whole*
ensemble behind the grid (that drifts toward `neo-soul-core`/lofi — see the
differentiation table in the genre file §8). Tempo/PPQ examples below assume
120 BPM (classic bossa) at 960 PPQ (quarter note ≈ 500 ms, 1 tick ≈ 0.52 ms);
the tick ranges do not change with tempo (recompute ms via
`advanced-microtiming.md` §2). `swing` should be set to **0.5** (no swing) —
lower than every other named profile in this file.

Reference layer: **straight 16th grid**, defined jointly by the guitar
batida, shaker, and cross-stick — all three stay tight to it.

| Role | Offset (ticks) | Approx ms @ 120 BPM/960 PPQ | Notes |
|---|---:|---:|---|
| Guitar batida (thumb bass note & finger chord) | 0 to +3 | ~0 to +1.6 | Anchor — dead straight, defines the grid other rhythm-section roles lock to. |
| Shaker (constant 16th pulse) | 0 to +2 | ~0 to +1 | Tight to the grid — the high-frequency pulse that makes "straight" audible. |
| Cross-stick (echoes the batida on the rim) | 0 to +3 | ~0 to +1.6 | Locked to the guitar's fingerpicking pattern, not offset from it. |
| Surdo/kick (muted, beat 1 soft / beat 3 fuller) | −2 to +3 | ~−1 to +1.6 | Near-silent thud, no boom — offset is negligible, the character is in the mute/velocity, not timing. |
| Bass, downbeat arrivals (beat 1: root) | −2 to +3 | ~−1 to +1.6 | On the grid with the rest of the rhythm section. |
| Bass, anticipation (beat 3 -> 5th, pulled ahead into the next bar) | written a subdivision early | — | This is a **notated displacement**, not a microtiming offset — write the anticipated note itself an 1/8-1/16 early on the grid (`advanced-microtiming.md` §1's notated-vs-performance distinction), then apply the small ±tick range above to that written position. Do not simulate it with a large negative tick offset on the written beat. |
| Lead/vocal, structural/target notes | +8 to +20 | ~+4 to +10 | Laid-back — the genre's one deliberately-behind-the-grid voice. |
| Lead/vocal, rubato phrases | not tick-bound | — | May depart from the grid entirely at phrase level; the rhythm section does not follow it (`advanced-microtiming.md` §4). |

**Gate (note-off / sustain ratio, fraction of nominal note length):**

| Role | Gate ratio | Notes |
|---|---:|---|
| Guitar batida | ~0.35–0.55 | Short, percussive fingerpicked chunks — the "click" of nail-on-string matters as much as pitch. |
| Bass | ~0.45–0.65 | Short pizzicato decay, never sustained. |
| Lead/vocal, legato phrasing | ~0.85–0.98 | Sustained, breathy — contrasts with the clipped rhythm section underneath it. |

**Ready-to-paste `drums.json` `timing` map** (all roles near zero — "straight"
is the point; character comes from mute/velocity, not offset):

```json
"timing": { "kick": 0, "snare": 0, "rimshot": 1, "chh": 0 }
```

Set `swing: 0.5` in the grid (contrast with `neo-soul-core`'s 0.57 and
`classic-jazz-swing`'s ~0.62–0.67 — bossa is the one profile in this file
with no swing at all). Map surdo to the `kick` role at reduced
`base_velocity` (heavily muted, no low-end boom) and shaker to `chh`, per
`../../midi-orchestration/references/midi-conversion.md`.

## Choosing vs. deriving

The composing brain (`jazz-composition`/`vibes-mood` at idea stage — dulu
`jazz-idea-generator` — or a human directing the `midi-orchestration`
module, dulu `abc-to-midi-orchestration`) should **select** a named profile —
currently `neo-soul-core` (laid-back swung-16th), `fusion-tight` (on-the-grid
16th funk), `classic-jazz-swing` (tight acoustic-ensemble triplet swing,
per `advanced-microtiming.md` §9 "Tight acoustic or ensemble profile"), and
`bossa-nova-straight` (unswung 16th rhythm section, laid-back/rubato lead
only) are defined here — rather than invent new per-role tick numbers ad
hoc. A genuinely different pocket is a candidate for a *new* named profile
added to this file, not a one-off number set buried in a single
composition's notes. Adding
a profile means adding a new table section here (same shape: reference
layer, per-role offset table, gate table), so it stays a shared, reusable
contract instead of drifting per song.

# Reasoning theory — the theory-reasoning layer (from `compose-song`)

Summarized and adapted from the Claude Code skill `compose-song`
(consolidated 2026-07-13). The original had 9 reasoning modules that
constrain the composition process *before* any note is written; this file
condenses them for `jazz-idea-generator` without changing the existing
six-step workflow in `SKILL.md` — treat the seven modules below as *extra
tools* used inside Step 2 (brief & mood), Step 3 (generate candidates), and
Step 5 (quality gate), alongside `ideation-theory.md` and
`style-cheatsheets.md`. The concrete genre profile (neo-soul/chill-jazz) now
lives in its own skill, `neo-soul-genre`.

## Module 1 — Emotional function: mood → musical parameters

Used at Step 2 (Lock the brief AND the emotional journey), as the concrete
complement to a vibe adjective. Every mood is mapped onto the same **seven
fixed dimensions** so moods stay comparable across candidates: tempo,
dynamics, harmonic stability & color, rhythmic activity, texture density,
register, voice-leading character.

| Mood | Tempo | Dynamics | Harmonic stability & color | Rhythmic activity | Texture density | Register | Voice-leading |
|---|---|---|---|---|---|---|---|
| **Calm** | Moderate (68-78 BPM) | Soft (mp), minimal swell | Stable — diatonic, maj7/m7, rare cadences | Little syncopation, settled groove | Sparse (1-2 active layers) | Mid, avoid extremes | Smooth — common tone, stepwise |
| **Tense** | Steady or slightly rising | Crescendo/sharp accents into the peak | Dissonant — chromaticism, dominant prolongation, altered dominant | More active, rising syncopation/ghosts | May thicken toward the climax | Rising toward the peak | Directed leaps, chromatic approach |
| **Focused** | Moderate, stable (72-82 BPM) | Even, minimal spikes | Consistent motif, slow harmonic rhythm | Repetitive, predictable | Not dense (tight density ceiling) | Mid, consistent | Repeating motif, minimal drastic variation |
| **Wistful** | Moderate-slow (70-80 BPM) | Soft, slight rubato feel | Borrowed iv/modal interchange, maj7 brushing minor | Gentle, slightly behind the beat | Medium, with space/rests | Mid-high for the melody | Subtle chromatic approach, gradual descent |
| **Warm** | Moderate (72-84 BPM) | Consistent mp-mf | Stable, maj9/6-9 color, smooth root movement | Settled groove, slight swing | Medium, layers complement each other's register | Mid, avoid too high/sharp | Common-tone dominant, gentle extensions |
| **Nocturnal** | Slow-moderate (66-76 BPM) | Soft, large space between phrases | Minor/modal, m9/m11, pedal point | Sparse, lots of rest/silence | Very sparse | Low-mid, occasional high for contrast | Long held tones, minimal motion |
| **Hopeful** | Moderate, slightly rising (78-86 BPM) | Building, swell into the return | Open major, secondary dominants aiming at resolution | Progressively active, energy rising in stages | Thickening as the progression moves | Rising in stages toward the peak | Directional, stepwise toward resolution |
| **Introspective** | Slow (66-74 BPM) | Very soft, close | Ambiguous minor/modal, sus chords not fully resolving | Minimal, rubato | Very sparse, near-solo instrument | Low-mid, intimate | Subtle inner voice, top note nearly static |

**How to use:** pick the dominant mood from the brief (a combination of 2 is
fine, but declare 1 as leading), copy that row into seven explicit
decisions — this is what constrains the candidate choices at Step 3, not the
reverse. For a mood outside the table: fill in the same seven dimensions;
don't add a new dimension without reflecting it back across all the other
rows. Contrast within one piece is healthy (e.g. calm intro → tense B →
warm outro), but each section has its own fully declared mood — don't mix
the seven dimensions of two different moods inside the same section.

## Module 2 — Theory-hierarchy declaration (gate)

Used approaching Step 3, before the first candidate is written concretely.
One **main theory** (usually a tonal center/mode) + **supporting theories**
per dimension (harmony, melody, texture, groove) that spell out how the main
theory is realized — not a random device list, but a coherent vocabulary.
The hierarchy declared up front **constrains the vocabulary** that may be
used without extra justification (see Module 3).

Template:

```
## Theory Hierarchy Declaration — <short title/brief>

- Main theory: <tonality/mode/tonal center + why it fits the Module 1 mood>
- Harmony support: <permitted chord/progression vocabulary>
- Melody support: <permitted motion/contour/targeting>
- Texture support: <permitted density/comping model/voicing>
- Groove support: <permitted rhythm feel/swing/time-feel>
- Devices outside the hierarchy (fill in later if they come up) + justification:
  <device> → <why, see Module 3>
```

Binding rules: mood (Module 1) precedes the hierarchy — the tonal
center/harmony choice must be consistent with the seven mood dimensions;
macro-level decisions (song form/tonal center, see Module 5) bind the levels
below them; one declaration per piece, with per-section variation recorded
as part of the same hierarchy, not a second independent hierarchy.

## Module 3 — Cause-and-effect device catalog

Used whenever picking a device (chord, voicing, rhythm) not already
explicit in the theory hierarchy (Module 2). Format: **Device → Why
(musical effect) → When NOT to**. Using a device per its "Why" column needs
no extra justification; using it beyond that (violating "When NOT to") still
needs explicit extra justification, recorded on the "Devices outside the
hierarchy" line of the Module 2 declaration.

| Device | Why (musical effect) | When NOT to |
|---|---|---|
| **ii–V–I** | Needs direction toward the tonic — a clear "coming home" feel | Section needs to stay static/ambiguous (e.g. nocturnal with pedal point) |
| **maj9 / 6-9** | Soft, warm color, not a harsh dominant | Approaching a climax that needs sharp tension |
| **secondary dominant** | Directed push toward the next chord | Used in a row every bar — becomes generic |
| **broken chord** | Flowing texture, leaves room for bass/melody | Bass is already rhythmically active — can mask the low register |
| **stepwise melody** | Smooth phrase, easy to follow, affirms the motif | Used the whole piece with no variation |
| **m7/m9/m11** | Soft/introspective color without dominant tension | Replacing the ENTIRE dominant function |
| **7sus/9sus/13sus** | Motion without aggression, deliberately delayed resolution | Used at a final cadence |
| **altered dominant** | Brief, concentrated tension, a peak marker | "Calm"/"focused" sections |
| **borrowed iv / modal interchange** | Wistful color, blurs the major/minor boundary | Without a top line that affirms the new color |
| **slash chord / inversion** | Melodic bass, smooths root motion | Bass already has an independent working line of its own |
| **chromatic approach** | Smooth, economical transition to a target chord-tone | Used more than 2x in a row |
| **pedal point** | Holds one harmonic area, focus & space | Section needs active root motion (e.g. a building hopeful) |
| **rest / silence** | Tension release, room for the motif to be "remembered" | Overused until the groove feels broken |
| **omit-root voicing** | Avoids low-register mud, leaves room for the bass | Chord instrument plays solo without a bass |
| **ghost note** | Feel/pocket (drum & bass), not decoration | Replacing the main groove |
| **register shift** | Raises intensity, marks a new section boundary | Used every bar |

How to use: first check whether the device is already covered by a
"Support ..." line of the hierarchy (Module 2) — if so, use it directly. If
not, find it in this table; the "Why" column is the automatic
justification, but check "When NOT to" first. Not in the table and not in
the hierarchy: needs explicit manual justification or don't use it. Re-check
"When NOT to" on each use, not once at the start and then assumed always
safe. The `neo-soul-genre` skill can add genre-specific devices that aren't
generic enough for this table.

## Module 4 — Compatibility, leadership, and idea limits per section

Used at Step 5 (quality gate), against the **full** candidate draft — not
per note. A draft that is theory-correct section by section can still fail
once the sections are assembled together.

**Lens 1 — Compatibility matrix.** Pairs that **fit** (give each other
room): complex harmony + simple melody; simple groove + rich voicing; calm
bass + more active piano; active melody + minimal accompaniment. Pairs that
**collide** (fight for the same room): busy melody + busy piano at once;
very chromatic harmony + overly free bass (two sources of instability at
once); slow tempo + too-frequent chord changes (disproportionate harmonic
rhythm); relaxed mood + aggressive rhythmic accents. If you hit a colliding
pair: reduce one (subtractive), don't add a third element to "balance" it.

**Lens 2 — Element leadership per section.** Each section has **ONE** leader;
the other elements give room:

| Section | Led by |
|---|---|
| Intro | Piano/comping texture |
| Theme (A) | Melody |
| Solo | Improvisation (whichever lead has the turn) |
| Transition | Harmony (chord motion marking a new direction) |
| Outro | Resolution (harmony back to the tonic + subtraction of elements) |

When the melody is the focus, harmony & rhythm section MUST give room — not
become a second focus. Two elements fighting for the foreground in the same
section is a red flag.

**Lens 3 — Main-idea limit per section.** Per section, limit the theory
ideas active at once to **one** of each: one harmonic character, one melodic
motif (a transformed version of the central motif), one main groove, one
dominant texture. Too many theories at once makes a section lose its
identity — the listener can't grasp "what this section is about". Variation
*between* sections is healthy (see the variation budget in the
`neo-soul-genre` skill); variation *within* the same section is dangerous.

**Running the three lenses:** split the draft by section → check Lens 1
(active pairings), Lens 2 (one leader), Lens 3 (one idea per dimension) →
any section failing one: revise (usually subtractive), then re-run Module 6
(tension/release) for the revised section.

## Module 5 — Structural levels: macro / meso / micro

Theory works at three levels; the work order must be large first, then
medium, then small.

| Level | Work unit | Example decisions | If problematic, revise here... |
|---|---|---|---|
| **Large (macro)** | The whole piece | Song form, tonal center, overall energy direction | Come back here DELIBERATELY — re-declare the hierarchy (Module 2) if the tonal center changes |
| **Medium (meso)** | Section / 4-8 bar phrase | Per-section chord progression, phrase boundaries, cadence, modulation | Revise that section; check the impact on neighboring sections |
| **Small (micro)** | Bar / beat | Specific voicing, passing tone, articulation, local rhythmic motif | Revise locally ONLY — not a reason to change the large form |

Binding rule: large decisions bind medium, medium binds small. Don't revise
the large level from a small-level complaint without realizing it — one odd
voicing in one bar is a cue to fix the voicing (small), not an automatic
reason to change the song form. Raise the revision level only when the
problem shows up consistently across many sections (a pattern, not one
point), and do it deliberately (state the reason explicitly).

In `jazz-idea-generator`, this means: Steps 2-3 work the large level (arc,
form, tonal center) first; bar-by-bar chords (Step 3 point 3) and phrasing
(point 6) are the medium level; concrete note-by-note voicing is the small
level, deliberately **deferred** to `abc-notation-writer`/
`abc-to-midi-orchestration` (see the "production-stage" note in the §Workflow
Step 3 of this SKILL.md) — that split is consistent with the "large first"
rule here.

## Module 6 — Tension & release as an evaluation tool

Distinct from the tension-release *palette* in `ideation-theory.md` §4c (a
list of *techniques* you can use), this module is an **evaluation tool**:
scan the written draft and compare it against the planned macro-level energy
direction (Module 5). Fixed vocabulary:

| Element | Effect |
|---|---|
| **Tonic** | Stability, "home" — the relaxation point |
| **Dominant** | Tension — needs resolution |
| **Chromatic note** | Momentary color / pressure |
| **Rest (silence)** | Release — room for the motif to be remembered |
| **High register** | Rising intensity |
| **Close voicing** | Density |
| **Open/spread voicing** | Openness |

Mandatory questions, asked BEFORE writing a section (plan) and AFTER
(verify): *where does the music need to be tense, where relaxed?* Build a
simple map:

| Section | Plan (before) | Realized (after) | Dominant element used |
|---|---|---|---|
| Intro | low | ... | e.g. tonic, open voicing, rest |
| A1 | medium | ... | e.g. dominant at the phrase end |
| B/detour | high | ... | e.g. chromatic note, close voicing |
| A3 | medium→low | ... | e.g. back to the tonic |
| Outro | low | ... | e.g. rest, tonic, descending register |

Plan says "high" but the realization is flat (all tonic/rest/low register)
= a signal to revise at the medium/small level (Module 5) — add the
appropriate device (Module 3), not change the song form. Common mistakes
this tool catches: a "tense" section written entirely in "release"
vocabulary; a climax that was never prepared; a resolution never reached
(tension piling up without enough rest/tonic to release it).

## Module 7 — Measurable verification protocol (adapted to this package's pipeline)

The original source (`compose-song`) wrote this protocol for its own
internal JS pipeline (`fromComposition`/`realize`/`toMidi`/`POST /api/render`
of the `daw_generative` repo). This `music-composition-skill` package does
**not** have that pipeline — this package's downstream is the `daw_generative`
engine (an external consumer, via the `POST /api/render {abc, drums?,
mastering?}` contract) **or** this package's own music21/`pretty_midi`
converters (`abc-notation-writer/scripts/validate_abc.py` →
`abc-to-midi-orchestration/scripts/abc_to_midi.py` + `grid_to_midi.py`)
toward BandLab/an external DAW. The principle and shape of the checks stay
the same; here is the adaptation:

1. **Mechanical validation** (mandatory, replacing "note-on velocity>0 in the
   canonical Song"): `validate_abc.py` (structure, bar durations, ties/slurs)
   and, when music21 is available, `music21.converter.parse` — this is the
   hard gate before moving on to orchestration (see
   `abc-notation-writer/SKILL.md` Step 4).
2. **Merged MIDI** (replacing the non-silent stereo WAV check when the
   downstream is NOT `daw_generative`): after `abc_to_midi.py` +
   `grid_to_midi.py` + merge
   (`abc-to-midi-orchestration/references/midi-conversion.md`), check
   inter-track sync, mono lead (max polyphony 1), and no drone (chord symbols
   stripped) — this checklist is already in `midi-conversion.md` and MUST be
   run, not assumed to pass because a `.mid` file exists.
3. **Duration vs. song form:** compute the expectation (`bars × beatsPerBar ×
   60 / bpm`) and compare with the actual MIDI/WAV duration. A large gap →
   the per-section bar count in the ABC (or the drum grid) doesn't match the
   plan — go back to `jazz-idea-generator`/`abc-notation-writer`, don't "skip
   it".
4. **Per-track density vs. genre density ceiling:** compute the proportion of
   time each track is active (not resting) per section, compare with the
   genre density ceiling (see the `neo-soul-genre` skill — e.g. ≤1 foreground
   voice at a time). This catches "theory-correct but overfull" that the
   mechanical validator misses — go back to Module 4 Lens 2/3 if it fails.
5. **Lead vs. comping register collision:** compare the lead's MIDI note range
   vs. the comping's per section; a large overlap while both are active =
   a masking indicator — fix via omit-root voicing/register shift (Module 3).
6. **If downstream = the `daw_generative` engine:** that server already runs
   its own `assertAudible` at `POST /api/render` (200 = passed the server-side
   silent/minimum-duration check). A 200 from the server is **not** a
   substitute for points 3-5 above — it only confirms it isn't dead silent.

**What the agent CANNOT do** (applies to this package too, no exceptions):
judge subjectively whether the piece is "enjoyable"/"moving"/"on-vibe";
listen without theory-expectation bias; catch elements that are
"excessive/distracting" even when they pass every theoretical check. That is
a human's authority — consistent with the "Ear first, metrics follow"
principle in the `daw_generative` project's `CLAUDE.md`. The existence of a
`.mid`/`.wav` file is **not** proof of success, only proof the pipeline ran
without crashing. This skill (and the others in this package) is
**FORBIDDEN** to claim "enjoyable"/"good"/"cool" — the strongest allowed
claim: *"passes theory + measured metrics are healthy, awaiting a human ear."*

## Relation to the other files in this package

- Modules 1-2 are used together with `ideation-theory.md` §4b (dramatic arc)
  during Steps 1-2 of `jazz-idea-generator/SKILL.md`.
- Modules 3-5 are used at Step 3 (generate candidates) and bind how
  candidates are differentiated structurally, not just cosmetically.
- Modules 4 and 6 together become the concrete content of Step 5 (quality
  gate) — that gate already exists in `SKILL.md`; these modules give it tools
  that can be run explicitly, not just "listen for whether it's good".
- Module 7 is relevant again after `abc-notation-writer` and
  `abc-to-midi-orchestration` have run — noted here because its question
  framework comes from the same reasoning process, even though the technical
  execution lives in the later skills.

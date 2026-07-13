# Neo-soul / chill-jazz — deep profile

The depth behind the `neo-soul-genre` skill's core (musical DNA, roles, vibe
map). Read when a neo-soul brief needs harmony, motif, pocket, rotation,
variation, arrangement, or mix specifics.

## 3. Functional harmony & voice-leading

Work order (aligned with `jazz-idea-generator/references/reasoning-theory.md`
Module 5, medium→small level):

1. The function of each harmonic area: home / departure / tension / return.
2. Simple root/bass motion.
3. Add seventh chords.
4. Add 9/11/13/sus/altered/borrowed **only when it improves color or melodic
   motion** — check the cause-and-effect catalog
   (`jazz-idea-generator/references/reasoning-theory.md` Module 3) for why
   each device.
5. Voicing with smooth inner voices (concrete voicing/register/attack detail
   is in `abc-to-midi-orchestration/references/exact-voicing.md`, done in that
   skill — here just decide the *color and motion*, not the exact pitches).
6. Test the melody over the voicing; revise chords that fight the motif.

Color vocabulary (cause-and-effect detail in
`jazz-idea-generator/references/reasoning-theory.md` Module 3): maj7/maj9/6-9
(warm) · m7/m9/m11 (soft) · 7sus/9sus/13sus (motion without aggression) ·
secondary dominant (direction) · altered dominant (brief tension) · borrowed
iv/modal interchange (wistful) · slash/inversion (melodic bass) · chromatic
approach (transition, economical).

Voice-leading: prioritize common tone + half/whole-step motion in the inner
voices · the bass carries the root so the chord instrument may **omit root** ·
each voicing's top note = a hidden countermelody · don't put every extension
on every chord · spread low voicings so they don't turn to mud (see §9, mix
direction).

## 4. One motif before writing a solo

A 3-7 note motif / a single rhythmic cell that survives transformation:
octave-shifted, played by another instrument, rhythmically displaced,
shortened to its last 2-3 notes, reharmonized in section B, quoted by
bass/Rhodes/outro.

Motif development (not random improvisation): **Statement → Answer → Fragment
→ Expansion → Absence.**

- **Statement** — play the motif clearly.
- **Answer** — change its ending interval/rhythm.
- **Fragment** — use only part of it.
- **Expansion** — lengthen one note or add a tail.
- **Absence** — leave empty space so the motif is "remembered", not repeated.

Motif = identity; solo/improvisation = an interpretation of that identity, not
a separate thing. This is the **hook** in `ideation-theory.md` §5 terms — give
that hook a fragment form, a full statement, and a transformed return, just
like in `jazz-idea-generator/assets/composition-plan-template.json`. Done when
≥3 sections use a transformed version of the same motif without copying the
exact phrase.

## 5. Pocket design (drum + bass)

**Drums:** round kick with minimal click · dusty snare/rimshot/clap · part of
the backbeat slightly behind the grid · vary hi-hat velocity + leave gaps ·
ghost notes as feel (not decoration) · short, meaningful fills (at section
boundaries, not every 4 bars).

**Bass:** start on root + long notes · approach note near a chord change ·
selective slide/ghost/syncopation · simple when the lead is active, more
melodic when the lead rests · coordinate with the kick without mirroring
every hit.

**Pocket rule:** don't randomly humanize every note — set a consistent
relationship. The concrete pocket numbers (per-role tick offsets, gate ratios)
are standardized in the `groove-design` skill as the `neo-soul-core` profile
(`groove-design/references/groove-profiles.md`) — the composition brain here
just **picks that profile**, it doesn't recompute ticks per note. Done when
the groove still feels intentional with only drums + bass + the simplest chord
voicing sounding.

**This package's drum doctrine (binding):** drums are **ALWAYS** a step-grid
JSON, never an ABC voice — this cross-skill rule is explained in
`abc-notation-writer/references/drums-and-abc.md` and `RED-FLAGS.md`.

## 6. Lead rotation without losing identity

Contrast comes from **timbre & register**, not loudness. Pattern:

```
Lead 1 states → silence → Lead 2 answers → rhythm section breathes → Lead 3 transforms
```

Each lead has a 2-4 bar window; only **one** foreground at a time; the
instrument that steps out becomes texture/countermelody/silence; the motif
vocabulary is shared across performers; each instrument's articulation is
distinct (guitar can bend/muted-attack, synth sustains, piano gives rhythmic
answers, sax/flute use breath/long curves). Done when each lead has a reason
to enter, a reason to leave, and a relationship to the central motif. The
concrete execution (who plays in which bar) is the interaction map — a
`abc-to-midi-orchestration` Step 2 job; here just plan the rotation pattern.

## 7. Controlled variation

Repetition is needed for focus. Prevent boredom by changing **only 1-2
dimensions** per interval:

| Interval | Appropriate change |
|---|---|
| Every 4 bars | Fill, ghost, pickup, chord stab, small lead answer, brief silence |
| Every 8 bars | Voicing, top note, hat pattern, bass ending, motif instrument, final chord |
| Every 16 bars | Lead rotation, texture change, new harmonic area, breakdown, register shift |
| Every 32 bars | Structural detour, emotional peak, big subtraction, full return |

**Variation budget** for each new section: keep ≥2 anchors (e.g. groove +
harmonic color) · change 1 primary dimension · optionally 1 secondary
detail · **do not** change harmony + groove + lead + palette + dynamics at
once. Use **subtractive arrangement** as often as additive — removing
kick/hat/bass/lead for a moment is often more effective than adding a new
instrument. This is axis B ("massive + original"): the same variation budget
can be reused for a large batch of outputs without becoming one reskinned
template.

## 8. Arrangement architecture

A reliable proportion (not rigid law):

```
Intro 8 · A1 16 · A2 16 · B/detour 8-16 · A3 16 · Breakdown 8 · Final A 16 · Outro 8
```

| Section | Dramatic function |
|---|---|
| Intro | Establish texture & a motif fragment; hold back the full groove |
| A1 | Present the core harmony, bass, drums, first lead |
| A2 | Keep the groove, change lead/voicing/bass ending |
| B/detour | Harmonic/modal/textural/rhythmic contrast — a new chord isn't required; contrast can come from a pedal bass, dropping drums, a register shift, reassigning the motif |
| A3 | Return with accumulated meaning, not a literal copy |
| Breakdown | Reduce density, reset attention |
| Final A | Present the clearest motif or a controlled ensemble exchange |
| Outro | Release elements one by one, leave a shadow of the motif |

Done when each section differs from its previous appearance in ≥1 meaningful
dimension (variation budget §7). This architecture aligns with arc-first in
`ideation-theory.md` §4b — map the arc first (e.g. intimate→build→peak→return),
then fit the bar proportions onto that arc, not the reverse.

## 9. Sound & mix direction

Compose & arrange **before** relying on effects. Warm, centered kick/bass ·
avoid low-register chord clusters colliding with the bass · subtle
saturation/tape/vinyl · lead with more upper-mid definition · reverb/delay as
a phrase tail, not a constant wash · keep ≥1 source of clarity so "lo-fi"
doesn't turn to mush. The hierarchy that must stay audible at low volume:
groove first, harmonic atmosphere second, lead rotation clear but not
dominant like a pop vocal.

> **Honest timbre (project-vision principle):** the final "is it good?"
> judgment uses samples/soundfonts as close to the final result as possible
> (e.g. via this package's music21 converter into a DAW/BandLab, or via
> `POST /api/render` when the downstream is the `daw_generative` engine), not
> a generic synth or a rough preview as the final decision.

## Common pitfalls

| Symptom | Fix |
|---|---|
| Complex chords with no memorable idea | Write the motif first (§4), extensions follow with a reason |
| Every instrument sounds all the time | Assign foreground/support/silence explicitly per section (skill body §2, `jazz-idea-generator/references/reasoning-theory.md` Module 4 Lens 2) |
| Variation feels random | Keep ≥2 anchors, change 1 primary dimension (§7) |
| The loop feels exactly repeated | Vary voicing/orchestration/bass ending/subtraction, not just repeat |
| Too much soloing | Short statement + rest (§6), not prolonged noodling |
| "Lo-fi" becomes all-muffled | Keep 1-2 clear elements (§9) |
| Bass & Rhodes mask each other | Omit-root voicing, separate the registers (`jazz-idea-generator/references/reasoning-theory.md` Module 3) |
| Humanize without pocket | Use the consistent `neo-soul-core` profile (§5), not random offsets |
| The B section feels like a different song | Keep the motif/groove fingerprint/core harmonic color |
| Imitating a reference too literally | Extract attributes (tempo/texture/density), re-create your own harmony/melody/rhythm |

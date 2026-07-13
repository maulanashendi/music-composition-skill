---
name: groove-design
description: Design the rhythmic pocket, feel, and meter of a piece — pick a named microtiming profile (per-role tick offsets, gate ratios) instead of inventing numbers, and handle swing, subdivision, odd meter, clave, and polyrhythm. Use when choosing or specifying a groove/pocket for a composition or a drum grid, when a section needs a particular feel (laid-back, behind-the-beat, shuffle vs. straight sixteenths), or for anything beyond a plain 4/4. Trigger on "design the pocket," "what groove," "swing feel," "behind the beat," "odd meter," "clave," "humanize the drums." Cross-cutting: used by both the idea and orchestration skills.
---

# Groove design — pocket, feel, and meter

The shared home for how a piece *feels* rhythmically. It is used at **both**
ends of the composition pipeline: `jazz-idea-generator` picks a pocket profile
by name at ideation, and `abc-to-midi-orchestration` applies it to the drum
grid and the pitched tracks at Step 4. Consolidating it here removes the
duplication that used to live across the orchestration references and the
neo-soul genre notes.

## The load-bearing doctrine

- **Pick a named profile; don't invent ticks.** The concrete numbers (per-role
  tick offsets, gate ratios) live once in `references/groove-profiles.md` as
  named profiles (e.g. `neo-soul-core`). The composing brain's job is to
  *name* a profile, never to write per-note tick numbers into a plan or ABC.
- **Offsets are relational and bounded**, not per-note randomization — a
  microtiming displacement is measured against a reference layer (usually the
  kick/ride), and stays inside a small range. Random humanization is not a
  substitute for groove design.
- **Keep notated displacement separate from performance offsets.** What the
  score says (note values) and how it is performed (pocket offsets) are two
  layers; don't bake performance feel into wrong note values.
- **Declare the choice in the ABC** as a directive — `%%pocket <id>` (e.g.
  `%%pocket neo-soul-core`) in the tune header before the first voice — so the
  downstream engine selects the matching profile. Picking the profile is this
  skill's job; realizing the ticks is the engine's.

## Read which reference when

| File | Read when | Canonical for |
|---|---|---|
| `references/groove-profiles.md` | picking/declaring a pocket (default) | the **numeric** profile table (`neo-soul-core`: per-role tick offsets, gate ratios) |
| `references/advanced-microtiming.md` | you need to justify or shape a pocket beyond an existing profile | the **principles** — reference layer, bounded offsets, velocity/note-length, instrument relationships, profile design |
| `references/meter-and-feel.md` | anything beyond straight 4/4 | meter, subdivision, swing, clave, odd/compound meter, polyrhythm, metric modulation, extreme syncopation |

## How this plugs into the pipeline

- `jazz-idea-generator` Step 3: when the groove matters (it usually does),
  name a profile here and record it in the plan — do not derive ticks.
- `abc-to-midi-orchestration` Step 4: read the declared `%%pocket <id>`, apply
  the profile to the drum grid and pitched tracks; the meter/subdivision
  reference backs any odd-meter or swing decision.
- The `neo-soul-genre` skill's pocket section points here for the numbers;
  this skill owns them.

---
name: neo-soul-genre
description: Concrete genre profile for neo-soul / chill-jazz / lo-fi-soul composition — musical DNA (tempo zone, warm Rhodes/Wurlitzer harmony, dusty pocket), the anchor/rotation/ear-candy role model, motif development, controlled variation, and arrangement architecture. Use when the target style is neo-soul, chill jazz, jazzhop, or lo-fi soul and you need the genre's specifics rather than generic composition advice. Trigger on "neo-soul," "chill jazz," "lo-fi soul," "warm Rhodes groove," "who plays what in neo-soul," or a brief in that family. Knowledge only — it does not write notation or MIDI.
---

# Neo-soul / chill-jazz — genre profile

Adapted from the `compose-song` Claude Code skill's genre file
(`references/genres/neo-soul.md`, consolidated 2026-07-13), itself adapted
from the Hermes skill `original-neo-soul-composition` (MIT). This is the
**first** genre with a concrete profile in this package; it deepens the
`Jazzhop / neo-soul` family entry in `jazz-idea-generator/references/style-cheatsheets.md`
rather than replacing it. Other genres (bebop, modal, bossa, etc.) still use
`style-cheatsheets.md` as a starting point; adapt the principles here and
label choices "default" explicitly when a brief asks for a style outside both.

**DO NOT** literally imitate a copyrighted artist, song, or arrangement —
translate references into musical attributes (tempo, texture, harmonic
density, articulation, dynamics, emotional arc). Governing principle: *keep
the foundation predictable enough to allow focus while developing the surface
enough to reward attention.* Originality comes from the **combination** of
motif + voicing + groove + phrasing + palette + arrangement — not from
complicated chord names.

## Musical DNA (defaults)

| Parameter | Default profile value |
|---|---|
| Tempo zone | 68-86 BPM (relaxed pocket; halftime feel for faster tempos) |
| Meter | 4/4, light swing / humanized sixteenths |
| Tonal center | Major (warm/open) or minor-modal (introspective); borrowed harmony may blur the boundary |
| Palette (role→instrument) | Anchor: Rhodes/Wurlitzer + finger bass + lo-fi drums · Rotation: clean guitar, soft synth, sax, flute, piano · Ear-candy: reverse tail, chord stab, perc fill |
| Density ceiling | ≤ 1 foreground voice at a time |

These are a starting point, not law — adjust to the brief's vibe while
staying in the neo-soul/chill-jazz family. If the final downstream is the
`daw_generative` engine (`POST /api/render`), note that it currently realizes
only `4/4` — check before promising another meter in the plan; this package's
own music21 converter (`abc-to-midi-orchestration`) has no such limit.

## 1. Vibe map (genre lens)

Use the seven dimensions of `jazz-idea-generator/references/reasoning-theory.md`
Module 1 as the basis. For neo-soul, the most useful contrast is: which
element is brighter/sharper/wider/more animated against a stable foundation.
Example intent sentence: *"A warm nocturnal focus track — Rhodes, bass, and
dusty drums stay stable while guitar, synth, and piano take turns carrying
short melodic statements."*

## 2. Role model (anchor / rotation / ear-candy)

| Layer | Function | Typical instruments |
|---|---|---|
| **Anchor** | Stability & focus | Rhodes/Wurlitzer, bass, drums |
| **Rotation** | Development & character | Clean guitar, soft synth, sax, flute, piano |
| **Ear candy** | Small moments of discovery | Reverse tail, chord stab, perc fill, tape stop, ambience |

Each sound has ONE role; don't let every instrument act as a lead. At every
moment, explicitly identify who is foreground/support/background — this is a
concrete case of element leadership per section
(`jazz-idea-generator/references/reasoning-theory.md` Module 4, Lens 2)
applied to the neo-soul ensemble.

## How this plugs into the pipeline

- Read during `jazz-idea-generator` Step 3 when the target style is
  neo-soul/chill-jazz — it supplies the genre specifics that the generic
  vocabulary can't.
- **Depth:** `references/neo-soul-profile.md` carries harmony & voice-leading,
  motif development, pocket, lead rotation, controlled variation, arrangement
  architecture, and sound/mix. Read it when you need more than the DNA above.
- **Pocket numbers** are not here — pick the `neo-soul-core` profile from the
  `groove-design` skill (`groove-design/references/groove-profiles.md`).
- **Exact voicing/register** is a production decision in
  `abc-to-midi-orchestration/references/exact-voicing.md`; the **bar-by-bar
  interaction map** is `abc-to-midi-orchestration/references/interaction-map.md`.
  This skill decides *feeling and role*, not exact pitches or the per-bar map.

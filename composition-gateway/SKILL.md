---
name: composition-gateway
description: The single entry point for making music with this package — greet any request to compose, write, arrange, or start a song or instrumental track, figure out where the person already is in the pipeline, and route them into the right skill (jazz-idea-generator, abc-notation-writer, or abc-to-midi-orchestration) instead of doing the work here. Use FIRST whenever someone wants to build a piece end-to-end, asks "how do I make this tune," "what's the process," "help me start a track," "arrange this," or hands over a mood, scene, brief, chord progression, composition-plan.json, or ABC without saying which step they want. This skill routes and holds the big-picture map of how a composition is built layer by layer; it does not itself write plans, notation, or MIDI.
---

# Composition Gateway

The **front door** of this package. A composition is built in layers — from
artistic concept down to note-level detail — and this package already
executes those layers across three skills. What has been missing is a single
place that **greets a raw request, works out where the person actually is,
and sends them to the right skill.** That is this skill's only job.

This skill **routes and maps. It does not compose.** It never writes a
`composition-plan.json`, never writes ABC, never writes MIDI. Those are the
downstream skills' jobs, and their boundaries are load-bearing — see
`../CLAUDE.md` and `../RED-FLAGS.md`.

## The one rule that keeps the gateway thin

**Point, don't perform.** The moment you know which skill owns the next step,
hand off to it and let it run its own workflow. Do not start designing an arc,
spelling chords, or arranging here to "save a step" — that is exactly how the
per-skill boundaries collapse and downstream skills get handed undecided
input. The package doctrine is explicit: *handing a downstream skill an
undecided input is a sign the upstream step was skipped.*

And the package's single most-broken rule, restated: **if a required field is
missing — key, tempo, meter, the actual chords, or whether the plan is even
locked yet — ask; do not guess.** The gateway is often where that gap first
shows; surface it here rather than passing a hole downstream.

## Router — "where are you?"

Read what the person actually handed you and match the first row that fits:

| What they have | What they want | Route to |
|---|---|---|
| Only a mood, scene, vibe, reference feel, or a fresh brief — nothing musical decided | Ideas, a direction, "help me start" | **`jazz-idea-generator`** |
| A locked `composition-plan.json`, or an already-decided progression / bassline / melody they're committed to | It written as notation | **`abc-notation-writer`** |
| Validated `song.abc` (with or without the plan) | It arranged / turned into a DAW-ready multi-track MIDI, "who plays when," drums | **`abc-to-midi-orchestration`** |
| "Do the whole thing" / unsure where they are | The finished piece, start to end | **`jazz-idea-generator`**, then walk the pipeline in order |

Then hand off in one sentence — name the skill and the artifact it takes as
input — and stop. The receiving skill owns the rest.

Two guards before you route:

- **Don't skip upstream.** If someone asks for ABC or an arrangement but has
  no locked plan and no decided material, the honest move is to route them
  *back* to `jazz-idea-generator` first, not to let a downstream skill invent
  the missing idea. A downstream skill inventing chords/melody is the exact
  boundary violation this package guards against.
- **Respect fixed material.** If the person already committed to a key,
  tempo, meter, progression, or ensemble, carry that forward as fixed — the
  routed skill should build on it, not override it.

## The layer map — how a composition is built, and who owns each layer

A piece is designed big-to-small: the large decisions constrain the medium
ones, and the medium constrain the small (the macro / meso / micro doctrine
in `../jazz-idea-generator/references/reasoning-theory.md`, Module 5). This
package spreads that work across three skills. Use this map to tell someone
*where* a given concern gets handled — not to handle it here.

**Macro — concept, form, energy** → `jazz-idea-generator`
: artistic identity, song architecture, the dramatic arc and energy curve.
  Owned by the idea skill's Steps 1–2.

**Meso — harmony, melody, groove, arrangement** → `jazz-idea-generator`
(design intent) then `abc-notation-writer` (encoded) and
`abc-to-midi-orchestration` (voiced/arranged)
: harmonic map, motif/melody phrasing, rhythm & groove, comping, bass, and
  the bar-by-bar interaction map. Design intent is decided in the plan;
  exact notes are encoded as ABC; voicing, interaction, and drums are built
  in orchestration.

**Micro — voicing, articulation, note placement, dynamics** →
`abc-to-midi-orchestration`
: exact voice-leading, drum step-grid, microtiming and dynamics, and the
  final quality-control audit
  (`../abc-to-midi-orchestration/references/quality-control.md`).

For the full fourteen-layer version of this map — every layer annotated with
the skill and reference file that executes it — read
`references/composition-layers.md`. Treat it as an index into the existing
skills, not as a second set of instructions to run here.

## What this gateway does NOT do

- **No ideation** — it does not design arcs, choose chords, or write hooks.
  That is `jazz-idea-generator`.
- **No notation** — it does not write or validate ABC. That is
  `abc-notation-writer`.
- **No arrangement or MIDI** — it does not build interaction maps, drum
  grids, or convert to MIDI. That is `abc-to-midi-orchestration`.
- **No audio** — nothing in this package renders audio; that is a separate
  downstream engine (see `../README.md`).

## References

- `references/composition-layers.md` — the full fourteen-layer composition
  map, each layer routed to its owning skill and reference. The index behind
  this skill's condensed layer map.
- `../CLAUDE.md` — package operating order and the ground rules the gateway
  enforces (ask-don't-guess; per-skill boundaries).
- `../README.md` — architecture and positioning (this package is the "brain";
  rendering is downstream).
- `../RED-FLAGS.md` — excuse-vs-reality failure patterns across all skills.

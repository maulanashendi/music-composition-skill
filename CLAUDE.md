# music-composition-skill — operating instructions

This package is **Tool 1, "the brain"**: it decides musical intent and writes
`plan.json` (schemaVersion 2). Rendering to MIDI/audio is a separate downstream
engine (`pyengine`) — see `README.md` for the architecture/positioning.

## Live skills (what actually exists)

Two entry points, chosen by **who is driving**:

- `skills/jazz-composing/SKILL.md` — **interactive** entry. Brief → Ideation →
  Plan. Asks when a required field is undecided.
- `skills/composing-headless/SKILL.md` — **headless/batch** entry. One turn, no
  questions, exactly one `plan.json`, declares `meta.template`. Used by automated
  triggers (the backend `batch` driver), never by interactive chat.

Then, regardless of entry point:

- `skills/plan-verifying/SKILL.md` — loop `pyengine validate` until clean.
- `skills/rendering-audition/SKILL.md` — `pyengine audition|release` + listening
  protocol.

Supporting content:

- `skills/jazz-composing/references/` — craft knowledge (harmony, melody,
  arrangement, groove, per-genre profiles, `contract.md`, cliché register,
  candidate→selection protocol). ~250 KB; read on demand.
- `skills/jazz-composing/templates/` — 10 style templates + `registry.md` (thin
  index) + `schema.md` (field contract). Read at Ideation to seed decisions.
- `skills/RED-FLAGS.md` — failure patterns that are easy to miss.
- `skills/abc-notation/` — **legacy** path, kept for the old `{abc, drums}`
  contract. Not used by `plan.json` v2.

**`archive/skills/` holds the previous structure** — the 14-level
`jazz-composition` orchestrator and its 8 per-level modules (`harmony`,
`melody-design`, `advanced-melody`, `vibes-mood`, `groove-rhythm`,
`arrangement`, `json-composition`, `midi-orchestration`). They are reference
material only. Do not start there, and do not treat their level numbering as the
current workflow.

## What the engine can actually render (check before promising a style)

Each template declares `engine_support`:

- `renderable` — whether `pyengine` can realize it **today**
- `engine_vibe` — which `VIBE_PRESETS` entry applies (or `null`)
- `tempo_range_effective` — intersection of the template's `tempo_range` with
  that vibe's range; the batch driver samples tempo from **this**, not from the
  raw range
- `blockers` — concrete missing engine capabilities when not renderable

At the time of writing only **2 of 10** templates are renderable: the engine has
one groove profile (`neo-soul-core`) and three vibe presets. The other eight
name groove profiles that do not exist yet. Batch generation enumerates only
`renderable: true` templates and reports what it skipped.

Consistency between this package and the engine is enforced by tests, not trust
— template chord symbols, tempo ranges, and `engine_support` declarations are all
gated. Three separate drifts (a chord the engine could not parse, a JSON shape
never documented, a tempo range outside the vibe) shipped undetected before those
gates existed.

## Ground rules

- **Craft and contract are single-source; only *workflow* may fork.**
  `composing-headless` is a workflow variant of `jazz-composing` — it must never
  duplicate craft knowledge or the contract, only override the interaction rules.
- **Interactive entry: if a required field is missing (key, tempo, meter, the
  chords, or whether the plan is locked) — ask; do not guess.** Headless entry
  overrides this and must decide, because nobody is there to answer.
- **Each phase stops at its own boundary.** Ideation does not write notation;
  `plan-verifying` does not invent musical content; `rendering-audition` does not
  re-compose.
- **Intent, not notes.** Never write absolute tick/ms values, per-note numeric
  velocity, or literal voicing pitches for `chords` voices — that is the engine's
  job, deterministic per `seed`. See `docs/DOCTRINE-NIAT-BUKAN-NOT.md`.
- A high rubric score (`skills/*/references/rubric.md`) is a floor, not a ceiling
  — see the last row of `skills/RED-FLAGS.md`.

## Why these skills exist, not just raw generation

`tests/` holds a real before/after evaluation, not a claim: fresh subagents ran
the same composition briefs once with no access to this package and once running
its skills end-to-end. See
`tests/results/2026-07-13-brief-01-02-armA-vs-armB.md` for the full comparison.
Two things came out of it that still matter:

- With-skill won a blind pairwise rubric comparison on both eval briefs — not by
  a landslide, and the no-skill baseline was a genuinely strong attempt, not a
  strawman. The margin came from traceable motif/arc development and a dedicated
  interaction map.
- The same eval found and fixed three real bugs in this package's own scripts and
  docs (tempo/meter tagging, a hardcoded 4/4 assumption, and a documented
  multi-voice ABC convention that silently produced 0 notes). **A clean validator
  pass does not mean the render worked** — always check the actual rendered
  output, not just an exit status.

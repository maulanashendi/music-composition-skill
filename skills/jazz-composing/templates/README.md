# Style templates — how they work

A **style template** is a reusable *recipe* the orchestrator names during
Ideation (the first phase of MDLC) to seed a `plan.json` with known-good
starting decisions: a harmonic palette, hook archetypes, groove profile, melody
phrasing per arc-phase, a drum skeleton, arrangement defaults, and anti-boredom
rules.

A template is a **starting kit, not a finished song.** It seeds decisions; it
never bypasses the full MDLC workflow (Ideation → Verification → Rendering)
or any gate/scorecard/quality review. The candidate→selection protocol still
runs — it now selects *from a template's options* instead of from scratch.

## Where a template sits in `plan.json`

A **template seeds the musical intent, not the concrete notes.** The canonical
contract is `plan.json` (schemaVersion 2), which holds the orchestrator's
decisions: arc phases, hooks, ensemble roles, key, tempo, sections, harmony
(chords + context), voices (who plays what), and dynamics. The engine then
renders this intent into concrete MIDI notes and audio—deterministically,
with a seed, so variations are reproducible.

A template provides a **chord vocabulary** and *signature moves*, not one
fixed progression. The Ideation skill picks specific chords from the palette
and varies them under `anti_boredom_rules`. Templating the recipe keeps
quality consistent while every song still comes out different.

## Anti-bloat: the 3-tier disclosure pattern

This mirrors `../../../archive/skills/groove-rhythm/references/groove-profiles.md` — the composing
brain only has to *name* a template; the recipe lives in one file, loaded on
demand. Nothing loads every template at once.

- **Tier 0 — `registry.md`** — the only file read by default. ~1 line per
  template: `id` + vibe + when-to-use. Small; always in context.
- **Tier 1 — `<id>.json`** — the full recipe. Loaded **only when that
  template is picked**. One file per template.
- **Tier 2 — reference by name, never copy** — a template points at
  `groove_profile: "neo-soul-core"`, at `cliche-register.md`, at
  `style-cheatsheets.md`. It does not restate their contents. Zero duplication.

Cost per compose = thin registry + one selected template file. Not N templates.

## How the orchestrator uses a template

1. **Ideation (jazz-composing skill)** — read the brief, read `registry.md`
   (thin), match the vibe, and **name one template**. If nothing fits well,
   compose without one rather than forcing a bad match — say so.
2. Load that one `<id>.json` and use it to **seed** `plan.json` (defaults,
   `harmony_palette`, a `hook_archetype`, phrasing, drum skeleton).
3. Continue building the plan: pick specific chords/notes **from the
   palette**, enforce variation via `anti_boredom_rules`.
4. Then the plan flows through Verification (plan-verifying) and Rendering
   (rendering-audition). Every gate, scorecard, and quality review still
   applies — the template skips none of them.

## Files

- `registry.md` — Tier 0 index. Read this first, always.
- `schema.md` — the field contract for a template JSON (types, what each field
  means, how it maps to `plan.json`).
- `<id>.json` — one file per template (Tier 1).

## Engine support (`engine_support`)

Batch generation uses templates to produce multiple compositions automatically.
Each template declares its **rendering readiness** via an `engine_support`
object that tracks compatibility with the current engine state:

- `renderable` — boolean. `true` if the template can be fully rendered to
  MIDI and audio by the engine; `false` if dependencies are missing.
- `engine_vibe` — string or null. The vibe profile name from the engine's
  `VIBE_PRESETS` (e.g., `neo-soul-core`), or `null` if no matching profile
  yet exists.
- `tempo_range_effective` — `[min, max]` or null. The intersection of the
  template's `defaults.tempo_range` with the vibe's supported tempo range,
  or `null` if no vibe is available.
- `blockers` — array of strings. Reasons the template is not yet renderable
  (e.g., `"missing vibe profile: neo-soul-core"`, `"groove out of range"`).

**Batch enumeration filters on `renderable: true`** — only templates marked
renderable are selected for mass generation. As of now, the engine has one
full groove profile (`neo-soul-core`), so only 2 of the 10 templates are
renderable; the rest are held at `renderable: false` until their profiles
are added to the engine. See `schema.md` for the field contract and how to
update it when a new vibe is added.

## Governance — adding a template

Same discipline as adding a groove profile: **add one row to `registry.md` and
one `<id>.json` file** that conforms to `schema.md`. Do not inline groove
numbers or chord theory that already lives in a reference — point at it by
name. A template that only restates an existing reference is not worth adding;
a template earns its place by encoding *style-specific decisions* (palette,
signature moves, hook shapes, variation rules) that would otherwise be
re-derived from scratch every song.

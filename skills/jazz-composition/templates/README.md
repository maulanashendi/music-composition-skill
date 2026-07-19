# Style templates — how they work

A **style template** is a reusable *recipe* the orchestrator names at Level 1
(konsep) to seed a `composition-plan.json` with known-good starting decisions:
a harmonic palette, hook archetypes, groove profile, melody phrasing per
arc-phase, a drum skeleton, arrangement defaults, and anti-boredom rules.

A template is a **starting kit, not a finished song.** It seeds decisions; it
never bypasses the 14-level pipeline or any gate/scorecard/L2 review. The
candidate→selection protocol still runs — it now selects *from a template's
options* instead of from scratch.

## Where a template sits (and why not `song.json`)

Two JSON layers exist in this package:

| Layer | File | Holds |
|---|---|---|
| Plan (the brain) | `composition-plan.json` | arc, hook, ensemble, feel, sections+chords, tension, phrasing |
| Notes (the output) | `song.json` | actual note events per voice |

Templates seed the **plan** layer, never the **notes** layer. Templating the
actual notes would make every song identical — the opposite of "not boring."
Templating the *recipe* keeps quality consistent while every song still comes
out different. The template supplies a chord **vocabulary** and *signature
moves*, not one fixed progression; the pipeline picks specific chords/notes
from it and varies them under `anti_boredom_rules`.

## Anti-bloat: the 3-tier disclosure pattern

This mirrors `../../groove-rhythm/references/groove-profiles.md` — the composing
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

1. **Level 1 (konsep)** — read the brief, read `registry.md` (thin), match the
   vibe, and **name one template**. If nothing fits well, compose without one
   rather than forcing a bad match — say so.
2. Load that one `<id>.json` and use it to **seed** `composition-plan.json`
   (defaults, `harmony_palette`, a `hook_archetype`, phrasing, drum skeleton).
3. Run the 14-level pipeline normally: pick specific chords/notes **from the
   palette**, keep the candidate→selection protocol (it now chooses among the
   template's options), enforce variation via `anti_boredom_rules`.
4. Every gate, scorecard, and L2 review still applies — the template skips
   none of them.

## Files

- `registry.md` — Tier 0 index. Read this first, always.
- `schema.md` — the field contract for a template JSON (types, what each field
  means, how it maps to `composition-plan.json`).
- `<id>.json` — one file per template (Tier 1).

## Governance — adding a template

Same discipline as adding a groove profile: **add one row to `registry.md` and
one `<id>.json` file** that conforms to `schema.md`. Do not inline groove
numbers or chord theory that already lives in a reference — point at it by
name. A template that only restates an existing reference is not worth adding;
a template earns its place by encoding *style-specific decisions* (palette,
signature moves, hook shapes, variation rules) that would otherwise be
re-derived from scratch every song.

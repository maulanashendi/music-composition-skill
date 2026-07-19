# Style template — field contract

The field contract for a `templates/<id>.json` file. A template seeds a
`composition-plan.json` (see `../assets/composition-plan-template.json`); every
field here maps to a plan decision the orchestrator would otherwise make from
scratch. Read `README.md` first for the 3-tier disclosure model and why
templates live at the plan layer, not `song.json`.

## Shape

```json
{
  "id": "neo-soul-midnight",
  "when_to_use": "one line — the same text that goes in registry.md",
  "style": "neo-soul",
  "defaults": {
    "key_options": ["F major", "Eb major"],
    "tempo_range": [68, 80],
    "meter": "4/4",
    "feel": "relaxed swung-16th, slightly behind the beat"
  },
  "groove_profile": "neo-soul-core",
  "harmony_palette": {
    "diatonic_core": ["Fmaj9", "Dm9", "Gm11", "Bbmaj7#11", "Am7"],
    "signature_moves": [
      "backdoor: Bbm7 -> Eb7 -> Fmaj9",
      "chromatic slide: Dm9 -> Db7#11 -> Cm9"
    ],
    "cadence_options": ["Gm11 -> C7alt -> Fmaj9", "tritone sub turnaround"],
    "avoid": ["plain ii-V-I with no reharm (see cliche-register)"]
  },
  "hook_archetypes": [
    {
      "name": "rise-and-settle",
      "rhythm": "syncopated pickup into a held target note",
      "contour": "rise a 6th, then settle to the 3rd",
      "first_appears": "Intro, bare"
    }
  ],
  "melody_phrasing": {
    "doubt":      { "note_lengths": "short phrases, long gaps", "contour": "gentle rise then fall, stop on the 6th", "placement": "behind the beat" },
    "hope":       { "note_lengths": "lines lengthen", "contour": "climb, reach higher each phrase", "placement": "on the beat" },
    "peak":       { "note_lengths": "sustained peak note", "contour": "hold the high target", "placement": "on the beat" },
    "acceptance": { "note_lengths": "sparse, resolving", "contour": "descend to tonic", "placement": "loosen, behind" }
  },
  "drum_skeleton": {
    "low_energy":  "kick on 1 & 3, snare laid-back on 2 & 4, hat sparse",
    "mid_energy":  "add off-beat hats (ghost, vel < 45), occasional kick pickup",
    "high_energy": "busier hat 16ths, snare accents, fill into the peak"
  },
  "arrangement_defaults": {
    "entrance_order": ["keys", "bass", "lead", "drums"],
    "layout_rules": "drop drums for the bridge; lead lays out during the keys turnaround"
  },
  "anti_boredom_rules": [
    "hook must reappear >=2x, always varied, never identical",
    ">=1 section drops one instrument for contrast",
    "no 2-bar loop repeats >4x without a fill or reharm",
    "velocity is never flat across a voice within a bar"
  ]
}
```

## Field contract

- `id` — string, kebab-case, unique. Matches the filename (`<id>.json`) and the
  registry row.
- `when_to_use` — one line. **Must be identical** to this template's line in
  `registry.md` (the registry is the copy the orchestrator reads first).
- `style` — string label, e.g. `neo-soul`, `lofi jazz`, `fusion`. Should match
  a `../../vibes-mood/references/style-cheatsheets.md` entry when one exists.
- `defaults` — starting values the orchestrator may adopt or override per brief:
  - `key_options` — array of candidate keys (`"F major"`, `"C# minor"`), plan
    picks one. Not a single locked key — the brief may steer it.
  - `tempo_range` — `[min, max]` BPM. Plan picks a concrete BPM inside it.
  - `meter` — default meter string `"n/d"`.
  - `feel` — prose feel descriptor, copied into `composition-plan.json.feel`.
- `groove_profile` — **a profile name** from
  `../../groove-rhythm/references/groove-profiles.md` (currently
  `neo-soul-core`). Reference by name only — never inline the tick/gate
  numbers. If a template needs a genuinely new pocket, add a named profile to
  `groove-profiles.md` first, then reference it here.
- `harmony_palette` — the style's chord **vocabulary**, not one progression:
  - `diatonic_core` — the everyday chords the style leans on.
  - `signature_moves` — the substitutions/turnarounds that give the style its
    identity; each written as a short chord chain. This is where "chord choices
    are appropriate" is enforced.
  - `cadence_options` — how phrases and sections resolve.
  - `avoid` — clichés to steer around; point at
    `../references/cliche-register.md` rather than restating it.
- `hook_archetypes` — 2–3 hook shapes to choose from, each `{name, rhythm,
  contour, first_appears}` mapping to `composition-plan.json.hook`. The plan
  picks one and develops it — this is the "has a hook" guarantee.
- `melody_phrasing` — phrasing defaults **keyed by arc-phase**
  (`doubt`/`hope`/`peak`/`acceptance` — match the phases the plan's `arc`
  actually uses), each `{note_lengths, contour, placement}`. Maps to each
  `sections[].phrasing`.
- `drum_skeleton` — drum density **keyed by section energy**
  (`low_energy`/`mid_energy`/`high_energy`), prose describing the pattern. The
  concrete GM `kick`/`snare`/`hihat`/`ride` events are written at Level 9 /
  Level 14 — this is the character, not the note grid.
- `arrangement_defaults` — `entrance_order` (voice names, first→last) and
  `layout_rules` (who sits out where). Seeds the interaction map; the actual
  map is still designed at Level 6.
- `anti_boredom_rules` — an array of **constraints** the finished piece must
  satisfy. These are requirements, not content — they connect directly to
  `../../RED-FLAGS.md` and the per-module rubrics. This is the mechanism for
  "not boring": variation is required, not hoped for.

## What a template does NOT store

- **No actual note events.** Pitches/velocities live in `song.json` at Level
  14, not here. A template that hardcodes notes defeats its own purpose.
- **No groove tick numbers.** Those live in `groove-profiles.md`; reference the
  profile name.
- **No cliché-register contents.** Point at `cliche-register.md`.
- **No single locked progression.** Store a palette + signature moves so every
  song built from the template can differ.

## Validation

There is no separate validator script for templates yet; the orchestrator
sanity-checks a template against this contract when it loads it. A template is
well-formed when: `id` matches filename and registry row; `groove_profile`
names a profile that exists in `groove-profiles.md`; `harmony_palette` holds a
vocabulary (not a single progression); at least one `hook_archetype` exists;
`melody_phrasing` keys cover the arc-phases the template targets; and
`anti_boredom_rules` is non-empty.

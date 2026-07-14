# music-composition-skill

**Tool 1 ("the brain") in the 2-tools architecture.** This package is a
portable, three-skill Agent Skills bundle that turns a brief, mood, or scene
into a locked musical idea, encodes it as valid ABC notation, and arranges +
converts it to a DAW-ready multi-track MIDI. It is deliberately independent
of any one engine or app — it reasons about music and hands off two
artifacts (ABC + a drum step-grid) that a separate rendering tool ("Tool 2",
the engine) turns into audio.

## `jazz-composition`, the single orchestrator, and its 8 modules

```
skills/jazz-composition  (single entry point + orchestrator, 14-level SOP)
   │
   ├─ harmony             (chord-scale, progression logic, voicing systems)
   ├─ melody-design        (phrasing, motif/hook, melody fundamentals)
   ├─ advanced-melody       (chromatic vocabulary, enclosures — Level 4 tahap 7-8)
   ├─ vibes-mood            (brief/mood → parameter, genre profile)
   ├─ groove-rhythm         (rhythm/subdivision, groove profiles, microtiming)
   ├─ arrangement           (form/dramaturgy, ensemble interaction, transitions)
   ├─ abc-notation          (plan → validated ABC)
   └─ midi-orchestration    (ABC + drum grid → arranged MIDI)
```

`skills/jazz-composition/SKILL.md` is the single entry point: it greets any
composition request, runs the 14-level workflow itself, and calls into
whichever of the 8 modules above is relevant to the level currently being
worked (see the 14-level → module table in `skills/jazz-composition/SKILL.md`).
There is no separate gateway or brief→plan/plan→ABC/ABC→MIDI skill split
anymore — the orchestrator owns the whole pipeline end to end, deferring
craft detail to modules per level.

## Artifact flow

```
run folder (progress.md, 01-brief.md … 14-review.md)  →  song.abc + drums.json  →  output.mid
        (skills/jazz-composition, all 14 levels)         (abc-notation,             (midi-
                                                            midi-orchestration)        orchestration)
```

- `composition-plan.json` — the idea contract: arc, key/tempo/meter,
  ensemble, bar-by-bar chords, hook, per-section phrasing/tension.
- `song.abc` — validated ABC notation for every **pitched** voice (lead,
  keys, bass, pads). Drums are never encoded in ABC in this package.
- `drums.json` — a step-grid (rows = drums, `x` = hit) with matching bar
  counts to the ABC, built section-by-section from the same plan.
- `song.mid` — the merged, multi-track output of the last skill: one track
  per pitched voice plus a channel-10 drum track.

## Who uses this package

Consumers are LLM/agent surfaces, not a single app: **Claude Code** (running
these skills directly), **GPT** or another chat LLM (via a flattened
composer-pack-style prompt), and **Hermes** (agent runtime). None of them
need API access to a specific engine to use this package — the three skills
are self-contained reasoning + validation + conversion steps.

## Downstream (rendering)

This package stops at MIDI (and the ABC/drum-grid artifacts that produce
it). Two downstream paths consume that output:

- **Primary: the `daw_generative` engine.** External HTTP contract —
  `POST /api/render {abc, drums?, mastering?}` — which realizes the ABC +
  drum grid itself (FluidSynth rendering, mastering) and returns audio. This
  package never calls that endpoint or any other engine/AI API; it only
  produces artifacts in the shape that contract expects.
- **Alternative: BandLab or any external DAW.** Import the `.mid` file this
  package's own `abc_to_midi.py` + `grid_to_midi.py` (music21 + pretty_midi)
  produce, then voice, mute, or edit tracks by hand.

Whichever path is used, this package's job ends at valid ABC + a
bar-matched drum grid (or the merged MIDI, if `skills/midi-orchestration`
ran) — it never renders audio and never calls an AI/LLM API itself.

## Origin

Consolidated 2026-07-13 from two prior "brains" so no craft was lost when
this package became the single source of composition truth:

- **`jazz-composition-designer`** — an archived portable skill package
  (English references) covering advanced microtiming, exact voicing,
  instrumental transitions, ensemble interaction, groove/meter, form and
  dramaturgy, loop development, and a comprehensive quality-control audit.
- **`compose-song`** — a Claude Code skill (Indonesian references) covering
  9 theory-reasoning modules (mood→parameter, theory-hierarchy declaration,
  cause-effect device catalog, compatibility review, structural levels,
  tension/release, ear-test protocol) plus a neo-soul/chill-jazz genre
  profile.

Both sources' substance now lives across `skills/vibes-mood/references/`,
`skills/arrangement/references/`, `skills/groove-rhythm/references/`,
`skills/harmony/references/`, and the other module folders under `skills/`
(the package was restructured 2026-07-14 from the earlier
gateway/idea-generator/notation-writer/orchestration split into the single
`jazz-composition` orchestrator + 8 modules above — see
`docs/migration-map.md` for the exact old-path → new-path mapping),
adapted to this package's own doctrine and pipeline (see each skill's
`SKILL.md` for exactly where each file is read in the workflow). Drums are
**always** a step-grid JSON in this package — never an ABC `%%MIDI
drummap` voice — regardless of which source a given reference file was
adapted from.

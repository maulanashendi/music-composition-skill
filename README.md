# music-composition-skill

**Tool 1 ("the brain") in the 2-tools architecture.** This package is a
portable, three-skill Agent Skills bundle that turns a brief, mood, or scene
into a locked musical idea, encodes it as valid ABC notation, and arranges +
converts it to a DAW-ready multi-track MIDI. It is deliberately independent
of any one engine or app — it reasons about music and hands off two
artifacts (ABC + a drum step-grid) that a separate rendering tool ("Tool 2",
the engine) turns into audio.

## The gateway and the three skills, in order

```
composition-gateway  →  jazz-idea-generator  →  abc-notation-writer  →  abc-to-midi-orchestration
   (route the request)    (brief → plan)          (plan → valid ABC)      (ABC → arranged MIDI)
```

0. **`composition-gateway`** — the single entry point. Greets any request to
   compose/write/arrange a track, works out where the person already is in
   the pipeline, and routes into the right skill below. Holds the
   fourteen-layer composition map (concept → detail), each layer pointing at
   the skill that executes it. Routes and maps; it does not compose, notate,
   or arrange itself.
1. **`jazz-idea-generator`** — turns a brief/mood/reference feel into a
   dramatic arc, hook, chord progression, groove, and phrasing plan, locked
   into `composition-plan.json`. Does not write notation.
2. **`abc-notation-writer`** — encodes a locked plan (or any already-decided
   progression/melody) into a portable, validated ABC subset. Does not
   invent musical content; validates with `scripts/validate_abc.py`.
3. **`abc-to-midi-orchestration`** — designs the interaction map (who leads/
   supports/answers/is silent, per section), writes the drum step-grid, and
   converts validated ABC + drum grid into a merged multi-track MIDI.

## Artifact flow

```
composition-plan.json  →  song.abc  +  drums.json  →  song.mid
   (jazz-idea-generator)    (abc-notation-writer,        (abc-to-midi-
                              abc-to-midi-orchestration)    orchestration)
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
bar-matched drum grid (or the merged MIDI, if `abc-to-midi-orchestration`
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

Both sources' substance now lives in `jazz-idea-generator/references/` and
`abc-to-midi-orchestration/references/`, adapted to this package's own
doctrine and pipeline (see each skill's `SKILL.md` for exactly where each
file is read in the workflow). Drums are **always** a step-grid JSON in this
package — never an ABC `%%MIDI drummap` voice — regardless of which source
a given reference file was adapted from.

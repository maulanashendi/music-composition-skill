# music-composition-skill

**Tool 1 ("the brain") in the 2-tools architecture.** This package is a
portable Agent Skills bundle — 3 skills covering the Music Development Life
Cycle (MDLC) — that turns a brief, mood, or scene into a locked musical idea,
encodes it as `plan.json` (schemaVersion 2), validates it, and renders +
audits it into a DAW-ready WAV/MIDI. It is deliberately independent of any
one engine or app — it reasons about music and hands off `plan.json` (a
niat-only contract: chord symbols, degrees, style+density, named groove
patterns — never voicing pitches, velocity, or off-grid timing) that
`pyengine`, a separate rendering engine, turns into audio deterministically.

## Install

The `skills/` folder is fully self-contained: it vendors its own
`skills/RED-FLAGS.md` and `skills/rendering-audition/references/audition-protocol.md`,
so nothing outside `skills/` (no root-level file, no `tests/`) is required
for the skills to work. Copying or symlinking `skills/` alone into another
project's skills directory is enough — `cp -r skills/ <target>` or
`ln -s $(pwd)/skills <target>/skills`.

## `jazz-composing`, `plan-verifying`, `rendering-audition` — 3 skill MDLC

```
skills/jazz-composing      (Brief -> Ideation -> Plan; writes plan.json)
skills/plan-verifying      (Verify; loops `pyengine validate`)
skills/rendering-audition  (Audition -> Review -> Release -> Remix; `pyengine audition|release`)
skills/abc-notation        (legacy path — ABC, superseded default is plan.json)
```

Doktrin: LLM menulis niat (chord symbol, degree, gaya+density, nama
pattern groove); `pyengine` menulis not (voicing, timing, humanization,
ber-`seed` deterministik). Lihat `docs/DOCTRINE-NIAT-BUKAN-NOT.md` — ini
membalik doktrin lama `json-composition` (kini di
`archive/skills/json-composition/`).

`skills/jazz-composing/SKILL.md` is the entry point for a new composition:
it runs the Brief → Ideation → Plan workflow and writes `plan.json`.
`skills/plan-verifying/SKILL.md` then loops `pyengine validate` against
that `plan.json` until it's structurally clean. `skills/rendering-audition/SKILL.md`
takes the validated plan through `pyengine audition`/`release` to produce
audio, runs the human-ear audition protocol, scores it against the rubric
checklist, and archives the release. `skills/abc-notation` remains as the
legacy path (plan → validated ABC) for callers not yet on `plan.json`.

## Artifact flow

```
run folder (progress.md, 01-brief.md ... plan.json)   ->   plan.json (verified)   ->   output.mid + render.wav + scorecard.md
        (skills/jazz-composing)                            (skills/plan-verifying)      (skills/rendering-audition)
```

- `plan.json` (schemaVersion 2) — niat lengkap: meta (title/vibe/key/
  tempo/meter/seed), sections, harmony (chord symbol), voices niat-level
  (melodi pitch+durasi, comping gaya+density, bass degree, drum pattern
  name).
- `verify-log.md` — hasil loop `pyengine validate` (error diperbaiki,
  warning ditinjau).
- `output.mid`/`render.wav`/`scorecard.md` — hasil `pyengine audition`/
  `release` + audit 3-lapis (mekanis/rubrik/telinga).

## Who uses this package

Consumers are LLM/agent surfaces, not a single app: **Claude Code** (running
these skills directly), **GPT** or another chat LLM (via a flattened
composer-pack-style prompt), and **Hermes** (agent runtime). None of them
need API access to a specific engine to use this package — the 3 MDLC
skills (plus the legacy `abc-notation` path) are self-contained reasoning +
validation + conversion steps.

## Downstream (rendering)

This package stops at `plan.json` (or, on the legacy path, at ABC + a
drum-grid). Two downstream paths consume that output:

- **Primary: `pyengine`, via `plan.json`.** `skills/plan-verifying` loops
  `python -m pyengine validate <plan.json>` until it's clean; `skills/rendering-audition`
  then calls `python -m pyengine audition`/`release` (CLI) — or the
  `daw_generative` engine's equivalent HTTP contract, see
  `skills/rendering-audition/references/engine-http-alternative.md` — to
  produce audio deterministically (seeded voicing, timing, humanization).
  This package never calls `pyengine` or any engine/AI API itself; it only
  produces artifacts (`plan.json`) in the shape the contract expects.
- **Alternative (legacy): ABC + drum-grid, or BandLab/any external DAW.**
  Callers not yet on `plan.json` can still use `skills/abc-notation` to
  produce validated ABC, then import the `.mid` this package's own
  `abc_to_midi.py` + `grid_to_midi.py` (music21 + pretty_midi) produce, or
  hand it to any external DAW to voice, mute, or edit tracks by hand.

Whichever path is used, this package's job ends at a validated `plan.json`
(or, on the legacy path, valid ABC + a bar-matched drum grid) — it never
renders audio and never calls an AI/LLM API itself.

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

Both sources' substance now lives across `skills/jazz-composing/references/`
(niat-level theory, arrangement, groove, harmony, melody — consolidated
from the earlier `vibes-mood`/`arrangement`/`groove-rhythm`/`harmony`
module split) and `skills/rendering-audition/references/` (audit,
scorecard, ear-check). The package went through two restructurings: 2026-07-14
took the earlier gateway/idea-generator/notation-writer/orchestration split
into a single `jazz-composition` orchestrator + 8 modules; 2026-07-18 took
that into the current 3-skill MDLC structure above (the pre-2026-07-18
modules now live under `archive/skills/`) — see `docs/migration-map.md`
for the exact old-path → new-path mapping of both rounds, adapted to this
package's own doctrine and pipeline (see each skill's `SKILL.md` for
exactly where each file is read in the workflow). Drum intent is expressed
as a named groove pattern in `plan.json` (realized deterministically by
`pyengine`) on the default path, or as a step-grid JSON alongside ABC on
the legacy `abc-notation` path — never an ABC `%%MIDI drummap` voice —
regardless of which source a given reference file was adapted from.

# Scorecard — Neo-soul listening trials (2026-07-30)

## Scope and honesty note

This run is **not** the full phase-by-phase MDLC artifact trail (no
`02-konsep.md`/`04-harmoni.md`/etc.). It was driven directly in chat as an
end-to-end proof that the `plan.json → pyengine validate → pyengine
release → human ear` pipeline actually works against the real `pyengine`
in `maulanashendi/daw_generative` — not a simulation. Engine identity was
verified independently: local clone HEAD (`04c55c37...`) and a git blob
hash of `contracts.py` both matched the GitHub API directly (not through
the session's git proxy).

Only `neo-soul-midnight` and `lofi-jazzhop` are `renderable: true` today
(see `skills/jazz-composing/templates/*.json` `engine_support` — verified
against the real `GROOVE_LIBRARY`/`VIBE_PRESETS` in `pyengine`, not just
trusted from the JSON declaration). All three plans below use custom
briefs on the `neo-soul` vibe rather than literally invoking the
`neo-soul-midnight` template's `meta.template` field.

## Plans in this folder

1. **`01-setelah-ragu.plan.json`** — F major, 74 BPM, Rhodes-led,
   doubt→acceptance arc seeded from the `neo-soul-midnight` template's
   harmony/hook/phrasing recipe. First real render; found and fixed a
   bass-octave-register bug in this session's own composing (not the
   template's fault) before it was documented — `contract.md` already
   warned about this, it was just missed on the first pass.
2. **`02-jam-malam-dorian.plan.json`** — D minor/Dorian, 82 BPM, guitar +
   sax call-and-response with double-stops, built from a live-jam neo-soul
   reference brief (laid-back groove, extended/altered chords, Dorian
   phrasing).
3. **`03-angkat-dari-bawah-final.plan.json`** — Bb minor, 70 BPM, modulates
   to Db major mid-piece. **This is the revised/final version** after two
   real listening-driven fixes (see below); comp uses `rhodes` (not
   `pad-strings`) and lead uses `acoustic-guitar` with `legato`/`tenuto`
   only (no `accent`).

## L1 — mechanical

All three: `pyengine validate` → 0 errors before render (warnings reviewed
per-note, not blanket-ignored — see below). `pyengine release` produced
non-silent WAV (RMS -15.5 to -16.9 dB, peak -1.4 to -1.5 dB, all in the
healthy range), duration within ~2s of the bar-count/tempo target in every
case.

## L2 — rubric / self-assessment (not a fresh reviewer)

Chord-tone target misses were treated as findings, not noise: 5 raised in
plan 1's first validate pass, 4 retargeted to the correct chord tone, 1
kept deliberately (a sustained peak note held static while the harmony
underneath moves — this is literally what this template's own
`melody_phrasing.peak` field asks for). Plans 2 and 3 validated clean on
the first pass.

## L3 — human ear (real, in this session — not simulated)

Actually listened to by the user, iteratively, across several rounds:

- **Finding 1**: comping on `pad-strings` produced an audible
  shimmer/warble artifact. Root-caused to the specific GM preset
  (`FluidR3_GM.sf2` program 89 = `Warm Pad`, confirmed via `fluidsynth`
  `inst 1`) — chorus/detune baked into that patch, most audible on long
  sustained notes. **Fixed** by swapping comp to `rhodes` (A/B'd, same
  plan otherwise) — now written up in `skills/RED-FLAGS.md`.
- **Finding 2**: lead (`alto-sax`) was too loud/piercing. Root-caused to
  `lead` being the loudest role by design (velocity 78-92 vs `chords`
  58-72 and `pad` 34-46) compounded by `artic: accent` (×1.22) on
  sustained notes, with no per-instrument mix/gain control in the render
  pipeline to correct it after the fact. **Fixed** per user request by
  swapping lead to `acoustic-guitar` (for a slower-jazz feel) and changing
  `accent` → `tenuto` on the affected notes. Also written up in
  `skills/RED-FLAGS.md`.
- Also tested (not a defect, a genuine finding): swapping the *default*
  soundfont from `FluidR3_GM` to `musescore-general-soundfont-lossless`
  gave a spectrally measurable but small difference (~1.3 dB in the >6kHz
  band) — not enough on its own to resolve the "sounds unfinished"
  complaint that `daw_generative`'s own
  `docs/unfinish-job/2026-07-29-vst-render-backend-HANDOFF.md` had already
  diagnosed as a timbre problem. That handoff's "Tangga 2/3" (dedicated
  sampled instruments via `sfizz`/VST-bounce) remain undone and are
  engine-repo work, out of scope here.

## Production-readiness verdict (asked directly, answered directly)

**Not production-ready.** Concretely: 8/10 style templates still cannot
render at all (missing `GROOVE_LIBRARY` entries); no per-instrument
mix/gain/EQ control exists in the render pipeline; the real timbre fix
(Tangga 2/3 in the `daw_generative` handoff) is undesigned code, not just
undone config. What *did* get closed out this session: the two listening
findings above are now written back to `skills/RED-FLAGS.md` so the next
person (or the next session) doesn't rediscover them from zero.

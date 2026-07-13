# music-composition-skill — operating instructions

This package is three Agent Skills meant to be read and run **in this
order** for any composition task — never skip ahead or run them out of
order:

1. `jazz-idea-generator/SKILL.md` — brief → locked `composition-plan.json`
2. `abc-notation-writer/SKILL.md` — plan → validated ABC
3. `abc-to-midi-orchestration/SKILL.md` — ABC → arranged, DAW-ready MIDI

See `README.md` for the architecture/positioning (this package is Tool 1,
"the brain"; rendering to audio is a separate downstream engine) and
`RED-FLAGS.md` for failure patterns that are easy to miss.

## Why these skills exist, not just raw generation

`tests/` holds a real before/after evaluation, not a claim: fresh subagents
ran the same composition briefs once with no access to this package and
once running its skills end-to-end. See
`tests/results/2026-07-13-brief-01-02-armA-vs-armB.md` for the full
comparison. Two things came out of it that matter for how you should treat
this package:

- With-skill won a blind pairwise rubric comparison on both eval briefs —
  not by a landslide, and the no-skill baseline was a genuinely strong
  attempt, not a strawman. The margin came from traceable motif/arc
  development and a dedicated interaction map, not from the no-skill
  attempt being broken.
- The same eval also found and fixed three real bugs in this package's own
  scripts and docs (tempo/meter tagging, a hardcoded 4/4 assumption, and a
  documented multi-voice ABC convention that silently produced 0 notes).
  **A clean `validate_abc.py` pass does not mean the MIDI conversion
  worked** — always check the actual rendered MIDI (track count, notes per
  track, tempo/time-signature), not just the validator's exit status.

## Ground rules that apply to all three skills

- If a required field is missing (key, tempo, meter, the actual chords —
  or whether the plan is even locked yet), **ask; do not guess.** Each
  SKILL.md says this individually; it's restated here because it's the
  single most common way these skills get used wrong.
- Each skill stops at its own boundary — `jazz-idea-generator` does not
  write notation, `abc-notation-writer` does not invent musical content,
  `abc-to-midi-orchestration` does not invent chords or melodies. Handing
  a downstream skill an undecided input is a sign the upstream skill's
  step was skipped, not a shortcut.
- A high rubric score (`abc-to-midi-orchestration/references/quality-control.md`)
  is a floor, not a ceiling — see `RED-FLAGS.md`'s last row.

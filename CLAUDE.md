# music-composition-skill — operating instructions

**Start at `skills/jazz-composition/SKILL.md`** — the single entry point and
orchestrator. It greets any composition request, runs the 14-level workflow
itself, and calls into whichever module below is relevant to the level
currently being worked; it is not a router that hands off to separate
brief→plan/plan→ABC/ABC→MIDI skills anymore.

The 8 modules it draws on for level detail (never run standalone out of
order — the orchestrator decides when each is relevant):

- `skills/harmony/SKILL.md`
- `skills/melody-design/SKILL.md`
- `skills/advanced-melody/SKILL.md`
- `skills/vibes-mood/SKILL.md`
- `skills/groove-rhythm/SKILL.md`
- `skills/arrangement/SKILL.md`
- `skills/abc-notation/SKILL.md`
- `skills/midi-orchestration/SKILL.md`

See `README.md` for the architecture/positioning (this package is Tool 1,
"the brain"; rendering to audio is a separate downstream engine) and
`skills/RED-FLAGS.md` for failure patterns that are easy to miss.

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

## Ground rules that apply to the orchestrator and all 8 modules

- If a required field is missing (key, tempo, meter, the actual chords —
  or whether the plan is even locked yet), **ask; do not guess.** Each
  SKILL.md says this individually; it's restated here because it's the
  single most common way these skills get used wrong.
- Each module stops at its own boundary — `vibes-mood`/`harmony`/
  `melody-design`/`advanced-melody`/`groove-rhythm`/`arrangement` do not
  write notation, `abc-notation` does not invent musical content,
  `midi-orchestration` does not invent chords or melodies. Handing a
  downstream module an undecided input is a sign an earlier level's step
  was skipped, not a shortcut.
- A high rubric score (`skills/*/references/rubric.md`, one per module) is
  a floor, not a ceiling — see `skills/RED-FLAGS.md`'s last row.

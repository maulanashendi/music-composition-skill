# Eval run 2026-07-13 — with-skill vs no-skill, 2 briefs

Methodology: two fixed briefs (`tests/briefs/`), each run once with a fresh
subagent given NO access to this skill package (Arm A — general knowledge
only) and once with a fresh subagent following the three skills end-to-end
for real (Arm B). Automated gate (`validate_abc.py` + a manual MIDI
track/note/tempo check) on all four outputs, then a blind pairwise judge per
brief scoring both versions against `quality-control.md`'s /64 rubric
without being told which arm produced which file. Full transcripts of every
subagent run are in this run's tool-call history; only the summarized
outputs are kept here as durable artifacts.

## Automated gate (layer 1)

All four `song.abc` files passed `validate_abc.py` with 0 errors/0 warnings,
and all four `song.mid` files contain real, non-empty note data on every
track (44-88 notes per pitched track, 150-229 drum hits). **The validator
passing is not sufficient evidence the pipeline works end-to-end** — see
bug #1 below, found precisely because "validator passed" and "MIDI has
notes" were checked as two separate, independent facts.

| Run | ABC validator | MIDI tracks/notes |
|---|---|---|
| brief-01 armA | PASS | 4 tracks, 44/71/44/196 notes |
| brief-01 armB | PASS | 4 tracks, 24/88/30/150 notes |
| brief-02 armA | PASS | 4 tracks, 48/182/56/229 notes |
| brief-02 armB | PASS | 4 tracks, 46/75/42/182 notes |

## Blind judge score (layer 2, quality-control.md §17, /64)

| Brief | Arm A (no-skill) | Arm B (with-skill) | Winner |
|---|---|---|---|
| 01 — neo-soul, doubt→acceptance | 45/64 | 49/64 | B, by 4 |
| 02 — fusion 7/8, urgency→release | 49/64 | 55/64 | B, by 6 |

With-skill won both blind comparisons, on motif/hook development that's
traceably tracked through the piece (fragment → statement → sequence →
return), harmonic/bass contour tied to the dramatic arc, and a dedicated
interaction map. No-skill's compositions were a genuinely strong baseline
(not a strawman) and in both runs had **better-realized MIDI dynamics**
(real velocity variation, some microtiming) than with-skill's flat
velocity=90 output — a real gap in this package's own converter, not a
win for "no skill," see bug #4.

## Human-ear layer (layer 3)

Not run in this pass — no audio was rendered (see `tests/human-ear-protocol.md`
for how to do this later). Every "confidence" caveat in every subagent
report explicitly says the same thing: whether either version is actually
*enjoyable* to listen to was not and cannot be verified by an agent reading
notation. This is disclosed, not glossed over.

## Real defects found (not style disagreements)

Found independently, by different fresh subagents/judges, across both
briefs — these are reproducible package bugs, not one-off mistakes:

1. **`abc-notation-writer/references/abc-syntax.md`'s documented multi-voice
   layout (one `V:id` header per system) does not work with
   `abc-to-midi-orchestration/scripts/abc_to_midi.py`**, which needs the
   voice marker repeated on every content line — otherwise it silently
   produces 0 notes for that voice while `validate_abc.py` still reports 0
   errors. Hit independently on both briefs by different subagents.
2. **`abc_to_midi.py` mis-tags the merged MIDI's tempo and time signature.**
   Confirmed twice: brief-01 armB tagged 120 BPM/4-4 instead of the
   ABC-implied 78 BPM/4-4; brief-02 armB tagged 120 BPM/4-4 instead of the
   ABC-implied 80 BPM/7-8. Total duration is still correct by coincidence of
   a separate scaling path, which is exactly why nobody's own duration check
   caught it — a DAW's piano roll would show garbled note values against the
   wrong grid.
3. **`abc-to-midi-orchestration/scripts/grid_to_midi.py` hardcodes
   `beats_per_bar = 4`**, invisible in 4/4 pieces but a real desync bug for
   any non-4/4 meter (confirmed on the 7/8 brief).
4. **`abc_to_midi.py` does not implement the microtiming/velocity groove
   described in `references/groove-profiles.md`/`advanced-microtiming.md`**
   — every pitched note in every with-skill run has flat velocity 90 and no
   timing offset. The reference docs describe per-role pocket profiles the
   script never applies. This is the reason no-skill's hand-rolled scripts
   sounded more dynamic on paper (per MIDI inspection) in this eval.

See the parent conversation / task list for the decision on whether to fix
these now (touches files another concurrent session may also be editing as
part of the 2-tools architecture work) or file them as follow-ups.

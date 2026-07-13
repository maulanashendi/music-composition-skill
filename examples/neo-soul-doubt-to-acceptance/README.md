# Example: neo-soul, doubt to acceptance

A complete, real run of all three skills against `brief.md`, kept as an
onboarding fixture and a regression reference (re-run the pipeline on
`song.abc` + `drums.json` after a script change and diff the result
against `song.mid` here).

- `brief.md` — the input brief.
- `composition-plan.json` — jazz-idea-generator's output.
- `song.abc` — abc-notation-writer's output (`validate_abc.py` clean).
- `drums.json`, `interaction-map.md` — abc-to-midi-orchestration's
  arrangement decisions.
- `pitched.mid`, `drums.mid`, `song.mid` — abc-to-midi-orchestration's
  rendered MIDI (merged = `song.mid`).
- `quality-report.md` — the filled-in quality-control.md §18 audit,
  **50/64** (see the file for the per-domain breakdown and disclosed weak
  spots — nothing is smoothed over).

This example was generated before three bugs were found and fixed in this
package (see `../../tests/results/2026-07-13-brief-01-02-armA-vs-armB.md`);
the MIDI files here were regenerated after the fix, so `song.mid`'s
tempo/time-signature tag is correct (78 BPM / 4-4), not the original run's
120 BPM / 4-4.

This is a worked example, not a claim that the piece is "good" — see
`tests/human-ear-protocol.md` for the layer of judgment this package
cannot make for you.

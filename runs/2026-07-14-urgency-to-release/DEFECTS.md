# Defects found while running this SOP (Undertow, brief-02)

Recorded here per `CLAUDE.md`'s rule — found while composing, worked
around in this run folder, `skills/` left untouched.

1. **Dangling reference: `midi-orchestration/SKILL.md` points to a
   `references/groove-meter.md` that doesn't exist in that module.**
   `skills/midi-orchestration/SKILL.md:56` and `:72` say
   "`references/groove-meter.md` is the deeper reference" (relative to
   `midi-orchestration/`'s own `references/` dir), but the file only
   exists at `skills/groove-rhythm/references/groove-meter.md`
   (confirmed: `skills/midi-orchestration/references/` has no
   `groove-meter.md`; `skills/groove-rhythm/SKILL.md:93` links to it
   correctly with a relative path inside its own module). A reader
   following the `midi-orchestration/SKILL.md` link literally gets a
   404/no-such-file. Workaround used in this run: read
   `skills/groove-rhythm/references/groove-meter.md` directly (found via
   `find`), used its §15 (odd meter grouping guidance) to justify the
   7/8 = 4+3 grouping decision recorded in `05-groove.md`.

2. **`grid_to_midi.py` doesn't implement the accent/ghost-note characters
   its own template documents.** `skills/midi-orchestration/assets/
   drum-grid-template.json`'s `_comment` says pattern characters are
   `'x' = hit, 'X' = accent, 'g' = ghost, '.' = rest`, but
   `skills/midi-orchestration/scripts/grid_to_midi.py:41` only checks
   `if ch != "x": continue` — any `'X'` or `'g'` character in a pattern
   row is silently treated as a rest (dropped), not rendered with
   different velocity as the template's own comment implies. This
   package's other velocity control (`humanize_velocity`, per-voice
   `base_velocity`) still works fine; it's specifically the promised
   per-hit accent/ghost characters that are dead. Workaround used in
   this run: `09-drums.json`/`drums.json` only use lowercase `'x'` for
   every hit, relying on `base_velocity` + `humanize_velocity` for
   dynamic variation instead of per-note accent/ghost marks (no accent
   or ghost characters were written, so nothing was silently dropped in
   this specific file — but the mismatch between template documentation
   and actual script behavior would bite the next person who takes the
   template's comment at face value).

# Defects / ambiguities found while running the skill (not fixed here)

Per task instructions: do not fix the skill itself, just record and work
around. Nothing here blocked completion.

1. **`skills/jazz-composition/references/run-folder-protocol.md:16`** —
   the folder listing says `04-melody.abc (atau .md untuk artefak
   non-notasi)`, but `SKILL.md`'s Tahap 5-8 (lines ~118-136) all point to
   the *same* artefak `04-melody.abc` for motif, target-tones, full
   melody-building, and outside material — i.e. a single file is supposed
   to capture 4 sub-stages of design reasoning *and* be valid ABC. In
   practice these two goals conflict: a single well-formed ABC tune can't
   also carry prose per-stage commentary without becoming multiple `X:`
   blocks (which most ABC parsers/validators treat as separate tunes, or
   which `validate_abc.py` may reject depending on strictness). Workaround
   used here: `04-melody.abc` in this run is a **design-note file** (prose
   + illustrative ABC fragments, several small `X:` snippets), not a
   single validated tune — the actual validated, final melody lives in
   `song.abc`'s `V:1`. This matches the parenthetical "atau .md" escape
   hatch, but the skill doesn't say which of the two modes Level 4 should
   default to, so a future run could reasonably do it differently.

2. **No functional defect found in the scripts.** `validate_abc.py`,
   `abc_to_midi.py`, and `grid_to_midi.py` all ran cleanly on the first
   try against `song.abc` / `drums.json` (adapted from the pre-existing
   `examples/neo-soul-doubt-to-acceptance/` fixture for this same brief).
   Sync check (pitched end ≈73.85s vs. drums end ≈69.79s — the ~4s gap is
   expected, since bar 24 has no drum pattern by design, see
   `09-drums.json`), mono check (Sax/Bass max-poly 1), and tempo/meter tag
   (78 BPM, 4/4) all came back correct — no self-healing retry loop was
   needed this run.

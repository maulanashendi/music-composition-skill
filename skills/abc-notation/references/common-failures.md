# Common failures in AI-generated ABC (and how to fix them)

AI-generated ABC frequently sounds fine but fails strict parsers like music21. The output is only useful if it parses, so these are the errors to prevent while writing and to target during the self-heal loop. Each entry: the symptom, the cause, the fix.

## 1. Bar duration mismatch (the #1 killer)

- **Symptom:** parser rejects a bar; renderer shows a blank or shifted measure.
- **Cause:** the notes and rests in a bar don't sum to the meter. With `M:4/4` and `L:1/8`, each full bar must total 8 eighth-note units. A stray or missing duration throws the whole bar off.
- **Fix:** count every bar explicitly as you write. `C2 D2 E2 F2` = 2+2+2+2 = 8 ✓. `C2 D2 E2 F` = 7 ✗. When a bar is wrong, adjust the offending note's length or add a rest (`z`) to fill — don't rewrite the bar from scratch.

## 2. Unclosed tie or slur

- **Symptom:** parse error in music21, often reported past the actual location.
- **Cause:** a tie `-` with no note to tie into (e.g. tying into a rest), or a slur `(` with no closing `)`.
- **Fix:** every `-` must sit between two notes of the *same pitch*; never tie a note into a rest (`z`). Every `(` needs a matching `)`. Ties that cross a barline are fine (`C4- | C4`) but both ends must be real notes.
- **Note:** `validate_abc.py` checks duration and structure but does **not** catch every semantic tie error (e.g. a tie into a rest). music21 will. So when MIDI is the target, run a music21 parse as the final check — the validator is the fast first pass, music21 is the authority.

## 3. Blank line inside a tune read as a tune separator

- **Symptom:** only the first section renders; everything after a blank line disappears.
- **Cause:** ABC treats a blank line as the end of a tune. Using blank lines to visually separate sections silently truncates the piece.
- **Fix:** never leave a blank line inside one tune. Separate sections with `%` comment lines (e.g. `% --- B section ---`) or just a newline with content. Keep exactly one tune per file.

## 4. Inconsistent or ambiguous note lengths

- **Symptom:** durations render wrong even though the bar "looks" right.
- **Cause:** mixing implicit and explicit lengths carelessly, or fractional lengths the parser reads differently than intended (`C/` vs `C/2`, `C3/2`).
- **Fix:** be explicit. With `L:1/8`: `C`=eighth, `C2`=quarter, `C4`=half, `C/2`=sixteenth, `C3/2`=dotted-eighth. Prefer the unambiguous forms.

## 5. Voice declared after use / missing voice header

- **Symptom:** multi-voice file fails or collapses voices together.
- **Cause:** a `[V:Bass]` used before `V:Bass` was declared in the header.
- **Fix:** declare every voice in the header (before the first `K:`-terminated header block ends) and reference them consistently. Keep voice IDs simple (`Melody`, `Keys`, `Bass`), no spaces.

## 6. Pickup (anacrusis) bar mishandled

- **Symptom:** the first and/or last bar flagged as wrong duration.
- **Cause:** a pickup bar is intentionally short, and its complementary final bar is short by the same amount — but one side is written wrong.
- **Fix:** a valid pickup + final bar together sum to one full bar. If bar 1 is a 2-unit pickup, the final bar must be 6 units (with `L:1/8`, `M:4/4`). The validator allows this pattern; make sure both halves are correct.

## 7. Meter/tempo header typos

- **Symptom:** immediate parse failure at the header.
- **Cause:** `M:` or `Q:` malformed (`M:44`, `Q:120` without the `1/4=`).
- **Fix:** `M:4/4`, `Q:1/4=120`. Follow the exact forms in `abc-syntax.md`.

## 8. Voice marker not repeated on every line (validator passes, converter produces 0 notes)

- **Symptom:** `validate_abc.py` reports 0 errors, but `scripts/abc_to_midi.py` writes a track with 0 notes for a voice (or the voice's later bars are missing from the MIDI).
- **Cause:** `abc_to_midi.py` extracts each voice's body with a per-line regex (`^\[V:id\]`) — only lines that literally start with `[V:id]` are captured. A second consecutive line of that voice's music, written without repeating `[V:id]` (relying only on the initial switch, as `abc-syntax.md`'s own §14 example used to show), is silently dropped. `validate_abc.py` still passes because it checks general ABC structural validity, not this specific converter's per-line parsing assumption.
- **Fix:** repeat the `[V:id]` marker at the start of *every* content line for that voice, not only at the first line or at switch points. When in doubt, prefix every line of music with its `[V:id]`.

## 9. Bare `z5`/`Z5` rest fails the downstream abcjs renderer

- **Symptom:** `validate_abc.py` reports 0 errors and music21 parses the file fine, but the downstream render engine (which gates ABC through the `abcjs` library) rejects the file with `"Duration not representable"`.
- **Cause:** `abcjs` has a narrow, isolated bug: a bare rest token `z5` or `Z5` (rest letter directly followed by exactly the digit `5`) fails to parse in `abcjs`, while every other count (`z1`, `z2`, `z3`, `z4`, `z6`, `z7`, `z8`, `z9`, `z10`, ...) parses fine. This is specific to `abcjs`, not a music21 or `validate_abc.py` limitation — that's why it slips past both of this package's checks.
- **Fix:** `validate_abc.py` now catches this and reports it as an error. Split the `z5` into two rest tokens whose durations add up to 5, e.g. `z2 z3` or `z4 z1` (`z1` is the same as a bare `z`). Total bar duration is unchanged, so no other note needs adjusting. Example: `A,2 z5 =E,` (2+5+1=8) becomes `A,2 z2 z3 =E,` (2+2+3+1=8).

## The self-heal loop in practice

Don't rewrite the whole file when validation fails. Read the error's line number and reason, fix that one issue, re-run the validator, repeat. Most failures are a single bad bar or an unclosed tie — a targeted fix is faster and doesn't introduce new errors. Only after `validate_abc.py` reports 0 errors (and, if MIDI is the target, music21 parses it cleanly) is the file ready.

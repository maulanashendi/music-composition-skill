---
name: abc-notation
description: Encode a finalized musical idea into valid, parseable ABC notation and validate it before it goes to MIDI. Use whenever someone has a locked composition idea — a composition-plan.json, a chord progression, a bassline, or a melody they've decided on — and wants it written as ABC, or when AI-generated ABC keeps failing to parse (bar-count mismatches, unclosed ties/slurs, wrong note lengths) and needs fixing or validating. Trigger on "write this as ABC," "turn this progression into ABC," "my ABC won't parse into MIDI," "validate this ABC," or handing over a composition plan to notate. This skill does the encoding and validation; it does not brainstorm musical ideas (that's jazz-composition) or render MIDI.
---

> **LEGACY (2026-07-16).** Jalur output default paket ini kini **JSON** —
> gunakan `../json-composition/SKILL.md`. Skill ABC ini dipertahankan hanya
> untuk backward-compat (engine masih menerima `POST /api/render {abc,drums?}`),
> BUKAN untuk komposisi baru. Jangan pakai untuk pekerjaan baru kecuali diminta
> eksplisit menargetkan jalur ABC.

# ABC Notation Writer

Encode a **decided** musical idea into ABC notation that parses cleanly on the first or second try. The value of this skill is reliability: AI-generated ABC often looks fine but fails strict parsers (music21) on subtle structural errors. This skill writes a constrained, portable ABC subset and validates it before hand-off.

This skill does **not** invent musical content. If the idea isn't decided yet, that's `jazz-composition`'s job — stop and say so rather than guessing chords or melodies.

## Input

Best input is a filled `composition-plan.json` (produced by `jazz-composition`). But this skill also accepts a raw progression, bassline, or melody the person already committed to (from jamming, a reference, or another session). If a critical field is missing — key, tempo, meter, or the actual notes/chords per bar — **ask; do not guess**. Guessing is how misaligned notation happens.

## Workflow

### Step 1 — Read the plan and confirm the essentials

Confirm you have: key, tempo (Q:), meter (M:), default note length (L:), the ensemble/voices, and bar-by-bar content for each voice. Map each `composition-plan.json` field to its ABC header field. If the plan gives chords but no melody notes yet and the person wants a lead sheet (chords + melody), confirm whether they want you to write a melody consistent with the plan's hook description, or just chord-symbol changes.

### Step 2 — Write a constrained ABC subset

Read `references/abc-syntax.md` for exact syntax (headers, octaves, durations, chord symbols, ties, repeats, multi-voice). Write portable core syntax first; add advanced features only when needed. The constrained subset below is what parses reliably — deviating from it is the usual cause of failures:

- Always include the required headers: `X: T: M: L: Q: K:` and a `V:` per voice.
- Every bar's note+rest durations must sum to exactly what `M:` and `L:` imply. This is the single most common failure — count each bar as you write it.
- Close every tie (`-`) and slur (`()`); an unclosed one breaks the parse.
- Keep one tune per file. A blank line inside a tune is read as a tune separator by many parsers — use `%` comment lines or continuation, not blank lines, to separate sections.
- Put chord symbols in double quotes before the note: `"Cm9" C2`.
- Declare all voices in the header before their first use.

Read `references/common-failures.md` before writing — it lists the specific LLM-generated ABC errors that break music21, with the fix for each. This is the payoff of the skill; don't skip it.

### Step 3 — Handle drums separately (do not force them into ABC)

ABC is built for pitched, diatonic material. Drums are not pitched — they map to GM percussion on MIDI channel 10, and both abcjs and music21 handle ABC percussion poorly. Do **not** try to write the drum kit as ABC notes. Instead, keep the pitched voices (lead, keys, bass) in ABC, and specify drums as a separate step-grid to be programmed downstream (in the DAW or a grid→MIDI converter). State this split explicitly in the output so the drum layer isn't silently lost. See `references/drums-and-abc.md`.

### Step 4 — Validate, and self-heal on failure

Run the validator:

```bash
python3 scripts/validate_abc.py <file.abc>
```

It checks required headers, per-bar duration, ties/slurs, tuplets, repeats, and multi-voice structure. If it reports errors:

1. Read the specific error (line number + reason).
2. Fix that exact issue — most often a bar whose durations don't sum correctly, or an unclosed tie.
3. Re-run. Repeat until it passes.

This is the **self-healing retry loop**: feed the parser's error back into a targeted fix rather than rewriting the whole file. It's the same principle that stabilizes the Gemini→ABC→music21 pipeline — the parser's own error message tells you precisely what to repair. Don't declare success until the validator passes with 0 errors.

If music21 is available and the target is MIDI, a second check is to attempt `music21.converter.parse(open('file.abc').read())` — the validator catches structural errors, but music21 is the actual downstream consumer, so a clean music21 parse is the real green light.

See `../RED-FLAGS.md` for common excuse-vs-reality failure patterns in this domain — a clean validator run is not the same as a correct render.

### Step 5 — Deliver

Output the validated `.abc` file, note the validator result, and flag anything handled outside ABC (drums, any feature a target renderer may not support). Say the ABC is ready for MIDI conversion — the ABC→MIDI/orchestration step is a separate skill and not done here.

## References

- `references/abc-syntax.md` — full ABC syntax for lead sheets and compact scores: headers, notes/octaves, durations, chord symbols, ties/slurs, repeats, tuplets, multi-voice. The syntax authority.
- `references/common-failures.md` — the specific ways AI-generated ABC breaks music21 and how to fix each; read before writing.
- `references/drums-and-abc.md` — why drums stay out of ABC and how to hand them off as a step-grid. Drums are **always** a step-grid JSON in this package, never an ABC `%%MIDI drummap` voice — that split is load-bearing, not a style choice.
- For exact register/attack/voice-leading precision (which pitches, not just which chord symbol), that's a production-stage decision made in `midi-orchestration`'s `references/exact-voicing.md` — this skill notates what's already decided, it doesn't decide voicings.
- `scripts/validate_abc.py` — structural + duration validator. Run on every file before hand-off.
- `scripts/test_validate_abc.py` — the validator's own test suite (for maintaining the validator, not per-composition use).
- `assets/lead-sheet-template.abc` — a minimal valid starting point to copy.

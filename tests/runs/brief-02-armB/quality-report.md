# Quality report — "Riptide" (brief-02-armB)

**Brief:** energetic jazz-fusion instrumental, 7/8, 16-24 bars, key open,
tempo fast (~150-170 BPM felt per eighth-note grouping). Arc: restless,
unsettled urgency building across the piece to a triumphant, released
climax near the end. Deliverables: lead sheet (melody+chords), bassline,
drum pattern, finished multi-track file. Small ensemble (lead, keys, bass,
drums).

**Delivered files (this directory):** `composition-plan.json`, `song.abc`,
`drums.json`, `interaction-map.md`, `pitched.mid`, `drums.mid`, `song.mid`
(merged, final deliverable), this `quality-report.md`.

**Output path targeted:** this package's own converters (`abc_to_midi.py` +
`grid_to_midi.py` -> merged `song.mid`) for BandLab or any DAW — the
*alternative* downstream path per `abc-to-midi-orchestration/SKILL.md`
Step 6. The *primary* downstream (`daw_generative` engine,
`POST /api/render`) was **not** exercised — and per `groove-meter.md`'s own
note, that engine currently only realizes `4/4`, so a 7/8 piece like this
one is not a candidate for that path today anyway. `song.abc` +
`drums.json` are the same artifacts either consumer would take.

---

## Real bugs found and fixed (self-heal loop, not hypothetical)

None of these were caught by `validate_abc.py`, which reported "0 errors, 0
warnings" on every version of the file, both before and after every fix
below — consistent with `common-failures.md`'s own warning that the
validator is a fast first pass, not the authority.

### 1. The known multi-voice issue (worked around from the start, then independently reconfirmed)

Per this run's own brief, `abc-syntax.md`'s documented multi-voice layout
(one `[V:id]` marker per block, bare continuation lines after it) is **not**
what `abc_to_midi.py` needs — its body-extraction is a per-line regex
(`^\[V:\s*(\S+)\]\s?(.*)`) that only captures a line if it *literally starts*
with `[V:id]`. `song.abc` was written from the first draft with the marker
repeated at the start of every content line (one marker per line, several
bars per line), specifically to avoid this. Verified, not assumed: after
writing the file this way, `abc_to_midi.py` produced 3 tracks with real,
hand-verifiable note counts (see "Verified, not just asserted" below) — the
workaround worked.

A related, second-order finding surfaced independently while doing the
music21-parse cross-check (`abc-notation-writer/SKILL.md` Step 4's "second
check"): running `music21.converter.parse()` on the *whole raw file*
collapses all three named voices (`Melody`, `Keys`, `Bass`) into a single
`Part` with all ~170 events concatenated sequentially, rather than three
simultaneous parts. This independently reproduces a finding from the
sibling `brief-01-armB` run in this same test suite (root-caused there to
`music21`'s `ABCHandler.splitByVoice()`, which only splits on *numeric*
voice IDs, never named ones) — and, as that run also found, switching to
numeric IDs does not actually fix anything once the per-line `[V:id]`
repetition `abc_to_midi.py` needs is also present. **The practical
conclusion (same as that run's): a generic whole-file `music21.converter.parse()`
is not a reliable "green light" for multi-voice ABC in this package.** The
check that actually matters is running `abc_to_midi.py` itself and
inspecting its per-track note counts, which is what this report's
verification is actually based on, not the generic-parse check.

### 2. NEW finding: `grid_to_midi.py` hardcodes a 4/4 bar, silently wrong for this 7/8 piece

`abc-to-midi-orchestration/scripts/grid_to_midi.py` line 26:
`beats_per_bar = 4` — a literal constant, never read from the grid JSON or
derived from any meter field. `sec_per_bar = (60/tempo_bpm) * 4` is then
computed unconditionally. For a 4/4 piece (like the sibling `brief-01-armB`
run) this is invisible, because it happens to be correct. **For this 7/8
piece it is a real bug**: a real bar here is 7 eighth-notes at `Q:1/8=160`
= 2.625 s, not `(60/tempo_bpm)*4`. Left uncorrected, the drum grid would
drift out of sync with the pitched tracks by a growing amount every bar.

Worked around (not patched in the script, since this is an evaluation of
the skill's tooling as-is): solved for a *fudged* `tempo_bpm` that makes the
script's hardcoded formula produce the correct real bar duration —
`tempo_bpm = 240 / 2.625 = 91.428571...` — combined with `steps_per_bar: 7`
(one step per real eighth note) and `swing: 0.5` (straight; see the groove
finding below for why swing had to be neutralized here, not just left at a
stylistic default). Verified, not assumed: `drums.mid`'s hit timing was
checked against the expected per-bar cursor position for several bars
(matches to well under a millisecond of drift over the whole 20-bar piece —
negligible). This fudge is documented at the top of `drums.json` itself, in
`composition-plan.json`'s `interpretive_choices`, and here, so anyone
re-running this pipeline on another odd-meter piece knows to do the same
thing (or fix the script).

### 3. Two real register bugs, caught only by inspecting the actual rendered MIDI pitch range

The composition plan states the climax's peak note is F#6 (bar 15) and
that nothing after it should exceed that ceiling. Checking the **actual
rendered MIDI** (not the ABC source by eye) against that claim found two
real violations:

- Bar 16 (first draft) was `a'3 ^g'2 ^f'2`, i.e. it opened on **A6** (MIDI
  93) — a full major third above the stated peak, and beyond any realistic
  lead-instrument range. Root cause: I mentally reserved apostrophe-octave
  notes for "the climax register" without checking that a *specific* note
  inside that octave (`a'`) is itself higher than the octave's other notes
  I'd already used as the ceiling. Fixed by rewriting the bar as
  `e'3 d'2 ^c'2` (E6-D6-C#6, all valid Dmaj7#11 tones — 9th, root, major7 —
  and all at or below F#6).
- Bar 17 (first draft) was `g'2 ^f'2 e'3`, opening on **G6** (MIDI 91),
  one semitone above the same F#6 ceiling — the identical class of mistake,
  caught on the *second* pass specifically because the first fix prompted a
  full re-scan of every apostrophe-register note in the file rather than
  trusting that one fix meant the problem was solved. Fixed by rewriting to
  `e'2 d'2 ^c'3` (E6-D6-C#6, the chord's 13th/root/major7 over Gmaj7#11 —
  a legitimate voicing, and consistent with bar 16's landing pitch).

Verified after both fixes, from the actual re-rendered `song.mid`: Lead
Sax's real MIDI range is **D4-F#6 (62-90)**, exactly matching the plan's
stated peak note, with note count unchanged (46 notes, since only pitches
changed, not durations). This is disclosed as a real, meaningful finding —
not a one-off typo, but the same *class* of octave-arithmetic mistake
happening twice in one file, caught only because the actual rendered pitch
data was inspected rather than the ABC source read by eye.

### A smaller, disclosed harmony fix made during composition (not caught downstream, caught during writing)

While drafting the melody against its chord symbols (not required by any
script, but done because the project's own standing principle is "sesuo
teori ⇒ tidak sumbang"): bar 11's original draft used a natural `A` passing
tone descending through a Bb7#11 chord, which actually wants `Ab` (the b7)
at that point in the scale; fixed to `_a`. The bar-16-*original* draft
(later fully replaced for the register bug above) had used a natural `g'`
against a chord explicitly asking for `#11`, i.e. the very "avoid note" the
`#11` label exists to avoid; fixed to `^g'` at the time, then superseded by
the bar-16 rewrite above (whose new pitches were independently re-checked
against `Dmaj7#11`'s tones).

---

## Verified, not just asserted

- `validate_abc.py`: **0 errors, 0 warnings** on the final `song.abc`
  (re-run after every fix above, not just the first draft).
- `abc_to_midi.py` on the final file: **3 tracks** — Lead Sax (46 notes,
  max-poly 1, program 65/Alto Sax, range D4-F#6), Rhodes (75 notes,
  max-poly 4, program 4/Electric Piano, range A#3-F#5), Bass (42 notes,
  max-poly 1, program 33/Electric Bass, range C#2-A3). Every voice's note
  count was hand-computed bar-by-bar from the ABC source (summing non-rest
  tokens/chord instances) *before* running the script, then compared —
  all three matched exactly (46/75/42) on the first attempt, confirming no
  notes were silently dropped by the per-line-marker workaround.
- `grid_to_midi.py`: **182 drum hits across 20 bars**, also hand-computed
  bar-by-bar from `drums.json` before running the script and matched
  exactly.
- Duration check: expected `20 bars * 7 eighths * (60/160)s = 52.5 s`; all
  three pitched tracks in the merged MIDI end at exactly `52.500 s`.
- Sync check: the drum track ends at `50.212 s`, a ~2.29 s gap. Traced to
  the *intentional* design of the final bar (bar 20's only drum event is a
  short kick/snare/ride stinger near the bar's start, "one clean stinger,
  then silence — no fade," while the pitched tracks sustain their final
  chord for the full bar) — both files independently confirmed at 20 bars,
  so this is the documented "intentional tail" case from
  `midi-conversion.md`, not a bar-count mismatch.
- No-drone / no-bad-note check: 0 notes with velocity ≤0, non-positive
  duration, or out-of-range pitch anywhere in the merged file; no note in
  any pitched track exceeds 2.625 s (one bar) — confirming Fix 1 (chord-symbol
  stripping) worked and no drone slipped through.
- Register-overlap check (Ensemble interaction, domain 11): Lead Sax
  (D4-F#6) and Rhodes (A#3-F#5) genuinely overlap in raw pitch range.
  Checked concretely, not just from the ranges: 123 time-overlapping
  lead/Rhodes note pairs exist in the merged MIDI, of which 11 pairs sit
  within a 2-semitone band (a real near-unison/masking risk). This is a
  disclosed, unmitigated-beyond-this-report finding, not smoothed over —
  the interaction map's role design (Rhodes mostly sustains while the lead
  moves) reduces but does not eliminate the risk.
- Velocity check (a real limitation, not a caveat): every note in Lead Sax,
  Rhodes, and Bass has **velocity exactly 90**, zero variation, in the
  final `song.mid` — only the drum track has real humanized velocity
  (base velocities 55-100, ±8 humanize, per `drums.json`). This mirrors the
  same finding in the sibling `brief-01-armB` run: `abc_to_midi.py` applies
  no dynamics/velocity shaping to pitched voices at all, regardless of the
  plan's stated dynamic arc.
- No named groove profile in `groove-profiles.md` fits this piece (only
  `neo-soul-core` is defined, an explicitly laid-back pocket); no `%%pocket`
  directive was written into `song.abc`, since declaring one that doesn't
  match would misrepresent intent. `swing: 0.5` (straight) was used in
  `drums.json` instead, partly for feel and partly because the swing
  formula in `grid_to_midi.py` (`if i % 2 == 1: push late`) is built for a
  16-step 8th/16th grid and does not have a coherent meaning at
  `steps_per_bar: 7` in an odd meter — any swing value other than 0.5 here
  would distort the 2+2+3 grouping rather than swing it.

---

## Rubric (`quality-control.md` §17), scored 0-4 per domain

| # | Domain | Score | Why |
|---|---|---:|---|
| 1 | Brief fit and ethics | 3 | Facts vs. interpretation separated explicitly (`interpretive_choices` in the plan covers the tempo reading, the 2+2+3 grouping choice, the parallel-mode-shift choice, and the missing groove profile). Output path stated above. No copyrighted/artist-specific material. Minor: "fixed DNA / forbidden shortcuts" language not used verbatim, only equivalent prose. |
| 2 | Identity and development | 4 | The hook motif appears 5 times with real transformation each time (bare fragment -> complete statement -> fragment restated -> sequenced up a step -> register-leap transformed return in the parallel major) — by its third appearance it is already doing new *functional* work (sequencing = building), not just repeating with new color. |
| 3 | Form | 4 | Every section has an exact bar count; total bars (20) and duration (52.5 s) agree exactly, verified programmatically, not estimated. Every section has a stated listener-facing function; recurrences are labeled (fragment/complete/sequenced/transformed). |
| 4 | Transitions | 2 | Section boundaries are handled (silence-into-hit at the climax is well specified: setup/threshold/arrival all named), but the deeper `instrumental-transitions.md` framework (transition families, explicit source-target analysis for every boundary) was **not** consulted in this run — a real, disclosed gap, not a hidden one. |
| 5 | Groove and microtiming | 2 | The qualitative design (straight, driving 7/8, audible 2+2+3 grouping via kick placement) is coherent, but real, disclosed limitations exist in the rendering: `grid_to_midi.py`'s hardcoded 4/4 bar required a tempo-fudge workaround for this meter (documented above); no groove profile fits an energetic fusion pocket; swing is functionally inert at this grid resolution/meter; `abc_to_midi.py` applies zero per-note microtiming to any pitched voice. |
| 6 | Harmony | 3 | Chords are correctly spelled and consistent with the theory-hierarchy declaration; the melody was audited note-by-note against its chord symbols and two real mismatches were found and fixed (bar 11's passing tone, bar 16-original's avoid-note). Bass and Rhodes voicings were correct by construction (verified when designed) but not independently re-audited line-by-line with the same rigor as the melody. |
| 7 | Bass and exact voicing | 3 | Register is exact and verified (C#2-A3, idiomatic for electric bass); the bar-11 chromatic walk-up is a deliberate, disclosed non-chord-tone passing gesture, not an oversight. Gate/attack behavior (per `exact-voicing.md` §9) was designed conceptually (implied by note length) but not realized as actual shortened note-off gates in the rendered MIDI — notes ring for their full written duration. |
| 8 | Melody, hook, thematic development | 3 | One motif organizes the whole piece with a clear fragment/complete/sequence/transformed-return arc, and the final range (D4-F#6) is exact and matches the stated peak note — but getting there took two real register bugs (documented above), and F#6 itself sits at the very top edge of even soprano sax's practical range (hence the plan's hedge to "soprano sax / lead synth"), not a comfortably safe number. |
| 9 | Loop development | 3 | Not a loop-centered piece by design (through-composed, arc-driven), so several bullets (a true "expanded vs. core vs. reduced" loop-state ladder) don't apply — scored on the bullets that do apply (protected hook identity, a genuine subtraction event, no info-free literal repeats), all of which are met. |
| 10 | Improvisation | 2 | Not attempted — the brief asks for a fully notated arc piece with no solo section, so this domain is honestly scored low rather than inflated; not a structural failure given the brief. |
| 11 | Ensemble interaction | 2 | The lead/support/answer/silent role design is real and bar-traceable (`interaction-map.md`), with a genuine call-response (bar 6) and subtraction (bar 14) present. Marked down for two disclosed, unresolved findings: bar 11's two-simultaneous-leader exception to the one-leader rule, and the measured 11 close-register (≤2-semitone) simultaneous lead/Rhodes note pairs. |
| 12 | Arrangement and orchestration | 3 | Every track has a distinct, verified role and GM program; ranges are exact and (mostly) playable, with the lead's F#6 ceiling flagged as instrument-dependent above. The brief's "lead sheet" deliverable is served by `song.abc`'s melody voice + chord symbols rather than a separately rendered score image (same disclosed simplification as the sibling run — no tool in this workflow renders a score image). |
| 13 | Production and DAW-first design | 2 | Layer addition/subtraction across the arc is deliberate and verified bar-by-bar (interaction map). Marked down because the rendered MIDI has **zero** dynamic/velocity variation on any pitched track (flat velocity 90, confirmed) despite the plan's explicit dynamics-building arc — the intent exists in the plan and prose, not in the audio-adjacent data. |
| 14 | Notation and data validation | 4 | `validate_abc.py` clean (0/0) on every version. Verification went well beyond "does it parse": per-track note counts were hand-computed *before* running the converter and matched exactly (twice, before and after the register fix); a new script bug (grid_to_midi.py's hardcoded 4/4 bar) was found, understood, and worked around with a documented, checked fix; two real register bugs were found by inspecting actual rendered MIDI pitch data, not by re-reading the ABC source; the "generic music21 parse as a green light" claim in the skill's own docs was tested and found not to hold for this package's multi-voice files, corroborating an independent prior finding. |
| 15 | Originality and cultural responsibility | 4 | Fully original composition; no artist, recording, or copyrighted melody referenced or imitated; genre attributes are generic jazz-fusion vocabulary (style-cheatsheet + groove-meter.md), not a specific artist's identifiable style. |
| 16 | Style specificity | 3 | Concrete jazz-funk/fusion DNA applied (bass-and-drum riff-lock at the climax, riff-driven groove, dominant/sus color, "identity from the riff lock" per the style cheatsheet) — but the brief's tempo (160 eighth-note pulse) and meter (7/8) both explicitly exceed the style cheatsheet's stated typical range (90-130 BPM, no odd meter mentioned); this is a disclosed, brief-directed override, not an oversight, but it does mean the piece leans more on the brief's numbers than on the cheatsheet's idiomatic defaults. |

**Total: 47/64.**

No domain scored below 2 (the rubric's own floor for a deliverable
composition). No domain is "blocking" under the rubric's definition
(structural validator error / originality concern / cultural concern) — all
validator-visible issues were repaired before this score was computed, and
the `validate_abc.py` + `music21`-parse-caveat + `abc_to_midi.py` chain is
clean and hand-verified.

---

## §18 Final validation report template

- **Composition-plan validation:** PASS (manual — this package has no
  `scripts/validate_blueprint.py`; checked `composition-plan-template.json`'s
  required fields for completeness and verified programmatically that
  every bar's chord-beats sum to exactly 7 (the 7/8 meter's beat count):
  20/20 bars checked, 0 mismatches).
- **DAW-plan validation:** NOT REQUIRED (this package has no separate "DAW
  plan" JSON artifact type; the equivalent sync/mono/no-drone checks were
  run manually against `drums.json` + the merged `song.mid` — see "Verified,
  not just asserted" above).
- **ABC validation:** PASS (`validate_abc.py`: 0 errors, 0 warnings, on the
  final file, re-checked after every fix; cross-checked against the real
  `abc_to_midi.py` conversion, which is what actually matters downstream —
  see the note above on why a generic `music21.converter.parse()` is not a
  reliable green light for multi-voice ABC in this package).
- **Musical audit: 47/64.**
- **Blocking issues repaired:**
  1. `abc_to_midi.py` silently drops all notes on a voice unless `[V:id]`
     is repeated on every physical content line (not just once per block,
     as `abc-syntax.md`'s own example shows) — `song.abc` was written with
     the repeated bracket from the start; confirmed working via exact
     per-track note counts.
  2. `grid_to_midi.py` hardcodes a 4/4 bar (`beats_per_bar = 4`) regardless
     of the actual meter — for this 7/8 piece, worked around with a solved
     "fudge" `tempo_bpm` (`91.428571`) in `drums.json` that makes the
     script's internal bar duration match the real 7/8 bar at `Q:1/8=160`;
     documented in `drums.json` itself and verified via bar-timing
     arithmetic.
  3. Two real register bugs (bar 16 opening on A6, bar 17 opening on G6 —
     both above the plan's own stated F#6 peak-note ceiling) — caught by
     inspecting the actual rendered MIDI pitch range rather than the ABC
     source, fixed, and re-verified (final Lead Sax range: D4-F#6, exactly
     matching the plan).
  4. Two smaller harmony mismatches caught during composition (a passing
     tone and an "avoid note" against a `#11` chord) — fixed before the
     first validator run.
- **Development risks reviewed:** the domains scored 2/4 above (transitions,
  not deeply consulted; groove/microtiming, real tooling limitations for
  odd meter; improvisation, N/A to this brief; ensemble interaction's
  disclosed two-leader bar and register-overlap counts; production's flat
  velocity) are real, verified gaps between the plan's musical intent and
  what this package's converters actually render — architecture-level
  limitations of the tooling (some already documented in the package's own
  reference files, e.g. `groove-profiles.md`), not something papered over.
- **Remaining interpretive choices:** the tempo reading (eighth-note pulse
  = 160, not quarter-note pulse); the 7/8 grouping as 2+2+3 (an arbitrary
  but declared choice, per `groove-meter.md`'s own instruction); the
  triumphant release realized as a parallel-mode shift (D minor/Dorian
  color -> D major/Lydian, same key signature) rather than a true key
  modulation; the exact bar allocation (Intro 2 / A1 4 / A2 4 / B 4 / C 4 /
  Outro 2 = 20 bars); ensemble voicing (soprano sax/lead synth, electric
  bass, Rhodes); the piece's title.
- **Live-performance alternatives:** nothing here depends on studio-only
  production (no automation, no reverse audio, no fades were used
  anywhere) — a real quartet could read `song.abc` + `interaction-map.md`
  and play the same arrangement, supplying by ear the dynamics and
  microtiming that the rendered MIDI itself does not encode.
- **Renderer or format limitations:**
  - Every pitched note in the final MIDI has a flat velocity of 90; the
    plan's dynamics dimension (the arc's building-then-release intensity)
    is not realized in the audio-adjacent data, only in the prose plan.
  - `abc_to_midi.py` applies no per-note micro-timing or gate-ratio shaping
    to pitched voices; `grid_to_midi.py` applies one global swing ratio to
    all drum voices (set to 0.5/straight here, since no swing value is
    musically coherent at `steps_per_bar: 7` in a 2+2+3 odd meter) rather
    than a per-role offset table. No `%%pocket` directive was written,
    since the only defined profile (`neo-soul-core`) does not fit this
    piece's energetic, straight feel and inventing an ad hoc one is
    explicitly discouraged by `groove-profiles.md` itself.
  - `grid_to_midi.py`'s hardcoded `beats_per_bar = 4` is a genuine
    architecture limitation for any non-4/4 piece, worked around here with
    a solved fudge value rather than a script patch (this evaluation
    exercised the skill's tooling as-is); a real fix belongs in the script.
  - The brief's "lead sheet" deliverable is represented as `song.abc`'s
    melody voice + chord symbols (any ABC renderer can turn this into a
    visual score); no separately rendered score image was produced, since
    no tool in this workflow does that.
  - Lead Sax's F#6 peak note is at the very top edge of even soprano sax's
    practical altissimo range; the plan hedges this explicitly by naming
    the lead instrument as "soprano sax / lead synth" rather than
    committing to acoustic sax alone.

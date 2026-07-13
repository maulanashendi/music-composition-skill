# Quality report — "Settling In (Late)"

Brief: laid-back neo-soul/chill-jazz instrumental, 16-24 bars, C minor, 4/4,
~78 BPM. Arc: quiet late-night self-doubt -> calm, unforced acceptance (no
big triumphant ending, just settling). Deliverables: lead sheet
(melody+chords), bassline, drum pattern, finished multi-track file.

Delivered files (this directory): `composition-plan.json`, `song.abc`,
`drums.json`, `interaction-map.md`, `pitched.mid`, `drums.mid`, `song.mid`
(merged, final deliverable), this `quality-report.md`.

**Output path targeted:** this package's own converters
(`abc_to_midi.py` + `grid_to_midi.py` -> merged `song.mid`) for BandLab or
any DAW -- the *alternative* downstream path per
`abc-to-midi-orchestration/SKILL.md` Step 6. The *primary* downstream
(`daw_generative` engine, `POST /api/render`) was not exercised in this run;
`song.abc` + `drums.json` are the same artifacts either consumer would take.

---

## Two real bugs found and fixed (self-heal loop, not hypothetical)

These were **not** caught by `validate_abc.py` (which reported "0 errors,
0 warnings" in every case below, both before and after each fix) -- they
were only caught by actually running the downstream consumers and checking
their output, exactly as `common-failures.md` and `midi-conversion.md`
predict is necessary.

1. **Named voice IDs never split into separate parts under music21.**
   `abc-syntax.md`'s own documented convention (`V:Melody`, `V:Bass`,
   switched inline with `[V:Melody]`) causes `music21.converter.parse()` to
   silently collapse the whole tune into a single sequential part (measure
   offsets running 0, 4, 8, 12... instead of three parts each starting at
   offset 0). Root cause, traced into `music21/abcFormat/__init__.py`
   `ABCHandler.splitByVoice()`: it only treats a voice token as a split
   point when `token.data[0].isdigit()` -- i.e. only numeric IDs (`V:1`,
   `V:2`, `V:3`) split into parts; named IDs never do, regardless of
   bracket usage. Fixed by using numeric voice IDs with `name=` for display.
2. **This package's own `abc_to_midi.py` requires the `[V:id]` bracket
   repeated on every physical content line, not just once per voice
   block.** Its body-extraction is a per-line regex
   (`^\[V:\s*(\S+)\]\s?(.*)`); a line that doesn't literally start with
   `[V:id]` contributes nothing. Tested directly: writing the file in the
   exact style `abc-syntax.md`'s own example shows (one `[V:Melody]` marker
   followed by un-prefixed continuation lines) produces **0 tracks, 0
   notes** through this script -- a silent, completely empty MIDI --
   while `validate_abc.py` still reports 0 errors and generic
   `music21.converter.parse()` still succeeds without exception. Fixed by
   repeating `[V:1]` / `[V:2]` / `[V:3]` at the start of every content line.

**These two fixes are in direct tension with each other, and there is no
single multi-voice convention that satisfies both at once.** Confirmed
directly on the final `song.abc`: after adding the repeated `[V:1]`/`[V:2]`/
`[V:3]` brackets that `abc_to_midi.py` requires (fix 2), a generic
whole-file `music21.converter.parse()` goes back to collapsing into one
part (measures `[0, 0, 72]` across the three `s.parts`) -- because
`splitByVoice()` only ever treats the three header-line declarations as
split points, never the repeated inline brackets, no matter how many times
they appear. The *only* way to make generic `music21.converter.parse()`
correctly produce 3 clean parts (24 measures each) is to declare each voice
exactly once, with no separate header block and no inline brackets at all
-- which is precisely the shape that makes `abc_to_midi.py` capture zero
notes (finding 2). This means **`abc-notation-writer/SKILL.md`'s own advice
that "a clean music21 parse is the real green light" for MIDI-bound,
multi-voice ABC is not just insufficient but actively misleading in this
package**: the file shape that passes that green light is exactly the shape
that silently produces an empty MIDI through this package's actual
converter, and the file shape the converter needs makes the "green light"
check fail. The only check that actually validates what matters is running
`abc_to_midi.py` itself and inspecting its per-track note counts -- which is
what this run did, and what `song.mid`'s correctness is actually based on
(verified below), not the generic-parse check.

Net effect: **the exact multi-voice style this skill package's own
reference doc (`abc-syntax.md`) teaches as the standard way to write
multi-voice ABC produces either wrongly-merged parts (generic music21) or a
silently empty MIDI (this package's actual converter) unless both of the
above are known and worked around -- and no single file satisfies both
"looks correct to a generic music21 parse" and "extracts correctly through
this package's own converter."** Neither `validate_abc.py` nor a bare "does
it parse" check surfaces either problem. This is the single most important
finding from this exercise, more consequential than anything in the
composition itself, and is worth fixing in the skill's own reference
material, validator, and/or converter script.

A third, less structural but still real issue was caught and fixed during
this run: my first draft of the B-section melody (written with ABC octave
apostrophes intended as "one octave above A1") actually resolved to MIDI
72-94, i.e. up to Bb6 -- an extreme, effectively unplayable register for
alto sax, directly contradicting the composition plan's own explicit
"register capped, never extreme, no big peak" design goal. Root cause: bare
lowercase ABC letters already sit close to C5 by default, so anchoring A1's
"low-mid" register in plain lowercase, then going up another full octave
for B, compounded into an unreasonable range. Fixed by shifting the whole
melody down one octave (A1/Outro to uppercase, B to plain lowercase without
apostrophes); verified after the fix that Sax's real MIDI range is C4-Bb5
(60-82), which is idiomatic for the instrument.

---

## Verified, not just asserted

- `validate_abc.py`: **0 errors, 0 warnings** on the final `song.abc`.
- `music21.converter.parse()` on the final file: as explained above, this
  generic whole-file check does **not** cleanly split by voice on the final
  file (it reports 3 `Part` objects, but with measures `[0, 0, 72]` --
  everything merged into the third). This is expected given the tension
  described above and does not indicate a problem with the deliverable
  itself; `abc_to_midi.py` (the tool that actually matters) parses each
  voice independently and correctly, verified next.
- `abc_to_midi.py` on the final file: 3 tracks -- Sax (24 notes, max-poly
  1), Rhodes (88 notes, max-poly 4), Bass (30 notes, max-poly 1). Note
  counts hand-verified bar-by-bar against the intended voicings (they
  matched exactly once I found my own arithmetic slip on the first
  recount). Re-ran this fresh, from the final files on disk, immediately
  before writing this report -- reproducible, not a one-off.
- `drums.json`: bars sum to exactly 24 (matches the ABC); every pattern row
  hand-verified at exactly 16 characters via script, not by eye.
- `grid_to_midi.py`: 150 drum hits across 24 bars, no errors.
- Duration check: expected `24 bars * 4 beats * 60/78 = 73.85s`; all three
  pitched tracks in the merged MIDI end at exactly 73.85s.
- Sync check: drum track ends at 69.79s, a ~4.06s gap. Traced this to the
  *intentional* design of the last ~1.3 bars (bar 23 has one hit near its
  end, bar 24 is deliberately empty -- "settling... no drums at all"), not
  a bar-count mismatch (both files independently confirmed at 24 bars).
  This matches `midi-conversion.md`'s own guidance to confirm bar counts
  rather than trust the raw end-time gap alone.
- Register overlap check: Sax and Rhodes both land at C4-Bb5 in the final
  MIDI (real, confirmed overlap in raw pitch range); Bass is cleanly
  isolated at C3-B3 below both. The overlap is a genuine finding, not
  dismissed -- reflected in the "Ensemble interaction" score below. In
  practice the risk is mitigated (not eliminated) by role design: Rhodes
  plays static, sustained rootless-shell chords while Sax is active, so the
  two are rarely both "busy" in the same register at once, even though
  their raw pitch ranges overlap.
- Velocity check (this one is a real limitation, not just a caveat): every
  note in Sax, Rhodes, and Bass has **velocity exactly 90**, with zero
  variation, in the final `song.mid`. Only the drum track has real
  velocity variation (range 38-97, humanized). Confirmed by direct
  inspection of the merged file, not inferred from reading the script.

---

## Rubric (quality-control.md §17), scored 0-4 per domain

| # | Domain | Score | Why |
|---|---|---:|---|
| 1 | Brief fit and ethics | 3 | Facts/assumptions separated, arc/instrumentation/production not conflated, output path now stated explicitly above. No copyrighted/artist-specific material. Minor: "fixed DNA / forbidden shortcuts" wasn't captured in that exact vocabulary, only as equivalent prose in the plan's `notes`. |
| 2 | Identity and development | 3 | Motif genuinely transforms (Statement/Answer/Expansion/Fragment) and macro/meso/micro levels were worked in the right order. The strict "third recurrence develops function" bullet doesn't apply cleanly -- only two recurrences of the main cell exist, not three. |
| 3 | Form | 4 | Every section has an exact, machine-verified bar count; total bars/duration agree exactly (73.85s @ 78bpm, confirmed programmatically); every section has a stated dramatic function. |
| 4 | Transitions | 3 | Every boundary is a deliberate move (texture handoff, chord-color shift, dominant resolution), but transition *families* are not very varied (mostly harmonic/textural; no rhythmic- or bass-led transition), and setup/threshold/arrival/aftercare is only explicitly labeled for the B->Outro boundary, not all three. |
| 5 | Groove and microtiming | 2 | Design intent is coherent (declared `%%pocket neo-soul-core`, consistent swing=0.57 in the drum grid), but the *rendered* MIDI mostly doesn't implement it: `abc_to_midi.py` applies no per-note micro-timing or gate-ratio shaping to pitched voices at all (confirmed by reading the script and by the flat velocity=90 finding above), and `grid_to_midi.py` applies only one global swing ratio to all drum voices, not the per-role offset table in `groove-profiles.md`. This is a known, disclosed limitation of the package (`groove-profiles.md` says as much), not something hidden. |
| 6 | Harmony | 3 | Chords correctly spelled and voiced from their symbols (hand-derived and verified); non-diatonic choices (borrowed bIII, altered dominant, half-diminished ii) all have stated rationale. Minor: didn't verify every single bar's melody-against-alteration fit, only spot-checked a few; `Bbm7b5`'s b5 was spelled as E natural rather than the "correct" Fb (a disclosed, deliberate simplification, sounds identical in MIDI). |
| 7 | Bass and exact voicing | 3 | Register/octaves are exact and playable (C3-B3, idiomatic for electric bass); voicings match their chord labels exactly (checked note-by-note). The bass is root-anchored throughout by genre-appropriate design, not really outlining 3rds/7ths as a melodic line; gate ratios (groove-profiles.md's bass ~0.78-0.90) are not applied -- notes ring for their full written duration. |
| 8 | Melody, hook, thematic development | 4 | The most carefully engineered dimension: one motif, clean fragment/complete/expansion/fragment-return arc, and -- after the register bug was caught and fixed -- a genuinely idiomatic C4-Bb5 sax range with the one elevated moment (Bb5) never repeated elsewhere. |
| 9 | Loop development | 3 | Not really a loop-centered piece (through-composed, arc-driven), so several bullets (e.g. a true "expanded" state) don't apply by design -- there is no louder/denser state anywhere, deliberately. The applicable bullets (protected features, return-contains-new-information via Abmaj9, subtractive outro) are met. |
| 10 | Improvisation | 2 | Not attempted -- the brief is a fully notated mood piece with no solo requested. Scored conservatively rather than inflated to 4, since the domain is genuinely unaddressed; not a structural failure given the brief. |
| 11 | Ensemble interaction | 2 | The lead/support/answer/silent role design itself is solid and documented bar-by-bar in `interaction-map.md`. Marked down because two real gaps surfaced during verification: Sax and Rhodes numerically overlap in register (C4-Bb5 both), and there is *zero* dynamic/velocity variation in any pitched track -- the arc's dynamics dimension (soft intro, modest lift, settling outro) exists in the plan but not in the rendered MIDI. |
| 12 | Arrangement and orchestration | 3 | Every track has a distinct, checked role; ranges/registers are all playable with comfortable endurance (longest note ~1 bar). The brief's "lead sheet" deliverable is served by `song.abc`'s Sax voice + chord symbols rather than a separately rendered score image -- disclosed as an interpretive choice, not a gap in this toolset. |
| 13 | Production and DAW design | 3 | Appropriately dry (pure MIDI, no fx layer expected at this stage per the skill's own scope). Layer addition/subtraction is deliberate and symmetric (Intro adds, Outro subtracts). No automation exists (no CC/volume curves) -- consistent with the flat-velocity finding above. |
| 14 | Notation and data validation | 4 | `validate_abc.py` passes cleanly; cross-checked against the actual `abc_to_midi.py` conversion, not just "does it parse" -- verified per-track note counts and max-polyphony numerically, reproducibly. Two non-obvious, validator-invisible bugs were found and fixed via genuine self-heal (including discovering that generic `music21.converter.parse()` and this package's `abc_to_midi.py` want mutually incompatible file shapes for multi-voice ABC), and disclosed in full above rather than glossed over. |
| 15 | Originality and cultural responsibility | 4 | Fully original; no artist/song referenced or imitated; genre attributes (voicing family, groove profile, arrangement architecture) drawn from the package's own genre file, not from a specific recording. |
| 16 | Style specificity | 4 | Concrete neo-soul DNA applied throughout (rootless shells, anchor/rotation roles, `neo-soul-core` pocket, ≤1-foreground-voice density ceiling, motif-development vocabulary) rather than surface markers alone. |

**Total: 50/64.**

No domain scored below 2 (the rubric's floor for a deliverable composition).
No domain is "blocking" under the rubric's own definition (structural
validator error / originality concern / cultural concern) -- the two ABC
bugs found above were both repaired before this score was computed, and the
final `validate_abc.py` + `music21` + `abc_to_midi.py` chain is clean.

---

## §18 Final validation report template

- **Composition-plan validation:** PASS (manual -- this package has no
  `scripts/validate_blueprint.py`; checked `composition-plan-template.json`'s
  required fields for completeness and verified chord-beats-per-bar sum to
  the meter programmatically: 96 total beats / 24 bars * 4 beats-per-bar,
  exact).
- **DAW-plan validation:** NOT REQUIRED (this package has no separate
  "DAW plan" JSON artifact type; the equivalent sync/mono/no-drone checks
  were run manually against `drums.json` + the merged `song.mid` -- see
  "Verified, not just asserted" above).
- **ABC validation:** PASS (`validate_abc.py`: 0 errors, 0 warnings, on the
  final file; cross-checked against the real `abc_to_midi.py` conversion,
  which is what actually matters downstream -- see the note above on why
  a generic `music21.converter.parse()` is not a reliable green light for
  multi-voice ABC in this package).
- **Musical audit: 50/64.**
- **Blocking issues repaired:**
  1. Named ABC voice IDs (`V:Melody`/`V:Bass`) silently fail to split into
     separate music21 parts -- switched to numeric IDs (`V:1`/`V:2`/`V:3`)
     with `name=` for display.
  2. This package's `abc_to_midi.py` silently drops all notes on a voice
     unless `[V:id]` is repeated on every physical content line (not just
     once per block, as `abc-syntax.md`'s own example shows) -- rewrote
     `song.abc` so every content line repeats its voice's bracket.
  3. B-section melody's ABC octave marks resolved to an unplayable Bb6
     (MIDI 94) instead of the intended modest lift -- shifted the whole
     melody down one octave; verified final Sax range is C4-Bb5.
- **Development risks reviewed:** the domains scored 2/4 above (groove and
  microtiming implementation depth; improvisation, N/A to this brief;
  ensemble interaction's register-overlap and flat-velocity findings) are
  real, disclosed gaps between the plan's musical intent and what this
  package's converters actually render -- they are architecture-level
  limitations of the tooling (documented in `groove-profiles.md` itself for
  the microtiming case), not something papered over here.
- **Remaining interpretive choices:** ensemble voicing (alto sax lead,
  electric bass fingered, Rhodes); the exact pitches realizing the hook's
  prose description (rise-a-minor-third-then-fall shape, landing on the
  6th/2nd); 3-note vs. 4-note rootless-shell choices per chord; the
  Intro(4)/A1(8)/B(4)/Outro(8) bar allocation; the piece's title; the
  decision to drop the composition-plan template's default 4th "peak"
  phase entirely (documented and justified in `composition-plan.json`'s
  own `notes`, since the brief explicitly forbids a big triumphant
  ending).
- **Live-performance alternatives:** nothing here depends on
  studio-only production (no automation, no reverse audio, no fades were
  used) -- a real quartet could read `song.abc` and the interaction map and
  play the same arrangement, applying by ear the dynamics and pocket that
  the MIDI itself does not currently encode.
- **Renderer or format limitations:**
  - Every pitched note in the final MIDI has a flat velocity of 90; the
    plan's dynamics dimension (mood -> dynamics mapping) is not realized in
    the audio-adjacent data, only in the prose plan.
  - `abc_to_midi.py` applies no per-note micro-timing/gate-ratio shaping to
    pitched voices; `grid_to_midi.py` applies one global swing ratio to all
    drum voices rather than the per-role offset table `groove-profiles.md`
    itself defines. The `%%pocket neo-soul-core` directive was written into
    the ABC as forward-compat/declarative intent, per that file's own
    guidance -- it is inert to the current converters.
  - `Bbm7b5`'s diminished fifth is spelled as E natural (enharmonic to the
    "correct" Fb) for ABC-writing convenience; identical sounding pitch,
    non-standard spelling.
  - The brief's "lead sheet" deliverable is represented as `song.abc`'s
    Sax voice + chord symbols (any ABC renderer can turn this into a
    visual score); no separate rendered score image was produced, since
    no tool in this workflow does that.

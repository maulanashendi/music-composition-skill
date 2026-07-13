# Notes — "Restless Seven" (working title)

Baseline attempt at the brief: energetic jazz-fusion instrumental in 7/8,
~16-24 bars, fast tempo, arc from restless/unsettled to a triumphant release.
Written from general music-theory/ABC/MIDI knowledge only, no specialized
composition tooling.

## Form / length

20 bars total, in four sections:

- **Bars 1-4 — Intro.** A groove-establishing vamp on Dm7, mostly rhythmic
  stabs (lead is tacet except a couple of punctuation hits) so the odd meter
  registers in the ear before the melody starts.
- **Bars 5-10 — A theme ("restless").** 6 bars, one chord change per bar,
  angular arpeggio-based melody over a Dorian-flavored progression with a
  b2 (Ebmaj7#11) borrowed chord and an altered dominant (C7#9 / A7alt) for
  tension. Grouping felt as 2+2+3.
- **Bars 11-16 — B / development ("more unsettled").** 6 bars. Same harmonic
  material sequenced and pushed further (Em7b5, second A7alt, Fmaj7#11 lift,
  G7#9 as the big dominant setup). The main device here: the *eighth-note
  grouping itself flips* from 2+2+3 to 3+2+2 for this section only, so the
  rhythmic feel is displaced relative to the rest of the piece — that
  displacement, more than tempo or dissonance, is what's doing the
  "unsettled" work. Bar 16 ends with a tom fill (drums) as a pickup into the
  climax.
- **Bars 17-20 — Climax ("triumphant, released").** Resolves to D major
  (parallel major of the Dm7 tonic — a deliberate "Picardy" turn), grouping
  locks back to a steady 2+2+3, melody opens up into long held unison notes
  instead of busy syncopation (bar 17 and bar 20 are each a single note held
  for the whole bar), hi-hat swaps for open ride cymbal, crash cymbals mark
  the arrival (bar 17) and the final hit (bar 20). The "release" is meant to
  read as: less rhythmic business, more sustain, brighter (major/Lydian)
  harmony, bigger dynamics — the opposite of the busy/displaced B section.

## Key / tempo

- Notated in `K:Ddor` (D Dorian — no accidentals in the signature; D minor
  tonic with a natural 6th, standard modal-jazz/fusion color) for bars 1-16,
  then the harmony turns to D major for the climax (bars 17-20) — done with
  explicit accidentals (`^F`, not a formal `K:D` key-signature change; see
  "ABC / tooling problems" below for why).
- `M:7/8`, `L:1/8`, tempo written as `Q:1/8=160` — i.e. the eighth note
  itself is the felt pulse at ~160/min, per the brief's "tempo felt per
  eighth-note grouping." That works out to a bar (7 eighths) = 2.625s, or
  roughly 22.9 bars/minute — a fast, driving fusion tempo, in the same
  ballpark as pieces like Mahavishnu Orchestra's or Dave Weckl's odd-meter
  fusion writing that I used as a mental reference point (no direct
  quotation, just genre/tempo intuition).

## Chords (one per bar, 20 bars)

Dm7 · Dm7 · Ebmaj7#11 · Dm7 | Dm7 · Ebmaj7#11 · Dm7 · C7#9 | Bbmaj7#11 ·
A7alt · Dm7 · Ebmaj7#11 | Em7b5 · A7alt · Fmaj7#11 · G7#9 | D · Gmaj7#11 ·
Bm7 · Dmaj7#11

Harmonic logic: Dm7 tonic with a repeating Ebmaj7#11 (bII, a very standard
modal-jazz/fusion "Phrygian-ish" color chord borrowed for darkness) as the
main restless color; C7#9 / A7alt as altered dominants for bite; a short
ii-V-ish push (Em7b5 - A7alt) and a Lydian IV (Fmaj7#11) and dominant (G7#9)
build into the D major arrival. The final D - Gmaj7#11 - Bm7 - Dmaj7#11 turn
in the climax is deliberately brighter/simpler harmonically (fewer altered
tensions) to make the "release" felt harmonically as well as rhythmically.

## Melody

Mostly chord-tone arpeggiation with a few idiomatic altered-dominant color
tones (e.g. the natural-C over A7alt in bars 10/14 is the `#9`/`b3`
"Hendrix-chord" tension, not a mistake — same idea with the `Bb` there as
the `b9`). Rhythms alternate quarter+quarter+dotted-quarter (2+2+3) and, in
the B section, dotted-quarter+quarter+quarter (3+2+2), matching the grouping
described above. The climax's two long whole-bar notes (bar 17, bar 20) are
the main "release" gesture — after 16 bars of syncopated, broken-up rhythm,
just letting a note ring for a full bar is meant to land as relief.

One motif I reused on purpose: the rising arpeggio figure in bar 16
(G7#9: G-B-D, climbing into a high D) reappears almost identically in bar 18
(Gmaj7#11: G-B-D) — same shape, but the chord under it flips from tense
dominant to consonant major, so the repeated shape is what carries the
tension→release payoff, not new melodic material.

## Bass

Root-position triadic outlining (root/3rd/5th or root/5th/7th depending on
the chord) in the same 2+2+3 / 3+2+2 rhythmic figure as the section it's in,
mostly moving in parallel with the lead's rhythmic groupings so the two
lock together as one riff, especially in the intro and at the climax where
both lead and bass hit the same long held root together (bars 17 and 20).
This is a straightforward, not especially virtuosic, fusion bassline —
I prioritized a clear, correct outline of the changes over a more
independent/soloistic bass part, given the time available.

## Drums

See `drums.md` for the full per-section breakdown. Short version: steady
2+2+3-driven kick/hihat groove in the intro and A section that gradually
adds ghost-note snare tension; the B section's groove is deliberately
regrouped as 3+2+2 (kick/snare accents literally move to different eighth
positions) to make the "unsettled" arc a rhythmic fact, not just a mood
label; a tom fill in bar 16 sets up the climax; the climax switches hi-hat
for open ride cymbal, adds crash cymbals at the arrival and the final hit,
and simplifies back to steady 2+2+3.

## Instrumentation (for the MIDI)

Lead = tenor sax (GM prog 66, 0-indexed), Keys = Rhodes electric piano
(GM prog 4), Bass = fretless bass (GM prog 35), Drums = standard GM drum
kit on the dedicated drum channel. Keys and Drums are not written out in
`song.abc` — see below for why — they're generated programmatically in
`make_midi.py` directly from the same chord chart / drum table described
above and in `drums.md`, so all three documents describe one consistent
piece, they're just split across a hand-notated ABC lead sheet (melody +
bass, the two parts the brief explicitly asks to see as notation) and a
script for the two backing/accompaniment parts.

## What I produced

- `song.abc` — 2-voice ABC (Lead melody with chord symbols above it = the
  lead sheet, and Bass) for all 20 bars. Parses cleanly with music21 (used
  only as a generic ABC-parsing library, not as a composition aid) — I
  checked pitch content and rhythmic durations note-by-note against my
  intended chart and they match.
- `drums.md` — prose + per-section grid description of the drum pattern.
- `make_midi.py` — a from-scratch script: parses `song.abc` with music21 to
  get exact Lead/Bass note events, generates Keys comping and Drums
  programmatically from explicit chord/rhythm tables mirroring the text
  above, and assembles everything into one multi-track file with
  pretty_midi.
- `song.mid` — successfully generated. Verified by reading it back with
  pretty_midi: 4 instruments (Lead/Keys/Bass/Drums, Drums correctly flagged
  `is_drum=True`), total length 52.5s (= 20 bars x 2.625s, matches the
  intended tempo/meter exactly), tempo 80 quarter-bpm (= 160 eighth-bpm),
  time signature 7/8, note counts and pitch ranges all sane and matching
  the chart above. I have not listened to the audio — I have no audio
  playback/rendering (e.g. no soundfont synthesis) available in this
  environment, so this is a structural/data verification only, not an
  audition. See caveats below.

## ABC / tooling problems hit (and how I worked around them)

- **First attempt failed:** I initially wrote the ABC with repeated `V:1`
  / `V:2` header lines once per 4-bar system (the normal way to lay out
  interleaved multi-voice ABC for human readability). music21's ABC parser
  turned that into 12 separate parts instead of 2 — it doesn't merge
  same-ID voices that are re-declared multiple times through the tune body
  the way I expected. Fix: keep each voice's music contiguous (all 20 bars
  of Lead in one block, then all 20 bars of Bass in one block), only
  declaring `V:1`/`V:2` once each. That parses as 2 usable parts (plus 2
  harmless empty ones from the header-only declaration lines, which I just
  filter out by checking for nonzero duration).
- **Second problem:** I originally tried a real key-signature change at the
  climax (`[K:D]` inline, bracketed field before the first note of bar 17)
  to move from D Dorian to D major. I tested this in isolation and
  confirmed with a minimal repro that music21's ABC parser silently ignores
  an *inline* `[K:D]` bracketed field — notes after it kept using the old
  key signature (F stayed natural instead of becoming F#). A standalone
  `K:D` on its own line *does* work in my repro. Rather than depend on that
  parser-specific behavior (and risk a different renderer/parser handling
  it differently), I dropped the formal key change entirely and just wrote
  explicit accidentals (`^F`) for the one place in bars 17-20 that actually
  needed a sharp (the F# in bar 19's Bm7 melody/bass). This is less
  "idiomatic" for a human sight-reading the chart (no visual courtesy key
  signature change) but is unambiguous and verified-correct in the actual
  parsed output, which I prioritized.
- Both of these were caught by actually parsing the ABC with music21 and
  dumping the resulting note-by-note offsets/pitches/durations to compare
  against what I intended, rather than assuming the text was correct — I'd
  recommend that verification step to anyone using an LLM to hand-write ABC.

## Honest confidence / caveats

- **Structural correctness: high.** I verified the ABC parses to exactly
  the pitches/rhythms I intended (dumped and checked every note), and the
  final MIDI's duration/tempo/time-signature/instrument/note-count math all
  checks out against hand calculation. I'm confident the file is not
  broken.
- **Musical quality / "does it actually sound good and feel like 7/8 done
  well": medium confidence at best.** I have no way to render and listen to
  this in the current environment, so everything about groove feel,
  whether the 2+2+3 <-> 3+2+2 grouping shift actually reads as "unsettled"
  rather than just "different," voicing balance between Keys/Bass/Lead, and
  whether the climax genuinely lands as "triumphant" rather than just
  "louder," is untested by ear. This is exactly the kind of judgment that
  benefits from an actual listen-back-and-iterate loop, which I did not
  have available here.
- **7/8 interpretation:** I read "tempo fast (150-170 bpm felt per
  eighth-note grouping)" as the eighth-note pulse itself running at
  150-170/min (so I picked 160), rather than the bar/dotted-quarter pulse.
  I think this is the more natural reading of the phrase, but it's the
  single biggest interpretive judgment call in the brief and I could be
  wrong about which was intended — if the intent was closer to "160 quarter
  notes per minute, subdivided into 7/8," the piece as written would be
  roughly twice as fast/frantic as intended.
- **Emotional arc:** I encoded "restless -> unsettled -> triumphant release"
  through fairly blunt, textbook devices (grouping displacement, altered
  dominants, ascending sequences, then modal brightening + sustained notes
  + hi-hat-to-ride + crash cymbals). These are reasonable, idiomatic tools
  for the job, but I'd call the arc "plausible on paper," not something
  I've confirmed actually reads that way to a listener.
- **Keys/Drums parts are not hand-composed the way the Lead/Bass are** —
  they're generated by simple, fairly mechanical rules (fixed two-stab
  comping rhythm per bar; a hand-designed but not audited drum table).
  They're functional and consistent with the harmony/form, but less
  individually "composed" than the lead sheet parts.
- No use of any project-specific composition methodology, reference
  library, or online lookup — this is entirely general knowledge, as
  instructed for this baseline run.

# "Settling In" — working notes (baseline attempt, no specialized tooling)

## Brief, as I read it
Laid-back neo-soul/chill-jazz instrumental, C minor, 4/4, ~78 BPM, 16-24 bars.
Arc: quiet late-night self-doubt -> calm, unforced acceptance (not a big ending,
just settling). Deliverables: lead sheet (melody+chords), bassline, drum
pattern, finished multi-track file.

## Form
20 bars total, in four 4-8 bar phrases. I mapped the emotional arc onto both
harmony and drum density rather than just tempo/dynamics, since a static groove
for 20 bars would undercut the "arc" requirement.

- **Bars 1-8 (A — self-doubt, circling).** Mostly i and iv (Cm7, Fm7), one bar
  of ii7b5-V7alt (Dm7b5 - G7b9) as a moment of real tension/questioning, then
  back to Cm7 and a soft landing on bIII^maj7-ish borrowed color (Abmaj7) to end
  the phrase without resolving anything. Melody is sparse and hesitant
  (deliberately full of rests) and reuses the same 2-bar motif twice (bars 1-2
  and 7 echo each other) — the idea being that self-doubt doesn't develop, it
  loops.
- **Bars 9-16 (B — searching, opening up).** More harmonic motion: Fm7-Bb7
  (secondary dominant motion) into Ebmaj7-Abmaj7 (the relative-major pair,
  the "brighter" moment), then the Dm7b5-G7 tension returns in bars 13-14 but
  weaker (no b9 this time, drums pull back instead of pushing) before settling
  onto Cm7 and a Cm7/Eb (bass moves to the 3rd, softening the harmony) by
  bar 16. Melody range opens upward here (reaches a C6 peak in bar 9-10) —
  meant to read as "reaching," then it steps back down.
- **Bars 17-20 (Outro — settling).** Plagal-ish iv-bIII-iv motion (Fm7-Abmaj7-
  Fm7) with the melody in long half notes, no syncopation, into a final bar
  that is just Cm(add9) held (root-b3-5-9), melody landing on Eb (the minor
  3rd, not the bare root) with a fermata. Deliberately *not* a V7-i authentic
  cadence — I wanted the ending to feel arrived-at rather than resolved-with-
  force, per the brief's "not a big triumphant ending, just settling."

## Chords (bar-by-bar)
1 Cm7 | 2 Cm7 | 3 Fm7 | 4 Fm7 | 5 Dm7b5 | 6 G7(b9) | 7 Cm7 | 8 Abmaj7 |
9 Fm7 | 10 Bb7 | 11 Ebmaj7 | 12 Abmaj7 | 13 Dm7b5 | 14 G7 | 15 Cm7 | 16 Cm7/Eb |
17 Fm7 | 18 Abmaj7 | 19 Fm7 | 20 Cm(add9)

Rhodes voicings are rootless-ish shells (3-5-b7-9 where it fit, 3-5-b7 for the
half-diminished/dominant shells) rather than root-position triads, since
block root-position chords read more "cocktail piano" than neo-soul.

## Melody idea
Built around a small motif (Eb5-C5, a descending minor third) stated in bar 1,
answered by a falling Cm7 arpeggio in bar 2, then transposed onto Fm7 in bars
3-4. The tension bars (5-6, 13-14) each introduce one deliberate chromatic
non-diatonic tone (B-natural, the 3rd of G7, which needs an explicit natural
sign against the Cm key signature) as the "questioning" gesture, resolving
by half-step up into C. Section B widens the range and adds a bit more
forward motion (steps instead of static repetition). The outro thins the
melody down to single long tones and ends on a held Eb over the final chord.

## Bass idea
Mostly root + arpeggiated chord tone on beat 3 (root-3rd-5th shapes), half
note on beat 1 to leave room, dropping to just a held root with rests in the
sparser bars (2, 4, 15-19) to match the "quiet"/"settling" parts of the arc.
Final bar is a held whole-note C3 root under the Cm(add9) chord.

## Drum/groove idea
See `drums.json` for the actual data. Conceptually: an "intro" groove (just
kick on 1 + a soft quarter-note hihat pulse, no snare) for bars 1-2, a "main"
pocket groove (kick on 1 and the "a" of 3, snare/ghost-snare on 2 and 4 with
a soft ghost before beat 3, 8th-note hihat with light accent pattern) for
bars 3-8 and again 13-14, a slightly busier "sectionB" groove for bars 9-12
(extra kick + extra ghost snare, reflecting the "searching" energy), a "calm"
groove for bars 15-16 (kick on 1 only, soft backbeat only on 4) as the
transition into the outro, an "outro" groove for 17-19 (half-time hihat pulse,
no snare at all), and a near-silent "final" groove for bar 20 (a single soft
kick, nothing else — deliberately no cymbal swell/fill, since the brief asked
for settling, not a triumphant finish).

I did not attempt swing/ghost-note realism beyond what's in the JSON — no
random humanization of the *pattern* itself, only of timing/velocity in the
MIDI render (see below). A real production would probably add more ghost
notes and some hihat-openness variation; I kept the pattern simple and
readable rather than maximally idiomatic.

## Honest uncertainties / things I'm not fully sure about
- **Emotional arc mapping is a judgment call.** I don't have a reliable way to
  verify that "Dm7b5-G7b9 in bars 5-6" actually reads as "self-doubt" to a
  listener versus just "jazz ii-V." I leaned on fairly conventional cues
  (static/repetitive harmony + sparse melody = introspective; more chord
  motion + wider range = searching; plagal motion + long tones + soft dynamics
  = settling) but this is a plausible interpretation, not a validated one.
- **The C6 peak in bars 9-10 (lead)** might sit outside a comfortable range
  for some lead instruments (e.g. alto sax's practical top range is roughly
  Eb6, so it's technically playable, but it's a stretch for a "laid-back"
  piece — a mellower instrument choice or an octave-down alternative might
  read better). I kept it because it's the one place the melody "reaches,"
  but flagging it as a spot I'd reconsider on a second pass.
- **No swing/groove template applied to the ABC file itself** — the ABC is
  written in plain quantized note values (as a lead sheet should be); the
  "laid-back" pocket feel is only expressed in the MIDI render via a small
  fixed micro-timing delay on off-beat notes and drum ghost notes, not in the
  notation. This matches how a real lead sheet works (performer/producer
  supplies the feel), but means the ABC alone, if played back literally
  quantized, will sound stiffer/more "on-the-grid" than intended.
- **ABC and MIDI were authored in parallel from the same bar-by-bar plan**,
  not generated from one another (I don't have a hand-rolled ABC parser here,
  and didn't want to lean on any specialized conversion tooling). I
  cross-checked every bar's pitches/durations by hand between the two, and
  additionally validated `song.abc` by parsing it with `music21`
  (generic library, not a specialized skill):
  - First attempt used inline `[V:1]`/`[V:2]`/`[V:3]` markers at the start of
    each line. music21 parsed this *wrong* — it silently concatenated all
    three voices end-to-end into one 240-quarter-length stream instead of
    layering them. I rewrote the file using the more standard convention
    (`V:1` alone on its own line, not bracketed) and re-validated.
  - After the rewrite, music21 parses each voice's notes/rests correctly and
    the chord symbols (`"Cm7"`, `"G7b9"`, etc.) come through as proper
    `ChordSymbol` objects with the expected pitch content (spot-checked
    several against my plan — e.g. bar 8 parses as Ab5-G5-Eb5-rest, exactly
    as intended). Each of the three sections (bars 1-8, 9-16, 17-20) sums to
    the expected number of quarter-lengths (32, 32, 16) for all three voices,
    so there's no missing or extra material.
  - One remaining music21-specific quirk: because `V:1`/`V:2`/`V:3` recur
    across three separate section blocks in the file, music21 creates a new
    `Part` object each time a voice letter reappears (12 parts total) instead
    of merging same-named voices back into one continuous part. This is a
    limitation of music21's ABC importer, not (as far as I can tell) an error
    in the notation itself — repeating `V:n` per section is standard ABC 2.1
    practice that renderers like abcjs/abc2midi handle as "continue this
    voice." I don't have abcjs or abc2midi installed in this environment to
    cross-check against a more complete ABC toolchain, so I can't fully rule
    out a subtler compatibility issue beyond what music21 caught.
- **Chord symbols vs. rhodes voicings**: the chord symbols printed above the
  lead line (e.g. "G7b9") describe the harmonic function; the actual Rhodes
  voicing sounding underneath is a rootless upper-structure shell, not a
  literal spelling of every extension in the symbol. This is normal lead-sheet
  practice but worth noting in case someone expects the Rhodes voice to be a
  literal chord-symbol realization.
- I am **moderately confident** in the harmonic/melodic content as reasonable,
  idiomatic neo-soul-adjacent material, and **fairly confident** the MIDI file
  is technically valid (tempo/time-sig/instruments/notes load correctly) — see
  the generation log noted at the bottom of this file. I am **less confident**
  that the piece actually delivers the specific emotional arc described in the
  brief in a way a listener would recognize without being told what to listen
  for; that's inherently a subjective/perceptual claim I can't verify from
  first principles alone.

## Files
- `song.abc` — lead sheet: 3 voices (Lead melody w/ chord symbols, Rhodes
  comping, Bass), 20 bars, K:Cmin, M:4/4, Q:1/4=78.
- `drums.json` — drum pattern as 16th-note-step grooves + a bar->groove map,
  GM drum note numbers, plus a legend.
- `generate_midi.py` — the from-scratch script (using `pretty_midi`) that
  encodes the same bar-by-bar note data as `song.abc`/the bass section/the
  drum grooves, applies tempo/instrument assignment and light humanization,
  and writes `song.mid`.
- `song.mid` — rendered multi-track MIDI (Lead, Rhodes, Bass, Drums).

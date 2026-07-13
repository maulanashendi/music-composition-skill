# ABC notation for jazz lead sheets and compact scores

ABC is a text notation format. Renderer support varies. Generate portable core syntax first, then add advanced features only when necessary.

## 1. Minimum header

Use:

```abc
X:1
T:Title
C:Composer
M:4/4
L:1/8
Q:1/4=120
R:Medium Swing
K:C
V:Melody clef=treble name="Melody"
```

Recommended optional fields:

- `S:` source or brief;
- `Z:` transcription or generation note;
- `P:` part order when supported;
- `%%score` for multi-voice layout when renderer supports it;
- comments beginning with `%`.

Place global header fields before the first `K:`. Declare voices in the header or before their first use.

## 2. Notes and octaves

In standard ABC pitch notation:

- `C D E F G A B` are the octave around middle C beginning at middle C;
- lowercase `c d e f g a b` is one octave higher;
- comma lowers an octave: `C,`;
- apostrophe raises an octave: `c'`;
- sharp: `^F`;
- flat: `_B`;
- natural: `=F`.

Use key-aware spelling. In `K:F`, B is flat by default, so write `B` for Bb and `=B` for B natural.

## 3. Default length and duration

`L:` defines the default unit. With `L:1/8`:

- `C` = eighth note;
- `C2` = quarter note;
- `C4` = half note;
- `C8` = whole note;
- `C/2` = sixteenth note;
- `C3/2` = dotted-eighth duration;
- `z` = rest;
- `x` = invisible rest or spacing rest where supported.

Each bar's total duration must match `M:` except a valid pickup and its complementary final bar, explicit multi-measure rests, or a documented cadenza/free-time passage.

## 4. Chord symbols and annotations

Place quoted chord symbols immediately before the onset they govern:

```abc
"Dm7"D2 F2 A2 c2 | "G7"B2 A2 G2 F2 |
```

Use portable ASCII chord text:

- `Cmaj7`;
- `Dm9`;
- `G7b9`;
- `Bm7b5`;
- `F#dim7`;
- `A7sus4`;
- `D/C`.

Use annotations:

- `"^A"` above the staff;
- `"_cue"` below when supported;
- `% Solo on form x2` as a comment for non-notated instructions.

Chord symbols are not bracketed note chords. Quoted text such as `"Cmaj7"` is metadata; `[CEG]` is a sounding notated chord.

## 5. Bar lines and repeats

Common bar syntax:

- `|` regular bar;
- `||` double bar;
- `|]` final bar;
- `|:` repeat start;
- `:|` repeat end;
- `[1` first ending;
- `[2` second ending.

Write repeat logic so a performer can count the form. For complex roadmaps, prefer explicit sections and comments over nested repeats that may render inconsistently.

## 6. Pickup or anacrusis

ABC normally represents a pickup as an incomplete first bar. The final bar may complete the missing duration.

Example in 4/4 with `L:1/8`, two-eighth pickup:

```abc
G A | B2 c2 d2 e2 | f4 e2 d2 | c6 |]
```

The validator accepts a partial first and final bar when their durations sum to one full bar. If the tune ends with a full bar after a pickup, add an explicit rest or state that the final phrase is intentionally extended.

## 7. Ties and slurs

Tie same pitch across duration or bar line:

```abc
C4-C4 | C8 |
```

Slur a phrase:

```abc
(C D E F) G4 |
```

A tie affects articulation, not total bar duration. Each tied segment still occupies written time.

## 8. Tuplets

Triplet:

```abc
(3CDE
```

General form:

```abc
(p:q:r
```

where `p` notes are played in the time of `q`, applied to `r` following note events. Use explicit form for uncommon tuplets.

Examples:

```abc
(3CDE F2 G2 |
(5:4:5 CDEFG A3 |
```

The bundled validator handles common tuplets and explicit `p:q:r` forms. Manually inspect nested tuplets or renderer-specific behavior.

## 9. Broken rhythm

`>` lengthens the preceding note and shortens the following note; `<` does the reverse.

```abc
C>D E<F |
```

Repeated marks increase the ratio, for example `C>>D`. Use for notated unequal rhythms, not as a universal replacement for swing feel.

## 10. Grace notes

Grace notes use braces:

```abc
{^C}D2
```

Grace notes normally do not consume metrical duration in the validator. Renderer and performance practice determine exact execution.

## 11. Notated chords

Use brackets for simultaneous notes:

```abc
[CEG]4 [DFA]4 |
```

A duration after the closing bracket applies to the chord event. The validator supports standard bracketed chords. Complex independent lengths inside a chord require manual review.

## 12. Decorations and articulations

Portable examples include:

- `.` staccato;
- `>` accent may conflict with broken-rhythm syntax, so prefer named decoration when supported;
- `!accent!`;
- `!tenuto!`;
- `!fermata!`;
- `!trill!`;
- `!crescendo(!` and `!crescendo)!` in supporting renderers.

Use comments when portability is uncertain.

## 13. Inline fields

Inline changes can use:

```abc
[M:3/4]
[L:1/16]
[K:Gm]
[Q:1/4=96]
[V:Trumpet]
```

The validator tracks inline meter, default length, key, tempo metadata, and voice changes in its supported subset. Keep changes at bar boundaries unless a deliberate advanced notation requires otherwise.

## 14. Multiple voices

Declare voices:

```abc
V:Melody clef=treble name="Melody"
V:Bass clef=bass name="Bass"
```

Switch voices:

```abc
[V:Melody] C2 D2 E2 F2 |
[V:Bass] C,4 G,,4 |
```

For polyphony, each voice should contain valid bar durations. Use `%%score` if the renderer supports grouping.

A lead sheet should normally use one melody voice plus chord symbols. Add voices for fixed counterlines, bass riffs, or ensemble hits only when requested.

## 15. Lyrics

A lyric line can use `w:` after the corresponding music line. Hyphens divide syllables, underscores extend syllables, and asterisks skip notes in common ABC practice.

Check renderer behavior and prosody manually. The validator does not assess lyric-note alignment.

## 16. Parts and roadmap

Use `P:` or comments for parts when supported:

```abc
P:A
"^A" ...
P:B
"^B" ...
```

For a jazz performance roadmap, comments are often clearest:

```abc
% Intro: piano rubato, 4 bars
% Head in: AABA
% Solos: form x3, backgrounds on final A
% Head out, tag last 2 bars x3, cut off
```

## 17. Swing and groove directions

Normally notate equal eighths and state:

```abc
R:Medium Swing
% Swing eighths; do not play dotted-eighth/sixteenth mechanically
```

For bossa, funk, Afro-Cuban, or mixed-meter pieces, include the named feel and grouping in `R:` and comments. ABC chord symbols alone cannot encode a groove.

## 18. Free time and cadenzas

ABC support for unmetered passages differs. Options:

- use `M:none` if renderer supports it;
- use a temporary meter with comments;
- use invisible rests and fermatas;
- notate a proportional sketch;
- provide text instructions outside the staff.

Disclose validator limitations for truly free notation.

## 19. Transposing instruments

For a concert lead sheet, keep chord symbols and melody at concert pitch.

For transposed parts:

- write each voice at its actual written pitch;
- label instrument and transposition;
- use explicit `K:` per voice where needed;
- verify octave-transposing instruments manually.

Renderer-specific `transpose` directives are not universally portable. Explicitly transposed notes are safer.

## 20. ABC generation workflow

1. lock meter, default length, key, tempo, form, and pickup;
2. enter melody without chord symbols;
3. validate note durations;
4. add chord symbols at exact onsets;
5. add repeats, endings, and section labels;
6. add arrangement comments;
7. add additional voices only if required;
8. run `scripts/validate_abc.py`;
9. repair errors;
10. render in at least one ABC-capable application when available.

## 21. Validator scope

The bundled validator checks:

- required headers;
- parseable meter and default length;
- balanced quoted annotations;
- notes, rests, bracket chords, ties, grace groups, common tuplets, broken rhythm, repeats, endings, and multiple voices;
- inline meter, length, key, tempo, and voice changes;
- bar durations;
- pickup and complementary final bar;
- basic voice consistency.

It warns about:

- overlays;
- nested or unusual tuplets;
- internal independent lengths in bracket chords;
- unmetered notation;
- complex part expansion;
- renderer-specific directives;
- advanced decorations;
- lyrics and transposition semantics.

A pass does not guarantee identical rendering in every ABC implementation.

## 22. Delivery requirements

For a full composition, provide:

- ABC source in a code block;
- a `.abc` file when file creation is available;
- validation output;
- disclosed warnings;
- a statement of whether the notation is concert pitch;
- comments for improvisation and arrangement information not encoded as fixed notes.

## 23. Extreme syncopation and staccato in ABC

For dense sixteenth-note displacement, prefer `L:1/16` so rests, late attacks, and ties can be expressed directly. A staccato mark changes articulation, not the bar-duration calculation.

Portable syntax:

```abc
L:1/16
z3 .E z .G z2 !accent!A3 z c B3- |
B z .A z2 .G z .E2 z2 .D z .C2 z |
```

Interpretation:

- `z3` delays the first attack until the fourth sixteenth-note position;
- `.E` and `.G` are staccato attacks;
- `!accent!A3` applies a selective accent to a sustained note;
- `B3- | B` ties the same pitch across the bar line and suppresses a new attack on the next downbeat.

For a two-hand piano example, keep each voice metrically complete and distinguish rhythmic function:

```abc
X:1
T:Extreme Syncopation and Staccato Piano Cell
M:4/4
L:1/16
Q:1/4=116
K:Cm
V:RH clef=treble name="Right Hand"
V:LH clef=bass name="Left Hand"
[V:RH]
z3 !accent!.E z .G z2 A3 z .c B3- |
B z .A z2 !accent!.G z .E2 z2 .D z .C2 z |
[V:LH]
"Cm7"[C,G,B]4 z4 [C,G]4 z4 |
"Abmaj7"[A,E,G]4 z2 [A,E]2 z4 [G,D]4 |
```

When generating this technique:

1. count every voice independently against the meter;
2. use rests to expose displaced attacks rather than filling all subdivisions;
3. tie only identical pitches;
4. do not assume `.` changes note length for validation purposes;
5. state `senza pedal` or a restrained-pedal direction in comments when articulation clarity is essential;
6. validate the ABC and manually inspect renderer support for named decorations such as `!accent!`.

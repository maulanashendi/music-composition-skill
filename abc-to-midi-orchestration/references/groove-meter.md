# Groove, meter, subdivision, and rhythmic design

> Adapted from `jazz-composition-designer` (archived portable skill package,
> consolidated 2026-07-13). Note this package's `abc_to_midi.py`/music21
> pipeline is not restricted to a single meter, but if the downstream target
> is the `daw_generative` engine (`POST /api/render`), that engine currently
> only realizes `4/4` — check the target pipeline before composing in an
> odd or compound meter. §22 below points to `advanced-microtiming.md`,
> which now also has a distilled numeric table in
> `references/groove-profiles.md`.

Meter defines the recurring measure structure. Feel defines how subdivisions, accents, articulation, and microtiming are performed. Groove emerges from the relationship among all parts.

## 1. Reading a time signature

The upper number indicates counted units per bar. The lower number indicates the notated unit.

Examples:

- 4/4: four quarter-note units;
- 3/4: three quarter-note units;
- 6/8: six eighth-note units, often grouped 3+3;
- 7/8: seven eighth-note units, often grouped 2+2+3 or another pattern.

The time signature alone does not define genre or feel.

## 2. Common meters

### 1/4

One quarter-note unit per bar. Rare as a sustained meter; useful for inserted beats, abrupt cuts, or metric re-framing.

### 2/4

Two quarter-note units. Common in march-related, ragtime-related, samba-related, and two-beat contexts. A piece notated in 4/4 can still be felt in two.

### 3/4

Three quarter-note units. Supports jazz waltz, ballad, straight or swung triple meter, cross-rhythm, and modern comping.

### 4/4

Four quarter-note units. Supports swing, bebop, blues, bossa, samba-related notation, funk, fusion, smooth, straight-eighth, and free-time-with-pulse approaches.

### 5/4 or 5/8

Group as 3+2, 2+3, or another explicit pattern. Keep the riff and accents consistent enough to be heard, then vary deliberately.

### 6/8

Usually two main beats, each divided into three. Supports Afro-diasporic, gospel, ballad, shuffle-related, and fusion contexts. Do not treat it as interchangeable with 3/4.

### 7/4 or 7/8

Common groupings: 4+3, 3+4, 2+2+3, 3+2+2. Define the grouping through bass, drums, and melody.

### 9/8

Can be compound 3+3+3 or additive 2+2+2+3 and other groupings. State the intended pattern.

### 12/8

Four main beats divided into three. Useful for slow blues, gospel, shuffle, soul-jazz, and compound-meter ballads.

## 3. Swing feel

Swing is not a fixed dotted-eighth/sixteenth ratio. It combines:

- unequal or flexible eighth-note placement;
- triplet-derived phrasing;
- articulation;
- accents;
- ride-cymbal phrasing;
- walking or two-feel bass;
- microtiming among players;
- forward motion and relaxation.

The ratio tends to become more even at faster tempos and may vary by era and player. In ABC, normally notate equal eighths and mark swing as a performance direction.

## 4. Two-feel and walking four

### Two-feel

Bass emphasizes two larger beats per 4/4 bar, often roots and fifths or longer lines. Useful for introductions, early choruses, lighter texture, or traditional and swing contexts.

### Walking four

Bass articulates four beats, connecting harmony continuously. It can increase momentum and make changes clear.

An arrangement may move from two-feel to walking four to shape energy.

## 5. Shuffle

Shuffle uses triplet-based long-short subdivision with a strong repeated feel. Distinguish:

- light swing;
- medium shuffle;
- heavy backbeat shuffle;
- 12/8 slow blues.

Drum, bass, and comping must agree on subdivision and accent profile.

## 6. Straight eighths

Equal eighth-note subdivision can support:

- bossa nova;
- samba-related jazz;
- fusion;
- rock or funk influence;
- contemporary acoustic jazz;
- odd-meter compositions.

Straight subdivision does not mean rigid performance. Microtiming and articulation remain expressive.

## 7. Bossa-nova-related feel

Treat bossa nova as a Brazilian song and guitar-derived practice, not generic soft jazz.

Core considerations:

- understated dynamics;
- syncopated chord attacks;
- bass pattern that supports roots and fifth-related motion without copying a walking line;
- melody floating across the groove;
- stable pulse often felt in two;
- smooth voice leading.

Do not force swing articulation. Do not claim authenticity from a single stock rhythm.

## 8. Samba-related feel

Samba-related jazz generally has more active percussion and forward motion than bossa. Consider:

- two-beat macro pulse;
- layered subdivisions;
- syncopated bass and chord patterns;
- percussion roles;
- ensemble hits;
- tempo-specific playability.

Identify the requested Brazilian tradition when possible rather than using "samba" as a universal label.

## 9. Afro-Cuban clave awareness

Select an actual framework such as 2-3 or 3-2 son clave, rumba clave, or another named pattern. Melody, bass, montuno, and horn figures should not contradict the chosen direction unless a deliberate cross-clave effect is designed.

Composition process:

1. choose clave orientation;
2. mark the two-bar cycle;
3. align major ensemble hits;
4. design bass tumbao and piano montuno roles;
5. test melodic accents;
6. maintain or explicitly flip clave only at a structurally valid point.

Do not invent a generic "Latin" pattern.

## 10. Caribbean and African-influenced frameworks

When the brief names a specific tradition, identify its meter, bell pattern, timeline, subdivision, and ensemble roles. Avoid flattening distinct traditions into one category.

For a general hybrid with insufficient detail, describe it honestly as an influence and keep the groove rules simple and internally consistent.

## 11. Jazz waltz

Jazz waltz may use:

- clear 1-2-3 pulse;
- dotted-quarter cross-rhythm;
- walking in three;
- one bass note per bar;
- syncopated comping;
- 3-over-2 implication;
- sections that feel in one at fast tempo.

It is not automatically classical. Harmony and articulation can be bluesy, modal, bop-derived, or contemporary.

## 12. Funk and jazz-funk

Core elements:

- stable 4/4 or explicit odd-meter groove;
- backbeat;
- syncopated bass riff;
- interlocking guitar, keyboard, and percussion parts;
- repeated vamp;
- ghost notes and articulation;
- sectional breakdown and rebuild.

Harmonic density is often lower than in bebop. Groove variation, timbre, and arrangement create form.

## 13. Fusion and rock-related feel

Possible elements:

- straight eighths or sixteenths;
- electric bass and drums;
- odd meters;
- riff-based harmony;
- rock backbeat;
- long-form development;
- metric modulation;
- electronic timbre.

Do not equate technical complexity with musical quality.

## 14. Hip-hop-informed jazz

Possible relationships include:

- loop-based form;
- swung or straight sixteenth-note pocket;
- sampled or sample-like texture;
- backbeat and sub-bass emphasis;
- repeated harmonic cell;
- improvisation over production layers.

Hip-hop-informed jazz is not simply jazz-funk. Define the beat, loop, and production relationship explicitly.

## 15. Odd meter

To make odd meter playable:

- choose grouping;
- encode grouping in riff and bass;
- keep at least one layer clear;
- use repeated cycles before adding displacement;
- cue section transitions;
- simplify harmony at fast tempo if needed.

Example 7/4 grouped 4+3:

Count 1 2 3 4 | 1 2 3.

A melody may cross the grouping, but drums or bass should preserve a reference layer.

## 16. Polyrhythm and cross-rhythm

Polyrhythm layers different subdivisions over the same time span. Cross-rhythm emphasizes a grouping that conflicts with the meter.

Examples:

- 3 over 2;
- dotted-quarter accents across 4/4;
- five-note grouping over four beats;
- 4 over 3 in a waltz.

Define which layer controls the bar line and how players return to it.

## 17. Polymeter

Polymeter layers different meter cycles over a shared pulse. Use sparingly and specify the common subdivision, cycle length, and convergence point.

ABC lead-sheet notation may not represent complex polymeter clearly. Use separate voices, comments, or a full-score format outside ABC when needed.

## 18. Metric modulation

Metric modulation reinterprets one note value or subdivision as the new pulse. Specify the equivalence, for example:

old eighth-note triplet = new eighth note.

Provide a written cue, rehearsal mark, and count-in or transition figure.

## 19. Rubato, free time, and time-no-changes

### Rubato

Tempo flexes around a shared phrase. Define who leads and where pulse returns.

### Free time

No regular pulse. Organize by breath, cue, duration, texture, or motif.

### Time-no-changes

Pulse and groove continue while fixed chord changes are removed or loosened. Define center, bass behavior, and interaction boundaries.

## 20. Microtiming

Players may phrase:

- ahead of the beat;
- on top of the beat;
- behind the beat;
- with laid-back backbeat;
- with forward ride or bass motion.

Do not notate microtiming as wrong note values unless the displacement is structural. Use performance directions.

## 21. Groove audit

Check:

- Do bass, drums, comping, and melody agree on subdivision?
- Is the meter grouping audible?
- Are major accents compatible with clave or timeline?
- Does harmonic rhythm fit the tempo?
- Are syncopations playable and breathable?
- Is the groove stable enough for intentional displacement?
- Does each section change energy without losing identity?
- Are performance directions sufficient without over-notation?

## 22. Extreme syncopation and staccato piano writing

Use extreme syncopation as controlled metric displacement, not random rhythmic clutter. Preserve at least one audible reference layer in the bass, drums, left hand, or recurring ostinato while the melodic layer attacks weak subdivisions, omits expected downbeats, or sustains across bar lines.

Design principles:

- place selected attacks on late sixteenths, offbeat eighths, or the final subdivision before a beat;
- use rests before accented notes so the displaced onset is perceptually clear;
- tie notes across strong beats or bar lines to suppress the expected re-attack;
- alternate compact staccato cells with tied or sustained tones to create articulation contrast;
- use accents selectively; do not accent every syncopated note;
- keep a recognizable motif, contour, or pitch cell so rhythmic complexity remains coherent;
- maintain a stable reference layer when the melody becomes highly displaced;
- avoid pedal blur in passages whose identity depends on short releases and silence.

For piano, distinguish the roles explicitly:

- right hand: fragmented, syncopated melodic cells, anticipations, accents, and staccato attacks;
- left hand: simpler chordal pulses, bass anchors, ostinato, or strategically placed responses;
- both hands: use coordinated ensemble hits only at structural landmarks so constant unison does not weaken the independence of the layers.

A practical escalation sequence:

1. write a clear 4/4 reference groove;
2. displace one melodic attack by a sixteenth;
3. replace a downbeat attack with a rest;
4. tie a phrase ending across the next downbeat or bar line;
5. add staccato to short cells and retain selected legato/tied tones;
6. verify that the bar line is still inferable from another layer;
7. test slowly without pedal before raising tempo.

Quality checks:

- the syncopation must be countable and reproducible;
- ties must connect identical pitches and must not create an unintended re-attack;
- staccato must shorten performed duration without altering the notated metric duration;
- the passage must remain playable at the stated tempo;
- silence must function as part of the groove rather than as accidental emptiness.

## 23. Advanced microtiming output

For DAW-first, lofi, jazzhop, neo-soul, sample-like, or explicit pocket requests, the per-role tick offsets, velocity ranges, and gate behavior live in `advanced-microtiming.md` (the "why") and `groove-profiles.md` (the numeric table) — read those rather than re-deriving them here. Keep notated displacement separate from performance offsets.

# Cool & modal jazz — genre profile

Adapted from a cool-jazz/modal-jazz style brief (submitted 2026-07-20,
translated and restructured into this package's conventions). **The
brief's worked ABC example ("Blue Modal Contemplation") is a reference
only, not a template to imitate note-for-note** — this file and the
Tier-1 template below stay at the level of chord vocabulary, phrasing
rules, and arrangement structure, the same instruction already applied to
`hiphop-jazz-genre.md`, `smooth-jazz-genre.md`, and `noir-jazz-genre.md`'s
source briefs. This deepens the existing "Modal" entry in
`style-cheatsheets.md`, now retitled "Cool & modal jazz" to cover the
wider family the brief describes — the cheatsheet stays the fast starting
point, this file is where the modal-voicing theory, brush-drumming detail,
and arrangement blueprint live.

Cool jazz and modal jazz emerged as a reaction against late-40s bebop's
aggressive, fast, virtuosic-display fatigue — bringing jazz back to
contemplation, breathing room, pure tone beauty, and structural
intelligence. **Do not copy** a specific recording, artist, or arrangement
literally — translate the reference into musical attributes (tempo,
texture, harmonic stasis, understated articulation, space). Identity comes
from **restraint** — both harmonic (modal stasis, §3) and melodic (the art
of leaving notes out, §4) — the calm, unhurried opposite of bebop's density
and jazz-funk's drive.

## Musical DNA baku

| Parameter | Default profile value |
|---|---|
| Tempo zone | 55-175 BPM depending on sub-style (see §2) — wide, but always "cool" in character even when fast |
| Meter | 4/4 is default; odd meters (5/4, 7/4, 9/8) are idiomatic when played smoothly, not stiffly (§2) |
| Tonal center | Modal — a single mode (usually Dorian) held for long stretches, not a fast-moving chord progression |
| Rhythmic grid | Brushed swing, floating/subdued pulse — bass and drums sit gently behind the beat without forcing hard accents; see the `cool-modal-floating` groove profile |
| Palette (role -> instrument) | Anchor: upright bass (pedal point) + brushed drums · Harmony: piano (sparse, interactive) or none at all (pianoless West Coast quartet, §1) · Lead: Harmon-muted trumpet, dry/breathy alto or tenor sax, baritone sax |
| Density ceiling | Extremely low, deliberately — one short motif, then 1-2 bars of rest, before development (§4) |

These are starting points, not law — bend toward the brief's specific
sub-style while staying inside the cool/modal family.

## 1. Sub-genres

| Sub-genre | Era | Character |
|---|---|---|
| West Coast cool jazz | Early 1950s | Very relaxed, elegant; often a **pianoless quartet**, emphasizing two-part counterpoint between horns (e.g. Chet Baker, Gerry Mulligan, Shorty Rogers, Dave Brubeck) |
| Modal jazz / structural minimalism | Late 1950s | Pioneered by Miles Davis (*Kind of Blue*), developed by John Coltrane — replaces fast chord progressions with a static mode, letting a soloist explore tonal color at length (e.g. Miles Davis, John Coltrane, Bill Evans, McCoy Tyner) |
| Chamber jazz / third stream | — | A crossing of European classical counterpoint with jazz's rhythmic swing structure; uses unusual instruments like French horn, flute, oboe/cello (e.g. Modern Jazz Quartet, Gil Evans Orchestra) |

## 2. Rhythmic feel & tempo matrix

- **Brushed swing / whispering beat** — wire brushes swept in a circular
  motion on the snare, creating a soft hiss background with no hard hits.
- **Floating 8ths / subdued pulse** — the rhythm feels weightless and
  relaxed; bass and drums often sit slightly behind the beat without
  forcing hard accents.
- **Odd-meter cool** — asymmetrical meters (5/4 as in "Take Five," or 7/4,
  9/8) played so smoothly and fluidly that they never feel stiff or
  academic.

| Sub-style / vibe | Category | BPM range | Character |
|---|---|---:|---|
| Cool ballad / nocturne | Slow drag | 55-72 | Intimate, hushed, soft Harmon mute, long tones, whispering brushes |
| Medium cool / modal walk | Sweet spot | 100-125 | Easy swing, relaxed, a "So What"-style bassline, wide breathing room |
| Up-tempo modal / West Coast | Fast contrapuntal | 140-175 | Stays "cool" even fast — winding counterpoint, minimal hard drum accents |

## 3. Harmony, modes, voicing & progressions (the modal framework)

Unlike pop or classic jazz's fast ii-V-I motion, modal jazz uses **modes**
as a canvas for emotional exploration, not a chord-change vehicle.

**Primary modes:**

- **Dorian (`1-2-b3-4-5-6-b7`)** — the single most crucial modal color:
  minor in character but neutral/elegant because of the natural 6th.
- **Mixolydian (`1-2-3-4-5-6-b7`)** — a relaxed, open dominant color with no
  excess tension.
- **Phrygian / Spanish Dorian (`1-b2-b3-4-5-6-b7`)** — exotic,
  introspective, melancholic (used on *Miles Ahead*/*Sketches of Spain*).

**Modal voicing techniques:**

- **The "So What" voicing (Bill Evans style)** — a voicing for `Dm7` (D
  Dorian): three stacked perfect 4ths, capped with a major 3rd on top.
  Notes (low to high): `E3-A3-D4-G4-B4`.
- **Quartal voicings** — build chords from stacked 4ths instead of 3rds/
  triads, removing major/minor certainty for an ambiguous, open, floating
  color. This is the harmonic engine underneath modal stasis — reference it
  by name; it is also documented in `harmony/references/voicing-systems.md`
  for the mechanical voicing detail, not restated here.

**Progression / cell library** (reference by name; pick and adapt, do not
restate verbatim in every song):

```
"So What / Impressions" form (32-bar AABA):
A section (16 bar): D Dorian (static Dm7).
B/bridge (8 bar): shift a half-step up to Eb Dorian (static Ebm7).
A section (8 bar): return to D Dorian (static Dm7).

Minor stepwise shift (2-chord cell):
| Dm7 (D Dorian) | Em7 (E Phrygian/Dorian) | Dm7 | Em7 |

West Coast pianoless contrapuntal cell (Gerry Mulligan style):
No chordal instrument at all - two independent melodic lines interlock:
Line 1 (trumpet): long guide-tone notes.
Line 2 (baritone sax): a low-register counter-melody.
```

## 4. Melody, motif, minimalism & space (the load-bearing section)

The key to cool/modal improvisation is not how many notes are played, but
how many are deliberately left out:

```
[ statement (2-3 notes) ] -> [ rest / silence (2 bar) ] -> [ development / variation ]
```

- **The power of rest** — silence is an instrument. Leave at least 1-2 bars
  of silence after a short melodic phrase.
- **Motivic development** — take a simple 3-note motif, repeat it in the
  next bar with a rhythmic displacement or a changed final note.
- **Focus on tone quality** — because so few notes are played, every note's
  tone color and articulation must be flawless; this is why §5's
  Harmon-trumpet/breathy-sax "secret recipes" matter as much as the notes
  themselves.

## 5. Instrument palette & "secret recipe" sound design

**Track setup:**

```
Lead instruments  : trumpet (Harmon mute), alto/tenor sax (dry/breathy), baritone sax
Chordal instruments: grand piano (soft touch / Bill Evans voicings), vibraphone
Bassline          : acoustic upright bass (pizzicato, warm resonance)
Drums/rhythm      : acoustic kit played with brushes (soft ride cymbal)
```

**Sound-design intent** (downstream — for whoever programs/mixes the
patch, not something this package's scripts implement, same framing as
`classic-jazz-genre.md` §9):

- **The Miles Davis Harmon-mute trumpet tone** — Harmon mute with the stem
  removed entirely, played close-mic'd; ribbon-mic emulation (RCA 44-BX
  style), tube-preamp saturation to soften transients, soft opto
  compression (2 dB gain reduction), a short studio-chamber reverb
  (~1.2s decay).
- **Breathy/dry saxophone (Paul Desmond/Stan Getz style)** — no vibrato
  (straight tone), a sub-tone technique where breath dominates over pitch;
  EQ: smooth high roll-off above 10 kHz, a gentle boost around 250-400 Hz
  for body warmth.
- **Bill Evans piano touch & voicings** — a soft-felt piano or a concert
  grand with a velocity curve tuned so quiet dynamics are easy to execute;
  mix: reduce percussive attack around 3 kHz, boost warmth around 200 Hz,
  spread the piano gently left-right (~25% L/R).

## 6. Groove engine, brush drumming & comping

**Drums:**

- **Brush swish** — the left hand sweeps the snare head in a continuous
  circular motion, the right hand adds a light ride accent.
- **Feathered bass drum** — an extremely light tap on beats 1-2-3-4,
  blending into the upright bass's own resonance rather than being heard
  as a separate hit.
- **Pedal hi-hat** — pressed softly on beats 2 and 4.

**Piano & bass interplay:**

- **Interactive comping** — the piano no longer strums a chord on every
  beat; it acts like a second soloist, offering short punctuation between
  the horn's phrases.
- **Pedal point / drone bass** — the bassline often holds a single note (a
  root pedal) for a dozen-plus bars, giving the modal stasis a strong
  foundation.

Groove detail (tick offsets, gate ratios) lives in
`../../groove-rhythm/references/groove-profiles.md` under the
`cool-modal-floating` profile — select it by name.

## 7. Vintage production intent (downstream — not this package's job)

As with every other genre file in this package, this package composes and
arranges; it does not mix audio. Record the brief's production intent here
as guidance for whoever renders/mixes (the "Columbia 30th Street Studio"
vibe):

```
[ dry acoustic tracks ] -> [ tube saturation ] -> [ intimate chamber reverb ] -> [ natural dynamics ]
```

- Cut sub-bass below 40 Hz; reduce modern brightness above 12 kHz.
- Chamber or warm wood-studio reverb, 20-30 ms pre-delay, 1.2-1.5s decay —
  avoid long, wet digital hall reverbs.
- Keep the master bus dynamics natural — no heavy limiting/compression;
  target loudness -14 to -16 LUFS, letting the music breathe.

## 8. Arrangement blueprint

```
[INTRO (BASS PEDAL)] -> [HEAD (MODAL MELODY)] -> [SOLO 1 (TRUMPET)] -> [SOLO 2 (SAX)] -> [HEAD RETURN] -> [OUTRO (FADE/STINGER)]
```

- **Intro (4-8 bar)** — the upright bass alone states a pedal-point motif
  under brushed drums; the piano enters sporadically with So What-style
  voicings.
- **Head/main theme (16-32 bar)** — the main melody is played
  unison or in simple counterpoint by two horns; calm, open, unhurried.
- **Solo section (modal exploration)** — soloists improvise over the
  Dorian/Mixolydian mode; the comping stays static and calm underneath.
- **Outro** — the main motif repeats, fading (*morendo*), ending on a
  suspended Harmon-mute note.

## 9. Four-genre comparison matrix

The fastest way to check whether a composition has drifted into a
neighboring genre — cross-reference against `classic-jazz-genre.md` and
`jazz-funk-genre.md` §9's three-way matrix, extended here to four:

| Element | Classic jazz | Soul jazz & jazz-funk | Smooth jazz | Cool & modal jazz |
|---|---|---|---|---|
| Dominant era | 1920s-1930s | Late 1950s-1970s | Late 1970s-2000s | 1950s-1960s |
| Main focus | Dance, collective improvisation | Groove, blues/gospel roots | Commercial melody, radio edit | Contemplation, space, mode |
| Rhythmic engine | Swing triplets | Swung 8ths / straight 16ths | Straight R&B 16th grid | Brushed swing / floating |
| Signature chord | Major 6, diminished 7th | Dominant 7(#9), minor 11th | Major 9, slash (`Fmaj7/G`) | So What voicing (stacked 4ths), modal stasis |
| Lead instrument | Trumpet, clarinet | Hammond B-3, sax, slap bass | Soprano sax, clean guitar | Harmon-muted trumpet, breathy sax |
| Sonic character | Vintage gramophone | Warm analog tube | Ultra-clean, "licked" | Intimate, dry room, minimal |
| Groove profile(s) | `classic-jazz-swing` | `soul-jazz-swing`, `fusion-tight`/`purdie-shuffle` | `smooth-jazz-rnb` | `cool-modal-floating` |

If a modal piece's harmony starts moving fast (ii-V chains every bar), it
has drifted toward bebop, not modal jazz — pull it back to a static mode
held for many bars (§3). If the groove tightens onto the grid with hard
accents, it has drifted toward classic-jazz-swing or jazz-funk — pull it
back to the brushed, floating `cool-modal-floating` pocket.

## Common Pitfalls

| Symptom | Fix |
|---|---|
| Solo sounds like a bebop run over changes | Harmony is meant to be static — hold one mode for many bars (§3), let the soloist explore color rather than navigate chord changes |
| Melody feels crowded/busy | Not enough rest — apply the statement/rest/development cycle (§4); cut notes rather than add them |
| Piano comping sounds like a normal jazz comp | Switch to interactive comping (§6) — sparse punctuation between horn phrases, not a chord on every beat |
| Groove feels stiff or hard-accented | Wrong profile selected — use `cool-modal-floating`'s brushed, behind-the-beat pocket, not `classic-jazz-swing`'s tight big-band feel |
| Odd meter (5/4, 7/4) feels academic/stiff | The brief's own instruction: it must flow smoothly, not feel "counted" — keep phrasing long and legato across the bar line |
| Mix sounds bright/modern | That's a downstream mix concern (§7) — target a dry, intimate chamber-reverb character, not a wet digital hall |

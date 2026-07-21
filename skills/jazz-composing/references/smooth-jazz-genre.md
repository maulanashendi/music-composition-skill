# Smooth jazz — genre profile

Adapted from a smooth-jazz style brief (submitted 2026-07-20, translated and
restructured into this package's conventions). **The brief's worked ABC
example ("Pacific Coast Breeze") is a reference only, not a template to
imitate structurally** — this file does not reproduce it, and neither does
the Tier-1 template below; both stay at the level of chord vocabulary,
phrasing rules, and arrangement structure, the same way every other genre
file in this package handles a source brief's worked examples (see the
same instruction in `hiphop-jazz-genre.md`'s opening note). This is a
**new** genre entry, and `style-cheatsheets.md` gets a new "Smooth jazz"
entry pointing here.

Smooth jazz is a synthesis of jazz's improvisational softness, R&B/soul
harmonic color, and radio-friendly pop song structure. It prioritizes
listener comfort, sonic luxury, and a singable, memorable melody (the
"hook") over harmonic or rhythmic complexity. **Do not copy** a specific
recording, artist, or arrangement literally — translate the reference into
musical attributes (tempo, texture, harmonic density, phrasing, dynamics).
Identity comes from the combination of a **vocal-centric lead phrasing**
(§4), the **smooth slash chord** (§3), and a **straight, ultra-polished
pop-R&B grid** (§7) — not from harmonic complexity, which is deliberately
kept smoother/simpler than jazz-funk or bebop despite using similar
extended chords.

## Musical DNA baku

| Parameter | Default profile value |
|---|---|
| Tempo zone | 65-115 BPM depending on sub-style (see §2) |
| Meter | 4/4 |
| Tonal center | Major, lush and consonant — maj9/add9/m11/9sus4, rarely altered/dissonant |
| Rhythmic grid | Straight 16ths (R&B/pop), precise and consistent — **not** swung, unlike classic jazz or soul jazz |
| Palette (role -> instrument) | Anchor: R&B-style drums/drum machine + bass (often fretless) + comping keys · Lead: soprano/alto sax or clean guitar, phrased like a vocalist · Ear-candy: synth pads, bells, wind chimes/mark tree, shaker |
| Density ceiling | 1 foreground voice (the lead) at a time; melody leaves deliberate rests (§4) — space is as much a device as notes |

These are starting points, not law — bend toward the brief's specific
sub-style while staying inside the smooth-jazz family.

## 1. Sub-genres

| Sub-genre | Character |
|---|---|
| Urban / quiet storm smooth jazz | Heavily R&B/slow-jam influenced (80s-90s); dominated by soprano/alto sax, gently programmed drum machine, fretless bass (e.g. Kenny G, Dave Koz, Grover Washington Jr., Boney James) |
| West Coast / L.A. pop-jazz | Bright, laid-back, beach-adjacent, sweetly virtuosic; nylon/electric guitar with thick chorus, shimmering e-piano (e.g. Lee Ritenour, Larry Carlton, The Rippingtons, Earl Klugh) |
| Contemporary vocal pop-jazz | Commercial pop song format, often an actual R&B vocalist, or a lead horn acting as "the singer" (e.g. Sade, Anita Baker, George Benson) |
| Smooth fusion / GRP era | Early digital/MIDI-era instrumentation crossed with lush synth-pad orchestration (e.g. Bob James, Dave Grusin) |

## 2. Rhythmic feel & tempo matrix

- **Straight 16th R&B groove** — unlike classic/soul jazz's swing, smooth
  jazz uses a straight, precise 8th/16th grid, consistent like R&B/pop.
- **Slow-jam / quiet-storm ballad feel** — very calm pulse; cross-stick
  snare (rimshot), soft hi-hat, a sliding fretless-bass line.
- **Mid-tempo breeze groove** — a light four-on-the-floor or 90s-R&B drum
  pattern, layered with hand percussion (shaker, wind chimes/mark tree,
  tambourine).

| Sub-style / vibe | Category | BPM range | Character |
|---|---|---:|---|
| Quiet storm / slow jam | Ballad | 65-78 | Ultra-smooth, romantic, night-time, fretless bass slides, thick pads |
| Mid-tempo radio edit | Sweet spot groove | 82-98 | Easy listening, radio-friendly, vocal-centric melody, relaxed groove |
| West Coast / sunshine | Up-tempo breeze | 100-115 | Bright, optimistic, nimble nylon-guitar picking, soft compressed slap bass |

## 3. Harmony: vocabulary, tricks & progressions

Smooth jazz borrows modern jazz's extended chords (9th/11th/13th) but
arranges them for minimal dissonance — easy on an untrained ear.

**Chord vocabulary:**

- Major 9th (Cmaj9 = C-E-G-B-D) — the most popular tonic chord: lush, calm,
  open.
- Add9 (Cadd9 = C-D-E-G) — a sweeter pop-jazz substitute for a plain major
  triad.
- Minor 11th (Cm11 = C-Eb-G-Bb-D-F) — the safest, warmest minor chord.
- Dominant 9(sus4) (C9sus4 = C-F-G-Bb-D) — replaces a plain dominant 7 to
  avoid sounding too raw/bluesy; a very smooth "hanging" color.
- **The smooth slash chord (Fmaj7/G or Dm7/G)** — the single most crucial
  chord in this genre. It substitutes for a plain G7: bass sounds G, the
  upper voices sound F-A-C-E, producing an elegant `G13sus4` color without
  ever stating a raw dominant 7th.

**Harmony tricks:**

- **Pedal bass (stasis bass)** — the bass holds one note (e.g. C) while the
  chords above it change: `Cmaj9 -> Dm7/C -> Fmaj7/C -> Cmaj9`.
- **Stepwise bass motion** — the bass descends diatonically under the
  melody: `Cmaj9 -> G/B -> Am11 -> C/G -> Fmaj7`.
- **Sub-V / backdoor resolution** — a sweet resolution to I via bVII:
  `Bbmaj7/C -> Fmaj7/G -> Cmaj9`.

**Progression library** (reference by name; pick and adapt, do not restate
verbatim in every song):

```
West Coast breeze (key of C major):
| Cmaj9 | Am11 | Fmaj7 | Dm7/G (Fmaj7/G) |

Urban slow jam / quiet storm vamp (key of A minor):
| Fmaj7 | Em11 | Dm11 | Am9 G/B |

Pop-jazz radio chorus (key of G major):
| Gmaj9 | Bm7 | Cmaj9 | Cm9 (Eb/F) |  (Cm9 = modal-interchange color)

The Grover Washington cell (key of Db major / F minor):
| Dbmaj7 | C7alt | Fm7 | Ebm7 Ab7 |
```

## 4. Melody: vocal-centric technique (the load-bearing section)

The lead instrument (usually a sax) must sound **singable** — it positions
itself as if it were a pop/R&B vocalist, not a jazz improviser:

- **Bends & scoop notes** — start a half-step below the target note and
  slide up into it smoothly.
- **Grace notes** — 1-2 small ornament notes just before landing on the
  main melody note.
- **Controlled vibrato** — never vibrato at the start of a note. Hold it
  straight-toned for the first 2 beats, then add slow, gentle vibrato only
  at the tail.
- **Space & breathing** — leave 1-2 bars of rest between phrases; do not
  fill every bar with notes. This restraint is a genre-defining discipline,
  not an absence of ideas — compare to bossa nova's restraint
  (`bossa-nova-genre.md` §8) but applied to a pop-vocal phrasing model
  rather than a jazz one.

**Call-and-response:**

```
Lead sax   : [ main melodic phrase / hook (2 bar) ] -> holds a long note
Comping key:                                        -> [ response: e-piano bell/chorus chops (2 bar) ]
```

**The ad-lib outro** — at the fade-out, the soloist does not play a
technical improvised scale run; they do a vocal-style ad-lib around the
song's tonic, interacting with a backing vocal or keyboard phrase, the same
way a singer would ad-lib over a fading chorus.

## 5. Instrument palette & "secret recipe" sound design

**Track setup:**

```
Lead instruments : soprano/alto saxophone, nylon-string guitar, clean electric guitar
Comping keyboards: FM e-piano (DX7-style), Fender Rhodes (stereo chorus), acoustic piano
Synth layers     : warm analog pads, digital strings, bell/fantasia tones
Bassline         : fretless electric bass, clean active precision bass, synth bass
Drums/rhythm     : R&B drum machine (808/909-style samples), layered acoustic drums
Percussion       : continuous 16th shaker, mark tree/wind chimes, triangle
```

**Sound-design intent** (downstream — for whoever programs/mixes the
patch, not something this package's scripts implement, same framing as
`classic-jazz-genre.md` §9):

- **FM e-piano (DX7-style)** — EQ cut below 100 Hz, gentle boost around
  10 kHz for "air"; stereo chorus (moderate depth, slow rate); dotted-8th
  ping-pong delay; a lush hall reverb.
- **Silk saxophone tone** — cut boxy 400-600 Hz, tame 3-4 kHz, gentle
  high-shelf above 8 kHz; a de-esser on breath noise; opto-compression
  (LA-2A style, 2-4 dB gain reduction) to smooth dynamics; a lush plate/
  large-hall reverb (2.8-3.5s decay) plus a soft 1/4- or 1/8-note stereo
  delay.
- **Clean chorus guitar** — a pristine clean amp model, thick stereo
  chorus, smooth optical compression, ambient reverb.
- **Fretless bass** — soft-fingered touch with pitch slides into target
  notes; a subtle stereo pitch-shift/micro-detune plus light chorus for a
  thick, "swimming" tone.

## 6. Groove engine & comping styles

**Drums:**

- Kick follows a stable but unobtrusive R&B syncopation pattern, not
  dominant in the sub-bass.
- Snare/rimshot: soft cross-stick in the verse, switching to a layered,
  tightly compressed full snare in the chorus — a **timbral** shift, not a
  timing one (see the `smooth-jazz-rnb` groove profile).
- Hi-hat plays velocity-layered straight 16ths, doubled with a continuous
  16th shaker to keep the groove flowing.

**Comping:**

- **E-piano/Rhodes "splay" (arpeggiated) comping** — chord tones are
  sounded in a very fast roll rather than struck simultaneously.
- **Nylon guitar arpeggios** — organic texture underneath digital synth
  pads.
- **Clean electric guitar "chucks"** — thin accented strums (wah or
  chorus) on off-beat 16ths.

Groove detail (tick offsets, gate ratios) lives in
`../../groove-rhythm/references/groove-profiles.md` under the
`smooth-jazz-rnb` profile — select it by name.

## 7. Differentiating smooth jazz from this package's other genres

Smooth jazz's chord vocabulary (maj9, m11, 9sus4, slash chords) overlaps
with bossa nova, jazzhop/neo-soul, and soul jazz — the distinguishing axes
are **production polish, straight-grid precision, and vocal-centric
phrasing**, not harmony:

| Genre | What actually differs from smooth jazz |
|---|---|
| Bossa nova (`bossa-nova-genre.md`) | Both use a straight, unswung grid — but bossa's identity is an intimate acoustic nylon-guitar batida with a laid-back/rubato lead; smooth jazz's grid is R&B-precise and *nothing* lays back, including the lead (§7's controlled-vibrato technique is about tone, not timing) |
| Jazzhop / neo-soul (`neo-soul-genre.md`) | Neo-soul drags the whole ensemble behind a swung-16th grid; smooth jazz stays dead-straight and on-the-grid, "licked"/polished rather than dusty |
| Soul jazz (`soul-jazz-genre.md`) | Soul jazz swings on an 8th grid with a gospel/blues backbone and sparse harmony; smooth jazz is straight-16th, pop-structured, and leans on lush 9th/11th/slash-chord harmony instead of blues |
| Jazz-funk (`jazz-funk-genre.md`) | Both are straight-16th — but jazz-funk is aggressive, riff-driven, and static-vamp harmonically; smooth jazz is soft, hook/melody-driven, and moves through a full pop song form (§8) |

## 8. Arrangement blueprint (radio pop-standard form)

```
[INTRO] -> [VERSE 1] -> [PRE-CHORUS] -> [CHORUS] -> [VERSE 2] -> [CHORUS] -> [SOLO / BRIDGE] -> [CHORUS] -> [OUTRO / FADE-OUT]
```

- **Intro (8 bar)** — nylon guitar or e-piano solos over a synth pad and
  wind chimes; drums are not yet full (just shaker or cross-stick).
- **Verse 1 (8-16 bar)** — the full R&B drum groove enters; sax/guitar
  plays a relaxed, lower-register theme.
- **Pre-chorus (4-8 bar)** — harmony shifts to slash chords
  (`Dm7/G -> Fmaj7/G`), tension builds gently.
- **Chorus (8-16 bar — the hook)** — the melodic peak (the catchy hook);
  the sax plays in a higher register, the snare switches from rimshot to
  full snare, a brass pad or synth strings thicken the harmony.
- **Bridge / solo section (8-16 bar)** — room for a soloist (guitar or
  keyboard); the melody stays structured and singable, avoiding overly
  fast/technical playing.
- **Outro (fade-out)** — the chorus hook repeats continuously while the
  soloist plays vocal-style ad-libs (§4) over it as the volume fades.

## Common Pitfalls

| Symptom | Fix |
|---|---|
| Melody feels like a jazz solo, not a song | Apply the vocal-centric phrasing rules (§4) — bends, grace notes, controlled vibrato, and deliberate space |
| Chorus doesn't feel like a payoff | Confirm register lift + snare timbre change + pad thickening actually happen at the chorus (§8) — a chorus that sounds identical to the verse has no hook |
| Groove feels dusty/laid-back | Wrong profile selected — smooth jazz is straight and precise (`smooth-jazz-rnb`), not `neo-soul-core`'s drag or `classic-jazz-swing`'s triplet feel |
| Harmony sounds raw/bluesy | Replace a plain dominant 7 with `9sus4` or the smooth slash chord (§3) |
| Solo section sounds too "jazz" | Keep it structured and singable per the brief's own instruction (§8) — this is not the place for dense/fast technical runs |
| Production sounds dry/unpolished | That's a downstream mix concern, not this package's job — see §5's sound-design intent for what "licked" means as a target |

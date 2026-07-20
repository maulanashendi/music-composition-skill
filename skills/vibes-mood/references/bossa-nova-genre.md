# Bossa nova — genre profile

Adapted from a bossa nova style brief (submitted 2026-07-20, translated and
restructured into this package's conventions). This deepens the "Bossa nova
/ latin" entry in `style-cheatsheets.md` the same way `neo-soul-genre.md`
and `classic-jazz-genre.md` deepen theirs — the cheatsheet stays the fast
starting point, this file is where the harmony bible, batida patterns, and
arrangement detail live.

Bossa nova fuses jazz harmonic structure with a smoothed-out Brazilian samba
swing. **Do not copy** a specific recording, artist, or arrangement
literally — translate the reference into musical attributes (tempo,
texture, harmonic density, articulation, dynamics, emotional arc — the
mood this genre names for itself is *saudade*, a wistful, melancholic
longing). Originality comes from the **combination** of harmony extension +
batida variation + melodic placement, not from novelty — bossa nova's
identity is precise and restrained, not dense.

## Musical DNA baku

| Parameter | Default profile value |
|---|---|
| Tempo zone | 80-160 BPM depending on sub-style (see §1) |
| Meter | 4/4 (felt in two — batida patterns are 2-bar loops) |
| Tonal center | Major with heavy jazz extension (maj7/maj9/6-9), or minor for the *saudade* mood (m9/m11/m6) |
| Rhythmic grid | **Straight 16ths — no swing.** This is the single most load-bearing distinction from every other genre in this package (see §7 differentiation table). |
| Palette (role -> instrument) | Anchor: nylon-string guitar batida + soft bass + cross-stick/shaker · Rotation: piano/Rhodes, flute, tenor sax (sub-tone), flugelhorn · Ear-candy: string pad, counter-melody flute |
| Density ceiling | 1 foreground voice (vocal/lead) at a time; the guitar batida is the constant floor under it, never competing for foreground |

These are starting points, not law — bend toward the brief's specific
sub-style while staying inside the bossa family.

## 1. Tempo & character options

| Category | BPM range | Character | Reference feel |
|---|---:|---|---|
| Bossa ballad | 80-100 | Intimate, slow, dramatic — night-time or melancholic *saudade* | "Corcovado", "Dindi" |
| Classic bossa nova | 110-130 | The standard tempo — perfect balance of relaxed rhythm and flowing energy | "The Girl from Ipanema", "Wave" |
| Samba-bossa / up-tempo | 135-160 | Energetic, joyful, driving — closer to samba's roots | "Só Danço Samba", "Mas Que Nada" |

## 2. Micro-timing & elasticity — the key to the bossa "feel"

This is the genre's most important and most commonly mis-applied rule, so
state it plainly:

- **The rhythm section stays on a straight 16th grid.** Guitar, shaker, and
  cross-stick drum hold 16th-note subdivisions dead straight — **no**
  American-jazz swing feel anywhere in the rhythm section.
- **The lead/vocal is laid back or rubato.** The melody or vocal sits behind
  the beat, or is pulled loosely out of time, creating a relaxed feel *on
  top of* a precise rhythmic foundation — the contrast is the point, not a
  uniformly loose ensemble.
- **Anticipation (push).** Melody notes or chord accents frequently "steal"
  the beat, entering 1/16 or 1/8 early ahead of a chord change — this is a
  written/placed anticipation, not a timing error, and it is the main
  source of forward momentum since the rhythm section itself never swings.

See §8 for how this differs from every swing- or humanize-based groove
already in this package.

## 3. Instrument palette, timbre & interaction

- **Nylon-string acoustic guitar** — plucked with the fingertips/nails, no
  pick. Warm tone, focused in the mid-range, soft attack. This is the
  anchor instrument; the batida pattern (§6) is bossa's signature texture.
- **Upright bass / fretless bass** — deep, woody, short pizzicato sustain;
  EQ rolled off above ~2.5 kHz.
- **Drums & percussion:**
  - Cross-stick/rim-click — a thick wooden stick played on the snare rim,
    echoing the guitar's batida rhythm.
  - Ganzá/shaker — aluminum shaker with fine sand, a constant high-frequency
    16th pulse.
  - Surdo/muted kick — heavily muffled (pillowed) for a soft "thud" with no
    boom.
  - Pandeiro/agogô (optional) — for up-tempo variation.
- **Keyboard/piano** — acoustic grand played with soft (una corda) pedal, or
  Fender Rhodes with a warm vintage tone and light chorus panning.
- **Woodwinds & brass:**
  - Flute/alto flute — breathy, airy.
  - Tenor saxophone — sub-tone technique, loose embouchure in the low
    register (Stan Getz style).
  - Flugelhorn — a warmer, more subdued alternative to trumpet.

## 4. Harmony vocabulary (chord bible)

Avoid plain triads (`C`, `Dm`, `G`) — bossa's identity is built on
extensions (7, 9, 11, 13) and alterations (b9, #9, b5, #11, b13).

**Major family (tonic/resolution):**

- Major 7th (Cmaj7 = C-E-G-B) — the base bossa sound.
- Major 9th (Cmaj9 = C-E-G-B-D) — more open and elegant.
- **Major 6/9 (C6/9 = C-E-A-D) — the most authentic bossa-nova chord**, and
  the standard final-cadence color.
- Major 7(#11) (Cmaj7#11 = C-E-G-B-F#) — Lydian, floating.
- Major 13 (Cmaj13 = C-E-B-D-A) — rich and lush.

**Minor family (subdominant/pre-dominant):**

- Minor 7th (Dm7 = D-F-A-C).
- **Minor 9th (Dm9 = D-F-A-C-E) — the standard bossa minor chord.**
- Minor 11th (Dm11 = D-F-A-C-G) — modern/cool color.
- Minor 6 (Dm6 = D-F-A-B) — melancholic, Dorian character.
- Minor(maj7) (Dm(maj7) = D-F-A-C#) — mysterious, "James Bond" sound.

**Dominant family (tension/dominant):**

- Dominant 9 (G9 = G-B-D-F-A).
- **Dominant 13 (G13 = G-B-F-A-E) — the most common dominant chord in bossa.**
- Dominant 7(b9) (G7b9 = G-B-F-Ab) — high tension resolving to minor/major.
- Dominant 7(#9) (G7#9 = G-B-F-A#) — edgy character tension.
- Dominant 7(b13) (G7b13 = G-B-F-Eb) — deeply melancholic.
- Dominant 7(#11) (G7#11 = G-B-D-F-C#) — Lydian dominant.
- Altered dominant (G7alt = G-B-F-Ab-A#-Eb) — maximum resolution pull.

**Half-diminished & diminished (passing/minor ii):**

- Half-diminished/m7b5 (Bm7b5 = B-D-F-A) — as the ii in a minor ii-V-i.
- Diminished 7th (C#dim7 = C#-E-G-Bb) — chromatic connecting chord.

## 5. Progression library & harmonic mechanics

Reference by name; pick and adapt, do not restate verbatim in every song.

```
Progression 1 - Classic major "standard" (I - VI - ii - V):
| Cmaj9 | A7(b9) | Dm9 | G13 G7(b13) |
Mechanism: A7(b9) is a secondary dominant resolving into Dm9.

Progression 2 - The Jobim chromatic descent:
| Cmaj7 | C#dim7 | Dm7 | D#dim7 | C/E | A7(b9,b13) |
Mechanism: the bass line climbs chromatically (C -> C# -> D -> D# -> E),
giving dynamic stability under moving harmony.

Progression 3 - The "Girl from Ipanema" formula (I - II7 - ii - V):
| Fmaj7 | G7(13) | Gm9 | C7(b9) |
Mechanism: a major-dominant II chord (G7 over an F tonic) gives the
floating quality that is Antonio Carlos Jobim's signature.

Progression 4 - Minor bossa (saudade):
| Am9 | Bm7b5 | E7(b9,b13) | Am(maj7) Am6 |
Mechanism: a minor line cliche (A -> G# -> F#) across the final bar.

Progression 5 - Modern backdoor & tritone substitution:
| Cmaj9 | Fm9 Bb13 | Cmaj7 | Db13 |
Mechanism: Fm9-Bb13 is a backdoor ii-V; Db13 is a tritone substitution
for G7.
```

## 6. Rhythm patterns & comping (batida)

The rhythmic interaction happens between a stable bass pulse and a
syncopated fingerpicked comp — see §2 for why nothing here swings.

**Bass pattern (thumb/bassist)** — a divided-in-two pulse (felt in 4/4 or 2/2):

- Beat 1: root.
- Beat 3: 5th — often pulled 1/16 early as an anticipation into the next
  bar.

**Guitar strumming variations (batida)** — `X` = pluck, `.` = rest, grid is
16 sixteenth-note steps per bar, two bars shown:

```
Variation 1 - Joao Gilberto classic (2-bar loop):
Beat:   | 1 . & . 2 . & . 3 . & . 4 . & . | 1 . & . 2 . & . 3 . & . 4 . & . |
Thumb:  | X . . . . . . . X . . . . . . . | X . . . . . . . X . . . . . . . |
Fingers:| X . . X . . X . . . X . . X . . | . . X . . X . . . . X . . X . . |

Variation 2 - Baden Powell afro-samba (syncopated push):
Beat:   | 1 . & . 2 . & . 3 . & . 4 . & . | 1 . & . 2 . & . 3 . & . 4 . & . |
Thumb:  | X . . . . . . . X . . . . . . . | X . . . . . . . X . . . . . . . |
Fingers:| X . . X . X . . . X . X . . X . | X . . X . X . . . X . X . . X . |
```

**Drum/percussion patterns:**

- Cross-stick (snare) — echoes the guitar's fingerpicking pattern on the
  rim.
- Shaker — constant 16th accent: `e-k-U-k e-k-U-k` (U = a soft accent on
  the hanging upbeat).
- Surdo/kick — beat 1 soft/muted, beat 3 fuller with a slight accent (open).

## 7. Melody construction & call-and-response

**Melodic pitch choice:**

- **Target extended tones** — land melody notes on the 9th, 11th, or 13th
  as the chord changes; this is where the "jazz color" comes from.
- **Minimalist/one-note technique** — hold a single melody note while the
  harmony underneath moves chromatically (e.g. "One Note Samba").

**Call-and-response patterns:**

- Vocal (call) -> guitar/piano (response): bars 1-2 the vocal sings the main
  phrase; bars 3-4 the vocal rests while guitar/piano fills the space with a
  denser batida motif.
- Lead melody (call) -> flute counter-melody (response): flute plays an
  obbligato line in a high register while the vocal holds a long note.

## 8. Differentiating bossa nova from this package's other genres

This is the section to check before composing — bossa nova is easy to
accidentally flatten into an adjacent genre already in this package. The
distinguishing axis is almost always **micro-timing** (see
`groove-rhythm/references/groove-profiles.md`), not harmony — several
genres share extended-chord vocabulary with bossa, but none share its
straight-grid-plus-laid-back-lead combination.

| Genre | Rhythmic grid | What actually differs from bossa |
|---|---|---|
| Bebop/hard bop, classic jazz swing | Swung 8ths/16ths (triplet-based) | Bossa is **never** swung — this is the single most common mistake: do not let a bossa arrangement drift onto a `classic-jazz-swing`/ride-swing feel |
| Lofi jazz, jazzhop/neo-soul | Swung or humanized 16ths, the **whole ensemble** drags behind the grid | Bossa's rhythm section (guitar/bass/percussion) stays precisely on a straight grid — only the lead/vocal lays back or goes rubato; a bossa arrangement where the guitar batida also drags has drifted into lofi/neo-soul territory |
| Jazz-funk/fusion | Straight 16ths, but hard-locked *on* the grid with a driving backbeat | Bossa is straight like fusion but soft/intimate, not driving — muted surdo kick vs. fusion's punchy backbeat, fingerpicked guitar vs. funk comping |
| Modal jazz | Sparse harmony, static pedal | Bossa's harmony moves constantly (chromatic bass motion, §5) — it borrows jazz's extension vocabulary but not modal's harmonic stasis |

If a candidate composition could be mistaken for lofi or swing jazz by ear,
the grid has drifted — go back to §2.

## 9. Arrangement blueprint (AABA form, 32 bars)

```
[INTRO] (4-8 bar)
- Nylon guitar plays the batida pattern solo.
- Shaker enters at bar 3.
- Bass enters at bar 5 with a root-5th line.

[VERSE A1] (8 bar)
- Vocal/lead melody enters (sotto voce, soft).
- Drums: thin cross-stick + shaker + muted kick.
- Harmony: the main progression (e.g. I - II7 - ii - V).

[VERSE A2] (8 bar)
- A thin counter-melody from flute or Rhodes enters.
- String pad (violin/cello) enters very softly in the background.

[BRIDGE B] (8 bar) - modulation / tension
- Key modulation (e.g. up a half-step, or to the parallel minor).
- Denser harmony (more altered-dominant chords).
- Dynamics rise slightly, pianissimo (pp) to mezzo-piano (mp).

[VERSE A3 / RE-HEAD] (8 bar)
- Return to the home key.
- Fullest arrangement: vocal + flute + Rhodes + full percussion.

[SOLO INTERLUDE] (16 bar)
- Flute, tenor sax, or nylon guitar solos over the Verse A progression.

[OUTRO / TAG ENDING] (4-8 bar)
- Repeat the last 2 bars of the progression 3 times (vamp).
- End on a softly strummed major 6/9 chord, left to ring out
  (fade out / ritardando).
```

## Common Pitfalls

| Symptom | Fix |
|---|---|
| Sounds like generic pop | Chords are plain triads — replace the whole progression with 7ths/9ths/6-9 minimum (§4) |
| Feels stiff, or like swing jazz | The rhythm section (drums/guitar) is swinging — force straight 16ths across the whole rhythm section (§2, §8) |
| Arrangement feels crowded/busy | Too many instruments filling at once — strip drum/piano fills back and let the guitar batida carry the space alone |
| Bass buries the guitar | Frequency clash in the low-mid — cut bass EQ around 250-500 Hz and let the guitar's fingerpicking dominate the mid-range (downstream mix note, see the production-intent framing in `classic-jazz-genre.md` §9 for how this package scopes mixing) |
| Vocal/lead feels too dominant/aggressive | Vocal is too loud or too wide a vibrato — write it as sotto voce, close-mic'd, minimal vibrato (also a downstream performance/mix note) |
| Reads as lofi or neo-soul instead of bossa | The whole ensemble is laid back, not just the lead — see §8; only the lead/vocal should drag, the rhythm section stays straight |

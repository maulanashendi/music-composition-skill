# Soul jazz — genre profile

Adapted from a soul jazz / jazz-funk style brief (submitted 2026-07-20,
translated and restructured into this package's conventions). This is a
**new** genre entry — unlike bossa nova and jazz-funk (see
`jazz-funk-genre.md`), `style-cheatsheets.md` had no soul jazz entry before
this file; one has been added there pointing here.

Soul jazz (late 1950s-1960s) was a reaction against Cool Jazz and Hard Bop
being seen as too academic — it pulled jazz back to its roots in Black
American church music: **Gospel**, rural blues, and early R&B. The
character is organic, analog, warm, communal ("soulful"), and built around
early electro-mechanical instruments (the Hammond organ above all). **Do
not copy** a specific recording, artist, or arrangement literally —
translate the reference into musical attributes (tempo, texture, harmonic
density, articulation, dynamics). Soul jazz's identity comes from the
**Hammond B-3 + gospel harmony + a thick swung backbeat** combination, not
from harmonic complexity — see §7 for how sparse this genre's chord
vocabulary is compared to bebop or jazz-funk.

## Musical DNA baku

| Parameter | Default profile value |
|---|---|
| Tempo zone | 65-145 BPM depending on sub-style (see §2) |
| Meter | 4/4, occasionally gospel 6/8 |
| Tonal center | Blues-major, gospel-inflected — dominant 7th/9th harmony over a 12-bar or vamp form, not through-composed changes |
| Rhythmic grid | Swung 8ths, bluesy and looser than a precise big-band ride — see the `soul-jazz-swing` groove profile for exactly how it differs from `classic-jazz-swing` |
| Palette (role -> instrument) | Anchor: Hammond B-3 (melody + harmony + bass pedal) + drums + guitar comping · Front line (optional): tenor sax (smokey/gritty), trumpet · Ear-candy: Leslie speaker speed changes, organ glissando/palm smear |
| Density ceiling | 1 foreground voice at a time; the organ is almost always present underneath, even as accompaniment |

These are starting points, not law — bend toward the brief's specific
sub-style while staying inside the soul-jazz family.

## 1. Sub-styles & hybrid variations

| Sub-style | Description |
|---|---|
| Jazz-boogaloo (Latin soul-jazz crossover) | Soul-jazz blues crossed with a Latin clave/cha-cha-cha feel; a tumbao/montuno bassline pattern combined with an R&B backbeat (e.g. Lee Morgan's "The Sidewinder") |
| Purdie shuffle (half-time funk swing) | Bernard Purdie's iconic drum pattern — a 16th-note triplet grid combined with very dense snare ghost notes; feels relaxed but has a "bouncing" rhythmic push. See the `purdie-shuffle` groove profile in `groove-rhythm/references/groove-profiles.md` — it bridges soul jazz and jazz-funk and is documented once there, shared by both genres. |

## 2. Feel & tempo matrix

| Category | BPM range | Character & vibe |
|---|---:|---|
| Slow blues/gospel | 65-85 | Swung 8ths / gospel 6/8, warm, Hammond B-3 humming sweetly |
| Mid-tempo cooker | 90-115 | The soul jazz sweet spot — relaxed, strutting, deeply groovy |
| Up-tempo hard-soul | 120-145 | Energetic, the organ runs fast lines, horn section trades call-and-response |

## 3. Ensemble & instrumentation

**Soul jazz organ trio/quintet setup:**

- **Hammond B-3 organ + Leslie speaker** — the center of melody, harmony,
  and bassline (via bass pedals or the lower drawbars); the single most
  identity-defining instrument of the genre.
- **Electric guitar (semi-hollow/hollow body)** — thick, clean tube tone,
  no sharp distortion (e.g. a Gibson ES-175/L-5 through a Fender Twin
  Reverb).
- **Acoustic drums** — thick ride cymbal, thick wooden snare, sloshy
  hi-hat.
- **Front-line horns (optional)** — tenor saxophone (smokey/gritty) and
  trumpet.

## 4. Hammond B-3 & FX "secret recipes"

**Drawbar registrations** (drawbar order:
`16' 5-1/3' 8' 4' 2-2/3' 2' 1-3/5' 1-1/3' 1'`):

- **Jimmy Smith classic lead:** `88 8000 000` — vibrato C-3 on, percussion
  3rd harmonic on (soft, fast decay).
- **Gospel/church full organ:** `88 8888 888` — Leslie set to fast
  tremolo, a thin tube overdrive.
- **Smokey low-end comping:** `80 0000 000` — percussion off, Leslie set to
  slow chorale.

**Keyboard FX chains:**

- Hammond -> Leslie rotary (chorale for comping/slow sections, tremolo/fast
  for solo peaks — see the arrangement blueprint §8) is the primary color
  control; automating the Leslie speed is itself a dynamic-arc device.
- A thin tube-amp overdrive on the organ, never a hard distortion — the
  grit stays "warm," not aggressive (contrast with jazz-funk's more
  processed electric tones, `jazz-funk-genre.md` §4).

## 5. Harmony: vocabulary & pro-level tricks

**Chord vocabulary (deliberately sparse compared to bebop/jazz-funk):**

- Dominant 7th & 9th (C7, C9) — the primary blues-based driver.
- Gospel plagal cadence: `IV -> I` or `IV/I -> I` (e.g. `F/C -> C`) for a
  warm, spiritual color — this is soul jazz's signature cadence, distinct
  from a jazz ii-V-I.

**Pro-level tricks:**

- **Gospel plagal cadence** (above) — reach for this instead of a dominant
  V-I when the brief wants a churchy, spiritual resolution.
- Side-stepping/outside soloing over a static vamp is documented once in
  `jazz-funk-genre.md` §5 (it applies to both genres' vamp-based sections,
  not just jazz-funk) — reference it rather than restating it here.

## 6. Progression library

```
Soul jazz gospel-blues 12-bar (key of F):
| F7     | Bb7    | F7     | F7 (F9) |
| Bb7    | Bbdim7 | F7     | D7(#9)  |
| Gm7    | C7(#9) | F7 D7  | Gm7 C7  |
```

Reference by name; pick and adapt, do not restate verbatim in every song.

## 7. Melody: scales

- Minor blues scale: `1 - b3 - 4 - b5 - 5 - b7`.
- Major/gospel blues scale: `1 - 2 - b3 - 3 - 5 - 6`.
- Dorian & Mixolydian — the primary choices for improvising over a static
  vamp (shared with jazz-funk, see `jazz-funk-genre.md` §6).

## 8. Groove engine & comping

**Drums:** ride cymbal swung (swung 8ths); snare gives a thick backbeat on
2 and 4; hi-hat occasionally opens (sloshy) on off-beat accents. Groove
detail (tick offsets, gate ratios) lives in
`../../groove-rhythm/references/groove-profiles.md` under the
`soul-jazz-swing` profile — select it by name.

**Guitar comping:** play 7th/9th chords with the thumb (Wes Montgomery
style), or bluesy, meandering comping lines — contrast with jazz-funk's
scratch/chank 16th-note strumming (`jazz-funk-genre.md` §7).

## 9. Vintage production intent (downstream — not this package's job)

As with `classic-jazz-genre.md` §9, this package composes and arranges; it
does not mix audio. Record the reference brief's production intent here as
guidance for whoever renders the mix, not as something this package's
scripts implement:

```
[ vintage tube preamp ] -> [ Leslie rotary emulation ] -> [ tape saturation (15 IPS) ]
```

- EQ: push warm low-mids, +2 dB around 250-500 Hz.
- Reverb: spring or plate reverb with a warm character.

## 10. Arrangement blueprint (organ trio/quintet form)

```
[INTRO (ORGAN VAMP)] -> [HEAD (BLUES/GOSPEL)] -> [ORGAN SOLO] -> [SAX/GUITAR SOLO] -> [HEAD RETURN] -> [OUTRO]
```

- **Intro (4-8 bar)** — the B-3 plays a bass-pedal vamp and its own chords
  alone, Leslie set slow (chorale).
- **Head (12 or 16 bar)** — tenor sax and trumpet play the theme in
  unison/sweet harmony; the organ comps a gospel-tinged rhythm underneath.
- **Organ solo (2-3 choruses)** — the organist improvises, pulling
  drawbars out gradually to build volume, switching the Leslie to fast
  tremolo at the solo's peak — a dynamic-arc device unique to this
  instrument.
- **Sax/guitar solo** — trades the foreground role while the organ shifts
  back to comping.
- **Head return** — the theme restates with the full band.
- **Outro** — close on a held `7#9` or `6/9` chord with an upward organ
  glissando (palm smear).

## 11. Differentiating soul jazz from classic jazz and jazz-funk

Soul jazz sits historically and sonically **between** `classic-jazz-genre.md`
and `jazz-funk-genre.md` — see the full three-way comparison matrix in
`jazz-funk-genre.md` §9 (era, instrumentation, rhythmic center, harmonic
pattern, sonic character). The two axes that most often get confused:

- **vs. classic jazz swing** — soul jazz's backbeat is thicker and sits
  *behind* the grid (a "strutting" pocket, `soul-jazz-swing` groove
  profile), where `classic-jazz-swing`'s big-band ride and snare stay tight
  and precise. Soul jazz is bluesier and looser; classic jazz swing is
  crisper and more written/arranged.
- **vs. jazz-funk** — soul jazz stays on a swung 8th grid (organ-and-guitar
  centered, acoustic drums); jazz-funk moves to a straight, tight 16th grid
  driven by electric bass and synths/Clavinet (see `jazz-funk-genre.md`
  §2, §8). If the rhythm section starts feeling like a 16th-note funk
  pocket, the piece has crossed from soul jazz into jazz-funk.

## Common Pitfalls

| Symptom | Fix |
|---|---|
| Sounds like plain blues-rock | Missing the Hammond B-3 centerpiece — the organ carries melody, harmony, *and* bass; without it the genre's identity is gone |
| Harmony feels too complex/modern-jazz | Soul jazz is deliberately sparse — 12-bar gospel-blues + a plagal cadence, not dense ii-V chains (§5, §6) |
| Organ solo has no arc | Automate the Leslie speed and drawbar pull-out across the solo (§10) — a static organ patch reads as flat |
| Groove reads as tight funk instead of soul jazz | The rhythm section has drifted onto a straight 16th grid — pull it back to `soul-jazz-swing`'s swung 8ths (§8, §11) |
| Guitar comping sounds like jazz-funk scratch/chank | Switch to Wes-style thumb chords or bluesy comping (§8) — scratch/chank belongs to jazz-funk |

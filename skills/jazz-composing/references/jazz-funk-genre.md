# Jazz-funk — genre profile

Adapted from a soul jazz / jazz-funk style brief (submitted 2026-07-20,
translated and restructured into this package's conventions). This deepens
the existing "Jazz-funk / fusion" entry in `style-cheatsheets.md` the same
way `neo-soul-genre.md`, `classic-jazz-genre.md`, and `bossa-nova-genre.md`
deepen theirs. It also carries the Tier-1 composition-plan template for this
family — `jazz-composition/templates/fusion-vamp.json` already exists and
needs no changes; this file explains where it sits and what other groove
options this genre has beyond it.

Jazz-funk (late 1960s-1970s) merges jazz's improvisational freedom with
electronic instrument technology and funk's syncopated rhythm. **Do not
copy** a specific recording, artist, or arrangement literally — translate
the reference into musical attributes (tempo, texture, harmonic density,
articulation, dynamics). The character is electric, futuristic, aggressive,
heavily percussive, and driven by a slap bassline and a tight 16th-note
groove built for dancing — the opposite pole from soul jazz's warm acoustic
swing (see §9).

## Musical DNA baku

| Parameter | Default profile value |
|---|---|
| Tempo zone | 75-140+ BPM depending on sub-style (see §2) |
| Meter | 4/4 |
| Tonal center | Static minor 11th vamps, dominant-altered color, and modal riffs — harmony is subservient to groove, not the other way around |
| Rhythmic grid | Straight, tight 16th-notes — see `fusion-tight` and `purdie-shuffle` groove profiles for the two pockets this genre draws on |
| Palette (role -> instrument) | Anchor: electric bass (slap/pop) + drums + Clavinet/Rhodes · Rotation: synth lead (Minimoog/ARP/Prophet-5), brass section · Ear-candy: wah-wah, phaser, talkbox/vocoder |
| Density ceiling | 1-2 chord vamps are the norm — harmonic stasis is a feature, variation comes from groove layering and dynamics, not chord motion |

These are starting points, not law — bend toward the brief's specific
sub-style while staying inside the jazz-funk family.

## 1. Sub-styles

| Sub-style | Era | Character |
|---|---|---|
| Japanese jazz-funk/fusion | Late 1970s-1980s | Very precise and crisp, sweet pop-jazz pentatonic melodies, high-speed slap bass, a very clean/bright/polished brass section (e.g. Casiopea, T-Square) |
| Electro-jazz-funk / talkbox era | Late 1970s | Acoustic/electric bass replaced by Moog synth bass, talkbox or vocoder on vocal/lead-synth melody (e.g. Herbie Hancock's *Sunlight* era, George Duke) |
| Purdie shuffle (half-time funk swing) | — | Shared with soul jazz — see `soul-jazz-genre.md` §1 and the `purdie-shuffle` groove profile; a hybrid that pulls jazz-funk toward soul jazz's looser pocket |
| Jazz-boogaloo | — | Also shared with soul jazz (`soul-jazz-genre.md` §1) — Latin clave/tumbao crossed with an R&B backbeat |

## 2. Tempo & feel matrix

| Category | BPM range | Character & vibe |
|---|---:|---|
| Slow down-tempo funk | 75-90 | Straight 16th-notes, heavy groove, thick bassline, slow wah-wah |
| Mid-tempo pocket funk | 95-115 | Classic "headhunters" vibe — driving slap bass, percussive Clavinet, head-bobbing |
| High-octane funk | 120-140+ | Aggressive, virtuosic, percussive drum solos, sharp and fast brass section |

## 3. Ensemble & instrumentation

**Jazz-funk electric ensemble setup:**

- **Electric bass guitar** — Fender Jazz Bass/Precision Bass, dominated by
  slap-and-pop technique (§6).
- **Rhythm keyboards** — Hohner Clavinet D6 (with a wah-wah pedal) & Fender
  Rhodes (with phaser/tremolo).
- **Synthesizers** — Minimoog, ARP Odyssey, Prophet-5 (lead, Moog bass, FX).
- **Electric guitar** — solid-body (Fender Stratocaster) for
  scratching/chank comping (§7).
- **Drums & world percussion** — tight piccolo snare, congas, bongos,
  agogo, timbales.
- **Phat brass section** — tenor sax, alto sax, trumpet, trombone.

## 4. Synth & keyboard "secret recipes"

- **Hohner Clavinet D6** — signal into a Mu-Tron III envelope filter
  (auto-wah), then a Twin Reverb amp simulation.
- **Fender Rhodes** — signal into a Small Stone phaser or stereo tremolo for
  a "floating"/dreamy vibe.
- **Synth bass/lead patching (Moog-style):** two oscillators (osc 1
  sawtooth, osc 2 square/sub-octave) into a 24dB low-pass filter with
  mid-range resonance and a short filter-envelope decay, for a plucky,
  percussive, bassy tone.

Contrast with soul jazz's Hammond-centric, warm-tube-overdrive palette —
see `soul-jazz-genre.md` §4; jazz-funk's processing is more electronic and
effects-forward (auto-wah, phaser, talkbox) rather than a rotary speaker.

## 5. Harmony: vocabulary & pro-level tricks

**Chord vocabulary:**

- Dominant 7th & 9th (C7, C9) — the blues-based driver, shared with soul
  jazz.
- **Dominant 7(#9) — "the Hendrix/funk chord"** (C7#9 = C-E-G-Bb-D#) —
  a sharply aggressive, stinging blues tension.
- **Minor 11th (Cm11 = C-Eb-G-Bb-D-F)** — the most popular static chord in
  jazz-funk, open and cool.
- Dominant 7(sus4)/9(sus4) — a "hanging" chord with no 3rd, ideal for a
  one-chord groove.
- Slash chords (upper-structure triads) — `D/C`, `F/G`, `Bb/C` — modern
  jazz color laid over a funk pulse.

**Pro-level tricks:**

- **Side-stepping/outside playing** — soloing over a static 1-chord vamp
  (e.g. parked on Em11): play E Dorian for 2 bars, then on bar 3 shift the
  entire melodic line a half-step up (F Dorian/F minor blues) for 1 bar to
  create dissonant "outside" tension, then resolve back to E Dorian on bar
  4 (back "inside"). This applies equally to soul jazz vamp sections
  (`soul-jazz-genre.md` §5) — documented once, here.
- Gospel plagal cadence (`IV -> I`) — borrowed from soul jazz
  (`soul-jazz-genre.md` §5) when a jazz-funk arrangement wants a warmer
  resolution instead of staying on the vamp.

## 6. Progression library

```
One-chord vamp (key of E minor):
| Em11 | Em11 | Em11 A7/E | Em11 |  (static 16 bar, varied by bass & synth layering)

Modal fusion progression ("Chameleon" style):
| Abm7 | Db7 | Abm7 | Db7 |  (interlocking bassline + Clavinet wah)
| Bm7  | E7  | Abm7 | Db7 |
```

Reference by name; pick and adapt, do not restate verbatim in every song.
This is the harmonic content the existing `fusion-vamp.json` template
already seeds — see §8.

## 7. Melody, slap bass & polyrhythm

**Scales:** minor blues, major/gospel blues (shared with soul jazz, see
`soul-jazz-genre.md` §7), and Dorian/Mixolydian as the primary vamp-solo
choices.

**Slap bass technique & notation:**

- Thumb slap (T) — the thumb strikes the string against the fretboard for a
  low, percussive note.
- Index pop (P) — the index finger snaps the string so it slaps back, a
  high popping sound.
- Ghost notes (x) — the left hand mutes the string, the right hand strikes
  it (pitchless percussive rhythm).
- Iconic 16th-note slap grid: `[ T . P x T P x T ]`.

**Guitar comping (scratch & chank):** the left hand loosens its grip on the
fretboard to mute the strings; the right hand strums a constant 16th-note
rhythm (down-up-down-up); the fretboard is only pressed for specific
syncopated accent hits. Contrast with soul jazz's Wes-style thumb comping
(`soul-jazz-genre.md` §8).

**Polyrhythmic stacking (3 against 4):** play a melodic phrase accenting
every 3 sixteenth-notes over a 4/4 drum groove — this creates the illusion
the tempo has shifted, while the underlying groove foundation stays stable.

## 8. Groove engine & the existing Tier-1 template

**Drums:**

- **Linear drumming** — the kick and snare never sound together; they
  alternate, precisely interlocking to fill the 16th-note grid. Snare is
  filled with ghost notes between the main 2-and-4 hits. This pattern
  concept layers onto the `fusion-tight` groove profile
  (`groove-rhythm/references/groove-profiles.md`) — it describes *which
  16th-note slots* kick/snare occupy, not a different set of tick
  offsets; use `fusion-tight`'s numeric pocket and arrange the hits
  linearly per this description.
- **Purdie shuffle** — for the half-time funk-swing hybrid feel, select the
  `purdie-shuffle` groove profile instead of `fusion-tight` (documented
  once in `groove-profiles.md`, shared with soul jazz).

**Existing Tier-1 template:** `jazz-composition/templates/fusion-vamp.json`
(registry id `fusion-vamp`) already encodes this genre's vamp-and-breakdown
recipe — static Em11 vamp, unison-riff and stab hooks, `fusion-tight`
groove, urgency->build->peak->release arc. Select it directly; it needs no
changes for this profile. Use `purdie-shuffle` as an alternate
`groove_profile` when a brief specifically wants the half-time shuffle pocket
instead of straight tight-16 funk (a template's `groove_profile` field can
be overridden per brief the same way `defaults` can, per
`templates/schema.md`).

## 9. Vintage production intent (downstream — not this package's job)

As with `classic-jazz-genre.md` §9 and `soul-jazz-genre.md` §9, this
package composes and arranges; it does not mix audio. Record the reference
brief's production intent here as guidance for whoever renders the mix:

```
[ DI bass + compressor ] -> [ wah-wah / phaser ] -> [ tight bus compression ]
```

- Parallel bass processing: one clean/punchy DI track, one lightly
  amp-driven/distorted track, blended.
- Kick drum EQ: punchy at 60 Hz, cut mud around 400 Hz, a click accent at
  3-5 kHz.
- Snare drum EQ: a sharp crack at 2.5-4 kHz.

Contrast with soul jazz's warm analog/tube chain (`soul-jazz-genre.md`
§9) — jazz-funk's intended sound is punchy and hi-fi electric, not vintage
warm.

## Three-way comparison matrix (Classic Jazz / Soul Jazz / Jazz-Funk)

The fastest way to check whether a composition has drifted into the wrong
neighboring genre — cross-reference `classic-jazz-genre.md` and
`soul-jazz-genre.md` §11 against this table:

| Element | Classic jazz (Dixieland/swing) | Soul jazz | Jazz-funk |
|---|---|---|---|
| Dominant era | 1920s-1930s | Late 1950s-1960s | Late 1960s-1970s |
| Main instruments | Brass, reeds, banjo, upright bass | Hammond B-3, tenor sax, guitar | Slap bass, Clavinet, synth, Rhodes |
| Rhythmic center | Swing triplets (2-beat/4-beat) | Bluesy swung 8ths / gospel | Straight 16th-notes (tight pocket) |
| Harmonic pattern | Complex progressions (AABA, turnarounds) | Blues 12-bar, gospel cadence | 1-2 chord vamps, static minor 11th |
| Sonic character | Natural acoustic, vintage gramophone | Warm analog, tube saturation | Punchy, hi-fi electric, synthetic |
| Groove profile(s) | `classic-jazz-swing` | `soul-jazz-swing` | `fusion-tight`, `purdie-shuffle` |

If a jazz-funk arrangement's rhythm section starts swinging or its harmony
starts moving through a long turnaround, it has drifted toward soul jazz or
classic jazz respectively — pull the groove back to a straight 16th grid
and the harmony back to a static vamp (§6).

## Common Pitfalls

| Symptom | Fix |
|---|---|
| Harmony keeps moving/modulating | Jazz-funk harmony is meant to be static — park on a vamp (§6) and generate variation from groove/dynamics, not chord changes |
| Slap bass sounds random | Use the T/P/x notation grid (§7) deliberately, don't freehand it |
| Groove reads as swing/soul jazz | The rhythm section has drifted off the straight 16th grid — confirm `fusion-tight` or `purdie-shuffle` is actually selected, not `soul-jazz-swing` or `classic-jazz-swing` (see the comparison matrix) |
| Soloing over the vamp sounds aimless | Apply the side-stepping trick (§5) for deliberate outside tension with a planned return |
| Arrangement never gets a payoff | Confirm the form actually reaches a breakdown + full-band release hit — `fusion-vamp.json`'s `anti_boredom_rules` already enforce this; don't skip it when building from scratch |
| Mix sounds vintage/warm instead of punchy | That's soul jazz's production intent, not jazz-funk's (§9) — also a downstream mix concern, not this package's job either way |

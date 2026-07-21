# Hip-hop jazz / jazz rap — genre profile

Adapted from a jazz-rap/hip-hop-jazz master-guide brief (submitted
2026-07-20, translated and restructured into this package's conventions —
**the brief's worked examples (chord progressions, the "Midnight Digging"
ABC score) are illustrative references only, not content to reproduce
literally**, same instruction the brief itself gives in §5's chop-and-flip
section and consistent with this package's standing rule against copying a
reference too literally). This is a **new** genre entry, closely adjacent
to the existing "Lofi jazz" cheatsheet entry — §9 below exists specifically
to keep the two distinct, since without care a "hip-hop jazz" brief and a
"lofi jazz" brief produce the same output.

Hip-hop jazz/jazz rap samples or emulates jazz's harmonic richness through
a boom-bap or Dilla-style drum lens: urban, contemplative, a late-night
street-corner mood, dusty and nostalgic. **Do not copy** a specific
sample, artist, or arrangement literally — translate the reference into
musical attributes (tempo, texture, harmonic loop, micro-timing,
sample-chop character). Identity comes from **micro-timing** first (§2) —
more than any other genre in this package, this one lives or dies on
whether the "push-pull" feel is actually there, not on the chords.

## Musical DNA baku

| Parameter | Default profile value |
|---|---|
| Tempo zone | 75-95 BPM, sweet spot 84-88 BPM |
| Meter | 4/4 |
| Tonal center | Minor 9th/11th (night, cool, urban) and major 7th/9th (warm, nostalgic) loops — see §4 |
| Rhythmic grid | Humanized/unquantized 16th grid with an explicit **push-pull**: kick ahead of the grid, snare behind it (see the `dilla-boom-bap` groove profile) |
| Palette (role -> instrument) | Anchor: kick + snare + sub-bass · Harmony: Rhodes/piano loop (often sample-chopped) · Rotation: muted trumpet/tenor sax lead riff · Ear-candy: vinyl crackle, tape hiss, vocal chops, street ambience |
| Density ceiling | The harmonic loop is 2-4 bars and repeats hypnotically — variation comes from filtering, drops, and layering (§8), not from changing the loop |

These are starting points, not law — bend toward the brief's specific
sub-style while staying inside the hip-hop-jazz family.

## 1. Sub-genres & hybridization

Pick one before choosing instrumentation — they lead to different palettes:

| Sub-genre | Approach |
|---|---|
| Golden-era boom-bap (classic '90s) | Built on vinyl-chop sampling plus a heavy drum machine (Akai MPC/E-mu SP-1200 character) — e.g. A Tribe Called Quest, Pete Rock, Gang Starr/Guru's *Jazzmatazz* |
| Lo-fi bossa / bossa-hop | Crosses bossa nova's nylon-guitar chords/picking (`bossa-nova-genre.md`) with dusty boom-bap drums — drops the Brazilian cross-stick in favor of a dusted kick/snare plus vinyl crackle |
| Neo-soul jazz rap (Soulquarians vibe) | Live instrumentation, no sampling, played with very slop/dragged timing — chorus/tremolo Rhodes, Moog sub-bass, D'Angelo/Questlove-style drums, muted trumpet. Shares ground with `neo-soul-genre.md`/`neo-soul-core` — see §9 |

## 2. Feel, micro-timing & the Dilla swing (the load-bearing section)

The defining trait of this genre is **imperfection as a deliberate
technique**, not sloppiness:

- **Unquantized/humanized** — computer precision is the enemy; the whole
  point is a human (or emulated-human) push-pull.
- **Laid-back snare** — dragged behind the grid, roughly +10 to +25 ms.
- **Pushed kick** — ahead of the grid, roughly -5 to -10 ms — together with
  the dragged snare this creates the "push-pull" tension that is this
  genre's single most identifiable fingerprint.
- **16th swing** — 54%-62% swing on percussive elements, especially the
  hi-hat.

Groove detail (tick offsets, gate ratios, and how this compares numerically
to `neo-soul-core`) lives in
`../../groove-rhythm/references/groove-profiles.md` under the
`dilla-boom-bap` profile — select it by name; do not re-derive per-note
timing here.

## 3. Instrument palette & hardware aesthetic

| Instrument | Role | Timbre / sound design |
|---|---|---|
| Kick drum | Heavy low-end punch | A dented, thudding sound — an old acoustic drum sample layered with a sub-sine (808-style) |
| Snare drum | Primary anchor | Gritty, dry wood crack/snap, layered with a rimshot or handclap |
| Hi-hats & cymbals | Groove driver | Feathered, dark/filtered metallic tone, a vinyl-hiss character |
| Sub-bass / upright | Harmonic foundation | Muted pure-sine sub-bass, or an upright-bass sample with a high-cut |
| Rhodes / piano | Main harmony | Fender Rhodes Mk I/II, Wurlitzer, or acoustic piano with vinyl crackle, chorus, and a low-pass filter |
| Muted trumpet / sax | Melody / lead riff | Harmon-muted trumpet (Miles Davis style) or a warm, smoky tenor sax |
| Textures/FX | Atmosphere | Vinyl crackle, tape hiss, spoken-word vocal, street ambience |

## 4. Harmony language & rootless-voicing bible

Harmony is a hypnotic 2-bar or 4-bar loop, not a developing progression.

**Chord types for a sample loop:**

- Minor 9th & 11th (Dm9, Dm11) — night, cool, urban.
- Major 7th & 9th (Fmaj7, Cmaj9) — warm, nostalgic.
- Dominant 13 & altered dominant (G13, G7b9, G7#9) — the turnaround back to
  the top of the loop.
- Minor 6/9 & minor(maj7) (Am6/9, Am(maj7)) — mysterious, dark.

**Rootless voicings** — omit the root on the harmony instrument so the bass
alone holds it, avoiding low-end clutter:

- **3rd & 7th shells** — voice only the 3rd, 7th, and extensions (9/11/13).
- Example over `Dm9 -> G13 -> Cmaj9`: play `F-A-C-E` for Dm9 (no D — reads
  as an Fmaj7 shape), `F-A-B-E` for G13 (no G), `E-G-B-D` for Cmaj9 (no C —
  reads as an Em7 shape).

**Drop-2 voicing** — take the second-highest note of a close-position
chord and drop it an octave, for a thicker Rhodes/piano sound with smooth
voice-leading (same technique named in `classic-jazz-genre.md` §5 and
`harmony/references/voicing-systems.md` — apply it here, don't re-derive
it).

## 5. Progression library & sample chop-and-flip technique

```
Golden-era boom-bap (A Tribe Called Quest / Pete Rock style):
| Dm9 | G13 | Cmaj9 | A7(b9,b13) |

Chill / lo-fi hop loop (J Dilla / Nujabes style):
| Fmaj9 | Em7 | Dm9 | Cmaj9 |

Dark urban minor (Mobb Deep / Guru style):
| Am9 | D9 | Fmaj7 | E7(alt) |
```

Reference by name; pick and adapt, do not restate verbatim in every song —
and treat these as vocabulary the way `templates/schema.md` intends a
`harmony_palette` to be read, not as one fixed progression to always use.

**Sample chop-and-flip technique** (describes a production workflow — a
composing brain working with this package writes the *result* of this
process as harmony/melody content, not the sampling steps themselves):

- **Filtering (the "Q-Tip trick")** — split an old jazz sample into two
  duplicate tracks: one low-passed at 300 Hz to isolate the bass, one
  high-passed at 400 Hz to isolate the piano/horn chords.
- **Pitch-shifting** — shift a sample -2 to +3 semitones for the stiff
  "artifact" character of an old hardware sampler.
- **Chop on transients** — cut a sample exactly on its main hits (chords,
  horn stabs, bass notes) and re-sequence them in a new order on a drum
  pad.

## 6. Rhythm pattern reference

One bar (4/4), 16 sixteenth-note steps. `K` = kick, `S` = snare, `H`/`x` =
hi-hat, `g` = ghost snare (quiet):

```
Standard boom-bap drum pattern (1-bar loop):
Beat:  | 1 . & . 2 . & . 3 . & . 4 . & . |
Hi-hat:| x . x . x . x . x . x . x . O . |
Kick:  | K . . . . . K . . . K . . . . . |
Snare: | . . . . S . . g . . . . S . . . |
```

This is the *written* pattern (which 16th-note slots sound) — the
`dilla-boom-bap` groove profile's ms/tick offsets (§2) are then applied on
top of it, per `advanced-microtiming.md` §1's notated-vs-performance
distinction. Program the pattern via
`../../midi-orchestration/assets/drum-grid-template.json`'s step-grid
format (`kick`/`snare`/`chh`/`ohh` roles), not as literal note events here.

## 7. Melody, horns & call-and-response

- **Solo brass riffs** — trumpet/sax do not play long lines; they play
  short 1-2 bar phrases that appear at the end of a 4-bar loop.
- **Vocal chops** — short vocal landings sampled from an old jazz/soul
  vocalist ("yeah", "baby", "ooh") used as rhythmic accents.
- **Call and response** — Rhodes/piano states the main pattern for bars
  1-3 (call); muted trumpet or DJ scratch answers on bar 4 (response).

## 8. Sound design & production intent (downstream — not this package's job)

As with `classic-jazz-genre.md` §9 and the other genre files, this package
composes and arranges; it does not mix or sample-process audio. Record the
brief's production intent here as guidance for whoever renders/mixes,
not as something this package's scripts implement:

- **Hardware/sampler emulation** — a bitcrusher around 12-bit/26 kHz for
  SP-1200/MPC-style crunch on high-mids; tape saturation on the drum bus to
  tame transients and add warmth.
- **Parallel drum compression ("New York" style)** — duplicate the drum
  bus, heavily compress one copy (8:1, fast attack/release), blend it in
  under the uncompressed bus.
- **Sidechain compression** — kick ducks bass and Rhodes 2-4 dB on every
  hit.
- **Frequency map & panning** (a starting reference, not a rule): kick/sub
  center, 30-120 Hz; snare center, 200 Hz body + 3-5 kHz snap; Rhodes/piano
  wide stereo (20-40% L/R), cut below 200 Hz, boost ~1.5 kHz; hi-hats
  slightly right, high-pass above 1 kHz; muted trumpet/lead slightly left,
  800 Hz-4 kHz; vinyl crackle extra-wide, band-passed 2-8 kHz.

## 9. Differentiating hip-hop jazz from this package's other genres

This is the section to check before composing — hip-hop jazz overlaps
harmonically and texturally with several genres already in this package.
The distinguishing axis is almost always **micro-timing and the presence
of a rap/sample-chop identity**, not the chord vocabulary (which is close
to lofi jazz's and neo-soul's).

| Genre | What actually differs from hip-hop jazz |
|---|---|
| Lofi jazz (`style-cheatsheets.md`) | Lofi jazz is the wider, more ambient "beat tape" family — loose swung-or-straight-16th, no requirement for a push-pull kick/snare split or a rap vocal. Hip-hop jazz is more specific: boom-bap or Dilla-style push-pull timing (§2), usually built for or around a rap vocal, and its identity leans harder on sample-chop/hardware-emulation character (§5, §8). If a piece has no push-pull and no sample-chop aesthetic, it is lofi jazz, not hip-hop jazz. |
| Jazzhop/neo-soul (`style-cheatsheets.md`, `neo-soul-genre.md`) | The `neo-soul-core` groove profile is numerically close to `dilla-boom-bap` (both drag the snare a similar amount) — the difference is the **kick**: `neo-soul-core`'s kick is an anchor near the grid; `dilla-boom-bap`'s kick is deliberately pushed *ahead* of it. Neo-soul also has no sampling/vinyl-crackle identity. The "Neo-soul jazz rap" sub-genre (§1C) is the deliberate bridge between the two — when a brief wants that hybrid, use `dilla-boom-bap` with neo-soul's Rhodes/chorus/mute palette. |
| Bossa nova (`bossa-nova-genre.md`) | Bossa is straight and unswung with only the lead laid back (`bossa-nova-straight` profile). The "lo-fi bossa/bossa-hop" sub-genre (§1B) deliberately crosses it with boom-bap drums — when building that hybrid, keep the guitar batida from `bossa-nova-genre.md` but swap the drum profile to `dilla-boom-bap`, not `bossa-nova-straight`. |
| Soul jazz / classic jazz swing | Both swing on an 8th-note grid; hip-hop jazz swings a 16th-note grid at a much slower tempo range and adds the push-pull kick/snare split those genres don't have. |

## 10. Arrangement blueprint

```
[INTRO] (4-8 bar)
- Vinyl crackle + night-city ambience.
- A filtered Rhodes chord loop (low-pass engaged, muffled).
- An old spoken-word/dialogue sample enters.

[VERSE 1] (16 bar) - entrance
- The low-pass filter releases (Rhodes becomes clear).
- Boom-bap drums + sub-bass enter together.
- Rap vocal enters with a laid-back flow.
- Bars 8 & 16: the drums drop out briefly before the next hit.

[HOOK / CHORUS] (8 bar)
- Muted trumpet/sax riff enters, playing the main melody.
- Optional DJ scratch or vocal-sample hook.
- Shaker/tambourine accents reinforce the groove.

[VERSE 2] (16 bar)
- Focus returns to the rap vocal.
- Variation: swap sub-bass for a sampled upright-bass character.

[BRIDGE / BREAKDOWN] (8 bar)
- Drums drop out entirely, leaving only the Rhodes chord loop, sub-bass,
  and a flute/sax soloist - contrast before the climax.

[OUTRO] (8 bar)
- The mix filters closed again (low-pass engaging).
- Vinyl crackle grows louder.
- Slow fade out.
```

## Common Pitfalls

| Symptom | Fix |
|---|---|
| Kick and bass clash (muddy) | Cut bass EQ at the kick's frequency (~60 Hz) and sidechain bass to kick (§8) |
| Loop feels boring over 16 bars | Add ghost snares, drop the drums on beat 4 every 4 bars, or add a random ear-candy hit (vinyl pop, horn stab) — vary the loop's texture, not its chords |
| Drums feel stiff/robotic, closer to a straight beat | Quantize is fully on — turn it off, apply the `dilla-boom-bap` profile's push-pull offsets and 54-62% hi-hat swing (§2) |
| Sample/instrument sounds too clean/modern | Missing the analog/vinyl texture — add the bitcrush/tape-saturation/vinyl-emulation chain (§8) |
| Low end is thick/muddy | A harmony instrument is doubling the bass's root — apply rootless voicings (§4), let the bass alone hold the root |
| Reads as lofi jazz or neo-soul instead of hip-hop jazz | No push-pull kick/snare split and no sample-chop identity present — see §9 |

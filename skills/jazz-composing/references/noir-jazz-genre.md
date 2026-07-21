# Noir jazz / dark jazz — genre profile

Adapted from a noir-jazz/dark-jazz style brief (submitted 2026-07-20,
translated and restructured into this package's conventions). **The
brief's worked ABC example ("Rain-Slicked Asphalt") is a reference only,
not a template to imitate note-for-note** — this file and the Tier-1
template below stay at the level of chord vocabulary, phrasing rules, and
arrangement structure, the same instruction already applied to
`hiphop-jazz-genre.md` and `smooth-jazz-genre.md`'s source briefs. This is
a **new** genre entry; `style-cheatsheets.md` gets a new "Noir jazz / dark
jazz" entry pointing here.

Noir jazz scores a scene, not a dancefloor: a dark urban alley, cigarette
smoke in an empty bar, rain on cold asphalt, a cynical/isolated detective
narrative — mysterious, melancholic, cinematic. **Do not copy** a specific
recording, artist, or arrangement literally — translate the reference into
musical attributes (tempo, texture, harmonic density, articulation,
silence). Identity comes from **space** first (§2) — more than any other
genre in this package, what is *not* played matters as much as what is.

## Musical DNA baku

| Parameter | Default profile value |
|---|---|
| Tempo zone | 35-65 BPM, sweet spot 42-50 BPM — the slowest genre in this package by a wide margin |
| Meter | 4/4, felt loosely — bar lines matter less than phrase/decay length |
| Tonal center | Minor, exotic-tinged — minor-major 7th as the signature tonic color, half-diminished tension, altered dominants |
| Rhythmic grid | Ultra-dragged/rubato — the whole melodic/harmonic surface sits far behind the beat; only the brushed-snare swirl stays "on grid" as a single soft timekeeper (see `noir-jazz-rubato` groove profile) |
| Palette (role -> instrument) | Anchor: upright bass (deep, sparse) + brushed snare/cymbal swirl · Voice: Harmon-muted trumpet or sub-tone tenor/bari sax · Harmony: felt/dark piano or filtered Rhodes · Ear-candy (optional, use with caution — see §3) environmental/foley texture |
| Density ceiling | Extremely low — one sustained note or chord at a time, left to decay fully before the next enters; dynamics stay ppp-pp throughout, no sudden emotional swells |

These are starting points, not law — bend toward the brief's specific
sub-style while staying inside the noir-jazz family.

## 1. Sub-genres & hybridization

Pick one before choosing instrumentation:

| Sub-genre | Approach |
|---|---|
| Classic 1950s detective noir (traditionalist) | Purely acoustic, evoking classic 1950s film-noir scoring (Miles Davis's *Ascenseur pour l'échafaud*) — muted trumpet, brushed snare, sparse upright-bass plucks, dark acoustic piano |
| Dark ambient / doom jazz (Bohren & der Club of Gore style) | Extremely slow (<35 BPM), minimal melody, drone-focused — chords held 8-16 seconds, heavy-tremolo/reverb electric guitar, an almost inaudible brushed snare |
| Cyberpunk / neo-noir synth (Blade Runner/Vangelis style) | Acoustic jazz instruments over vintage analog synth pads (CS-80/Prophet-5 style), deep synthetic sub-bass, a dark futuristic sheen |
| Trip-hop noir (Portishead/Massive Attack style) | Dark piano chords over a heavier downtempo/vinyl-loop drum feel, still tied to a slow tempo |

## 2. Feel, micro-timing & the power of silence (the load-bearing section)

- **The power of silence (space)** — noir jazz is not powered by a dense
  groove but by the empty space between notes. Let piano/trumpet notes
  ring and fully decay before the next note sounds.
- **Ultra-dragged/rubato feel** — the whole lead melody and chord voice sit
  far behind the beat, as if the player is exhausted or walking slowly
  through rain.
- **Non-linear dynamics** — the dynamic range stays *pianississimo* (ppp)
  to *pianissimo* (pp). No sudden emotional swells; the mood stays settled
  and low-intensity throughout.

Groove detail (canonical ms offsets, gate ratios) lives in
`../../groove-rhythm/references/groove-profiles.md` under the
`noir-jazz-rubato` profile — select it by name; do not re-derive per-note
timing here. Note that this profile is dominated by rubato/phrase-level
placement rather than a subdivided swing grid — unlike every faster genre
in this package, there usually isn't a 16th grid worth swinging.

## 3. Instrument palette & timbre

| Instrument | Role | Timbre / sound design |
|---|---|---|
| Brushed snare & cymbals | Textural pulse | Constant wire-brush swirl/stirring on the snare; ride cymbal struck softly on the edge (washy) |
| Kick drum | Low pulse | A soft felt beater, fully muted, no sharp attack — a gentle heartbeat "thud" |
| Upright bass (contrabass) | Deep anchor | Very deep pizzicato, or arco (bowed); dominant low end, long sustain |
| Acoustic piano / Rhodes | Harmonic stabs | A felt-muted acoustic piano, or a Rhodes with a low-pass filter and dark chorus |
| Muted trumpet | Primary voice | Harmon mute (stem out) — thin, nasal, very private, with a high, singing resonance |
| Tenor/baritone sax | Secondary voice | Sub-tone technique (breath dominates over pitched tone) in the low register |
| Electric guitar | Atmospheric wall | Clean tone, slow-rate vintage tremolo, wet spring reverb |
| Environmental/foley texture | Atmospheric depth (**optional — see warning below**) | Rain, neon hum, footsteps, a match strike, ice, street ambience |

### Warning: ambient/foley texture is 100% optional

Environmental samples are easy to overuse. Layered too loud or too dense,
they create excess noise-floor clutter — hiss in the high end (rain),
mud in the low end (neon hum) — that buries the primary instruments'
detail and tires the listener. If used at all: fader it **-18 to -24 dB**
below the main music (it should read as a shadow behind the music, not a
foreground element); band-pass it (cut below 400 Hz, cut above 5 kHz) so
it never competes with the kick/bass or the brushed-snare hiss. **If the
core instrumentation (piano, bass, trumpet, reverb) already has enough
space and a beautiful decay, skip the ambient layer entirely** — it is
never required for the genre to work.

## 4. Harmony: vocabulary, cluster voicings & exotic scales

**Required chord vocabulary:**

- **Minor-major 7th (Am(maj7) = A-C-E-G#)** — the genre's single most
  iconic chord (the "James Bond sound").
- Minor 9th & 11th (Dm9, Dm11) — cold, wide, melancholic.
- Half-diminished/m7b5 (Bm7b5 = B-D-F-A) — tension that hangs without
  resolving.
- Major 7(#11) (Fmaj7#11 = F-A-C-E-B) — a mysterious Lydian color.
- Altered dominant (E7b9b13 = E-G#-D-F-C) — maximum tension before a
  resolution.

**Cluster voicings & friction** — place two notes a semitone apart near
the middle of a piano/Rhodes voicing to create a mysterious frequency
friction. Example cluster for `Am(maj7,9)`:
`A1-E2-G#2-A2-C3-B3` (the friction sits between G#-A and C-B).

**Exotic scales for melody/solo:**

- Hungarian minor (`1-2-b3-#4-5-b6-7`) — dramatic, tense darkness.
- Double harmonic minor — an investigative, anxious character.
- Microtonality/quarter-tone bends — the trumpet/sax approaches a target
  pitch with a slow micro-glissando from a quarter-tone below rather than
  attacking it cleanly (a "crying" effect).

## 5. Progression library & structural mechanics

```
The detective's walk (classic minor line cliche):
| Am(maj7) | Am7 | Am6 | Fmaj7(#11) | E7(b9,b13) |
Mechanism: an inner voice descends chromatically (G# -> G -> F# -> F -> E)
over a static A bass.

The rainy alleyway (modal minor interchange):
| Cm9 | Fm9 | Abmaj7(#11) | G7alt |
Mechanism: i - iv - bVI - V7, a broad, gradually darkening color.

Twin Peaks mood (suspended melancholy):
| Dm11 | Bbm9/D | Dm9 | A7(b9) |
Mechanism: the move from Dm11 to Bbm9/D creates a disorientation/loss feel.
```

Reference by name; pick and adapt, do not restate verbatim in every song.

## 6. Rhythm pattern reference

One bar (4/4), felt very slow. `S` = constant brush swirl, `T` = a very
soft brush tap, `K` = soft felt kick, `R` = a fading ride cymbal hit:

```
Beat:          | 1   .   2   .   3   .   4   .   |
Brushed swirl: | [====== constant swirl ======]  |
Soft tap/rim:  | .   .   .   .   T   .   .   .   |
Soft kick:     | K   .   .   .   .   .   K   .   |
Ride cymbal:   | R   .   .   .   R   .   .   .   |
```

The brush swirl is the only element that stays on the grid (offset 0) —
everything else drags behind it, per §2 and the `noir-jazz-rubato` profile.

## 7. Melody, horns & call-and-response

- **Melodic character** — very short phrases, filled with long sustained
  notes, followed by silence.
- **Muted-trumpet technique** — lean on blue notes (especially the b5 and
  b3), approached with a slow bend/glissando from below the target.
- **Call and response:** the muted trumpet blows a mournful 3-note phrase
  over bars 1-2 (call); 2 seconds of silence, then a single low piano
  chord answers, left to ring, over bars 3-4 (response).

## 8. Sound design & production intent (downstream — not this package's job)

As with every other genre file in this package, this package composes and
arranges; it does not mix or process audio. Record the brief's production
intent here as guidance for whoever renders/mixes:

- **Reverb architecture (the "dark chamber")** — a convolution reverb using
  a Large Church, Wooden Hall, or Dark Plate impulse response; decay
  3.5-6.0 seconds; high-cut the reverb return above 4-5 kHz (keeps it from
  reading as bright/digital), low-cut below 200 Hz (keeps it from reading
  as muddy).
- **Sidechain reverb "blooming"** — duck the reverb return while the
  trumpet is sounding (keeps the melody close/clear), then let the reverb
  tail bloom open into the silence the instant the trumpet stops — a
  compressor on the reverb aux, sidechained from the trumpet/sax channel.
- **Pitch instability / wow & flutter** — automate a tape-emulator's pitch
  modulation ±5 to 15 cents, slowly, on long notes, for an old
  tape/vinyl-degradation character.
- **Frequency map & panning** (a starting reference): upright bass center,
  boost 80-150 Hz, cut above 2 kHz; muted trumpet center/slightly left,
  boost 1.2-2.5 kHz (mute "bite"), cut above 7 kHz; dark piano wide stereo
  (30% L/R), high-pass above 100 Hz, low-pass below 6 kHz; brushed snare
  20% right, high-pass above 300 Hz; optional ambient/rain extra-wide, per
  §3's warning (band-passed 400 Hz-5 kHz, very low volume).

## 9. Arrangement blueprint (cinematic "scene" form)

Noir jazz is scored in **scenes**, not verse/chorus — a deliberately
different structural language from this package's other genre files:

```
[SCENE 1: THE ALLEYWAY / INTRO] (8 bar)
- Upright bass plays a single note (e.g. A), plucked once every 2 bars.
- The first piano chord (Am(maj7)) sounds and is left to decay over 4 bars.
- (Optional) a very thin rain/ambience texture in the background.

[SCENE 2: THE SHADOW / MAIN THEME] (8 bar)
- The brushed-snare swirl enters very softly.
- Muted trumpet enters with the slow, mournful main melody.
- Harmony: the line-cliche progression (Am(maj7) -> Am7 -> Am6 -> Fmaj7#11).

[SCENE 3: THE CONFESSION / INTERLUDE] (8 bar)
- The trumpet stops.
- Tenor sax (sub-tone) enters in a low register, duetting with the piano.
- A temporary modulation to Dm9.

[SCENE 4: THE FOG / AMBIENT BREAK] (4 bar)
- Drums and bass stop entirely.
- Only the piano's reverb tail and a single trumpet note with feedback
  delay remain.

[SCENE 5: THE RESOLUTION / OUTRO] (8 bar)
- The full ensemble returns to restate the main theme.
- The tempo naturally slows (molto ritardando).
- Ends on a single upright-bass pluck and an Am(maj7,9) chord left to
  decay into total silence.
```

## Common Pitfalls

| Symptom | Fix |
|---|---|
| Music feels busy/rushed | Too many notes, phrases too close together — cut roughly half the melody notes; let every chord ring for at least a full 2 bars |
| Noisy/muddy mix | Ambient/foley samples are burying the primary instruments — turn the ambient layer off, or drop it to -20 dB and band-pass 400 Hz-5 kHz (§3) |
| Mood reads as cheerful/bright | Plain major chords or overly bright high-end — swap major 7ths for `maj7#11` or `m(maj7)` (§4); low-pass piano/trumpet above ~6 kHz |
| Reverb tail buries clarity | The reverb return carries too much low/low-mid — apply sidechain reverb blooming and cut the return below 200 Hz / above 4 kHz (§8) |
| Drums feel like pop/rock | Using drumsticks or a standard snare sample — replace with brushed-snare swirls; remove the kick's sharp attack entirely (§3, §6) |
| Reads as bossa/lofi/neo-soul instead of noir | Not dragged nearly far enough, or the tempo is too fast — noir's offsets (§2) are several times larger than any other profile in this package, and its tempo range (35-65 BPM) sits well below every other genre's floor |

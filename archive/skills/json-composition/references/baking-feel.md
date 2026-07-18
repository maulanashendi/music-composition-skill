# Baking feel into authoring JSON

**The engine does not humanize the JSON path.** Whatever pocket, swing, or
dynamic shape a performance needs has to be written explicitly into `beat`,
`vel`, and `artic` values on individual notes — there is no post-processing
step downstream that adds it for you. This is the opposite of the drum
step-grid path (`grid_to_midi.py`), which does apply swing/humanization at
render time. If it isn't in the JSON, it will not be heard.

This is the single most common way a schema-valid file still sounds
mechanical: every note dead-on-grid, every velocity the same number. The
validator (`scripts/validate_composition.py`) cannot catch this — it checks
structure, not feel. `rubric.md` is what checks for it.

## Three levers, all mandatory to touch

### 1. `beat` — off-grid placement

A note written exactly on `1`, `2`, `3`, `4` sounds quantized. Nudge notes
that should sit ahead of or behind the beat:

- **Backbeat laid-back**: instead of snare on beat 2 and 4 exactly, write
  `2.02`/`4.02` (a touch behind) — see the template's drum voice, which does
  exactly this on every backbeat hit.
- **Lead phrase pickups/lay-back**: a lead note that should feel like it's
  "reaching" for the next downbeat can sit at `2.52` instead of `2.5` (the
  template's lead voice does this on the `C5` pickup) — a hair late relative
  to the literal half-beat grid.
- Don't nudge everything by the same offset — that just moves the grid, it
  doesn't create feel. Nudge selectively: backbeats behind, pickups ahead or
  behind depending on the phrase, downbeats/arrivals usually stay closer to
  the grid (that's what makes them read as arrivals).

### 2. `vel` — dynamic shape, not a flat number

Every voice needs velocity spread, not one repeated value:

- **Ghost notes / secondary hits low**: an off-beat hi-hat or a passing
  comping stab should sit well below the section's main dynamic — low
  velocity relative to the anchors around it.
- **Accents high**: a hook note, a backbeat snare, an arrival chord tone
  should sit above the surrounding average.
- A voice where every note has the same `vel` will fail the rubric's
  dynamics row regardless of how good the pitches are — write the spread
  deliberately, per note, not as an afterthought pass at the end.

### 3. `artic` — length, not just legato everywhere

`artic` controls gate length downstream (how much of `dur` actually sounds).
Use it to separate held tones from clipped ones: `legato` for phrases that
should breathe into each other, `staccato` for detached comping stabs,
`accent` for a note that should hit hard and cut, `normal` as the default
for drums and anything that isn't making a deliberate length statement.

## Where the numbers come from — don't invent them per song

`../groove-rhythm/references/groove-profiles.md` (the `neo-soul-core`
profile) is the shared numeric table this package already maintains for
exactly this purpose — instrument-relationship offsets (kick as anchor,
snare/keys laid-back behind the grid, bass pickups ahead of it) and gate
ratios per role (bass ~0.78–0.90, keys ~0.62–0.86, lead ~0.86–0.96). That
table is written in ticks/ms against a reference tempo; this skill's job is
to **translate those relationships into concrete `beat`/`vel`/`artic`
numbers** for the song at hand, not to re-derive the feel from scratch or
invent a different set of offsets. Concretely:

- Snare/keys behind the grid → write their `beat` a hair past the grid
  value (`2.02`–`2.05`-ish territory for a quarter-note grid, scaled to
  however fine the written rhythm is) — same direction as the profile's
  tick offsets, just expressed as a beat fraction instead of ticks.
- Bass pickups ahead of the grid → write their `beat` slightly *before* the
  nominal value where the meter allows it (e.g. a pickup approaching beat 3
  can sit fractionally earlier within beat 2's span).
- Gate ratios → translate into `artic` choice (a ratio near the top of a
  role's range reads as `legato`; near the bottom reads as `staccato`) —
  don't try to write a literal fractional gate length, `artic` is the
  authoring-level knob for it.

If a song calls for a pocket other than `neo-soul-core`, name the deviation
and translate its numbers the same way — don't silently default to
dead-on-grid because no profile was named.

## Check yourself before declaring the file done

- Does every voice have at least one note off the literal integer/half-beat
  grid where the groove calls for it (drums almost always; lead and comping
  voices at least at phrase edges)?
- Does every voice's velocity column have a visible spread (not one value
  repeated `n` times)?
- Are ghost/secondary hits distinguishably lower than accents in the same
  voice?

If any answer is "no" for a voice the groove requires feel in, go back and
write it in — this is not something a downstream pass will add.

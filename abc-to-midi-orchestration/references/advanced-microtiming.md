# Advanced microtiming, pocket, velocity, and note length

> Adapted from `jazz-composition-designer` (archived portable skill package,
> consolidated 2026-07-13). This is the deep reference for *why* a pocket is
> shaped the way it is. For the ready-to-use numeric starting points this
> package and the downstream `daw_generative` engine share (per-role tick
> offsets, gate ratios), see `references/groove-profiles.md` — that file
> distills §4 and §9 below into a concrete table so the composing brain only
> has to *pick a profile*, not derive ticks per note.

## Contents

1. Principles
2. Time conversion
3. Reference-layer method
4. Instrument relationships
5. Swing and subdivision
6. Velocity and timing covariance
7. Note-off timing
8. Section-level pocket development
9. Microtiming profiles
10. DAW output format
11. Audit

## 1. Principles

Microtiming is the controlled relationship between performed events and a reference pulse. It is not indiscriminate randomization.

Use timing offsets only after the notated rhythm and groove work on the grid. Keep structural attacks, ensemble hits, and transition cues precise enough to remain intelligible.

Separate:

- **notated displacement:** a compositional event expressed in rhythm;
- **performance placement:** a small offset around the intended onset;
- **swing:** systematic unequal subdivision or accent behavior;
- **humanization:** bounded variation in timing, velocity, duration, and articulation.

Do not use microtiming to repair a weak rhythm.

## 2. Time conversion

At tempo `BPM`:

- quarter-note duration in milliseconds = `60000 / BPM`;
- one beat at PPQ resolution has `PPQ` ticks;
- ticks for a beat fraction = `PPQ * fraction`;
- milliseconds for a tick = `(60000 / BPM) / PPQ`.

Example at 75 BPM and 960 PPQ:

- quarter note = 800 ms;
- one tick = approximately 0.833 ms;
- 12 ticks = approximately 10 ms.

Report both ticks and approximate milliseconds when a DAW-first brief requires portability.

## 3. Reference-layer method

1. choose the reference layer;
2. mark anchor events that stay near grid;
3. choose which layers push, sit, or drag relative to the reference;
4. set bounded offset ranges;
5. set velocity and note-length ranges;
6. test the pocket at low volume and without effects;
7. change the profile only at a formal reason.

Possible reference layers:

- snare or backbeat;
- hi-hat grid;
- kick pattern;
- bass pulse;
- sampled-feeling harmonic loop;
- ride cymbal in swing.

A reference layer may itself contain intentional swing, but it must remain internally consistent.

## 4. Instrument relationships

### Drums

- keep primary downbeats and major fills structurally clear;
- allow hats or ride to imply forward motion;
- allow backbeat to sit slightly behind when a relaxed pocket is desired;
- use ghost notes as dynamic and timing responses, not random clutter;
- keep kick-bass relationships deliberate.

### Bass

Choose one dominant relationship per section:

- lock with kick;
- slightly anticipate selected chord attacks;
- sit behind the drum reference for weight;
- use mixed placement, with arrivals centered and passing notes flexible.

Do not offset every bass note equally.

### Piano, Rhodes, or guitar

- chord attacks may sit behind the reference while pickups anticipate;
- grace notes and rolled attacks require internal order;
- note lengths influence groove as strongly as onset timing;
- separate left-hand and right-hand placement only when the texture remains clear.

### Lead melody

- phrase-level push and pull is more convincing than per-note randomness;
- keep structural target notes close enough to the harmonic arrival;
- allow pickups, repeated notes, and phrase endings to carry timing character;
- preserve breath and silence.

## 5. Swing and subdivision

Do not encode swing as one fixed ratio across all tempi and layers.

Specify:

- subdivision: eighth, sixteenth, triplet, or mixed;
- primary swing carrier;
- approximate range or qualitative feel;
- whether melody follows, resists, or floats over the swing carrier;
- whether the ratio becomes more even in fills or faster passages;
- whether backbeat placement is independent of subdivision swing.

For DAW output, state swing as either:

- grid ratio or template amount;
- explicit alternate-subdivision offsets;
- performance direction when exact offsets would be misleading.

## 6. Velocity and timing covariance

Timing and velocity should not be randomized independently without purpose.

Possible relationships:

- stronger anchor notes stay closer to grid;
- softer ghost notes may vary more;
- anticipated notes may be lighter to avoid sounding rushed;
- delayed backbeats may be stronger for weight;
- phrase-ending notes may be softer and longer;
- fills may tighten toward the target downbeat.

Use velocity ranges by role, not one global range.

## 7. Note-off timing

Gate and release create pocket.

Specify for each role:

- staccato, detached, sustained, or legato behavior;
- percentage or musical duration of the nominal note;
- whether note-offs precede drum accents;
- whether chord tails overlap the next event;
- pedal behavior;
- whether repeated chords reattack fully or partially.

Avoid pedal blur when syncopation depends on silence. Avoid uniformly short notes when warmth depends on overlap.

## 8. Section-level pocket development

Pocket may evolve with form.

Examples:

- intro: harmony loose, percussion minimal;
- groove establishment: reference layer stable;
- theme: bass and kick lock more clearly;
- breakdown: hats continue while kick drops out;
- solo: comping becomes more responsive and less quantized;
- final return: anchor events tighten while fills remain expressive;
- outro: note lengths increase as rhythmic density falls.

Do not change timing profile at every section unless the form requires it.

## 9. Microtiming profiles

These are starting frameworks, not universal genre presets.

### Tight acoustic or ensemble profile

- major attacks near grid;
- small bounded variation on inner notes;
- fills converge on target beats;
- articulation creates most of the feel.

### Relaxed lofi profile

- stable drum reference;
- selected snare or chord attacks slightly late;
- pickups may be early;
- bass alternates lock and drag by phrase;
- velocity and note length carry much of the imperfection.

### Sample-like profile

- repeated harmonic clip retains consistent internal timing;
- drums may have a separate pocket;
- loop seam and pickup remain identical until a deliberate mutation;
- do not re-randomize each repetition.

### Elastic neo-soul profile

- chord attacks and bass may negotiate the beat;
- inner grace notes use ordered timing;
- strong arrivals remain clear;
- syncopated anticipation is not confused with early humanization.

### Forward modern-jazz profile

- ride or subdivision layer may push;
- bass may center or slightly lead structural motion;
- comping placement remains responsive;
- ensemble figures tighten at landmarks.

## 10. DAW output format

For each event or event class, provide:

| Track | Event role | Nominal position | Offset ticks | Approx ms | Velocity | Duration/gate | Variation rule |
|---|---|---|---:|---:|---:|---|---|

For repeated patterns, define:

- fixed anchor events;
- bounded variation events;
- distribution or alternating pattern;
- section exceptions;
- reset rule at transitions.

Do not create a giant note-by-note table when a concise pattern rule is clearer. Provide explicit events for the core loop and rules for controlled variation.

## 11. Audit

- Is the notated rhythm strong before humanization?
- Is the reference layer named?
- Are offsets relational and bounded?
- Are structural cues tight enough?
- Do timing, velocity, and note length support one pocket?
- Is the loop internally consistent across repetitions?
- Are section-level timing changes justified?
- Can performers interpret the feel without DAW numbers?
- Are approximate milliseconds derived from the stated BPM and PPQ?

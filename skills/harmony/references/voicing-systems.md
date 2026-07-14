# Exact voicing, register, attack, and voice-leading systems

> Adapted from `jazz-composition-designer` (archived portable skill package,
> consolidated 2026-07-13). Pitches here use **scientific pitch notation**
> (middle C = `C4`), which is not this package's ABC pitch notation. When
> translating a voicing into the ABC written by the `abc-notation` module
> (`skills/abc-notation/references/abc-syntax.md`; called `abc-notation-writer`
> before the restructure), convert explicitly: ABC's unmarked uppercase
> `C` = `C4`, each comma lowers an octave (`C,` = `C3`, `C,,` = `C2`), and
> each apostrophe raises one (`c'` = `C6`, where lowercase `c` = `C5`). Use
> this reference to decide *which* pitches and voice-leading path to write;
> use `abc-syntax.md` for how to notate the result.

## Contents

1. Required exactness
2. Pitch and register notation
3. Voice hierarchy
4. Register zones
5. Core voicing families
6. Piano and Rhodes procedures
7. Exact voice-leading path
8. Inner-line design
9. Attack and release design
10. Voicing variation across form
11. Instrument-specific reductions
12. Audit

## 1. Required exactness

Use this reference when the user requests lofi, neo-soul, smooth jazz, contemporary jazz, production-ready harmony, playable keyboard parts, or exact voicings.

Do not stop at chord symbols. For every important chord event provide:

- concert pitch names with octave numbers;
- optional MIDI note numbers for DAW-first output;
- bass note and instrument;
- left-hand and right-hand allocation when keyboard-specific;
- top note;
- attack position and duration;
- pedal or release behavior;
- voice-leading into and out of the voicing;
- optional variation voicing for later recurrence.

Use scientific pitch notation where middle C is `C4`. State another convention explicitly if required.

## 2. Pitch and register notation

Recommended format:

`Bass: C2; LH: E3-Bb3; RH: D4-A4; top: A4`

For DAW output:

`C2=36, E3=52, Bb3=58, D4=62, A4=69`

Spell notes by harmonic function even when the DAW displays enharmonic equivalents.

## 3. Voice hierarchy

Prioritize in this order unless style requires otherwise:

1. written melody or intended top line;
2. quality-defining tones;
3. guide-tone path;
4. requested color tone;
5. bass architecture;
6. root when needed for clarity;
7. fifth when it contributes quality, support, or line;
8. doublings only when register or power justifies them.

A voicing is not improved by containing every chord tone.

## 4. Register zones

These are practical starting zones, not absolute limits.

### With a separate bass instrument

- bass foundation: approximately C1-C3 as instrument permits;
- keyboard left hand: approximately C3-C4 for shells and guide tones;
- keyboard right hand: approximately C4-C6 for color and melody;
- keep dense seconds and sevenths out of the lowest zone unless weight or cluster is intentional.

### Solo keyboard or no-bass setting

- left hand may include root or tenth;
- separate bass from dense upper structure;
- avoid placing all essential voices in one middle-register block;
- use sustain and spacing to create depth rather than excessive note count.

Adjust for instrument timbre, dynamics, and arrangement.

## 5. Core voicing families

Examples are in C and must be transposed and respelled by function.

### Major 6/9

Possible pitch content: `C-E-A-D`.

Use for open tonic color without a strong major seventh. Possible exact realization with bass:

`Bass C2; LH E3-A3; RH D4-G4-C5`.

### Major 9

Core color: `3-7-9`, with optional 5 or 13.

Example:

`Bass C2; LH E3-B3; RH D4-G4`.

### Major 9 sharp 11

Preserve the sharp 11 and avoid an unnecessary natural 11.

Example:

`Bass C2; LH E3-B3; RH D4-F#4-A4`.

### Minor 9

Core color: `b3-b7-9`.

Example:

`Bass C2; LH Eb3-Bb3; RH D4-G4`.

### Minor 11

Use the 11 as structural color and control low density.

Example:

`Bass C2; LH Eb3-Bb3; RH D4-F4-G4`.

### Minor 6/9

Useful for tonic minor and modal color.

Example:

`Bass C2; LH Eb3-A3; RH D4-G4`.

### Dominant 13

Core function: `3-b7-13`, with optional 9.

Example:

`Bass C2; LH E3-Bb3; RH D4-A4`.

### Dominant 13 sus

Prioritize `4-b7-9-13`; omit the third unless the suspension resolves.

Example:

`Bass C2; LH F3-Bb3; RH D4-A4`.

### Altered dominant

Choose alterations from melody and destination. Example C7 with b9 and b13:

`Bass C2; LH E3-Bb3; RH Db4-Ab4`.

State the resolution of `Db4` and `Ab4`.

### Quartal or hybrid field

Define bass and top note because stacked fourths alone do not determine function.

Example over C pedal:

`Bass C2; LH Bb3-Eb4; RH A4-D5-G5`.

## 6. Piano and Rhodes procedures

### With bass instrument

1. omit root from keyboard unless ambiguity or effect requires it;
2. place guide tones in left hand or distribute across hands;
3. assign color tones and top line to right hand;
4. keep left hand rhythm sparse enough for bass clarity;
5. vary note duration and attack, not only pitch content.

### Without bass instrument

1. write a bass line or root/tenth framework;
2. avoid sustained low root under every chord when movement is needed;
3. separate bass attacks from upper syncopation when groove benefits;
4. use pedal carefully to prevent low-register blur.

### Rhodes-oriented color

- exploit sustained upper extensions;
- use sparse left-hand shells;
- use inner semitone movement;
- allow delayed or rolled attacks;
- avoid constant full-register density;
- coordinate tremolo, chorus, or drive with form outside the pitch notation.

## 7. Exact voice-leading path

For a sequence, create a voice table rather than selecting isolated shapes.

| Chord | Bass | Voice 1 | Voice 2 | Voice 3 | Voice 4 | Top |
|---|---|---|---|---|---|---|

Procedure:

1. lock melody or intended top line;
2. lock bass destinations;
3. identify common tones;
4. move guide tones by semitone or whole tone where functional;
5. preserve one color line when possible;
6. avoid unnecessary register jumps;
7. check hand span and instrument range;
8. listen for independent inner lines;
9. revise chord symbols if the actual voicing implies a different quality.

Use a simple motion cost as an audit aid:

- common tone: 0;
- semitone: 1;
- whole tone: 2;
- third: 3;
- fourth or larger: 5 or more;
- voice crossing or register reset: add a penalty unless intentional.

Do not minimize every voice mechanically. Strategic leaps create contour and section lift.

## 8. Inner-line design

Choose at least one inner line for a loop or phrase.

Useful designs:

- chromatic descent;
- chromatic ascent;
- scale-degree suspension and resolution;
- static common tone against moving bass;
- contrary motion to top line;
- delayed guide-tone resolution;
- repeating neighbor tone;
- line transferred between hands or instruments.

State which voice carries the line and how it changes on recurrence.

## 9. Attack and release design

Exact voicing includes performance behavior.

Specify:

- simultaneous, rolled, grace-note, or staggered attack;
- attack order for rolled voicings;
- nominal onset and microtiming profile;
- gate length or release point;
- pedal on/off or half-pedal concept;
- whether the bass and upper structure attack together;
- whether repeated voicings fully reattack.

Use silence between syncopated chords when clarity depends on the gap.

## 10. Voicing variation across form

Create at least three states when harmony recurs:

- **core:** defines the piece;
- **reduced:** shell, dyad, or partial upper structure;
- **expanded:** wider register, added color, counterline, or top-note lift.

Optional fourth state:

- **transformed:** reharmonized bass, planed voicing, altered top line, or different instrument.

Do not expand every recurrence. A reduced final statement can be more effective than a larger one.

## 11. Instrument-specific reductions

### Guitar

Reduce to essential guide tones, top note, and one color. Check string and fret feasibility. Do not copy a six-note keyboard voicing blindly.

### Horns

Distribute by range and timbre. Preserve lead clarity, avoid low dense seconds, and check breath and balance.

### Vibraphone

Account for sustain, motor/tremolo, mallet count, and pedal. Use fewer low notes than piano when resonance becomes cloudy.

### Synth or pad

Pitch density may be sparse because spectrum is dense. Specify envelope and register separately from chord symbol.

## 12. Audit

- Are exact pitches and octaves present?
- Is the top line intentional?
- Does the bass clarify or enrich the harmony?
- Do guide tones move coherently?
- Are alterations resolved or retained intentionally?
- Is low-register density controlled?
- Are hand allocation and span playable?
- Are attack and release specified where groove depends on them?
- Does each recurrence have an appropriate voicing state?
- Does the actual voicing match the chord label?

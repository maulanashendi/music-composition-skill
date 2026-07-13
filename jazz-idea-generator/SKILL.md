---
name: jazz-idea-generator
description: Turn a brief, mood, reference feel, or emotional journey into a rich, comparable instrumental composition idea — built around a dramatic arc, with melody phrasing, a memorable hook, tension-and-release design, chord progression, groove, and structure — then lock the winning idea into a machine-readable composition-plan.json. Use whenever someone wants to start a new instrumental jazz, lofi, jazzhop, neo-soul, fusion, or jazz-derived piece from scratch, wants help deciding between musical directions, asks for chord/melody/groove/feel ideas, or describes a mood or feeling they want a track to express. Use even when they don't say "composition" — phrases like "I want a laid-back C minor groove," "a song that goes from doubt to acceptance," "give me some chord ideas," or "help me start a lofi track" should trigger this.
---

# Jazz Idea Generator

Turn a brief into a **locked, concrete musical idea with a felt emotional shape** — captured in `composition-plan.json` — that a downstream notation step can encode without guessing. This skill stops at the plan. It does not write ABC notation or MIDI; those are separate skills.

The core belief: **a chord progression alone loops and feels empty. What gives a piece feeling is a dramatic arc that everything else serves.** This skill designs the arc first, then makes every other decision — melody phrasing, hook, tension, groove — answer to it.

## The one rule that prevents "complete on paper but weird to the ear"

**The dramatic arc is the master. Every other dimension serves it — and you only use a technique when it serves the arc.** Do not stack every available device to prove sophistication. A great arrangement picks the two or three moves that fit the emotional moment and leaves the rest out. If a technique (contrary bass, tight rhythm, silence, register climb) doesn't serve what the section is *feeling*, leave it out. Over-arrangement is how many dimensions turn into noise.

## What "done" looks like

A filled `composition-plan.json` with: a stated dramatic arc, key/tempo/meter/ensemble, bar-by-bar chords per section, a concrete hook, per-section phrasing intent, and a tension-release plan — all coherent with the arc. Prose like "funky, C minor, laid-back" is a starting point, not a plan.

## Workflow

### Step 1 — Lock the brief AND the emotional journey

Instrumental-only; ignore lyrics. Extract the technical basics (purpose, duration, style family, tempo/feel, meter, ensemble, harmonic language, any fixed material the person already committed to — respect fixed material, don't override it).

But the most important input is the **feeling**. Ask, in the person's own terms: *what journey does this piece take? From what feeling, to what feeling?* Examples of an arc: "doubt → hope → peak → acceptance," "calm → longing → warmth → rest," "tension building to release."

If the person only gives a vibe ("chill lofi jazz"), **propose an arc** and confirm it — e.g. "how about: settled → a touch of longing → warm lift → quiet resolution?" A piece needs a journey, or it's just a loop. Don't proceed to candidates until there's an arc, even a simple one.

### Step 2 — Design the dramatic arc as the backbone

Before any chords, map the emotional journey onto sections. For each phase state the feeling, the section it lives in, and what that feeling *requires* musically. This table drives everything after it:

| Phase | Feeling | Section | What it requires |
|---|---|---|---|
| (e.g. doubt) | unsure, searching | Intro / Verse | low-mid register, melody stops on unresolved tones, minimal instruments, laid-back placement |
| (e.g. hope) | opening up | Pre-chorus | rhythm tightens, bass steps up, register creeps up, one instrument enters |
| (e.g. peak) | full, bursting | Chorus | high register, full ensemble, melody reaches and holds its peak note, open harmony |
| (e.g. acceptance) | at rest | Outro | register falls, rhythm loosens, full resolution to tonic, space, widening ambience |

The arc decides how quiet the verse is, how the pre-chorus builds, whether the chorus feels open or bursts, and how it ends.

### Step 3 — Generate comparable candidates (each built on the arc)

Read `references/ideation-theory.md` (grounding vocabulary) and `references/style-cheatsheets.md` (target style). Produce **2–4 materially different candidates** — differing on real structural axes (functional vs. modal, fast vs. slow harmonic rhythm, root-cycle vs. pedal bass, tight loop vs. through-composed). For each candidate give:

1. **the arc realized** — one line on how this candidate expresses the emotional journey;
2. key, tempo, meter;
3. bar-by-bar chord progression (actual symbols);
4. groove/feel and bassline character;
5. **the hook, written concretely** — its rhythm (where it lands), its interval shape/contour, and where it first appears. Not "a catchy motif" — an actual described figure;
6. **melody phrasing intent per section** — long vs. short notes, gaps between phrases, rising/falling contour, the peak note and whether it's held, motif repetition, and whether the line sits on the beat or slightly behind. This is *how the melody is played*, the thing that makes it sing;
7. **tension-and-release plan** — where tension builds and how it releases, choosing only techniques that serve the arc. Options include: a dominant held before the tonic, a melody stopping on an unresolved tone, bass moving contrary to melody, rhythm tightening, instruments being added, register climbing, intensity/volume rising, widening reverb/ambience, a beat of silence before the chorus, broken chords, or deliberate space. **Pick the few that fit each moment — do not use all of them.**

Keep section structure varied — repeats must reorchestrate, reharmonize, thin, or transform, never literal copy-paste.

Detailed voice-leading (how each note inside a chord moves) and the bar-by-bar interaction map (who leads / supports / answers / is silent, per bar) are **production-stage** decisions — they belong to the notation/arrangement skill, not here. At ideation, decide the *feeling and shape*; let production execute the exact voices. This split is deliberate: it keeps ideation from drowning in simultaneous systems that can contradict each other.

### Step 4 — Recommend and select

Say which candidate you'd pick and why, and why the others lose — in terms of how well each *expresses the arc*, plus hook strength, groove fit, and playability. Have an opinion; let the person override.

### Step 5 — Quality gate: does this sound like music or like a checklist?

Before locking, read the whole plan back and judge it by ear, not by completeness:

- Does each section *feel* different from the next, following the arc? If the chorus doesn't feel more open than the verse, fix it.
- Is any technique present that doesn't serve the arc? Remove it — a plan is better with three purposeful moves than ten piled-up ones.
- Does the hook actually stand out, and does the melody phrasing give it room to breathe?
- Would this move a listener, or just tick boxes?

This gate judges coherence and feeling, not how many dimensions are filled. Completeness is not the goal; a felt journey is.

### Step 6 — Lock into composition-plan.json

Fill `assets/composition-plan-template.json` completely, including the `arc`, `hook`, and per-section `phrasing` and `tension` fields. Self-check: chords sum correctly against the meter; key/tempo/meter/ensemble set; the arc is stated and each section's phrasing/tension serves it; one identifiable hook with a varied return; a defined ending. If the person is still exploring, stop at Step 4 and say so rather than forcing a half-empty plan.

### Hand-off

When locked, say the idea is ready to notate and that `abc-notation-writer` takes this `composition-plan.json` as input. Production-stage detail (interaction map, voice-leading) is decided there, guided by the arc this plan defines. Don't write ABC here.

## References

- `references/ideation-theory.md` — compact working vocabulary: rhythm/subdivision, scales & chords, progression logic, harmonic rhythm, melody/motif/hook, **phrasing**, **dramatic arc & tension-release**, harmony feel, structure, arrangement, interaction. Read at Step 3.
- `references/style-cheatsheets.md` — per-style quick reference. Read only the target style's entry.
- `assets/composition-plan-template.json` — the output contract. Copy and fill this.

## Default assumptions

When the brief omits details and the style doesn't imply better: one lead instrument plus keys, bass, and drums; 4/4 at a moderate tempo; 2–4 minutes; a 16–32 bar core form (or a 4-bar loop developed across ~48–64 bars for loop-centered lofi); one clear hook with a fragment, full statement, and varied return; at least one contrast/subtraction moment and a finite ending; and — always — a stated dramatic arc, proposed and confirmed if the person didn't give one. Replace any default the requested style, ensemble, concept, or arc points away from.

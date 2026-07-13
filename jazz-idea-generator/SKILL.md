---
name: jazz-idea-generator
description: Turn a brief, mood, or emotional journey into a locked instrumental composition idea — dramatic arc, hook, chord progression, groove, and phrasing — saved as a machine-readable composition-plan.json. Use to start a new jazz, lofi, jazzhop, neo-soul, or fusion piece, to decide between musical directions, or for chord/melody/groove/feel ideas. Triggers even without the word "composition": "a laid-back C minor groove," "a song that goes from doubt to acceptance," "give me some chord ideas," "help me start a lofi track."
---

# Jazz Idea Generator

Turn a brief into a **locked, concrete musical idea with a felt emotional shape** — captured in `composition-plan.json` — that a downstream notation step can encode without guessing. This skill stops at the plan. It does not write ABC notation or MIDI; those are separate skills.

The core belief: **a chord progression alone loops and feels empty. What gives a piece feeling is a dramatic arc that everything else serves.** This skill designs the arc first, then makes every other decision — melody phrasing, hook, tension, groove — answer to it.

## The one rule that prevents "complete on paper but weird to the ear"

**The dramatic arc is the master. Every other dimension serves it — and you only use a technique when it serves the arc.** Do not stack every available device to prove sophistication. A great arrangement picks the two or three moves that fit the emotional moment and leaves the rest out. If a technique (contrary bass, tight rhythm, silence, register climb) doesn't serve what the section is *feeling*, leave it out. Over-arrangement is how many dimensions turn into noise.

See `../RED-FLAGS.md` for common excuse-vs-reality failure patterns in this domain.

## What "done" looks like

A filled `composition-plan.json` with: a stated dramatic arc, key/tempo/meter/ensemble, bar-by-bar chords per section, a concrete hook, per-section phrasing intent, and a tension-release plan — all coherent with the arc. Prose like "funky, C minor, laid-back" is a starting point, not a plan.

## Workflow

### Step 1 — Lock the brief AND the emotional journey

Instrumental-only; ignore lyrics. Extract the technical basics (purpose, duration, style family, tempo/feel, meter, ensemble, harmonic language, any fixed material the person already committed to — respect fixed material, don't override it).

But the most important input is the **feeling**. Ask, in the person's own terms: *what journey does this piece take? From what feeling, to what feeling?* Examples of an arc: "doubt → hope → peak → acceptance," "calm → longing → warmth → rest," "tension building to release."

If the person only gives a vibe ("chill lofi jazz"), **propose an arc** and confirm it — e.g. "how about: settled → a touch of longing → warm lift → quiet resolution?" A piece needs a journey, or it's just a loop. Don't proceed to candidates until there's an arc, even a simple one.

For a concrete mood-to-parameter mapping (tempo, dynamics, harmonic color, rhythm activity, texture density, register, voice-leading — the same seven dimensions for every mood), see `references/reasoning-theory.md` Module 1. It turns a vibe word into explicit musical decisions before Step 2's table is filled.

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

**Default read — always:** `references/ideation-theory.md` (compact grounding vocabulary) and the one matching entry in `references/style-cheatsheets.md`. That is enough for most briefs. Pull in a deeper reference only when its trigger below is actually met — one file at a time, not all at once:

| Read this | Only when |
|---|---|
| `references/reasoning-theory.md` Module 2 (theory-hierarchy gate), then Module 3's device catalog as needed | before locking a candidate's vocabulary — declare one main theory + supporting harmony/melody/texture/groove; it constrains which devices are usable without extra justification |
| `references/neo-soul-genre.md` | the target style is neo-soul / chill-jazz (musical DNA, roles, arrangement architecture for that family) |
| `references/form-and-dramaturgy.md` | a bar-count or formal-family decision needs more depth than `ideation-theory.md` §7 gives |
| `references/loop-development.md` | the form is loop-centered (lofi, jazzhop, groove-first) |

Produce **2–4 materially different candidates** — differing on real structural axes (functional vs. modal, fast vs. slow harmonic rhythm, root-cycle vs. pedal bass, tight loop vs. through-composed). For each candidate give:

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

For a more structured pass before the ear-judgment below, run the winning candidate through `references/reasoning-theory.md` Module 4 (compatibility matrix, one leader per section, one idea per dimension per section) and Module 6 (a tension/release map — planned vs. realized per section). If a fix is needed, Module 5 (macro/meso/micro levels) keeps you revising at the right altitude — one odd voicing is a micro fix, not a reason to rebuild the form. These catch "correct in theory but flat or cluttered" issues that a read-through alone can miss.

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

Read the default core; pull a deep file only when its trigger is met (see Step 3's table).

| File | Read when | Canonical for |
|---|---|---|
| `references/ideation-theory.md` | **default, every brief** (Step 3) | the compact working vocabulary — and the **dramatic arc & tension-release** (§4b–4c), the home other files point back to |
| `references/style-cheatsheets.md` | **default** — only the target style's entry | per-style quick reference |
| `references/reasoning-theory.md` | by module: Module 1 at Step 2, Module 2 (+3) at Step 3, Modules 4 & 6 at Step 5, Module 7 downstream | mood→parameter, theory-hierarchy gate + device catalog, compatibility/leadership/tension evaluation, verification |
| `references/neo-soul-genre.md` | style is neo-soul / chill-jazz (Step 3) | that genre's DNA and architecture; defers to `groove-profiles.md` / `interaction-map.md` for pocket & roles |
| `references/form-and-dramaturgy.md` | a form/bar-count call needs more than `ideation-theory.md` §7 | deeper form mechanics (formal families, cadence, solo/intro/ending) |
| `references/loop-development.md` | the form is loop-centered | loop DNA, mutation classes, development timescales |
| `assets/composition-plan-template.json` | Step 6 | the output contract — copy and fill |

## Default assumptions

When the brief omits details and the style doesn't imply better: one lead instrument plus keys, bass, and drums; 4/4 at a moderate tempo; 2–4 minutes; a 16–32 bar core form (or a 4-bar loop developed across ~48–64 bars for loop-centered lofi); one clear hook with a fragment, full statement, and varied return; at least one contrast/subtraction moment and a finite ending; and — always — a stated dramatic arc, proposed and confirmed if the person didn't give one. Replace any default the requested style, ensemble, concept, or arc points away from.

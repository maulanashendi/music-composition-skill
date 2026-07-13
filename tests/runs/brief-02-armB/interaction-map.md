# Interaction map — "Riptide"

Per `abc-to-midi-orchestration/references/interaction-map.md`: for each
section, is each instrument **lead / support / answer / silent**? This map
traces to the actual bars realized in `song.abc` + `drums.json` (verified
against the real note data in `song.mid`, not an aspirational document
written separately from what was encoded).

| Bars | Section | Feeling | Lead Sax | Rhodes | Bass | Drums | Event |
|---|---|---|---|---|---|---|---|
| 1-2 | Intro | restless/unsettled | lead (bare fragment: pickup into a held F4, bar 1) then silent (bar 2) | silent | support (sparse root pedal, D2 held then space) | near-silent (a single soft rimshot on the downbeat only) | the hook's first, bare appearance; three of four voices are silent at any given instant |
| 3-6 | A1 | restless/unsettled | lead (states the complete hook bar 3, answers/descends bar 4, restates the fragment bar 5, holds a suspended tone into silence bar 6) | support, entering here for the first time (one comping stab/bar) -- **answers** in bar 6 specifically: silent while the lead holds its G4, then plays into the exact 3 units the lead leaves empty | support (same sparse pedal pattern as the Intro, restated -- A1 reads as "more of the same idea," not a new one) | support (kick+hat groove enters; a pickup snare hit on the last eighth of bar 6 leads into A2) | keys' entrance is the section's one "instrument added" build device; bar 6 is the piece's clearest call-and-response moment |
| 7-10 | A2 | building urgency | lead (hook sequenced up a step, climbs to a temporary ceiling Bb5/C6, reaches and stops) | support, thickening (two stabs/bar instead of one) | support, now "stepping up" (stepwise ascending motion replaces the pedal, per the arc's "bass steps up" requirement) | support, building (kick fills all three group-downbeats, snare backbeat enters on the 3-group) -- bar 10 pulls back to a bare kick + sparse hat, mirroring the melody/bass's reach-and-rest | one of very few sections where three voices (lead, bass, drums) all move upward/denser together -- deliberate, since A2's whole job is "building" |
| 11 | B (push) | building urgency, hardest push | lead (busiest rhythm of the piece: a 6-note descending run, all single eighths) | support, deliberately **simplified to one sustained chord for the whole bar** -- a compatibility-matrix call: lead and bass are both maximally active here, so keys steps back rather than adding a third busy layer | **co-foregrounded with the lead** (a full 7-note chromatic walk-up, contrary to the lead's descent) -- see note below on this being a disclosed exception to "one leader per section" | support, at its busiest (kick on every group-downbeat, syncopated snare, driving hats) | the single densest bar of the piece: rhythm tightening + contrary motion stacked together, deliberately, once |
| 12-13 | B (hold) | building urgency, dominant prolongation | lead (holds the altered b9 tone, bar 12; a chromatic inner move previews the D-major arrival a bar early, bar 13) | support (one held stab in bar 12, matching the lead's held-then-rest shape; **silent** in bar 13, stepping back again so the lead's chromatic anticipation is the one active idea) | support, deliberately simple (a plain pedal on A, letting the lead carry all the harmonic motion here -- another compatibility-matrix call) | support, still driving through bar 13 | the dominant (A7b9) is held across two full bars -- a single prolonged tension device, not restated per-bar |
| 14 | B (breath) | the subtraction moment | silent | silent | support, alone (one long pedal tone, the only sound) | **silent** (an empty pattern -- total drum drop-out) | the "beat of silence right before a big section," realized as an entire bar, with only the bass pedal remaining -- everything else genuinely stops |
| 15-18 | C (climax) | triumphant/released | **lead**, tutti entrance: the hook returns as a register-leap (bar 15, D6 into a held F#6 -- the single highest, most exposed note of the piece), then a still-bright descent (16-18) | support, full tutti block chords (all four-note voicings, several held for the full bar) | support, full driving riff-lock (root-based tutti hits, then arpeggiated triad motion) | support, full tutti (kick+snare hit together on the downbeat/3-group landing points; hats **and** ride both driving, "ride opens it up") | the one true tutti event of the piece -- reserved for exactly this arrival, per interaction-map.md's own advice not to overuse it |
| 19-20 | Outro | confident landing (not a fade) | lead (a short descending tag, touching F#6 once more without exceeding the climax's peak, then a single held final D6 for the whole last bar) | support (sustained chords, no new material) | support (a final pedal-then-root gesture, held under the last chord) | support/tag (a confident hit on bar 19, then one clean stinger on bar 20 -- deliberately not a fade or ritard) | ends decisively, matching the brief's "triumphant... near the end" rather than a slow cool-down |

## The one disclosed exception to "one leader per section" (bar 11)

`reasoning-theory.md` Module 4 (Lens 2) calls for exactly one leader per
section. Bar 11 genuinely has **two** simultaneously foregrounded voices --
the lead's fast descending run and the bass's full chromatic walk-up moving
contrary to it -- while keys deliberately steps back to a single sustained
chord specifically *because* two voices are already busy (the
compatibility-matrix check that *did* get applied: "don't add a third busy
layer when two are already active"). This is disclosed rather than smoothed
over: it is a considered exception (contrary motion is a single coordinated
tension gesture, not two competing ideas fighting for the same musical
role), but it is still a real departure from the strict one-leader rule, and
is reflected in the "Interaction" rubric score in `quality-report.md` rather
than scored as if it weren't there.

## Reading the map against the arc

- **Restless/unsettled (Intro-A1, bars 1-6):** at most two voices active at
  once; keys is entirely absent until bar 3 (an "instrument added" build
  device); the section's one call-and-response moment (bar 6) is deliberately
  small-scale, matching a still-restless, still-quiet phase.
- **Building urgency (A2-B, bars 7-14):** density and register climb through
  A2, peak in bar 11 (the disclosed two-leader exception), then the harmonic
  tension is held (12-13) and finally subtracted to near-nothing (14) --
  every technique in this arc phase points at the same arrival.
- **Triumphant/released (C, bars 15-18):** the only tutti of the piece,
  reserved for exactly this moment; the hook's transformed return (register
  leap + parallel major) is the clearest "development, not repetition" event
  in the whole piece.
- **Confident landing (Outro, bars 19-20):** subtraction continues (no new
  voices, no new material) but the piece stops on a decisive held chord
  rather than fading, per the brief's explicit request for the triumphant
  release to land "near the end," not dissolve afterward.

## Quality-gate check (per `interaction-map.md`'s own checklist)

- **Does each section's density match its arc phase?** Yes, verified by ear
  of the written arrangement and by the drum-hit/note counts themselves:
  Intro/A1 are the sparsest (2-3 active elements at most), B builds to the
  densest single bar (11) then empties to total silence (14), C is the
  piece's only full tutti.
- **Is any instrument active only to fill space, not to serve the moment?**
  No instance found on review -- every "support" entry above ties to a
  specific function (pedal, comping, groove, or an explicit answer/step-back
  decision); bars 13 and 14 specifically have keys/drums *removed* rather
  than padded in to avoid looking sparse.
- **Is there at least one subtraction and one call-response?** Yes on both:
  bar 6 (keys answers the lead's rest) is the call-response; bar 14 (total
  ensemble drop to a lone bass pedal) is the subtraction, and the whole
  Outro continues subtracting rather than adding.
- **Would a listener feel the journey?** Per `reasoning-theory.md` Module 7
  ("what the agent cannot do"), this is a human, ear-first judgment this
  document cannot certify for itself -- it documents that the arrangement is
  *built* to make the journey audible (density, register, and harmonic
  tension all point the same direction at every arc phase), not that it has
  been confirmed to land emotionally.

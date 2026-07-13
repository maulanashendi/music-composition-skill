# Comprehensive quality control

> Adapted from `jazz-composition-designer` (archived portable skill package,
> consolidated 2026-07-13). This package's validator surface is narrower than
> the one this checklist was written against: only
> `abc-notation-writer/scripts/validate_abc.py` exists here (§15 below,
> "ABC and notation"). Where this file says "Run `scripts/validate_blueprint.py`"
> (§14, composition plan), there is no such script in this package — check
> the checklist items manually against `jazz-idea-generator/assets/composition-plan-template.json`
> and disclose that validation was manual, exactly as this file's own
> fallback instruction says. Where it says "Run `scripts/validate_daw_plan.py`"
> (§14, DAW plan), the equivalent here is the manual sync/mono/no-drone check
> in `references/midi-conversion.md` against `assets/drum-grid-template.json`
> — again, disclose as manual. Treat every other item in this checklist
> (form, transitions, groove, harmony, voicing, melody, loop development,
> interaction, style specificity, the scoring rubric) as directly applicable.

Run this audit before final delivery. Do not pass a composition because the chord symbols, plugin notes, or rhythmic offsets look sophisticated.

## 1. Brief, identity, and ethics

- User facts and assumptions are separated.
- Mood, style, groove, form, instrumentation, performance practice, and production are not conflated.
- Development level and output path are explicit.
- Primary and secondary engines match the brief.
- Fixed DNA, flexible parameters, protected arrivals, forbidden shortcuts, and return signal are stated.
- Reference material is translated into broad attributes rather than copied.
- No copyrighted sample, recognizable melody, or living artist's distinctive style is reproduced.

## 2. Candidate selection

- At least two materially different concepts were considered for a full composition unless the user locked the design.
- Differences are structural, not only chord extensions or instrumentation.
- Selection criteria are explicit.
- Rejected alternatives lose on specific brief-related criteria.
- Hard failures such as range, form, clave, output-path mismatch, or unplayable voicing override numeric scores.

## 3. Development and anti-boredom

- Identity remains recognizable after transformation.
- Development occurs at appropriate micro, meso, and macro scales.
- Repetition communicates groove, memory, insistence, ritual, or formal return.
- A complete loop is not repeated three times literally without a reason.
- At least one subtraction event is present in Level 3-5 work unless the concept is continuous accumulation.
- The third recurrence develops function, not only surface color.
- At least one technique or textural state is reserved for the later form.
- The climax is prepared and has a consequence.
- The ending resolves, transforms, or deliberately suspends the identity.

## 4. Form and section function

- Every section has an exact bar count or explicit duration/cue rule.
- Total bars and estimated duration agree.
- Every section has a listener-facing function.
- Recurrences are labeled literal, micro-varied, reorchestrated, reharmonized, reframed, fragmented, expanded, compressed, or transformed.
- Written form, performance order, loop clips, head in/out, and solo choruses are distinguished.
- Repeats, endings, and open sections are unambiguous.
- Hook, verse, chorus, bridge, interlude, tag, coda, and outro labels match audible function.

## 5. Instrumental transitions

Audit every section boundary against the full criteria in `instrumental-transitions.md` (families, duration proportional to the change, setup/threshold/arrival/aftercare, handoffs). Blocking gates: at least one element is preserved across each boundary unless rupture is intentional; different transition families are used across the piece (fills/crashes/risers are not the default at every seam).

## 6. Meter, tempo, groove, and microtiming

Audit against `groove-meter.md` (meter/subdivision/feel) and, for pocket, `groove-profiles.md` (the numeric table) with `advanced-microtiming.md` (the principles). Blocking gates: bass, drums, comping, and melody agree on the groove framework; the notated rhythm works before microtiming is added; timing offsets are relational and bounded (a named profile, not per-note invention); random humanization is not a substitute for groove design.

## 7. Harmony

- Chords are correctly spelled.
- Roman numerals are used only where meaningful.
- Local centers or nonfunctional processes are identified.
- Non-diatonic events have functional, modal, voice-leading, bass, color, or formal rationale.
- Dominant alterations fit melody and destination.
- Pedals, planing, polychords, symmetric cycles, and common-tone networks are audible as designed.
- Harmonic rhythm fits tempo and groove.
- Removing a decorative chord would not improve clarity.

## 8. Bass and exact voicing

Audit against `exact-voicing.md` (voicing families, register zones, voice-leading, attack/gate) when the brief needs exact pitches. Blocking gates: the actual voicing matches the chord label; MIDI values agree with pitch names in DAW-first output; register and hand/instrument allocation are playable and low-register density is controlled.

## 9. Melody, hook, and thematic development

- One primary motif and at most one necessary contrasting motif organize the piece.
- Rhythm and interval identity remain recognizable after transformation.
- Phrase lengths, breath, silence, and target notes are perceptible.
- Long, repeated, accented, and phrase-ending notes fit or intentionally challenge harmony.
- Range and tessitura suit the lead instrument.
- Fragment, complete, and transformed-return states are defined for hook-centered work.
- The climax is not weakened by repeated earlier high points.
- The head remains memorable after removing decorative notes.

## 10. Loop development

- Loop DNA and seam are intentional.
- Protected features are stated.
- Reduced, core, expanded, contrast, return, and outro states are defined as appropriate.
- Every eight- to sixteen-bar recurrence changes listener perception when the style requires development.
- Harmony is not the only source of variation.
- Bass, drums, voicing, melody, register, density, timbre, and silence share developmental work.
- Contrast preserves at least one invariant.
- Return contains new information.
- Outro removes, transforms, or completes the loop mechanism.

## 11. Improvisation

- Form, landmarks, and cue points are clear.
- Targets and guide tones are more specific than scale labels.
- Optional pitch resources do not replace phrase strategy.
- Outside material has a return path.
- Modal or static sections include motif, rhythm, register, and density development.
- Successive choruses or states change.
- Solo entry and return are arranged.
- The solo belongs to the composition through identity material, groove, voicing field, or cue.

## 12. Ensemble interaction and arrangement

Audit against `interaction-map.md` (roles, subtraction, density that tracks the arc) and `ensemble-interaction.md` for deeper conventions. Blocking gates: every instrument/track has a meaningful primary role and accompaniment leaves space (no range conflict); density curves are planned to serve the arc, not to keep everyone busy; a lead sheet is not falsely presented as a complete score.

## 13. Production and DAW-first design

- The dry composition works before noise, filtering, and degradation.
- Track roles are distinct.
- Exact event data are supplied for critical motifs, bass, voicings, and groove classes.
- Automation has a musical purpose.
- Production state changes reinforce form.
- Sample-like material is original.
- Layer addition and subtraction are balanced.
- Production effects do not conceal an unprepared section change.
- Fade, edit, reverse audio, or automation-dependent events have live alternatives.
- Hybrid plans specify click, cue ownership, flexible bars, recovery, and stage ending.

## 14. Machine-readable plans

### Composition plan

- Section labels are unique.
- Bar numbers and chord-duration totals are valid.
- Open sections are labeled explicitly.
- Performance order and solo form reference existing sections.
- The plan matches prose and notation.

Run `scripts/validate_blueprint.py`; when script execution is unavailable, verify the checklist above manually and disclose that validation was manual.

### DAW plan

- Track IDs, section labels, loop states, and references are valid.
- Sections fit within total length.
- Pitch names and MIDI values agree.
- Velocity, offset, and gate values are in range.
- Groove profiles identify a reference track.
- Transitions include source, target, setup, threshold, arrival, aftercare, and live alternative.
- Arrangement timeline and automation fit the composition length.
- Ending cue and final identity state are explicit.

Run `scripts/validate_daw_plan.py`; when script execution is unavailable, verify the checklist above manually and disclose that validation was manual.

Any structural error is a blocking failure.

## 15. ABC and notation

- Required headers exist and are parseable.
- Note spelling matches key and function where practical.
- Chord symbols align with intended onsets.
- Bar durations, pickups, tuplets, rests, ties, overlays, repeats, and endings validate.
- Each voice remains metrically consistent.
- Swing and production directions are not falsely encoded as incorrect note values.
- Improvised material is not frozen unless requested.
- Renderer-specific limitations are disclosed.

Run `scripts/validate_abc.py`; when script execution is unavailable, verify the checklist above manually and disclose that validation was manual.

## 16. Style specificity and cultural responsibility

- Style uses more than superficial markers.
- Lofi is not reduced to vinyl noise and maj7 chords.
- Jazz-funk is not treated as identical to hip-hop.
- Smooth jazz is not defined only by saxophone and slow tempo.
- Bossa, samba, clave, and named traditions use specific frameworks or are honestly labeled broad influences.
- Free music is governed by audible constraints rather than randomness.
- Hybridization identifies the role of each source vocabulary.

## 17. Scoring rubric

Score each domain from 0 to 4:

- 0: absent or contradictory;
- 1: major failure;
- 2: usable with substantial revision;
- 3: strong with minor revision;
- 4: excellent and internally consistent.

Domains:

1. brief fit and ethics;
2. identity and development;
3. form;
4. transitions;
5. groove and microtiming;
6. harmony;
7. bass and exact voicing;
8. melody and hook;
9. loop development;
10. improvisation;
11. interaction;
12. arrangement and orchestration;
13. production and DAW design;
14. notation and data validation;
15. originality and cultural responsibility;
16. style specificity.

A full composition should not be delivered with any domain below 2. A structural validator error, originality concern, or cultural concern is blocking until repaired.

## 18. Final validation report template

- Composition-plan validation: PASS / PASS WITH WARNINGS / NOT REQUIRED / FAIL.
- DAW-plan validation: PASS / PASS WITH WARNINGS / NOT REQUIRED / FAIL.
- ABC validation: PASS / PASS WITH WARNINGS / NOT REQUIRED / FAIL.
- Musical audit: [score]/64.
- Blocking issues repaired:
- Development risks reviewed:
- Remaining interpretive choices:
- Live-performance alternatives:
- Renderer or format limitations:

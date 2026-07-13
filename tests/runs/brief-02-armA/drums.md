# Drum pattern — "Restless Seven"

7/8, felt as eighth-note groupings that *change* across the form (that shift
is the main device used to paint "restless/unsettled" vs "triumphant/released").
Tempo: eighth note = 160 bpm (bar = 2.625s at that tempo). GM drum note numbers
in parentheses.

Groupings used:
- **2+2+3** (slots 1-2 | 3-4 | 5-6-7) — the "settled" feel, used in the intro,
  the A theme, and the climax.
- **3+2+2** (slots 1-2-3 | 4-5 | 6-7) — the "displaced" feel, used only in the
  B/development section, so the groove itself feels like it's been knocked
  off balance — restless by construction, not just by faster drums.

Slot numbers below are eighth-note positions 1..7 within the bar.

## Section 1 — Intro (bars 1-4), grouping 2+2+3

- Kick (36): slots 1, 3, 5
- Snare (38): slot 6 only (sparse — leaves room to build)
- Hi-hat closed (42): every slot 1-7, straight eighths, driving
- Crash (49): bar 1 / slot 1 only, to mark the downbeat of the whole piece

## Section 2 — A theme (bars 5-10), grouping 2+2+3

- Kick (36): slots 1, 3, 5
- Snare (38): ghost on slot 2 (vel ~50), accent on slot 6 (vel ~100)
- Hi-hat closed (42): every slot, slight accent on 1/3/5
- No crash — energy is building, kept contained

## Section 3 — B / development (bars 11-16), grouping 3+2+2 ("the groove trips")

- Kick (36): slots 1, 4, 6
- Snare (38): ghost on slot 3, accent on slot 7 (the accent lands on the
  "wrong" side of the bar relative to section 1/2 — deliberately unsettling)
- Hi-hat: closed (42) on slots 1,2,3,5,6; **open** (46) on slots 4 and 7 for
  extra friction/texture
- Bar 16 only (last bar before the climax): drop the hi-hat pattern for a
  2-beat tom fill on the last group — high tom (50) slot 5, mid tom (47)
  slot 6, low tom (45) slot 7 — kick stays on 1 and 4 as an anchor, snare
  is silent so the toms read clearly. This is the pickup into the climax.

## Section 4 — Climax (bars 17-20), grouping back to steady 2+2+3

- Kick (36): slots 1, 3, 5
- Snare (38): slot 1 (together with the crash, big hit) and slot 6 (backbeat)
- Ride (51) replaces the hi-hat for the whole section — opened-up, sustained
  cymbal wash instead of the tight hi-hat pulse = the "release"
- Crash (49): bar 17 / slot 1 (arrival) and bar 20 / slot 1 (final hit)
- Bar 20 (final bar) is a deliberate exception to the rest of the section:
  kick + snare + crash land together on slot 1 only, then the ride simply
  rings through slots 2-7 with nothing else added underneath, so the piece
  ends on a sustained cymbal wash rather than more busy hits.

This pattern is realized programmatically (not hand-sequenced note by note)
in `make_midi.py`, from the exact per-bar event table above, so the drum
MIDI track matches this description exactly. See that script for the literal
event list if useful.

## Honest caveats

- This is a reasonable, idiomatic-sounding fusion drum pattern for a demo,
  but it was designed "on paper" by ear/theory, not iteratively auditioned —
  I did not render and listen back before finalizing it (no fast feedback
  loop for that available in this environment).
- Ghost-note/open-hihat velocities are my own defaults (50/70/100 roughly for
  ghost/normal/accent) — reasonable but arbitrary; a real drummer or a mix
  pass would likely retune these.

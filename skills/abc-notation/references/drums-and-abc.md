# Drums and ABC — keep them separate

## Why drums don't belong in ABC

ABC notation assumes each letter (C, D, E…) is a **pitch** in a key. Drums have no key — each drum is a fixed physical instrument in the General MIDI percussion map on MIDI channel 10 (e.g. kick=36, snare=38, rimshot=37, closed hi-hat=42, ride=51). Forcing drums into ABC via the `%%MIDI drummap` + channel-10 hack is technically possible but fragile: the syntax is fiddly, LLMs write it inconsistently, and music21's percussion support is weak. For lofi and jazz — where the groove *is* the foundation — that fragility is exactly where you don't want it.

## The split

Keep the **pitched** voices (lead, keys, bass, pads) in ABC. Handle **drums** as a separate symbolic layer, then merge at the MIDI/DAW stage. Two viable drum representations:

- **Program directly in the DAW** (e.g. BandLab's native drum machine) — simplest when the person is already arranging there. Recommended when the ABC voices will be imported as MIDI and drums added by hand.
- **Step-grid** — a text grid the downstream converter turns into channel-10 MIDI. LLMs generate grids far more reliably than fake drum notation, and swing/humanization apply cleanly at the grid level.

Example step-grid format (one row per drum, `x` = hit):

```json
{
  "bars": 4,
  "steps_per_bar": 16,
  "swing": 0.58,
  "tracks": {
    "kick":  "x-------x---x---|x-------x---x---|...",
    "snare": "----x-------x---|----x-------x---|...",
    "hihat": "x-x-x-x-x-x-x-x-|x-x-x-x-x-x-x-x-|...",
    "ride":  "x---x---x---x---|..."
  }
}
```

Downstream, each `x` becomes a note-on at its GM number with humanized velocity (±10–15 for lofi feel), and swing is applied by nudging off-beat (even) steps back a few ticks.

## What to do in this skill

Write the pitched voices as ABC and validate them. For drums, do **not** put them in the ABC file. Instead, state explicitly in the output that drums are handled separately, and either hand off a step-grid (if the plan specifies a drum pattern) or note that drums should be programmed in the DAW. The point is that the drum layer is never silently dropped — the person always knows it lives outside the ABC and where it will be added. Building the grid→MIDI converter and the actual merge is downstream (the ABC→MIDI/orchestration step), not this skill.

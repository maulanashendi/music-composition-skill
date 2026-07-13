# MIDI conversion: how it works and the mandatory fixes

Two scripts turn a validated ABC file and a drum grid into a DAW-ready multi-track MIDI. Both fixes below were discovered by actually importing output into BandLab — they are not optional; skipping them produces broken or unusable MIDI.

## The two mandatory fixes

### Fix 1 — Strip chord symbols before rendering (or the arrangement drones)

ABC chord symbols in quotes (`"Cm9"`, `"G7alt"`) are meant as **harmony labels**, not notes to play. But music21 will render them as actual chord notes — a full stack of pitches with long duration — layered onto *every* voice. The result is a smeared drone that sounds awful and buries the melody.

`abc_to_midi.py` strips these before parsing: it removes quoted chord symbols from each voice line, and also removes any `ChordSymbol` objects music21 still produces. **Never render raw ABC to MIDI without this step.** If a rendered lead track has notes lasting many seconds when the melody should be short, the strip was skipped.

### Fix 2 — Force the lead voice monophonic

A melody (sax, lead) should be one note at a time. If a chord slips through on a lead voice, the converter keeps only the top note per attack time, restoring a clean single-line melody. Non-lead voices (keys, pad) keep their polyphony — they're supposed to play chords.

## How the pitched converter works

`abc_to_midi.py <file.abc> <out.mid>`:

1. Splits the ABC into per-voice stubs (each `V:` header + its `[V:id]` body lines), so voices don't leak into each other.
2. Strips chord symbols (Fix 1) from each stub.
3. Parses each stub with music21 and exports it to a temporary MIDI.
4. Reads each back with pretty_midi, assigns a GM program from the voice's `name`, applies mono-lead (Fix 2) where the name looks like a lead, and appends it as its own track.
5. Writes one multi-track MIDI.

GM program mapping (by keyword in the voice name): sax→65, horns→61, rhodes→4, piano→0, bass/upright→33/32, strings/pad→48/89, guitar→27. Extend the map in the script for other instruments.

## How the drum converter works

`grid_to_midi.py <grid.json> <out.mid>`:

- Reads a step-grid (rows = drums, `x` = hit) and writes GM percussion on channel 10 (`is_drum=True`).
- **Swing**: off-beat (odd-index) 16th steps are nudged later by `(swing - 0.5)` of a step, giving the laid-back feel. 0.5 = straight; ~0.56–0.58 = typical lofi/funk swing.
- **Humanization**: each hit's velocity varies by ±`humanize_velocity` around the drum's base velocity, for a natural, non-machine feel.
- GM map and base velocities are set in the grid JSON, so you can tune the kit per song.

## Merging and verifying

Merge by appending the drum track to the pitched PrettyMIDI object and writing once:

```python
import pretty_midi
p = pretty_midi.PrettyMIDI('pitched.mid')
d = pretty_midi.PrettyMIDI('drums.mid')
for tr in d.instruments:
    p.instruments.append(tr)
p.write('final.mid')
```

Then run these checks before delivering:

- **Sync**: every track's `get_end_time()` should be roughly equal. A gap of more than about one bar's worth of time usually means the drum grid and ABC have different bar counts — rebuild the grid to match the ABC's sections. A small gap (a few seconds) is normal when the final chord or bass note is tied and left ringing while drums stop; that's an intentional tail, not a sync error. Confirm bar counts match rather than trusting the raw end-time alone.
- **Mono lead**: the lead track's maximum simultaneous notes should be 1. More than that means Fix 2 didn't apply (check the voice name contains a lead keyword).
- **No drone**: the lead track's longest note should be reasonable (well under a section's length). A multi-second lead note means Fix 1 was skipped.

Optional detache: shortening lead note gates to ~85–88% of their length gives a more articulate, less sustained feel — helpful for sax/horn leads that otherwise sound like they're holding forever.

# pyengine — Kontrak Skema JSON Composition Plan

## Top-level
`{schemaVersion: 2, meta: {title, vibe, key, seed}, grooves?: {...}, sections: [...]}`

## Roles
bass, chords, drums, guitar, lead, pad

## Artikulasi (`artic`)
- `legato`: velocity x1.0, length x1.0
- `staccato`: velocity x1.0, length x0.45
- `tenuto`: velocity x1.04, length x1.0
- `accent`: velocity x1.22, length x1.0
- `ghost`: velocity x0.35, length x0.8

## Comping (`voices.<name>.style` + `.density`)
style: arpeggiated, block, rootless, shell · density: busy, medium, sparse

## Vibe presets
- `neo-soul`: tempo 70-95 bpm, swing 0.55-0.62, mode ['dorian', 'minor', 'mixolydian'], groove default `neo-soul-core`
- `ballad`: tempo 55-75 bpm, swing 0.5-0.55, mode ['major', 'minor'], groove default `neo-soul-core`
- `medium-swing`: tempo 100-132 bpm, swing 0.62-0.68, mode ['dorian', 'major', 'mixolydian'], groove default `neo-soul-core`

## Groove library tersedia
`neo-soul-core`

## Drum pattern library
`neo-soul-basic`, `ballad-brush`

## Degree chord-tone (melody/bass)
degree valid: [1, 3, 5, 7, 9, 11, 13] (index posisi dlm stack root-3-5-7-9-11-13 realisasi chord)

## Simbol chord kualitas major-9/11/13
`<Root>maj9`, `<Root>maj11`, `<Root>maj13` (mis. `Cmaj9`, `Fmaj11`) DIDUKUNG -- dinormalisasi otomatis ke kapitalisasi music21 (`Maj9`/`Maj11`/`Maj13`), pitch identik. Bentuk `<Root>M9`/`<Root>M11`/`<Root>M13` (mis. `CM9`) juga diterima langsung.
Override simbol eksplisit lain (ambigu/gagal music21): Dm9, G13(b9).

## Batas ukuran plan.json (LIMITS, ditegakkan validator)
- `maxSections`: 32
- `maxTotalBars`: 512
- `maxVoicesPerSection`: 12
- `maxNotesPerVoice`: 4096
- `maxHarmonyPerSection`: 512
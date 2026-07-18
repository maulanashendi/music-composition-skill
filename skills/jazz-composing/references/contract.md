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
- `ghost`: velocity x0.5, length x0.8

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

## Beat desimal & pickup (push/antisipasi)
`beat` boleh desimal (mis. `2.5`, `4.5`), bukan cuma bilangan bulat. Aturan deteksi pickup (persis `pipeline.py` `_is_pickup`): sebuah not dianggap **pickup** kalau `beat` OFF-beat (bukan bilangan bulat) DAN `dur < 1`. Not pickup dimainkan groove engine sedikit MENDAHULUI beat nominal (tick offset negatif) -- inilah mekanisme push/antisipasi khas neo-soul. Cara idiomatis 'mencuri start' menuju chord/bar berikutnya: tulis not pendek (`dur` < 1 beat) di `beat: 4.5`.

## Field `pitch` vs `degree` (semua role ber-notes)
Role ber-notes: bass, guitar, lead, pad. `pitch` (nama nota bebas, mis. `"F#2"`) berlaku utk SEMUA role di atas -- bukan cuma `lead` -- dan cocok utk approach tone kromatik yang bukan chord tone. `degree` HANYA menghasilkan chord tone (posisi dlm stack root-3-5-7-9-11-13, lihat `DEGREE_INDEX`). Termasuk `bass`: approach tone kromatik ke root berikutnya ditulis via `pitch`, bukan `degree`.

## Register & oktaf per instrumen
| instrument | rentang MIDI | rentang nota |
|---|---|---|
| `rhodes` | 48-84 | C3-C6 |
| `upright-bass` | 28-55 | E1-G3 |
| `alto-sax` | 55-82 | G3-A#5 |
| `acoustic-guitar` | 52-88 | E3-E6 |
| `pad-strings` | 48-84 | C3-C6 |

**Peringatan:** tanpa field `octave` eksplisit, oktaf default engine utk `bass` bisa mendarat terlalu tinggi (kasus nyata: `upright-bass` jatuh di C4-Bb4, jauh di atas register bass yang wajar). Plan SEBAIKNYA selalu menulis `octave` eksplisit utk voice `bass` -- root nyaman `upright-bass`: oktaf **2**, sesekali **3** utk not tinggi/approach tone.

## Artikulasi berlaku di semua role ber-notes (termasuk bass)
`artic` bukan cuma milik `lead` -- berlaku sama di `bass`, `chords`/`pad`/`guitar` mana pun yang bertipe notes. Catatan `ghost`: efeknya 'dirasakan, bukan didengar' (velocity multiplier 0.5). Hindari menumpuk `artic: ghost` dengan not pickup di section ber-`dynamics` sangat rendah (intro/outro pelan) kalau ingin not itu masih terdengar -- atenuasi pickup groove x dynamics section x ghost bisa menumpuk sampai di bawah ambang berguna sampel.

## Apa yang groove engine tambahkan otomatis (jangan ditulis manual)
Groove default `neo-soul-core` (swing ratio 0.58) menambah humanization berikut secara OTOMATIS di atas plan -- LLM komposer cukup menulis NIAT ritmis (beat, dur, artic), JANGAN mencoba menulis micro-timing manual (tick offset, jitter) sendiri:
- **bass/lead**: laid-back di target beat (offset positif kecil) + pickup dimainkan mendahului beat (offset negatif) utk not off-beat berdurasi pendek (lihat section pickup di atas).
- **chords**: roll antar-voice (step 0.0010 beat/voice, maks 6 voice) + late attack (offset positif) -- voicing tak pernah nge-hit persis serentak.
- **snare**: behind-the-beat (offset positif thd nominal), khas feel neo-soul/laid-back.
- **hi-hat**: swing bertingkat per posisi grid (quarter/offbeat-8th/sixteenth beda offset & velocity scale), bukan flat 8th/16th mekanis.
- **ensemble drift**: seluruh voice hanyut bersama antar not (maks 0.0300 beat, step 0.0088 beat/not) -- simulasi band manusia yang tak pernah 100% presisi metronom.
- **velocity humanization**: jitter acak (amplitudo 0.08) + skala dynamics per section (`dynamics.start/end`, lantai 0.6 + rentang 0.4 di atasnya).

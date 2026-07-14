# 14 — Detail Low Level / Review (Level 14, Tahap 15)

## Revisi low-level yang diperiksa

- **Voice leading**: dicek di `07-comping.md` (top note bergerak
  stepwise antar-shell voicing berurutan; tidak ada lompatan besar).
- **Interval**: hook memakai minor third naik + step turun (lihat
  `04-melody.abc`); interval besar dibatasi ke sekuens B (naik sepertiga),
  tidak dipakai berlebihan.
- **Phrasing**: frase 2-bar terpisah rest di A1 (space eksplisit,
  konsisten dengan "laid-back").
- **Density**: diverifikasi menurun/naik sesuai arc di `13-dynamics.md`
  (sparse→medium→medium-lift→sparse).
- **Voicing**: rootless-shell dipakai konsisten, tidak ada block chord
  penuh/dobel yang bikin padat (dicek `07-comping.md`).
- **Bass line**: kontur + approach note dicek di `08-bassline.md`.
- **Drum setup**: bar count grid dicek sama persis dengan ABC (24 bar,
  2+2+7+1+4+6+1+1 = 24) — lihat `09-drums.json` vs `song.abc`.
- **Articulation**: laid-back/behind-the-beat lewat `%%pocket
  neo-soul-core`, bukan ditulis manual per-not di ABC (sesuai doktrin
  midi-orchestration §Step 4).

## L1 mekanis — hasil aktual (dijalankan, bukan diasumsikan)

Validator:

```
$ python3 skills/abc-notation/scripts/validate_abc.py runs/2026-07-14-doubt-to-acceptance/song.abc
OK: 0 errors, 0 warning(s)
```

Konversi + merge MIDI:

```
$ python3 skills/midi-orchestration/scripts/abc_to_midi.py song.abc pitched.mid
wrote pitched.mid: 3 tracks
  Sax     24 notes  max-poly 1
  Rhodes  88 notes  max-poly 4
  Bass    30 notes  max-poly 1

$ python3 skills/midi-orchestration/scripts/grid_to_midi.py drums.json drums.mid
wrote drums.mid: 150 drum hits across 24 bars

# merge pitched.mid + drums.mid -> output.mid
wrote output.mid: 4 tracks
  Sax    24 notes  end 73.85s
  Rhodes 88 notes  end 73.85s
  Bass   30 notes  end 73.85s
  Drums 150 notes  end 69.79s   (expected: bar 24 has no drum pattern by design)
tempo changes: 78.000078 BPM
time sig: 4/4
```

Checks:
- [x] `validate_abc.py` lulus tanpa error (0 errors, 0 warnings)
- [x] `output.mid`: 4 track, notes-per-track > 0 semua voice (Sax 24,
      Rhodes 88, Bass 30, Drums 150), tempo tag 78 BPM cocok Q:1/4=78,
      meter 4/4 cocok M:4/4 — diperiksa langsung dari objek PrettyMIDI,
      bukan hanya exit status validator.
- [x] Mono check: Sax dan Bass max-poly 1 (lead & bass memang harus
      monofonik).
- [x] Sync check: pitched dan drum track berakhir dalam rentang wajar
      satu sama lain (selisih ~4s dijelaskan oleh drum bar 24 yang memang
      silent by design, bukan desync yang tidak disengaja).

## L2/L3

Belum diisi di sini — lihat `scorecard.md` (L2 wajib diisi subagent
reviewer segar tanpa histori percakapan ini; L3 wajib telinga manusia
sesuai `../../tests/human-ear-protocol.md`, keduanya di luar wewenang
agent yang menulis artefak ini).

## Gate check

`validate_abc.py` lulus 0 error; `output.mid` diverifikasi langsung
(track count, notes-per-track, tempo/meter) — bukan hanya exit status.

# Rhythm fundamentals — compact working vocabulary

Diekstrak dari `ideation-theory.md` §1 (konsolidasi Task 3, arsitektur
skill baru). Vocabulary kerja tahap ide untuk feel dan pocket — dibaca
sebelum menulis pola groove/bass/drum konkret di `groove-rhythm/SKILL.md`.

> **Niat, bukan not.** Bagian ini niat-level: pilih *karakter* ritme
> (feel family, kapan syncopation/anticipation dipakai) dan nama pattern
> groove (lihat `groove-vocabulary.md`). Tick offset, swing ratio
> numerik, dan walking-bass not-demi-not adalah kerja `pyengine` —
> lihat `../../../docs/DOCTRINE-NIAT-BUKAN-NOT.md`. Bass ditulis di
> level niat: posisi chord-tone stack per bar/beat (field `degree`:
> 1/3/5/7/9/11/13 — lihat koreksi istilah di `../SKILL.md`) untuk
> chord tone; `pitch` eksplisit sah untuk approach tone kromatik yang
> bukan chord-tone; `octave` eksplisit wajib secara konvensi (validator
> tidak menegakkan ini, tapi tanpanya register jatuh salah); dan
> `beat` desimal (pickup/push) sah sebagai niat ritmis. Yang tetap
> terlarang: micro-timing/tick-offset mentah, velocity per-not
> numerik, dan voicing pitches literal — bukan pula scale degree
> tonal.

## Rhythm and subdivision

- **Feel** is set by subdivision family and where accents land —
  straight-eighths, swung-eighths, and 16th-based (funk, neo-soul) are
  the common families. Declare the family as *niat* (mis. "swung
  16th-based, neo-soul") lewat nama groove pattern
  (`groove-vocabulary.md`); jangan menulis rasio swing numerik sendiri.
- **Backbeat** (snare on 2 and 4) anchors most jazz-derived grooves; where
  you *break* it is where you create motion — dicatat sebagai niat
  ("backbeat dipertahankan"/"backbeat di-anticipate di bar X"), bukan
  offset tick.
- **Pocket** = karakter hubungan micro-timing antar-layer (mis. "bass
  laid-back, hi-hat sedikit di depan"). Karakter ini **dipilih lewat
  nama groove pattern** (`groove-vocabulary.md`, mis. `neo-soul-core`
  sudah membawa pocket laid-back) — bukan diputuskan/ditulis sebagai
  angka micro-timing oleh LLM; realisasinya deterministik-ber-seed di
  `pyengine`.

## Karakter bassline

Dipindah dari `ideation-theory.md` §4 (rapikan Task 3 — bukan materi
melodi, jadi tidak lagi tinggal di `melody-fundamentals.md`).

The bass defines the groove as much as the drums. Decide its *type* at
idea stage — niat karakter, bukan not konkret; realisasi jadi posisi
chord-tone stack (`degree`) per bar/beat, biarkan `pyengine` mengisi
pitch oktaf/walking-line/timing konkretnya:

- **Root-cycle / walking** — root/chord-tone tiap beat mengikuti
  pergerakan chord; swing and bebop default. Tulis urutan `degree`
  (mis. `1, 5, 1, 3`), bukan pitch literal per not.
- **Pedal** — satu `degree` (biasanya `1`) ditahan/diulang di bawah
  harmoni yang bergerak; tension and modal stasis.
- **Riff / ostinato** — pola `degree` berulang; funk, fusion, lofi hooks.
- **Sparse / syncopated** — space and off-beat hits (niat: "landing di
  beat 1 lalu ruang" = relaxed); laid-back neo-soul and lofi. Pola
  syncopation dicatat sebagai niat ("anticipation di akhir bar"), bukan
  offset tick — realisasi tetap kerja `pyengine`.

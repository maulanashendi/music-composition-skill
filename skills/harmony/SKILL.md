---
name: harmony
description: >-
  Pendalaman peta harmoni jazz — tonal center, harmonic rhythm, fungsi
  harmonik, tension map, teknik reharmonisasi, dan sistem voicing/voice-leading
  presisi. Dipanggil oleh `jazz-composition` saat mengerjakan Level 3 (peta
  harmoni) dan Level 7 (comping/voicing).
---

# Harmony

## Kapan dipakai

Dipanggil dari `jazz-composition` di dua titik:

- **Level 3 — Peta Harmoni**: menentukan tonal center, harmonic rhythm,
  fungsi harmonik tiap chord, dan tension map per bar.
- **Level 7 — Comping/Voicing**: menerjemahkan skeleton harmoni jadi voicing
  konkret + gerakan voice-leading, dipakai piano/gitar untuk comping.

Jika salah satu field ini belum ditentukan di brief atau `composition-plan.json`
(tonal center, harmonic rhythm, chord function tiap bar) — **tanya, jangan
menebak.**

## Langkah 1 — Tentukan tonal center

Contoh: `C major`, `D minor`, `F Dorian`, `G Mixolydian`, atau multi-tonal.

## Langkah 2 — Tentukan harmonic rhythm

Harmonic rhythm adalah seberapa sering chord berubah — 1 chord per bar,
2 chord per bar, 1 chord setiap 2 bar, atau kombinasi. Harmonic rhythm lambat
memberi ruang modal; harmonic rhythm cepat memberi kesan bebop atau
functional jazz.

## Langkah 3 — Buat harmonic skeleton

Contoh delapan bar (baru kerangka fungsi):

```
| Dm7 | G7 | Cmaj7 | Cmaj7 |
| Em7 | A7 | Dm7   | G7    |
```

## Langkah 4 — Tentukan fungsi harmonik

Tonic, Predominant, Dominant, Resolution, Temporary tonicization, Modal area,
Chromatic departure. Contoh: `Dm7 = predominant`, `G7 = dominant`,
`Cmaj7 = tonic`, `A7 = secondary dominant`.

## Langkah 5 — Tambahkan warna

Kerangka sederhana `Dm7 – G7 – Cmaj7` dapat dikembangkan menjadi
`Dm9 – G13b9 – Cmaj9`, atau `Dm11 – Db13 – Cmaj9`.

## Langkah 6 — Buat tension map

Tandai tingkat tegangan setiap bar, mis.: bar 1 stabil, bar 2 mulai bergerak,
bar 3 stabil, bar 4 terbuka, bar 5 meningkat, bar 6 tinggi, bar 7 dominan
kuat, bar 8 resolusi. Tension map inilah yang dipakai `advanced-melody`
untuk memutuskan bar mana boleh outside.

## Teknik harmonik

- ii–V–I
- secondary dominant
- tritone substitution
- backdoor dominant
- modal interchange
- diminished passing chord
- chromatic mediant
- pedal point
- constant structure
- slash chord
- polychord
- reharmonization
- side-slipping harmony

## Vocabulary kerja

Ringkasan kerja chord quality, chord-progression logic, dan voice-leading
feel (diekstrak dari `ideation-theory.md`, bagian harmoni):

**Scales dan chord quality** — kualitas inti dan warna/fungsi defaultnya:

- **maj7 / 6 / 6/9** — stabil, resting (tonic).
- **m7 / m6 / m9** — stabil minor atau supertonic; m6 dan m(maj7) condong ke
  tonic-minor.
- **dom7 (7, 9, 13, alt)** — tidak stabil, ingin resolve turun perfect fifth;
  `alt` (b9#9b13) memaksimalkan tension.
- **m7b5 (half-dim)** — pre-dominant di minor (ii dari minor ii-V-i).
- **dim7** — passing/leading, simetris, menghubungkan chord diatonis secara
  kromatik.

Pasangan scale-chord yang benar-benar dipakai: major/Ionian di atas maj7,
Dorian di atas m7 (warna minor default jazz), Mixolydian di atas dom7, Lydian
di atas maj7#11, altered/diminished di atas dom7alt, minor-pentatonic/blues
di atas hampir semua chord untuk lead yang rootsy.

Modal writing: pilih satu mode dan *bertahan*, warnai dengan characteristic
note-nya (natural 6 di Dorian, b2 di Phrygian, #4 di Lydian). Groove modal
hidup di satu atau dua chord — gerakan datang dari bass dan melodi, bukan
pergantian chord.

**Chord progression logic**:

- **Functional motion** = tension→resolution via descending fifths (ii-V-I,
  dan bentuk minornya ii(m7b5)-V(alt)-i). Pakai saat butuh dorongan ke depan
  dan arrival yang jelas. Jangan pakai ii-V-I secara refleks — hanya saat
  motion terarah memang melayani mood.
- **Loop-based / static harmony** = sel pendek (biasanya 2 atau 4 chord) yang
  berulang; identitas datang dari groove dan melodi. Ini tulang punggung
  lofi/jazzhop. Loop 4-chord yang kuat biasanya mencampur satu tonic stabil,
  satu color chord (maj7 naik minor third, atau bIII/bVI), dan satu tension
  chord ringan.
- **Modal interchange / borrowed chords** (bVImaj7, bVIImaj7, iv, bII)
  menambah kehangatan dan kejutan tanpa keluar dari key center.
- **Harmonic rhythm** = seberapa cepat chord berubah. Lambat (satu chord per
  bar atau lebih lambat) = lapang, groove-forward, lofi. Cepat (dua+ per bar)
  = bebop, sibuk, forward-driving. Memilih harmonic rhythm sering jadi
  keputusan identitas yang lebih besar daripada memilih chord itu sendiri.

Contoh loop minor (C minor, lofi): `Cm9 | Abmaj7 | Fm9 | G7alt` — tonic, warna
bVI yang hangat, subdominant minor, tension kembali ke i. Terasa laid-back
karena harmonic rhythm satu chord per bar dan tension chord resolve dengan
lembut.

**Harmony dan voice-leading feel** — di tahap ide belum menulis voicing
persis (itu urusan `references/voicing-systems.md`), tapi tentukan
*tekstur*-nya: rootless comping (shell 3-7-9-13) terbaca modern/jazzy; open
triad di atas bass terbaca bersih/pop-jazz; quartal/stacked-4th terbaca modal
dan cool. Prinsip voice-leading yang perlu diingat: common tone ditahan,
voice lain bergerak stepwise, memberi perubahan yang halus; lompatan paralel
besar terbaca berani atau naif tergantung intent.

## Voicing presisi

> Pitches di `references/voicing-systems.md` pakai **scientific pitch
> notation** (middle C = `C4`), bukan notasi oktaf ABC. Saat menerjemahkan
> voicing ke ABC yang ditulis `abc-notation-writer`, konversi eksplisit: `C`
> tanpa tanda di ABC = `C4`, tiap koma menurunkan satu oktaf (`C,` = `C3`,
> `C,,` = `C2`), tiap apostrof menaikkan satu (`c'` = `C6`, dengan `c`
> huruf kecil = `C5`). Pakai referensi ini untuk memutuskan *pitch dan jalur
> voice-leading* mana yang dipakai; pakai `abc-syntax.md` untuk cara
> menotasikannya.

Baca `references/voicing-systems.md` untuk sistem voicing lengkap: hierarki
voice, register zone, keluarga voicing inti (shell, rootless, quartal,
spread, upper-structure, drop, intervallic, cluster), prosedur piano/Rhodes,
jalur voice-leading presisi, desain inner-line, attack/release, variasi
voicing lintas form, reduksi per-instrumen, dan audit checklist.

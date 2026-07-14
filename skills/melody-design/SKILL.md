---
name: melody-design
description: >-
  Desain melodi dasar — motif, kontur, target tone, broken chord. Dipanggil
  `jazz-composition` untuk Level 4 tahap 1–6.
---

# Melody Design

## Kapan dipakai

Dipanggil dari `jazz-composition` untuk **Level 4 — Desain Melodi, tahap
1–6**: motif, kontur, target tone, dan broken chord. Melodi di sini
dirancang sebagai struktur horizontal, bukan sekadar nada yang ditempelkan
pada chord.

Untuk **outside playing/chromatic vocabulary (tahap 7–8)**, lihat
`../advanced-melody/SKILL.md` — jangan campur di sini.

Jika harmonic skeleton (Level 3) atau tension map belum dikunci — **tanya,
jangan menebak**, karena target tone di sini bergantung pada chord yang
sudah pasti.

## Tahap 1 — Tentukan motif inti

Motif dapat berasal dari: interval, ritme, contour, repeated note, arpeggio
fragment, chromatic cell.

Contoh motif intervalik: `D – A – F` (struktur interval: naik perfect
fifth, turun major third). Contoh motif ritmis: pickup – quarter note – two
eighth notes – long note.

## Tahap 2 — Tentukan kontur

Contoh: rendah → naik → puncak → turun. Atau: angular → stabil → angular →
resolusi. Kontur membuat frase terasa memiliki arah.

## Tahap 3 — Tentukan target tones

Pilih nada utama pada setiap chord. Contoh:

```
| Dm7 | G7 | Cmaj7 |
| F   | B  | E     |
```

Nada target biasanya: chord tone, guide tone, extension, atau alteration
yang akan diresolusikan.

## Tahap 4 — Hubungkan target tones

Gunakan: stepwise motion, interval leap, arpeggio, chromatic approach,
enclosure, passing tone, neighbor tone.

Contoh: `F – A – C – B | Bb – B – D – F | E`.

## Tahap 5 — Gunakan interval secara sadar

Interval kecil memberi kesan lyrical, smooth, singable, connected. Interval
besar memberi kesan angular, modern, dramatic, energetic.

Prinsip yang efektif: **leap → recovery**. Contoh: `D – Bb – A – G – F` —
setelah lompatan besar, melodi kembali dengan gerakan bertahap.

## Tahap 6 — Gunakan broken chord

Broken chord membuat harmoni terdengar secara linear. Contoh pada Dm9:
`D – F – A – C – E`.

Jangan selalu berurutan — gunakan displacement (`D – A – F – E – C`) atau
intervallic arpeggio (`F – C – E – A`).

## Gate tempo — densitas ritmis vs BPM (wajib)

Artefak Level 4 wajib:

1. Menyebut **BPM brief secara eksplisit** (angka, bukan "sedang").
2. Menyatakan **IOI (inter-onset interval) tercepat** yang benar-benar
   dipakai melodi (subdivisi terkecil antar onset, mis. 16th) dan **rest
   ratio** melodi (proporsi waktu rest per section).
3. Mengecek keduanya terhadap tabel BPM band di
   `../vibes-mood/references/reasoning-theory.md` (kolom "Subdivisi melodi
   wajar" + "Napas minimum" untuk band BPM brief).

Melodi yang memakai subdivisi lebih rapat dari kolom "Subdivisi melodi
wajar" band-nya, atau napas lebih pendek dari "Napas minimum", **direvisi
atau diberi justifikasi eksplisit tertulis** — bukan dilewatkan diam-diam.
Motif 16th padat yang lolos semua rubrik teori tetap ditolak di sini bila
tidak bisa dimainkan wajar pada BPM brief.

## Output level ini

Melodi utama dalam bentuk notasi atau MIDI yang sudah memiliki: motif,
kontur, target tone, tension, resolution, ruang, dan identitas ritmis.

## Referensi lanjutan

`references/melody-fundamentals.md` — vocabulary kerja tambahan: dramatic
arc dan phrasing/tension-release (menghubungkan pilihan melodi ke arc
emosional keseluruhan), motif/hook/development, song structure, dan
arrangement/instrument interaction. Baca saat butuh landasan mengapa suatu
pilihan motif/kontur cocok untuk arc lagu, bukan sekadar mekanik tahap 1–6.

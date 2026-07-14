---
name: arrangement
description: >-
  Pendalaman aransemen instrumen, comping/voicing role, interlude/shout
  chorus/transisi, intro/ending, dan dinamika/dramaturgi. Dipanggil
  `jazz-composition` untuk Level 6, 7, 11, 12, 13.
---

# Arrangement

## Kapan dipakai

Dipanggil dari `jazz-composition` di lima titik:

- **Level 6 — Aransemen Instrumen**: distribusi fungsi musik ke tiap
  instrumen.
- **Level 7 — Comping** (bagian teknik saja — voicing presisi ada di
  `harmony/SKILL.md`).
- **Level 11 — Interlude, Shout Chorus, dan Transisi**.
- **Level 12 — Intro dan Ending**.
- **Level 13 — Dinamika dan Dramaturgi**.

Jika struktur bagian (section list) belum dikunci di Level 2 — **tanya,
jangan menebak** sebelum mengerjakan level-level di atas.

## Level 6 — Aransemen instrumen

**Tujuan**: mendistribusikan fungsi musik kepada masing-masing instrumen.
Setiap instrumen harus punya peran.

**Instrumen melodi** — membawa head, memainkan counterline, improvisasi,
memberikan artikulasi utama.

**Piano atau gitar** — comping, voice leading, harmonic color, rhythmic
interaction, fills, countermelody.

**Bass** — root movement, walking line, pedal point, counterpoint, rhythmic
grounding.

**Drum** — timekeeping, shaping dynamics, interaction, transitions, accents,
form marking.

Hindari semua instrumen bermain penuh sekaligus. Gunakan perubahan
kepadatan: sparse → medium → dense → sparse.

Output level ini — sebuah orchestration map, contoh:

```
Intro: Piano rubato, bass pedal
A1: Sax melody, piano sparse voicing, bass two-feel
A2: Sax melody, piano active comping, walking bass, ride cymbal
Bridge: Full rhythm section, stronger dynamics
A3: Unison line pada dua bar terakhir
```

## Level 7 — Teknik comping

**Tujuan**: menghindari permainan solid chord yang statis — comping harus
jadi bagian dialog musikal.

Hindari block chord terus-menerus. Sebagai alternatif, gunakan variasi
sudut pakai voicing (jenis voicing itu sendiri ada di `harmony/SKILL.md` §
Voicing presisi): top note bergerak, inner voice bergerak, bass bergerak,
ritme berubah, density berubah — bukan sekadar chord 1, chord 2, chord 3
dipukul berurutan.

**Teknik comping**: Charleston rhythm, anticipatory stab, sustained pad,
fragmented chord, rhythmic answer, fill, call and response, delayed
resolution, pedal voicing.

Output level ini — comping chart per bagian, contoh:

```
A1: sparse, 2–3 attacks per bar
A2: syncopated responses
Bridge: denser voicing
Solo: interactive comping
Head out: simplified voicing
```

## Level 11 — Interlude, shout chorus, dan transisi

**Tujuan**: mencegah bentuk lagu terasa hanya seperti tema → solo → tema.

**Interlude** — mengubah warna, memindahkan tonal center, memberi reset,
menyiapkan solo berikutnya.

**Shout chorus** — menciptakan klimaks, menggabungkan ensemble, memperkuat
motif utama. Dapat memakai unison line, harmonized line, rhythmic hits,
sequence, call and response, high register, metric displacement.

**Transition** — drum fill, bass pickup, dominant pedal, chromatic sequence,
breakdown, fermata, rubato bar.

Output level ini: bagian transisi yang tertulis jelas.

## Level 12 — Intro dan ending

**Intro** harus memperkenalkan dunia lagu. Pilihan: vamp, rubato, pedal
point, motif preview, reharmonized theme, drum groove, bass ostinato.
Contoh: 4 bar piano rubato, 4 bar bass pedal, masuk head.

**Ending** — pilihan: tag ending, ritardando, fermata, repeated vamp, sudden
stop, unresolved dominant, final unison hit, fade-style vamp. Ending
sebaiknya berhubungan dengan motif utama.

Output level ini: intro dan coda yang punya identitas, bukan sekadar
tambahan.

## Level 13 — Dinamika dan dramaturgi

**Tujuan**: membuat lagu terasa hidup dari awal sampai akhir.

Buat energy curve, contoh:

```
Intro        20%
A1           35%
A2           45%
Bridge       60%
A3           50%
Solo 1       55–70%
Solo 2       65–85%
Shout chorus 100%
Head out     70%
Coda         30%
```

**Parameter dinamika** bukan hanya volume — gunakan register, density,
articulation, harmonic tension, rhythmic activity, number of instruments,
note duration, silence.

Output level ini: peta energi per section.

## Referensi lanjutan

- `references/ensemble-interaction.md` — mekanik call-and-response dan
  interaksi antar-instrumen presisi. Baca saat Level 6/7 butuh detail siapa
  merespons siapa, bukan sekadar peran garis besar.
- `references/instrumental-transitions.md` — teknik transisi antar-section
  presisi (fill, pickup, breakdown). Baca saat mengerjakan Level 11.
- `references/interaction-map.md` — peta interaksi lengkap per section untuk
  arrangement yang kompleks. Baca saat orchestration map Level 6 perlu
  detail lebih dari sekadar tabel peran.
- `references/form-and-dramaturgy.md` — mekanik form: panjang bar/phrase,
  dimensi kontras antar-section, kekuatan kadens, bentuk solo, strategi
  intro/ending. Baca untuk Level 11–13 saat butuh mekanik lebih dalam dari
  ringkasan di atas.
- `references/loop-development.md` — DNA loop, kelas mutasi, dan timescale
  pengembangan untuk brief yang loop-centered (lofi, jazzhop, neo-soul).
  Baca saat aransemen berbasis loop, bukan form linear tradisional.

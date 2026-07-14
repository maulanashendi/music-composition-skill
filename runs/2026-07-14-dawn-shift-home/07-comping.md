# 07 — Comping dan Voicing (Level 7)

Rhodes diam bar 1-4 (section 1, bass solo). Comping chart di bawah
mencakup bar 5-23 (Rhodes aktif); bar 24 Rhodes reda ke diam (lihat
`06-arrangement.md`).

## Comping chart per section

- **Section 2 (bar 5-8):** sparse, shell/rootless voicing, 1 attack per
  bar (whole-note sustain) — "kehadiran pertama", tidak mendominasi.
- **Section 3 (bar 9-12):** masih 1 attack per bar tapi chord makin
  berwarna (Fmaj7, Gm9, CMaj9) — momentum menumpuk lewat WARNA, bukan
  lewat densitas ritme (ritme comping baru berubah di section 4).
- **Section 4 (bar 13-18):** comping paling aktif — voicing terkaya
  (Cmaj7#11 dengan #11 ditonjolkan di top note, lihat catatan gate di
  bawah).
- **Section 5 (bar 19-21):** menipis ke voicing 3-nada (sustain pad,
  graft — bukan diam total).
- **Section 6 (bar 22-23):** sustain pad sama seperti section 5 (jejak
  terakhir), reda ke diam di bar 24.

## Voicing per bar (rootless/shell — bass membawa root)

| Bar | Chord | Voicing (bawah→atas) | Top note |
|---|---|---|---|
| 5 | Dm9 | F4 A4 C5 E5 | E |
| 6 | Gm7 | D4 Bb4 F5 | F |
| 7 | Dm9 | F4 A4 C5 E5 | E |
| 8 | Cmaj7 | E4 G4 B4 | B |
| 9 | Dm9 | F4 A4 C5 E5 | E |
| 10 | Fmaj7 | A4 C5 E5 | E |
| 11 | Gm9 | D4 Bb4 F5 A5 | A |
| 12 | CMaj9 | E4 G4 B4 D5 | D |
| 13 | Dm9 | F4 A4 C5 E5 | E |
| 14 | Dm9 | F4 A4 C5 E5 | E |
| 15 | A7sus4 | D4 E4 G4 | G |
| 16 | D9 | F#4 A4 C5 E5 | E |
| 17 | Cmaj7#11 | E4 G4 B4 F#5 | **F# (#11 ditonjolkan)** |
| 18 | D9 | F#4 A4 C5 E5 | E |
| 19 | D6add9 | F#4 B4 E5 | E |
| 20 | Gmaj7 | D4 B4 F#5 | F# |
| 21 | D6add9 | F#4 B4 E5 | E |
| 22 | D6add9 | F#4 B4 E5 | E |
| 23 | D6add9 | F#4 B4 E5 | E |

## Voice-leading — klaim (diverifikasi terhadap fakta, lihat gate di bawah)

Top note **E** berfungsi sebagai common-tone anchor yang berulang di
mayoritas bar (5,7,9,10,13,14,16,18,19,21,22,23) — nada ini TIDAK
bergerak antar-chord-chord itu (voice-leading paling halus: diam di
tempat). Top note baru berpindah untuk warna spesifik: **F** (bar 6,
borrowed iv), **B** (bar 8, bVII), **A** (bar 11, borrowed iv/9),
**D** (bar 12, bVII/9), **G** (bar 15, sus4 approach), **F#** (bar 17 dan
20 — sengaja ditonjolkan sebagai penanda brightening/#11, menjawab
risiko yang dicatat selector Level 1 soal "nada pembeda mode harus
ditonjolkan, bukan disembunyikan di voicing"). Inner voice (A/C, D/Bb,
dst.) bergerak stepwise/common-tone mengikuti perubahan chord — detail
lengkap ada di kolom "Voicing" tabel di atas, bukan diklaim terpisah dari
notasi tertulis.

## Cek fakta notasi (gate wajib Level 7)

Voicing di atas ditulis sebagai bracket chord ABC lalu dijalankan lewat
`notation_facts.py --voice 1` (dua segmen, sama seperti Level 3, karena
pc-collection berbeda sebelum/sesudah brightening):

```
uv run --with music21 --with pretty_midi python notation_facts.py <bar5-14.abc> --voice 1   # K:C proxy D Dorian
uv run --with music21 --with pretty_midi python notation_facts.py <bar15-23.abc> --voice 1  # K:G proxy D Mixolydian
```

Hasil (`top-note` per bar dari output asli script): bar5-14 =
E,F,E,B,E,E,A,D,E,E — **cocok persis** dengan kolom "Top note" tabel di
atas. bar15-23 = G,E,F#,E,E,F#,E,E,E — **cocok persis**. Tidak ada
mismatch antara klaim voice-leading (top note anchor di E, F# ditonjolkan
di bar 17/20) dan fakta tertulis — tidak perlu revisi.

Semua chord terklasifikasi `diatonik` kecuali Gm7 (bar6) dan Gm9 (bar11)
= `borrowed`, konsisten dengan label fungsi harmonik di `03-harmony.md`.
Tidak ada chord `unparsed`.

## Gate check (Level 7)

Comping chart mencakup semua bagian yang butuh comping (section 2-6,
bar 5-23). Klaim voice-leading top-note diverifikasi cocok dengan
`notation_facts.py` — lihat di atas. Lanjut ke Level 8.

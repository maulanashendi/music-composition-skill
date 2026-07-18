# 05 — Desain Melodi: Kandidat & Seleksi (Level 4)

**Objective:** motif 1-2 bar untuk bar 1-2 head (atas Dm9→Gm9) yang
terasa "menyala satu-satu" — gerak bertahap, ada rest (ruang), landing
di chord tone hangat (9th/3rd), dimainkan rhodes sebagai lead.

**Immutable constraints:** niat-level (pitch+durasi eksplisit, TANPA
velocity/off-grid — lihat doktrin); instrumen rhodes, range
INSTRUMENT_RANGES rhodes = MIDI 48-84 (C3-C6).

**Assumptions:** motif ini dipakai sebagai template bar1-2, lalu
diulang/divariasikan bar5-6 (loop head kedua) dan digemakan sekilas di
outro bar1 (graft dari Kandidat B Level 1).

## Kandidat (pitch+durasi eksplisit 1-2 bar, atas Dm9 bar1 → Gm9 bar2)

**Motif A — "menyala satu-satu" (stepwise, banyak rest).**
Bar1: beat1 D5 dur1.5, beat3 F5 dur1, (rest beat4). Bar2: beat1 G5
dur1.5, beat3 Bb4 dur1, (rest beat4).
- Jumlah pitch aktual: 4 (rest tidak dihitung pitch).
- Interval berurutan: D5→F5 = +3 semitone (minor third naik); F5→G5
  = +2 semitone (major second naik, lompat antar-bar); G5→Bb4 = -3
  semitone (minor third turun).
- Relasi ke chord: D5 = root Dm9 (chord-tone); F5 = b3 Dm9
  (chord-tone); G5 = root Gm9 (chord-tone); Bb4 = b3 Gm9
  (chord-tone). Semua landing di chord-tone, tak ada tension/outside.

**Motif B — "menahan nada" (long tone, target 9th).**
Bar1: beat1 E5 dur4 (satu nada penuh 1 bar, 9th dari Dm9 — tension
diatonik, bukan chord-tone triad tapi bagian ekstensi 9). Bar2: beat1
A5 dur4 (9th dari Gm9).
- Jumlah pitch aktual: 2.
- Interval berurutan: E5→A5 = +5 semitone (perfect fourth naik).
- Relasi ke chord: E5 = 9th Dm9 (tension-diatonik/ekstensi, bukan
  chord-tone triad); A5 = 9th Gm9 (sama).

**Motif C — "lompat lalu turun" (leap, kontur lebih dramatis).**
Bar1: beat1 A5 dur1, beat2 D5 dur2, beat4 F5 dur1. Bar2: beat1 Bb5
dur1, beat2 G5 dur2, beat4 D5 dur1.
- Jumlah pitch aktual: 6.
- Interval berurutan: A5→D5 = -7 semitone (perfect fifth turun);
  D5→F5 = +3 semitone (minor third naik); F5→Bb5 = +5 semitone
  (perfect fourth naik, lompat antar-bar); Bb5→G5 = -3 semitone
  (minor third turun); G5→D5 = -7 semitone (perfect fifth turun).
- Relasi ke chord: A5 = 5th Dm9 (chord-tone); D5 = root Dm9
  (chord-tone); F5 = b3 Dm9 (chord-tone); Bb5 = 5th Gm9 (chord-tone);
  G5 = root Gm9 (chord-tone); D5 = b3 Gm9 (chord-tone). Semua
  chord-tone, tak ada tension.

## Pre-mortem

- Kelemahan A: interval kecil semua (2nd/3rd) — aman tapi mungkin
  kurang "sedikit rindu" (tidak ada tension/9th yang biasanya
  membawa rasa itu).
- Kelemahan B: hanya 2 pitch di 2 bar (sangat jarang), landing di 9th
  yang cocok "hangat/rindu" tapi terlalu minim untuk motif yang harus
  "dikenali kembali" di outro (kurang karakter ritmik).
- Kelemahan C: kontur leap besar (5th/4th) terasa lebih "dramatis
  aktif" daripada "tenang" — sedikit bertentangan dengan brief
  "tenang tapi tidak sedih" yang minta gerak lebih halus.

## Selected + alasan (dengan graft)

**A** dipilih sebagai basis (stepwise, tenang, banyak rest = ruang
"jalan basah yang sepi") meski kelemahannya (kurang tension/rindu)
lebih ringan daripada kelemahan B (motif terlalu tipis utk dikenali
ulang) dan C (kontur terlalu aktif utk vibe tenang). **Graft dari B:**
satu nada panjang bertahan (9th) diselipkan di bar 3 head (atas
Cmaj9) sebagai puncak kalimat — memberi warna "rindu" yang hilang di
A murni, tanpa mengubah karakter stepwise-tenang keseluruhan motif.

**Exact artifact:** `05-melodi.md`.

**Unresolved/confidence:** sedang-tinggi — kombinasi A+graft-B belum
pernah diuji telinga (itu peran `rendering-audition` fase Review);
confidence di level niat (kontur+chord-tone koheren) tinggi, confidence
"terdengar enak" menunggu audition.

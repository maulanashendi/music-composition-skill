# 05 — Desain Melodi (Level 4)

1. **Level:** 4 — Desain Melodi.
2. **Aesthetic thesis (rujukan):** lihat `02-konsep.md`.
3. **Immutable constraints:** niat-level saja (pitch+durasi+artikulasi,
   TANPA velocity/off-grid); instrumen rhodes.
4. **Assumptions:** motif dipakai di head (bar1-8), digemakan sekilas
   di outro bar1, intro tanpa melodi (murni comp+bass+drum, lihat
   `03-bentuk.md`).
5. **Decision:** Motif **A** (stepwise, banyak rest) + graft dari
   Motif B (satu nada panjang 9th sebagai puncak kalimat di bar 3).
6. **Rationale:** gerak stepwise + rest = citra "lampu menyala
   satu-satu, jalan sepi tenang"; nada panjang 9th di puncak kalimat
   (bar 3, atas Cmaj9) = warna "hangat, sedikit rindu" tanpa mengubah
   karakter tenang keseluruhan.
7. **Alternatives considered/rejected:** Motif B murni (terlalu tipis
   utk motif yang harus dikenali ulang), Motif C (kontur leap terlalu
   aktif utk vibe tenang) — lihat `05-melodi-candidates.md`.
8. **Interaction with other levels:** landing tiap downbeat bar baru
   ada di chord-tone (root/3rd) kecuali bar 3 (9th, tension diatonik
   sengaja) — memenuhi rekomendasi target-tone di `plan-verifying`
   (downbeat bar baru sebaiknya 3rd/7th; bar 3 sengaja menyimpang ke
   9th untuk warna "rindu", dicatat di sini sebagai keputusan sadar
   supaya kalau `plan-verifying` melaporkan warning target-tone di bar
   itu, itu **diterima sadar**, bukan bug).
9. **Risks:** warning target-tone di bar 3 (lihat poin 8) — mitigasi:
   dicatat eksplisit sebagai keputusan niat, bukan kecelakaan.
10. **Confidence:** sedang-tinggi (niat koheren; "enak" menunggu
    audition).
11. **Next action:** lanjut Level 5 — Ritme/Groove.

## Niat melodi final (per bar, head + gema outro)

Chord acuan per bar: lihat `04-harmoni.md`.

- **Bar 1 (Dm9):** D5 dur1.5 legato (beat1) → F5 dur1 legato (beat3)
  → rest beat4.
- **Bar 2 (Gm9):** G5 dur1.5 legato (beat1) → Bb4 dur1 tenuto (beat3)
  → rest beat4.
- **Bar 3 (Cmaj9, puncak kalimat — graft Motif B):** E5 dur2 tenuto
  (beat1, 9th Cmaj9 — tension diatonik sengaja) → rest beat3-4.
- **Bar 4 (Fmaj9):** A4 dur1 legato (beat1) → C5 dur1 legato (beat2)
  → A4 dur2 tenuto (beat3).
- **Bar 5 (Dm9, ulang loop kedua — variasi artikulasi):** D5 dur1.5
  legato (beat1) → F5 dur1 accent (beat3, aksen sedikit beda dari bar1
  supaya tidak identik) → rest beat4.
- **Bar 6 (Gm9):** Bb4 dur1.5 legato (beat1) → G5 dur1 legato (beat3)
  → rest beat4.
- **Bar 7 (Cmaj9, puncak kedua — ditahan lebih lama, arc menuju
  outro):** E5 dur4 tenuto (beat1, seluruh bar).
- **Bar 8 (Fmaj9, penutup head):** C5 dur4 ghost (beat1, memudar).
- **Outro bar 1 (Fmaj9, gema motif — bukan progresi baru):** A4 dur4
  ghost (beat1, gema landing chord-tone Fmaj9, lebih pelan dari bar 8
  head).

Fakta objektif (jumlah pitch, interval, relasi chord) untuk motif inti
bar1-2 sudah dihitung di `05-melodi-candidates.md` (Motif A); bar 3-8
+ gema outro adalah ekstensi niat yang memetakan arc Level 1-2 ke
kalimat penuh, tidak diklaim melalui protokol kandidat→seleksi ulang
(hanya Level 4 "inti" 1-2 bar yang wajib 3-kandidat per
`candidate-selection-protocol.md` — perpanjangan ke bar 3-8 adalah
pekerjaan komposisi biasa, bukan titik keputusan ber-leverage tinggi
baru).

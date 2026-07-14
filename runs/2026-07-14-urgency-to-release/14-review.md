# 14 — Review Keseluruhan & Revisi Low Level (Level 14/Tahap 14-15)

## Bentuk besar (Tahap 14) sebelum detail nada

Dicek terhadap `02-form.md`/`13-dynamics.md`: energy curve naik monoton
Intro->Climax lalu turun tajam di Coda; density (`06-arrangement.md`)
sparse->full->sparse; tidak ada section yang menumpuk semua device
sekaligus (comping paling sibuk justru di B, bukan di climax, yang malah
disederhanakan jadi unison hits — kontras disengaja, lihat
`07-comping.md`). Bentuk besar terasa konsisten dengan brief sebelum turun
ke revisi nada per Tahap 15.

## Revisi low-level (Tahap 15) — perubahan dari desain abstrak ke `song.abc`

Tabel target-tone di `04-melody.abc` adalah niat awal; saat ditulis jadi
notasi valid, beberapa target tone digeser demi voice leading yang
benar-benar mulus dan supaya durasi tiap bar pas 7 unit (7/8):

- Bar 3-5, 7, 9: motif inti disederhanakan jadi 3 not seperdelapan (bukan
  campuran durasi seperti draf ilustratif awal) supaya pas persis 3 unit
  di grup pendek, sisa 4 unit diam di grup panjang — realisasi literal
  dari "ruang" yang dicatat di Tahap 7.
- Bar 13 (G7#11): target awal dicatat C# di `04-melody.abc`, tapi realisasi
  akhir memakai D-G-E (mengulang bentuk sel asli) supaya sequence B section
  terasa "kembali pulang" sesaat sebelum lompatan besar bar 14 — perubahan
  disengaja, dicatat di sini alih-alih diam-diam menyimpang dari tabel.
- Bar 14 (A7alt, titik pivot): diperluas jadi arpeggio 3-nada dari chord
  tone A7 (C#-E-G#) alih-alih sel motif standar — pivot dominan butuh
  warna yang lebih terbuka daripada sel P4/m3 biasa.
- Climax (bar 15-18): interval dilebarkan ke leap oktaf/lompat besar (per
  rencana Tahap 9), durasi not diperpanjang (2-2-3 unit, bukan 1-1-1) untuk
  kesan "sustained, triumphant" bukan buru-buru.

Voice leading dicek: top note Rhodes tetap bergerak stepwise/half-step
antar-bar sepanjang A/A′ (F->A->F->F#->E->Ab->E->Bb, sama seperti draf
`07-comping.md`, tidak berubah saat direalisasi). Register seimbang: sax
naik dari midrange (bar 3-14) ke oktaf lebih tinggi hanya di climax
(bar 15-18), tidak sebelumnya — supaya lompat register itu memang terasa
sebagai puncak, bukan dipakai lebih awal. Voicing Rhodes di climax
disederhanakan jadi satu chord sustain per bar (bukan padat) — sengaja,
lihat `07-comping.md`. Ending (bar 19-20) memakai motif yang sama
(rising-4th shape, dilebarkan) sebelum landing di D terbuka — terasa
selesai karena kembali ke identitas motif, bukan formula kadens generik.

## Gate check (Level 14, prosa)

Semua poin Tahap 14-15 (voice leading, interval, phrasing, density,
voicing, bass line, drum setup, articulation) diperiksa di atas relatif
terhadap draf Level 4-13; validasi mekanis (validator + MIDI) ada di
`scorecard.md` L1.

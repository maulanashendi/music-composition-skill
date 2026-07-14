# 05 — Ritme dan Groove (Level 5)

## Feel

Straight-eighth/sixteenth ter-humanize (bukan swing kental) — profil
`neo-soul-core` (lihat `groove-rhythm/references/groove-profiles.md`).
Tempo 74 BPM, konstan sepanjang lagu (aesthetic thesis Level 1: bass yang
"tak pernah mempercepat langkahnya"). Swing ringan (0.56) — cukup untuk
nuansa lo-fi, tidak sampai terasa shuffle jazz klasik.

## Rhythmic identity per section

| Section | Identitas ritmis |
|---|---|
| 1 Alone | Spacious, laid-back — bass sendirian, ruang besar antar-nada |
| 2 Comping in | Masih spacious, Rhodes comping jarang (2-3 attack/bar) |
| 3 Steps gather | Mulai syncopated — drum masuk, hi-hat membangun subdivisi |
| 4 Light arrives | Anticipatory — lead masuk dengan leap yang jatuh sedikit di belakang grid (laid-back, bukan tepat di depan) |
| 5 Thinning/Return | Spacious lagi — kembali dekat section 1, tapi groove drum tetap jalan (ghost hi-hat), bukan berhenti total |
| 6 Arrival | Dense-tapi-tenang sesaat (unison convergence), lalu spacious penuh di bar akhir |

## Placement aksen (dari profil `neo-soul-core`)

- Kick = anchor, nyaris tepat di grid (0 s/d +4 tick).
- Snare/rimshot = laid-back, +18 s/d +24 tick di belakang grid — sumber
  utama nuansa "lelah tapi lapang" secara ritmis.
- Bass, kedatangan (downbeat ganti chord) = +2 s/d +7 tick, dekat kick.
- Bass, pickup/approach = -12 s/d -6 tick (mendahului grid).
- Rhodes comping = +16 s/d +22 tick, mirip snare — comping "bernapas"
  bersama backbeat.
- Lead, nada target/struktural = +3 s/d +10 tick (dekat grid, sedikit di
  belakang) — termasuk lompatan 6th di bar 16, ditempatkan SEDIKIT di
  belakang grid supaya "arrival" terasa lega, bukan terburu-buru.
- Hi-hat = tiered: quarter-note kuat dekat grid, off-beat lebih pelan
  (ghost-level, velocity <45).

Nilai eksak (map `timing` siap-pakai untuk `09-drums.json`, disalin dari
`groove-profiles.md`, tidak dihitung ulang): `{"kick": 0, "snare": 15,
"rimshot": 25, "chh": -3}`.

## Pola comping (ringkas, detail penuh di `07-comping.md`)

Sparse di awal (section 2), makin interaktif seiring drum masuk
(section 3-4), menipis lagi di section 5 (graft: sisakan sustain pad,
jangan diam total), diam di section 6 (fokus ke unison bass+lead).

## Pola bass (ringkas, detail penuh di `08-bassline.md`)

Walking/pedal hybrid: bukan walking bass penuh 4-beat (terlalu "sibuk"
untuk karakter restrained), bukan pedal statis murni (terlalu datar) —
kontur dari root + 5th + satu approach note per perubahan chord, dengan
ruang (rest) di antaranya supaya "spacious" section 1 benar-benar
terdengar tenang, bukan kosong.

## Karakter drum (ringkas, detail penuh di `09-drums.json`)

Lo-fi, kick bulat minim click, snare/rimshot dusty, backbeat laid-back
(lihat placement aksen di atas). Masuk bertahap: section 3 hanya
hi-hat/rimshot; ride/kick penuh baru section 4; ghost hi-hat saja di
section 5 (graft — jangan diam total); minim/diam di section 6 kecuali
satu aksen di titik konvergensi.

## Gate check (Level 5)

Feel dan rhythmic identity ditentukan eksplisit per section (tabel di
atas). Groove reference (`neo-soul-core`) cukup spesifik untuk diturunkan
ke comping/bass/drum (nilai timing eksak sudah disalin, bukan dihitung
ulang ad hoc). Lanjut ke Level 6.

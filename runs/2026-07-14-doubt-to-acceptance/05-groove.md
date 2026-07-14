# 05 — Desain Ritme dan Groove (Level 5, Tahap 9)

## Feel

Swung-16th, laid-back — semua suara sedikit di belakang beat sepanjang
lagu. Diimplementasikan lewat pocket bernama `neo-soul-core` (lihat
`../../skills/midi-orchestration/references/groove-profiles.md`), dideklarasikan
di ABC final sebagai directive `%%pocket neo-soul-core` — bukan angka tick
per-not yang ditulis manual di level ini (itu tugas midi-orchestration).

## Rhythmic identity

Spacious, syncopated-tapi-jarang, tidak dense. Bagian B sedikit lebih rapat
(gap antar-frase menyempit) tapi tidak sampai "dense" — ini satu-satunya
device ritmis yang berubah di B (lihat `06-arrangement.md`/`13-dynamics.md`
untuk kenapa hanya satu dimensi yang dinaikkan).

## Elemen utama yang dipakai

- **Syncopation**: hook masuk dengan pickup 8th-rest, bukan on-the-beat.
- **Anticipation**: tidak dipakai secara eksplisit — piece ini sengaja
  menghindari nada "mendahului" downbeat karena itu memberi kesan
  forward-driving yang bertentangan dengan "doubt" yang searching, bukan
  bergerak maju.
- **Displacement**: motif hook di A1 bar 9-10 memindah posisi ritmis
  motifnya dibanding bar 5-6 (statement vs answer).
- **Rhythmic augmentation**: Outro memakai nilai nada lebih panjang
  (long tone di bar akhir) dibanding A1 — bagian dari subtraksi menuju
  "settling".
- Polyrhythm/rhythmic diminution: tidak dipakai — piece ini pendek dan
  restrained, menambahkan device ini akan melanggar prinsip "jangan
  menumpuk semua device" (lihat RED-FLAGS.md, dikutip di `06-arrangement.md`).

## Groove reference untuk turunan Level 7/8/9

- **Comping** (`07-comping.md`): sustained rootless-shell voicing, 1
  attack/bar (statis) — anchor yang TIDAK berubah supaya lift di B murni
  dari harmoni+register, bukan dari comping jadi lebih aktif.
- **Bass** (`08-bassline.md`): sparse, root + space, chromatic approach di
  transisi chord tertentu.
- **Drum** (`09-drums.json`): minimal groove masuk di A1 (kick+rimshot+hat
  gapped), naik satu notch di B (hat steady 8th + 1 open-hat accent, tanpa
  ride/cymbal wash), lalu subtraksi total di Outro.

## Gate check

Feel dan rhythmic identity ditentukan eksplisit (swung-16th laid-back,
`neo-soul-core`). Cukup spesifik untuk diturunkan langsung ke
comping/bass/drum di level 7-9 tanpa perlu menebak ulang.

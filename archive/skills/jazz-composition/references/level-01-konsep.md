# Level 1 — Konsep Artistik

LEVEL 1 — KONSEP ARTISTIK
Tujuan
Menentukan identitas dasar komposisi sebelum menulis nada.
Pertanyaan utama

* Lagu ini ingin terdengar seperti apa?
* Emosi utama apa yang ingin dibangun?
* Apakah lagu bersifat lyrical, rhythmical, angular, modal, bluesy, atau harmonically dense?
* Apakah lagu ditujukan untuk combo kecil, big band, solo piano, atau vokal?
* Seberapa kompleks tingkat harmoninya?
Keputusan utama
Gaya
Contoh:

* swing
* bebop
* hard bop
* modal jazz
* jazz ballad
* bossa nova
* jazz-funk
* contemporary jazz
* fusion
* free jazz
Karakter
Contoh:

* hangat
* gelap
* elegan
* agresif
* reflektif
* playful
* misterius
* urban
* cinematic
Energi
Tentukan arah energi lagu:

tenang → berkembang → tegang → klimaks → resolusi
Instrumentasi
Contoh combo:

Tenor saxophone
Piano
Double bass
Drum
Atau:

Vokal
Gitar
Piano
Bass
Drum
Output level ini
Sebuah brief pendek:

Judul sementara:
Gaya:
Tempo:
Birama:
Karakter:
Instrumentasi:
Tingkat kompleksitas:
Arah energi:
Contoh:

Judul sementara: Midnight Passage
Gaya: contemporary modal jazz
Tempo: 118 BPM
Birama: 4/4
Karakter: misterius dan progresif
Instrumentasi: tenor sax, piano, bass, drum
Kompleksitas: menengah
Arah energi: tenang, berkembang, intens, lalu terbuka

## Kandidat & seleksi (Level 1)

Level ini memakai protokol kandidat→seleksi (`candidate-selection-protocol.md`). Tambahan wajib pada output level ini:

- **Aesthetic thesis** — 1 kalimat ide musikal spesifik yang bisa **didengar** (bukan daftar atribut genre). Contoh: "satu nada yang awalnya terasa salah tak pernah dihilangkan; di akhir, harmoni di bawahnya berubah sehingga nada itu terasa diterima."
- **2 konsep kandidat berbeda secara struktural** ditulis sebagai material telanjang (≤1 kalimat intent per kandidat, tanpa pembelaan). Ini yang memenuhi tuntutan rubrik `vibes-mood` "minimal dua konsep berbeda secara struktural".
- Kandidat + verdict selector ditulis ke `01-konsep-candidates.md`; `01-brief.md` memakai pemenang.

## Template gaya (opsional — seed konsep, bukan pintasan)

Setelah brief mood/gaya jelas, **baca `../templates/registry.md`** (index tipis
Tier 0) dan cocokkan vibe brief dengan satu baris. Bila ada yang cocok:

- Muat **hanya** satu `../templates/<id>.json` (Tier 1) — jangan muat semua.
- Pakai untuk **menyemai** kandidat konsep/plan: `defaults` (key/tempo/meter/
  feel), `harmony_palette`, satu `hook_archetype`, `groove_profile`,
  `melody_phrasing`, `drum_skeleton`, `arrangement_defaults`, dan
  `anti_boredom_rules`.

Template adalah **starting kit, bukan lagu jadi**. Ia menyemai keputusan; ia
**tidak** melewati protokol kandidat→seleksi maupun gate/scorecard/L2 mana pun.
Protokol kandidat tetap jalan — kini memilih **di antara opsi template**
(mis. dua `hook_archetypes`, beberapa `signature_moves`), bukan dari nol.
`anti_boredom_rules` template ikut jadi checklist "tidak membosankan" yang
diverifikasi di L2/scorecard.

Bila **tidak ada** baris registry yang benar-benar cocok, **komposisi tanpa
template** dan sebut alasannya di `01-brief.md` — match paksaan lebih buruk
daripada tanpa template. Mekanisme lengkap + kontrak field: `../templates/README.md`
dan `../templates/schema.md`.

## Gate instrumentasi — registry engine (wajib)

- Instrumentasi run **WAJIB** dipilih dari registry instrumen engine
  `daw_generative` — tabel id → nama → GM program (plus 4 palet siap
  pakai) di `../../midi-orchestration/references/engine-export.md` — ATAU
  disertai justifikasi eksplisit di `01-brief.md` bila memakai GM lain
  (engine menerima GM 0-127 penuh; registry = menu default yang
  direkomendasikan, bukan pagar keras).
- Konsekuensi hilir: ABC final (Level 14 / modul `abc-notation`)
  **WAJIB** menulis `%%MIDI program N` eksplisit per voice sesuai nomor
  tabel registry — jangan mengandalkan name-matching otomatis engine
  (hanya menebak keyword `sax`/`bass`/`guitar`/`piano`, jatuh ke piano
  untuk selainnya) sebagai satu-satunya jalur penentuan timbre.

## Gate — ask, don't guess

- Jika field wajib artefak level ini belum diputuskan brief/level sebelumnya — **tanya, jangan menebak.**

## Modul pendalaman

- `../../vibes-mood/SKILL.md` — baca saat perlu menerjemahkan brief mood
  ("tenang", "misterius", "urban") menjadi keputusan gaya/tempo/karakter
  yang konkret; selain itu cukup prosedur di atas dan `../../RED-FLAGS.md`.

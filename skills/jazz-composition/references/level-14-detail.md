# Level 14 — Detail Low Level

LEVEL 14 — DETAIL LOW LEVEL
Pada tahap ini, komposisi sudah utuh secara makro. Baru kemudian turun ke detail per bar dan per beat.
Detail melodi
Periksa:

* nada target
* interval
* phrasing
* articulation
* register
* rhythmic placement
* peak note
* repetition
* variation
Detail harmony
Periksa:

* chord spelling
* extension
* alteration
* bass note
* voice leading
* avoid note
* chord-scale implication
Detail rhythm
Periksa:

* syncopation
* rest
* anticipation
* accent
* subdivision
* swing placement
* displacement
Detail voicing
Periksa:

* top note
* inner voice
* spacing
* register
* doubling
* dissonance
* resolution
Detail orchestration
Periksa:

* siapa bermain
* siapa diam
* siapa memimpin
* siapa merespons
* bagaimana transisi terjadi

## Setelah level ini — export produksi

Setelah semua gate/checklist Level 14 terpenuhi (dan checklist pra-L3 di
`../SKILL.md` §Penilaian tercentang semua), jalankan section
`## Export produksi (Tool 2 — engine daw_generative)` di `../SKILL.md`:
konversi drum (`drums_to_engine.py`) → pra-cek `conformance-audit.mjs` →
`POST /api/render` → simpan `runs/<run>/render.wav` + catat
`X-Conformance-Summary` di `scorecard.md` (status **PENDING** yang jujur
bila lingkungan tidak lengkap — run tidak dianggap gagal).

## Gate — ask, don't guess

- Jika field wajib artefak level ini belum diputuskan brief/level sebelumnya — **tanya, jangan menebak.**

## Modul pendalaman

- Tidak ada modul pendalaman khusus untuk level ini — cukup prosedur di atas dan `../../RED-FLAGS.md`.

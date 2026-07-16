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

## Artefak final Level 14 — `song.json`

Keluaran final dari level ini adalah **`song.json`**, komposisi JSON yang
dihasilkan lewat `../json-composition/SKILL.md`. Drum bukan file
terpisah — drum adalah **satu voice di dalam `song.json`** seperti voice
instrumen lain. Semua pemeriksaan di atas (detail melodi, harmony,
rhythm, voicing, orchestration) mengarah ke satu artefak ini, bukan ke
pasangan `song.abc` + `drums.json`.

**Jalur legacy (ABC):** `song.abc` + `drums.json` (via `%%MIDI drummap`
atau step-grid) masih didukung untuk run yang belum migrasi ke
`json-composition`, dan tetap diterima engine lewat body legacy
`{abc, drums?}` — tapi bukan lagi jalur default untuk run baru.

## DoD Level 14

Level ini **selesai** hanya bila:

1. `python3 ../json-composition/scripts/validate_composition.py song.json`
   lulus **0 violations**.
2. Real-output check — salah satu:
   - kirim `song.json` ke `POST /api/render` bila server dev tersedia
     (lihat `## Setelah level ini — export produksi` di bawah), atau
   - bila server tidak tersedia: verifikasi manual bar-count dan
     notes-per-voice `song.json` **konsisten dengan
     `composition-plan.json`** (jumlah bar per section, voice yang
     dijanjikan benar-benar ada isinya).

Sesuai aturan paket ini: **validate bersih ≠ render benar** — kedua
langkah wajib, bukan salah satu (lihat `CLAUDE.md` root paket §"Why these
skills exist").

## Setelah level ini — export produksi

Setelah semua gate/checklist Level 14 terpenuhi (dan checklist pra-L3 di
`../SKILL.md` §Penilaian tercentang semua), jalankan section
`## Export produksi (Tool 2 — engine daw_generative)` di `../SKILL.md`:
validasi `song.json` → pra-cek `conformance-audit.mjs` → `POST /api/render`
→ simpan `runs/<run>/render.wav` + catat header `X-Gate-Summary`
(inScalePct, floorPass, rangeWarnings — sinyal Gate A objektif dari
engine) di `scorecard.md` (status **PENDING** yang jujur bila lingkungan
tidak lengkap — run tidak dianggap gagal). Jalur legacy mencatat
`X-Conformance-Summary`.

## Gate — ask, don't guess

- Jika field wajib artefak level ini belum diputuskan brief/level sebelumnya — **tanya, jangan menebak.**

## Modul pendalaman

- `../json-composition/SKILL.md` untuk encoding `song.json` final
  (validator, kontrak field) dan `../midi-orchestration/SKILL.md` untuk
  realisasi ke MIDI/render; lihat juga `../../RED-FLAGS.md`.

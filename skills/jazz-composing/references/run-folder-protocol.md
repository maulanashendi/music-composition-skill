# Protokol Run Folder

Setiap komposisi yang dikerjakan dengan skill `jazz-composing` menulis
artefaknya ke satu **run folder** persisten, bukan ke output sekali-pakai
yang hilang setelah sesi berakhir. Ini yang membuat pekerjaan bisa
dihentikan dan dilanjutkan (resume) tanpa mengulang fase yang sudah selesai.

## Struktur folder

```
runs/<tanggal>-<slug>/
├── progress.md
├── 01-brief.md
├── 02-konsep-candidates.md   (Level 1: konsep artistik)
├── 02-konsep.md
├── 03-bentuk-candidates.md   (Level 2: arsitektur lagu)
├── 03-bentuk.md
├── 04-harmoni-candidates.md  (Level 3: peta harmoni, niat-level)
├── 04-harmoni.md
├── 05-melodi-candidates.md   (Level 4: motif/melodi, niat-level)
├── 05-melodi.md
├── 06-groove.md              (nama pattern groove dipilih)
├── 07-arrangement.md         (interaction map + gaya comping)
├── plan.json                 (artefak fase Plan — dikonsumsi plan-verifying)
├── verify-log.md             (ditulis plan-verifying — lihat skill itu)
├── output.mid / render.wav / scorecard.md  (ditulis rendering-audition)
```

Artefak `01`-`07` mengikuti urutan fase Brief → Ideation (poin 1-6, lihat
`../SKILL.md`), bukan urutan bebas — artefak level N selalu ditulis
sebelum level N+1 dimulai. `plan.json` adalah artefak fase Plan (ditulis
skill ini); `verify-log.md` dan `output.mid`/`render.wav`/`scorecard.md`
ditulis fase Verify/Audition oleh `../plan-verifying/` dan
`../rendering-audition/` ke run folder yang sama.

### Artefak `NN-<level>-candidates.md` (hanya Level 1-4)

Level 1-4 (konsep, bentuk, harmoni, melodi) memakai protokol
kandidat→seleksi (`candidate-selection-protocol.md`), jadi selain
artefak utama bernomor, tiap level itu juga menulis satu
`NN-<level>-candidates.md` (`02-konsep-`, `03-bentuk-`, `04-harmoni-`,
`05-melodi-`). File ini memuat material kandidat telanjang + verdict
selector di bagian akhirnya, mengikuti kontrak artefak ramping (7 field)
di `candidate-selection-protocol.md` — **bukan** kontrak 11-field artefak
lain. Groove (06) dan arrangement (07) **tidak** punya artefak
`-candidates.md` (single-shot, lihat `../SKILL.md`).

### Catatan khusus `05-melodi.md`

`05-melodi.md` menulis niat melodi (pitch + durasi + artikulasi per
not) hasil tahap motif/kontur/target-tone (`melody.md`) dan, bila
tension map menandai butuh tegangan tinggi, outside material
(`advanced-melody.md`) — **bukan** ABC, bukan velocity/off-grid (lihat
doktrin `../../../docs/DOCTRINE-NIAT-BUKAN-NOT.md`). File ini boleh berisi
prosa penjelasan + fragmen niat kecil untuk mendemonstrasikan motif atau
target tone tertentu; representasi final yang dipetakan ke skema hidup
di `plan.json`, bukan di sini — jangan memperlakukan `05-melodi.md`
sebagai sumber kebenaran untuk rendering, itu peran `plan.json`.

## Aturan penamaan

- `<tanggal>` = `YYYY-MM-DD`, tanggal saat run folder pertama kali dibuat
  (bukan tanggal update terakhir).
- `<slug>` = kebab-case dari judul sementara brief (Level 1, field "Judul
  sementara"). Contoh: judul sementara "Midnight Passage" → folder
  `runs/2026-07-14-midnight-passage/`.
- Sekali dibuat, nama folder tidak berubah walau judul lagu berubah di
  level lanjut — judul final dicatat di `progress.md`, bukan di-rename ke
  folder.

## Format `progress.md`

Tabel dengan kolom berikut, satu baris per level:

| Level | Status | Artefak | Next action |
|---|---|---|---|
| Brief | done | `01-brief.md` | — |
| 1 — Konsep Artistik | done | `02-konsep.md` | — |
| 2 — Arsitektur Lagu | done | `03-bentuk.md` | — |
| 3 — Peta Harmoni | in-progress | `04-harmoni.md` (draft) | Lengkapi tension map bar 5-8 |
| 4 — Desain Melodi | blocked | — | Tunggu Level 3 selesai; motif belum bisa dipatok tanpa harmonic skeleton final |
| 5 — Ritme/Groove | blocked | — | — |
| 6 — Aransemen | blocked | — | — |
| Plan (`plan.json`) | blocked | — | — |
| ... | ... | ... | ... |

Status yang valid: `done`, `in-progress`, `blocked`. Kolom "Next action"
wajib diisi untuk status selain `done` — ini yang dibaca saat resume untuk
tahu persisnya harus mulai dari mana, bukan menebak ulang dari artefak.

## Aturan resume

Sebelum mulai mengerjakan run folder yang **sudah ada**, baca
`progress.md` lebih dulu — jangan mulai dari Level 1 lagi atau menebak
level mana yang sudah selesai dari isi folder. `progress.md` adalah satu-
satunya sumber kebenaran soal status; jika `progress.md` menyatakan
"blocked" pada suatu level karena field wajib belum diputuskan, tanyakan
field itu ke user sebelum melanjutkan — jangan menebak nilainya sendiri
supaya run folder terlihat "berjalan".

Setiap kali sebuah level selesai (artefaknya lulus gerbang DoD level itu),
`progress.md` diperbarui pada baris yang sama sebelum pindah ke level
berikutnya.

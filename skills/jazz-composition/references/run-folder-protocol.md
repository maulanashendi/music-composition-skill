# Protokol Run Folder

Setiap komposisi yang dikerjakan dengan skill `jazz-composition` menulis
artefaknya ke satu **run folder** persisten, bukan ke output sekali-pakai
yang hilang setelah sesi berakhir. Ini yang membuat pekerjaan bisa
dihentikan dan dilanjutkan (resume) tanpa mengulang level yang sudah selesai.

## Struktur folder

```
runs/<tanggal>-<slug>/
├── progress.md
├── 01-brief.md
├── 02-form.md
├── 03-harmony.md
├── 04-melody.abc          (atau .md untuk artefak non-notasi)
├── 05-groove.md
├── 06-arrangement.md
├── 07-comping.md
├── 08-bassline.md
├── 09-drums.json
├── 10-solo-map.md
├── 11-transitions.md
├── 12-intro-ending.md
├── 13-dynamics.md
├── 14-review.md
├── song.abc                (artefak final)
├── drums.json               (artefak final)
├── output.mid                (artefak final)
└── scorecard.md
```

Nomor artefak `01`–`14` mengikuti urutan 14 level SOP (lihat tabel di
`../SKILL.md`), bukan urutan bebas — artefak level N selalu ditulis sebelum
level N+1 dimulai.

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
| 1 — Konsep Artistik | done | `01-brief.md` | — |
| 2 — Arsitektur Lagu | done | `02-form.md` | — |
| 3 — Peta Harmoni | in-progress | `03-harmony.md` (draft) | Lengkapi tension map bar 5-8 |
| 4 — Desain Melodi | blocked | — | Tunggu Level 3 selesai; motif belum bisa dipatok tanpa harmonic skeleton final |
| 5 — Desain Ritme dan Groove | blocked | — | — |
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

# Template `scorecard.md`

Setiap run folder (lihat `../jazz-composing/references/run-folder-protocol.md`)
memiliki satu `scorecard.md` yang mengumpulkan penilaian tiga lapis (L1
mekanis, L2 rubrik, L3 telinga) untuk fase-fase MDLC (Brief, Ideation, Plan,
Verify, Audition, Review, Release), ditulis dalam bahasa Indonesia. Salin
struktur di bawah ini persis, ganti isi placeholder `<...>` sesuai run yang
sedang dikerjakan.

## Status validasi mekanis (L1) — dari `verify-log.md`

Status validasi mekanis (L1) diambil langsung dari `verify-log.md` yang
ditulis `plan-verifying` — jangan mengulang checklist manual di sini, cukup
rujuk apakah `plan.json` lolos `pyengine validate` tanpa error (dan berapa
iterasi yang dibutuhkan, serta warning apa yang diterima sadar). Struktur/
bar count/kontiguitas/referensi section sudah dijamin oleh gerbang itu,
bukan checklist manual di scorecard.

## Format skor dan laporan

Kriteria kualitatif (L2 rubrik) memakai skala 0-2 per kriteria: 0 =
tidak ada/kontradiktif, 1 = usable dengan revisi substansial, 2 =
kuat/konsisten. Kriteria yang menilai kehadiran suatu device (mis. klimaks,
fills/setup) butuh afforansi N/A: jika device itu sengaja absen sesuai brief
(bukan lupa/tidak sengaja), isi kolom skor dengan **N/A** + satu kalimat
justifikasi kenapa device itu absen — jangan diberi skor 0, karena 0 berarti
"ada tapi gagal", bukan "sengaja tidak ada".

```markdown
# Scorecard — <judul sementara / slug run>

## Status validasi (L1 — dari verify-log.md)

- [ ] `pyengine validate` lolos tanpa error (`"valid": true`, `errors: []`)
- Jumlah iterasi sampai bersih: <n>
- Warning yang tersisa (diterima sadar + alasan): <ringkas dari verify-log.md, atau "tidak ada">

## L2 — Rubrik kualitatif (dari `rubric-checklist.md`)

Diisi oleh subagent reviewer segar tanpa konteks generasi (self-grading
dilarang). Salin tabel per domain dari `rubric-checklist.md`, isi kolom
skor + alasan untuk piece ini. Kalau tidak bisa spawn reviewer/subagent
terpisah, ikuti fallback solo-agent eksplisit di `audition-protocol.md`
§"Fallback solo-agent" — beri anotasi jujur di kolom alasan (mis.
"self-assessment, bukan reviewer segar") alih-alih diam-diam self-grade.

### Vibe/Brief

| Kriteria | Skor (0-2) | Alasan (1 kalimat) |
|---|---|---|
| ... | | |

### Harmoni

| Kriteria | Skor (0-2) | Alasan (1 kalimat) |
|---|---|---|
| ... | | |

### Melodi

| Kriteria | Skor (0-2) | Alasan (1 kalimat) |
|---|---|---|
| ... | | |

### Groove/Ritme

| Kriteria | Skor (0-2) | Alasan (1 kalimat) |
|---|---|---|
| ... | | |

### Aransemen

| Kriteria | Skor (0-2) | Alasan (1 kalimat) |
|---|---|---|
| ... | | |

### Produksi/DAW (MIDI-orchestration)

| Kriteria | Skor (0-2) | Alasan (1 kalimat) |
|---|---|---|
| ... | | |

## L2 global — kriteria blocker lintas-piece (fail-closed)

Dinilai terhadap **keseluruhan piece** (bukan per fase), oleh reviewer
segar, setelah render Audition tersedia. Empat kriteria di bawah adalah
**BLOCKER**:

| # | Kriteria blocker | Skor (0-2) | Bukti dari notasi/plan (bar spesifik) |
|---|---|---|---|
| 1 | Identitas — 4 bar pertama bisa dibedakan dari template genre | | |
| 2 | Memorability — motif bisa diingat/dinyanyikan setelah sekali baca-dengar | | |
| 3 | Interaction — instrumen terdengar saling mendengar (ada bukti call-response/ruang) | | |
| 4 | Emotional specificity — arc terasa dari plan/audio tanpa membaca brief | | |

**Semantik fail-closed**: skor **0** pada **salah satu** dari keempat
kriteria ini = run **BELUM SELESAI**, terlepas dari skor kriteria lain —
wajib revisi (kembali ke `jazz-composing`) + re-review sebelum boleh disebut
selesai. Skor tinggi di L2-rubrik per-domain **tidak menyelamatkan** blocker
yang gagal.

### L2-blind — uji buta arc emosional

Prosedur: 3 opsi arc emosional (verbatim, tanpa menandai yang benar) →
reviewer segar dengan diet informasi ketat → pilih 1 + alasan.

| Field | Isi |
|---|---|
| 3 opsi arc (verbatim, tanpa menandai yang benar) | |
| Opsi yang dipilih reviewer segar | |
| Arc sebenarnya (dari `01-brief.md`) | |
| Hasil | benar / salah |
| Alasan reviewer (apa adanya) | |

**Salah pilih** = kriteria blocker #4 (emotional specificity) otomatis
**0** — fail-closed, run belum selesai.

### L2-cliche — audit originalitas

Reviewer segar menandai match terhadap
`../jazz-composing/references/cliche-register.md`; composer merespons tiap
temuan:

| Temuan (entri register + lokasi bar) | Respons (revisi / justifikasi audible) | Detail respons |
|---|---|---|

Temuan tanpa respons = run belum selesai. Justifikasi generik ("ini
disengaja") tanpa mekanisme yang bisa didengar = tidak diterima.

## Bukti revisi (wajib sebelum run disebut selesai)

≥1 pasangan before/after untuk 2 masalah terbesar yang ditemukan
L1/L2-rubrik/L2-blind/L2-cliche:

| Temuan (sumber: L1/L2-rubrik/L2-blind/L2-cliche) | Before (kutipan plan/nilai lama) | After (kutipan baru) | Efek yang diharapkan terdengar (1 kalimat) |
|---|---|---|---|

Run tanpa satu pun revisi tercatat = red flag "first draft dianggap
final" (`../RED-FLAGS.md`).

## Audition/Release (Fase Audition — pyengine)

Diisi setelah `python -m pyengine audition <plan.json> -o <run-folder>/audition/`
dijalankan (kontrak lengkap: `references/engine-http-alternative.md` untuk
jalur HTTP alternatif):

| Field | Isi |
|---|---|
| Status | <selesai / PENDING + alasan konkret> |
| Path MIDI | <`<run-folder>/audition/<slug>.mid`> |
| Path WAV | <`<run-folder>/audition/<slug>.wav`> |
| durationSec (wall-clock render, bukan durasi lagu) | |
| Render final (fase Release) | <path `<run-folder>/release/` bila sudah dijalankan> |

## L3 (telinga) — hanya diisi sekali, di akhir

Diisi **setelah** WAV Audition ada, mengikuti `audition-protocol.md`. Skor L2
yang tinggi adalah lantai (tidak ada yang rusak/tipis), bukan langit-langit
(belum tentu enak didengar) — L3 adalah pemeriksaan wajib terakhir sebelum
piece dianggap selesai.

<isi hasil telinga di sini setelah WAV Audition tersedia>
```

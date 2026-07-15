# Template `scorecard.md`

Setiap run folder (lihat `run-folder-protocol.md`) memiliki satu
`scorecard.md` yang mengumpulkan penilaian tiga lapis (L1 mekanis, L2
rubrik, L3 telinga) untuk seluruh 14 level, ditulis dalam bahasa Indonesia.
Salin struktur di bawah ini persis, ganti isi placeholder `<...>` sesuai
run yang sedang dikerjakan.

## Validasi mesin lintas-level (dari `quality-control.md` §14 lama)

Bagian "composition plan" dari §14 (Machine-readable plans) — label
section unik, bar count/durasi chord valid, section terbuka dilabeli
eksplisit, performance order/solo form merujuk section yang benar-benar
ada, plan cocok dengan prosa dan notasi — adalah pemeriksaan **L1
mekanis**, bukan rubrik L2 subjektif, jadi tempatnya bukan di satu
`rubric.md` modul melainkan di sini, sebagai gerbang lintas-level yang
dicek tiap kali `composition-plan.json` diperbarui. Jalankan validator
kalau tersedia; kalau tidak, verifikasi checklist ini manual dan tulis di
`scorecard.md` bahwa validasinya manual — jangan diam-diam dilewati.
(Bagian "DAW plan" dari §14 sudah dipindah ke
`../../midi-orchestration/references/rubric.md`, karena itu pemeriksaan
output MIDI/DAW, bukan composition plan.)

## Format skor dan laporan (dari `quality-control.md` §17-18 lama)

Setiap `rubric.md` modul memakai skala 0-2 (bukan 0-4 seperti §17 lama)
karena granularitasnya per-kriteria, bukan per-domain — tapi prinsip
skalanya sama: 0 = tidak ada/kontradiktif, 1 = usable dengan revisi
substansial, 2 = kuat/konsisten. Kriteria yang menilai kehadiran suatu
device (mis. klimaks, fills/setup) butuh afforansi N/A: jika device itu
sengaja absen sesuai brief (bukan lupa/tidak sengaja), isi kolom skor
dengan **N/A** + satu kalimat justifikasi kenapa device itu absen —
jangan diberi skor 0, karena 0 berarti "ada tapi gagal", bukan "sengaja
tidak ada". Struktur laporan akhir §18 lama (status
validasi tiap artefak, skor musikal, isu blocking yang sudah diperbaiki,
risiko development, pilihan interpretatif yang tersisa, alternatif live,
keterbatasan renderer/format) sudah terwakili oleh gabungan L1+L2 per
level di bawah ini plus `L3 (telinga)` di akhir — tidak diduplikasi jadi
satu blok laporan terpisah.

```markdown
# Scorecard — <judul sementara / slug run>

## Level 1 — Konsep Artistik

### L1 (mekanis)

- [ ] Semua field brief wajib terisi (Judul sementara, Gaya, Tempo, Birama,
      Karakter, Instrumentasi, Kompleksitas, Arah energi)
- [ ] Tidak ada field bernilai "TBD" atau kosong

### L2 (rubrik)

Diisi oleh subagent reviewer segar tanpa konteks generasi (self-grading
dilarang).

| Kriteria | Skor (0-2) | Alasan (1 kalimat) |
|---|---|---|
| Identitas artistik jelas | | |
| Karakter/emosi konsisten dengan instrumentasi | | |
| Arah energi masuk akal untuk gaya yang dipilih | | |

## Level 2 — Arsitektur Lagu

### L1 (mekanis)

- [ ] Bentuk lagu dipilih secara eksplisit (AABA/ABAC/through-composed/blues)
- [ ] Struktur performa lengkap (intro..coda) tercantum dengan panjang bar

### L2 (rubrik)

| Kriteria | Skor (0-2) | Alasan (1 kalimat) |
|---|---|---|
| Setiap bagian punya fungsi dramaturgis | | |
| Ada kontras antar-bagian | | |
| Klimaks ditempatkan pada bagian yang tepat (jika klimaks sengaja absen sesuai brief, isi N/A + 1 kalimat justifikasi — bukan skor 0) | | |

## Level 3 — Peta Harmoni

### L1 (mekanis)

- [ ] Tonal center dan harmonic rhythm ditentukan
- [ ] Bar count skeleton konsisten dengan Level 2 (arsitektur)

### L2 (rubrik)

| Kriteria | Skor (0-2) | Alasan (1 kalimat) |
|---|---|---|
| Tension map jelas per bar | | |
| Fungsi harmonik tiap chord teridentifikasi | | |
| Chord kompleks (extension/alteration) memang diperlukan, bukan dekorasi | | |

## Level 4 — Desain Melodi

### L1 (mekanis)

- [ ] Motif inti, kontur, dan target tone ditentukan
- [ ] Bar count melodi konsisten dengan Level 3

### L2 (rubrik)

| Kriteria | Skor (0-2) | Alasan (1 kalimat) |
|---|---|---|
| Motif mudah dikenali dan dipertahankan | | |
| Target tone/guide tone terhubung logis | | |
| Outside material (jika ada) terkontrol dan diresolusikan | | |

## Level 5 — Desain Ritme dan Groove

### L1 (mekanis)

- [ ] Feel dan rhythmic identity ditentukan eksplisit

### L2 (rubrik)

| Kriteria | Skor (0-2) | Alasan (1 kalimat) |
|---|---|---|
| Placement aksen konsisten dengan feel yang dipilih | | |
| Groove reference cukup spesifik untuk diturunkan ke comping/bass/drum | | |

## Level 6 — Aransemen Instrumen

### L1 (mekanis)

- [ ] Orchestration map mencakup semua bagian dari Level 2

### L2 (rubrik)

| Kriteria | Skor (0-2) | Alasan (1 kalimat) |
|---|---|---|
| Setiap instrumen punya peran per bagian | | |
| Density berubah antar-bagian (bukan semua instrumen penuh terus) | | |

## Level 7 — Desain Comping dan Voicing

### L1 (mekanis)

- [ ] Comping chart mencakup semua bagian yang butuh comping

### L2 (rubrik)

| Kriteria | Skor (0-2) | Alasan (1 kalimat) |
|---|---|---|
| Voice leading antar-chord halus | | |
| Comping bergerak (bukan block chord statis) | | |

## Level 8 — Desain Bass Line

### L1 (mekanis)

- [ ] Bass concept ditentukan untuk setiap section

### L2 (rubrik)

| Kriteria | Skor (0-2) | Alasan (1 kalimat) |
|---|---|---|
| Bass punya kontur (bukan selalu root) | | |
| Approach note ke chord berikutnya masuk akal | | |

## Level 9 — Desain Drum

### L1 (mekanis)

- [ ] Bar count drum roadmap/grid sama persis dengan ABC section demi section

### L2 (rubrik)

| Kriteria | Skor (0-2) | Alasan (1 kalimat) |
|---|---|---|
| Dinamika drum mengikuti struktur lagu | | |
| Fills/setup ditempatkan pada transisi yang logis (jika fills/setup sengaja absen sesuai brief, isi N/A + 1 kalimat justifikasi — bukan skor 0) | | |

## Level 10 — Desain Improvisasi

### L1 (mekanis)

- [ ] Solo map mencantumkan jumlah chorus per solois — atau, untuk piece
      tanpa solo section: micro-improvisation map terisi lengkap (5 field,
      lihat `level-10-improvisasi.md`)

### L2 (rubrik)

| Kriteria | Skor (0-2) | Alasan (1 kalimat) |
|---|---|---|
| Solo section punya arah perkembangan (bukan datar) | | |
| Background figure (jika ada) mendukung, bukan mengganggu | | |

## Level 11 — Interlude, Shout Chorus, dan Transisi

### L1 (mekanis)

- [ ] Bagian transisi tertulis eksplisit, bukan diasumsikan

### L2 (rubrik)

| Kriteria | Skor (0-2) | Alasan (1 kalimat) |
|---|---|---|
| Shout chorus terasa sebagai klimaks | | |
| Transisi tidak terasa tiba-tiba/janggal | | |

## Level 12 — Intro dan Ending

### L1 (mekanis)

- [ ] Intro dan ending punya identitas materi sendiri (bukan placeholder)

### L2 (rubrik)

| Kriteria | Skor (0-2) | Alasan (1 kalimat) |
|---|---|---|
| Intro memperkenalkan dunia lagu | | |
| Ending berhubungan dengan motif utama | | |

## Level 13 — Dinamika dan Dramaturgi

### L1 (mekanis)

- [ ] Peta dinamika observabel tercantum per section (tabel metrik +
      micro-apex terisi) — bukan persentase (lihat
      `level-13-dinamika-dramaturgi.md`)

### L2 (rubrik)

| Kriteria | Skor (0-2) | Alasan (1 kalimat) |
|---|---|---|
| Kurva energi masuk akal untuk arc lagu | | |
| Parameter dinamika bervariasi (bukan hanya volume) | | |

## Level 14 — Detail Low Level

### L1 (mekanis)

- [ ] `validate_abc.py` lulus tanpa error
- [ ] `output.mid`: jumlah track, notes-per-track > 0 untuk semua voice, dan
      tag tempo/meter cocok dengan ABC — diperiksa langsung dari MIDI,
      bukan hanya dari status exit validator (lihat `RED-FLAGS.md`)

### L2 (rubrik)

| Kriteria | Skor (0-2) | Alasan (1 kalimat) |
|---|---|---|
| Voice leading halus di level not | | |
| Register seimbang antar-instrumen | | |
| Voicing tidak terlalu padat | | |
| Ending terasa selesai | | |

## L2 global — kriteria blocker lintas-level (fail-closed)

Dinilai terhadap **keseluruhan piece** (bukan per level), oleh reviewer
segar, setelah Level 14 selesai. Empat kriteria di bawah adalah
**BLOCKER**:

| # | Kriteria blocker | Skor (0-2) | Bukti dari notasi (bar spesifik) |
|---|---|---|---|
| 1 | Identitas — 4 bar pertama bisa dibedakan dari template genre | | |
| 2 | Memorability — motif bisa diingat/dinyanyikan setelah sekali baca-dengar | | |
| 3 | Interaction — instrumen terdengar saling mendengar (ada bukti call-response/ruang) | | |
| 4 | Emotional specificity — arc terasa dari notasi tanpa membaca brief | | |

**Semantik fail-closed**: skor **0** pada **salah satu** dari keempat
kriteria ini = run **BELUM SELESAI**, terlepas dari skor kriteria lain —
wajib revisi + re-review sebelum boleh disebut selesai. Skor tinggi di
L2-rubrik per-level **tidak menyelamatkan** blocker yang gagal.

### L2-blind — uji buta arc emosional

Prosedur lengkap di `SKILL.md` §Penilaian (3 opsi arc → reviewer segar
dengan diet informasi ketat → pilih 1 + alasan). Catat di sini, jujur:

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

Reviewer segar menandai match terhadap `cliche-register.md`; composer
merespons tiap temuan (prosedur di `SKILL.md` §Penilaian):

| Temuan (entri register + lokasi bar) | Respons (revisi / justifikasi audible) | Detail respons |
|---|---|---|

Temuan tanpa respons = run belum selesai. Justifikasi generik ("ini
disengaja") tanpa mekanisme yang bisa didengar = tidak diterima.

## Bukti revisi (wajib sebelum run disebut selesai)

≥1 pasangan before/after untuk 2 masalah terbesar yang ditemukan
L1/L2-rubrik/L2-blind/L2-cliche (lihat `SKILL.md` Tahap 15):

| Temuan (sumber: L1/L2-rubrik/L2-blind/L2-cliche) | Before (kutipan notasi/nilai lama) | After (kutipan baru) | Efek yang diharapkan terdengar (1 kalimat) |
|---|---|---|---|

Run tanpa satu pun revisi tercatat = red flag "first draft dianggap
final" (`RED-FLAGS.md`).

## Export (Tool 2 — engine daw_generative)

Diisi setelah section `## Export produksi` di `SKILL.md` dijalankan
(kontrak lengkap: `midi-orchestration/references/engine-export.md`):

| Field | Isi |
|---|---|
| Status | <selesai / PENDING + alasan konkret> |
| Path | <`runs/<run>/render.wav` bila ada> |
| Conformance summary | <isi header `X-Conformance-Summary` apa adanya> |
| Mastering | <profil yang dipakai: `neo-soul` / `legacy` / `false`> |

## L3 (telinga) — hanya diisi sekali, di akhir

Diisi **setelah** `output.mid` ada, mengikuti
`human-ear-protocol.md`. Skor L2 yang tinggi adalah lantai
(tidak ada yang rusak/tipis), bukan langit-langit (belum tentu enak
didengar) — L3 adalah pemeriksaan wajib terakhir sebelum piece dianggap
selesai.

<isi hasil telinga di sini setelah output.mid tersedia>
```

# Template `scorecard.md`

Setiap run folder (lihat `run-folder-protocol.md`) memiliki satu
`scorecard.md` yang mengumpulkan penilaian tiga lapis (L1 mekanis, L2
rubrik, L3 telinga) untuk seluruh 14 level, ditulis dalam bahasa Indonesia.
Salin struktur di bawah ini persis, ganti isi placeholder `<...>` sesuai
run yang sedang dikerjakan.

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
| Klimaks ditempatkan pada bagian yang tepat | | |

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
| Fills/setup ditempatkan pada transisi yang logis | | |

## Level 10 — Desain Improvisasi

### L1 (mekanis)

- [ ] Solo map mencantumkan jumlah chorus per solois

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

- [ ] Energy curve tercantum per section dengan angka/persentase

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

## L3 (telinga) — hanya diisi sekali, di akhir

Diisi **setelah** `output.mid` ada, mengikuti
`../../../tests/human-ear-protocol.md`. Skor L2 yang tinggi adalah lantai
(tidak ada yang rusak/tipis), bukan langit-langit (belum tentu enak
didengar) — L3 adalah pemeriksaan wajib terakhir sebelum piece dianggap
selesai.

<isi hasil telinga di sini setelah output.mid tersedia>
```

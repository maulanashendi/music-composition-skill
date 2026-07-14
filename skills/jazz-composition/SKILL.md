---
name: jazz-composition
description: The single entry point for making music with this package — greet any request to compose, write, arrange, or start a song or instrumental track, figure out where the person already is, and run the full SOP 14-level jazz composition pipeline yourself (not just routing to other skills — this skill IS the pipeline, from artistic concept down to note-level detail and DAW-ready MIDI). Use FIRST whenever someone wants to build a piece end-to-end, asks "how do I make this tune," "what's the process," "help me start a track," "arrange this," or hands over a mood, scene, brief, chord progression, composition-plan.json, or ABC without saying which step they want. Holds the big-picture map of how a composition is built layer by layer, and drills down into eight companion modules (harmony, melody-design, advanced-melody, vibes-mood, groove-rhythm, arrangement, abc-notation, midi-orchestration) for depth per level. Writes numbered artefacts to a persistent runs/ folder with per-level DoD gates and a three-layer scorecard (mechanical, rubric, ear).
---

# Jazz Composition — orchestrator

Skill ini adalah **satu-satunya entry point** untuk membuat musik dengan
paket ini. Sebelumnya ada skill terpisah khusus untuk "routing"
(`composition-gateway`) yang tidak pernah menulis nada sendiri; peran itu
sekarang **diserap di sini** — skill ini bukan hanya menunjuk arah, tapi
**menjalankan seluruh pipeline SOP 14-level**, dari konsep artistik sampai
detail low level, dan menghasilkan artefak run-folder yang bisa dilanjutkan
ke arranger/MIDI.

Delapan modul pendalaman (`harmony`, `melody-design`, `advanced-melody`,
`vibes-mood`, `groove-rhythm`, `arrangement`, `abc-notation`,
`midi-orchestration`) dipanggil **per level, sesuai kebutuhan** — bukan
dijalankan sebagai pipeline linear terpisah. Skill ini yang memutuskan
kapan sebuah level butuh pendalaman modul tertentu.

## Aturan dasar yang berlaku di semua level

- Jika field wajib belum diputuskan — key, tempo, meter, chord, bentuk,
  atau apakah plan/level sebelumnya sudah "locked" — **tanya, jangan
  menebak.** Ini aturan yang paling sering dilanggar; lihat
  `../RED-FLAGS.md` untuk pola kegagalannya.
- Level berikutnya **tidak boleh mulai** tanpa artefak level sebelumnya
  memenuhi DoD-nya (field wajib terisi + bar count konsisten dengan
  artefak hulu). Ini gerbang anti-halu di titik handoff antar-level.
- Setiap generate menulis artefak bernomor ke run folder — lihat
  `## Run folder` di bawah — bukan output sekali-pakai yang hilang antar
  sesi.

## Gambaran besar — 10 lapisan

Komposisi jazz sebaiknya tidak dimulai dari memilih chord secara acak lalu
menambahkan melodi di atasnya. Proses yang lebih kuat membangun lagu dalam
beberapa lapisan, dari arah besar ke detail kecil:

1. Konsep artistik
2. Arsitektur lagu
3. Peta harmoni
4. Desain melodi
5. Desain ritme dan groove
6. Aransemen instrumen
7. Ruang improvisasi
8. Dinamika dan dramaturgi
9. Detail voicing dan orchestration
10. Evaluasi dan revisi

Setiap lapisan menjawab pertanyaan yang berbeda. Level tinggi menentukan
arah lagu; level rendah menentukan bagaimana setiap nada, chord, aksen, dan
tekstur bekerja. Paket ini memecah kesepuluh lapisan ini menjadi **14 level
kerja konkret** (lihat tabel di bawah) plus workflow 15-tahap yang
mengeksekusinya secara berurutan.

## 14 level → referensi → modul pendalaman

| Level | Referensi | Modul pendalaman |
|---|---|---|
| 1 — Konsep Artistik | `references/level-01-konsep.md` | — |
| 2 — Arsitektur Lagu | `references/level-02-arsitektur.md` | — |
| 3 — Peta Harmoni | `references/level-03-harmoni.md` | `../harmony/SKILL.md` |
| 4 — Desain Melodi | `references/level-04-melodi.md` | `../melody-design/SKILL.md`, `../advanced-melody/SKILL.md` (tahap 7-8) |
| 5 — Desain Ritme dan Groove | `references/level-05-ritme-groove.md` | `../groove-rhythm/SKILL.md` |
| 6 — Aransemen Instrumen | `references/level-06-aransemen.md` | `../arrangement/SKILL.md` |
| 7 — Desain Comping dan Voicing | `references/level-07-comping-voicing.md` | `../arrangement/SKILL.md` |
| 8 — Desain Bass Line | `references/level-08-bass.md` | `../groove-rhythm/SKILL.md` |
| 9 — Desain Drum | `references/level-09-drum.md` | `../groove-rhythm/SKILL.md` |
| 10 — Desain Improvisasi | `references/level-10-improvisasi.md` | — |
| 11 — Interlude, Shout Chorus, dan Transisi | `references/level-11-interlude-shout-transisi.md` | `../arrangement/SKILL.md` |
| 12 — Intro dan Ending | `references/level-12-intro-ending.md` | `../arrangement/SKILL.md` |
| 13 — Dinamika dan Dramaturgi | `references/level-13-dinamika-dramaturgi.md` | `../arrangement/SKILL.md` |
| 14 — Detail Low Level | `references/level-14-detail.md` | — (ABC/MIDI encoding: `../abc-notation/SKILL.md`, `../midi-orchestration/SKILL.md`) |

Modul `vibes-mood/SKILL.md` tidak terikat satu level saja — dipakai untuk
menerjemahkan mood/vibe mentah dari brief (Level 1) ke parameter musik
konkret yang dipakai di seluruh level lain; panggil kapan pun brief hanya
berupa mood/scene tanpa keputusan musik.

## Workflow praktis dari nol (Tahap 1–15)

Setiap tahap dianotasi dengan artefak run-folder yang harus dihasilkan
(lihat `## Run folder`). Beberapa tahap berbagi satu artefak karena
levelnya sama (mis. Tahap 5–8 semuanya bagian dari desain melodi,
`04-melody.abc`). `04-melody.abc` adalah **artefak catatan desain**
(prosa + fragmen ABC ilustratif boleh, tidak wajib satu tune valid) —
melodi final yang tervalidasi hidup di `song.abc`; lihat catatan detail
di `references/run-folder-protocol.md`.

**Tahap 1 — Buat brief** → artefak `01-brief.md`

Gaya:
Mood:
Tempo:
Form:
Instrumentasi:
Referensi karakter:

**Tahap 2 — Buat form kosong** → artefak `02-form.md`

Intro 8 bar
A1 8 bar
A2 8 bar
B 8 bar
A3 8 bar
Solo section
Shout chorus
Head out
Coda

**Tahap 3 — Isi harmonic skeleton** → artefak `03-harmony.md`
Gunakan chord sederhana terlebih dahulu.

| Dm7 | G7 | Cmaj7 | A7 |

**Tahap 4 — Buat tension map** → artefak `03-harmony.md` (bagian tension map, sama artefak dengan Tahap 3)
Tentukan bagian stabil, tegang, outside, dan resolved.

**Tahap 5 — Buat motif** → artefak `04-melody.abc`
Gunakan satu identitas interval dan satu identitas ritmis.

**Tahap 6 — Tentukan target tones** → artefak `04-melody.abc`
Hubungkan guide tones antar-chord.

**Tahap 7 — Bangun melodi** → artefak `04-melody.abc`
Gunakan:

* interval
* broken chord
* passing tone
* enclosure
* chromaticism
* space
* repetition

**Tahap 8 — Tambahkan outside material** → artefak `04-melody.abc`
Letakkan pada area tension tinggi.

**Tahap 9 — Rancang groove** → artefak `05-groove.md` (mencakup feel, bass motion untuk `08-bassline.md`, dan karakter drum untuk `09-drums.json`)
Tentukan feel, bass motion, dan karakter drum.

**Tahap 10 — Rancang comping** → artefak `07-comping.md`
Gunakan voicing bergerak dan ritme interaktif.

**Tahap 11 — Buat arrangement map** → artefak `06-arrangement.md`
Tentukan siapa memainkan apa pada setiap section.

**Tahap 12 — Rancang solo form** → artefak `10-solo-map.md`
Tentukan jumlah chorus, background figure, dan klimaks.

**Tahap 13 — Buat intro, interlude, dan coda** → artefak `11-transitions.md` dan `12-intro-ending.md`
Pastikan semuanya berkaitan dengan identitas lagu.

**Tahap 14 — Review keseluruhan** → artefak `13-dynamics.md` (energy curve/dramaturgi dicek di sini sebelum turun ke detail nada)
Dengarkan bentuk besar sebelum memperbaiki detail nada.

**Tahap 15 — Revisi low level** → artefak `14-review.md`
Perbaiki:

* voice leading
* interval
* phrasing
* density
* voicing
* bass line
* drum setup
* articulation

## Checklist final

Konsep

* Apakah lagu memiliki identitas?
* Apakah karakter emosinya jelas?
* Apakah gaya dan instrumentasi sesuai?

Form

* Apakah setiap bagian memiliki fungsi?
* Apakah ada kontras?
* Apakah klimaks berada di tempat yang tepat?

Harmoni

* Apakah chord memiliki arah?
* Apakah tension dan resolution jelas?
* Apakah chord kompleks memang diperlukan?

Melodi

* Apakah motif mudah dikenali?
* Apakah interval memiliki karakter?
* Apakah broken chord terasa melodis?
* Apakah outside material terkontrol?
* Apakah nada target terdengar jelas?

Ritme

* Apakah melodi memiliki ruang?
* Apakah syncopation terasa natural?
* Apakah motif ritmis konsisten?

Aransemen

* Apakah semua instrumen memiliki fungsi?
* Apakah tekstur berubah?
* Apakah ada terlalu banyak instrumen bermain bersamaan?

Improvisasi

* Apakah solo section memiliki arah?
* Apakah pemain memiliki ruang?
* Apakah ada perkembangan menuju klimaks?

Detail

* Apakah voice leading halus?
* Apakah register seimbang?
* Apakah voicing terlalu padat?
* Apakah ending terasa selesai?

## Run folder

Semua artefak di atas ditulis ke `runs/<tanggal>-<slug>/` — struktur folder
lengkap, format `progress.md`, dan aturan resume ada di
`references/run-folder-protocol.md`. Baca file itu sebelum membuat run
folder baru atau melanjutkan run folder yang sudah ada.

## Penilaian

Setiap run folder punya satu `scorecard.md` berisi penilaian tiga lapis
(L1 mekanis, L2 rubrik oleh reviewer segar, L3 telinga manusia di akhir).
Template lengkap dan aturan pengisiannya ada di
`references/scorecard-template.md`.

## Reviewer segar (L2)

Rubrik L2 tiap level (lihat tabel `| Kriteria | Skor (0-2) | Alasan |` di
`references/scorecard-template.md`) **wajib** diisi oleh subagent yang
**baru** — tanpa histori percakapan generasi artefak yang sedang dinilai.
Self-grading oleh agent/percakapan yang sama yang membuat artefak itu
**dilarang**: agent yang baru saja menulis `04-melody.abc` tidak boleh
juga yang mengisi skor rubriknya sendiri.

Alur konkret:

1. Setelah artefak level tertentu selesai (mis. `03-harmony.md`), spawn
   subagent baru khusus review — jangan lanjutkan di agent/context yang
   sama.
2. Beri subagent itu **hanya** dua hal: artefak yang mau dinilai, dan
   `rubric.md` modul yang relevan (mis. Level 3 →
   `../harmony/references/rubric.md`; Level 5/8/9 →
   `../groove-rhythm/references/rubric.md`; Level 4 →
   `../melody-design/references/rubric.md` dan/atau
   `../advanced-melody/references/rubric.md`; Level 1 → `vibes-mood`;
   Level 2/6/7/10/11/12/13 → `arrangement`; Level 14 → `abc-notation`
   dan/atau `midi-orchestration` — lihat tabel "14 level" di atas untuk
   pemetaan level-ke-modul lengkap). Jangan beri histori percakapan
   generasi, brief asli di luar yang tertulis di artefak, atau alasan di
   balik keputusan desain — reviewer harus menilai apa yang benar-benar
   ada di artefak, bukan apa yang dimaksud.
3. Subagent mengisi tabel skor (0-2) + alasan 1 kalimat per kriteria dari
   `rubric.md` yang diberikan, lalu **menulis hasilnya langsung ke bagian
   L2 di `scorecard.md`** run folder yang bersangkutan — bukan melaporkan
   balik lewat chat untuk ditranskrip manual.
4. Skor rubrik tinggi tetap lantai, bukan langit-langit — lanjut ke
   `RED-FLAGS.md` dan (untuk `output.mid` final) L3 telinga manusia di
   `references/human-ear-protocol.md` sebelum piece dianggap selesai.

## Sebelum menganggap sebuah piece selesai

Baca `../RED-FLAGS.md` — kumpulan pola "alasan yang terdengar masuk
akal, tapi realitanya tidak" yang sudah terbukti muncul berulang di paket
ini (dari section yang di-stack semua device sampai skor rubrik tinggi
yang dikira berarti enak didengar). Skor rubrik tinggi adalah lantai,
bukan langit-langit — L3 (telinga) tetap wajib sebelum menyebut sebuah
piece selesai.

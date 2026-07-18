---
name: jazz-composing
description: Turn a brief, mood, or scene into a decided musical idea and encode it as plan.json (schemaVersion 2) — the fase Brief, Ideation, dan Plan dari Music Development Life Cycle (MDLC). Use this first whenever someone wants to compose, write, arrange, or start a jazz/neo-soul/chill-jazz piece, hands over a vibe/mood/scene without saying which MDLC phase they're in, or has a locked idea (chords, form, melody) that needs to become plan.json. This skill writes musical intent only — chord symbols, comping style+density, bass chord-tone-stack position, per-note melody pitch/duration/articulation, named groove-pattern references — never voicing pitches, velocity, off-grid timing, or humanization (that is pyengine's job downstream, see plan-verifying and rendering-audition). Genre-first: neo-soul/chill-jazz.
---

# Jazz Composing — Brief, Ideation, Plan

Skill ini adalah entry point untuk **tiga fase pertama MDLC**
(`docs/new-prd.md` §6 di repo `daw_generative`): **Brief** (gali maksud),
**Ideation** (baca knowledge base craft → pilih vibe, form, progresi,
groove, instrumentasi), **Plan** (tulis `plan.json`). Fase-fase
setelahnya — Verify, Audition, Review, Release, Remix — adalah tanggung
jawab `../plan-verifying/SKILL.md` dan `../rendering-audition/SKILL.md`.

## Doktrin: niat, bukan not

**Baca `../../docs/DOCTRINE-NIAT-BUKAN-NOT.md` sebelum menulis
`plan.json` apapun.** Ringkasnya: harmoni = simbol chord, comping =
gaya+density, bass = posisi stack chord-tone (root-3-5-7-9-11-13, field
`degree` — lihat catatan di bawah), melodi = pitch+durasi(+artikulasi)
per not TANPA velocity/off-grid, drum = nama pattern dari groove
library, feel/humanization = tidak ditulis sama sekali (milik
`pyengine`, deterministik ber-`seed`). Skill ini **tidak pernah**
menulis angka waktu absolut, velocity per-not, atau voicing pitch
literal untuk voice `chords`. Kalau kamu merasa perlu menulis salah
satu dari itu, berhenti — itu tanda kamu sedang bekerja di level yang
salah.

> **Koreksi istilah bass**: field `bass.notes[].degree` di `plan.json`
> **bukan** scale degree (posisi di tangga nada terhadap tonal center),
> melainkan **posisi bass di stack chord-tone saat itu** — `1` = root,
> `3` = third, `5` = fifth, `7` = seventh, dst. sampai `13`, dihitung
> dari chord/harmony yang berlaku di bar itu (lihat contoh
> `pyengine/examples/plan-neo-soul-8bar.json`: `degree: 1` = root chord
> berjalan, `degree: 5` = fifth chord berjalan). Pastikan `degree` yang
> ditulis valid untuk chord-tone chord aktif di bar/beat tersebut —
> cek `contract.md` untuk bound pastinya.

## Aturan dasar (berlaku semua fase di skill ini)

- Field wajib belum diputuskan (key, tempo, meter, vibe, bentuk) —
  **tanya, jangan menebak.** Lihat `../RED-FLAGS.md`.
- Fase berikutnya tidak mulai tanpa fase sebelumnya "locked" — Ideation
  tidak mulai tanpa Brief disetujui; Plan tidak mulai tanpa Ideation
  punya vibe/form/progresi/groove/instrumentasi yang konkret.
- Setiap fase menulis artefak bernomor ke run folder persisten — lihat
  `references/run-folder-protocol.md` — bukan output sekali-pakai.
- Level 1-4 lama (konsep, bentuk, harmoni, melodi) memakai protokol
  **kandidat→seleksi**, bukan generate-then-defend — lihat
  `references/candidate-selection-protocol.md`. Level lain di fase ini
  (instrumentasi, groove) single-shot.
- Kaidah baru masuk knowledge base HANYA dari temuan uji dengar (fase
  Review, dipegang `rendering-audition`) — jangan menambah aturan teori
  generik yang tidak berasal dari piece nyata yang pernah dinilai.

## Workflow

### Fase 1 — Brief

Gali: vibe/mood, durasi target, referensi rasa (artis/track pembanding
kalau ada), instrumentasi kasar. Tulis `01-brief.md` ke run folder. Kalau
brief hanya kata sifat mood ("tenang", "urban") tanpa detail konkret,
baca `references/vibe-technique-map.md` untuk mengusulkan
gaya/karakter/energi — **konfirmasikan ke user, jangan menebak diam-diam.**

### Fase 2 — Ideation

Dengan brief terkunci, putuskan (pakai protokol kandidat→seleksi untuk
Level 1-2 di bawah):

1. **Konsep artistik** — aesthetic thesis 1 kalimat yang bisa **didengar**
   (bukan daftar atribut genre) + 2 kandidat berbeda struktural.
2. **Bentuk/arsitektur lagu** — Intro–Head–Solos–Head Out–Outro atau
   variannya; ≥2 alternatif bentuk sebelum memilih. Baca
   `references/structure.md`.
3. **Peta harmoni** (niat-level, simbol chord saja) — baca
   `references/harmony.md`. Progresi utama + 1 alternatif lebih
   sederhana + 1 lebih berani, exact chord symbols per bar.
4. **Desain melodi** (niat-level, pitch+durasi saja) — baca
   `references/melody.md` untuk motif/kontur/target-tone (tahap 1-6),
   `references/advanced-melody.md` untuk outside material (tahap 7-8,
   hanya bar yang tension map menandai butuh tegangan tinggi). Kalau
   interaction map (poin 6) menandai peran answer/dialog, baca juga
   `references/call-and-response.md` untuk resep phrase-level.
5. **Ritme/groove** (niat-level, nama pattern saja) — baca
   `references/groove-vocabulary.md`. Pilih nama pattern dari groove
   library `pyengine` (lihat `contract.md` untuk daftar nama valid —
   groove terimplementasi saat ini: `neo-soul-core`); jangan menulis
   tick offset atau swing ratio numerik sendiri.
6. **Aransemen/instrumentasi** — baca `references/arrangement.md` untuk
   interaction map (siapa lead/support/answer/silent per section) dan
   comping/voicing **gaya** (bukan voicing pitch — lihat
   `references/harmony.md` §"Yang TIDAK ditulis di sini"). Kalau ada
   peran answer/dialog di peta, baca `references/call-and-response.md`
   untuk resep phrase-level + pemetaan `plan.json`.

Tulis kandidat Level 1-4 ke `NN-<level>-candidates.md` per
`references/candidate-selection-protocol.md`; keputusan final tiap
tahap ke artefak bernomor di run folder.

### Fase 3 — Plan

Tulis `plan.json` (schemaVersion 2). **Baca `references/contract.md`
lebih dulu** — itu satu-satunya sumber kebenaran field/enum/bounds skema,
dihasilkan `python -m pyengine gen-context -o skills/jazz-composing/references/`.
Kalau `contract.md` belum ada atau terasa usang, jalankan ulang perintah
itu sebelum menulis — jangan menebak skema dari ingatan atau dari versi
lama plan lain.

Petakan keputusan Ideation ke field `plan.json`:
- `meta.title`/`vibe`/`key`/`seed` dari Fase 1-2.
- `sections[]` dari bentuk/arsitektur (Fase 2 poin 2).
- Harmoni tiap section = simbol chord per bar/beat (Fase 2 poin 3),
  ditulis persis sesuai field harmony di `contract.md`.
- Melodi = pitch+durasi(+artikulasi) per not (Fase 2 poin 4), TANPA
  velocity/off-grid.
- Comping = gaya+density (Fase 2 poin 6, bukan voicing pitch).
- Bass = posisi stack chord-tone (`degree`: 1/3/5/7/9/11/13) per
  bar/beat terhadap chord yang berlaku — **bukan** scale degree,
  bukan pitch oktaf konkret (lihat catatan koreksi istilah di atas).
- Drum = nama pattern groove (Fase 2 poin 5, bukan grid/hit konkret).
- `grooves`/`meta.seed` sesuai `contract.md` — jangan menambahkan field
  yang tidak ada di `contract.md`.

Setelah `plan.json` ditulis, serahkan ke `../plan-verifying/SKILL.md`
untuk fase Verify — skill ini **tidak** menjalankan `pyengine validate`
sendiri, supaya loop validasi (baca error → perbaiki → ulang) punya satu
pemilik jelas.

## Run folder

Lihat `references/run-folder-protocol.md` untuk struktur lengkap dan
aturan resume. Skill ini menulis sampai `plan.json` (artefak fase Plan);
`../plan-verifying/` menambah catatan verify ke folder yang sama;
`../rendering-audition/` menambah `.mid`/`.wav`/`scorecard.md`.

## References

- `references/contract.md` — **GENERATED**, jangan edit manual. Field
  contract `plan.json` schemaVersion 2 lengkap (skema, enum, bounds,
  nama pattern groove valid). Regenerate: `python -m pyengine gen-context -o skills/jazz-composing/references/`.
- `references/vibe-technique-map.md` — tabel vibe → teknik → field skema
  (3 kolom): brief mood → keputusan craft konkret → field `plan.json`
  mana yang diisi.
- `references/foundation-neo-soul.md` — genre foundation neo-soul/chill-jazz.
- `references/mood-to-parameter.md` — 9 modul teori penalaran mood→parameter.
- `references/style-cheatsheets.md` — cheatsheet gaya per referensi rasa.
- `references/harmony.md` — chord-scale, ii-V-I, ekstensi/altered, reharmonisasi (niat-level).
- `references/melody.md` — motif, kontur, target tone, broken chord (niat-level).
- `references/advanced-melody.md` — chromatic vocabulary/outside playing (niat-level, gated oleh tension map).
- `references/rhythm-groove.md`, `references/groove-vocabulary.md`, `references/groove-meter.md` — ritme, sinkopasi, nama pattern groove, meter/swing/clave.
- `references/structure.md`, `references/loop-development.md` — bentuk lagu, dramaturgi, variasi antar-loop.
- `references/arrangement.md` — interaction map, comping style (bukan voicing), ensemble interaction.
- `references/call-and-response.md` — resep phrase-level dialog antar-voice (caller/responder, non-overlap, transformasi motif) + pemetaan `plan.json`.
- `references/run-folder-protocol.md` — struktur run folder + aturan resume.
- `references/candidate-selection-protocol.md` — protokol kandidat→seleksi Level 1-4.
- `references/cliche-register.md` — register cliché neo-soul/AI-jazz + jalur reinterpretasi.
- `../RED-FLAGS.md` — pola kegagalan umum lintas skill.

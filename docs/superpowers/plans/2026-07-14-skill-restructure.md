# Plan: Restrukturisasi music-composition-skill ke `skills/`

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (- [ ]) syntax for tracking.

## Goal

Restrukturisasi 4 skill root (`composition-gateway`, `jazz-idea-generator`,
`abc-notation-writer`, `abc-to-midi-orchestration`) menjadi satu folder
installable `skills/` berisi 9 skill (1 orchestrator + 8 modul), dengan run
folder persisten, gerbang DoD per level, dan penilaian 3 lapis, sesuai
`docs/superpowers/specs/2026-07-14-skill-restructure-design.md`.

## Architecture

`skills/jazz-composition/` menjadi satu-satunya orchestrator: `SKILL.md`-nya
berisi SOP 14-level dipadatkan + workflow 15-tahap + CHECKLIST FINAL, dengan
detail per level di `references/level-01-*.md` … `level-14-*.md` (progressive
disclosure — dibaca hanya saat level itu dikerjakan). Delapan modul
(`harmony`, `melody-design`, `advanced-melody`, `vibes-mood`,
`groove-rhythm`, `arrangement`, `abc-notation`, `midi-orchestration`)
dipanggil oleh main skill per level untuk pendalaman, bukan pipeline
linear seperti tiga skill lama. Setiap generate menulis artefak bernomor ke
`runs/<tanggal>-<slug>/` dengan `progress.md` sebagai sumber resume dan
`scorecard.md` sebagai hasil penilaian L1 (mekanis)/L2 (rubrik subagent
segar)/L3 (telinga manusia, hanya di final).

## Tech Stack

Markdown (Agent Skills format: frontmatter `name`/`description` + body),
Python 3 (script existing: `validate_abc.py`, `abc_to_midi.py`,
`grid_to_midi.py` — dipindah tanpa diubah logikanya), JSON (composition
plan, drum grid, scorecard), git (untuk `git mv` demi menjaga histori file).

## Global Constraints

- **Struktur folder**: semua skill baru hidup di `skills/<nama>/SKILL.md`.
  9 nama final: `jazz-composition` (orchestrator), `harmony`,
  `melody-design`, `advanced-melody`, `vibes-mood`, `groove-rhythm`,
  `arrangement`, `abc-notation`, `midi-orchestration`.
- **Instalasi**: tetap operasi filesystem murni — copy atau symlink folder
  `skills/` ke `.claude/skills/` project lain. Tidak ada installer script,
  tidak ada format plugin.
- **Konvensi run folder**: `runs/<tanggal>-<slug>/` (mis.
  `runs/2026-07-14-midnight-passage/`), berisi:
  - `progress.md` — status per level (`done`/`in-progress`/`blocked`) + next
    action.
  - Artefak DoD bernomor urut mengikuti urutan level:
    `01-brief.md`, `02-form.md`, `03-harmony.md`, `04-melody.abc` (atau
    `.md` untuk artefak non-notasi), `05-groove.md`, `06-arrangement.md`,
    `07-comping.md`, `08-bassline.md`, `09-drums.json`, `10-solo-map.md`,
    `11-transitions.md`, `12-intro-ending.md`, `13-dynamics.md`,
    `14-review.md`.
  - Artefak final: `song.abc`, `drums.json`, `output.mid`.
  - `scorecard.md` — hasil L1 + L2 (+ L3 di final) seragam lintas run.
- **Gerbang DoD antar level**: level berikutnya tidak boleh mulai tanpa
  artefak hulu memenuhi DoD-nya (field wajib + konsistensi bar count dengan
  artefak hulu-hulu sebelumnya). Ini gerbang anti-halu di titik handoff.
- **Penilaian 3 lapis**: L1 script (bar count, notes-per-track>0, tempo/meter
  tag cocok, semua voice terisi) untuk tiap level; L2 rubrik 4–6 kriteria
  skala 0–2 per artefak oleh **subagent reviewer segar tanpa konteks
  generasi** (self-grading dilarang); L3 telinga manusia via
  `tests/human-ear-protocol.md`, hanya di `output.mid` final.
- **Bahasa dokumen**: semua `SKILL.md` dan `references/*.md` baru/di-split
  ditulis dalam **Bahasa Indonesia** (mengikuti konvensi SOP sumber dan
  `CLAUDE.md` project induk), kecuali isi yang murni kode/script (Python
  tetap dalam bahasa aslinya, komentar boleh tetap Inggris jika sudah ada).
- **Larangan hapus dini**: folder lama (`composition-gateway/`,
  `jazz-idea-generator/`, `abc-notation-writer/`,
  `abc-to-midi-orchestration/`) **tidak boleh dihapus** sebelum
  `docs/migration-map.md` (Task 5) memverifikasi tidak ada file yatim.
  Task 1–4 hanya **create** di `skills/` baru (copy isi, bukan `git mv`,
  untuk file yang kontennya di-split ke beberapa tujuan); Task 2 boleh
  `git mv` untuk file yang pindah 1:1 utuh (abc-notation, midi-orchestration
  script inti) karena tidak ada ambiguitas split.
- **Tidak ada placeholder**: setiap file yang dibuat harus berisi konten
  final, bukan "TBD"/"isi nanti".
- **RED-FLAGS berulang**: gate "ask, don't guess" dan baris RED-FLAGS.md yang
  relevan diulang di titik level terkait di `references/level-XX-*.md`
  masing-masing, bukan hanya sekali di preambul.

## Task 1 — Scaffold `skills/` + main skill `jazz-composition`

**Files**
- Create: `skills/jazz-composition/SKILL.md`
- Create: `skills/jazz-composition/references/level-01-konsep.md` … `level-14-detail.md` (14 file)
- Create: `skills/jazz-composition/references/run-folder-protocol.md`
- Create: `skills/jazz-composition/references/scorecard-template.md`
- Create: `skills/jazz-composition/assets/composition-plan-template.json` (copy dari `jazz-idea-generator/assets/composition-plan-template.json`, file lama tetap ada sampai Task 5)

**Interfaces**
- Konsumsi: `docs/raw/sop-komposisi-jazz-14-level.md` (sumber SOP verbatim).
- Produksi: satu-satunya entry point yang dipakai Task 2–6; setiap level
  file di sini dirujuk oleh modul terkait di Task 3/4 (mis. `harmony`
  merujuk balik ke `level-03-harmoni.md` untuk prosedur, dan sebaliknya
  `level-03-harmoni.md` merujuk ke `references/harmony/*` — lihat Task 3).

**Steps**

- [ ] Buat direktori `skills/` di root repo: `mkdir -p skills`.
- [ ] Untuk tiap level, ekstrak blok SOP persis dari
  `docs/raw/sop-komposisi-jazz-14-level.md` memakai heading `LEVEL N —` s/d
  heading `LEVEL N+1 —` (atau s/d `WORKFLOW PRAKTIS DARI NOL` untuk Level
  14) sebagai batas, lalu tulis ke file `references/level-NN-<slug>.md`
  dengan judul `# Level N — <Nama>` di baris pertama:
  - `level-01-konsep.md` ← `LEVEL 1 — KONSEP ARTISTIK` s/d sebelum `LEVEL 2`
  - `level-02-arsitektur.md` ← `LEVEL 2 — ARSITEKTUR LAGU`
  - `level-03-harmoni.md` ← `LEVEL 3 — PETA HARMONI`
  - `level-04-melodi.md` ← `LEVEL 4 — DESAIN MELODI` (tahap 1–9 utuh)
  - `level-05-ritme-groove.md` ← `LEVEL 5 — DESAIN RITME DAN GROOVE`
  - `level-06-aransemen.md` ← `LEVEL 6 — ARANSEMEN INSTRUMEN`
  - `level-07-comping-voicing.md` ← `LEVEL 7 — DESAIN COMPING DAN VOICING`
  - `level-08-bass.md` ← `LEVEL 8 — DESAIN BASS LINE`
  - `level-09-drum.md` ← `LEVEL 9 — DESAIN DRUM`
  - `level-10-improvisasi.md` ← `LEVEL 10 — DESAIN IMPROVISASI`
  - `level-11-interlude-shout-transisi.md` ← `LEVEL 11 — INTERLUDE, SHOUT CHORUS, DAN TRANSISI`
  - `level-12-intro-ending.md` ← `LEVEL 12 — INTRO DAN ENDING`
  - `level-13-dinamika-dramaturgi.md` ← `LEVEL 13 — DINAMIKA DAN DRAMATURGI`
  - `level-14-detail.md` ← `LEVEL 14 — DETAIL LOW LEVEL` (berhenti sebelum `WORKFLOW PRAKTIS DARI NOL`)
- [ ] Di tiap `level-XX-*.md`, setelah konten SOP yang diekstrak, tambahkan
  section `## Gate — ask, don't guess` yang menyalin satu baris RED-FLAGS
  yang relevan dari `RED-FLAGS.md` root (mis. `level-06-aransemen.md`
  menyalin baris "This section needs every device..."; `level-03-harmoni.md`
  dan `level-04-melodi.md` menyalin baris "The chorus should basically
  repeat the verse..."; `level-09-drum.md` menyalin baris "The drum grid
  and the ABC don't line up..."), plus satu baris eksplisit: "Jika field
  wajib artefak level ini belum diputuskan brief/level sebelumnya — **tanya,
  jangan menebak.**"
- [ ] Di tiap `level-XX-*.md`, tambahkan section `## Modul pendalaman` yang
  menunjuk modul terkait dari tabel spec (mis. `level-03-harmoni.md` →
  `../../harmony/SKILL.md`; `level-04-melodi.md` → `../../melody-design/SKILL.md`
  dan `../../advanced-melody/SKILL.md` untuk tahap 7–8; `level-05-ritme-groove.md`,
  `level-08-bass.md`, `level-09-drum.md` → `../../groove-rhythm/SKILL.md`;
  `level-06-aransemen.md`, `level-07-comping-voicing.md`,
  `level-11-interlude-shout-transisi.md`, `level-12-intro-ending.md`,
  `level-13-dinamika-dramaturgi.md` → `../../arrangement/SKILL.md`).
- [ ] Tulis `skills/jazz-composition/SKILL.md` dengan frontmatter:
  `name: jazz-composition`, `description:` menyerap deskripsi lama
  `composition-gateway` (single entry point, greet & route) digabung
  kalimat bahwa skill ini **juga** menjalankan seluruh pipeline (bukan
  cuma routing) — karena gateway lama dihapus dan perannya diserap di sini.
  Body memuat, berurutan:
  1. Ringkasan "Gambaran Besar" (10 lapisan) dari
     `docs/raw/sop-komposisi-jazz-14-level.md` bagian atas.
  2. Tabel 14 level → file `references/level-NN-*.md` → modul pendalaman.
  3. Salinan verbatim section `WORKFLOW PRAKTIS DARI NOL` (Tahap 1–15) dari
     `docs/raw/sop-komposisi-jazz-14-level.md`, dengan tiap tahap dianotasi
     nomor artefak run-folder yang harus dihasilkan (Tahap 1 → `01-brief.md`,
     Tahap 2 → `02-form.md`, dst mengikuti daftar di Global Constraints).
  4. Salinan verbatim section `CHECKLIST FINAL` dari SOP raw file.
  5. Section `## Run folder` yang merujuk `references/run-folder-protocol.md`.
  6. Section `## Penilaian` yang merujuk `references/scorecard-template.md`.
  7. Baris penutup yang merujuk `../../RED-FLAGS.md` (path relatif dari
     `skills/jazz-composition/SKILL.md` ke root, dua level naik).
- [ ] Tulis `skills/jazz-composition/references/run-folder-protocol.md`:
  jelaskan struktur `runs/<tanggal>-<slug>/`, format `progress.md` (contoh
  tabel: kolom Level | Status | Artefak | Next action), aturan penamaan
  `<tanggal>` = `YYYY-MM-DD` dan `<slug>` = kebab-case dari judul sementara
  brief, dan aturan resume (baca `progress.md` dulu sebelum mulai kerja baru
  di run folder yang sudah ada).
- [ ] Tulis `skills/jazz-composition/references/scorecard-template.md`:
  template markdown `scorecard.md` dengan section per level, tiap section
  berisi sub-bagian `L1 (mekanis)` (checklist pass/fail dari script), `L2
  (rubrik)` (tabel kriteria 0–2 + skor + alasan 1 kalimat, diisi subagent
  reviewer segar), dan catatan bahwa `L3 (telinga)` hanya diisi sekali di
  bagian akhir setelah `output.mid` ada, merujuk `tests/human-ear-protocol.md`.
- [ ] Copy (bukan move) `jazz-idea-generator/assets/composition-plan-template.json`
  ke `skills/jazz-composition/assets/composition-plan-template.json`.
- [ ] Verifikasi: `ls skills/jazz-composition/references/ | grep -c '^level-'`
  → harus `14`. `test -f skills/jazz-composition/SKILL.md && grep -c "Tahap " skills/jazz-composition/SKILL.md`
  → harus ≥15 (workflow 15 tahap tersalin). `grep -c "^## " skills/jazz-composition/SKILL.md`
  → cek section utama ada (brief manual review, tidak perlu angka pasti).
- [ ] Commit: `git add skills/jazz-composition docs/raw && git commit -m "feat: scaffold skill orchestrator jazz-composition dari SOP 14-level"`.

## Task 2 — Migrasi `abc-notation` dan `midi-orchestration` (1:1, `git mv`)

**Files**
- Create (via `git mv`): `skills/abc-notation/SKILL.md`,
  `skills/abc-notation/references/abc-syntax.md`,
  `skills/abc-notation/references/common-failures.md`,
  `skills/abc-notation/references/drums-and-abc.md`,
  `skills/abc-notation/scripts/validate_abc.py`,
  `skills/abc-notation/scripts/test_validate_abc.py`,
  `skills/abc-notation/assets/lead-sheet-template.abc`
- Create (via `git mv`): `skills/midi-orchestration/SKILL.md`,
  `skills/midi-orchestration/references/midi-conversion.md`,
  `skills/midi-orchestration/scripts/abc_to_midi.py`,
  `skills/midi-orchestration/scripts/grid_to_midi.py`,
  `skills/midi-orchestration/scripts/test_abc_to_midi_and_grid.py`,
  `skills/midi-orchestration/assets/drum-grid-template.json`
- Delete: `abc-notation-writer/scripts/__pycache__/` (cache, tidak di-mv)
- Modify: path relatif internal di kedua `SKILL.md` yang di-mv (lihat steps)

**Interfaces**
- Konsumsi: tidak ada dependensi ke Task 1/3/4 — dua modul ini pindah utuh
  tanpa split konten (per spec §3, "scripts & references moved utuh").
- Produksi: `skills/abc-notation/scripts/validate_abc.py` dan
  `skills/midi-orchestration/scripts/{abc_to_midi.py,grid_to_midi.py}`
  dipakai langsung oleh Task 6 (dry-run) dan oleh `jazz-composition/SKILL.md`
  Tahap 7 (notasi) dan Tahap 11 (arrangement map → MIDI).

**Steps**

- [ ] `mkdir -p skills/abc-notation/references skills/abc-notation/scripts skills/abc-notation/assets`
- [ ] `git mv abc-notation-writer/SKILL.md skills/abc-notation/SKILL.md`
- [ ] `git mv abc-notation-writer/references/abc-syntax.md skills/abc-notation/references/abc-syntax.md`
- [ ] `git mv abc-notation-writer/references/common-failures.md skills/abc-notation/references/common-failures.md`
- [ ] `git mv abc-notation-writer/references/drums-and-abc.md skills/abc-notation/references/drums-and-abc.md`
- [ ] `git mv abc-notation-writer/scripts/validate_abc.py skills/abc-notation/scripts/validate_abc.py`
- [ ] `git mv abc-notation-writer/scripts/test_validate_abc.py skills/abc-notation/scripts/test_validate_abc.py`
- [ ] `git mv abc-notation-writer/assets/lead-sheet-template.abc skills/abc-notation/assets/lead-sheet-template.abc`
- [ ] `rm -rf abc-notation-writer/scripts/__pycache__ abc-notation-writer` (folder sekarang kosong — hapus; jika masih ada file lain yang belum dipindah, JANGAN hapus, laporkan dan hentikan step ini)
- [ ] Di `skills/abc-notation/SKILL.md`, ganti setiap referensi `../RED-FLAGS.md`
  menjadi `../../RED-FLAGS.md` (naik satu level lebih dalam dari sebelumnya),
  dan ganti sebutan skill lama `jazz-idea-generator`/`abc-to-midi-orchestration`
  menjadi `jazz-composition`/`midi-orchestration` di teks deskriptif (bukan
  di frontmatter `name`).
- [ ] `mkdir -p skills/midi-orchestration/references skills/midi-orchestration/scripts skills/midi-orchestration/assets`
- [ ] `git mv abc-to-midi-orchestration/SKILL.md skills/midi-orchestration/SKILL.md`
- [ ] `git mv abc-to-midi-orchestration/references/midi-conversion.md skills/midi-orchestration/references/midi-conversion.md`
- [ ] `git mv abc-to-midi-orchestration/scripts/abc_to_midi.py skills/midi-orchestration/scripts/abc_to_midi.py`
- [ ] `git mv abc-to-midi-orchestration/scripts/grid_to_midi.py skills/midi-orchestration/scripts/grid_to_midi.py`
- [ ] `git mv abc-to-midi-orchestration/scripts/test_abc_to_midi_and_grid.py skills/midi-orchestration/scripts/test_abc_to_midi_and_grid.py`
- [ ] `git mv abc-to-midi-orchestration/assets/drum-grid-template.json skills/midi-orchestration/assets/drum-grid-template.json`
- [ ] Di `skills/midi-orchestration/SKILL.md`, ganti `../RED-FLAGS.md` →
  `../../RED-FLAGS.md`, ganti sebutan `abc-notation-writer` →
  `abc-notation`, `jazz-idea-generator` → `jazz-composition`. Catat bahwa
  `references/{advanced-microtiming,ensemble-interaction,exact-voicing,
  groove-meter,groove-profiles,instrumental-transitions,interaction-map,
  quality-control}.md` **belum dipindah** — itu tugas Task 3/4, jangan
  hapus `abc-to-midi-orchestration/` di task ini.
- [ ] Verifikasi: `ls skills/abc-notation/scripts/ skills/midi-orchestration/scripts/`
  menunjukkan 5 file `.py` total (2 + 3). `test -d abc-notation-writer` →
  harus **false** (folder terhapus). `test -d abc-to-midi-orchestration` →
  masih **true** (belum dihapus, sisa referensi menunggu Task 3/4).
  `git status --short | grep '^R'` menunjukkan rename terdeteksi git untuk
  file yang di-`git mv`.
- [ ] Commit: `git add -A && git commit -m "refactor: pindahkan abc-notation dan midi-orchestration ke skills/ (1:1)"`.

## Task 3 — Modul detailing: harmony, melody-design, advanced-melody, vibes-mood, groove-rhythm, arrangement

**Files**
- Create: `skills/harmony/SKILL.md`, `skills/harmony/references/voicing-systems.md` (dari `exact-voicing.md`)
- Create: `skills/melody-design/SKILL.md`, `skills/melody-design/references/melody-fundamentals.md` (dari `ideation-theory.md` bagian melodi)
- Create: `skills/advanced-melody/SKILL.md` (konten baru, disintesis dari SOP Level 4 tahap 7–8, tidak ada file lama sumbernya — dicatat sebagai "tanpa sumber lama" di migration-map)
- Create: `skills/vibes-mood/SKILL.md`, `skills/vibes-mood/references/neo-soul-genre.md`, `skills/vibes-mood/references/reasoning-theory.md`, `skills/vibes-mood/references/style-cheatsheets.md`
- Create: `skills/groove-rhythm/SKILL.md`, `skills/groove-rhythm/references/rhythm-fundamentals.md` (dari `ideation-theory.md` §1), `skills/groove-rhythm/references/advanced-microtiming.md`, `skills/groove-rhythm/references/groove-meter.md`, `skills/groove-rhythm/references/groove-profiles.md`
- Create: `skills/arrangement/SKILL.md`, `skills/arrangement/references/form-and-dramaturgy.md`, `skills/arrangement/references/loop-development.md`, `skills/arrangement/references/ensemble-interaction.md`, `skills/arrangement/references/instrumental-transitions.md`, `skills/arrangement/references/interaction-map.md`
- Modify: none (source files di `jazz-idea-generator/` dan `abc-to-midi-orchestration/` tetap dibaca sebagai sumber, belum dihapus)

**Interfaces**
- Konsumsi: `jazz-idea-generator/references/{ideation-theory,neo-soul-genre,
  reasoning-theory,style-cheatsheets}.md`, `abc-to-midi-orchestration/references/
  {advanced-microtiming,ensemble-interaction,exact-voicing,groove-meter,
  groove-profiles,instrumental-transitions,interaction-map}.md`.
- Produksi: setiap modul dirujuk balik dari `skills/jazz-composition/references/level-XX-*.md`
  (Task 1) di section "Modul pendalaman"; jadi Task 3 harus memastikan
  nama file & path yang dijanjikan di Task 1 benar-benar ada di sini.

**Steps**

- [ ] `mkdir -p skills/harmony/references skills/melody-design/references skills/advanced-melody/references skills/vibes-mood/references skills/groove-rhythm/references skills/arrangement/references`
- [ ] `git mv abc-to-midi-orchestration/references/exact-voicing.md skills/harmony/references/voicing-systems.md`
- [ ] Tulis `skills/harmony/SKILL.md` (frontmatter `name: harmony`,
  `description:` "Pendalaman peta harmoni jazz — tonal center, harmonic
  rhythm, fungsi harmonik, tension map, teknik reharmonisasi, dan sistem
  voicing/voice-leading presisi. Dipanggil oleh `jazz-composition` saat
  mengerjakan Level 3 (peta harmoni) dan Level 7 (comping/voicing)."). Body:
  salin ringkas Langkah 1–6 dan daftar "Teknik harmonik" dari
  `docs/raw/sop-komposisi-jazz-14-level.md` LEVEL 3, lalu section
  `## Voicing presisi` yang merujuk `references/voicing-systems.md`
  (catatan pitch: file itu pakai scientific pitch notation `C4`=middle C,
  perlu dikonversi eksplisit ke oktaf ABC — salin catatan ini dari header
  asli `exact-voicing.md`).
- [ ] Ekstrak bagian harmoni dari `jazz-idea-generator/references/ideation-theory.md`
  (bagian yang membahas chord/harmoni, bukan §1 Rhythm) ke dalam body
  `skills/harmony/SKILL.md` sebagai section `## Vocabulary kerja` (bukan
  file references terpisah karena isinya ringkas, cukup disalin inline).
- [ ] `git mv abc-to-midi-orchestration/references/groove-meter.md skills/groove-rhythm/references/groove-meter.md`
- [ ] `git mv abc-to-midi-orchestration/references/groove-profiles.md skills/groove-rhythm/references/groove-profiles.md`
- [ ] `git mv abc-to-midi-orchestration/references/advanced-microtiming.md skills/groove-rhythm/references/advanced-microtiming.md`
- [ ] Ekstrak §1 "Rhythm and subdivision" dari
  `jazz-idea-generator/references/ideation-theory.md` ke
  `skills/groove-rhythm/references/rhythm-fundamentals.md`.
- [ ] Tulis `skills/groove-rhythm/SKILL.md` (`name: groove-rhythm`,
  `description:` "Pendalaman ritme, groove, bass line, dan drum — feel,
  syncopation, microtiming/pocket, walking bass, dan roadmap drum. Dipanggil
  `jazz-composition` untuk Level 5 (ritme/groove), Level 8 (bass), Level 9
  (drum)."). Body: salin ringkas isi LEVEL 5, LEVEL 8, LEVEL 9 dari SOP raw
  file (Elemen utama, Walking bass dasar, Komponen utama drum), lalu section
  `## Referensi lanjutan` menautkan ke ke-4 file references di atas dengan
  1 kalimat per file (kapan dibaca).
- [ ] `git mv abc-to-midi-orchestration/references/ensemble-interaction.md skills/arrangement/references/ensemble-interaction.md`
- [ ] `git mv abc-to-midi-orchestration/references/instrumental-transitions.md skills/arrangement/references/instrumental-transitions.md`
- [ ] `git mv abc-to-midi-orchestration/references/interaction-map.md skills/arrangement/references/interaction-map.md`
- [ ] `git mv jazz-idea-generator/references/form-and-dramaturgy.md skills/arrangement/references/form-and-dramaturgy.md`
- [ ] `git mv jazz-idea-generator/references/loop-development.md skills/arrangement/references/loop-development.md`
- [ ] Tulis `skills/arrangement/SKILL.md` (`name: arrangement`,
  `description:` "Pendalaman aransemen instrumen, comping/voicing role,
  interlude/shout chorus/transisi, intro/ending, dan dinamika/dramaturgi.
  Dipanggil `jazz-composition` untuk Level 6, 7, 11, 12, 13."). Body: salin
  ringkas LEVEL 6, LEVEL 7 (bagian teknik comping saja — voicing presisi
  sudah di `harmony`), LEVEL 11, LEVEL 12, LEVEL 13 dari SOP raw file, lalu
  section `## Referensi lanjutan` menautkan ke 5 file di atas.
- [ ] `git mv jazz-idea-generator/references/ideation-theory.md skills/melody-design/references/melody-fundamentals.md`
  (file ini sudah kehilangan bagian rhythm & harmony yang diekstrak di atas
  — edit file hasil `git mv` ini untuk **menghapus** section rhythm §1 yang
  sudah disalin ke `groove-rhythm/references/rhythm-fundamentals.md` dan
  section harmoni yang sudah disalin ke `harmony/SKILL.md`, supaya tidak
  duplikat; sisakan hanya bagian melodi/interval/kontur).
- [ ] Tulis `skills/melody-design/SKILL.md` (`name: melody-design`,
  `description:` "Desain melodi dasar — motif, kontur, target tone,
  broken chord. Dipanggil `jazz-composition` untuk Level 4 tahap 1–6."
  ). Body: salin ringkas Tahap 1–6 dari SOP LEVEL 4, section
  `## Referensi lanjutan` → `references/melody-fundamentals.md`, dan baris
  eksplisit "Untuk outside playing/chromatic vocabulary (tahap 7–8), lihat
  `../advanced-melody/SKILL.md` — jangan campur di sini."
- [ ] Tulis `skills/advanced-melody/SKILL.md` (`name: advanced-melody`,
  `description:` "Chromatic vocabulary, enclosure, dan outside playing
  terkontrol — dipanggil `jazz-composition` untuk Level 4 tahap 7–8, hanya
  saat tension map (Level 3) menandai bar itu perlu tegangan tinggi."
  ). Body: salin verbatim Tahap 7 "Tambahkan chromatic vocabulary" dan
  Tahap 8 "Tentukan area outside" dari SOP LEVEL 4 (termasuk contoh
  `Eb–E`, `Inside/Outside/Resolution`), plus baris syarat efektif ("pola
  ritmenya kuat, bentuk motifnya jelas, durasinya terbatas, resolusinya
  nyata") sebagai gate wajib sebelum dipakai.
- [ ] `git mv jazz-idea-generator/references/neo-soul-genre.md skills/vibes-mood/references/neo-soul-genre.md`
- [ ] `git mv jazz-idea-generator/references/reasoning-theory.md skills/vibes-mood/references/reasoning-theory.md`
- [ ] `git mv jazz-idea-generator/references/style-cheatsheets.md skills/vibes-mood/references/style-cheatsheets.md`
- [ ] Tulis `skills/vibes-mood/SKILL.md` (`name: vibes-mood`,
  `description:` "Mood → parameter musikal, 9 modul teori penalaran, dan
  profil genre neo-soul/chill-jazz. Dipanggil `jazz-composition` di Level 1
  (konsep artistik) untuk menerjemahkan brief mood menjadi keputusan gaya/
  tempo/karakter yang konkret."). Body: section `## Referensi` menautkan
  ke 3 file di atas dengan 1 kalimat per file, plus catatan genre-first
  neo-soul/chill-jazz dipertahankan (salin kalimat dari header lama
  `neo-soul-genre.md`).
- [ ] Verifikasi tidak ada file jazz-idea-generator tersisa selain SKILL.md
  dan asset yang sudah dicopy di Task 1:
  `find jazz-idea-generator -type f` → harus hanya menyisakan `SKILL.md`
  dan `assets/composition-plan-template.json` (dihapus di Task 5).
  `find abc-to-midi-orchestration -type f` → harus hanya menyisakan
  `SKILL.md`, `references/{midi-conversion,quality-control}.md`,
  `scripts/*` (sudah di-mv di Task 2 — jika masih tampak berarti Task 2
  belum commit; jika `quality-control.md` masih ada itu memang benar,
  ditangani Task 4), `assets/*` (sudah di-mv Task 2).
- [ ] Commit: `git add -A && git commit -m "feat: pecah konten jazz-idea-generator + abc-to-midi-orchestration jadi 6 modul detailing"`.

## Task 4 — Rubrik per level dari `quality-control.md`

**Files**
- Create: `skills/harmony/references/rubric.md`, `skills/melody-design/references/rubric.md`,
  `skills/advanced-melody/references/rubric.md`, `skills/vibes-mood/references/rubric.md`,
  `skills/groove-rhythm/references/rubric.md`, `skills/arrangement/references/rubric.md`,
  `skills/abc-notation/references/rubric.md`, `skills/midi-orchestration/references/rubric.md`
- Delete (setelah split selesai): `abc-to-midi-orchestration/references/quality-control.md`
- Modify: `skills/jazz-composition/SKILL.md` (tambah section reviewer-segar)

**Interfaces**
- Konsumsi: `abc-to-midi-orchestration/references/quality-control.md`
  (§1–§16 kriteria kualitatif, §17 scoring rubric `/64`, §18 template
  laporan) — sumber tunggal untuk semua rubrik modul.
- Produksi: `scorecard-template.md` (Task 1) mengacu ke rubrik-rubrik ini
  per level; dry-run Task 6 memakainya untuk mengisi L2.

**Steps**

- [ ] Baca `abc-to-midi-orchestration/references/quality-control.md` §1–16
  dan petakan tiap section ke modul: §1 Brief/identity/ethics + §2
  Candidate selection → `vibes-mood`; §3 Development/anti-boredom + §10
  Loop development → `arrangement`; §4 Form/section function → `arrangement`;
  §5 Instrumental transitions → `arrangement`; §6 Meter/tempo/groove/
  microtiming → `groove-rhythm`; §7 Harmony → `harmony`; §8 Bass/exact
  voicing → `harmony` (voicing) + `groove-rhythm` (bass); §9 Melody/hook/
  thematic development → `melody-design`; §11 Improvisation →
  `arrangement`; §12 Ensemble interaction/arrangement → `arrangement`;
  §13 Production/DAW-first → `midi-orchestration`; §15 ABC and notation →
  `abc-notation`.
- [ ] Untuk tiap modul, tulis `references/rubric.md` berisi tabel 4–6
  kriteria skala 0–2, diturunkan dari poin-poin section terkait di §1–16
  (ubah kalimat checklist panjang jadi kriteria skor pendek, mis. §7
  "Harmony" → kriteria "Fungsi harmonik tiap chord jelas (tonic/predominant/
  dominant/dst)" skala 0–2), plus 1 baris instruksi "Diisi subagent reviewer
  segar tanpa konteks generasi — skor + alasan 1 kalimat per kriteria."
- [ ] Tambahkan ke `skills/harmony/references/rubric.md` dan
  `skills/groove-rhythm/references/rubric.md` kriteria bass/voicing dari §8
  sesuai pembagian di atas (masing-masing subset berbeda, jangan duplikat
  penuh).
- [ ] Salin §17 "Scoring rubric" dan §18 "Final validation report template"
  dari `quality-control.md` sebagai referensi format skor 0–2 dan struktur
  laporan — jadikan dasar format tiap `rubric.md` yang baru dibuat (bukan
  disalin utuh, tapi formatnya dipakai konsisten).
- [ ] Update `skills/jazz-composition/SKILL.md`: tambah section
  `## Reviewer segar (L2)` yang menjelaskan subagent yang mengisi L2 harus
  **baru** (tanpa histori percakapan generasi), diberi hanya artefak +
  `rubric.md` modul terkait, dan menulis hasil ke `scorecard.md` — bukan ke
  chat.
- [ ] `git rm abc-to-midi-orchestration/references/quality-control.md` (isi
  sudah sepenuhnya terdistribusi ke 8 `rubric.md` di atas — verifikasi step
  berikutnya sebelum menghapus).
- [ ] Verifikasi: `ls skills/*/references/rubric.md | wc -l` → harus `8`.
  `grep -L "skala 0" skills/*/references/rubric.md` → harus kosong (semua
  file punya skala skor). `test -f abc-to-midi-orchestration/references/quality-control.md`
  → harus **false**.
- [ ] Commit: `git add -A && git commit -m "feat: pecah rubrik quality-control.md jadi rubric.md per modul"`.

## Task 5 — Migration map, hapus folder lama, update dokumen induk

**Files**
- Create: `docs/migration-map.md`
- Delete: `composition-gateway/`, `jazz-idea-generator/`,
  `abc-to-midi-orchestration/` (folder tersisa setelah Task 2–4)
- Modify: `README.md`, `CLAUDE.md`, `RED-FLAGS.md` (path baru)

**Interfaces**
- Konsumsi: hasil Task 1–4 (semua file `skills/**`).
- Produksi: `docs/migration-map.md` adalah bukti verifikasi utama yang
  disyaratkan spec §Verifikasi poin 1; Task 6 mengasumsikan folder lama
  sudah tidak ada dan semua dokumen induk menunjuk `skills/`.

**Steps**

- [ ] Tulis `docs/migration-map.md`: tabel dengan kolom
  `File lama | Tujuan baru | Catatan`, satu baris per file dari inventori
  awal (24 file: 2 dari `composition-gateway`, 7 dari `jazz-idea-generator`,
  7 dari `abc-notation-writer`, 12 dari `abc-to-midi-orchestration` —
  termasuk `SKILL.md` masing-masing dan `__pycache__` yang dibuang), diisi
  dari mapping yang sudah dieksekusi di Task 1–4 (mis. baris
  `jazz-idea-generator/references/ideation-theory.md | skills/melody-design/references/melody-fundamentals.md (+ split ke groove-rhythm/references/rhythm-fundamentals.md, harmony/SKILL.md §Vocabulary kerja) | dipecah 3 arah`).
  Tandai `composition-gateway/SKILL.md` dan
  `composition-gateway/references/composition-layers.md` sebagai
  "diserap ke skills/jazz-composition/SKILL.md + references/level-*.md".
- [ ] Verifikasi tidak ada file yatim: jalankan
  `find composition-gateway jazz-idea-generator abc-notation-writer abc-to-midi-orchestration -type f 2>/dev/null`
  dan pastikan setiap baris hasilnya (kalau masih ada folder tersisa) punya
  padanan baris di `docs/migration-map.md`. Idealnya di titik ini semua
  folder lama sudah kosong dari file (Task 2–4 sudah `git mv`/`git rm`
  semuanya) kecuali `composition-gateway/` yang belum disentuh — tangani
  sekarang: `git mv composition-gateway/references/composition-layers.md /tmp/_reference_only_for_diff.md`
  tidak diperlukan karena kontennya sudah disalin manual ke
  `skills/jazz-composition/SKILL.md` + `references/level-*.md` di Task 1;
  cukup hapus.
- [ ] `git rm -r composition-gateway jazz-idea-generator abc-to-midi-orchestration`
  (folder ini harus sudah kosong file kontennya per Task 1–4; jika
  `git rm -r` menolak karena masih ada file tak-terlacak, jalankan
  `find <folder> -type f` dulu, pastikan tercatat di migration-map, baru
  hapus).
- [ ] Update `README.md`: ganti diagram
  `composition-gateway → jazz-idea-generator → abc-notation-writer → abc-to-midi-orchestration`
  menjadi deskripsi baru: `jazz-composition` sebagai orchestrator tunggal
  yang memanggil 8 modul (`harmony`, `melody-design`, `advanced-melody`,
  `vibes-mood`, `groove-rhythm`, `arrangement`, `abc-notation`,
  `midi-orchestration`) sesuai level yang sedang dikerjakan; update section
  "Artifact flow" dan "Origin" agar menyebut lokasi baru
  (`skills/vibes-mood/references/`, dst) alih-alih
  `jazz-idea-generator/references/`.
- [ ] Update `CLAUDE.md` (root package ini): ganti baris "Start at the
  gateway... `composition-gateway/SKILL.md`" dan daftar bernomor 3 skill
  menjadi: "Start at `skills/jazz-composition/SKILL.md` — satu-satunya
  entry point dan orchestrator." plus daftar 8 modul pendalaman. Update
  referensi `abc-to-midi-orchestration/references/quality-control.md` di
  bagian "ground rules" menjadi merujuk rubrik per modul
  (`skills/*/references/rubric.md`).
- [ ] Update `RED-FLAGS.md`: ganti tiap path kolom "Where to check" dari
  path lama (`jazz-idea-generator/SKILL.md`, `abc-to-midi-orchestration/
  references/midi-conversion.md`, dst) ke path `skills/` baru yang sesuai
  (`skills/jazz-composition/SKILL.md`, `skills/midi-orchestration/
  references/midi-conversion.md`, `skills/abc-notation/references/
  abc-syntax.md`, `skills/*/references/rubric.md` untuk baris rubrik).
- [ ] Verifikasi: `test -d composition-gateway -o -d jazz-idea-generator -o -d abc-to-midi-orchestration`
  → harus gagal (exit non-zero, folder tidak ada). `test -d abc-notation-writer`
  → harus gagal juga (sudah dihapus Task 2).
  `grep -rl "composition-gateway\|jazz-idea-generator\|abc-notation-writer\|abc-to-midi-orchestration" README.md CLAUDE.md RED-FLAGS.md`
  → harus kosong (tidak ada sisa referensi path lama di 3 file ini).
  `wc -l docs/migration-map.md` → harus mencakup baris untuk semua 24 file
  inventori awal (cek manual bila count tidak pas, karena beberapa baris
  boleh gabung file terkait).
- [ ] Commit: `git add -A && git commit -m "docs: migration map lengkap, hapus skill lama, update README/CLAUDE/RED-FLAGS ke skills/"`.

## Task 6 — Dry-run verifikasi end-to-end

**Files**
- Create: `runs/<tanggal>-<slug>/` (hasil dry-run, dari salah satu
  `tests/briefs/*.md` — mis. `tests/briefs/brief-01-neo-soul-doubt-to-acceptance.md`)
- Modify: none di `skills/` (hanya dipakai, tidak diedit — kecuali dry-run
  menemukan bug nyata, lihat step terakhir)

**Interfaces**
- Konsumsi: seluruh `skills/jazz-composition/` + 8 modul dari Task 1–4,
  `tests/briefs/brief-01-neo-soul-doubt-to-acceptance.md`,
  `tests/human-ear-protocol.md`.
- Produksi: bukti pemenuhan spec §Verifikasi poin 2 — laporan singkat di
  akhir task ini (bukan file baru selain run folder) yang mengonfirmasi tiap
  butir.

**Steps**

- [ ] Spawn subagent segar (tanpa histori percakapan yang menulis plan ini)
  dengan brief: "Jalankan `skills/jazz-composition/SKILL.md` end-to-end
  untuk `tests/briefs/brief-01-neo-soul-doubt-to-acceptance.md`. Ikuti
  workflow 15 tahap, buat run folder `runs/2026-07-14-doubt-to-acceptance/`,
  isi `progress.md` dan artefak DoD bernomor tiap level, panggil modul
  pendalaman sesuai tabel di SKILL.md, hasilkan `song.abc`, `drums.json`,
  `output.mid` di run folder, isi `scorecard.md` L1+L2 tiap level."
- [ ] Setelah subagent selesai, verifikasi run folder terbentuk:
  `test -d runs/2026-07-14-doubt-to-acceptance` → true.
- [ ] Verifikasi `progress.md` mencerminkan status level yang benar:
  `grep -c "done" runs/2026-07-14-doubt-to-acceptance/progress.md` → ≥14
  (semua level selesai atau ditandai sesuai kondisi nyata — kalau ada yang
  `blocked`, itu temuan valid, bukan kegagalan verifikasi).
- [ ] Verifikasi artefak DoD bernomor ada dan berurutan:
  `ls runs/2026-07-14-doubt-to-acceptance/ | grep -E '^[0-9]{2}-' | sort`
  → menunjukkan urutan `01-...` s/d `14-...` tanpa lompatan nomor.
- [ ] Verifikasi `output.mid` benar-benar berisi musik (bukan cuma exit
  status validator — sesuai `RED-FLAGS.md`): jalankan
  `python3 -c "import pretty_midi; m = pretty_midi.PrettyMIDI('runs/2026-07-14-doubt-to-acceptance/output.mid'); print(len(m.instruments)); [print(i.name, len(i.notes)) for i in m.instruments]; print(m.get_tempo_changes())"`
  → track count > 1, tiap instrument punya notes > 0, tempo/time-signature
  cocok dengan header ABC di `song.abc`.
- [ ] Verifikasi `scorecard.md` terisi: `grep -c "L1\|L2" runs/2026-07-14-doubt-to-acceptance/scorecard.md`
  → > 0 untuk tiap level yang dilalui.
- [ ] Jika dry-run menemukan bug nyata di `skills/` (bukan salah pakai oleh
  subagent) — perbaiki file terkait langsung, catat perbaikannya di pesan
  commit.
- [ ] Commit: `git add runs/2026-07-14-doubt-to-acceptance && git commit -m "test: dry-run brief-01 lewat skills/jazz-composition, verifikasi run folder + MIDI aktual"`
  (jika ada perbaikan bug dari step sebelumnya, sertakan file `skills/**`
  yang diperbaiki di commit yang sama dengan pesan yang menyebut fix-nya).

## Self-review sebelum dianggap selesai

- [ ] Scan seluruh `skills/**/*.md` untuk placeholder terlarang:
  `grep -rniE "TBD|isi nanti|tulis rubrik yang sesuai|lorem ipsum" skills/`
  → harus kosong.
- [ ] Cek tidak ada file yatim: bandingkan output
  `find skills -type f | sort` dengan seluruh baris "Tujuan baru" di
  `docs/migration-map.md` — tiap file `skills/**` harus muncul sebagai
  tujuan di minimal satu baris.
- [ ] Cek konsistensi path: `grep -rn "abc-to-midi-orchestration\|jazz-idea-generator\|abc-notation-writer\|composition-gateway" skills/ docs/migration-map.md README.md CLAUDE.md RED-FLAGS.md`
  → hasil yang tersisa (jika ada) harus berupa catatan historis eksplisit
  (mis. di `docs/migration-map.md` kolom "File lama"), bukan path aktif
  yang dirujuk sebagai lokasi hidup.

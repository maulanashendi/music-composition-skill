# Migration map — restrukturisasi `skills/` (Task 1–5)

Peta lengkap dari 4 folder skill lama (`composition-gateway/`,
`jazz-idea-generator/`, `abc-notation-writer/`, `abc-to-midi-orchestration/`)
ke struktur baru `skills/<nama>/`. Kolom "File lama" bersifat historis —
tidak diubah walau folder aslinya sudah dihapus di task ini. Sumber:
`git show --stat`/`--name-status` untuk commit `cc1e73f`, `4b28085`,
`2856394`, `9a667e3`, `436d452`, `5a2cfb2`, disilangkan dengan laporan
`.superpowers/sdd/task-{1,2,3,4}-report.md`.

Inventori nyata (dihitung dari tree sebelum task-2, commit `1ee4734`) adalah
**30 file**: 2 dari `composition-gateway`, 7 dari `jazz-idea-generator`,
7 dari `abc-notation-writer`, 14 dari `abc-to-midi-orchestration`. (Brief
Task 5 menyebut "24 file" sebagai estimasi kasar — dihitung ulang di sini
per file nyata; selisihnya berasal dari brief tidak menghitung semua 8
reference file `abc-to-midi-orchestration` + `quality-control.md` secara
terpisah. Tidak ada file yang hilang; lihat verifikasi "no orphan" di bawah.)

## `composition-gateway/` (2 file)

| File lama | Tujuan baru | Catatan |
|---|---|---|
| `composition-gateway/SKILL.md` | `skills/jazz-composition/SKILL.md` | Diserap: deskripsi entry-point/greet-and-route jadi bagian frontmatter `description` + preambul "Aturan dasar" di SKILL.md orchestrator baru (Task 1). |
| `composition-gateway/references/composition-layers.md` | `skills/jazz-composition/SKILL.md` (gambaran besar 10-lapisan) + `skills/jazz-composition/references/level-*.md` (14 file) | Diserap dan dipecah manual ke ringkasan gambaran-besar + 14 file level; tidak ada `git mv` karena kontennya disintesis ulang dari `docs/raw/sop-komposisi-jazz-14-level.md`, bukan disalin baris-per-baris. |

## `jazz-idea-generator/` (7 file)

| File lama | Tujuan baru | Catatan |
|---|---|---|
| `jazz-idea-generator/SKILL.md` | `skills/jazz-composition/SKILL.md` (workflow Tahap 1-15, checklist final) + `skills/vibes-mood/SKILL.md` (brief→mood→parameter) | **Digantikan, bukan disalin literal**: workflow "Step 1-N" versi lama diganti oleh Workflow "Tahap 1-15" yang diekstrak dari `docs/raw/sop-komposisi-jazz-14-level.md` (Task 1); pointer ke `reasoning-theory.md` Module 1 diwarisi via `vibes-mood/SKILL.md`. |
| `jazz-idea-generator/assets/composition-plan-template.json` | `skills/jazz-composition/assets/composition-plan-template.json` | Disalin (`cp`, bukan `git mv`) di Task 1; file asli tidak disentuh sampai penghapusan folder di task ini. |
| `jazz-idea-generator/references/ideation-theory.md` | Dipecah 3+ arah: `skills/melody-design/references/melody-fundamentals.md` (via `git mv`, lalu di-strip), `skills/groove-rhythm/references/rhythm-fundamentals.md` (§1 Rhythm + §4 Bassline character), `skills/harmony/SKILL.md` §Vocabulary kerja (§2 Scales/chord qualities, §3 Chord progression logic, §6 Harmony/voice-leading), `skills/arrangement/references/form-and-dramaturgy.md` §11a (§4b Dramatic arc, §4c tension-release-dramaturgi, §7 Song structure), `skills/arrangement/references/ensemble-interaction.md` §20 (§8 Arrangement/instrument interaction) | Dipecah 5 arah (Task 3 commit `2856394`, direvisi lebih lanjut di fix-pass `9a667e3` — lihat detail per-§ di `task-3-report.md`). Sisa di `melody-fundamentals.md`: Phrasing (interval/kontur/timing dari §4c) + Melody/motif/hook (§5). |
| `jazz-idea-generator/references/form-and-dramaturgy.md` | `skills/arrangement/references/form-and-dramaturgy.md` | `git mv` 1:1 (Task 3, commit `2856394`). |
| `jazz-idea-generator/references/loop-development.md` | `skills/arrangement/references/loop-development.md` | `git mv` 1:1 (Task 3, commit `2856394`). |
| `jazz-idea-generator/references/neo-soul-genre.md` | `skills/vibes-mood/references/neo-soul-genre.md` | `git mv` 1:1 (Task 3, commit `2856394`). |
| `jazz-idea-generator/references/reasoning-theory.md` | `skills/vibes-mood/references/reasoning-theory.md` | `git mv` 1:1 (Task 3, commit `2856394`). |
| `jazz-idea-generator/references/style-cheatsheets.md` | `skills/vibes-mood/references/style-cheatsheets.md` | `git mv` 1:1 (Task 3, commit `2856394`). |

## `abc-notation-writer/` (7 file)

| File lama | Tujuan baru | Catatan |
|---|---|---|
| `abc-notation-writer/SKILL.md` | `skills/abc-notation/SKILL.md` | `git mv` (Task 2, commit `4b28085`) + edit prosa (path RED-FLAGS, sebutan skill lama → baru). Frontmatter `name:` masih `abc-notation-writer` sampai fix di task ini (lihat bagian "Perbaikan tambahan" di bawah). |
| `abc-notation-writer/assets/lead-sheet-template.abc` | `skills/abc-notation/assets/lead-sheet-template.abc` | `git mv` 1:1 (Task 2). |
| `abc-notation-writer/references/abc-syntax.md` | `skills/abc-notation/references/abc-syntax.md` | `git mv` 1:1 (Task 2); path stale ke `abc_to_midi.py` diperbaiki di task ini (lihat bawah). |
| `abc-notation-writer/references/common-failures.md` | `skills/abc-notation/references/common-failures.md` | `git mv` 1:1 (Task 2); path stale ke `abc_to_midi.py` diperbaiki di task ini (lihat bawah). |
| `abc-notation-writer/references/drums-and-abc.md` | `skills/abc-notation/references/drums-and-abc.md` | `git mv` 1:1 (Task 2). |
| `abc-notation-writer/scripts/test_validate_abc.py` | `skills/abc-notation/scripts/test_validate_abc.py` | `git mv` 1:1 (Task 2); 16 test lulus dari lokasi baru. |
| `abc-notation-writer/scripts/validate_abc.py` | `skills/abc-notation/scripts/validate_abc.py` | `git mv` 1:1 (Task 2). |

## `abc-to-midi-orchestration/` (14 file)

| File lama | Tujuan baru | Catatan |
|---|---|---|
| `abc-to-midi-orchestration/SKILL.md` | `skills/midi-orchestration/SKILL.md` | `git mv` (Task 2, commit `4b28085`) + edit prosa. Frontmatter `name:` masih `abc-to-midi-orchestration` sampai fix di task ini (lihat bawah). |
| `abc-to-midi-orchestration/assets/drum-grid-template.json` | `skills/midi-orchestration/assets/drum-grid-template.json` | `git mv` 1:1 (Task 2). |
| `abc-to-midi-orchestration/references/advanced-microtiming.md` | `skills/groove-rhythm/references/advanced-microtiming.md` | `git mv` 1:1 (Task 3, commit `2856394`). |
| `abc-to-midi-orchestration/references/ensemble-interaction.md` | `skills/arrangement/references/ensemble-interaction.md` | `git mv` 1:1 (Task 3); kemudian menerima tambahan §20 dari `ideation-theory.md` §8. |
| `abc-to-midi-orchestration/references/exact-voicing.md` | `skills/harmony/references/voicing-systems.md` | `git mv` dengan **rename** (Task 3, commit `2856394`) — nama file berubah, isi 1:1. |
| `abc-to-midi-orchestration/references/groove-meter.md` | `skills/groove-rhythm/references/groove-meter.md` | `git mv` 1:1 (Task 3). |
| `abc-to-midi-orchestration/references/groove-profiles.md` | `skills/groove-rhythm/references/groove-profiles.md` | `git mv` 1:1 (Task 3). |
| `abc-to-midi-orchestration/references/instrumental-transitions.md` | `skills/arrangement/references/instrumental-transitions.md` | `git mv` 1:1 (Task 3). |
| `abc-to-midi-orchestration/references/interaction-map.md` | `skills/arrangement/references/interaction-map.md` | `git mv` 1:1 (Task 3). |
| `abc-to-midi-orchestration/references/midi-conversion.md` | `skills/midi-orchestration/references/midi-conversion.md` | `git mv` 1:1 (Task 2, commit `4b28085`). |
| `abc-to-midi-orchestration/references/quality-control.md` | Dipecah ke 8 `skills/*/references/rubric.md` (`vibes-mood`, `arrangement`, `groove-rhythm`, `harmony`, `melody-design`, `midi-orchestration`, `abc-notation`) + `skills/jazz-composition/references/scorecard-template.md` (§14 composition-plan validasi mekanis, §17 format skor, §18 laporan akhir) | Dipecah per-§ (Task 4, commit `436d452`); §8 dipecah 2 arah lagi (bass/groove → `groove-rhythm`, voicing eksak → `harmony`). Tabel §→tujuan lengkap ada di `task-4-report.md`. File asli dihapus (`D`) di commit ini, bukan `git mv`, karena isinya dipecah bukan pindah 1:1. |
| `abc-to-midi-orchestration/scripts/abc_to_midi.py` | `skills/midi-orchestration/scripts/abc_to_midi.py` | `git mv` 1:1 (Task 2). |
| `abc-to-midi-orchestration/scripts/grid_to_midi.py` | `skills/midi-orchestration/scripts/grid_to_midi.py` | `git mv` 1:1 (Task 2). |
| `abc-to-midi-orchestration/scripts/test_abc_to_midi_and_grid.py` | `skills/midi-orchestration/scripts/test_abc_to_midi_and_grid.py` | `git mv` 1:1 (Task 2); 4 test lulus (butuh venv dengan `pretty_midi`/`music21` — lihat `task-2-report.md`). |

## Artefak folder-kosong (bukan file, dibuang tanpa mapping isi)

Ditemukan Task 3, dibuang Task 5 sebagai bagian dari `git rm -r` /
pembersihan folder lama — bukan konten yang perlu dipetakan, hanya
direktori kosong/keliru yang tersisa dari operasi `git mv` Task 2:

- `abc-to-midi-orchestration/assets/` — direktori kosong (semua isinya
  sudah `git mv` di Task 2).
- `abc-to-midi-orchestration/scripts/` — direktori kosong (idem).
- `abc-to-midi-orchestration/{references,scripts,assets}/` — direktori
  dengan **nama literal berisi kurung kurawal**, artefak keliru dari shell
  brace-expansion yang tidak ter-expand saat `git mv` Task 2 (dicatat
  sebagai concern di `task-3-report.md`). Tidak pernah berisi file.
- `jazz-idea-generator/{references,assets}/` — direktori dengan nama
  literal serupa, artefak keliru yang sama, kosong.

## Verifikasi "tidak ada file yatim"

```
$ find composition-gateway jazz-idea-generator abc-notation-writer abc-to-midi-orchestration -type f 2>/dev/null
composition-gateway/SKILL.md
composition-gateway/references/composition-layers.md
jazz-idea-generator/SKILL.md
jazz-idea-generator/assets/composition-plan-template.json
```

Kedua baris `composition-gateway/*` dan kedua baris `jazz-idea-generator/*`
di atas punya padanan baris di tabel migration-map ini (baris pertama di
tiap tabel folder). `abc-notation-writer` dan `abc-to-midi-orchestration`
sudah tidak punya file tersisa (0 hasil `find -type f`) — hanya direktori
kosong/keliru yang tercatat di bagian "Artefak folder-kosong" di atas.
Tidak ada file di keempat folder lama yang tidak punya baris di dokumen
ini.

## Vendoring untuk self-contained install (final-review fix)

Selain restrukturisasi 4 folder lama di atas, dua file pendukung
dipindah ke dalam `skills/` supaya folder itu bisa di-copy/symlink
sendirian tanpa root repo:

| File lama | Tujuan baru | Catatan |
|---|---|---|
| `RED-FLAGS.md` | `skills/RED-FLAGS.md` | `git mv`; semua referensi lintas paket (SKILL.md orchestrator + `abc-notation`/`midi-orchestration`, plus mention di `CLAUDE.md`) diperbaiki ke kedalaman relatif baru. |
| `tests/human-ear-protocol.md` | `skills/jazz-composition/references/human-ear-protocol.md` | `git mv`; referensi dari `skills/jazz-composition/SKILL.md` dan `references/scorecard-template.md` diperbaiki ke lokasi baru (sama-direktori untuk yang kedua). |

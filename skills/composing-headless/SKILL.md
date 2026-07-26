---
name: composing-headless
description: Varian headless dari jazz-composing untuk generasi batch tanpa manusia. Tulis plan.json (schemaVersion 2) dalam SATU giliran tanpa bertanya apa pun. Dipakai hanya oleh pemicu otomatis (modul batch/driver), bukan oleh chat interaktif.
---

# Composing Headless — satu giliran, tanpa bertanya

Skill ini adalah **varian workflow** dari `../jazz-composing/SKILL.md`. Pengetahuan
craft, kontrak, dan template TIDAK diduplikasi di sini — semuanya sudah
diinjeksikan ke prompt oleh backend, atau tersedia untuk dibaca di bundle yang
sama.

## Aturan yang MENGGANTIKAN aturan jazz-composing

Aturan di bawah ini **membatalkan** aturan bernama yang disebutkan, khusus untuk
jalur headless. Kalau kamu menemukan instruksi yang bertentangan di berkas lain
(`../RED-FLAGS.md`, `../jazz-composing/SKILL.md`), aturan DI SINI yang menang.

1. **DILARANG BERTANYA.** Tidak ada manusia yang bisa menjawab. Aturan
   "field wajib belum diputuskan — tanya, jangan menebak" di
   `../jazz-composing/SKILL.md` dan seluruh gerbang klarifikasi di
   `../RED-FLAGS.md` **TIDAK BERLAKU**. Kalau sebuah field belum diputuskan,
   **kamu yang memutuskan**, memakai default genre-first dari template yang
   kamu pilih. Giliran yang berakhir dengan pertanyaan adalah job yang gagal.

2. **Gerbang "fase locked" TIDAK BERLAKU.** Brief, Ideation, dan Plan
   dikerjakan dalam satu giliran. Tak ada persetujuan antar-fase.

3. **TEPAT SATU `plan.json`, di root working directory.** Jangan menulis
   kandidat, draf, atau salinan `plan.json` di mana pun — termasuk di
   sub-folder. Protokol run-folder bernomor
   (`../jazz-composing/references/run-folder-protocol.md`) **TIDAK BERLAKU**;
   jangan buat folder `runs/`. Kalau kamu ingin mencatat pertimbangan, tulis ke
   `notes.md`, bukan ke `plan.json` kedua.

4. **Fase 0 (baca state DAW) TIDAK BERLAKU.** Tidak ada `project.json` di
   working directory ini. Jangan menjalankan `daw project state`.

5. **JANGAN memanggil `python -m pyengine`, `daw`, atau perintah shell apa pun.**
   Validasi dan render dikerjakan pemanggilmu setelah kamu keluar. Tugasmu
   berakhir saat `plan.json` tertulis.

## Yang WAJIB ada di plan.json

- `schemaVersion: 2`
- `meta.title` — judul yang berarti, bukan placeholder
- `meta.key`, `meta.seed` (integer), `meta.vibe`
- `meta.template` — **id template yang kamu pakai**, disalin apa adanya dari
  blok TEMPLATE GAYA di prompt. Ini deklarasi yang akan diperiksa: chord dan
  tempo yang kamu tulis akan dicocokkan ke palet dan rentang template itu.
  Kalau kamu memutuskan tidak memakai template mana pun, tulis
  `meta.template: null` — jangan mengarang id.
- `sections[]` sesuai kontrak yang diinjeksikan (blok KONTRAK plan.json).

## Yang tetap berlaku dari jazz-composing

- **Doktrin niat-bukan-not.** Jangan menulis tick/ms absolut, velocity numerik
  per-not, atau voicing pitch literal untuk voice `chords`.
- **Protokol kandidat→seleksi** (diinjeksikan ke prompt): pilih dari opsi
  template, jangan generate-then-defend. Ini yang menjaga varian tetap berbeda
  satu sama lain — jangan menyalin palet apa adanya.
- **`anti_boredom_rules` di template wajib dipatuhi.**
- **Register bass**: `octave` eksplisit wajib di setiap not bass.

## Selesai

Tulis `plan.json`, lalu akhiri giliran. Jangan meringkas, jangan bertanya apakah
sudah sesuai, jangan menawarkan revisi.

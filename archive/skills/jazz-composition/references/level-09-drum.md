# Level 9 — Desain Drum

LEVEL 9 — DESAIN DRUM
Tujuan
Membentuk waktu, dinamika, dan transisi.
Komponen utama

* ride cymbal pattern
* hi-hat
* snare comping
* bass drum comping
* fills
* setup
* accents
* form cue
Drum mengikuti struktur
Contoh:

Intro: brushes
A1: light ride
A2: stronger ride
Bridge: active comping
Solo: responsive
Shout chorus: full dynamics
Coda: cymbal swell dan final accent
Output level ini
Drum roadmap, bukan notasi penuh pada tahap awal.

## Aturan komposisi drum (v2 — dibaca oleh pembuat `drums.json`)

Ini aturan doktrin, bukan enforced di kode (kode hanya memberi warning). Melanggarnya adalah salah satu sumber utama rasa "generative loop".

- **Hierarchy wajib untuk section > 2 bar.** Susun dengan `pattern` berupa **list per-bar** (bukan satu dict yang di-tile):
  - **base groove 2-bar** — bar ganjil & genap boleh identik satu sama lain dalam pasangannya (base groove yang bernapas dua bar);
  - **variation** di sekitar bar ke-4 (bukan pengulangan mentah base);
  - **transition variation** di bar terakhir section (fill/lift menuju section berikutnya).
- **Minimal satu one-off imperfection di seluruh lagu** — satu kejadian sekali-saja yang disengaja (bukan berulang): ghost note tunggal setelah frase lead, kick hilang di satu downbeat, atau open-hat sekali. Tandai di `label` bar-nya supaya jelas ini sengaja, bukan error.
- **Dilarang: section > 2 bar dengan semua bar identik.** `grid_to_midi.py` memberi `WARNING` pada kasus ini (lihat `../../midi-orchestration/references/midi-conversion.md`), tapi warning saja tidak cukup — perbaiki jadi base+variation+transition sebelum lanjut.
- **`phrase_velocity`** dipakai untuk membentuk arc dinamika per bar (naik ke transition, turun saat reda) — bukan mengandalkan `humanize_velocity` acak. `humanize_velocity` dijaga kecil (single digit): perannya polish, bukan sumber variasi.
- **`timing`** relasional per-role dipilih dari profil di `../../groove-rhythm/references/groove-profiles.md` (mis. `neo-soul-core`) — salin map-nya, jangan menurunkan angka tick ad hoc.

Sebutkan BPM brief secara eksplisit di artefak level ini dan cek swing/timing
drum terhadap tabel BPM band di
`../../vibes-mood/references/reasoning-theory.md` (lihat ground rule tempo
di SKILL.md).

## Gate — ask, don't guess

- "Drum grid dan ABC gak pas persis bar-per-bar, tapi udah cukup dekat kok." (alasan yang ditolak, lihat RED-FLAGS.md) → "Cukup dekat" perlahan menjadi desync yang terdengar seiring lagu berjalan. Jumlah bar antara drum step-grid dan ABC harus persis sama, section demi section.
- Jika field wajib artefak level ini belum diputuskan brief/level sebelumnya — **tanya, jangan menebak.**

## Modul pendalaman

- ../../groove-rhythm/SKILL.md

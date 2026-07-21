# 03 — Bentuk/Arsitektur Lagu: Kandidat & Seleksi (Level 2)

**Objective:** bentuk yang muat ~1 menit di tempo lambat, cukup ruang
untuk dynamics ramp (Level 1) tanpa terasa terpotong.

**Immutable constraints:** ~60 detik, tempo lambat (ballad, 55-75bpm).

**Assumptions:** tempo final 64 bpm (tengah rentang ballad) → 1 bar
4/4 = 3.75 detik.

## Kandidat

**Alt 1 — Intro(4)–Head(8)–Outro(4), 16 bar total.** 16 × 3.75s = 60.0
detik persis. 3 section rapi, dynamics ramp: intro naik, head puncak,
outro turun — memetakan pas ke arc Level 1.

**Alt 2 — Head(8)–Head-variasi(8), 16 bar, tanpa intro/outro
terpisah.** Sama total durasi, tapi tanpa "ruang napas" di awal/akhir
— piece langsung mulai penuh dan berhenti penuh, lebih cocok untuk
vibe yang butuh energi masuk, bukan vibe "tenang, ruang, lampu
menyala satu-satu" yang justru minta ruang masuk/keluar pelan.

## Pre-mortem

- Kelemahan Alt 1: 3 section pendek (4/8/4 bar) berarti tiap section
  py sedikit ruang untuk berkembang sendiri — cocok untuk piece
  pendek tapi tidak untuk piece panjang (bukan masalah di sini karena
  target memang ~1 menit).
- Kelemahan Alt 2: risiko statis-simetris (2 blok identik durasi)
  terasa seperti loop mentah tanpa arc masuk/keluar, bertentangan
  dengan citra "lampu menyala satu-satu" (proses gradual) di brief.

## Selected + alasan

**Alt 1** — kelemahan Alt 2 (tanpa ruang masuk/keluar gradual)
bertentangan langsung dengan citra sentral brief ("lampu menyala
satu-satu"), sementara kelemahan Alt 1 (section pendek) tidak relevan
untuk piece target 1 menit.

**Exact artifact:** `03-bentuk.md`.

**Unresolved/confidence:** tinggi — durasi matematis pas (16 bar × 3.75s
= 60.0s di 64bpm), tidak perlu bar filler.

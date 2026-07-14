# Rubrik kualitas — abc-notation

Diturunkan dari `quality-control.md` §15 (ABC and notation) — bagian dari
SOP lama, kini didistribusikan per modul.

Diisi subagent reviewer segar tanpa konteks generasi — skor + alasan 1
kalimat per kriteria.

| Kriteria | Skor (0-2) | Alasan (1 kalimat) |
|---|---|---|
| Header wajib ada dan bisa di-parse (`validate_abc.py` lulus tanpa error) | | |
| Ejaan not cocok dengan key dan fungsi harmonik selama masih praktis | | |
| Bar duration, pickup, tuplet, rest, tie, overlay, dan repeat/ending tervalidasi konsisten | | |
| Setiap voice tetap konsisten secara metrik (tidak ada voice yang kehilangan bar) | | |
| Arah swing/produksi tidak salah dikodekan sebagai note value yang keliru | | |
| Keterbatasan renderer (jika ada) diungkap eksplisit, bukan disembunyikan | | |

skala 0-2: 0 = tidak ada/kontradiktif, 1 = ada tapi lemah/tidak konsisten,
2 = jelas dan konsisten sepanjang artefak.

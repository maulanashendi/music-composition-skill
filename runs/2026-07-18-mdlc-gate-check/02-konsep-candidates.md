# 02 — Konsep Artistik: Kandidat & Seleksi (Level 1)

Kontrak artefak ramping (`candidate-selection-protocol.md`).

**Objective:** efek audible yang dikejar — pendengar merasa ditemani,
bukan ditinggal sendirian, oleh suasana habis hujan: tenang, hangat,
sedikit rindu tapi tidak sedih.

**Immutable constraints (dari brief):** ~1 menit, rhodes + upright bass
+ brush drum saja (tanpa lead horn terpisah), tempo lambat, tenang
tapi tidak sedih.

**Assumptions:** vibe preset `ballad` (lihat `01-brief.md`); key
diputuskan di sini sebagai bagian konsep, bukan menunggu Level 3.

## Kandidat

**A — "Lampu yang bertahan menyala" (statis-hangat).** Aesthetic
thesis: *satu progresi 4-chord yang tidak pernah benar-benar
"selesai" — tiap kali kembali ke akar (i), warnanya sedikit lebih
terang dari putaran sebelumnya, seperti lampu jalan yang tetap
menyala walau hujan sudah lama reda.* Struktural: loop harmoni yang
sama diulang, variasi datang dari dynamics + density comping
(intro sparse → head medium → outro sparse lagi), bukan dari
perubahan progresi. Key: D minor (warna minor tapi ekstensi mayor
9/maj9 di setiap bar untuk hangat).

**B — "Jalan basah, refleksi cahaya" (kontras-terarah).** Aesthetic
thesis: *melodi yang di head dimulai ragu-ragu (interval kecil,
banyak rest) lalu di outro nada yang sama muncul lagi tapi dengan
harmoni di bawahnya berubah jadi lebih terbuka — refleksi cahaya di
genangan air yang tadinya buram jadi jelas.* Struktural: 3 bagian
(intro-head-outro) dengan **progresi berbeda** di outro (rekontekstual,
bukan diulang persis) untuk membawa "arc" psikologis eksplisit.

## Pre-mortem (kelemahan sebelum memilih)

- Kelemahan A: karena progresi diulang persis, risiko monoton kalau
  dynamics/density tidak dieksekusi kuat oleh engine hilir — arc-nya
  bergantung penuh pada layer yang tidak ditulis LLM (dynamics ramp),
  bukan pada keputusan harmoni.
- Kelemahan B: rekontekstualisasi harmoni di outro butuh progresi
  kedua yang koheren secara voice-leading dengan progresi head —
  untuk piece 1-menit, ruang untuk membangun *dan* membayar arc itu
  sangat sempit (~4 bar outro), risiko terasa terburu-buru/tidak
  terjustifikasi secara musikal dibanding A yang lebih hemat scope.

## Selected + alasan

**A** dipilih meski kelemahannya (bergantung pada dynamics ramp yang
bukan keputusan LLM), karena kelemahan B (rekontekstualisasi harmoni
yang butuh ruang, sementara piece ini hanya ~16 bar/60 detik) lebih
berat untuk brief spesifik ini — durasi terlalu pendek untuk membayar
sebuah pivot harmoni dengan meyakinkan. **Graft:** ambil dari B ide
"nada yang sama muncul lagi di outro" sebagai niat melodi/motif (bukan
sebagai perubahan progresi) — dipetakan ke Level 4 (motif kembali di
outro, harmoni tetap loop A).

**Exact artifact:** `02-konsep.md`.

**Unresolved/confidence:** confidence sedang-tinggi — pilihan aman
untuk piece pendek; risiko monoton A dimitigasi lewat instruksi
dynamics ramp eksplisit per section di Plan (start/end tiap section
berbeda, lihat `plan.json`).

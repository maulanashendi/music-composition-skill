# 13-dynamics.md — Level 13: Dinamika dan Dramaturgi (Porch Light)

Tidak memakai klaim persentase — semua metrik di bawah diambil dari sumber terverifikasi: `notation_facts.py` (Level 4/7) dan hitung langsung `09-drums.json` (skrip Python, lihat catatan di bawah tabel).

## Tabel metrik observabel per section

| Section | Active voices | Note-attacks/bar (Rhodes+comping) | Register lead | Durasi not (ql) | Drum hits/bar (`09-drums.json`) |
|---|---|---|---|---|---|
| Intro (4 bar) | 1→2 (Rhodes pad saja, bass masuk bar 3-4) | 0 (RH diam total) | — (belum ada melodi) | — | **0.25** (hanya 1 tick di bar 4) |
| A1/A2 (8 bar tiap) | 3 (Rhodes+bass+drum, drum ringan) | melodi **2.6/bar** (21 not/8 bar, rest-ratio 0.276); comping **1.0/bar** (sustained, `07-comping-check.abc`: 56 not/16 bar antara A+B) | Tengah (A4 dominan, motif Level 4) | Melodi: 0.5-2.0 (shortest-longest, `notation_facts.py`); comping: 4.0 (sustained penuh, whole-bar) | **5.00** |
| B (8 bar) | 3 (semua aktif, density naik) | Melodi RH: **3.25/bar** (26 not/8 bar, rest-ratio 0.188, `notation_facts.py` pada `song.abc` bar 21-28); comping **1.0/bar** (rootless bergerak, top-note dalam band A-Bb-C, `07-comping.md`) | Tengah (C#4-B4, sama band register dengan A section — tidak melompat ke ekstrem) | Melodi: seluruhnya quarter note (ql 1.0, konsisten); comping: 4.0 (1 attack/bar, ditahan penuh) | **14.50** (puncak piece) |
| A3 head (8 bar) | 3 | Sama seperti A1/A2 (motif identik, Level 3) | Tengah (A4) | Sama seperti A1/A2 | **4.88** |
| Solo A1'/A2' (8 bar tiap) | 3 | **Sekarang dinotasi konkret di `song.abc`** — reuse identik materi A1/A2 (2.6/bar) ditambah 1 sisipan `A7/C#` di bar 6 tiap section (graft Level 2/3); Solo A3' (bar 61-68) sama tapi dinaikkan 1 oktaf penuh (graft register Level 10) | Tengah (A1'/A2'); satu oktaf lebih tinggi khusus A3' (±1 oktaf sesuai batas Level 10 field 3) | Sama seperti A1/A2 | **13.00** |
| Solo B' (8 bar) | 3 | **Sekarang dinotasi konkret** — identik not dengan B (3.25/bar, fakta sama seperti baris B di atas) | Sama seperti B (C#4-B4) | Sama seperti B | **14.50** |
| Head out (8 bar) | 3 | Sama A1 (simplified, tanpa ornamentasi, `06-arrangement.md`) | Tengah (A4) | Sama seperti A1 | **5.00** |
| Coda (4 bar) | 3→1 (fade ke Rhodes+bass saja, drum diam di bar 4) | 1 (voicing `F-A-C` ditahan atas bass D, `12-intro-ending.md`) | Tengah (A4, top-note sama seperti sepanjang piece) | 16.0 (ditahan penuh 4 bar, per desain "sustain/decay") | **1.50** (terendah kedua setelah Intro) |

**Sumber drum hits/bar:** dihitung dari `09-drums.json` (jumlah karakter bukan `.` per bar, dirata-rata per section) — bukan estimasi.

## Arc keseluruhan (dari tabel di atas, bukan klaim persentase)
Density drum naik dari **0.25 (Intro) → 5.0 (A) → 14.5 (B, puncak) → 4.88 (A3 resolusi) → 13.0 (Solo A) → 14.5 (Solo B) → 5.0 (Head out) → 1.5 (Coda)** — kurva ini **mengonfirmasi** klaim density arc di `06-arrangement.md` (sparse→medium→dense→resolusi→medium-dense solo→sparse→sparse) dengan angka terukur, bukan cuma prosa.

## Micro-apex (wajib, mekanisme non-volume)

- **Micro-apex utama (piece level): bar 8 A3 head** — **drop groove**: kick sengaja dihilangkan (one-off imperfection tunggal seluruh lagu, `09-drums.json`) tepat di bar resolusi paling penting (kembali ke tema sebelum solo) — bass+Rhodes mendarat di `F/D` sendirian tanpa kick, membuat momen itu berbeda dari 3 resolusi lain (A1/A2/Solo-A3') yang sama persis.
- **Intro:** **delayed entrance** — bass masuk bar 3 (bukan bar 1), bukan volume naik.
- **A1/A2/Solo (setiap A):** **ruang terjadwal** — bar 5 motif ditahan 4 ketuk penuh (`04-melody.abc` Tahap 7) tanpa nada baru — "restrained" section ini punya momennya sendiri, bukan datar tanpa peak.
- **B section:** **dissonance singkat** — bar 14 (`Ebmaj7`, klasifikasi `luar-key` paling "outside" di seluruh piece, `03-harmony.md`) adalah titik harmoni paling menyimpang, bukan lewat volume.
- **Coda:** **silence** — bar 4 diam total (drum berhenti sepenuhnya) setelah cymbal swell bar 3 — penutup lewat ruang kosong, bukan fade volume gradual semata.

Tidak ada section berlabel "restrained" tanpa micro-apex terdefinisi — memenuhi gate Level 13.

## Referensi
Fakta notasi: `04-melody.abc`, `07-comping.md`. Drum grid: `09-drums.json`. Harmoni: `03-harmony.md`. Arrangement: `06-arrangement.md`.

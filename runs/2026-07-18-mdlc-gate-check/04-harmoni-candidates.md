# 04 — Peta Harmoni: Kandidat & Seleksi (Level 3)

**Objective:** loop 4-bar hangat-minor yang tidak "pergi ke mana-mana"
(Level 1), cukup warna (9th/maj9) untuk "hangat".

**Immutable constraints:** key D minor, loop dipakai persis di intro
(terpotong) dan head (2×), direkontekstualisasi ringan di outro
(mundur, bukan progresi baru).

**Assumptions:** semua simbol memakai grammar chord validator
(`root[A-G][#b]? + quality(maj|min|m|dim|aug|sus2|sus4)? +
ext(5|6|7|9|11|13)? + ...`) — dicek manual terhadap `contract.md`
sebelum ditulis ke kandidat.

## Kandidat

**Utama — i–iv–bVII–bIII (Dm9–Gm9–Cmaj9–Fmaj9).** Per bar: bar1 Dm9,
bar2 Gm9, bar3 Cmaj9, bar4 Fmaj9. Warna: minor tapi tiap chord ber-9,
2 di antaranya maj9 (hangat). Gerakan akar: D→G (4th naik) → C (4th
naik) → F (4th naik) → kembali D (4th naik) — sepenuhnya circle-of-
fourths, familiar/tenang, tak ada kejutan harmonik.

**Alt lebih sederhana — i–iv–i–v (Dm7–Gm7–Dm7–Am7).** Bar1 Dm7, bar2
Gm7, bar3 Dm7, bar4 Am7. Lebih statis/repetitif (root kembali di bar
3), warna lebih polos (7th saja, tanpa 9th) — kurang "hangat" tapi
lebih aman/predictable.

**Alt lebih berani — reharm dgn secondary dominant (Dm9–G7alt/A–
Cmaj9–A7(b9)).** Bar1 Dm9, bar2 "G7(b9)/A" (dominan sekunder menuju
Dm berikutnya, dgn slash bass), bar3 Cmaj9, bar4 A7(b9) (dominan V
kembali ke Dm). Lebih ada tarikan/tegangan tiap 2 bar, tapi risiko
"tidak sesederhana itu" untuk brief yang eksplisit minta tenang.

## Pre-mortem

- Kelemahan Utama: circle-of-fourths sangat familiar/aman — sedikit
  risiko generik/klise (tapi klise di sini justru cocok untuk vibe
  "familiar, menenangkan").
- Kelemahan Alt sederhana: tanpa 9th, kurang memenuhi requirement
  "hangat" eksplisit dari Level 1.
- Kelemahan Alt berani: slash-bass dominan sekunder menambah
  kompleksitas voice-leading utk piece 1 menit yang justru minta
  simplicity; risiko melodi Level 4 harus bekerja lebih keras
  menyesuaikan tension per 2 bar, mengurangi ruang untuk "rest/napas"
  yang jadi ciri vibe ini.

## Selected + alasan

**Utama (i-iv-bVII-bIII)** — memenuhi "hangat" (9th/maj9) tanpa
kompleksitas tambahan Alt berani yang bertentangan dengan "tenang",
dan lebih hangat dari Alt sederhana yang kelemahannya (tanpa 9th)
langsung melanggar requirement Level 1.

**Exact artifact:** `04-harmoni.md`.

**Unresolved/confidence:** tinggi — 4 simbol chord tervalidasi manual
terhadap grammar regex validator sebelum ditulis (lihat catatan di
`04-harmoni.md`).

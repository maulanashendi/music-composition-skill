# 04 — Peta Harmoni (Level 3)

1. **Level:** 3 — Peta Harmoni.
2. **Aesthetic thesis (rujukan):** lihat `02-konsep.md`.
3. **Immutable constraints:** key D minor, loop 4-bar dipakai
   berulang/direkontekstualisasi (Level 1-2).
4. **Assumptions:** simbol chord ditulis niat-level (simbol saja, TANPA
   voicing pitch — lihat doktrin), dicek manual lolos grammar
   validator sebelum ditulis ke `plan.json`.
5. **Decision:** loop **Dm9 – Gm9 – Cmaj9 – Fmaj9** (i–iv–bVII–bIII),
   1 chord per bar.
6. **Rationale:** circle-of-fourths yang familiar (tenang, tak
   mengejutkan) + tiap chord ber-9th/maj9 (hangat) — persis memenuhi
   Level 1 tanpa kompleksitas voice-leading tambahan.
7. **Alternatives considered/rejected:** Alt sederhana (Dm7-Gm7-Dm7-
   Am7, kurang hangat) dan Alt berani (reharm dominan sekunder, terlalu
   kompleks utk 1 menit) — lihat `04-harmoni-candidates.md`.
8. **Interaction with other levels:** Level 4 (melodi) menaruh target
   tone di 3rd/9th tiap downbeat bar baru (persis rekomendasi warning
   target-tones di `plan-verifying`); Level 6 (arrangement) memakai
   comp style `rootless` (bukan block penuh) supaya warna 9th terdengar
   jelas, bukan tertutup.

## Peta per section (bar:chord)

- **Intro (4 bar, dipotong 2 chord):** bar1 Dm9 — bar3 Gm9 (chord
  ditahan 2 bar masing-masing, comp sparse).
- **Head (8 bar, loop penuh 2×):** bar1 Dm9, bar2 Gm9, bar3 Cmaj9,
  bar4 Fmaj9, bar5 Dm9, bar6 Gm9, bar7 Cmaj9, bar8 Fmaj9.
- **Outro (4 bar, mundur — rekontekstualisasi ringan, bukan progresi
  baru):** bar1 Fmaj9, bar2 Cmaj9, bar3 Gm9, bar4 Dm9 (loop yang sama
  dibaca terbalik, memberi rasa "menutup" tanpa chord baru).

## Verifikasi manual grammar (sebelum ditulis ke `plan.json`)

Semua 4 simbol dicek terhadap grammar `contract.md`/`validator.py`
(`root[A-G][#b]? + quality? + ext? + add? + alterasi? + slash?`):
`Dm9` (root D, quality m, ext 9) — ok. `Gm9` — ok. `Cmaj9` (quality
maj, ext 9) — ok secara grammar. `Fmaj9` — ok secara grammar. Tidak ada
simbol di luar grammar; tidak perlu `CHORD_SYMBOL_OVERRIDES` (diduga).

> **Koreksi retroaktif (setelah `pyengine validate` iterasi 1 —
> lihat `verify-log.md` dan Temuan #1 `gate-report.md`):** `Cmaj9` dan
> `Fmaj9` lolos grammar whitelist TAPI ditolak `music21.ChordSymbol`
> ("Invalid chord abbreviation 'maj9'"). Diganti ke **`Cmaj7add9`** /
> **`Fmaj7add9`** (pitch set identik — root,3,5,7,9 — lolos grammar
> DAN music21). Peta section di bawah dan `plan.json` sudah memakai
> simbol yang dikoreksi ini. `harmony.md` (referensi jazz-composing)
> masih mencontohkan `Fmaj9` sebagai simbol "standar" — itu sendiri
> bagian dari temuan gate ini, bukan diperbaiki di sesi ini (di luar
> mandat "jangan mengubah skill").

9. **Risks:** progresi diulang persis di head (2×) — mitigasi lewat
   variasi comp density (Level 6) dan melodi (Level 4) antar
   pengulangan.
10. **Confidence:** tinggi.
11. **Next action:** lanjut Level 4 — Desain Melodi.

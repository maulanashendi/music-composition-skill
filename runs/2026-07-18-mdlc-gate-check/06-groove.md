# 06 — Ritme/Groove (single-shot)

**Groove pattern (section-level, `contract.md` groove library):**
`neo-soul-core` — satu-satunya groove terimplementasi saat ini di
`GROOVE_LIBRARY`, dipakai di ketiga section (intro/head/outro).

**Drum pattern (voice-level, `DRUM_PATTERN_LIBRARY`):** `ballad-brush`
— dipilih karena brief eksplisit minta "brush drum" dan pattern ini
namanya persis mencerminkan itu (vs. `neo-soul-basic` yang lebih untuk
groove neo-soul standar, bukan brush/ballad). Dipakai di semua
section (intro/head/outro) — tidak ada pattern lain yang lebih cocok
untuk brush-ballad di library saat ini.

Tidak menulis tick offset, swing ratio, atau grid hit manual — itu
tanggung jawab `pyengine` (deterministik, ber-`meta.seed`).

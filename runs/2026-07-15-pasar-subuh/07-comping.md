# 07-comping.md — Level 7: Desain Comping dan Voicing (Rhodes)

## Comping chart per section

| Section (bar) | Density | Cell |
|---|---|---|
| Intro/Layer-Drum (1-8) | tacet | — (Rhodes belum masuk) |
| Layer-Rhodes (9-12) | sparse, 1 attack/bar (whole-note pad) | Cell "sustained pad" — **justifikasi uniform 1 attack/bar**: sax belum bermain sama sekali di section ini (tacet s.d. bar 15), jadi tidak ada peta napas lead untuk direspons; comping seragam di sini sengaja, bukan lupa memvariasikan (memenuhi gate `level-07-comping-voicing.md`). |
| Dip (13-14) | tacet | Rhodes mundur/diam — bagian dari "held breath" (`02-form.md`) |
| Sax+Call-Response (15-20) | interaktif, ≥3 cell berbeda (lihat di bawah) | lihat tabel napas-lead |
| Coda (21-24) | sparse-warm, sustained | Cell "sustained pad" reprise |

## ≥3 comping cell berbeda + peta napas lead (wajib)

| Bar | Sax (napas/aktivitas) | Comping cell Rhodes | Kenapa |
|---|---|---|---|
| 15 | Motif call aktif (`z E E z G G z B`) | **diam** (mengisi ruang dengan tidak bermain, membiarkan call sax berdiri sendiri) | Call perlu berdiri sendiri dulu sebelum dijawab — respons prematur akan menabrak motif. |
| 16 | Sax diam (napas, jawaban giliran Rhodes) | **Cell 1 — held/sustained pad**: `[CEA]` Fmaj7, 1 attack ditahan penuh 1 bar | Mengisi persis ruang yang ditinggalkan sax — call-response literal. |
| 17 | Motif dikembangkan, register naik, banyak rest internal | **Cell 2 — short syncopated stab**: `[G,DB]` G7, stab pendek di offbeat sela-sela rest sax | Mengisi celah-celah kecil tanpa menabrak nada sax yang sedang aktif. |
| 18 | Sax diam sebagian (jawaban kedua) | **Cell 3 — delayed answer**: `[G,DB]` Em7, masuk agak terlambat dari downbeat (bukan tepat di beat 1) | Delayed entrance membuat dialog terasa dua pihak yang benar-benar saling menunggu, bukan mekanis. |
| 19 | Micro-apex — satu nada tinggi tipis (Ab) berdiri sendiri | **Cell 4 — deliberate silence**: Rhodes diam total | Micro-apex Level 13 butuh mekanisme non-volume (nada tunggal berdiri sendiri) — comping ramai di sini akan menenggelamkan efeknya. |
| 20 | Sax turun/mereda | Rhodes kembali masuk ringan mengikuti split-chord Em7\|Dm7 | Menyertai resolusi lokal sebelum coda. |
| 21-24 | Reprise motif (enclosure), mereda | Cell 1 reprise — `[FAB]` Dm6add9, sustained | Menutup dengan tekstur hangat yang menyertai (bukan menonjol). |

**Gate comping ≥3 cell + napas lead: terpenuhi** — 4 cell berbeda (held/sustained, short syncopated stab, delayed answer, deliberate silence) dipetakan eksplisit ke ruang napas sax.

## Cek fakta notasi (voice-leading top-note, wajib)

Dijalankan: `notation_facts.py comping-check.abc --voice 1` atas 4 voicing kunci (Fmaj7 bar16, G7 bar17, Em7 bar18, Dm6add9 bar24):

| Bar (chord) | Voicing (bawah→atas) | Top-note (fakta script) |
|---|---|---|
| 16 (Fmaj7) | C4, E4, A4 | **A** |
| 17 (G7) | G3, D4, B4 | **B** |
| 18 (Em7) | G3, D4, B4 | **B** |
| 24 (Dm6add9) | F4, A4, B4 | **B** |

Klaim voice-leading: top note bergerak **A → B → B → B** — A(16)→B(17) stepwise naik M2 (smooth), B(17)→B(18) **common tone statis** (G7 dan Em7 berbagi 3 chord tone: G,B,D — voicing sengaja dipilih identik untuk mewujudkan ini), B(18)→...→B(24) callback: nada top yang sama muncul lagi di chord akhir coda, sebuah gema kecil yang memperkuat rekontekstualisasi (B adalah nada yang sama yang juga jadi fokus bass ostinato dan reprise sax). **Semua terverifikasi cocok fakta script** — tidak ada ketidakcocokan top-note yang perlu direvisi.

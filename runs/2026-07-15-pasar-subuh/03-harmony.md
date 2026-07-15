# 03-harmony.md — Level 3: Peta Harmoni

Tonal center: D Dorian (D E F G A B C). Harmonic rhythm: mayoritas 1 chord/bar (bar 1-19, 21-24), dengan 1 bar harmonic-rhythm cepat (bar 20 = 2 chord/bar, Em7|Dm7) sebagai variasi sengaja — menghindari cliche "harmonic rhythm seragam full-piece" (`cliche-register.md`).

## Skeleton + fungsi harmonik per bar

| Bar | 1-9 | 10 | 11 | 12 | 13-14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 | 24 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Chord | Dm7 | Dm9 | Dm7 | Dm9 | Dm7 | Em7 | Fmaj7 | G7 | Em7 | G7b9#5 | Em7\|Dm7 | G7 | Cmaj9 (=CM9) | Dm9 | Dm6/9 (=Dm6add9) |
| Fungsi | tonic (i7) | tonic+color | tonic (i7) | tonic+color | tonic (i7), diam sengaja (dip) | predominant (ii7) | modal color (bIII) | dominant-color Dorian (IV7, backdoor) | predominant (ii7) | chromatic departure/outside (micro-apex) | predominant→tonic (resolusi lokal) | dominant-color (IV7, backdoor) | bVII (backdoor pre-resolusi) | tonic+color | **tonic rekontekstualisasi final** |

Catatan penulisan simbol: prosa jazz-standar "Cmaj9"/"Dm6/9" ditulis di ABC sebagai `CM9`/`Dm6add9` (spelling yang bisa di-parse `music21.harmony.ChordSymbol` — `Cmaj9`/`Dm6/9` gagal parse, lihat cek fakta di bawah). Simbol `G7alt` di prosa = `G7b9#5` di ABC.

## Tension map (per section, `02-form.md`)
- Intro (1-4): **stabil** — Dm7 pedal, tonic, tanpa gerakan. Bass ostinato sendirian.
- Layer-Drum (5-8): **stabil** — harmoni tidak berubah (kontras section ini murni ritmis, drum masuk).
- Layer-Rhodes (9-12): **stabil-berwarna** — Dm9 muncul di bar genap (10,12), ekstensi warna tanpa mengubah fungsi tonic.
- Dip (13-14): **stabil, diam sengaja** — Dm7 polos, tidak ada materi harmonik baru (syarat "held breath" dari Level 2).
- Sax+Call-Response/micro-apex (15-20): **meningkat** — ii(Em7) → bIII(Fmaj7) → IV7-Dorian-backdoor(G7) → ii(Em7) → **outside G7b9#5 (bar 19, puncak tension)** → resolusi lokal (Em7|Dm7 split, bar 20).
- Coda (21-24): **menurun ke resolusi hangat** — G7(backdoor) → Cmaj9/bVII → Dm9 → **Dm6/9 final (rekontekstualisasi: B, nada ostinato ke-6, jadi chord tone penuh)**.

## Cek fakta notasi (`notation_facts.py`, wajib sebelum Level 4)

Dijalankan: `cd skills/abc-notation/scripts && uv run --with music21 --with pretty_midi python notation_facts.py ../../../runs/2026-07-15-pasar-subuh/harmony-check.abc --voice 1`

Ringkasan hasil relevan (chord-vs-key per bar):
- Bar 1-18, 20-24: seluruhnya `chord-vs-key=diatonik` — cocok dengan label "tonic"/"predominant"/"modal color"/"backdoor" di atas (semua chord memang diatonik terhadap D Dorian).
- **Bar 19 (`G7b9#5`): `chord-vs-key=borrowed`** — cocok persis dengan label artefak "chromatic departure/outside (micro-apex)"; fakta objektif mengonfirmasi klaim teori, bukan kontradiksi.
- Bar 24 (`Dm6add9`): chord tones dilaporkan `D, F, A, B, E` — **B ada di daftar chord tone**, mengonfirmasi mekanisme rekontekstualisasi Level 1/12: nada B (bagian ostinato) sekarang benar-benar chord tone (6th), bukan cuma warna mengambang.
- Tidak ada chord `unparsed` di seluruh 24 bar — semua simbol berhasil di-parse script.

**Kecocokan label teori vs fakta: 100% cocok, tidak ada revisi diperlukan** di level ini (berbeda dari catatan RED-FLAGS soal `Abmaj7`/`Ebmaj7` yang salah label "borrowed" — di sini label "borrowed" justru benar dipakai untuk bar 19, dikonfirmasi script sendiri).

## Kandidat & seleksi
Lihat `03-harmoni-candidates.md` — Progresi utama di atas dipilih oleh selector segar dari 3 kandidat (utama, sederhana, berani).

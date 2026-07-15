# Level 3 — Peta Harmoni: kandidat & seleksi

## Objective
Progresi 24 bar di D Dorian yang mendukung: bass ostinato D+B dipertahankan hampir sepanjang piece; tension rendah di section awal (Intro/Layer-Drum/Layer-Rhodes/Dip), naik di section micro-apex (bar 15-20), lalu resolusi hangat rekontekstualisasi di coda (B — nada ke-6 Dorian yang selama ini "mengambang" sebagai warna ostinato — menjadi chord tone penuh di chord akhir).

## Immutable constraints
- Key: D Dorian (D E F G A B C).
- Bar count = 24, mengikuti section `02-form.md`.
- Bar 1-14 (Intro..Dip) harus TETAP tonic/rendah-tension (bass ostinato sendirian s.d. dip).
- Bar 24 (chord akhir) wajib membuat B (nada ke-6, bagian ostinato) jadi chord tone penuh — mekanisme rekontekstualisasi Level 1.

## Kandidat

### Progresi utama
| Bar | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Chord | Dm7 | Dm7 | Dm7 | Dm7 | Dm7 | Dm7 | Dm7 | Dm7 | Dm7 | Dm9 | Dm7 | Dm9 |

| Bar | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 | 24 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Chord | Dm7 | Dm7 | Em7 | FMaj7 | G7 | Em7 | G7alt | Em7\|Dm7 | G7 | Cmaj9 | Dm9 | Dm6/9 |

Fungsi: Dm7=tonic(i7), Em7=predominant(ii7), FMaj7=modal color(bIII), G7=dominant-color Dorian(IV7, "backdoor" ke i/bVII), G7alt=chromatic departure/outside (micro-apex, bar 19), Cmaj9=bVII (backdoor pre-resolusi), Dm6/9=tonic rekontekstualisasi final (B jadi chord tone ke-6).
Harmonic rhythm: 1 chord/bar mayoritas, kecuali bar 20 (2 chord/bar, Em7|Dm7) — variasi sengaja supaya harmonic rhythm tidak seragam sepanjang piece (menghindari cliche register).

### Alternatif lebih sederhana
Seluruh piece **Dm7 statis** bar 1-20, lalu Am7(bar 21) | Cmaj7(22) | Dm7(23) | Dmaj7(24, Picardy-third literal, bukan Dm6/9). Tidak ada modal color (FMaj7/G7/Cmaj9), tidak ada outside (G7alt). Risiko: rekontekstualisasi jadi terlalu literal (major 3rd penuh, bukan warna Dorian minor-6/9) — kurang halus, dan tidak ada tension map yang bisa didengar di section micro-apex (bar 15-20 harmoninya identik dengan intro, kontras hilang).

### Alternatif lebih berani
Tambahkan tritone substitution & side-slip: bar 16 diganti `Abmaj7` (chromatic mediant dari FMaj7, side-slip sesaat), bar 19 (micro-apex) diganti `Ab7alt` (tritone sub dari G7alt, lebih jauh dari tonal center), bar 22 diganti `Db13` (tritone sub dari G7, backdoor lebih eksotis daripada Cmaj9). Risiko: kompleksitas brief hanya "menengah" — tritone sub ganda + side-slip berisiko terdengar terlalu "outside" untuk piece restrained 24-bar yang temanya "tenang, hangat", bisa mengaburkan kejelasan ostinato/pedal yang jadi identitas utama Level 1.

## Selected + alasan
(diisi setelah verdict selector segar)

## Exact artifact
Pemenang dituliskan ke `03-harmony.md` + hasil `notation_facts.py`.

## Unresolved/confidence
- G7alt voicing eksak (nada alterasi mana: b9/#9/#5) dikunci saat menulis ABC final Level 3, dicek fakta objektifnya via `notation_facts.py`.

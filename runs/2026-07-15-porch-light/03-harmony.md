# 03-harmony.md — Level 3: Peta Harmoni (Porch Light)

Tonal center: **D Dorian** (D E F G A B C — B natural, tanpa key signature). Harmonic rhythm: A section sangat lambat (1 voicing tertahan 6 bar, `F/A`), lalu bergerak di 2 bar terakhir (`F/G`→`F/D`); B section cepat (1 chord/bar) — kontras eksplisit sesuai fungsi "B = kontras" (Level 2).

Device kunci: voicing atas **F major triad (F-A-C)** ditahan literal sama persis di bar 1-6 setiap A section; hanya **not bass** yang bergerak (A pedal → G → D). Karena voicing atas tidak berubah sama sekali, resolusi di bar 8 murni efek reinterpretasi bass, bukan perubahan chord baru.

## Skeleton + fungsi harmonik per bar (A section — dipakai identik di A1/A2/A3)

| Bar | 1-6 | 7 | 8 |
|---|---|---|---|
| Chord | `F/A` | `F/G` | `F/D` |
| Fungsi | tonic-ambigu / suspended pedal (dominant-pedal mengambang) | predominant (bass bergerak, upper structure sama) | tonic resolution (=`Dm9` penuh) |

## Skeleton + fungsi harmonik per bar (B section — kontras)

| Bar | 9 | 10 | 11 | 12 | 13 | 14 | 15-16 |
|---|---|---|---|---|---|---|---|
| Chord | `Bbmaj7` | `A7b9#5` | `Gm9` | `C7b9#5` | `FM9` | `Ebmaj7` | `A7b9#5` |
| Fungsi | modal interchange (bVI, luar-key) | dominant altered | predominant (iv, borrowed dari Aeolian) | secondary dominant altered (borrowed) | **diatonik bIII** (relative major — bukan chromatic mediant, lihat catatan revisi di bawah) | modal interchange (bII-ish, luar-key) | dominant approach kembali ke A3 (2 bar) |

## Tension map

- **A (bar 1-6):** stabil-mengambang, tension rendah tapi terasa "unresolved" (voicing sama diulang tanpa gerak).
- **A bar 7:** mulai bergerak (predominant, bass G).
- **A bar 8:** **resolusi** — voicing identik, bass tonic D.
- **B bar 9:** terbuka (modal interchange, luar-key — lompatan warna pertama).
- **B bar 10:** dominan altered (naik).
- **B bar 11:** predominant borrowed (turun sedikit, iv Aeolian).
- **B bar 12:** dominan sekunder altered (tinggi).
- **B bar 13:** **diatonik bIII** — justru titik paling "konsonan"/terbuka di B, bukan puncak tension; kontras B section datang dari gerak cepat (1 chord/bar) dan warna borrowed di sekitarnya, bukan dari bar ini sendiri.
- **B bar 14:** modal interchange (bII-ish, luar-key — paling "outside" di section ini).
- **B bar 15-16:** dominan kuat menahan, tension tertinggi, menunggu resolusi ke A3 bar 1 (`F/A`, kembali mengambang).

## Progresi solo chorus (graft Level 2)
Struktur sama persis, kecuali bar 6 tiap A section (hanya saat solo, bukan head): sisipan secondary dominant singkat `A7/C#` di beat 3-4, sebelum kembali ke `F/G`→`F/D` di bar 7-8. Detail voicing/register solo (variasi oktaf A2'/A3') diturunkan ke Level 10 (solo map).

## Cek fakta notasi (`notation_facts.py`, wajib sebelum Level 4)

Dijalankan: `cd skills/abc-notation/scripts && uv run --with music21 --with pretty_midi python notation_facts.py ../../../runs/2026-07-15-porch-light/harmony-check.abc --voice 1`

File `harmony-check.abc` berisi A1 (bar 1-8) + B (bar 9-16) + A3 (bar 17-24) — A2 dilewati karena identik-persis dengan A1/A3 (bukan kelalaian, lihat catatan di `03-harmoni-candidates.md`).

Ringkasan hasil:
- Bar 1-8, 17-24 (`F/A`×6, `F/G`, `F/D`): seluruhnya **`chord-vs-key=diatonik`** — cocok dengan label "tonic-ambigu/predominant/resolution" (semua chord tone A/C/F/D/G ada di D Dorian).
- Bar 9 (`Bbmaj7`) dan bar 14 (`Ebmaj7`): **`chord-vs-key=luar-key`** — cocok dengan label "modal interchange".
- Bar 10, 12, 15, 16 (`A7b9#5`, `C7b9#5`): **`chord-vs-key=borrowed`**.
- Bar 11 (`Gm9`): **`chord-vs-key=borrowed`** — mengonfirmasi bahwa iv di sini memang borrowed dari Aeolian (Bb menggantikan B natural Dorian), bukan diatonik Dorian murni seperti awalnya diasumsikan implisit.
- **Bar 13 (`FM9`): `chord-vs-key=diatonik`** — **REVISI dari draft kandidat**: label awal di `03-harmoni-candidates.md` menyebut ini "chromatic mediant", tapi fakta notasi menunjukkan seluruh chord tone (F,A,C,E,G) ada di D Dorian — ini **bIII diatonik** (relative major), bukan chromatic. Tension map di atas sudah dikoreksi (bar 13 = titik paling konsonan di B, bukan puncak tension); lihat juga catatan revisi.
- Tidak ada chord `unparsed` setelah perbaikan ejaan `Fmaj9`→`FM9` (spelling yang bisa di-parse `music21.harmony.ChordSymbol`; `Fmaj9` sempat dilaporkan `unparsed` pada percobaan pertama).

**Kecocokan label teori vs fakta: 1 ketidakcocokan ditemukan dan diperbaiki** (bar 13, chromatic mediant → diatonik bIII) — dicatat di sini per gate Level 3, bukan disembunyikan.

## Kandidat & seleksi
Lihat `03-harmoni-candidates.md` — progresi pedal/slash-chord di atas dipilih oleh selector segar dari 3 kandidat (utama, sederhana ii-V-I, quartal/polychord berani).

# Level 4 candidates — Porch Light

## Objective
Motif inti untuk A section (atas `F/A`, voicing suspended dari Level 3) yang punya identitas jelas, cocok dikembangkan lewat 3× repeat (A1/A2/A3) tanpa terasa monoton, dan selaras karakter "hangat, reflektif, late-night mellow".

## Immutable constraints
- Berlaku atas chord `F/A` (Level 3), 4/4, 86 BPM, D Dorian.
- Harus punya "ruang" (rest) — brief menuntut karakter reflektif, bukan padat.
- Fakta objektif wajib dari `notation_facts.py` (dijalankan pada tiap kandidat, file `04-melody-cand-{a,b,c}.abc`).

## Assumptions
- Motif ditulis 2 bar (1 bar aktif + 1 bar resolusi/ruang), mewakili bar 1-2 dari 8-bar A section; bar 3-8 (termasuk resolusi ke `F/D` bar 8) adalah pengembangan motif ini, bukan bagian dari fragmen kandidat.

## Kandidat

### A — "Leap and arpeggio descent"
```
X:1
T:Motif Candidate A
M:4/4
L:1/4
K:DDor
V:1
[V:1] "F/A" D A F C | "F/A" A2 z2 |]
```
**Intent (≤1 kalimat):** Leap perfect fifth lalu recovery lewat arpeggio turun, mendarat di A yang ditahan sebagai "pertanyaan" terbuka.

**Fakta objektif (`notation_facts.py`):**
- 5 pitch (D,A,F,C,A), 1 rest (rest-ratio 0.167).
- Interval berurutan: D→A **+7 Perfect Fifth naik**; A→F **-4 Major Third turun**; F→C **-5 Perfect Fourth turun**; C→A **+9 Major Sixth naik**.
- Relasi ke chord `F/A`: D=**tension-diatonik**; A,F,C=**chord-tone**.

### B — "Static repeated-note, chromatic neighbor"
```
X:1
T:Motif Candidate B
M:4/4
L:1/8
K:DDor
V:1
[V:1] "F/A" A2 A2 _B1 A1 A2 | "F/A" z2 A2 F2 z2 |]
```
**Intent (≤1 kalimat):** Nada tunggal (A) diulang dengan satu neighbor kromatik (Bb) dan sinkopasi ritmis — device "kesamaan" thesis Level 1 dipindah ke level melodi, bukan hanya harmoni.

**Fakta objektif:**
- 7 pitch (A,A,Bb,A,A,A,F), 2 rest (rest-ratio 0.222).
- Interval berurutan: unison, **+1 Minor Second naik** (A→Bb), **-1 Minor Second turun** (Bb→A), unison, unison, **-4 Major Third turun** (A→F).
- Relasi ke chord: A=**chord-tone** (4×); **Bb=outside** (bukan chord-tone maupun diatonik D Dorian — cocok dengan intent "chromatic neighbor"); F=**chord-tone**.

### C — "Angular chromatic-passing line"
```
X:1
T:Motif Candidate C
M:4/4
L:1/8
K:DDor
V:1
[V:1] "F/A" F2 D2 _E2 C2 | "F/A" A4 z4 |]
```
**Intent (≤1 kalimat):** Garis turun lebih angular dengan warna kromatik (Eb) di tengah, lebih aktif/modern dibanding A/B.

**Fakta objektif:**
- 5 pitch (F,D,Eb,C,A), 1 rest (rest-ratio 0.167).
- Interval berurutan: F→D **-3 Minor Third turun**; D→Eb **+1 Minor Second naik**; Eb→C **-3 Minor Third turun**; C→A **+9 Major Sixth naik**.
- Relasi ke chord: F,C,A=**chord-tone**; D=**tension-diatonik**; **Eb=outside**.
- **Catatan koreksi vs intent awal:** Eb di sini bukan "chromatic passing tone" klasik menuju C secara stepwise (interval Eb→C adalah lompatan minor third, bukan langkah/stepwise resolution) — deskripsi yang akurat: Eb berfungsi sebagai upper-chromatic-neighbor terhadap D yang kemudian melompat ke C, bukan pendekatan kromatik halus. Dicatat di sini supaya tidak diklaim sebagai "smooth chromatic approach" yang salah.

## Selected + alasan
**Terpilih: Kandidat B — "Static repeated-note, chromatic neighbor".**

Alasan (efek audible, bukan deskripsi):
- **Paling cocok secara struktural dengan thesis Level 1.** Thesis-nya adalah "satu voicing diulang tanpa berubah, baru resolusi di bar terakhir" — sumbu harmoni statis. B memindahkan device yang sama persis ke melodi: nada tunggal (A) diulang, hanya diwarnai satu neighbor kromatik (Bb). Ini artinya harmoni dan melodi bergerak sejalan (kedua sumbu "diam lalu lepas"), persis yang diminta brief agar resolusi terasa *inevitable*, bukan trik satu-lapis. A dan C, sebaliknya, sudah bergerak/melompat besar di motif itu sendiri — mereka mendahului momen resolusi, membuat sumbu melodi dan harmoni tidak sinkron.
- **Interval terkecil dari ketiganya secara audible = paling "intim".** Interval terbesar di B hanya turun ke unison/m2 sampai m3 (A→F di akhir). A punya lompatan P5 naik lalu M6 naik lagi; C bahkan lebih angular (m3/m2/m3/M6). Untuk karakter "hangat, reflektif, intim, late-night mellow", lompatan besar (P5/M6) di awal frasa terdengar lebih ekstrover/assertif — cocok untuk klimaks di B section, bukan untuk head A yang sengaja "menahan".
- **Rest-ratio tertinggi (0.222 vs 0.167) dan paling "berbunyi seperti nafas".** Brief eksplisit menuntut motif berruang, bukan padat — B dengan 2 rest tersinkopasi (z2 di awal bar 2, z2 di akhir) memberi jeda yang terasa disengaja, bukan sekadar penutup kalimat seperti A/C.
- **Paling tahan diulang 3x tanpa berubah sendiri.** Karena identitasnya justru ADALAH pengulangan-dengan-warna-minimal (bukan garis melodi yang harus "diingat" lewat kontur besar), device ini secara desain sudah kompatibel dengan repetisi harfiah A1/A2/A3 — variasi antar-repeat cukup dibawa oleh pocket yang mengendur (Level 2), motif itu sendiri tidak perlu berubah untuk tetap menarik, malah kalau berubah terlalu banyak akan merusak efek "kesamaan yang disengaja". A dan C punya kontur naik-turun yang lebih "menceritakan sesuatu" sekali jalan — diulang identik 3x berisiko terasa seperti pertanyaan yang sama diajukan 3x tanpa berkembang (monoton), karena kontur besar biasanya menuntut jawaban/perkembangan yang di sini justru ditahan sampai bar 8.
- **Bb sebagai outside-tone adalah warna yang pas ukurannya.** Satu chromatic neighbor (bukan chromatic run seperti Eb di C) memberi cukup "gigitan" untuk menghindari terdengar datar, tanpa membuat motif terasa aktif/modern secara berlebihan — pas untuk kompleksitas harmonik "menengah" di brief.

**Graft dari kandidat yang kalah:** pinjam gestur akhir Kandidat A — nada ditahan lalu rest (`A2 z2`) — sebagai varian opsional untuk **A3** (repeat terakhir sebelum masuk B section): ganti not F penutup bar 2 B (`...F2 z2`) dengan A yang ditahan lebih panjang (`A4`) khusus di A3, supaya repeat terakhir terasa sedikit "menggantung"/belum selesai tepat sebelum climax lembut di B — echo dari lompatan P5 D→A milik A tanpa mengambil lompatannya, hanya nuansa "menahan di nada tinggi"-nya. Ini opsional, bukan wajib; A1/A2 tetap memakai versi B apa adanya.

## Exact artifact
Pemenang akan diturunkan ke `04-melody.abc`.

## Unresolved/confidence
Confidence tinggi pada pilihan B (interval kecil + rest-ratio tinggi + sinkron dengan thesis stasis-lalu-lepas Level 1 adalah argumen objektif, bukan preferensi rasa). Graft A3 (`A4` menggantikan `F2 z2` di bar 2) bersifat opsional — perlu dikonfirmasi ulang saat Level 5/6 menuliskan pengembangan motif penuh 8-bar, karena fragmen kandidat di sini hanya mewakili bar 1-2 dari section 8-bar.

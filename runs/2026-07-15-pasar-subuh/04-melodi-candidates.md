# Level 4 — Desain Melodi: kandidat & seleksi

## Objective
Motif inti sax lead yang pertama muncul di bar 15 (Em7→Fmaj7, awal section micro-apex), cukup kuat untuk dikenali/diingat, lalu dikembangkan & direprise di coda (rekontekstualisasi).

## Immutable constraints
- Harus dimulai di konteks Em7 (bar 15) menuju Fmaj7 (bar 16), sesuai `03-harmony.md`.
- Key D Dorian.
- Harus punya "ruang" (rest terjadwal) — Level 4 output wajib termasuk ruang, bukan hanya notasi padat.

## Kandidat (fakta dari `notation_facts.py`, dijalankan per kandidat)

### Kandidat A — interval leap+recovery ("Lampu pertama, terbuka")
ABC: `"Em7" E B G z | "Fmaj7" z A C E |`
Fakta objektif: 6 pitch aktual (2 rest). Interval berurutan: +7 (P5 naik, E→B), -4 (M3 turun, B→G), +2 (M2 naik, G→z...A lintas rest), -9(M6 turun, A→C, lintas bar), +4(M3 naik, C→E). Semua nada **chord-tone** (E,B,G = Em7; A,C,E = Fmaj7) — arpeggio murni, tanpa tension.
Intent: leap besar (P5) lalu recovery bertahap, kontur terbuka meniru "lampu menyala tiba-tiba di gelap, lalu menetap".

### Kandidat B — repeated-note syncopated call ("Detak lampu")
ABC: `"Em7" z E E z G G z B | "Fmaj7" A2 z2 C2 z2 |` (L:1/8)
Fakta objektif: 7 pitch aktual (5 rest, rest-ratio 0.417 — paling banyak ruang). Interval: unison(E→E), +3(m3 naik E→G), unison(G→G), +4(M3 naik G→B lintas bar... sebenarnya B→A lintas bar dilaporkan -9 lihat detail script), -2, -9. Semua nada **chord-tone** juga (E,G,B=Em7; A,C=Fmaj7).
Intent: repeated-note sebagai "detak"/panggilan pendek berulang dengan syncopation (entri offbeat E-E, G-G, B), ruang paling besar dari 3 kandidat.

### Kandidat C — chromatic enclosure ke target tone ("Mencari nyala")
ABC: `"Em7" F ^D E2 | "Fmaj7" A C E2 |`
Fakta objektif: 6 pitch aktual, TANPA rest. Klasifikasi nada: **F = tension-diatonik** (dalam skala D Dorian, bukan chord-tone Em7), **D# = outside** (kromatik, bukan bagian skala D Dorian sama sekali), **E = chord-tone** (target landing). Interval: -2(turun, F→D#, enclosure klasik atas-bawah-target), +1(naik D#→E, resolusi setengah-nada), lalu +5, -9, +4 di bar 2 (arpeggio Fmaj7, semua chord-tone).
Intent: enclosure kromatik dua-nada (upper F, lower D#) landing di target tone E — motif "mencari" nada sebelum menetap, cocok tematik "lampu yang baru menyala belum stabil".

## Selected + alasan

**Dipilih: Kandidat B — "Detak lampu"** (verdict selector segar):

> The brief needs the motif to enter softly after a deliberate two-bar dip and function as one half of a call-response with Rhodes — that requires literal silence for the response to sit in. B has the highest rest ratio (0.417) of the three, and the rests aren't just padding, they're syncopated off-beat entries, which is what makes a repeated-note figure memorable rather than static (a "heartbeat" reads as pulse specifically because of the gaps). C's zero-rest chromatic enclosure is the most harmonically interesting on paper, but arriving right after a quiet dip with a continuous chromatic line works against "restrained," and leaves no bar-space for Rhodes to answer inside the same phrase. A's leap-and-recover is a fine gesture but the least distinctive rhythmically (arpeggio-up/-down is a very common shape).
>
> **Graft:** keep B's rhythm/space skeleton as the motif's core identity (also what makes it transformable at the ending), and steal C's chromatic enclosure (F–D#–E) as a substitute for B's plain landing gesture specifically in the ending reprise (bar 21-24) — so recontextualization gets the "flickering into steady light" color, while the bar-15 entrance stays restrained/call-response-friendly.

## Exact artifact
Pemenang (Kandidat B core + graft enclosure-C di reprise ending) dituliskan ke `04-melody.abc`.

## Unresolved/confidence
- Motif pemenang akan ditransposisi/divariasi saat direprise di coda (bar 21-24, di atas Dm6/9) — variasi itu didesain di Level 14/15, bukan di sini.

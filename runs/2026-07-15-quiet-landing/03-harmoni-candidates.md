# Level 3 candidates — Quiet Landing

## Objective
Membuat E terdengar belum berumah di minor/sus pada awal, tertekan singkat di B, lalu menjadi 9th/warna hangat di Dm6/9 pada coda.

## Immutable constraints
- D minor, 76 BPM, 4/4, 48 bar; satu chord per bar (3.16 detik/chord, aman >2 detik).
- Kompleksitas menengah; altered dominant hanya sebagai tension lokal.

## Assumptions
Section form: Intro/A1/A2/B/Release/Coda masing-masing 8 bar.

## Kandidat

### A — utama
Intro: Dm11 | A7sus4 | Dm9 | Gm9 | Bbmaj9 | A7sus4 | Dm9 | A7alt
A1: Dm9 | Gm9 | Bbmaj9 | A7sus4 | Dm9 | Gm9 | Em7b5 | A7alt
A2: Dm9 | Bbmaj9 | Gm9 | A7sus4 | Dm9 | Gm9 | Bbmaj9 | A7alt
B: Fmaj9 | Gm9 | C13sus4 | A7alt | Bbmaj9 | Gm9 | Em7b5 | A7alt
Release: Dm9 | C/E | Bbmaj9 | Gm9 | Fmaj9 | Gm9 | A7sus4 | A7alt
Coda: Dm6/9 | Bbmaj9/D | Gm9/D | Dm6/9 | Dm6/9 | Bbmaj9/D | Dm6/9 | Dm6/9

### B — lebih sederhana
Loop Dm9 | Bbmaj9 | Gm9 | A7sus4 dan coda Dm6/9.

### C — lebih berani
Dm11 | Ebmaj7#11 | Bbmaj9 | A7alt dengan side-slip di B, lalu coda Dm6/9.

## Selected + alasan
**Selector segar memilih A.** Minor/sus menjaga kelembutan; A7alt yang hanya muncul di ujung frase memberi tarikan cukup untuk tesis E; B dan Release membuka warna tanpa menenggelamkan narasi. Graft yang diterapkan: dua bar awal A1/A2 memakai Dm9–Bbmaj9–Gm9–A7sus4 yang lebih sederhana, dan A7alt disimpan untuk akhir frase besar.

## Exact artifact
`03-harmony.md`

## Unresolved/confidence
Keyakinan tinggi. `notation_facts.py` menandai beberapa symbol extended (`Bbmaj9`, `Fmaj9`, `Dm6/9`) sebagai unparsed; ini diverifikasi manual sebagai chord color yang sengaja dipakai, bukan label borrowed yang diklaim script.

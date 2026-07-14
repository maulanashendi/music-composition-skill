# 03 — Peta Harmoni (Level 3)

Hasil protokol kandidat→seleksi — lihat `03-harmoni-candidates.md` untuk
ketiga kandidat dan verdict selector lengkap. Pemenang: **Kandidat utama —
"Slow pivot"**, dengan satu penyesuaian dari catatan selector (tahan bar
13-14 di Dm9, tidak lompat ke Gm7, supaya terasa "satu tarikan napas
terakhir" sebelum pivot — mengorbankan satu chord warna, bukan syarat wajib
tapi diterapkan karena memperkuat kontras pivot).

## Tonal center & harmonic rhythm

Tonal center: **D**, tidak pernah modulasi ke key lain. Yang bergerak
adalah **mode**: D Dorian (D E F G A B C — nada ke-3 minor, F) di section
1-3 dan awal section 4, brighten ke **D Mixolydian** (D E F# G A B C —
nada ke-3 jadi mayor, F#, TAPI b7/C tetap natural — bukan D Ionian/mayor
penuh) mulai bar 16. bVII (C) dipertahankan di kedua mode supaya
"brightening" terasa sebagai pergeseran warna modal, bukan resolusi V-I
mayor besar (konsisten dengan brief "bukan klimaks besar").

Harmonic rhythm: sedang di section aktif (1-2 bar per chord warna),
melambat drastis di section 5-6 (chord yang sama ditahan 2-4 bar) —
harmonic rhythm sendiri jadi bagian dari kurva "menumpuk lalu mereda".

## Peta chord — fungsi — tension (24 bar)

| Bar | Section | Chord | Fungsi | Tension |
|---|---|---|---|---|
| 1 | 1 Alone | Dm9 | tonic/modal area | stabil, napas panjang |
| 2 | 1 Alone | Dm9 | tonic | stabil |
| 3 | 1 Alone | Dm9 | tonic | stabil |
| 4 | 1 Alone | Dm9 | tonic | stabil |
| 5 | 2 Comping in | Dm9 | tonic | stabil |
| 6 | 2 Comping in | Gm7 | **borrowed iv** (modal interchange dari D Aeolian/minor asli — bukan Dorian sendiri; lihat catatan gate di bawah) | mulai bergerak |
| 7 | 2 Comping in | Dm9 | tonic (kembali) | stabil |
| 8 | 2 Comping in | Cmaj7 | **diatonik bVII** (warna asli Dorian, bukan borrowed — lihat catatan gate) | terbuka, sedikit warna baru |
| 9 | 3 Steps gather | Dm9 | tonic | stabil |
| 10 | 3 Steps gather | Fmaj7 | diatonik bIII (relative major, hangat) | momentum bertambah |
| 11 | 3 Steps gather | Gm9 | borrowed iv (sama seperti bar 6) | meningkat |
| 12 | 3 Steps gather | CMaj9 | diatonik bVII, mempersiapkan pivot | meningkat |
| 13 | 4 Light arrives | Dm9 | tonic — napas terakhir sebelum pivot | stabil tapi menahan |
| 14 | 4 Light arrives | Dm9 | tonic — napas terakhir (ditahan, bukan lompat ke Gm7 seperti kandidat asli) | stabil tapi menahan |
| 15 | 4 Light arrives | A7sus4 | dominant (V, tanpa leading-tone penuh — sus4 membuang not ke-3) | tinggi — titik pivot |
| 16 | 4 Light arrives | D9 | tonic **brightened** (Mixolydian, F# muncul, C tetap natural) | resolusi — klimaks dimulai |
| 17 | 4 Light arrives | Cmaj7#11 | diatonik bVII Lydian-color (puncak warna terkaya) | radiant, puncak |
| 18 | 4 Light arrives | D9 | tonic brightened | resolusi kuat — puncak klimaks |
| 19 | 5 Thinning/Return | D6add9 | tonic, mulai mereda | turun |
| 20 | 5 Thinning/Return | Gmaj7 | diatonik IV (Lydian-color, hangat) | tenang |
| 21 | 5 Thinning/Return | D6add9 | tonic | tenang, mendekati diam |
| 22 | 6 Arrival | D6add9 | tonic — konvergensi unison dimulai | tenang |
| 23 | 6 Arrival | D6add9 | tonic | tenang |
| 24 | 6 Arrival | D | tonic, final (triad polos, terbuka) | resolusi penuh |

## Teknik harmonik dipakai

- **Borrowed iv** (Gm7/Gm9, dari D Aeolian/natural minor) — warna
  "wistful" khas neo-soul (lihat `vibes-mood/references/neo-soul-genre.md`
  §3), dipakai di section 2-3 untuk memberi gerak tanpa keluar dari
  tonal center.
- **Diatonik bVII/bIII** (Cmaj7/CMaj9, Fmaj7) — warna asli D Dorian,
  bukan outside — dipakai sebagai "momentum" harmonik yang tetap aman.
- **Dominant sus (A7sus4)** sebagai titik pivot — memberi gerak akar V→I
  yang jelas tanpa leading-tone mayor penuh, supaya brightening tetap
  modal (retained-bVII), bukan resolusi klasik.
- **Mode brightening di root sama** (Dorian→Mixolydian, F→F#, C tetap
  natural) sebagai mekanisme utama "langit mulai terang" — bukan
  modulasi ke key lain.
- **Penipisan chord** (D9/Cmaj7#11 yang kaya → D6add9 yang lebih polos →
  D triad polos) sebagai realisasi harmonik dari "mereda"/settled.

## Cek fakta notasi (gate wajib Level 3)

Dijalankan di dua segmen (segmentasi karena scope pc-collection berbeda:
segmen 1 = D Dorian, segmen 2 = D Mixolydian — keduanya diverifikasi
terhadap key signature yang benar secara terpisah, bukan diasumsikan):

```
cd skills/abc-notation/scripts && uv run --with music21 --with pretty_midi python notation_facts.py <bar1-14.abc>   # K:C, pc-set == D Dorian
uv run --with music21 --with pretty_midi python notation_facts.py <bar15-24.abc>  # K:G, pc-set == D Mixolydian
```

Ringkasan output relevan (chord-vs-key per bar, dari run aktual):

Segmen 1 (bar 1-14, key C major dipakai sebagai proxy pc-set D Dorian —
sama-sama {C D E F G A B}): Dm9=diatonik ×9 (bar 1,2,3,4,5,7,9,13,14 —
dikoreksi dari draf awal yang salah hitung "×6", ditemukan saat reviewer
L2 mencocokkan ringkasan ini terhadap tabel fungsi di atas; lihat
`scorecard.md` Level 3), **Gm7=borrowed** (bar6),
Cmaj7=diatonik (bar8), Fmaj7=diatonik (bar10), **Gm9=borrowed** (bar11),
CMaj9=diatonik (bar12).

Segmen 2 (bar 15-24, key G major dipakai sebagai proxy pc-set D
Mixolydian — sama-sama {G A B C D E F#}): A7sus4=diatonik, D9=diatonik
×2, Cmaj7#11=diatonik, D6add9=diatonik ×4, Gmaj7=diatonik, D=diatonik.
Semua bar segmen 2 diatonik — tidak ada borrowed/outside di zona
"mereda", konsisten dengan tujuan (setelah pivot, tidak ada lagi warna
asing).

**Mismatch yang ditemukan & direvisi** (gate bekerja seperti seharusnya):

1. Draf awal melabeli Gm7 (bar 6) dan Gm9 (bar 11) sebagai "subdominant
   (Dorian iv)" — salah. Chord diatonik ke-4 D Dorian yang sebenarnya
   adalah **G7 (dominant, B natural)**, bukan Gm7 (perlu Bb). Script
   melaporkan keduanya **borrowed**, bukan diatonik. Label direvisi jadi
   "borrowed iv (modal interchange dari D Aeolian)" — lihat tabel di atas.
2. Draf awal melabeli Cmaj7 (bar 8) sebagai "modal interchange (bVII)" —
   kurang tepat, karena "modal interchange"/borrowed menyiratkan berasal
   dari luar Dorian. Script melaporkan **diatonik** (C-E-G-B semua ada di
   koleksi D Dorian). Label direvisi jadi "diatonik bVII", dipisahkan
   tegas dari Gm7/Gm9 yang benar-benar borrowed.
3. **Temuan tool, bukan temuan musikal**: `notation_facts.py`/music21 gagal
   mem-parse `"Cmaj9"` (lowercase "maj9") dan `"D6/9"` — dilaporkan
   `unparsed` sebelum diperbaiki. Diverifikasi manual dengan
   `music21.harmony.ChordSymbol` langsung: music21 butuh **`CMaj9`**
   (capital M) untuk chord major-9, dan tidak mengenali notasi slash
   `6/9` sama sekali — diganti **`D6add9`** (menghasilkan pitch set
   identik: R-3-5-6-9, diverifikasi cocok). Ini murni penyesuaian ejaan
   simbol untuk kompatibilitas parser, bukan perubahan bunyi chord — bunyi
   yang dimaksud (C major-9 / D 6/9 chord) tidak berubah. Ejaan `CMaj9`/
   `D6add9` inilah yang dipakai di `song.abc` nanti, bukan `Cmaj9`/`D6/9`.

Tidak ada chord `unparsed` yang tersisa setelah perbaikan ejaan di atas.

## Gate check (Level 3)

Tonal center (D) dan harmonic rhythm ditentukan eksplisit. Bar count
(24 bar) konsisten dengan `02-form.md`. Cek fakta notasi selesai, 2
mismatch label ditemukan dan direvisi (dicatat di atas), 1 temuan
kompatibilitas ejaan simbol diperbaiki. Lanjut ke Level 4.

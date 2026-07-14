# 04 — Melodi — Kandidat & Seleksi (Level 4)

## Objective

Motif inti untuk lead (flugelhorn/muted trumpet) yang masuk di bar 15-16
(section 4 "Light arrives", chord A7sus4→D9) dengan **satu lompatan
interval naik yang lebar** — ini konstrain terkunci dari Level 1/2 (satu-
satunya lompatan besar di seluruh lagu = "momen paling berarti"). Level
ini memilih KARAKTER motif tersebut: interval mana, dan bagaimana ia pulih
sesudahnya (leap → recovery).

## Immutable constraints

- Harus mengandung lompatan naik yang lebar, tepat di transisi
  A7sus4 (bar15) → D9 (bar16) — titik brightening.
- Motif ini akan jadi identitas utama lead untuk sisa lagu (dikutip lagi
  saat konvergensi unison di section 6) — karakternya menentukan nuansa
  "momen paling berarti" itu.
- Tidak boleh bertentangan dengan karakter brief ("lelah tapi lapang" →
  "keyakinan tenang", BUKAN agresif) tanpa alasan eksplisit.

## Kandidat

Tiap kandidat ditulis sebagai tune ABC mini lengkap (2 bar: A7sus4 lalu
D9), lalu dijalankan lewat `notation_facts.py --voice 1`. Fakta di bawah
ini adalah **output asli script**, bukan klaim dari ingatan.

### Kandidat 1 — "Major 6th leap, stepwise recovery" (lyrical)

```abc
X:1
M:4/4
L:1/8
K:G
V:1
[V:1] "A7sus4"z4 A4 | "D9"^f4 e2 d2 |
```

Intent (≤1 kalimat): lompatan sedang (6th) yang segera pulih lewat
langkah bertahap turun — karakter lyrical/smooth, paling dekat ke
"leap → recovery" klasik.

Fakta (`notation_facts.py`): 3 pitch (bukan rest) di bar 2 + 1 pitch di
bar 1 = 4 not total. Interval: **+9 (Major Sixth) naik** (A→F#), lalu
**-2 (Major Second) turun** (F#→E), lalu **-2 (Major Second) turun**
(E→D). Klasifikasi: A=chord-tone (A7sus4), F#=chord-tone, E=chord-tone,
D=chord-tone — **seluruhnya chord-tone, tidak ada outside**.

### Kandidat 2 — "Octave leap, arpeggio-cascade recovery" (soaring)

```abc
X:1
M:4/4
L:1/8
K:G
V:1
[V:1] "A7sus4"z4 D4 | "D9"d4 A2 ^F2 |
```

Intent (≤1 kalimat): lompatan seluas mungkin (oktaf penuh) lalu pulih
lewat arpeggio turun yang melintasi register lebar — karakter paling
"terbuka/lapang" secara harfiah (rentang nada terlebar).

Fakta: 4 not total. Interval: **+12 (Perfect Octave) naik** (D→D'), lalu
**-5 (Perfect Fourth) turun** (D'→A), lalu **-3 (Minor Third) turun**
(A→F#). Klasifikasi: D=chord-tone, D'=chord-tone, A=chord-tone,
F#=chord-tone — **seluruhnya chord-tone, tidak ada outside**.

### Kandidat 3 — "Major 7th leap, chromatic-enclosure recovery" (angular)

```abc
X:1
M:4/4
L:1/8
K:G
V:1
[V:1] "A7sus4"z4 G4 | "D9"f4 ^d2 e2 |
```

Intent (≤1 kalimat): lompatan paling tajam (7th mayor, bukan 7th minor —
lihat catatan fakta di bawah) lalu pulih lewat enclosure kromatik
(nada bawah kromatik menuju target) — karakter paling angular/dramatic
dari ketiganya.

Fakta: 4 not total. Interval: **+11 (Major Seventh) naik** (G→F#), lalu
**-3 (Minor Third) turun** (F#→D#), lalu **+1 (Minor Second) naik**
(D#→E). Klasifikasi: G=chord-tone (A7sus4), F#=chord-tone, **D#=outside**
(bukan diatonik D Mixolydian maupun chord-tone D9 — ini kromatisme
kandidat 3 yang disengaja, enclosure lower-neighbor menuju E), E=chord-
tone (9th dari D9, target resolusi).

**Koreksi nama vs fakta** (ditemukan saat menjalankan gate, bukan
diasumsikan dari ingatan): draf awal menyebut kandidat ini "minor 7th
leap" — salah. Karena `K:G` sudah mengandung F# di key signature, menulis
nada polos `f` otomatis jadi F# (bukan F natural yang dibutuhkan untuk
interval minor 7th sungguhan). Fakta script melaporkan **major 7th**
(+11 semitone), bukan minor 7th (+10). Nama kandidat direvisi sesuai fakta
di atas.

## Selected + alasan

**Kandidat 1 — "Major 6th leap, stepwise recovery" (lyrical).**

Alasan (berdasarkan efek audible, bukan kompleksitas teori):

- **+9 (major sixth)** cukup lebar untuk memenuhi konstrain "satu lompatan
  naik yang lebar", tapi secara karakter bunyi jauh lebih hangat dan
  lyrical dibanding **+12 (oktaf, kandidat 2)** — yang terdengar sebagai
  "reaching" ekstrem, gerakan fisik besar — apalagi **+11 (major 7th,
  kandidat 3)** yang tajam dan tegang, nyaris selalu terdengar
  "straining"/mendesak, bukan "tiba dengan tenang".
- Recovery **stepwise** (F#→E→D, dua whole-step turun berurutan, jarak
  rapat) adalah yang paling *settling* dari ketiganya — menutup gerakan
  dengan langkah kecil dan dekat, pas dengan "keyakinan tenang". Ini kontras
  dengan arpeggio-cascade kandidat 2 yang tetap melintasi register lebar
  (masih terasa "bergerak/soaring", bukan menetap) dan jelas kontras dengan
  chromatic enclosure kandidat 3 yang membawa nada outside (D#) — tegangan
  kromatik itu yang paling berisiko terdengar dramatic/agresif, bertentangan
  langsung dengan instruksi eksplisit brief ("BUKAN agresif").
- Seluruh 4 not kandidat 1 chord-tone (tidak ada outside), sama seperti
  kandidat 2 — jadi memilih opsi paling restrained ini tidak mengorbankan
  kebersihan harmoni.

**Graft yang disarankan:** pertimbangkan mengganti not akhir dari D (root
D9) menjadi E (9th dari D9) — meniru pilihan resolusi kandidat 3 yang juga
berhenti di E, tapi TANPA mengimpor enclosure kromatiknya. Mendarat di
color-tone (9th) alih-alih root polos memberi sedikit warna neo-soul yang
lebih "lush" pada titik arrival, sambil tetap mempertahankan gerak
stepwise yang tenang dari kandidat 1.

## Exact artifact

`04-melody.abc` (catatan desain) memakai pemenang seleksi di atas.

## Unresolved/confidence

Confidence: **medium**.

Risiko terbuka:

- 6th mungkin terasa "kurang lebar" untuk menandai status motif ini
  sebagai satu-satunya lompatan besar di seluruh lagu ("momen paling
  berarti") — jika arc lagu secara keseluruhan butuh statement yang lebih
  besar secara fisik/register, kandidat 2 (oktaf) bisa jadi under-valued
  di keputusan ini.
- Judul section 4 "Light arrives" menyiratkan brightening/arrival yang
  cukup jelas terdengar; recovery stepwise kandidat 1 adalah yang paling
  landai dari ketiganya — ada risiko efek "arrival"-nya kurang menonjol
  dibanding chord change A7sus4→D9 itu sendiri sudah menyediakan.
- Register aktual (A4→F#5, dst.) belum dicek terhadap tessitura
  flugelhorn/muted trumpet sungguhan — apakah lompatan ini nyaman dan
  bersinar di instrumen tsb belum diverifikasi di level ini.
- Keputusan ini murni berdasarkan motif dalam isolasi 2 bar; interaksi
  dengan section 6 (dikutip ulang saat unison convergence) dan dengan
  dinamika/artikulasi arrangement penuh belum diuji.

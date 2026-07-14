# 03 — Harmoni — Kandidat & Seleksi (Level 3)

## Objective

Peta harmoni 24 bar yang merealisasikan arc "Home by Dawn": D Dorian
(lelah, terbuka) yang brighten ke D Mixolydian/mayor-ish (F->F#, langit
mulai terang) tepat di section 4 (klimaks tunggal), lalu menetap.

## Immutable constraints

- 24 bar, mengikuti 6 section `02-form.md` (1: bar1-4, 2: bar5-8, 3:
  bar9-12, 4: bar13-18, 5: bar19-21, 6: bar22-24).
- Tonal center D sepanjang lagu — TIDAK modulasi ke key asing (Level 1).
- Brightening = mode shift di root yang sama (bukan pindah key).
- Section 4 = satu-satunya klimaks; section 5-6 harus terdengar mereda,
  bukan puncak kedua.

## Assumptions

- "Brighten" secara teori = nada ke-3 F (minor) -> F# (mayor); C tetap
  natural (bVII dipertahankan) supaya brightening tetap modal/restrained,
  bukan resolusi V-I mayor penuh yang terasa seperti "klimaks besar".

## Kandidat

### Kandidat utama — "Slow pivot" (1 chord change besar, harmonic rhythm sedang)

Intent: harmonic rhythm sedang (1-2 bar per chord di section aktif),
dengan SATU titik pivot jelas (F->F#) tepat di puncak section 4.

| Bar | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Chord | Dm9 | Dm9 | Dm9 | Dm9 | Dm9 | Gm7 | Dm9 | Cmaj7 | Dm9 | Fmaj7 | Gm9 | Cmaj9 |

| Bar | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 | 24 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Chord | Dm9 | Gm7 | A7sus4 | Dmaj9 | Cmaj7#11 | Dmaj9 | Dmaj9 | Gmaj7 | Dmaj9 | Dmaj9 | D6/9 | D |

### Kandidat lebih sederhana — "One change" (harmonic rhythm sangat lambat)

Intent: hanya SATU perubahan chord di seluruh lagu (Dm7 -> Dmaj7 tepat di
bar 16, awal section 4 lanjut), sisanya statis — paling literal terhadap
"restrained".

| Bar | 1-12 | 13-15 | 16-24 |
|---|---|---|---|
| Chord | Dm7 (12 bar, tanpa perubahan) | Dm7 (3 bar) | Dmaj7 (9 bar, tanpa perubahan lagi) |

Ditulis per-bar: bar1=Dm7, bar2=Dm7, ... bar15=Dm7, bar16=Dmaj7, bar17=Dmaj7,
... bar24=Dmaj7 (setiap bar chord sama persis dengan bar sebelumnya dalam
rentangnya).

### Kandidat lebih berani — "Chromatic wander" (harmonic rhythm cepat, banyak warna outside)

Intent: harmonic rhythm 1 chord/bar dari awal, memakai secondary dominant,
tritone substitution, dan chromatic mediant bahkan di section-section awal
yang seharusnya "tenang" — paling jauh dari restrained.

| Bar | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Chord | Dm9 | Gm6/D | Ebmaj7#11 | Dm9 | Bbmaj7 | A7alt | Dm9 | Cmaj7#11 | Fmaj7#11 | Bm7b5 | E7alt | A7#9 |

| Bar | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 | 24 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Chord | Dm9 | Ab7#11 | G#7alt | Dmaj9#11 | F#m7 | Bm9 | Emaj7#11 | A7sus | Dmaj9 | Gmaj7#11 | Dmaj9/A | D |

## Selected + alasan

**Kandidat utama — "Slow pivot".**

Section 1-3 tetap dijangkarkan di Dm9 dengan hanya beberapa chord warna
diatonis-Dorian (Gm7, Fmaj7, Cmaj9) — cukup untuk nuansa "lelah/terbuka"
tanpa jatuh ke statis-membosankan (risiko Kandidat sederhana, 12 bar Dm7
tanpa gerak sama sekali) atau ramai/outside sejak awal (risiko Kandidat
berani, yang sudah memakai Ebmaj7#11 chromatic-mediant di bar 2-3, jauh
sebelum section klimaks manapun). Pivot A7sus4 (bar15) -> chord terang
(bar16) memberi titik angkat yang jelas terdengar tepat di ambang section
4: gerak akar V->I (A->D) memberi rasa "tiba" tanpa leading-tone C# penuh,
karena sus4 membuang not ke-3 — brightening tetap terasa modal, konsisten
dengan asumsi "bukan resolusi V-I mayor penuh". Section 4 memuncak lewat
warna terkaya (Cmaj7#11), lalu section 5-6 benar-benar mereda: chord
menyederhana dari alternasi Dmaj9/Gmaj7 ke D6/9 dan akhirnya D polos di
bar24 — kontras audible yang tak dimiliki Kandidat sederhana (bar16-24
satu chord identik, klimaks vs reda tak terbedakan secara harmoni) maupun
Kandidat berani (warna outside terus jalan sampai section 6 — Gmaj7#11,
Dmaj9/A — sehingga "reda" tak pernah benar-benar reda). Tidak perlu graft;
arsitekturnya sudah lengkap. Micro-tweak opsional (bukan syarat): tahan
bar13-14 di Dm9 satu bar lebih lama sebelum bergerak ke Gm7, supaya jeda
sebelum pivot A7sus4 terasa seperti satu tarikan napas terakhir.

## Exact artifact

`03-harmony.md` memakai pemenang seleksi di atas (lalu wajib lolos gate
"Cek fakta notasi" via `notation_facts.py` sebelum Level 4 dimulai).

## Unresolved/confidence

**Confidence: high** — Kandidat utama menang jelas pada kriteria yang
diminta (single climax audible di section 4, section 5-6 mereda secara
harmoni), bukan menang tipis.

Risiko yang genuinely masih terbuka:

1. Notasi "Dmaj9"/"Dmaj7" di bar16 dst secara konvensi mengandung mayor-7
   (C#), padahal asumsi eksplisit di dokumen ini minta C tetap natural
   (bVII dipertahankan, D Mixolydian) — bukan D Ionian penuh. Ini berlaku
   di ketiga kandidat, bukan cuma yang menang, jadi wajib dikoreksi saat
   menulis `03-harmony.md`: ganti ke voicing dominant/6/9 (D9, D6/9,
   Dadd9) atau anotasi eksplisit "omit 7th", supaya brightening tidak
   diam-diam berubah jadi major-key penuh.
2. Chord "Gm7" pinjaman (iv minor, butuh Bb) di bar6 & bar14 adalah warna
   modal-interchange yang disengaja, tapi belum dicek terhadap melodi —
   kalau melodi di bar itu memakai B natural (ciri Dorian) bersamaan, bisa
   jadi cross-relation yang cantik atau malah benturan. Perlu cek telinga
   di Level 4/5, jangan diasumsikan aman hanya dari grid chord.
3. Harmonic rhythm section 1-3 kandidat ini masih agak lebih aktif (chord
   warna tiap ~2 bar) dibanding "restrained" yang diminta brief. Kalau pas
   didengar terasa terlalu banyak kejadian untuk mood lelah/terbuka,
   gampang ditipiskan (mis. buang Fmaj7 bar10, balik ke Dm9) tanpa
   mengubah struktur pivot.

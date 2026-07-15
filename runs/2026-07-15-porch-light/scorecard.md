# Scorecard — Porch Light

## Level 1 — Konsep Artistik

### L1 (mekanis)

- [x] Semua field brief wajib terisi (Judul sementara, Gaya, Tempo, Birama, Karakter, Instrumentasi, Kompleksitas, Arah energi) — lihat `01-brief.md`
- [x] Tidak ada field bernilai "TBD" atau kosong

### L2 (rubrik)

Diisi oleh subagent reviewer segar tanpa konteks generasi (self-grading dilarang).

| Kriteria | Skor (0-2) | Alasan (1 kalimat) |
|---|---|---|
| Identitas artistik jelas | 2 | Aesthetic thesis menyatakan satu device konkret dan spesifik (voicing suspended add9 tetap, pocket makin behind-the-beat A1→B, resolusi di bar terakhir tiap A) yang membedakannya dari deskripsi genre generik. |
| Karakter/emosi konsisten dengan instrumentasi | 2 | Karakter hangat/reflektif/intim/late-night mellow cocok langsung dengan trio minimal Rhodes + finger bass + jazz kit tanpa gitar/tiup, sesuai referensi Glasper-ish yang disebut. |
| Arah energi masuk akal untuk gaya yang dipilih | 2 | Arc tenang/menahan → mengendur bertahap → resolusi hangat per-A → klimaks lembut di B → kembali tenang di head out koheren dan wajar untuk contemporary jazz/neo-soul mellow, dua sumbu (harmoni + rhythm feel) dijelaskan berjalan sejalan menuju resolusi yang sama. |

## Level 2 — Arsitektur Lagu

### L1 (mekanis)

- [x] Bentuk lagu dipilih secara eksplisit (AABA) — `02-form.md`
- [x] Struktur performa lengkap (intro..coda) tercantum dengan panjang bar (80 bar total)

### L2 (rubrik)

| Kriteria | Skor (0-2) | Alasan (1 kalimat) |
|---|---|---|
| Setiap bagian punya fungsi dramaturgis | 2 | Tabel struktur performa memberi fungsi dramaturgi eksplisit dan berbeda untuk ke-8 section (membuka dunia, memperkenalkan identitas, kontras, penegasan, eksplorasi, resolusi). |
| Ada kontras antar-bagian | 2 | Head B eksplisit dideskripsikan sebagai titik pocket paling mengendur/kontras terhadap A section yang lebih tight, didukung detail voicing bergerak vs beku. |
| Klimaks ditempatkan pada bagian yang tepat | 2 (direvisi dari 1, lihat "Bukti revisi") | Setelah revisi Tahap 15: `02-form.md` kini punya section "Klimaks lagu" eksplisit yang menunjuk Solo B' (bar 53-60) sebagai klimaks, dengan alasan terukur dari `13-dynamics.md` (peak density di atas fondasi energi kumulatif solo, bukan density peak berdiri sendiri seperti head B). |

## Level 3 — Peta Harmoni

### L1 (mekanis)

- [x] Tonal center (D Dorian) dan harmonic rhythm ditentukan — `03-harmony.md`
- [x] Bar count skeleton konsisten dengan Level 2 (32 bar head = 4×8, cocok AABA)

### L2 (rubrik)

| Kriteria | Skor (0-2) | Alasan (1 kalimat) |
|---|---|---|
| Tension map jelas per bar | 2 | Setiap bar A dan B punya deskripsi tension eksplisit (stabil-mengambang, predominant, resolusi, lompatan modal, puncak tension bar 15-16), termasuk koreksi terdokumentasi untuk bar 13. |
| Fungsi harmonik tiap chord teridentifikasi | 2 | Semua chord di A dan B diberi label fungsi yang konsisten (tonic-ambigu, predominant, modal interchange, dominant altered, dst.) dan dikonfirmasi silang dengan output notation_facts.py. |
| Chord kompleks (extension/alteration) memang diperlukan, bukan dekorasi | 1 | Chord altered (A7b9#5, C7b9#5) dan extended (Gm9, FM9) diberi label fungsional tapi tidak dijelaskan mengapa alterasi/extension spesifik itu (bukan versi lebih sederhana) dibutuhkan secara voice-leading atau warna. |

## Level 4 — Desain Melodi

### L1 (mekanis)

- [x] Motif inti, kontur, dan target tone ditentukan — `04-melody.abc`
- [x] Bar count melodi konsisten dengan Level 3

### L2 (rubrik)

| Kriteria | Skor (0-2) | Alasan (1 kalimat) |
|---|---|---|
| Motif mudah dikenali dan dipertahankan | 2 | Repeated-note A + chromatic neighbor Bb dipertahankan konsisten di bar 1-4 (A1 hampir identik A2) dan tetap jadi acuan bar 5-8 (held note, broken chord, stepwise resolve). |
| Target tone/guide tone terhubung logis | 2 | Tabel target-tone bar-per-bar (A→C→A→F-A-C→A→G→F) membentuk jalur logis menuju resolusi bar 8, dan diverifikasi objektif oleh `notation_facts.py` sebagai chord-tone di tiap titik kunci. |
| Outside material (jika ada) terkontrol dan diresolusikan | 1 | Outside tone Bb pada tema A terkontrol baik (satu titik per repeat, langsung resolve ke A dalam bar yang sama, diverifikasi `outside`), tapi klaim outside material B section (mis. b9/#5 di bar 14) baru berupa rencana penempatan, belum notasi/verifikasi konkret dalam artefak ini.

## Level 5 — Desain Ritme dan Groove

### L1 (mekanis)

- [x] Feel dan rhythmic identity ditentukan eksplisit — `05-groove.md`

### L2 (rubrik)

| Kriteria | Skor (0-2) | Alasan (1 kalimat) |
|---|---|---|
| Placement aksen konsisten dengan feel yang dipilih | 2 | Anticipation comping/bass ditempatkan konsisten di titik resolusi harmonik (bar 7-8 tiap A, turnaround B→A3), selaras dengan swing behind-the-beat yang mengendur dari 60% (A1) ke 66% (B) sesuai arc pocket. |
| Groove reference cukup spesifik untuk diturunkan ke comping/bass/drum | 2 | Referensi Robert Glasper trio diturunkan jadi karakter konkret per instrumen (comping anticipated stab, bass pedal-then-walkdown, drum brush/ghost-rimshot understated) sehingga langsung actionable ke Level 7/8/9, bukan sekadar label genre. |

## Level 6 — Aransemen Instrumen

### L1 (mekanis)

- [x] Orchestration map mencakup semua bagian dari Level 2 — `06-arrangement.md`

### L2 (rubrik)

| Kriteria | Skor (0-2) | Alasan (1 kalimat) |
|---|---|---|
| Setiap instrumen punya peran per bagian | 2 | Peta orkestrasi mendefinisikan peran spesifik untuk Rhodes RH/LH, bass, dan drum di tiap section (mis. LH pad beku vs rootless bergerak, bass pedal vs walking, drum sparse vs kick menegaskan downbeat). |
| Density berubah antar-bagian (bukan semua instrumen penuh terus) | 2 | Arc density eksplisit dan bertingkat (sparse→sparse-medium→medium→dense→medium-sparse→medium-dense→sparse-medium→sparse) dengan aturan pembatas "maks 2-3 gerakan device baru per section" yang dipatuhi konsisten. |

## Level 7 — Desain Comping dan Voicing

### L1 (mekanis)

- [x] Comping chart mencakup semua bagian yang butuh comping — `07-comping.md`

### L2 (rubrik)

| Kriteria | Skor (0-2) | Alasan (1 kalimat) |
|---|---|---|
| Voice leading antar-chord halus | 2 | Top-note movement B section diverifikasi lewat `notation_facts.py` dan klaim direvisi mengikuti fakta (band sempit A-Bb-C, stepwise), bukan sekadar prosa yang tidak dicek. |
| Comping bergerak (bukan block chord statis) | 1 | A section (mayoritas bar piece: A1/A2/A3/head out) sengaja tetap block-chord statis secara pitch (hanya attack/rhythm yang bervariasi via anticipatory stab/delayed answer) — bergerak nyata hanya terjadi di B section dan solo interactive, jadi sebagian besar durasi piece masih voicing yang sama persis. |

## Level 8 — Desain Bass Line

### L1 (mekanis)

- [x] Bass concept ditentukan untuk setiap section — `08-bassline.md`

### L2 (rubrik)

| Kriteria | Skor (0-2) | Alasan (1 kalimat) |
|---|---|---|
| Bass punya kontur (bukan selalu root) | 1 | Ada stepwise/chromatic/leap yang jelas di titik transisi (bar 6-8, turnaround B→A3) dan root+5th movement di B, tapi mayoritas durasi tiap A (bar 1-6, porsi terbesar piece) adalah pedal statis di satu not sehingga kontur riil terkonsentrasi hanya di segmen kecil per repeat. |
| Approach note ke chord berikutnya masuk akal | 2 | Dua titik chromatic approach (G→F#→D enclosure ke resolusi A, dan Bb→A upper-neighbor ke A3) punya alasan musikal eksplisit dan kuota dijaga (2/8 ≈25%, di bawah batas 1/3) sehingga tidak terasa dipakai sembarangan. |

## Level 9 — Desain Drum

### L1 (mekanis)

- [x] Bar count drum roadmap/grid sama persis dengan ABC section demi section — diverifikasi: 11 section `09-drums.json` (4+8×9+4=80 bar) cocok persis 11 section `song.abc`

### L2 (rubrik)

| Kriteria | Skor (0-2) | Alasan (1 kalimat) |
|---|---|---|
| Dinamika drum mengikuti struktur lagu | 2 | `phrase_velocity` naik bertahap dan konsisten mengikuti arc bentuk (intro 0.5-0.6, A1/A2 ~0.72-0.92, B melompat ke 0.9-1.1, solo lebih tinggi lagi, coda turun ke 0.4), sejalan dengan narasi mengendur→klimaks→resolusi di level lain. |
| Fills/setup ditempatkan pada transisi yang logis | 2 | Setup rimshot tunggal di bar 4 intro menjelang A1, penebalan chh/rimshot/kick di bar 8 tiap B menjelang A3, dan one-off penghilangan kick di bar 8 A3-head semuanya ditempatkan tepat di titik transisi/resolusi struktural dan dijelaskan alasannya, bukan fill generik. |

## Level 10 — Desain Improvisasi

### L1 (mekanis)

- [x] Solo map mencantumkan jumlah chorus (1 chorus AABA, Rhodes) — `10-solo-map.md`

### L2 (rubrik)

| Kriteria | Skor (0-2) | Alasan (1 kalimat) |
|---|---|---|
| Solo section punya arah perkembangan (bukan datar) | 2 | Tabel perkembangan internal chorus jelas dan bertahap (A1' spacious → A2' rhythmic development → B' harmonic tension → A3' klimaks lokal+kembali) dengan anchor/batas kebebasan konkret per section. |
| Background figure (jika ada) mendukung, bukan mengganggu | 1 | Dokumen sendiri mengakui tidak ada figur latar literal (trio tidak menambah instrumen) — dukungan hanya berupa peningkatan interaksi bass/drum yang disebut "implisit", jadi lemah dibanding contoh figure eksplisit yang dijadikan pembanding di dokumen itu sendiri. |

## Level 11 — Interlude, Shout Chorus, dan Transisi

### L1 (mekanis)

- [x] Bagian transisi tertulis eksplisit (tabel 3-fase, semua boundary) — `11-transitions.md`

### L2 (rubrik)

| Kriteria | Skor (0-2) | Alasan (1 kalimat) |
|---|---|---|
| Shout chorus terasa sebagai klimaks | N/A | Piece ini adalah piano trio tanpa shout chorus formal per desain (Level 2/11 eksplisit menyatakan absen) — klimaks dibawa density peak di B section dan chorus solo Rhodes, bukan section shout terpisah, sehingga absennya konsisten dengan brief "minimal trio" bukan kelalaian. |
| Transisi tidak terasa tiba-tiba/janggal | 2 | Tabel 3-fase (preparation/boundary/after-effect) terisi penuh untuk seluruh 8 batas section dengan mekanisme konkret (fill drum, one-off kick drop, density shift terukur), tidak ada kolom kosong. |

## Level 12 — Intro dan Ending

### L1 (mekanis)

- [x] Intro dan ending punya identitas materi sendiri — `12-intro-ending.md`

### L2 (rubrik)

| Kriteria | Skor (0-2) | Alasan (1 kalimat) |
|---|---|---|
| Intro memperkenalkan dunia lagu | 2 | Pilihan pedal point + delayed entrance dijustifikasi eksplisit terhadap alternatif lain (vamp/rubato/motif-preview) dan langsung menegaskan karakter "reflektif" sejak bar 1 lewat ruang/rest yang disengaja. |
| Ending berhubungan dengan motif utama | 2 | Coda memakai voicing `F-A-C` identik dengan setiap resolusi A section sepanjang piece (bukan device baru), dengan justifikasi eksplisit kenapa fade-vamp murni ditolak. |

## Level 13 — Dinamika dan Dramaturgi

### L1 (mekanis)

- [x] Peta dinamika observabel tercantum per section (tabel metrik + micro-apex terisi, tanpa persentase) — `13-dynamics.md`

### L2 (rubrik)

| Kriteria | Skor (0-2) | Alasan (1 kalimat) |
|---|---|---|
| Kurva energi masuk akal untuk arc lagu | 2 | Kurva drum-hits/bar terukur (0.25→5.0→14.5→4.88→13.0→14.5→5.0→1.5) langsung dari `09-drums.json` dan konsisten mengonfirmasi klaim density arc di Level 6 dengan angka, bukan estimasi. |
| Parameter dinamika bervariasi (bukan hanya volume) | 1 | Banyak parameter terisi (active voices, register, durasi not, drum hits) tapi beberapa sel kunci untuk B section dan solo (note-attacks melodi RH) eksplisit ditandai "belum dinotasi konkret / TBD Level 14", jadi variasi dinamika belum sepenuhnya terverifikasi di semua section. |

## Level 14 — Detail Low Level

### L1 (mekanis)

- [x] `validate_abc.py` lulus tanpa error (0 errors, 0 warnings)
- [x] `output.mid`: 3 track, notes-per-track > 0 semua voice — **diverifikasi ulang setelah revisi Tahap 15** (Rhodes 205, Rhodes 265, Bass-Finger 149 — turun dari 154 karena 5 bass lick chromatic disederhanakan jadi stepwise, dampak yang diharapkan dan sudah diverifikasi), durasi tetap 223.256s cocok persis perhitungan 80 bar @ 86 BPM (tidak ada regresi bar count dari revisi register/ritme) — diperiksa langsung dari MIDI (`pretty_midi`), bukan hanya status exit validator

### L2 (rubrik)

| Kriteria | Skor (0-2) | Alasan (1 kalimat) |
|---|---|---|
| Voice leading halus di level not | 1 | `notation_facts.py` menunjukkan lompatan besar berulang (minor/major sixth, diminished/augmented interval) baik di melodi (bar 20-21 bridge) maupun perpindahan chord-to-chord comping V2 (mis. pola -9/+5/+4 berulang tiap ganti chord F/A→A7/C#→F/G), jadi belum konsisten halus meski riff inti groove A section stepwise/kecil. |
| Register seimbang antar-instrumen | 2 (direvisi dari 1, lihat "Bukti revisi") | Setelah revisi Tahap 15: comping diturunkan 1 oktaf dan bass diturunkan 2 oktaf tambahan (clef=bass ternyata tidak mengubah pitch di `abc_to_midi.py`) — MIDI aktual sekarang menunjukkan 3 register terpisah (melodi 60-82, comping 46-60, bass 36-46), diverifikasi ulang lewat `pretty_midi`. |
| Voicing tidak terlalu padat | 2 | Comping tidak pernah lebih dari 3-4 not per chord sepanjang bar (mis. `[FAC]`, `[DFAc]`, `[^CFG_B]`), melodi monofonik, bass satu not — total tekstur simultan tetap ringan untuk trio (maks ~5-6 not). |
| Ending terasa selesai | 2 | Empat bar terakhir (bar 77-80) mendarat solid di pedal D (V3) di bawah chord F/D (Dm7, tonic D Dorian) yang stabil sementara melodi menahan not ke-5 (A) lalu diam, dan `09-drums.json` section Coda memfade sinkron (half-time ride bar 1-2, cymbal swell bar 3, diam bar 4) — resolusi harmonik dan dinamis terkoordinasi. |

## L2 global — kriteria blocker lintas-level (fail-closed)

| # | Kriteria blocker | Skor (0-2) | Bukti dari notasi (bar spesifik) |
|---|---|---|---|
| 1 | Identitas — 4 bar pertama bisa dibedakan dari template genre | 2 | Bar 1-4: intro tacet total kecuali comping pad `F/A` beku dan satu tick rimshot ghost di bar 4 (delayed bass entrance bar 3) — bukan pola generik "pad sempurna sejak beat 1" yang ditolak `level-12-intro-ending.md`. |
| 2 | Memorability — motif bisa diingat/dinyanyikan setelah sekali baca-dengar | 2 | Motif A section (bar 5-6, dst.): nada tunggal A berulang + 1 neighbor kromatik Bb + turun ke F — sederhana, berbasis repetisi, gampang diingat (dikonfirmasi L2-blind: reviewer segar tanpa brief bisa mengartikulasikan mekanisme motif secara akurat hanya dari notasi). |
| 3 | Interaction — instrumen terdengar saling mendengar (ada bukti call-response/ruang) | 2 | Bar 4 tiap repeat A: comping "menjawab" (`z6 [FAC]2`) tepat sesudah lead menyelesaikan frasenya; bar 7: comping "menahan masuk" (`z4 [FAC]4`) sampai lead selesai — direvisi Tahap 15 supaya benar-benar tertulis di notasi (bukan cuma diklaim), lihat "Bukti revisi". |
| 4 | Emotional specificity — arc terasa dari notasi tanpa membaca brief | 2 | **L2-blind lulus** — reviewer segar (tanpa brief/artefak lain) memilih arc yang benar (Opsi A) dan mengutip mekanisme literal yang tepat (voicing `F/A`→`F/G`→`F/D` beku lalu direinterpretasi bass) sebagai dasar pilihannya. |

**Semantik fail-closed**: skor **0** pada **salah satu** dari keempat kriteria ini = run **BELUM SELESAI**, terlepas dari skor kriteria lain.

### L2-blind — uji buta arc emosional

| Field | Isi |
|---|---|
| 3 opsi arc (verbatim, tanpa menandai yang benar) | **A** "Ragu menuju penerimaan hangat" — sonoritas statis/ambigu ditahan sebagian besar tiap siklus, pocket makin longgar sepanjang siklus, lalu sonoritas yang SAMA persis direinterpretasi lewat pergeseran not bass jadi terasa resolve/diterima; satu section kontras lebih aktif secara harmoni per siklus; berulang beberapa siklus lalu menetap ke ending yang tenang dan resolve penuh. / **B** "Urgency building to release" — eskalasi berkelanjutan (density harmoni, ritme, register naik terus dari opening sparse) menuju satu klimaks besar tunggal, lalu berhenti tiba-tiba tanpa mereda. / **C** "Nostalgia fading into emptiness" — dibuka penuh/hangat (tekstur & harmoni paling kaya di awal), lalu progresif menipis (instrumen gugur, harmoni menyederhana, register menyempit), berakhir di nada sparse yang terasa hilang/tak resolve. |
| Opsi yang dipilih reviewer segar | **A** |
| Arc sebenarnya (dari `01-brief.md`) | A |
| Hasil | **benar** |
| Alasan reviewer (apa adanya) | Mengutip mekanisme literal: voicing comping `[F,A,C,]` identik ditahan lintas-bar berlabel `"F/A"` lalu direlabel `"F/G"`→`"F/D"` tanpa not berubah (hanya bass V3 berjalan `A,,→G,,→^F,,→D,,`); pocket/phrase_velocity berfluktuasi halus per-bar (bukan eskalasi monoton, menyingkirkan opsi B); ada satu section B per siklus dengan gerak harmoni nyata (Bbmaj7→A7b9#5→Gm9→C7b9#5→FM9→Ebmaj7→A7b9#5) sebagai kontras; piece dibuka tacet (bar 1-3 kosong) bukan penuh (menyingkirkan opsi C); coda mendarat stabil di `D,,8` (tonic) dengan fade drum terkendali — resolusi tenang, bukan kehilangan/terbuka. |

### L2-cliche — audit originalitas

Dijalankan oleh reviewer segar independen terhadap seluruh 9 entri `cliche-register.md`. Hasil: **3 match ditemukan** (bukan 0 seperti perkiraan awal composer sendiri — composer sempat melakukan cek pendahuluan yang keliru menyimpulkan hanya 1 match; hasil reviewer segar di bawah ini yang otoritatif, menggantikan cek pendahuluan itu). 6 entri lain diperiksa dan tidak match, dengan bukti bar spesifik (intro delayed-entrance bar 1-4; harmonic rhythm non-seragam; progresi B section bukan i-bVI-iv-V verbatim; drum hierarchy per section; micro-apex tiap section restrained; phrase_velocity sebagai driver utama, humanize_velocity=5 kecil).

| Temuan (entri register + lokasi bar) | Respons (revisi / justifikasi audible) | Detail respons |
|---|---|---|
| "Rhodes block-chord 1 attack/bar sepanjang lagu" — comping V2 memakai `[FAC]8` tanpa variasi ritme di **seluruh 80 bar**; klaim "3 cell" di `07-comping.md` draft awal ternyata **tidak benar-benar tertulis** di notasi (gate ≥3 cell `level-07-comping-voicing.md` gagal secara faktual) | **Revisi** | Bar 4 tiap repeat A (7×) diubah ke `z6 [FAC]2` (delayed answer, menjawab sesudah lead selesai); bar 7 tiap repeat A (7×) diubah ke `z4 [FAC]4` (held-back entrance, masuk di paruh kedua). Sekarang 3 cell genuinely berbeda ada di notasi (sustained pad, delayed answer, held-back entrance) + voicing bergerak di B — diverifikasi `notation_facts.py` (chord-tone/diatonik tetap benar, register tetap 46-60 MIDI). Detail: `07-comping.md`. |
| "Ending fade + held tonic" (bar 77-80) — voicing `F-A-C`/bass D ditahan datar tanpa elemen tegang yang direkontekstualisasi di coda itu sendiri; klaim "rekontekstualisasi" di `12-intro-ending.md` draft awal hanya mengacu ke device yang SUDAH terjadi di bar 8 tiap A, bukan device baru di coda | **Revisi** | Melodi (V1) coda diubah dari `A8\|A8\|A8\|z8` menjadi `_B8\|_B8\|_B8\|z8` — menahan Bb (nada chromatic-neighbor yang sepanjang piece selalu `outside`/sekilas, Level 4) di atas `F-A-C`/D, membentuk `Dm(add b6)` yang hangat. Ini rekontekstualisasi sungguhan: nada yang selalu tegang/sekilas kini dipertahankan dan diterima sebagai warna chord akhir. Detail: `12-intro-ending.md`. |
| "Chromatic approach di tiap transisi bass jadi refleks" — bass `A→G→F#→D` dipakai **identik di 7 dari 7** repeat A (100%, bukan 25% seperti klaim draft awal yang keliru menghitung per-jenis-device alih-alih per-kemunculan) | **Revisi** | Chromatic approach dipertahankan hanya di **2 dari 7** kemunculan (A1, A3-head — dua momen paling struktural). 5 kemunculan lain (A2, Solo A1'/A2'/A3', Head out) diubah ke device stepwise tanpa chromatic (`A→G→D`). Proporsi baru **2/7 ≈ 28.6%**, di bawah kuota 1/3, dihitung per-kemunculan (cara yang benar). Detail: `08-bassline.md`. |

## Bukti revisi (wajib sebelum run disebut selesai)

| Temuan (sumber: L1/L2-rubrik/L2-blind/L2-cliche) | Before (kutipan notasi/nilai lama) | After (kutipan baru) | Efek yang diharapkan terdengar (1 kalimat) |
|---|---|---|---|
| L2-rubrik Level 14 "Register seimbang antar-instrumen" (skor 1) — comping (V2) dan melodi (V1) berbagi oktaf treble yang sama, top-note comping (A4) tumpang tindih persis dengan pitch dominan melodi (A4) | `[V:2] "F/A" [FAC]8` (chord tones F4/A4/C4, MIDI range V2 min58-max72, avg 64.9 — hampir sama dengan V1 avg 68.4) | `[V:2] "F/A" [F,A,C,]8` (diturunkan 1 oktaf: MIDI range V2 min46-max60, avg 52.9) — juga bass (V3) diturunkan 2 oktaf tambahan (dari avg 67.2, tumpang tindih penuh dengan treble, ke avg 43.2) karena `clef=bass` di header ternyata **tidak mengubah pitch aktual** (diverifikasi: `abc_to_midi.py` tidak punya logika transposisi clef), jadi bass sebelumnya bersuara di register yang sama persis dengan melodi/comping — bukan cuma masking dua voice, tapi tiga-tiganya bertumpuk | Tiga instrumen sekarang terpisah jelas secara register (melodi 60-82, comping 46-60, bass 36-46) — comping dan bass akan terdengar mendukung dari bawah, bukan bersaing dengan melodi di rentang pitch yang sama; durasi total MIDI tidak berubah (223.256s, diverifikasi ulang) jadi tidak ada regresi bar count |
| L2-rubrik Level 2 "Klimaks ditempatkan pada bagian yang tepat" (skor 1) — `02-form.md` tidak pernah menyebut eksplisit bagian mana yang jadi klimaks, harus disimpulkan sendiri dari Level 6/13 | `02-form.md` tidak punya section "Klimaks" — hanya deskripsi dramaturgi arc umum | Ditambahkan section "## Klimaks lagu (eksplisit)": **Solo B' (bar 53-60)** dinyatakan sebagai klimaks, dengan alasan terukur dari `13-dynamics.md` (density 14.50 hit/bar dicapai SETELAH energi solo sudah naik ke 13.00 di A1'/A2', beda dari head B yang naik dari baseline 5.00) | Pendengar akan merasakan Solo B' sebagai puncak "sungguhan" karena datang di atas fondasi energi yang sudah terbangun sepanjang solo, bukan lompatan density yang sama besarnya tanpa konteks kumulatif seperti head B |
| L2-cliche "Rhodes block-chord 1 attack/bar sepanjang lagu" — comping tanpa variasi ritme di 80 bar, klaim 3-cell di `07-comping.md` tidak benar-benar tertulis di notasi | `[V:2] "F/A" [FAC]8` di SEMUA bar 4 dan bar 7 tiap 7 repeat A (56 bar identik) | Bar 4: `z6 [FAC]2` (delayed answer); bar 7: `z4 [FAC]4` (held-back entrance) — diterapkan konsisten di semua 7 repeat A | Comping sekarang benar-benar "menjawab" dan "menahan masuk" di titik-titik napas lead yang sama, bukan sekadar diam menempel chord sepanjang bar tanpa variasi ritmis apa pun |
| L2-cliche "Ending fade + held tonic" — coda menahan tonic polos tanpa elemen tegang yang direkontekstualisasi | `[V:1]` coda: `A8 \| A8 \| A8 \| z8` | `[V:1]` coda: `_B8 \| _B8 \| _B8 \| z8` — Bb (chromatic-neighbor yang selalu "outside" sepanjang piece) ditahan di atas `F-A-C`/D, membentuk `Dm(add b6)` | Nada yang sepanjang lagu selalu terdengar sekilas/tegang kini ditahan dan diterima sebagai warna hangat penutup — rekontekstualisasi sungguhan, bukan sekadar tonic ditahan |
| L2-cliche "Chromatic approach bass jadi refleks" — device `A→G→F#→D` identik di 7/7 repeat A (100%, melebihi kuota 1/3) | `A,,4 G,,2 ^F,,2 \| D,,8` di ke-7 repeat A | Dipertahankan hanya di A1 & A3-head (2/7≈28.6%); 5 repeat lain (`A2`, Solo A1'/A2'/A3', Head out) diganti `A,,4 G,,4 \| D,,8` (stepwise, tanpa not kromatik) | Resolusi bass terasa bervariasi antar-repeat alih-alih satu lick yang sama diputar ulang mentah 7 kali, sambil tetap menegaskan device kromatik di dua titik paling struktural (perkenalan & resolusi head) |

## Export (Tool 2 — engine daw_generative)

| Field | Isi |
|---|---|
| Status | **Selesai.** Dev server `daw_generative` dijalankan (`npm run dev`, port 5173, auto-increment tidak terjadi). `drums_to_engine.py` sukses konversi 80 bar. **Bug ditemukan + diperbaiki sebelum render:** `conformance-audit.mjs` gagal pertama kali dengan `bridgeHarmony: harmony ABC kosong/tak terparse` — root cause: importer engine (`src/abc/parse.js`) hanya membaca chord symbol dari `voices[0]` ("lead"), sedangkan `song.abc` awal menaruh semua chord symbol di `V:2` (comping), bukan `V:1` (melodi). Diperbaiki dengan menambahkan chord symbol yang sama persis ke tiap bar `V:1` (murni aditif, tidak mengubah pitch melodi manapun) — diverifikasi ulang `validate_abc.py` (0 error) dan `conformance-audit.mjs` (`"ok":true`, semua pocket check `keys`/`bass`/`drums` lolos) sebelum render sungguhan. |
| Path | `runs/2026-07-15-porch-light/render.wav` (37.9 MB, 2ch/44100Hz, durasi 225.09s — selisih ~1.8s dari `output.mid` 223.26s karena tail mastering, wajar) |
| Conformance summary | `{"bars":80,"totalNotes":1329,"tracks":4,"velStdMin":0.0178,"pctOnGridMax":37.4648,"pocket":"neo-soul-core","pocketOk":true}` |
| Mastering | `neo-soul` (default, tidak di-override) |

## L3 (telinga) — hanya diisi sekali, di akhir

<isi hasil telinga di sini setelah output.mid tersedia>

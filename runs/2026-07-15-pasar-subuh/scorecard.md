# Scorecard — Lampu Warung (Pasar Subuh)

## Level 1 — Konsep Artistik

### L1 (mekanis)
- [x] Semua field brief wajib terisi (Judul sementara, Gaya, Tempo, Birama, Karakter, Instrumentasi, Kompleksitas, Arah energi) — lihat `01-brief.md`.
- [x] Tidak ada field bernilai "TBD" atau kosong.

### L2 (rubrik) — reviewer segar (vibes-mood)

| Kriteria | Skor (0-2) | Alasan |
|---|---|---|
| Fakta user dan asumsi dipisahkan; mood/gaya/groove/instrumentasi tidak tercampur jadi satu blob | 2 | Header memisahkan judul/gaya/tempo/birama/karakter/instrumentasi/kompleksitas/arah-energi sebagai baris terpisah, dan bagian "Asumsi" eksplisit dilabeli terpisah dari fakta brief. |
| DNA tetap (fixed), parameter fleksibel, arrival terlindungi, dan shortcut terlarang dinyatakan eksplisit | 1 | DNA tetap dinyatakan jelas (bass ostinato "identitas yang tidak berubah secara nada") dan arrival digambarkan (rekontekstualisasi di ending), tapi tidak ada pernyataan eksplisit soal parameter mana yang fleksibel maupun shortcut yang dilarang. |
| Minimal dua konsep berbeda secara struktural dipertimbangkan, kriteria pemilihan eksplisit | 1 | Perbandingan lengkap 2 konsep hidup di `01-konsep-candidates.md`; `01-brief.md` sendiri hanya menyebut sekilas "graft dari Kandidat B" tanpa merestate kriteria pemilihan di badan artefak yang dinilai. |
| Gaya memakai penanda lebih dari sekadar superfisial | 2 | Penanda gaya masuk ke mekanisme struktural (mode D Dorian nada ke-6 mayor, ostinato dua-nada, layering bertahap, rekontekstualisasi), bukan label genre permukaan. |
| Materi referensi diterjemahkan jadi atribut luas, bukan disalin | 2 | Citra "pasar subuh/lampu warung" diterjemahkan jadi atribut musik abstrak tanpa referensi artis/rekaman/melodi spesifik yang bisa dikenali. |

_(Catatan: kriteria 2-3 lantai bukan langit-langit — perbandingan kandidat lengkap ada di `01-konsep-candidates.md`, hanya rangkumannya yang tipis di `01-brief.md` sendiri.)_

## Level 2 — Arsitektur Lagu

### L1 (mekanis)
- [x] Bentuk lagu dipilih secara eksplisit (through-composed dengan dip, `02-form.md`).
- [x] Struktur performa lengkap tercantum dengan panjang bar (6 section, 24 bar total).

### L2 (rubrik) — reviewer segar (arrangement, gabungan L2/6/7/10/11/12/13)
_(lihat tabel gabungan di bagian bawah scorecard ini, "L2 arrangement-family")_

## Level 3 — Peta Harmoni

### L1 (mekanis)
- [x] Tonal center (D Dorian) dan harmonic rhythm ditentukan.
- [x] Bar count skeleton (24) konsisten dengan Level 2.

### L2 (rubrik) — reviewer segar (harmony)

| Kriteria | Skor (0-2) | Alasan |
|---|---|---|
| Fungsi harmonik tiap chord jelas | 2 | Setiap bar (1-24) diberi label fungsi eksplisit di tabel skeleton, konsisten dengan tension map per section. |
| Event non-diatonis punya rasionale fungsional/modal/voice-leading/warna/formal | 2 | Satu-satunya event non-diatonis (bar 19, G7b9#5) diberi rasional eksplisit "chromatic departure/outside (micro-apex)" dan dikonfirmasi `chord-vs-key=borrowed` oleh `notation_facts.py`. |
| Ritme harmonik cocok tempo/groove; tak ada chord dekoratif berlebih | 1 | Ada narasi harmonic rhythm dan alasan anti-cliche, tapi tempo/meter tidak disebut ulang di file `03-harmony.md` itu sendiri sehingga kecocokan dengan tempo tak terverifikasi dari artefak ini sendiri (verifikasi tempo memang hidup di `05-groove.md`, bukan hilang dari run). |
| Voicing eksak (pitch+oktaf) disediakan | 0 | `03-harmony.md` hanya berisi chord symbol, tanpa voicing eksak — **sesuai desain**: voicing eksak+oktaf adalah tanggung jawab Level 7 (`07-comping.md`), bukan Level 3. Skor 0 di sini adalah pembagian tanggung jawab antar-level, bukan kelalaian; lihat catatan silang di bawah. |
| Top line/inner-line bergerak sengaja | 0 | Sama — dibahas di `07-comping.md` (top-note A→B→B→B terverifikasi script), bukan di Level 3. |
| Register/alokasi instrumen playable | 0 | Sama — di luar cakupan lead-sheet harmony Level 3; dibahas di `06-arrangement.md`/`07-comping.md`. |

**Catatan silang penting**: rubrik `harmony/references/rubric.md` menggabungkan kriteria "harmony" dan subset "voicing" (lihat header rubric-nya sendiri: "plus subset voicing dari §8"). SOP 14-level paket ini memisahkan itu ke Level 7 (`groove-rhythm`/`arrangement`), sehingga 3 kriteria voicing di rubrik ini **by design** bernilai 0 untuk artefak lead-sheet Level 3 — bukan kegagalan, tapi mismatch cakupan rubrik-vs-level yang sudah tertutup oleh Level 7's rubrik sendiri (skor tinggi di sana, lihat gabungan arrangement di bawah).

## Level 4 — Desain Melodi

### L1 (mekanis)
- [x] Motif inti, kontur, target tone ditentukan (`04-melody.abc`).
- [x] Bar count melodi konsisten dengan Level 3.

### L2 (rubrik) — reviewer segar (melody-design + advanced-melody)

**Tabel 1 — `melody-design/references/rubric.md`**

| Kriteria | Skor (0-2) | Alasan |
|---|---|---|
| Satu motif utama mengorganisasi keseluruhan piece | 1 | Motif "detak lampu" terlacak konsisten di bar 15/17/19/20/24, tapi `04-melody.abc` hanya mencakup segmen 10-bar terakhir, bukan bukti eksplisit untuk piece penuh (bar 1-14 tacet secara desain, dicatat di `06-arrangement.md`). |
| Identitas ritmis/interval tetap dikenali setelah transformasi | 1 | Identitas repeated-note/syncopated jelas di bar 15/17; reprise bar 24 (enclosure kromatik) menautkan lewat target-tone (B) bersama, bukan lewat fingerprint ritme/interval yang sama persis. |
| Panjang phrase, napas, silence, target note jelas | 2 | Rest terjadwal di tiap motif + tabel target-tone per bar (Tahap 6) eksplisit. |
| Nada panjang/berulang/aksen cocok harmoni atau menantangnya dengan alasan | 2 | Bar 19 Ab dijelaskan sebagai chord-tone dari chord borrowed (bukan "outside" polos) — rasional pada level chord, bukan gestur vague. |
| Range/tessitura sesuai instrumen lead | 0 | Tidak ada rentang sax eksplisit disebut/dicek di file ini. |
| Klimaks tidak dilemahkan oleh titik tinggi berulang; head tetap memorable tanpa dekorasi | 1 | Apex bar 19 sudah didesain sebagai satu nada tunggal terisolasi (niat baik), tapi uji "tetap memorable setelah dekorasi dihapus" tidak pernah dilakukan eksplisit. |
| Kepadatan ritmis proporsional BPM brief (IOI/rest-ratio cocok tabel band) | 0 | BPM tidak disebut ulang di `04-melody.abc` sendiri (hidup di `05-groove.md`) — tak bisa dicek dari artefak ini sendiri. |

**Tabel 2 — `advanced-melody/references/rubric.md`**

| Kriteria | Skor (0-2) | Alasan |
|---|---|---|
| Outside/chromatic vocabulary hanya di bar tension tinggi | 2 | Kedua event kromatik (bar19 Ab, bar24 A#) terikat momen struktural bernama (micro-apex, rekontekstualisasi). |
| Enclosure/approach note punya target diatonis jelas & tercapai | 2 | Enclosure bar 24 (C→A#→B) mencapai target B (chord-tone terkonfirmasi); Ab bar19 diberi jalur resolusi eksplisit ke G bar20. |
| Chromatic vocabulary tak menutupi motif inti | 1 | Klaim koherensi motivic bar15↔bar24 bersandar pada target-tone bersama (B) saja; bentuk ritme/interval enclosure tidak menggemakan identitas repeated-note aslinya. |
| Outside line punya jalur kembali jelas | 2 | Bar19→20 (Ab turun ke G, chord-tone Em7 berikutnya) dinyatakan eksplisit. |
| Kerumitan chromatic proporsional level kompleksitas brief | 0 | Tidak ada rujukan eksplisit ke level kompleksitas brief ("menengah") di file ini untuk dicek proporsionalitasnya. |

_(Catatan reviewer independen: beberapa skor 0 di atas mencerminkan cakupan `04-melody.abc` sebagai catatan desain 10-bar terakhir, bukan bukti bahwa BPM/range/kompleksitas diabaikan proyek — keduanya memang didokumentasikan di artefak Level lain: BPM di `05-groove.md`, kompleksitas "menengah" di `01-brief.md`. Dicatat apa adanya per instruksi "jangan digenerouskan", bukan disunting ulang agar terlihat lebih tinggi.)_

## Level 5 — Desain Ritme dan Groove

### L1 (mekanis)
- [x] Feel dan rhythmic identity ditentukan eksplisit (`05-groove.md`).

### L2 (rubrik) — reviewer segar (groove-rhythm, gabungan L5/8/9)
_(lihat tabel gabungan "L2 groove-rhythm-family" di bawah)_

## Level 6 — Aransemen Instrumen

### L1 (mekanis)
- [x] Orchestration map mencakup semua bagian dari Level 2 (`06-arrangement.md`).

### L2 (rubrik) — lihat gabungan "L2 arrangement-family" di bawah

## Level 7 — Desain Comping dan Voicing

### L1 (mekanis)
- [x] Comping chart mencakup semua bagian yang butuh comping (`07-comping.md`).

### L2 (rubrik) — lihat gabungan "L2 arrangement-family" di bawah

## Level 8 — Desain Bass Line

### L1 (mekanis)
- [x] Bass concept ditentukan untuk setiap section (`08-bassline.md`).

### L2 (rubrik) — lihat gabungan "L2 groove-rhythm-family" di bawah

## Level 9 — Desain Drum

### L1 (mekanis)
- [x] Bar count drum roadmap (24) sama persis dengan ABC section demi section — dikonfirmasi `grid_to_midi.py` (207 hits, 24 bar, tanpa WARNING anti-tile).

### L2 (rubrik) — lihat gabungan "L2 groove-rhythm-family" di bawah

## Level 10 — Desain Improvisasi

### L1 (mekanis)
- [x] Micro-improvisation map terisi lengkap (5 field, `10-solo-map.md`) — piece tanpa solo section formal.

### L2 (rubrik) — lihat gabungan "L2 arrangement-family" di bawah

## Level 11 — Interlude, Shout Chorus, dan Transisi

### L1 (mekanis)
- [x] Bagian transisi tertulis eksplisit (`11-transitions.md`, 5 boundary, semua kolom terisi).

### L2 (rubrik) — lihat gabungan "L2 arrangement-family" di bawah

## Level 12 — Intro dan Ending

### L1 (mekanis)
- [x] Intro dan ending punya identitas materi sendiri (`12-intro-ending.md`).

### L2 (rubrik) — lihat gabungan "L2 arrangement-family" di bawah

## Level 13 — Dinamika dan Dramaturgi

### L1 (mekanis)
- [x] Peta dinamika observabel per section + micro-apex terisi (`13-dynamics.md`).

### L2 (rubrik) — lihat gabungan "L2 arrangement-family" di bawah

## Level 14 — Detail Low Level

### L1 (mekanis)
- [x] `validate_abc.py` lulus tanpa error (`OK: 0 errors, 0 warning(s)`).
- [x] `output.mid`: 4 track (Tenor Sax 16 not/max-poly 1, Rhodes 45 not/max-poly 4, Finger Bass 51 not/max-poly 1, Drums 207 hits); tempo 76 BPM, TS 4/4 — cocok ABC (`Q:1/4=76`, `M:4/4`). Lihat `14-review.md`.

### L2 (rubrik) — reviewer segar (abc-notation + midi-orchestration)

**Tabel 1 — `abc-notation/references/rubric.md`**

| Kriteria | Skor (0-2) | Alasan |
|---|---|---|
| Header wajib ada & bisa di-parse | 2 | Reviewer menjalankan ulang `validate_abc.py` independen: `OK: 0 errors, 0 warning(s)`. |
| Ejaan not cocok key & fungsi harmonik | 2 | `_A` (Ab) mengeja b9 `G7b9#5` dengan benar; `^A,` di bar `Dm6add9` terbaca sebagai chromatic approach naik ke B, bukan salah eja Bb. |
| Bar duration/pickup/tuplet/rest/tie/overlay/repeat konsisten | 2 | Tiap bar total 8 eighth-note (`L:1/8`,`M:4/4`); tidak ada tie/tuplet/overlay/repeat yang perlu divalidasi lebih lanjut. |
| Tiap voice konsisten metrik (tak ada voice kehilangan bar) | 2 | Dihitung ulang independen: V:1/V:2/V:3 masing-masing persis 24 bar, cocok total bar drum grid (24). |
| Swing/produksi tidak salah dikodekan sebagai note value keliru | 2 | Note value ABC straight-eighth; swing & timing hidup di `09-drums.json`, pemisahan tanggung jawab benar. |
| Keterbatasan renderer diungkap eksplisit | 2 | `14-review.md` menyebut eksplisit Fix 1 (strip chord symbol/anti-drone) & Fix 2 (mono-lead) dengan angka max-poly sebagai bukti. |

**Tabel 2 — `midi-orchestration/references/rubric.md`**

| Kriteria | Skor (0-2) | Alasan |
|---|---|---|
| Komposisi kering berfungsi sebelum efek produksi ditambahkan | 2 | `pitched.mid`/`drums.mid`/`output.mid` adalah render kering tanpa efek produksi di tahap ini. |
| Tiap track/role punya identitas jelas; automation punya tujuan musikal | 2 (setelah revisi) | Awalnya reviewer menemukan **mismatch**: `output.mid` merender bass GM program **32** padahal ABC menulis `%%MIDI program 3 33` (nama voice "Finger Bass" tak cocok keyword `bass-finger` di `abc_to_midi.py`) — **sudah direvisi** (`14-review.md` Revisi 3, nama voice → "Bass-Finger", program terkonfirmasi 33 setelah re-render). |
| Event data eksak (pitch/velocity/offset/gate) tersedia untuk motif kritis/bass/voicing/groove | 2 | `09-drums.json` punya `base_velocity`/`timing`/`phrase_velocity` bernilai valid; ABC membawa pitch/durasi/chord eksplisit per voice. |
| Pitch name & nilai MIDI konsisten di seluruh track | 2 (setelah revisi) | Sama akar masalah dengan baris di atas — sudah konsisten setelah Revisi 3 (program 33 di semua tempat: ABC directive, nama voice, `output.mid`). |
| Perubahan state produksi memperkuat form, bukan menutupi section belum siap | 2 | 6 section drum (tacet→drum→rhodes→dip→micro-apex→coda) tersusun membangun/melepas tension selaras arc, diperkuat `phrase_velocity`. |
| `output.mid`: track/notes-per-track/tempo/meter cocok, diverifikasi langsung dari file | 2 | Reviewer memuat ulang independen via `pretty_midi`: 4 track, semua notes>0, tempo 76.00, TS 4/4 — cocok `Q:`/`M:` ABC. |

**Temuan penting reviewer (sudah direspons)**: mismatch GM program bass
(32 vs 33 dideklarasikan) — akar masalah `abc_to_midi.py` mengabaikan
`%%MIDI program`, menentukan program dari keyword nama voice; nama
"Finger Bass" tak mengandung substring `bass-finger`. **Direvisi**: nama
voice diganti `"Bass-Finger"`, diverifikasi ulang program=33 di
`output.mid`, tanpa regresi jumlah not/track lain. Lihat `14-review.md`
Revisi 3 untuk detail before/after lengkap.

## L2 arrangement-family (Level 2/6/7/10/11/12/13, reviewer segar arrangement)

| Kriteria | Skor (0-2) | Alasan |
|---|---|---|
| Setiap section punya bar count/durasi eksplisit dan fungsi dramaturgis yang jelas | 2 | `02-form.md` memberi tabel bar-range eksplisit untuk 6 section dan fungsi dramaturgis berbeda tiap baris, bukan label generik. |
| Identitas (motif/groove) tetap dikenali setelah transformasi; repetisi loop punya alasan | 2 | Bass ostinato D-B dipertahankan sebagai identitas dengan variasi kecil (Dm9 bar 10/12); top-note Rhodes A→B→B→B (`07-comping.md`, diverifikasi `notation_facts.py`) — repetisi terikat mekanisme rekontekstualisasi. |
| Setiap batas antar-section punya transisi disengaja | 2 | Kelima boundary di `11-transitions.md` punya mekanisme berbeda dengan detail bar-level, tak ada kolom kosong/pola riser seragam. |
| Setiap instrumen punya peran per section; akomodasi register jelas | 2 | `06-arrangement.md` memberi peran berbeda per instrumen; `07-comping.md` menjustifikasi tiap cell relatif ruang napas sax. |
| Solo/improvisasi punya landmark/target tone jelas + jalur kembali | 2 | `10-solo-map.md` micro-improvisation map 5 field; anchor tone B/Ab eksplisit; gesture terlarang eksplisit menggantikan "jalur kembali dari outside" (tak ada outside diizinkan performer). |
| Klimaks disiapkan, punya konsekuensi, ada subtraction | 2 | Micro-apex bar19 disiapkan build drum 6→12, didahului subtraction di Dip (13-14) dan subtraction kedua di klimaks sendiri (kick hilang + Rhodes diam). |

_Catatan reviewer: skor solo/improvisasi bergantung pada penerimaan micro-improvisation map sebagai substitusi sah untuk piece through-composed tanpa solo — dicatat sebagai risiko interpretasi, bukan langit-langit._

## L2 groove-rhythm-family (Level 5/8/9, reviewer segar groove-rhythm)

| Kriteria | Skor (0-2) | Alasan |
|---|---|---|
| Meter/grouping/beat unit/subdivisi eksplisit, bass/drum/comping/melodi sepakat | 2 | 76 BPM, 4/4, 16-step grid dan 8th-note motif konsisten lintas artefak. |
| Swing/feel tidak diperlakukan sebagai rasio kaku seragam | 1 | `swing:0.6` global tanpa diferensiasi per-layer; ditemukan inkonsistensi kecil "60-66%" vs "60-64%" di `05-groove.md` (revisi kosmetik minor, tidak mengubah musik). |
| Offset timing relasional & deliberate, bukan humanization acak | 2 | `timing` map per-role deterministik (kick0/snare+15/rimshot+25/chh-3), `humanize_velocity` dipisah eksplisit hanya untuk polish velocity. |
| Velocity/onset/note-length/artikulasi mendukung satu pocket konsisten | 1 | `phrase_velocity`+`base_velocity` membentuk arc jelas, tapi gate/note-length bass-drum tetap kualitatif ("pedal","held-through"), belum dikuantifikasi. |
| Kontur bass mendukung form/groove; interval karakteristik koheren | 2 | Tabel 24-transisi memetakan device ke fungsi harmonik+arc; kuota chromatic-approach (3/24=12.5%) terverifikasi benar aritmetik oleh reviewer. |
| Attack order/gate/note-off/reattack bass dispesifikasikan | 1 | Lock-point bass-kick jelas per section, tapi gate/durasi konkret belum berangka. |

## L2-blind — uji buta arc emosional

| Field | Isi |
|---|---|
| Opsi A (verbatim) | "This piece opens in dark solitude (almost no instruments), then grows layer by layer, gradually, without ever exploding into one big climax, and ends warm because the same element present from the start (not new material) resolves harmonically by the end." |
| Opsi B (verbatim) | "This piece builds tension consistently from the start to one big explosive point in the middle-to-late section (a full climax, all instruments tutti forte), then recedes quickly toward a calm ending — the classic single-peak build-and-release shape." |
| Opsi C (verbatim) | "This piece opens with a full warm texture from the very first bars, then loses energy and color toward a darker/tenser middle section, before returning to the original warmth by the end — an arch (U-shape) that returns to its starting point." |
| Opsi yang dipilih reviewer segar | **A** |
| Arc sebenarnya (`01-brief.md`) | A (sepi-gelap → tumbuh bertahap → hangat-hidup via rekontekstualisasi) |
| Hasil | **BENAR** |
| Alasan reviewer (apa adanya) | Reviewer hanya diberi `song.abc`+`09-drums.json`+`notation_facts.py` output (tanpa brief). Menunjuk: bar 1-4 sax/Rhodes tacet total (menyingkirkan C yang mengklaim "full warm sejak awal"); entrance instrumen bertahap (bass→drum bar5→Rhodes bar9→sax bar15, rest-ratio sax 0.636 tertinggi); dip eksplisit bar13-14 (`phrase_velocity` 0.6/0.55, terendah di piece) mematahkan "build konsisten ke satu klimaks" (opsi B); kick sengaja hilang di bar19 (bukan tutti forte); puncak `phrase_velocity` hanya 1.15 lalu langsung mereda 0.9→0.85→0.8→0.6 di coda; pola drum coda bar21-22 identik dengan bar5-6 (materi awal muncul lagi, bukan materi baru); chord akhir Dm6add9 dibangun di atas tonic D yang sama sejak bar1. |

**Fail-closed check**: reviewer memilih BENAR → kriteria blocker #4 (emotional specificity) TIDAK di-nol-kan oleh mekanisme ini (skornya tetap ditentukan L2-global di bawah, yang juga sudah ≥1).

## L2-cliche — audit originalitas

Reviewer segar (tanpa histori generasi) memeriksa `song.abc`+`09-drums.json` terhadap 9 entri `cliche-register.md`. 7/9 tidak match (dengan reinterpretasi jelas dicatat reviewer); 2 ditandai perlu respons:

| Temuan (entri register + lokasi bar) | Respons | Detail respons |
|---|---|---|
| "Rhodes block-chord 1 attack/bar" — bar 9-12 (4 bar whole-note pad tanpa variasi internal) | **Justifikasi audible** | Sax benar-benar tacet total di bar 1-14 (`song.abc` V:1 `z8`×14) — tidak ada napas lead untuk direspons Rhodes di section ini, jadi comping seragam di sini secara harfiah tak punya "napas" untuk dipetakan (beda dari section 15-20 yang langsung menampilkan 4 comping cell berbeda begitu sax masuk — held/stab/delayed/silence, `07-comping.md`). Ini persis skenario pengecualian yang sudah dicatat gate Level 7 sendiri ("comping seragam di sini sengaja, bukan lupa memvariasikan") — bukan dalih generik "ini disengaja" tanpa mekanisme, karena mekanismenya konkret dan bisa didengar: tidak ada dialog untuk dua pihak sebelum salah satu pihak (sax) hadir. |
| "Ending fade + held tonic" — bar 24 (Dm6add9 + fade `phrase_velocity`) | **Justifikasi audible** | Reviewer independen tidak diberi histori bahwa B adalah nada ostinato sejak bar 1 — tapi mekanisme itu terverifikasi murni dari notasi/fakta script: `notation_facts.py` melaporkan B sebagai `tension-diatonik` (bukan chord-tone) di SETIAP bar Dm7/Dm9 sepanjang bar 1-14 (bass ostinato memainkan B tiap bar), dan baru jadi `chord-tone` tepat di bar 24 (`Dm6add9`) — bukan sekadar fade ke triad polos + ekstensi warna kosmetik, melainkan SATU pitch class spesifik yang "berubah status" dari tension ke resolved, ditebalkan lagi karena ketiga voice (bass D2-z2-B4, Rhodes top-note B `[FAB]`, sax landing note B) sama-sama mendarat di B di bar itu juga — penebalan ansambel pada satu pitch tunggal ini yang membedakannya dari fade-ke-tonic generik. |

Tidak ada temuan tanpa respons — checklist L2-cliche pra-L3 terpenuhi.

## L2 global — kriteria blocker lintas-level (fail-closed)

Reviewer segar dinilai HANYA dari `song.abc`+`09-drums.json` (tanpa brief/desain lain), cold-read:

| # | Kriteria blocker | Skor (0-2) | Bukti dari notasi (bar spesifik) |
|---|---|---|---|
| 1 | Identitas — 4 bar pertama bisa dibedakan dari template genre | **1** | Bar 1-4 sax/Rhodes tacet total, bass ostinato `D2 z2 B2 z2` identik 4x — nada B natural (bukan diflatkan) menandakan Dorian bukan vamp minor generik, dan satu ghost rimshot anticipation bar4 memberi niat, tapi 4 bar identik-datar dinilai reviewer masih dekat cliché "bass-alone vamp intro". |
| 2 | Memorability — motif bisa diingat/dinyanyikan setelah sekali baca-dengar | **1** | Motif bar15/17 (cell ritmis identik ditransposisi) adalah motivic craft nyata, tapi hanya muncul di jendela 6-bar dari 24 bar total dan berbasis fragmen pendek-berjeda, bukan garis kontur panjang yang mudah dinyanyikan. |
| 3 | Interaction — instrumen terdengar saling mendengar | **2** | Call-response literal bar15(sax sendiri)→bar16(Rhodes menjawab, sax diam); interlocking bar17 (sax di posisi eighth 2-3/5-6-8, Rhodes di posisi 3-4/7-8, saling mengisi celah); kick sengaja dihilangkan bar19 tepat saat sax memegang nada tertinggi — drum "memberi ruang", bukan menabrak. |
| 4 | Emotional specificity — arc terasa dari notasi tanpa membaca brief | **2** | Arc build→dip→micro-apex→release→fade terbaca murni dari density/entrance/harmoni (dikonfirmasi independen oleh L2-blind di atas, hasil BENAR). |

**Semantik fail-closed**: TIDAK ADA kriteria bernilai 0 — checklist pra-L3
"4 kriteria blocker semuanya ≥1" **terpenuhi**. Kriteria #1 dan #2 (skor 1,
bukan 2) adalah titik terlemah piece ini — dicatat jujur sebagai area yang
bisa diperkuat (mis. varian kecil di salah satu dari 4 bar intro, atau
memperluas jendela motif sax), tapi bukan blocker.

## Bukti revisi

Lihat `14-review.md` — 2 pasangan before/after (label teori-vs-fakta bar 19; voicing top-note comping bar 16-18-24), keduanya terhubung ke gate cek-fakta Level 4/7.

## Checklist pra-L3 (fail-closed) — semua tercentang

- [x] L1 (mekanis) — lulus semua level (`validate_abc.py` 0 error, `output.mid` 4 track semua notes>0, tempo/TS cocok, `grid_to_midi.py` 207 hits/24 bar tanpa WARNING).
- [x] L2-rubrik — lengkap terisi semua 14 level (lihat tabel per-level + gabungan arrangement-family/groove-rhythm-family di atas).
- [x] 4 kriteria blocker (L2 global) — semuanya ≥1 (Identitas 1, Memorability 1, Interaction 2, Emotional specificity 2).
- [x] L2-blind — dijalankan, hasil **BENAR** (Opsi A dipilih reviewer segar).
- [x] L2-cliche — 2 temuan, keduanya direspons dengan justifikasi audible spesifik (bukan generik).
- [x] Bukti revisi — 3 pasangan before/after tercatat di `14-review.md` (label teori bar19; voicing top-note comping; GM program bass), semuanya terhubung ke temuan gate/reviewer nyata.

## Export (Tool 2 — engine daw_generative)

| Field | Isi |
|---|---|
| Status | **DONE** |
| Path | `runs/2026-07-15-pasar-subuh/render.wav` (13.1 MB, RIFF/WAVE PCM 16-bit stereo 44100 Hz — diverifikasi via `file`) |
| Conformance summary | `{"bars":24,"totalNotes":319,"tracks":4,"velStdMin":0.0193,"pctOnGridMax":57.0048,"pocket":"neo-soul-core","pocketOk":true}` |
| Mastering | `neo-soul` |

Pra-cek `conformance-audit.mjs` (sebelum render penuh) juga `ok:true`, bar
match 24=24 antara `song.abc` dan `drums-engine.json`. Server dev berjalan
di port **5178** (auto-increment dari 5173, dibaca dari log `npm run dev`,
bukan diasumsikan). Server dimatikan setelah render selesai.

## L3 (telinga) — hanya diisi sekali, di akhir

KOSONG — menunggu telinga manusia. Tidak diisi oleh agent manapun.

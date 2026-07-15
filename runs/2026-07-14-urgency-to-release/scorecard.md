# Scorecard — Undertow (fusion 7/8, brief-02 urgency-to-release)

## Validasi mesin lintas-level

Verifikasi ulang L1 (2026-07-14): `validate_abc.py` mengembalikan `OK: 0 errors,
0 warning(s)`; `music21` memuat 3 part; `drums.json` berjumlah 20 bar; dan
`output.mid` memuat Tenor Sax 50, Rhodes 67, Bass 53, serta Drums 260 note,
dengan tempo 80 BPM dan meter 7/8.

No `composition-plan.json` was produced for this run (this SOP path used
`jazz-composition`'s own numbered artefacts directly, not a separate
machine-readable plan sidecar) — cross-artefact bar-count validation was
done manually: `02-form.md` (20 bars) = `song.abc` (20 bars per voice,
confirmed by counting `|` in each `V:` line) = `09-drums.json`/`drums.json`
(`bars` fields sum to 20, confirmed by script). All three agree. Stated
here explicitly per the template's rule (manual check declared, not
silently skipped).

## Level 1 — Konsep Artistik

### L1 (mekanis)

- [x] Semua field brief wajib terisi (Judul sementara, Gaya, Tempo, Birama, Karakter, Instrumentasi, Kompleksitas, Arah energi) — lihat `01-brief.md`
- [x] Tidak ada field bernilai "TBD" atau kosong — 2 field brief tidak disebut brief asli (key, ensemble instrumentation, 7/8 grouping, exact bar count) direkam eksplisit di bagian "Asumsi" `01-brief.md`

### L2 (rubrik)

| Kriteria | Skor (0-2) | Alasan (1 kalimat) |
|---|---|---|
| Identitas artistik jelas | 2 | Judul, gaya (fusion odd-meter 7/8), dan karakter "restless→triumphant" tergambar konsisten dan konkret di `01-brief.md`. |
| Karakter/emosi konsisten dengan instrumentasi | 2 | Tenor sax + Rhodes + electric bass + drum kit adalah instrumentasi fusion idiomatik yang cocok dengan karakter restless/triumphant yang dipilih. |
| Arah energi masuk akal untuk gaya yang dipilih | 2 | Arc "tenang-tegang → klimaks → resolusi singkat" adalah bentuk arc fusion yang wajar untuk brief urgency-to-release. |

## Level 2 — Arsitektur Lagu

### L1 (mekanis)

- [x] Bentuk lagu dipilih secara eksplisit (through-composed) — `02-form.md`
- [x] Struktur performa lengkap tercantum dengan panjang bar (Intro 2, A 4, A′ 4, B 4, Climax 4, Coda 2 = 20)

### L2 (rubrik)

| Kriteria | Skor (0-2) | Alasan (1 kalimat) |
|---|---|---|
| Setiap bagian punya fungsi dramaturgis | 2 | Tiap section punya deskripsi dramaturgi yang berbeda dan spesifik (bukan label generik), dari "membuka dunia lagu" sampai "kesimpulan". |
| Ada kontras antar-bagian | 2 | Density (sparse→full→sparse) dan warna modal (Dorian→outside→brightened) berubah jelas antar section, dikonfirmasi oleh `06-arrangement.md`/`03-harmony.md`. |
| Klimaks ditempatkan pada bagian yang tepat | 2 | Klimaks di bar 15-18 (75-90% dari total 20 bar) setelah build B section — posisi lazim untuk arc "urgency to release" pendek. |

## Level 3 — Peta Harmoni

### L1 (mekanis)

- [x] Tonal center (D) dan harmonic rhythm (1 chord/bar, exception noted bar 14) ditentukan — `03-harmony.md`
- [x] Bar count skeleton (20) konsisten dengan Level 2

### L2 (rubrik)

| Kriteria | Skor (0-2) | Alasan (1 kalimat) |
|---|---|---|
| Tension map jelas per bar | 2 | Tabel `03-harmony.md` memberi label tension per bar (stabil/outside/dominan puncak/resolusi) untuk semua 20 bar tanpa lompatan. |
| Fungsi harmonik tiap chord teridentifikasi | 2 | Kolom "Function" mengisi label spesifik (modal interchange, tritone sub, secondary dominant, dst) untuk tiap chord, bukan label kosong. |
| Chord kompleks (extension/alteration) memang diperlukan, bukan dekorasi | 1 | Hampir semua chord (termasuk tonic Dm11/Dm9) memakai ekstensi/alterasi tanpa titik pembanding "polos", sehingga argumen "diperlukan bukan dekorasi" sulit diverifikasi karena tak ada kontras baseline. |

## Level 4 — Desain Melodi

### L1 (mekanis)

- [x] Motif inti (rising P4/falling m3), kontur, dan target tone ditentukan — `04-melody.abc`
- [x] Bar count melodi (bars 3-20 covered) konsisten dengan Level 3

### L2 (rubrik)

| Kriteria | Skor (0-2) | Alasan (1 kalimat) |
|---|---|---|
| Motif mudah dikenali dan dipertahankan | 2 | `song.abc` bar 3, 5, 7, 9 memakai sel D-G-E identik dan bar 4/6/8 memvariasikannya secara tertata, jadi motif tetap terdengar sebagai satu identitas. |
| Target tone/guide tone terhubung logis | 1 | Bar 8 (`Ebmaj7#11`) di `04-melody.abc` Tahap 6 menyatakan target Bnat, Tahap 8 menuliskan arpeggio ilustratif Eb-G-Bb-D, tetapi `song.abc` bar 8 aktual berbunyi Eb-Ab-F — tak satu pun cocok, dan `14-review.md` tidak mendokumentasikan penyimpangan ini (hanya bar 13/14/climax yang dicatat berubah). |
| Outside material (jika ada) terkontrol dan diresolusikan | 1 | Bar 8 memang genuinely outside (side-slip kromatik dari Dm); tapi bar 11-14 yang diklaim "outside" di `04-melody.abc` Tahap 8 ternyata di `song.abc` hanya memainkan chord-tone dari tiap chord eksotik itu sendiri (mis. bar 14 C#-E-G# = triad A7 polos, bukan tensi altered) — label "outside" untuk bar 11-14 terlalu longgar, resolusi di bar 15 tetap kuat tapi klaim "outside"-nya sebagian mislabel. |

## Level 5 — Desain Ritme dan Groove

### L1 (mekanis)

- [x] Feel (odd-meter 7/8, 4+3, straight eighths) dan rhythmic identity (syncopated/anticipatory) ditentukan eksplisit — `05-groove.md`

### L2 (rubrik)

| Kriteria | Skor (0-2) | Alasan (1 kalimat) |
|---|---|---|
| Placement aksen konsisten dengan feel yang dipilih | 2 | `song.abc` melodi konsisten diam 4 eighth lalu masuk di grup pendek, dan `09-drums.json` kick jatuh di step 1 dan step 9 (tepat batas 4+3) di hampir semua section — cocok dengan rencana. |
| Groove reference cukup spesifik untuk diturunkan ke comping/bass/drum | 2 | Deskripsi bass/kick sebagai "reference layer" langsung dipakai konsisten di `07-comping.md` (comping mengisi grup "4" yang kosong), `08-bassline.md`, dan `09-drums.json`. |

## Level 6 — Aransemen Instrumen

### L1 (mekanis)

- [x] Orchestration map mencakup semua 6 bagian dari Level 2 — `06-arrangement.md`

### L2 (rubrik)

| Kriteria | Skor (0-2) | Alasan (1 kalimat) |
|---|---|---|
| Setiap instrumen punya peran per bagian | 2 | Tiap section di `06-arrangement.md` merinci peran keempat instrumen (termasuk "silent" sebagai peran eksplisit di intro), bukan daftar generik. |
| Density berubah antar-bagian (bukan semua instrumen penuh terus) | 2 | Kurva density eksplisit sparse→medium→dense→full→sparse, dan hanya climax+hit terakhir yang memakai keempat instrumen penuh sekaligus. |

## Level 7 — Desain Comping dan Voicing

### L1 (mekanis)

- [x] Comping chart mencakup semua bagian yang butuh comping (semua kecuali intro, tacet by design) — `07-comping.md`

### L2 (rubrik)

| Kriteria | Skor (0-2) | Alasan (1 kalimat) |
|---|---|---|
| Voice leading antar-chord halus | 0 | `07-comping.md`/`14-review.md` mengklaim top note bergerak F→C→F→F#..., tapi voicing aktual di `song.abc` bar 3-4 (`[FAce]` lalu `[Ace]`) sama-sama bertopnote e, bukan F→C seperti yang diklaim — klaim voice-leading tidak cocok dengan notasi final. |
| Comping bergerak (bukan block chord statis) | 2 | Aktivitas comping berubah nyata per section (tacet→sparse 2 attacks→call-response→dense→disederhanakan jadi sustain di climax), bukan satu tekstur statis sepanjang lagu. |

## Level 8 — Desain Bass Line

### L1 (mekanis)

- [x] Bass concept ditentukan untuk setiap section (6/6) — `08-bassline.md`

### L2 (rubrik)

| Kriteria | Skor (0-2) | Alasan (1 kalimat) |
|---|---|---|
| Bass punya kontur (bukan selalu root) | 2 | `song.abc` V:3 bar 3-6 memainkan D-F-D, G-B-D, D-F-A, C-E-G — persis kontur chord-tone yang diklaim `08-bassline.md`, bukan sekadar root statis. |
| Approach note ke chord berikutnya masuk akal | 2 | Chromatic approach D→Eb (bar 8→9) dan walk D-F-A-Ab menuju G7alt (bar 9→10) yang diklaim benar-benar muncul di `song.abc` V:3, bukan hanya prosa. |

## Level 9 — Desain Drum

### L1 (mekanis)

- [x] Bar count drum grid sama persis dengan ABC section demi section: `drums.json` sections sum to 20 bars (script-verified); `song.abc` = 20 bars per voice (script-verified); `02-form.md` = 20 bars. Semua tiga sepakat.

### L2 (rubrik)

| Kriteria | Skor (0-2) | Alasan (1 kalimat) |
|---|---|---|
| Dinamika drum mengikuti struktur lagu | 2 | `09-drums.json` menambah instrumen (kick busier, ride, hi-hat 16th, crash) tepat sinkron dengan curve density `06-arrangement.md`/energy `13-dynamics.md`. |
| Fills/setup ditempatkan pada transisi yang logis | 2 | Snare fill "........x..x.." muncul di bar 9-10 tepat sebelum masuk B section, sesuai klaim transisi di `11-transitions.md`. |

## Level 10 — Desain Improvisasi

### L1 (mekanis)

- [x] Solo map: N/A oleh desain, dijustifikasi eksplisit di `10-solo-map.md` (bukan diam-diam dilewati, bukan skor 0)

### L2 (rubrik)

| Kriteria | Skor (0-2) | Alasan (1 kalimat) |
|---|---|---|
| Solo section punya arah perkembangan (bukan datar) | N/A | Tidak ada solo section oleh desain (through-composed, brief tidak minta vehicle jam) — dijustifikasi eksplisit di `10-solo-map.md`. |
| Background figure (jika ada) mendukung, bukan mengganggu | N/A | Tidak ada background figure solo karena tidak ada solo section — konsekuensi langsung dari absennya Level 10 yang sudah dijustifikasi. |

## Level 11 — Interlude, Shout Chorus, dan Transisi

### L1 (mekanis)

- [x] Bagian transisi tertulis eksplisit di setiap batas section — `11-transitions.md`

### L2 (rubrik)

| Kriteria | Skor (0-2) | Alasan (1 kalimat) |
|---|---|---|
| Shout chorus terasa sebagai klimaks | 2 | Meski tak ada shout chorus terpisah 8-16 bar, bar 15-18 (`song.abc`) benar-benar unison/harmonized hit di ketiga voice serentak dengan crash+ride penuh di `09-drums.json`, memenuhi fungsi shout secara proporsional seperti diargumentasikan. |
| Transisi tidak terasa tiba-tiba/janggal | 2 | Tiap batas section dipasangkan device konkret yang terverifikasi (fill drum bar 9-10, dominant pedal A7alt bar 14, drop tekstural climax→coda), bukan pernyataan generik. |

## Level 12 — Intro dan Ending

### L1 (mekanis)

- [x] Intro dan ending punya identitas materi sendiri (bass riff / motif utama, bukan placeholder) — `12-intro-ending.md`

### L2 (rubrik)

| Kriteria | Skor (0-2) | Alasan (1 kalimat) |
|---|---|---|
| Intro memperkenalkan dunia lagu | 2 | Intro (bass+kick ostinato di `09-drums.json`/`song.abc`) sudah menetapkan asimetri 4+3 sebelum melodi masuk, sesuai klaim di `12-intro-ending.md`. |
| Ending berhubungan dengan motif utama | 1 | Ending diklaim "restates rising-4th shape, widened" tapi not aktual bar 19 (`a2 ^f2 d3`) justru turun (a→f#→d), arah terbalik dari climax bar 17 yang naik (`a2 d'2 ^f'3`) — hubungan intervalik ada (pitch class sama) tapi arah kontur yang diklaim tidak persis cocok. |

## Level 13 — Dinamika dan Dramaturgi

### L1 (mekanis)

- [x] Energy curve tercantum per section dengan angka eksplisit (15%->100%->fade) — `13-dynamics.md`

### L2 (rubrik)

| Kriteria | Skor (0-2) | Alasan (1 kalimat) |
|---|---|---|
| Kurva energi masuk akal untuk arc lagu | 2 | Kurva 15%→30%→45%→70/85%→100%→40%→0% naik monoton lalu jatuh tajam, cocok dengan brief "urgency building to triumphant climax". |
| Parameter dinamika bervariasi (bukan hanya volume) | 2 | Register, density, tensi harmonik, aktivitas ritmis, jumlah instrumen, dan silence semua dilacak terpisah dan konsisten dengan artefak level lain (`06`, `03`, `09`). |

## Level 14 — Detail Low Level

### L1 (mekanis) — hasil aktual, diperiksa langsung dari file (bukan hanya exit status)

- [x] `validate_abc.py` lulus: **"OK: 0 errors, 0 warning(s)"** (run dengan venv `pretty_midi`/`music21` yang disediakan)
- [x] `music21.converter.parse()` langsung terhadap `song.abc`: berhasil, **3 parts** — cek kedua di luar validator sendiri, sesuai anjuran `abc-notation/SKILL.md` Step 4.
- [x] `output.mid` diperiksa langsung dari file (bukan hanya status validator):
  - **4 track**: Tenor Sax (50 notes, max-poly 1 — monophonic, benar untuk lead), Rhodes (67 notes, max-poly 4 — chordal comping, benar), Bass (53 notes, max-poly 1 — monophonic, benar), Drums (260 hits, channel 10/`is_drum=True`).
  - **Tempo**: 80 BPM (quarter-note) tertanam di MIDI — ini setara `Q:1/8=160` di ABC (eighth-note pulse 160, quarter 80); dicek lewat `pretty_midi.get_tempo_changes()`, bukan diasumsikan.
  - **Time signature**: **(7, 8)** tertanam di MIDI pada waktu 0.0 — dicek lewat `pretty_midi.time_signature_changes`, mengonfirmasi meter 7/8 benar-benar sampai ke file, bukan default 4/4 yang diam-diam disisipkan converter.
  - Semua 20 bar di ketiga voice ABC + drum grid saling cocok bar-demi-bar (lihat bagian "Validasi mesin lintas-level" di atas).
  - Catatan kecil (bukan bug): drum track's last note-off (~50.8s) berakhir sedikit lebih awal dari pitched tracks (~52.5s) karena hit terakhir drum-grid ada di awal bar coda terakhir, bukan disustain sampai akhir bar — bukan drift bar count (bar count tetap 20/20 match), hanya karakter hit pendek di not terakhir.

### L2 (rubrik)

| Kriteria | Skor (0-2) | Alasan (1 kalimat) |
|---|---|---|
| Voice leading halus di level not | 1 | Bass dan melodi bisa diverifikasi cocok dengan desain, tapi klaim voice-leading Rhodes di `07-comping.md`/`14-review.md` tidak cocok dengan top-note aktual di `song.abc` bar 3-4 (lihat Level 7). |
| Register seimbang antar-instrumen | 2 | Sax naik ke oktaf tertinggi hanya di climax, bass melompat oktaf (D,→d) tepat di climax untuk bobot, Rhodes tetap di register menengah — sesuai klaim `13-dynamics.md`/`14-review.md`. |
| Voicing tidak terlalu padat | 2 | Voicing Rhodes climax memang disederhanakan jadi satu chord sustain penuh bar (`[D^FAd]7` dst di `song.abc`), kontras disengaja dengan B section yang lebih padat. |
| Ending terasa selesai | 2 | Bar 20 seluruh voice landing di D (unison/oktaf D-d), resolusi terbuka yang jelas mengakhiri arc setelah climax. |

## L3 (telinga) — hanya diisi sekali, di akhir

*menunggu telinga manusia — belum diisi. `output.mid` sudah tersedia di
run folder ini untuk didengarkan.*

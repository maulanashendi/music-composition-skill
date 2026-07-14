# Scorecard — Settling In (Late) / 2026-07-14-doubt-to-acceptance

Catatan proses: L1 (mekanis) di bawah diisi oleh agent yang menulis
artefak ini (checks otomatis/dijalankan, bukan penilaian subjektif — ini
diperbolehkan). **Semua L2 (rubrik) diisi 2026-07-14 oleh reviewer segar**
(subagent baru, tanpa histori percakapan generasi artefak — hanya membaca
artefak run folder ini + rubric.md modul terkait), memenuhi larangan
self-grading di `../../skills/jazz-composition/SKILL.md` (§Reviewer segar).
L3 (telinga) masih belum diisi — butuh manusia, per
`../../skills/jazz-composition/references/human-ear-protocol.md`.

## Validasi mesin lintas-level

- [x] Label section unik: Intro, A1, B, Outro — tidak ada duplikat.
- [x] Bar count/durasi chord valid: tiap bar di `03-harmony.md`/`song.abc`
      berisi tepat 8 eighth-note (L:1/8, M:4/4) worth of duration —
      dikonfirmasi lulus oleh `validate_abc.py` (0 errors).
- [x] Section terbuka dilabeli eksplisit: tidak ada section "solo"/
      "shout chorus" yang disebut lalu tidak dipakai — `10-solo-map.md`
      dan `11-transitions.md` eksplisit mencatat bahwa keduanya tidak
      ada di piece ini (bukan lupa ditulis).
- [x] Performance order/solo form merujuk section yang benar-benar ada:
      tidak ada solo form (lihat di atas).
- [x] Plan cocok dengan prosa dan notasi: bar count `09-drums.json`
      (2+2+7+1+4+6+1+1=24) = bar count `song.abc` (4+8+4+8=24). Dicek
      manual, bukan lewat validator otomatis khusus cross-file (tidak ada
      validator seperti itu di paket ini saat ini) — dicatat di sini
      bahwa pengecekan ini manual, bukan diam-diam dilewati.

## Level 1 — Konsep Artistik

### L1 (mekanis)

- [x] Semua field brief wajib terisi (Judul sementara, Gaya, Tempo,
      Birama, Karakter, Instrumentasi, Kompleksitas, Arah energi) — lihat
      `01-brief.md`
- [x] Tidak ada field bernilai "TBD" atau kosong — field yang brief tidak
      sebutkan eksplisit dicatat sebagai asumsi (§ Asumsi), bukan "TBD"

### L2 (rubrik)

Diisi reviewer segar (2026-07-14), sumber: `01-brief.md` saja.

| Kriteria | Skor (0-2) | Alasan (1 kalimat) |
|---|---|---|
| Identitas artistik jelas | 2 | Judul, gaya, karakter, dan arah energi dinyatakan konkret dan spesifik, bukan generik ("neo-soul/chill-jazz reflektif" + arc doubt→acceptance tiga-fase). |
| Karakter/emosi konsisten dengan instrumentasi | 2 | Alto sax mid-register, rhodes, fingered bass, dan brushed/lo-fi drum semuanya cocok dengan "late-night, laid-back, reflektif" tanpa kombinasi yang janggal. |
| Arah energi masuk akal untuk gaya yang dipilih | 1 | Arc tenang→terbuka→tenang cocok dengan larangan brief soal klimaks besar, tapi field ini hanya prosa satu paragraf tanpa kurva/angka (itu baru muncul di `13-dynamics.md`, level lain) sehingga di level ini sendiri masih dangkal. |

## Level 2 — Arsitektur Lagu

### L1 (mekanis)

- [x] Bentuk lagu dipilih secara eksplisit (through-composed pendek,
      lihat `02-form.md` § Asumsi)
- [x] Struktur performa lengkap tercantum dengan panjang bar (Intro 4,
      A1 8, B 4, Outro 8 = 24)

### L2 (rubrik)

*menunggu reviewer segar*

| Kriteria | Skor (0-2) | Alasan (1 kalimat) |
|---|---|---|
| Setiap bagian punya fungsi dramaturgis | 2 | Tabel di `02-form.md` memberi fungsi berbeda dan spesifik ke tiap bagian (buka dunia lagu / statement penuh / lift terkendali / resolusi+subtraksi), bukan label kosong. |
| Ada kontras antar-bagian | 2 | Kontras nyata lewat densitas dan tekstur (Intro nyaris diam → A1 penuh tapi sparse → B satu-satunya lift → Outro menipis ke diam), dikonfirmasi juga oleh `06-arrangement.md`/`13-dynamics.md`. |
| Klimaks ditempatkan pada bagian yang tepat | 1 | Brief eksplisit melarang klimaks besar, jadi kriteria ini secara literal tidak berlaku penuh; "lift" pengganti klimaks (bagian B) ditempatkan masuk akal (sebelum resolusi), tapi dokumen ini tidak membandingkan alternatif penempatan lain sehingga klaimnya asertif, bukan diuji. |

## Level 3 — Peta Harmoni

### L1 (mekanis)

- [x] Tonal center (Cm) dan harmonic rhythm (1 chord/bar) ditentukan
- [x] Bar count skeleton (24) konsisten dengan Level 2

### L2 (rubrik)

*menunggu reviewer segar*

| Kriteria | Skor (0-2) | Alasan (1 kalimat) |
|---|---|---|
| Tension map jelas per bar | 2 | Tabel bar-by-bar 1-24 di `03-harmony.md` mencatat arah tegangan konkret (stabil/meningkat/tertahan/resolusi) untuk setiap bar, bukan hanya per-section. |
| Fungsi harmonik tiap chord teridentifikasi | 2 | Setiap chord diberi label fungsi eksplisit (tonic/predominant-ish/subdominant minor/dominant, dst.) sesuai bar. |
| Chord kompleks (extension/alteration) memang diperlukan, bukan dekorasi | 1 | Rasional diberikan untuk tiap chord non-diatonis (bIII, G7alt, Bbm7b5) tapi semuanya alasan prosa ("menambah ambiguitas") tanpa verifikasi terhadap efek nyata di melodi/voicing — sama persis pola "alasan yang terdengar masuk akal" yang diperingatkan `RED-FLAGS.md`. |

## Level 4 — Desain Melodi

### L1 (mekanis)

- [x] Motif inti, kontur, dan target tone ditentukan (`04-melody.abc`)
- [x] Bar count melodi (24, tersebar Intro/A1/B/Outro) konsisten dengan
      Level 3

### L2 (rubrik)

*menunggu reviewer segar*

| Kriteria | Skor (0-2) | Alasan (1 kalimat) |
|---|---|---|
| Motif mudah dikenali dan dipertahankan | 2 | Cell 4-not (naik minor third, turun step, mendarat tak-resolve) muncul dan dikenali di hook (bar 5), answer variasi (bar 9-10), dan tail Outro — identitas ritmis/interval bertahan lewat variasi, bukan hilang. |
| Target tone/guide tone terhubung logis | 1 | Tabel guide-tone (3rd/6th) hanya dipetakan untuk 4 chord A1 statement; B dan Outro tidak punya tabel target-tone eksplisit yang sama, jadi klaim "terhubung logis" hanya diverifikasi sebagian bagian piece. |
| Outside material (jika ada) terkontrol dan diresolusikan | 1 | Bagian B diberi label "outside material" tapi not yang dipakai (e,g,b lalu a,b) adalah chord tone diatonis Ebmaj7/Fm9, bukan vokabuler chromatic/di luar harmoni — istilah "outside" di dokumen tidak cocok dengan isi notasinya sendiri, meski durasi terbatas dan resolusinya memang jelas. |

## Level 5 — Desain Ritme dan Groove

### L1 (mekanis)

- [x] Feel (swung-16th, laid-back) dan rhythmic identity (spacious,
      sparingly syncopated) ditentukan eksplisit

### L2 (rubrik)

*menunggu reviewer segar*

| Kriteria | Skor (0-2) | Alasan (1 kalimat) |
|---|---|---|
| Placement aksen konsisten dengan feel yang dipilih | 2 | Pilihan syncopation/anticipation/displacement dijelaskan satu-satu dengan alasan konsisten ke "doubt yang searching, bukan bergerak maju" — bukan daftar generik. |
| Groove reference cukup spesifik untuk diturunkan ke comping/bass/drum | 2 | Tiga sub-bagian ("Groove reference untuk turunan Level 7/8/9") memberi instruksi konkret per instrumen (attack/bar, sparse+approach note, pola drum per section) yang memang cocok dengan isi `07-comping.md`/`08-bassline.md`/`09-drums.json`. |

## Level 6 — Aransemen Instrumen

### L1 (mekanis)

- [x] Orchestration map mencakup semua bagian dari Level 2 (Intro, A1,
      B, Outro — lihat `06-arrangement.md`)

### L2 (rubrik)

*menunggu reviewer segar*

| Kriteria | Skor (0-2) | Alasan (1 kalimat) |
|---|---|---|
| Setiap instrumen punya peran per bagian | 2 | Tabel 4-instrumen x 4-bagian di `06-arrangement.md` mengisi peran berbeda untuk tiap sel, tidak ada sel generik "main seperti biasa". |
| Density berubah antar-bagian (bukan semua instrumen penuh terus) | 2 | Kurva density eksplisit (sparse→medium→medium-lift-1-dimensi→sparse menurun) dan piece tidak pernah mencapai "dense" di section manapun, sesuai brief. |

## Level 7 — Desain Comping dan Voicing

### L1 (mekanis)

- [x] Comping chart mencakup semua bagian yang butuh comping (4/4 bagian)

### L2 (rubrik)

*menunggu reviewer segar*

| Kriteria | Skor (0-2) | Alasan (1 kalimat) |
|---|---|---|
| Voice leading antar-chord halus | 1 | Hanya dua transisi chord yang benar-benar diverifikasi (Cm9→Abmaj7, Abmaj7→Fm9) dari total ~10 perubahan chord di piece; klaim "voice leading dicek" berlebihan dibanding bukti yang ditulis. |
| Comping bergerak (bukan block chord statis) | 1 | Dokumen sendiri mengakui comping tetap "sustained pad, 1 attack/bar" nyaris sepanjang piece dan menyebut pergerakan hanya lewat perubahan voicing antar-chord, bukan ritme — secara literal ini condong ke block-chord statis, kriteria hanya terpenuhi sebagian. |

## Level 8 — Desain Bass Line

### L1 (mekanis)

- [x] Bass concept ditentukan untuk setiap section (4/4)

### L2 (rubrik)

*menunggu reviewer segar*

| Kriteria | Skor (0-2) | Alasan (1 kalimat) |
|---|---|---|
| Bass punya kontur (bukan selalu root) | 2 | `song.abc` V:3 memang berisi chromatic approach note tiap batas bar A1/B (mis. =E,, =A,, =B,, D,), bukan root murni, kecuali dua bar terakhir Outro yang sengaja dan diakui eksplisit sebagai root. |
| Approach note ke chord berikutnya masuk akal | 2 | Dicek langsung di `song.abc`: tiap approach note setengah-langkah di bawah root chord berikutnya (mis. =E, sebelum Fm9, =A, sebelum Bbm7b5, D, sebelum Ebmaj7 lintas-section) — konsisten secara harmonik, bukan asal taruh. |

## Level 9 — Desain Drum

### L1 (mekanis)

- [x] Bar count drum grid (2+2+7+1+4+6+1+1=24) sama persis dengan bar
      count `song.abc` (4+8+4+8=24), section demi section

### L2 (rubrik)

*menunggu reviewer segar*

| Kriteria | Skor (0-2) | Alasan (1 kalimat) |
|---|---|---|
| Dinamika drum mengikuti struktur lagu | 2 | Pattern `09-drums.json` per-section jelas mengikuti arc (silent→minimal groove→lift hat/kick→subtraksi bertahap→silent), label tiap section eksplisit menyebut alasan musikalnya. |
| Fills/setup ditempatkan pada transisi yang logis | 1 | Tidak ada fill/setup drum sungguhan di titik manapun (perubahan hanya lewat ganti pattern section, bukan hit setup); ini keputusan sadar ("bukan drum fill/breakdown", lihat `11-transitions.md`) tapi berarti kriteria literal "fills ditempatkan" tidak benar-benar dipenuhi. |

## Level 10 — Desain Improvisasi

### L1 (mekanis)

- [x] Solo map mencantumkan jumlah chorus per solois — **0 chorus**,
      alasan dicatat eksplisit di `10-solo-map.md` (piece tidak
      mengandung solo section)

### L2 (rubrik)

*menunggu reviewer segar — catatan: rubrik "solo section punya arah
perkembangan" tidak berlaku karena tidak ada solo section di piece ini;
reviewer segar perlu menilai apakah keputusan "0 solo" itu sendiri masuk
akal terhadap brief, bukan mengarang skor untuk solo yang tidak ada*

| Kriteria | Skor (0-2) | Alasan (1 kalimat) |
|---|---|---|
| Solo section punya arah perkembangan (bukan datar) | N/A | tidak ada solo section (lihat `10-solo-map.md`) |
| Background figure (jika ada) mendukung, bukan mengganggu | N/A | tidak ada solo section |

## Level 11 — Interlude, Shout Chorus, dan Transisi

### L1 (mekanis)

- [x] Bagian transisi tertulis eksplisit (3 transisi, lihat
      `11-transitions.md`), bukan diasumsikan

### L2 (rubrik)

*menunggu reviewer segar*

| Kriteria | Skor (0-2) | Alasan (1 kalimat) |
|---|---|---|
| Shout chorus terasa sebagai klimaks | N/A | tidak ada shout chorus (lihat `11-transitions.md`) |
| Transisi tidak terasa tiba-tiba/janggal | 2 | Ketiga sambungan (Intro→A1 handoff melodi, A1→B kejutan harmonik, B→Outro resolusi dominant) masing-masing punya device bernama dan lokasi bar yang bisa dicek langsung di `song.abc`, bukan diasumsikan mulus tanpa bukti. |

## Level 12 — Intro dan Ending

### L1 (mekanis)

- [x] Intro dan ending punya identitas materi sendiri (bukan
      placeholder) — lihat `12-intro-ending.md`

### L2 (rubrik)

*menunggu reviewer segar*

| Kriteria | Skor (0-2) | Alasan (1 kalimat) |
|---|---|---|
| Intro memperkenalkan dunia lagu | 2 | Bar 1-4 di `song.abc` konsisten dengan klaim dokumen (Cm9 held 2 bar penuh, lalu hook fragment bare di Rhodes saja bar 3-4) — register, harmoni, dan motif diperkenalkan tanpa memainkan tema penuh. |
| Ending berhubungan dengan motif utama | 1 | Klaim "falling tail" di bar 19-20/23 hanya sebagian cocok dengan notasi aktual: not di bar 19 (E2 A4) justru naik seperti hook asli, bukan turun seperti diklaim, dan fragment bar 23 cuma satu not tunggal (A2) — hubungan ke motif ada tapi istilah "falling" tidak akurat terhadap `song.abc`. |

## Level 13 — Dinamika dan Dramaturgi

### L1 (mekanis)

- [x] Energy curve tercantum per section dengan angka/persentase (lihat
      `13-dynamics.md`)

### L2 (rubrik)

*menunggu reviewer segar*

| Kriteria | Skor (0-2) | Alasan (1 kalimat) |
|---|---|---|
| Kurva energi masuk akal untuk arc lagu | 2 | Kurva 10%→25/20%→45%→30/5% naik-turun sesuai arc doubt→turning→acceptance dan tidak pernah menyentuh "tinggi", cocok dengan larangan klimaks besar di brief. |
| Parameter dinamika bervariasi (bukan hanya volume) | 2 | Tujuh dimensi berbeda didaftar dengan contoh konkret per dimensi (register, density, artikulasi, harmonic tension, rhythmic activity, jumlah instrumen, panjang nada) — bukan hanya klaim "dinamis" tanpa rincian. |

## Level 14 — Detail Low Level

### L1 (mekanis)

- [x] `validate_abc.py` lulus tanpa error — `OK: 0 errors, 0 warning(s)`
- [x] `output.mid`: 4 track (Sax 24 notes, Rhodes 88 notes, Bass 30
      notes, Drums 150 notes) — semua > 0; tempo 78.000078 BPM cocok
      `Q:1/4=78`; meter 4/4 cocok `M:4/4` — diperiksa langsung dari
      `pretty_midi.PrettyMIDI(output.mid)`, bukan hanya exit status
      validator (lihat `14-review.md` untuk log lengkap)

### L2 (rubrik)

*menunggu reviewer segar*

| Kriteria | Skor (0-2) | Alasan (1 kalimat) |
|---|---|---|
| Voice leading halus di level not | 1 | Sama seperti L7: pengecekan voice leading di `07-comping.md` hanya mencontohkan 2 dari ~10 transisi chord, jadi "diperiksa" di `14-review.md` sebenarnya mewarisi cakupan parsial itu, bukan verifikasi penuh. |
| Register seimbang antar-instrumen | 0 | Tidak ada satu pun bagian di `14-review.md` (atau artefak lain) yang secara eksplisit mengecek potensi tabrakan register antara Sax lead dan Rhodes comping — kriteria ini absen, bukan sekadar dangkal. |
| Voicing tidak terlalu padat | 2 | Rootless-shell/quartal dipakai konsisten (dicek di `07-comping.md`), tidak ada block chord penuh/dobel, dan `output.mid` Rhodes max-poly 4 konsisten dengan voicing 4-not yang didesain. |
| Ending terasa selesai | 2 | Bar 24 diverifikasi held Cm9(add9) penuh, drum sudah silent sejak bar 24, bass sustain root, tanpa Picardy third — cocok dengan brief "not a big triumphant ending, just settling". |

## L3 (telinga) — hanya diisi sekali, di akhir

*Belum diisi. `output.mid` sudah tersedia di
`runs/2026-07-14-doubt-to-acceptance/output.mid` — L3 menunggu sesi
`../../skills/jazz-composition/references/human-ear-protocol.md` oleh manusia/reviewer terpisah.*

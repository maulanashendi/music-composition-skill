# Scorecard — Home by Dawn (dawn-shift-home)

## Level 1 — Konsep Artistik

### L1 (mekanis)

- [x] Semua field brief wajib terisi (Judul sementara, Gaya, Tempo, Birama,
      Karakter, Instrumentasi, Kompleksitas, Arah energi) — lihat `01-brief.md`
- [x] Tidak ada field bernilai "TBD" atau kosong

### L2 (rubrik)

Diisi oleh subagent reviewer segar tanpa konteks generasi (self-grading
dilarang).

| Kriteria | Skor (0-2) | Alasan (1 kalimat) |
|---|---|---|
| Fakta user dan asumsi dipisahkan; mood/gaya/groove/instrumentasi tidak tercampur jadi satu blob | 2 | Field inti (judul, gaya, tempo, birama, karakter, instrumentasi, kompleksitas, arah energi) tercantum baris per baris di badan brief, dan seluruh asumsi (key, panjang bar, pilihan lead instrument, risiko warisan) dipisah eksplisit ke section "## Asumsi" tersendiri. |
| DNA tetap (fixed), parameter fleksibel, arrival terlindungi, dan shortcut terlarang dinyatakan eksplisit | 1 | Tempo dikunci eksplisit ("tidak pernah berubah sepanjang lagu") dan arrival dilindungi jelas (satu-satunya lompatan interval lebar, konvergensi eksplisit "BUKAN puncak kedua yang bersaing"), tapi brief tidak menyatakan secara eksplisit parameter mana yang sengaja dibiarkan fleksibel untuk level berikutnya. |
| Minimal dua konsep berbeda secara struktural dipertimbangkan (kecuali user sudah mengunci desain), dan kriteria pemilihannya eksplisit | 1 | Brief mengonfirmasi dua kandidat berbeda struktural sudah dipertimbangkan (Kandidat A "accretive texture" menang, dengan satu graft konvergensi unison dari Kandidat B), tapi kriteria pemilihan konkretnya tidak dikutip di file brief ini sendiri, hanya dirujuk ke dokumen lain. |
| Gaya memakai penanda lebih dari sekadar superfisial (mis. lofi bukan cuma vinyl noise + maj7, jazz-funk tidak disamakan dengan hip-hop) | 2 | Penanda gaya mencakup pilihan mode (Dorian vs Aeolian/harmonic-minor yang lebih dramatis), tingkat kompleksitas (modal menengah-rendah, bukan reharm bebop yang padat), dan peran instrumen spesifik (walking/pedal bass, comping Rhodes, drum lo-fi masuk bertahap dari hi-hat/rimshot), bukan sekadar label genre atau tempo. |
| Materi referensi diterjemahkan jadi atribut luas, bukan disalin; tidak ada sample berhak cipta/melodi dikenali/gaya artis hidup yang direproduksi | 2 | Brief menyatakan eksplisit bahwa kualitas "solitary walking at dawn" adalah "referensi atribut, bukan meniru rekaman/artis tertentu", diterjemahkan jadi atribut musikal konkret (timbre breathy, register menengah-tinggi, serangan lembut) tanpa menyebut rekaman atau artis spesifik. |

## Level 2 — Arsitektur Lagu

### L1 (mekanis)

- [x] Bentuk lagu dipilih secara eksplisit (through-composed + bookend
      return — lihat `02-form.md`)
- [x] Struktur performa lengkap (6 section, bar 1-24) tercantum dengan
      panjang bar

### L2 (rubrik)

| Kriteria | Skor (0-2) | Alasan (1 kalimat) |
|---|---|---|
| Setiap section punya bar count/durasi eksplisit dan fungsi dramaturgis yang jelas ke pendengar | 2 | Tabel 6 section mencantumkan bar, panjang, dan fungsi dramaturgis eksplisit untuk semua bagian, konsisten dengan total 24 bar. |
| Identitas (motif/groove) tetap dikenali setelah transformasi; repetisi loop punya alasan (bukan diulang literal 3x tanpa tujuan) | 1 | Prinsip "graft, jangan hapus total lapisan, sisakan jejak" disebut eksplisit untuk penipisan section 5, tapi detail motif konkret didelegasikan ke file lain (04-melody.abc), tidak dijelaskan langsung di sini. |
| Setiap batas antar-section punya transisi yang disengaja (cut langsung atau transisi terancang), bukan default fill/riser generik di semua tempat | 1 | Section 5 disebut sebagai "transisi turun yang disengaja" dan ada catatan penyesuaian bar, tapi mekanisme transisi konkret per-batas belum dirinci (baru didetailkan di 11-transitions.md). |
| Setiap instrumen/track punya peran utama yang berarti per section; akomodasi memberi ruang dan menghindari konflik register | 1 | Kolom "Instrumentasi aktif" mencantumkan siapa main per section, tapi peran spesifik dan pertimbangan register belum dijelaskan di sini (baru dirinci di 06-arrangement.md). |
| Solo/improvisasi punya landmark form, target/guide tone yang jelas, dan jalur kembali (return path) jika memakai materi outside | N/A | Absennya solo section dinyatakan eksplisit dan dijustifikasi di file ini sendiri (baris 35-37): piece through-composed 24 bar bukan untuk di-solo-i berulang. |
| Klimaks disiapkan (bukan tiba-tiba) dan punya konsekuensi; setidaknya satu elemen "subtraction" hadir jika bukan konsep akumulasi kontinu | 2 | Klimaks tunggal di section 4 dibangun bertahap dari section 1-3 (accretive), dan section 5 eksplisit berupa "penipisan subtraktif" dengan graft menyisakan jejak. |

## Level 3 — Peta Harmoni

### L1 (mekanis)

- [x] Tonal center (D) dan harmonic rhythm ditentukan
- [x] Bar count skeleton (24 bar) konsisten dengan Level 2

### L2 (rubrik)

| Kriteria | Skor (0-2) | Alasan (1 kalimat) |
|---|---|---|
| Fungsi harmonik tiap chord jelas (tonic/predominant/dominant/dst), atau local center/proses nonfungsional teridentifikasi | 1 | Setiap bar (1-24) diberi label fungsi eksplisit (tonic/borrowed iv/diatonik bVII-bIII/dominant), tapi ringkasan gate `notation_facts.py` menyatakan "Dm9=diatonik ×6" padahal tabel utama menunjukkan 9 bar berlabel Dm9 di segmen bar 1-14, sehingga verifikasi tonic itu sendiri tidak sepenuhnya konsisten secara internal. |
| Event non-diatonis (alterasi, pedal, planing, polychord) punya rasionale fungsional/modal/voice-leading/warna/formal | 2 | Kedua chord non-diatonis (Gm7 bar 6, Gm9 bar 11) diberi rasionale modal eksplisit (borrowed iv dari D Aeolian, warna "wistful" neo-soul dengan rujukan referensi genre), dan hasil gate-check untuk keduanya konsisten 1:1 dengan tabel utama. |
| Ritme harmonik cocok dengan tempo dan groove; menghapus satu chord dekoratif tidak akan memperjelas progresi | 1 | Harmonic rhythm dijelaskan dan dikaitkan ke kurva dramaturgis (sedang di section aktif, melambat drastis di section 5-6, tak ada chord yang tampak dekoratif/bisa dihapus), tapi file ini tidak pernah mengaitkannya ke nilai tempo/BPM atau feel groove yang konkret. |
| Voicing eksak (pitch dan oktaf) disediakan ketika brief butuh voicing spesifik; nilai MIDI sesuai nama pitch di output DAW-first | 0 | Peta harmoni hanya memberi simbol chord (mis. Dm9, A7sus4, D6add9) tanpa satu pun pitch atau oktaf eksak/nilai MIDI, dan tidak ada pernyataan eksplisit bahwa voicing detail sengaja didelegasikan ke level lain. |
| Top line dan inner-line voicing bergerak dengan sengaja; tension teralter di-resolve, dilanjutkan, atau ditransformasi secara sengaja | 1 | Kolom Tension melacak naik-turunnya tension chord secara sengaja (penipisan progresif D9/Cmaj7#11 -> D6add9 -> triad polos sebagai "mereda", A7sus4 membuang not ke-3 secara sengaja di titik pivot), tapi tidak ada pembahasan pergerakan top-line/inner-voice secara konkret not-per-not. |
| Register dan alokasi tangan/instrumen playable; kepadatan register rendah terkontrol; voicing aktual cocok dengan label chord | 1 | Kesesuaian voicing aktual dengan label chord diverifikasi lewat music21 untuk kasus spesifik (ejaan CMaj9/D6add9 menghasilkan pitch set yang benar), tapi register, alokasi instrumen/tangan, dan kepadatan register rendah sama sekali tidak dibahas di file ini. |

## Level 4 — Desain Melodi

### L1 (mekanis)

- [x] Motif inti, kontur, dan target tone ditentukan
- [x] Bar count melodi (bar 13-24) konsisten dengan Level 3

### L2 (rubrik)

Diisi oleh subagent reviewer segar tanpa konteks generasi (tidak membaca
`04-melodi-candidates.md`). Level 4 ditopang dua modul sekaligus
(`melody-design` + `advanced-melody`), jadi tabel berikut menggabungkan
kriteria penuh dari kedua rubrik referensinya.

| Kriteria | Sumber | Skor (0-2) | Alasan (1 kalimat) |
|---|---|---|---|
| Satu motif utama (plus maksimal satu motif kontras yang benar-benar perlu) mengorganisasi keseluruhan piece | melody-design | 2 | Satu motif (leap major 6th A->F#, recovery ke E/9th) mengorganisasi seluruh alur Statement->Leap->Answer->Fragment->Absence->Convergence tanpa motif kontras kedua yang bersaing. |
| Identitas ritmis dan interval tetap dikenali setelah transformasi | melody-design | 2 | Interval leap +9 lalu -2 (tervalidasi `notation_facts.py`) muncul konsisten di bar 16, fragment bar 18, dan konvergensi bar 22-24 tanpa berubah bentuk. |
| Panjang phrase, napas, silence, dan target note terasa jelas (bukan aliran nada tanpa jeda) | melody-design | 1 | Struktur frasa dan rest eksplisit (z4/z2/z6 dst.) jelas, tapi label interval di bar 17 keliru (B->G ditulis "minor 3rd turun", padahal 4 semitone = major 3rd), sehingga akurasi deskripsi target note tidak sepenuhnya konsisten. |
| Nada panjang/berulang/aksen/akhir-frasa cocok dengan harmoni, atau sengaja menantangnya dengan alasan | melody-design | 2 | Semua target (F,A pada Dm9; A pada A7sus4; F#,E pada D9; B,G pada Cmaj7#11) chord-tone, dan potensi cross-relation B natural vs Bb (Gm7) dianalisis eksplisit lalu dibuktikan tidak pernah bertabrakan secara waktu. |
| Range dan tessitura sesuai instrumen lead | melody-design | 1 | Instrumen lead disebut (flugelhorn/muted trumpet) dan register disinggung sebagai sumber tension, tapi tidak ada pembahasan eksplisit apakah rentang nada F4-F#5 idiomatis/nyaman untuk instrumen tersebut. |
| Klimaks tidak dilemahkan oleh titik tinggi yang sudah berulang sebelumnya; head tetap memorable setelah nada dekoratif dihapus | melody-design | 2 | Leap ke F#5 eksplisit dinyatakan "satu-satunya lompatan lebar di seluruh lagu", pengulangan berikutnya diberi label gema/kutipan (bukan pernyataan baru), dan motif tetap dikenali saat direduksi ke 2 nada telanjang (fragment bar 18). |
| Outside material/chromatic vocabulary hanya dipakai pada bar yang tension map memang menandai butuh tegangan tinggi, bukan ditaburkan merata | advanced-melody | N/A | Motif LEAD sengaja 100% chord-tone tanpa outside pitch sama sekali (Tahap 8) karena tension dibawa oleh harmoni (borrowed iv), jadi tidak ada outside material untuk dinilai penempatannya. |
| Setiap enclosure/approach note punya target diatonis yang jelas dan tercapai | advanced-melody | N/A | Tidak ada enclosure/approach note kromatik pada motif LEAD (desain sengaja murni chord-tone), sehingga tidak ada target pendekatan untuk diverifikasi. |
| Chromatic vocabulary tidak menutupi motif inti — identitas ritmis/interval dari `melody-design` tetap terdengar | advanced-melody | N/A | Tidak ada chromatic vocabulary sama sekali pada motif LEAD, sehingga kriteria "tidak menutupi motif inti" tidak berlaku — motif inti tak pernah dihadapkan risiko tertutup kromatisme. |
| Outside line punya jalur kembali (return path) yang jelas ke harmoni yang berlaku | advanced-melody | N/A | Tidak ada outside line pada motif LEAD — satu-satunya outside pitch di desain ini eksplisit disebut ada di kandidat yang kalah (Kandidat 3) dan sengaja tidak dipakai — sehingga tidak ada return path untuk dinilai. |
| Tingkat kerumitan chromatic vocabulary proporsional dengan level kompleksitas yang dinyatakan di brief | advanced-melody | N/A | Tidak ada chromatic vocabulary yang bisa dinilai proporsionalitasnya karena kompleksitasnya sengaja dibuat nol, pilihan yang dikaitkan eksplisit ke karakter "restrained, bukan agresif" sejak Level 1, bukan kelalaian. |

## Level 5 — Desain Ritme dan Groove

### L1 (mekanis)

- [x] Feel dan rhythmic identity ditentukan eksplisit

### L2 (rubrik)

| Kriteria | Skor (0-2) | Alasan (1 kalimat) |
|---|---|---|
| Meter, grouping, beat unit, dan subdivisi dinyatakan eksplisit; bass/drum/comping/melodi sepakat pada satu kerangka groove | 1 | Tempo 74 BPM dan subdivisi (straight-eighth/sixteenth) disebut, dan placement aksen menyamakan kerangka antar kick/snare/bass/comping/lead/hi-hat, tapi meter (mis. 4/4) sendiri tidak dinyatakan eksplisit di file ini. |
| Swing/feel tidak diperlakukan sebagai satu rasio kaku untuk semua tempo dan layer | 1 | Swing dinyatakan sebagai satu nilai tunggal (0.56) yang berlaku sepanjang lagu untuk semua layer, tanpa variasi per section atau instrumen. |
| Offset timing (microtiming) relasional, terbatas, dan diturunkan dari PPQ/tempo yang dinyatakan — bukan humanization acak sebagai pengganti desain groove | 2 | Offset tick per instrumen (kick, snare, rimshot, bass, comping, lead, hi-hat) diberikan sebagai rentang relasional terhadap grid, eksplisit disalin dari profil groove referensi, bukan humanization acak. |
| Velocity, onset timing, note length, dan artikulasi mendukung satu pocket yang konsisten | 1 | Onset timing dibahas rinci per instrumen dan velocity hi-hat ghost disebut eksplisit (<45), tapi note length dan artikulasi sama sekali tidak dibahas di file ini. |
| Kontur bass mendukung form dan groove; third/seventh/degree karakteristik membentuk garis yang koheren | 1 | Kontur bass disinggung ringkas (root+5th+approach note dengan rest) selaras karakter spacious section 1, tapi detailnya sengaja didelegasikan ke 08-bassline.md. |
| Attack order, gate, note-off, dan reattack bass dispesifikasikan ketika groove bergantung padanya | 0 | Tidak ada pembahasan gate, note-off, atau reattack bass di file ini — hanya offset onset yang dibahas. |

## Level 6 — Aransemen Instrumen

### L1 (mekanis)

- [x] Orchestration map mencakup semua 6 bagian dari Level 2

### L2 (rubrik)

| Kriteria | Skor (0-2) | Alasan (1 kalimat) |
|---|---|---|
| Setiap section punya bar count/durasi eksplisit dan fungsi dramaturgis yang jelas ke pendengar | 2 | Setiap section diberi rentang bar dan penjelasan fungsi peran instrumen yang eksplisit, sejalan dengan 02-form.md. |
| Identitas (motif/groove) tetap dikenali setelah transformasi; repetisi loop punya alasan (bukan diulang literal 3x tanpa tujuan) | 1 | Kontinuitas kontur bass dan prinsip graft (Rhodes ke sustain pad, drum ke ghost hi-hat) disebut untuk menjaga jejak saat menipis, tapi identitas motif secara melodis tidak dibahas di level orkestrasi ini. |
| Setiap batas antar-section punya transisi yang disengaja (cut langsung atau transisi terancang), bukan default fill/riser generik di semua tempat | 1 | Entri instrumen bertahap per section (bass->Rhodes->drum->lead) tersirat sebagai transisi terencana, tapi tidak dibahas eksplisit sebagai "titik transisi" (itu ranah 11-transitions.md). |
| Setiap instrumen/track punya peran utama yang berarti per section; akomodasi memberi ruang dan menghindari konflik register | 2 | Setiap instrumen (bass, Rhodes, drum, lead) punya peran eksplisit dan berbeda di tiap section, dengan prinsip "tidak ada dua instrumen mendominasi bersamaan tanpa alasan section-nya" menghindari tabrakan peran. |
| Solo/improvisasi punya landmark form, target/guide tone yang jelas, dan jalur kembali (return path) jika memakai materi outside | N/A | File ini tidak menyinggung solo sama sekali, konsisten dengan ketiadaan solo section yang dijustifikasi di 02-form.md/10-solo-map.md, bukan kontradiksi. |
| Klimaks disiapkan (bukan tiba-tiba) dan punya konsekuensi; setidaknya satu elemen "subtraction" hadir jika bukan konsep akumulasi kontinu | 2 | Persiapan klimaks eksplisit (drum full tepat bar 15 sebagai "dorongan" sebelum leap) dan subtraction eksplisit di section 5 (Rhodes ke sustain, drum ke ghost hi-hat, keduanya berlabel graft). |

## Level 7 — Desain Comping dan Voicing

### L1 (mekanis)

- [x] Comping chart mencakup semua bagian yang butuh comping (bar 5-23)

### L2 (rubrik)

| Kriteria | Skor (0-2) | Alasan (1 kalimat) |
|---|---|---|
| Setiap section punya bar count/durasi eksplisit dan fungsi dramaturgis yang jelas ke pendengar | 2 | Comping chart per section mencantumkan rentang bar dan fungsi ringkas (mis. "kehadiran pertama, tidak mendominasi") untuk section 2-6. |
| Identitas (motif/groove) tetap dikenali setelah transformasi; repetisi loop punya alasan (bukan diulang literal 3x tanpa tujuan) | 2 | Top-note E diklaim dan diverifikasi via notation_facts.py sebagai common-tone anchor berulang di mayoritas bar, dengan penyimpangan warna (F, B, A, D, F#) dijustifikasi per bar, bukan acak. |
| Setiap batas antar-section punya transisi yang disengaja (cut langsung atau transisi terancang), bukan default fill/riser generik di semua tempat | 1 | Ada catatan peningkatan aktivitas comping di section 4 ("momentum menumpuk lewat warna"), tapi titik transisi antar-section tidak dibahas eksplisit sebagai device transisi. |
| Setiap instrumen/track punya peran utama yang berarti per section; akomodasi memberi ruang dan menghindari konflik register | 2 | Voicing rootless/shell dipilih eksplisit karena "bass membawa root", sebuah keputusan register yang langsung menghindari tabrakan Rhodes-bass. |
| Solo/improvisasi punya landmark form, target/guide tone yang jelas, dan jalur kembali (return path) jika memakai materi outside | N/A | Tidak dibahas di file ini, konsisten dengan ketiadaan solo section yang dijustifikasi di level lain, tanpa kontradiksi. |
| Klimaks disiapkan (bukan tiba-tiba) dan punya konsekuensi; setidaknya satu elemen "subtraction" hadir jika bukan konsep akumulasi kontinu | 2 | Voicing terkaya dengan #11 ditonjolkan di section 4 mempersiapkan klimaks brightening, dan section 5 eksplisit menipis ke voicing 3-nada berlabel graft sebagai subtraction. |

## Level 8 — Desain Bass Line

### L1 (mekanis)

- [x] Bass concept ditentukan untuk setiap section (6/6)

### L2 (rubrik)

| Kriteria | Skor (0-2) | Alasan (1 kalimat) |
|---|---|---|
| Meter, grouping, beat unit, dan subdivisi dinyatakan eksplisit; bass/drum/comping/melodi sepakat pada satu kerangka groove | 1 | Panjang not per bar (mis. D2A2z4 = 8 unit) konsisten sepanjang 24 bar dan selaras tempo/groove 05-groove.md, tapi meter/subdivisi tidak dinyatakan eksplisit sebagai teks di file ini, hanya implisit lewat notasi durasi. |
| Swing/feel tidak diperlakukan sebagai satu rasio kaku untuk semua tempo dan layer | 0 | Swing/feel sama sekali tidak dibahas di file ini (didelegasikan penuh ke 05-groove.md). |
| Offset timing (microtiming) relasional, terbatas, dan diturunkan dari PPQ/tempo yang dinyatakan — bukan humanization acak sebagai pengganti desain groove | 0 | Tidak ada offset microtiming yang dibahas di file ini — hanya referensi ke timing map 05-groove.md tanpa detail relasional sendiri. |
| Velocity, onset timing, note length, dan artikulasi mendukung satu pocket yang konsisten | 1 | Note length dieksplorasi rinci lewat kontras not ditahan vs walking (mis. bar 14 D8 vs bar 15 walking penuh), tapi velocity, onset-timing, dan artikulasi sama sekali tidak disebut di file ini. |
| Kontur bass mendukung form dan groove; third/seventh/degree karakteristik membentuk garis yang koheren | 2 | Kontur eksplisit per section (root + 3rd/5th/7th/9th, approach note, contrary motion ke bVII di bar 12 & 17 sebagai motif bass yang bisa dikenali) koheren dan konsisten dengan form/harmoni. |
| Attack order, gate, note-off, dan reattack bass dispesifikasikan ketika groove bergantung padanya | 2 | Gate/note-off/reattack bass dispesifikasikan jelas per bar (mis. D8 ditahan penuh vs mini-walk 4 not tanpa rest di bar 12), konsisten mendukung arc tension/release lagu. |

## Level 9 — Desain Drum

### L1 (mekanis)

- [x] Bar count drum grid (24 bar) sama persis dengan ABC section demi
      section — diverifikasi lewat total durasi `output.mid` (77.84s =
      24 bar x 60/74x4, lihat `14-review.md`)

### L2 (rubrik)

| Kriteria | Skor (0-2) | Alasan (1 kalimat) |
|---|---|---|
| Meter, grouping, beat unit, dan subdivisi dinyatakan eksplisit; bass/drum/comping/melodi sepakat pada satu kerangka groove | 2 | `tempo_bpm`, `beats_per_bar`, dan `steps_per_bar` dinyatakan eksplisit dan numerik, konsisten dengan tempo 74 BPM & subdivisi sixteenth di 05-groove.md serta struktur bar di 08-bassline.md. |
| Swing/feel tidak diperlakukan sebagai satu rasio kaku untuk semua tempo dan layer | 1 | Swing dinyatakan sebagai satu field global (0.56) yang berlaku untuk seluruh section dan instrumen tanpa variasi per layer. |
| Offset timing (microtiming) relasional, terbatas, dan diturunkan dari PPQ/tempo yang dinyatakan — bukan humanization acak sebagai pengganti desain groove | 2 | `timing` map per instrumen (kick 0, snare 15, rimshot 25, chh/ride -3) eksplisit, bounded, dan konsisten dengan nilai yang disalin dari 05-groove.md, bukan random. |
| Velocity, onset timing, note length, dan artikulasi mendukung satu pocket yang konsisten | 2 | `base_velocity` per instrumen, `phrase_velocity` per bar (arc naik-turun mengikuti label section), dan tingkat ghost/normal/accent (g/x/X) semuanya konsisten mendukung satu pocket yang berkembang sesuai narasi lagu, termasuk TACET section 1-2 yang eksplisit dijustifikasi "by design". |
| Kontur bass mendukung form dan groove; third/seventh/degree karakteristik membentuk garis yang koheren | N/A | File ini adalah step-grid drum murni (gm_map hanya kick/snare/rimshot/chh/ride); kontur bass secara struktural tidak relevan di sini, dibahas di 08-bassline.md. |
| Attack order, gate, note-off, dan reattack bass dispesifikasikan ketika groove bergantung padanya | N/A | Kriteria ini spesifik untuk bass; file drum step-grid ini tidak memuat data bass sama sekali by design (lihat title "drum step-grid"). |

## Level 10 — Desain Improvisasi

### L1 (mekanis)

- [x] Solo map: **N/A disengaja** — tidak ada solo section (dijustifikasi
      di `10-solo-map.md`, bukan terlewat)

### L2 (rubrik)

| Kriteria | Skor (0-2) | Alasan (1 kalimat) |
|---|---|---|
| Setiap section punya bar count/durasi eksplisit dan fungsi dramaturgis yang jelas ke pendengar | 1 | Total 24 bar dan arc "sendiri->menumpuk->tiba" disebut, tapi tidak ada tabel per-section bar/fungsi tersendiri di file ini (hanya mengacu ke 02-form.md). |
| Identitas (motif/groove) tetap dikenali setelah transformasi; repetisi loop punya alasan (bukan diulang literal 3x tanpa tujuan) | 2 | Tahapan transformasi motif lead (Statement->Answer->Fragment->Absence->Expansion) disebut eksplisit sebagai pengganti fungsi solo, langsung menjawab identitas-lewat-transformasi. |
| Setiap batas antar-section punya transisi yang disengaja (cut langsung atau transisi terancang), bukan default fill/riser generik di semua tempat | 0 | Tidak ada pembahasan titik transisi antar-section di file ini sama sekali. |
| Setiap instrumen/track punya peran utama yang berarti per section; akomodasi memberi ruang dan menghindari konflik register | 0 | File berfokus pada lead/motif sebagai pengganti solo; peran instrumen lain dan pertimbangan register tidak dibahas di sini. |
| Solo/improvisasi punya landmark form, target/guide tone yang jelas, dan jalur kembali (return path) jika memakai materi outside | N/A | Absennya solo section dijustifikasi paling lengkap di file ini sendiri: batasan panjang 24 bar, fungsi eksplorasi sudah dibawa device lain, dan solo akan bertentangan dengan arc brief — bukan kelalaian. |
| Klimaks disiapkan (bukan tiba-tiba) dan punya konsekuensi; setidaknya satu elemen "subtraction" hadir jika bukan konsep akumulasi kontinu | 1 | Leap bar 15-16 dan penipisan section 5-6 disebut sebagai pengganti fungsi solo, tapi hanya sebagai argumen pendukung, bukan pembahasan mandiri soal persiapan klimaks. |

## Level 11 — Interlude, Shout Chorus, dan Transisi

### L1 (mekanis)

- [x] Bagian transisi tertulis eksplisit (4 titik, lihat `11-transitions.md`)

### L2 (rubrik)

| Kriteria | Skor (0-2) | Alasan (1 kalimat) |
|---|---|---|
| Setiap section punya bar count/durasi eksplisit dan fungsi dramaturgis yang jelas ke pendengar | 1 | Empat titik transisi disertai nomor bar eksplisit dan fungsi masing-masing, tapi tidak ada tabel bar/panjang untuk keenam section secara utuh di file ini. |
| Identitas (motif/groove) tetap dikenali setelah transformasi; repetisi loop punya alasan (bukan diulang literal 3x tanpa tujuan) | 0 | Tidak ada pembahasan eksplisit soal identitas motif/groove yang dipertahankan di file ini. |
| Setiap batas antar-section punya transisi yang disengaja (cut langsung atau transisi terancang), bukan default fill/riser generik di semua tempat | 2 | Keempat transisi (12->13, 14->15, 18->19, 21->22) dijelaskan detail dan masing-masing eksplisit menyangkal jadi fill/riser generik ("bukan cut tiba-tiba", "bukan fill konvensional", dst). |
| Setiap instrumen/track punya peran utama yang berarti per section; akomodasi memberi ruang dan menghindari konflik register | 1 | Instrumen spesifik disebut di tiap titik transisi (drum fill, bass mini-walk, kick dihilangkan), tapi bukan pemetaan peran per-section yang komprehensif. |
| Solo/improvisasi punya landmark form, target/guide tone yang jelas, dan jalur kembali (return path) jika memakai materi outside | N/A | Konsisten dengan ketiadaan solo (dan shout chorus/interlude) yang dijustifikasi di 02-form.md/10-solo-map.md; file ini tidak berkontradiksi. |
| Klimaks disiapkan (bukan tiba-tiba) dan punya konsekuensi; setidaknya satu elemen "subtraction" hadir jika bukan konsep akumulasi kontinu | 2 | Transisi bar 18->19 eksplisit berupa "ONE-OFF imperfection" (kick dihilangkan) berlabel subtraction disengaja, dan absennya shout chorus dijustifikasi karena section 4 sudah membawa fungsi klimaks dalam skala kecil. |

## Level 12 — Intro dan Ending

### L1 (mekanis)

- [x] Intro dan ending punya identitas materi sendiri (bukan placeholder)

### L2 (rubrik)

| Kriteria | Skor (0-2) | Alasan (1 kalimat) |
|---|---|---|
| Setiap section punya bar count/durasi eksplisit dan fungsi dramaturgis yang jelas ke pendengar | 2 | Intro (bar 1-4) dan ending (bar 22-24) masing-masing diberi rentang bar eksplisit dan fungsi dramaturgis yang jelas (thesis telanjang vs konvergensi motif). |
| Identitas (motif/groove) tetap dikenali setelah transformasi; repetisi loop punya alasan (bukan diulang literal 3x tanpa tujuan) | 2 | Ending eksplisit mengutip ulang motif leap major 6th lead oleh bass di oktaf rendah, dikonfirmasi lintas file (08-bassline.md) sebagai realisasi konkret, bukan materi baru. |
| Setiap batas antar-section punya transisi yang disengaja (cut langsung atau transisi terancang), bukan default fill/riser generik di semua tempat | 1 | Ada penyebutan konsep makro instrumen "menyatu" sebagai realisasi arrival, tapi mekanisme transisi konkret antar-bar didelegasikan ke 11-transitions.md. |
| Setiap instrumen/track punya peran utama yang berarti per section; akomodasi memberi ruang dan menghindari konflik register | 2 | Konvergensi bass+lead dilakukan di oktaf rendah secara sengaja agar unison tidak bertabrakan pitch, sebuah keputusan register eksplisit. |
| Solo/improvisasi punya landmark form, target/guide tone yang jelas, dan jalur kembali (return path) jika memakai materi outside | N/A | Tidak disinggung, konsisten dengan ketiadaan solo yang dijustifikasi di level lain. |
| Klimaks disiapkan (bukan tiba-tiba) dan punya konsekuensi; setidaknya satu elemen "subtraction" hadir jika bukan konsep akumulasi kontinu | 1 | Ending disebut sebagai gema/resolusi dari klimaks section 4 dengan mereda ke diam, tapi persiapan klimaks itu sendiri di luar scope file ini (section 4 dibahas di level lain). |

## Level 13 — Dinamika dan Dramaturgi

### L1 (mekanis)

- [x] Energy curve tercantum per section dengan angka/persentase

### L2 (rubrik)

| Kriteria | Skor (0-2) | Alasan (1 kalimat) |
|---|---|---|
| Setiap section punya bar count/durasi eksplisit dan fungsi dramaturgis yang jelas ke pendengar | 2 | Tabel energy curve mencantumkan section, bar, dan persentase energi eksplisit untuk seluruh 6 section termasuk pemecahan internal section 4. |
| Identitas (motif/groove) tetap dikenali setelah transformasi; repetisi loop punya alasan (bukan diulang literal 3x tanpa tujuan) | 1 | Stabilitas register bass sepanjang lagu disebut sebagai bentuk identitas, tapi identitas motif melodis secara spesifik tidak dibahas di file ini. |
| Setiap batas antar-section punya transisi yang disengaja (cut langsung atau transisi terancang), bukan default fill/riser generik di semua tempat | 1 | Bar 14 disebut sebagai "napas terakhir"/silence-as-tension yang tumpang tindih dengan device transisi Level 11, tapi tidak dibahas sistematis untuk semua batas section. |
| Setiap instrumen/track punya peran utama yang berarti per section; akomodasi memberi ruang dan menghindari konflik register | 2 | Bullet "Register" eksplisit memetakan trayektori register tiap instrumen (bass rendah stabil, Rhodes naik-turun, lead menengah-tinggi menurun) yang saling terpisah menghindari tabrakan. |
| Solo/improvisasi punya landmark form, target/guide tone yang jelas, dan jalur kembali (return path) jika memakai materi outside | N/A | Kurva energi tidak menampilkan solo section, konsisten dengan ketiadaan yang dijustifikasi di level lain. |
| Klimaks disiapkan (bukan tiba-tiba) dan punya konsekuensi; setidaknya satu elemen "subtraction" hadir jika bukan konsep akumulasi kontinu | 2 | Kurva menunjukkan build bertahap ke satu puncak 90% (bar 15-16) tanpa puncak kedua, dan subtraction terukur lewat penurunan 45%->30%->15% di section 5-6. |

## Level 14 — Detail Low Level

### L1 (mekanis)

- [x] `validate_abc.py` lulus tanpa error (0 errors, 0 warnings)
- [x] `output.mid`: 4 track, notes-per-track > 0 semua voice (13/67/51/126),
      tempo 74 BPM & TS 4/4 cocok header ABC — diperiksa langsung dari
      MIDI (lihat `14-review.md`), bukan hanya status exit validator

### L2 (rubrik)

Diisi oleh subagent reviewer segar tanpa konteks generasi (self-grading
dilarang). Level 14 ditopang dua modul sekaligus (`abc-notation` +
`midi-orchestration`), jadi tabel berikut menggabungkan kriteria penuh
dari kedua rubrik referensinya.

| Kriteria | Sumber | Skor (0-2) | Alasan (1 kalimat) |
|---|---|---|---|
| Header wajib ada dan bisa di-parse (`validate_abc.py` lulus tanpa error) | abc-notation | 2 | `validate_abc.py song.abc` dilaporkan "OK, 0 errors, 0 warnings" di `14-review.md`. |
| Ejaan not cocok dengan key dan fungsi harmonik selama masih praktis | abc-notation | 1 | Ejaan chord-tone per not sudah tepat (mis. `^F`=3rd pada `D9`, `_B`=b3 pada `Gm7`), tapi bar 15-24 memakai F# eksplisit berulang kali di bawah satu header global `K:C` tanpa inline key change, yang oleh review sendiri diakui membuat analisis chord-vs-key mekanis salah baca sebagai "borrowed". |
| Bar duration, pickup, tuplet, rest, tie, overlay, dan repeat/ending tervalidasi konsisten | abc-notation | 2 | Pengecekan manual ke-24 bar di ketiga voice menunjukkan setiap bar menjumlah tepat 8 unit eighth-note (`L:1/8`, `M:4/4`) dan tidak ada pickup/tuplet/tie/overlay/repeat yang dipakai sama sekali, konsisten dengan `validate_abc.py` 0 error. |
| Setiap voice tetap konsisten secara metrik (tidak ada voice yang kehilangan bar) | abc-notation | 2 | Ketiga voice (Lead Trumpet, Rhodes, Bass) sama-sama punya 6 baris x 4 bar = 24 bar; tidak ada voice yang bar-nya lebih pendek/panjang dari yang lain. |
| Arah swing/produksi tidak salah dikodekan sebagai note value yang keliru | abc-notation | 2 | Tidak ada usaha mengkodekan swing lewat note value di `song.abc` (semua durasi straight eighth/quarter/whole); swing/groove didesain terpisah di layer `drums.json` step-grid sehingga tidak ada risiko note value ABC bertentangan dengan feel produksi. |
| Keterbatasan renderer (jika ada) diungkap eksplisit, bukan disembunyikan | abc-notation | 2 | `14-review.md` menjelaskan eksplisit keterbatasan `notation_facts.py` (hanya membaca key signature pertama, inline `[K:...]` tak terbaca) dan menunjuk ke file segmented terpisah sebagai verifikasi silang, bukan menyembunyikan diskrepansi. |
| Komposisi kering (tanpa noise/filter/degradasi) sudah berfungsi sebelum efek produksi ditambahkan | midi-orchestration | 2 | Inspeksi `output.mid` di `14-review.md` murni data not MIDI (track count, notes-per-track, max-poly, durasi) tanpa satu pun efek produksi/degradasi disebutkan, menunjukkan komposisi kering sudah berfungsi sebelum mastering. |
| Setiap track/role punya identitas yang jelas dan berbeda; automation punya tujuan musikal | midi-orchestration | 2 | Keempat track punya karakter jelas berbeda (Lead mono `max-poly=1`, Rhodes blok akor `max-poly=4`, Bass mono `max-poly=1`, Drums `max-poly=2`), dan keluarnya Rhodes di bar 24 serta drum di bar 23-24 eksplisit dikaitkan ke desain "reda" penutup, bukan efek acak. |
| Event data eksak (pitch, velocity, offset, gate) tersedia untuk motif kritis, bass, voicing, dan groove class — nilai berada dalam rentang valid | midi-orchestration | 1 | Offset/gate/pitch (durasi not, end-time, chord tone) diverifikasi langsung dari MIDI dan ABC, tapi velocity sama sekali tidak dilaporkan/diverifikasi untuk track manapun di `14-review.md`. |
| Pitch name dan nilai MIDI konsisten satu sama lain di seluruh track | midi-orchestration | 1 | Konsistensi ejaan-vs-MIDI diverifikasi via music21 pada gate Level 3/7 (file segmented terpisah), tapi `14-review.md` sendiri tidak mengulang cross-check pitch-name-vs-nilai-MIDI pada `song.abc`/`output.mid` final, hanya mewarisi hasil gate sebelumnya. |
| Perubahan state produksi (layer masuk/keluar) memperkuat form, bukan menutupi section yang belum siap | midi-orchestration | 2 | Rhodes berhenti tepat bar 24 dan drum berhenti tepat bar 23-24 sesuai desain arrangement/drum grid yang sudah ditentukan sebelumnya, memperkuat wind-down ending, bukan menyembunyikan section yang belum matang. |
| `output.mid`: jumlah track, notes-per-track > 0 untuk semua voice, dan tag tempo/meter cocok — diverifikasi langsung dari file MIDI, bukan hanya exit status validator | midi-orchestration | 2 | `14-review.md` melaporkan 4 track, notes-per-track > 0 di semua voice (13/67/51/126), tempo 74 BPM dan TS 4/4 cocok header ABC — semua diverifikasi langsung dari MIDI. |

## L3 (telinga) — hanya diisi sekali, di akhir

Diisi **setelah** `output.mid` ada, mengikuti `human-ear-protocol.md`.
Skor L2 yang tinggi adalah lantai (tidak ada yang rusak/tipis), bukan
langit-langit (belum tentu enak didengar) — L3 adalah pemeriksaan wajib
terakhir sebelum piece dianggap selesai.

**SENGAJA KOSONG** — menunggu manusia. `output.mid` sudah tersedia di
run folder ini; belum ada sesi mendengarkan blind A/B oleh manusia sesuai
`../../skills/jazz-composition/references/human-ear-protocol.md`. Jangan
diisi oleh agent manapun.

# Scorecard — After Rain, Still Warm

## Validasi mesin lintas-level

- [x] Form adalah Intro 2 + A 4 + B 4 + C 4 + Outro 2 = 16 bar.
- [x] `drums.json` mendeklarasikan section bar 2+4+4+4+2 = 16.
- [x] `validate_abc.py`: `OK: 0 errors, 0 warning(s)`.
- [x] `music21` memuat 3 part; MIDI memiliki 4 track dengan note > 0 untuk tiap track.
- [x] Tempo 74.000074 BPM dan meter 4/4 tertanam pada MIDI.

## L1

| Level | Gate | Status |
|---:|---|---|
| 1 | Field brief wajib terisi; asumsi tercatat eksplisit | pass |
| 2 | Form dan panjang section eksplisit | pass |
| 3 | Tonal center, fungsi chord, tension per bar | pass |
| 4 | Motif, contour, target tone, resolution | pass |
| 5 | Feel dan rhythmic identity spesifik | pass |
| 6–9 | Role map/comping/bass/drum mencakup semua section | pass |
| 10 | N/A dijustifikasi | pass |
| 11–13 | Transisi, intro/outro, energy curve eksplisit | pass |
| 14 | ABC/MIDI audit | pass |

## L2 (rubrik reviewer segar)

### Level 1 — Konsep Artistik

| Kriteria | Skor (0–2) | Alasan (1 kalimat) |
|---|---:|---|
| Identitas artistik jelas | 2 | Gaya neo-soul/chill-jazz, tonalitas, tempo, instrumen, dan citra suasana dinyatakan dengan spesifik. |
| Karakter/emosi konsisten dengan instrumentasi | 2 | Rhodes, alto sax, bass elektrik, dan drum tipis selaras dengan karakter hangat serta laid-back yang ditetapkan. |
| Arah energi masuk akal untuk gaya yang dipilih | 2 | Arc hening menuju lift terkendali lalu landing diterjemahkan konsisten ke tiap section. |

### Level 2 — Arsitektur Lagu

| Kriteria | Skor (0–2) | Alasan (1 kalimat) |
|---|---:|---|
| Setiap bagian punya fungsi dramaturgis | 2 | Intro, A, B, C, dan Outro masing-masing memiliki fungsi dengar yang jelas dari pengenalan sampai resolusi. |
| Ada kontras antar-bagian | 2 | Masuknya groove, kenaikan register, penebalan tekstur, dan subtraksi outro memberi kontras yang terdengar. |
| Klimaks ditempatkan pada bagian yang tepat | 2 | C ditempatkan sebagai peak terbatas setelah B dan segera diikuti pelepasan menuju outro. |

### Level 3 — Peta Harmoni

| Kriteria | Skor (0–2) | Alasan (1 kalimat) |
|---|---:|---|
| Tension map jelas per bar | 2 | Setiap bar memiliki tingkat tensi eksplisit yang membentuk kenaikan menuju bar 14 dan pelepasan akhir. |
| Fungsi harmonik tiap chord teridentifikasi | 2 | Fungsi tonic, iv, bVI/bIII/bVII, dan dominant minor dijelaskan untuk seluruh progresi. |
| Chord kompleks memang diperlukan, bukan dekorasi | 2 | A7alt dipusatkan pada titik pengarah return sehingga warna alterasinya mempunyai fungsi formal yang nyata. |

### Level 4 — Desain Melodi

| Kriteria | Skor (0–2) | Alasan (1 kalimat) |
|---|---:|---|
| Motif mudah dikenali dan dipertahankan | 2 | Kontur naik minor-third lalu turun langkah tetap menjadi dasar frasa sax dari A sampai outro. |
| Target tone/guide tone terhubung logis | 1 | Target per section disebutkan, tetapi beberapa label derajat nada dan realisasi notasinya tidak sepenuhnya bersesuaian. |
| Outside material terkontrol dan diresolusikan | 1 | C# hanya muncul pada bar dominant, namun resolusi yang diklaim ke D tidak terjadi langsung pada semua kemunculannya. |

### Level 5 — Desain Ritme dan Groove

| Kriteria | Skor (0–2) | Alasan (1 kalimat) |
|---|---:|---|
| Placement aksen konsisten dengan feel yang dipilih | 1 | Backbeat dan pola hi-hat mendukung pocket 16th, tetapi detail placement antar-layer masih terutama berupa deskripsi umum. |
| Groove reference cukup spesifik untuk diturunkan ke comping/bass/drum | 2 | Tempo, subdivisi, profile pocket, peran tiap layer, serta grid drum 16 langkah memberikan arahan implementasi yang cukup jelas. |

### Level 6 — Aransemen Instrumen

| Kriteria | Skor (0–2) | Alasan (1 kalimat) |
|---|---:|---|
| Setiap instrumen punya peran per bagian | 2 | Role map menetapkan sax sebagai foreground, Rhodes sebagai support, bass sebagai fondasi, dan drum sebagai pembawa groove pada semua section. |
| Density berubah antar-bagian | 2 | Artefak bergerak dari Rhodes solo ke ensemble penuh terbatas lalu mengurangi layer pada outro. |

### Level 7 — Desain Comping dan Voicing

| Kriteria | Skor (0–2) | Alasan (1 kalimat) |
|---|---:|---|
| Voice leading antar-chord halus | 1 | Intent common-tone dan top-line dicatat, tetapi voicing aktual satu serangan per bar menunjukkan perpindahan yang masih cukup blok. |
| Comping bergerak (bukan block chord statis) | 1 | Perubahan voicing mengikuti harmoni, namun ritme comping yang seluruhnya berupa sustain satu chord per bar membatasi gerak internalnya. |

### Level 8 — Desain Bass Line

| Kriteria | Skor (0–2) | Alasan (1 kalimat) |
|---|---:|---|
| Bass punya kontur (bukan selalu root) | 2 | Notasi bass memakai fifth, seventh, dan approach selain root sambil menaikkan aktivitas pada B/C. |
| Approach note ke chord berikutnya masuk akal | 1 | C# menuju D bekerja pada return ke Dm, tetapi penggunaan C# sebelum perpindahan A7alt ke F tidak memberi resolusi target yang sama. |

### Level 9 — Desain Drum

| Kriteria | Skor (0–2) | Alasan (1 kalimat) |
|---|---:|---|
| Dinamika drum mengikuti struktur lagu | 2 | Drum diam di intro, meningkat dari A ke C dengan ride, lalu menyusut menjadi hit/rimshot pada outro. |
| Fills/setup ditempatkan pada transisi yang logis | 1 | Perubahan pola mendukung batas section, tetapi tidak ada setup drum yang terdefinisi khusus untuk mayoritas transisi. |

### Level 10 — Desain Improvisasi

| Kriteria | Skor | Alasan (1 kalimat) |
|---|---:|---|
| Solo section punya arah perkembangan | N/A | Artefak secara eksplisit menetapkan vignette 16 bar tanpa section solo agar arc singkatnya tetap utuh. |
| Background figure mendukung, bukan mengganggu | N/A | Tidak ada solo maupun background figure karena desainnya bukan vehicle improvisasi. |

### Level 11 — Interlude, Shout Chorus, dan Transisi

| Kriteria | Skor | Alasan (1 kalimat) |
|---|---:|---|
| Shout chorus terasa sebagai klimaks | N/A | Shout chorus sengaja tidak digunakan dan fungsi peak skala pendek sudah ditempatkan pada section C. |
| Transisi tidak terasa tiba-tiba/janggal | 2 | Setiap boundary memiliki device yang konkret, termasuk masuk groove, dominant resolution, dan subtraksi menuju outro. |

### Level 12 — Intro dan Ending

| Kriteria | Skor (0–2) | Alasan (1 kalimat) |
|---|---:|---|
| Intro memperkenalkan dunia lagu | 2 | Dua bar Rhodes Dm9 tanpa pulse langsung menetapkan pusat tonal dan ruang hangat lagu. |
| Ending berhubungan dengan motif utama | 2 | Fragmen motif menurun menuju sustain Dm6/9 mengikat ending pada materi utama dan memberi finalitas. |

### Level 13 — Dinamika dan Dramaturgi

| Kriteria | Skor (0–2) | Alasan (1 kalimat) |
|---|---:|---|
| Kurva energi masuk akal untuk arc lagu | 2 | Nilai energi 12%→35%→52%→68%→0% membentuk kenaikan dan pelepasan yang proporsional untuk 16 bar. |
| Parameter dinamika bervariasi | 2 | Perubahan density, register, activity, articulation, tension, dan silence melampaui sekadar perubahan volume. |

### Level 14 — Detail Low Level

| Kriteria | Skor (0–2) | Alasan (1 kalimat) |
|---|---:|---|
| Voice leading halus di level not | 1 | Common-tone intent dan beberapa perpindahan tertulis jelas, tetapi sustain chordal per bar membuat keluwesan voice-leading terbatas. |
| Register seimbang antar-instrumen | 2 | Sax berada di mid-upper, Rhodes di tengah, dan bass di register rendah tanpa tumpang tindih register yang mencolok. |
| Voicing tidak terlalu padat | 2 | Rhodes memakai empat nada per voicing dengan tekstur satu serangan per bar sehingga ruang untuk lead tetap tersedia. |
| Ending terasa selesai | 2 | Resolusi ke Dm6/9 dengan tonic sustain, penghentian drum, dan landing bass memberi penutup yang tegas namun tenang. |

## L3 (telinga manusia)

Belum diisi. Tidak ada klaim bahwa hasilnya enak sebelum evaluasi manusia.

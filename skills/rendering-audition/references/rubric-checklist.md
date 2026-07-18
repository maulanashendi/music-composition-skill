# Rubrik kualitas konsolidasi — rendering-audition

File ini menggantikan 8 `rubric.md` terpisah di modul lama (`abc-notation`,
`advanced-melody`, `arrangement`, `groove-rhythm`, `harmony`, `melody-design`,
`midi-orchestration`, `vibes-mood` — akan diarsipkan ke `archive/skills/`
setelah migrasi MDLC tuntas) — konsolidasi supaya audit pra-Release satu
tempat, bukan 8 file yang harus dibuka bergantian.

Diisi subagent reviewer segar tanpa konteks generasi — skor 0-2 + alasan 1
kalimat per kriteria (skala: 0 = tidak ada/kontradiktif, 1 = ada tapi
lemah/tidak konsisten, 2 = jelas dan konsisten sepanjang piece). Kriteria
yang menilai kehadiran suatu device (klimaks, fills/setup, dst) butuh
afforansi N/A: kalau device itu sengaja absen sesuai brief, isi skor N/A +
1 kalimat justifikasi — bukan skor 0.

Baris yang dulu ada di modul lama tapi sekarang **otomatis** dari
`pyengine validate` (fase Verify) — vibe conformance, target tones/downbeat
chord-tone — **dibuang** dari sini; itu sudah jadi warning otomatis di
`plan-verifying`, bukan kriteria manual lagi.

**Catatan cakupan:** `json-composition/references/rubric.md` **dikecualikan**
dari konsolidasi ini — jalur JSON lama (legacy, akan diarsipkan ke
`archive/skills/`), bukan modul yang disatukan ke file ini.

## Vibe/Brief

| Kriteria | Skor (0-2) | Alasan (1 kalimat) |
|---|---|---|
| Fakta user dan asumsi dipisahkan; mood/gaya/groove/instrumentasi tidak tercampur jadi satu blob | | |
| DNA tetap (fixed), parameter fleksibel, arrival terlindungi, dan shortcut terlarang dinyatakan eksplisit | | |
| Minimal dua konsep berbeda secara struktural dipertimbangkan (kecuali user sudah mengunci desain), dan kriteria pemilihannya eksplisit | | |
| Gaya memakai penanda lebih dari sekadar superfisial (mis. lofi bukan cuma vinyl noise + maj7, jazz-funk tidak disamakan dengan hip-hop) | | |
| Materi referensi diterjemahkan jadi atribut luas, bukan disalin; tidak ada sample berhak cipta/melodi dikenali/gaya artis hidup yang direproduksi | | |

## Harmoni

| Kriteria | Skor (0-2) | Alasan (1 kalimat) |
|---|---|---|
| Fungsi harmonik tiap chord jelas (tonic/predominant/dominant/dst), atau local center/proses nonfungsional teridentifikasi | | |
| Event non-diatonis (alterasi, pedal, planing, polychord) punya rasionale fungsional/modal/voice-leading/warna/formal | | |
| Ritme harmonik cocok dengan tempo dan groove; menghapus satu chord dekoratif tidak akan memperjelas progresi | | |
| Voicing eksak (pitch dan oktaf) disediakan ketika brief butuh voicing spesifik; nilai MIDI sesuai nama pitch di output DAW-first | | |
| Top line dan inner-line voicing bergerak dengan sengaja; tension teralter di-resolve, dilanjutkan, atau ditransformasi secara sengaja | | |
| Register dan alokasi tangan/instrumen playable; kepadatan register rendah terkontrol; voicing aktual cocok dengan label chord | | |

## Melodi

| Kriteria | Skor (0-2) | Alasan (1 kalimat) |
|---|---|---|
| Satu motif utama (plus maksimal satu motif kontras yang benar-benar perlu) mengorganisasi keseluruhan piece | | |
| Identitas ritmis dan interval tetap dikenali setelah transformasi | | |
| Panjang phrase, napas, silence, dan target note terasa jelas (bukan aliran nada tanpa jeda) | | |
| Nada panjang/berulang/aksen/akhir-frasa cocok dengan harmoni, atau sengaja menantangnya dengan alasan | | |
| Range dan tessitura sesuai instrumen lead | | |
| Klimaks tidak dilemahkan oleh titik tinggi yang sudah berulang sebelumnya; head tetap memorable setelah nada dekoratif dihapus | | |
| Kepadatan ritmis melodi proporsional dengan tempo brief (BPM disebut eksplisit; IOI tercepat dan rest ratio cocok dengan tabel BPM band `../../vibes-mood/references/reasoning-theory.md`) | | |
| Outside material/chromatic vocabulary hanya dipakai pada bar yang tension map memang menandai butuh tegangan tinggi, bukan ditaburkan merata | | |
| Setiap enclosure/approach note punya target diatonis yang jelas dan tercapai | | |
| Chromatic vocabulary tidak menutupi motif inti — identitas ritmis/interval tetap terdengar | | |
| Outside line punya jalur kembali (return path) yang jelas ke harmoni yang berlaku | | |
| Tingkat kerumitan chromatic vocabulary proporsional dengan level kompleksitas yang dinyatakan di brief | | |

## Groove/Ritme

| Kriteria | Skor (0-2) | Alasan (1 kalimat) |
|---|---|---|
| Meter, grouping, beat unit, dan subdivisi dinyatakan eksplisit; bass/drum/comping/melodi sepakat pada satu kerangka groove | | |
| Swing/feel tidak diperlakukan sebagai satu rasio kaku untuk semua tempo dan layer | | |
| Offset timing (microtiming) relasional, terbatas, dan diturunkan dari PPQ/tempo yang dinyatakan — bukan humanization acak sebagai pengganti desain groove | | |
| Velocity, onset timing, note length, dan artikulasi mendukung satu pocket yang konsisten | | |
| Kontur bass mendukung form dan groove; third/seventh/degree karakteristik membentuk garis yang koheren | | |
| Attack order, gate, note-off, dan reattack bass dispesifikasikan ketika groove bergantung padanya | | |

## Aransemen

| Kriteria | Skor (0-2) | Alasan (1 kalimat) |
|---|---|---|
| Setiap section punya bar count/durasi eksplisit dan fungsi dramaturgis yang jelas ke pendengar | | |
| Identitas (motif/groove) tetap dikenali setelah transformasi; repetisi loop punya alasan (bukan diulang literal 3x tanpa tujuan) | | |
| Setiap batas antar-section punya transisi yang disengaja (cut langsung atau transisi terancang), bukan default fill/riser generik di semua tempat | | |
| Setiap instrumen/track punya peran utama yang berarti per section; akomodasi memberi ruang dan menghindari konflik register | | |
| Solo/improvisasi punya landmark form, target/guide tone yang jelas, dan jalur kembali (return path) jika memakai materi outside | | |
| Klimaks disiapkan (bukan tiba-tiba) dan punya konsekuensi; setidaknya satu elemen "subtraction" hadir jika bukan konsep akumulasi kontinu | | |

## Produksi/DAW (MIDI-orchestration)

| Kriteria | Skor (0-2) | Alasan (1 kalimat) |
|---|---|---|
| Komposisi kering (tanpa noise/filter/degradasi) sudah berfungsi sebelum efek produksi ditambahkan | | |
| Setiap track/role punya identitas yang jelas dan berbeda; automation punya tujuan musikal | | |
| Event data eksak (pitch, velocity, offset, gate) tersedia untuk motif kritis, bass, voicing, dan groove class — nilai berada dalam rentang valid | | |
| Pitch name dan nilai MIDI konsisten satu sama lain di seluruh track | | |
| Perubahan state produksi (layer masuk/keluar) memperkuat form, bukan menutupi section yang belum siap | | |
| Voice leading halus di level not; register seimbang antar-instrumen; voicing tidak terlalu padat; ending terasa selesai | | |
| `<slug>.mid` hasil `pyengine audition`/`release`: jumlah track, notes-per-track > 0 untuk semua voice, dan tag tempo/meter cocok — diverifikasi langsung dari file MIDI, bukan hanya exit status `pyengine validate` | | |

## Notasi (jalur legacy ABC — `abc-notation`)

Relevan hanya kalau artefak di tangan adalah ABC (bukan `plan.json`, lihat
jalur legacy di `../SKILL.md`). Untuk jalur `plan.json`, kriteria berikut
sudah terjamin `pyengine validate`, tidak perlu diskor manual di sini.

| Kriteria | Skor (0-2) | Alasan (1 kalimat) |
|---|---|---|
| Header wajib ada dan bisa di-parse (`validate_abc.py` lulus tanpa error) | | |
| Ejaan not cocok dengan key dan fungsi harmonik selama masih praktis | | |
| Bar duration, pickup, tuplet, rest, tie, overlay, dan repeat/ending tervalidasi konsisten | | |
| Setiap voice tetap konsisten secara metrik (tidak ada voice yang kehilangan bar) | | |
| Arah swing/produksi tidak salah dikodekan sebagai note value yang keliru | | |
| Keterbatasan renderer (jika ada) diungkap eksplisit, bukan disembunyikan | | |

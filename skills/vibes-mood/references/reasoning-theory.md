# Reasoning theory — lapisan penalaran teori (dari `compose-song`)

Dirangkum dan diadaptasi dari skill Claude Code `compose-song` (konsolidasi
2026-07-13). Sumber aslinya punya 9 modul penalaran yang mengikat proses
komposisi *sebelum* nada ditulis; file ini merangkumnya untuk orchestrator
`jazz-composition` (workflow lama `jazz-idea-generator` kini bagian dari
`jazz-composition`/`vibes-mood`) tanpa mengubah workflow enam-langkah yang
sudah ada di `SKILL.md` — anggap
tujuh modul di bawah sebagai *perkakas tambahan* yang dipakai di dalam Step 2
(brief & mood), Step 3 (generate candidates), dan Step 5 (quality gate),
berdampingan dengan `ideation-theory.md` dan `style-cheatsheets.md`. Profil
genre konkret (neo-soul/chill-jazz) ada di file terpisah:
`references/neo-soul-genre.md`.

Bahasa Indonesia dipertahankan (mengikuti bahasa sumber `compose-song`);
file-file lain di paket ini (asal JCD) berbahasa Inggris — konsisten per
sumber, bukan campur dalam satu file.

## Modul 1 — Fungsi emosional: mood → parameter musikal

Dipakai di Step 2 (Lock the brief AND the emotional journey), sebagai
pelengkap konkret untuk kata sifat vibe. Setiap mood dipetakan ke **tujuh
dimensi baku** yang sama supaya lintas-mood tetap bisa dibandingkan: tempo,
dinamika, stabilitas & warna harmoni, aktivitas ritme, densitas tekstur,
register, karakter voice-leading.

| Mood | Tempo | Dinamika | Stabilitas & warna harmoni | Aktivitas ritme | Densitas tekstur | Register | Voice-leading |
|---|---|---|---|---|---|---|---|
| **Tenang** | Moderat (68-78 BPM) | Lembut (mp), swell minim | Stabil — diatonic, maj7/m7, cadence jarang | Minim sinkopasi, groove menetap | Jarang (1-2 layer aktif) | Menengah, hindari ekstrem | Halus — common tone, stepwise |
| **Tegang** | Tetap atau naik tipis | Crescendo/aksen tajam menjelang puncak | Disonan — chromaticism, dominant prolongation, altered dominant | Lebih aktif, sinkopasi/ghost meningkat | Bisa menebal menjelang klimaks | Naik menjelang puncak | Leap terarah, chromatic approach |
| **Fokus** | Moderat, stabil (72-82 BPM) | Rata, minim lonjakan | Motif konsisten, harmonic rhythm lambat | Berulang, predictable | Tidak padat (density ceiling ketat) | Tengah, konsisten | Motif berulang, minim variasi drastis |
| **Wistful** | Moderat-lambat (70-80 BPM) | Lembut, sedikit rubato-feel | Borrowed iv/modal interchange, maj7 bersentuhan minor | Lembut, sedikit di belakang beat | Sedang, ada ruang/rest | Menengah-tinggi utk melodi | Chromatic approach halus, turun bertahap |
| **Hangat** | Moderat (72-84 BPM) | mp-mf konsisten | Stabil, warna maj9/6-9, root movement smooth | Groove menetap, sedikit swing | Medium, layer saling melengkapi register | Tengah, hindari terlalu tinggi/tajam | Common tone dominan, extension lembut |
| **Nocturnal** | Lambat-moderat (66-76 BPM) | Soft, ruang besar antar frase | Minor/modal, m9/m11, pedal point | Jarang, banyak rest/silence | Sangat jarang, sparse | Rendah-menengah, sesekali tinggi utk kontras | Held tone lama, gerak minimal |
| **Hopeful** | Moderat naik tipis (78-86 BPM) | Membangun (build), swell menjelang return | Mayor terbuka, secondary dominant mengarah resolusi | Aktif progresif, energi naik bertahap | Menebal seiring progresi | Naik bertahap menuju puncak | Directional, stepwise menuju resolusi |
| **Introspektif** | Lambat (66-74 BPM) | Sangat lembut, dekat | Minor/modal ambigu, sus chord tak resolve penuh | Minimal, rubato | Sangat jarang, hampir solo instrumen | Rendah-menengah, intim | Inner voice halus, top note nyaris statis |

**Cara pakai:** pilih mood dominan dari brief (boleh kombinasi 2, declare 1
sebagai leading), salin baris itu jadi tujuh keputusan eksplisit — inilah
yang membatasi pilihan kandidat di Step 3, bukan sebaliknya. Mood di luar
tabel: isi ketujuh dimensi yang sama, jangan menambah dimensi baru tanpa
merefleksikannya balik ke semua baris lain. Kontras dalam satu lagu wajar
(mis. intro tenang → B tegang → outro hangat), tapi tiap section punya
mood-nya sendiri yang dideklarasikan penuh — jangan campur tujuh dimensi dari
dua mood berbeda dalam satu section yang sama.

## Tabel BPM band — tempo sebagai parameter hilir

Dipakai lintas-level oleh orchestrator `jazz-composition` (Level 4 melodi,
Level 5 groove, Level 8 bass, Level 9 drum — lihat ground rule tempo di
`../../jazz-composition/SKILL.md`): setiap keputusan materi ritmis dicek
terhadap band BPM brief, bukan diputuskan seolah tempo hanya dekorasi.
Prinsip arah: **makin cepat BPM, makin jarang subdivisi rapat dipakai dan
makin panjang frase dalam bar.**

| BPM band | Label | Subdivisi melodi wajar | Napas minimum | Harmonic rhythm wajar | Swing feel |
|---|---|---|---|---|---|
| < 72 | Ballad | 16th aman | ≥2 beat | 1 chord/bar; 2 chord/bar hanya aman ≤60 BPM (cek rumus durasi absolut) | ≈2:1 (66%) |
| 72-92 | Medium-slow | 16th selektif | ≥1.5 beat | 1 chord/bar; 2 chord/bar <2 detik di band ini — butuh justifikasi eksplisit | ≈60-66% |
| 92-120 | Medium | 8th dominan, 16th sebagai ornamen | ≥1 beat | 1 chord/bar default; 2 chord/bar mulai berisiko | ≈60-64% |
| > 120 | Up | 8th/quarter, 16th berisiko | ≥1 beat | 1 chord per 1-2 bar; hindari 2 chord/bar | mendekati even (≈55-57%) |

Keterangan:

- **Napas minimum** = panjang minimum jeda/rest sebelum frase melodi
  berikutnya, dalam beat; konversi ke detik via `60/BPM × jumlah beat`.
- Kolom **Harmonic rhythm wajar** dirinci sebagai rumus durasi absolut per
  chord di `../../harmony/SKILL.md` (Langkah 2, sub-bagian "Durasi absolut
  per chord") — angka di sini ringkasan arah, bukan pengganti rumusnya.
- Kolom **Swing feel** dirinci sebagai breakpoint operasional di
  `../../groove-rhythm/references/groove-meter.md` §3 — band tabel ini
  interpolasi kasarnya.

## Modul 2 — Deklarasi hierarki teori (gate)

Dipakai menjelang Step 3, sebelum kandidat pertama ditulis konkret. Satu
**teori utama** (biasanya tonal center/mode) + **teori pendukung** per
dimensi (harmoni, melodi, tekstur, groove) yang menjabarkan bagaimana teori
utama diwujudkan — bukan daftar device acak, tapi kosakata yang koheren.
Hierarki yang dideklarasikan lebih dulu **membatasi kosakata** yang boleh
dipakai tanpa justifikasi tambahan (lihat Modul 3).

Template:

```
## Deklarasi Hierarki Teori — <judul/brief singkat>

- Teori utama: <tonalitas/mode/tonal center + kenapa cocok dgn mood Modul 1>
- Pendukung harmoni: <vokabulari chord/progresi yang diizinkan>
- Pendukung melodi: <gerak/kontur/targeting yang diizinkan>
- Pendukung tekstur: <kepadatan/model comping/voicing yang diizinkan>
- Pendukung groove: <feel ritme/swing/time-feel yang diizinkan>
- Device di luar hierarki (isi belakangan bila muncul) + justifikasi:
  <device> → <mengapa, lihat Modul 3>
```

Aturan pengikat: mood (Modul 1) mendahului hierarki — pilihan tonal
center/harmoni harus konsisten dengan tujuh dimensi mood; keputusan level
besar (bentuk lagu/tonal center, lihat Modul 5) mengikat level di bawahnya;
satu deklarasi per lagu, variasi per section dicatat sebagai bagian hierarki
yang sama, bukan hierarki kedua yang independen.

## Modul 3 — Katalog sebab-akibat device

Dipakai setiap kali memilih device (chord, voicing, ritme) yang belum
eksplisit tercantum di hierarki teori (Modul 2). Format: **Device → Mengapa
(efek musikal) → Kapan JANGAN**. Memakai device sesuai kolom "Mengapa" tidak
butuh justifikasi tambahan; memakainya di luar itu (melanggar "Kapan JANGAN")
tetap butuh justifikasi eksplisit ekstra, dicatat di baris "Device di luar
hierarki" pada deklarasi Modul 2.

| Device | Mengapa (efek musikal) | Kapan JANGAN |
|---|---|---|
| **ii–V–I** | Butuh arah menuju tonic — rasa "pulang" yang jelas | Section butuh statis/ambigu (mis. nocturnal dengan pedal point) |
| **maj9 / 6-9** | Warna lembut & hangat, bukan dominant yang keras | Menjelang klimaks yang butuh tegangan tajam |
| **secondary dominant** | Dorongan terarah ke chord berikutnya | Dipakai berturutan di tiap bar — jadi generik |
| **broken chord** | Tekstur mengalir, beri ruang bagi bass/melodi | Bass sudah aktif secara ritmis — bisa masking register rendah |
| **melodi stepwise** | Frase smooth, mudah diikuti, menegaskan motif | Dipakai sepanjang lagu tanpa variasi |
| **m7/m9/m11** | Warna lembut/introspektif tanpa tegangan dominant | Menggantikan SELURUH fungsi dominant |
| **7sus/9sus/13sus** | Gerak tanpa agresi, menunda resolusi sengaja | Dipakai di cadence final |
| **altered dominant** | Tensi singkat & terkonsentrasi, penanda puncak | Section "tenang"/"fokus" |
| **borrowed iv / modal interchange** | Warna wistful, kaburkan batas mayor/minor | Tanpa top-line yang menegaskan warna baru |
| **slash chord / inversi** | Bass melodis, memuluskan gerak root | Bass sudah punya garis independen yang berfungsi sendiri |
| **chromatic approach** | Transisi halus menuju target chord-tone, hemat | Dipakai berturutan >2x |
| **pedal point** | Menahan satu area harmoni, fokus & ruang | Section butuh gerak root aktif (mis. hopeful yang membangun) |
| **rest / silence** | Pelepasan tensi, ruang bagi motif untuk "diingat" | Berlebihan hingga groove terasa terputus |
| **omit-root voicing** | Hindari mud register rendah, beri ruang bass | Instrumen chord main solo tanpa bass |
| **ghost note** | Feel/pocket (drum & bass), bukan hiasan | Menggantikan groove utama |
| **register shift** | Menaikkan intensitas, menandai batas section baru | Dipakai tiap bar |

Cara pakai: cek dulu apakah device sudah tercakup di baris "Pendukung ..."
hierarki (Modul 2) — kalau ya, pakai langsung. Kalau tidak, cari di tabel
ini; kolom "Mengapa" jadi justifikasi otomatis, cek "Kapan JANGAN" dulu.
Tidak ada di tabel dan tidak di hierarki: butuh justifikasi manual eksplisit
atau jangan dipakai. Cek "Kapan JANGAN" ulang tiap pemakaian, bukan sekali di
awal lalu diasumsikan selalu aman. `neo-soul-genre.md` bisa menambah device
khas genre yang tak generik cukup untuk tabel ini.

## Modul 4 — Kompatibilitas, leadership, dan batas ide per section

Dipakai di Step 5 (quality gate), terhadap draft kandidat **penuh** — bukan
per not. Draft yang benar secara teori per section masih bisa gagal ketika
disusun bersama.

**Lensa 1 — Matriks kompatibilitas.** Pasangan yang **cocok** (saling
memberi ruang): harmoni kompleks + melodi sederhana; groove sederhana +
voicing kaya; bass tenang + piano lebih aktif; melodi aktif + accompaniment
minimal. Pasangan yang **tabrakan** (saling merebut ruang): melodi ramai +
piano ramai bersamaan; harmoni sangat chromatic + bass terlalu bebas (dua
sumber ketidakstabilan sekaligus); tempo lambat + pergantian chord terlalu
sering (harmonic rhythm tak proporsional); mood santai + aksen ritmis
agresif. Kalau ketemu pasangan tabrakan: kurangi salah satu (subtractive),
jangan tambah elemen ketiga untuk "menyeimbangkan".

**Lensa 2 — Element leadership per section.** Tiap section punya **SATU**
pemimpin; elemen lain memberi ruang:

| Section | Dipimpin oleh |
|---|---|
| Intro | Tekstur piano/comping |
| Tema (A) | Melodi |
| Solo | Improvisasi (lead yang sedang giliran) |
| Transisi | Harmoni (pergerakan chord yang menandai arah baru) |
| Outro | Resolusi (harmoni kembali ke tonic + subtraksi elemen) |

Saat melodi jadi fokus, harmoni & rhythm section WAJIB memberi ruang — bukan
ikut jadi fokus kedua. Dua elemen berebut foreground di section yang sama
adalah red flag.

**Lensa 3 — Batas ide utama per section.** Per section, batasi ide teori
yang aktif bersamaan ke **satu** masing-masing: satu karakter harmoni, satu
motif melodi (versi transformasi motif pusat), satu groove utama, satu
tekstur dominan. Terlalu banyak teori sekaligus membuat section kehilangan
identitas — pendengar tak bisa menangkap "section ini tentang apa". Variasi
*antar*-section itu sehat (lihat variation budget di `neo-soul-genre.md`);
variasi *di dalam* satu section yang sama itu bahaya.

**Menjalankan ketiga lensa:** bagi draft per section → cek Lensa 1 (pasangan
aktif), Lensa 2 (satu pemimpin), Lensa 3 (satu ide per dimensi) → section
yang gagal salah satu: revisi (biasanya subtractive), lalu jalankan ulang
Modul 6 (tension/release) untuk section yang direvisi.

## Modul 5 — Level struktur: makro / meso / mikro

Teori bekerja pada tiga level; urutan pengerjaan wajib besar dulu, baru
menengah, baru kecil.

| Level | Unit kerja | Contoh keputusan | Kalau bermasalah, revisi di sini... |
|---|---|---|---|
| **Besar (makro)** | Seluruh lagu | Bentuk lagu, tonal center, arah energi keseluruhan | Balik ke sini SADAR — re-declare hierarki (Modul 2) bila tonal center berubah |
| **Menengah (meso)** | Section / frase 4-8 bar | Progresi chord per section, batas frase, cadence, modulasi | Revisi section itu; cek dampak ke section tetangga |
| **Kecil (mikro)** | Bar / beat | Voicing spesifik, passing tone, artikulasi, motif ritmis lokal | Revisi lokal SAJA — bukan alasan mengubah bentuk besar |

Aturan pengikat: keputusan besar mengikat menengah, menengah mengikat kecil.
Jangan revisi level besar dari keluhan level kecil tanpa sadar — satu voicing
aneh di satu bar adalah petunjuk perbaikan voicing (kecil), bukan alasan
otomatis ganti bentuk lagu. Naikkan level revisi hanya bila masalah muncul
konsisten di banyak section (pola, bukan satu titik), dan lakukan itu secara
sadar (nyatakan eksplisit alasannya).

Di alur `jazz-idea-generator` lama (kini `jazz-composition` + `vibes-mood`),
ini berarti: Step 2-3 mengerjakan level besar (arc, bentuk, tonal center)
lebih dulu; bar-by-bar chords (Step 3 poin 3) dan phrasing (poin 6) adalah
level menengah; voicing konkret nota-per-nota adalah level kecil yang
sengaja **ditunda** ke modul `abc-notation`/`midi-orchestration` (lihat
catatan "production-stage" di §Workflow Step 3 SKILL.md ini) — pemisahan
itu konsisten dengan aturan "besar dulu" di sini.

## Modul 6 — Tension & release sebagai alat evaluasi

Berbeda dari palet teknik tension-release di `ideation-theory.md` §4c (daftar
*teknik* yang bisa dipakai), modul ini adalah **alat evaluasi**: scan draft
yang sudah ditulis dan bandingkan dengan rencana arah energi level besar
(Modul 5). Kosakata baku:

| Elemen | Efek |
|---|---|
| **Tonic** | Stabilitas, "rumah" — titik rileks |
| **Dominant** | Tegangan — butuh resolusi |
| **Chromatic note** | Warna / tekanan sesaat |
| **Rest (silence)** | Pelepasan — ruang bagi motif untuk diingat |
| **Register tinggi** | Intensitas naik |
| **Voicing rapat (close)** | Kepadatan |
| **Voicing terbuka (open/spread)** | Kelonggaran |

Pertanyaan wajib, ditanyakan SEBELUM menulis section (rencana) dan SESUDAH
(verifikasi): *di mana musik perlu tegang, di mana harus rileks?* Buat peta
sederhana:

| Section | Rencana (sebelum) | Realisasi (sesudah) | Elemen dominan yang terpakai |
|---|---|---|---|
| Intro | rendah | ... | mis. tonic, voicing terbuka, rest |
| A1 | sedang | ... | mis. dominant di akhir frase |
| B/detour | tinggi | ... | mis. chromatic note, voicing rapat |
| A3 | sedang→rendah | ... | mis. kembali ke tonic |
| Outro | rendah | ... | mis. rest, tonic, register turun |

Rencana "tinggi" tapi realisasi datar (semua tonic/rest/register rendah) =
sinyal revisi di level menengah/kecil (Modul 5) — tambahkan device yang
sesuai (Modul 3), bukan mengubah bentuk lagu. Kesalahan umum yang ditangkap
alat ini: section "tegang" ditulis dengan kosakata "release" semua; klimaks
yang tak pernah dipersiapkan; resolusi yang tak pernah tercapai (tension
menumpuk tanpa rest/tonic yang cukup untuk melepaskannya).

## Modul 7 — Protokol verifikasi terukur (adaptasi pipeline paket ini)

Sumber asli (`compose-song`) menulis protokol ini untuk pipeline JS
internalnya sendiri (`fromComposition`/`realize`/`toMidi`/`POST /api/render`
milik repo `daw_generative`). Paket `music-composition-skill` ini **tidak**
memiliki pipeline itu — hilir paket ini adalah engine `daw_generative`
(pemakai eksternal, lewat kontrak `POST /api/render {abc, drums?,
mastering?}`) **atau** konverter music21/`pretty_midi` milik paket ini sendiri
(`skills/abc-notation/scripts/validate_abc.py` →
`skills/midi-orchestration/scripts/abc_to_midi.py` +
`grid_to_midi.py`, dulu `abc-notation-writer`/`abc-to-midi-orchestration`)
menuju BandLab/DAW eksternal. Prinsip dan bentuk
pengecekan tetap sama; berikut adaptasinya:

1. **Validasi mekanis** (wajib, mengganti "note-on velocity>0 di canonical
   Song"): `validate_abc.py` (struktur, durasi bar, tie/slur) dan, bila
   music21 tersedia, `music21.converter.parse` — ini gerbang keras sebelum
   lanjut ke orchestration (lihat `skills/abc-notation/SKILL.md`, dulu
   `abc-notation-writer/SKILL.md` Step 4).
2. **MIDI hasil merge** (menggantikan cek WAV stereo non-silent bila hilir
   BUKAN `daw_generative`): setelah `abc_to_midi.py` + `grid_to_midi.py` +
   merge (`skills/midi-orchestration/references/midi-conversion.md`), cek
   sync antar-track, lead mono (polifoni maks 1), dan tidak ada drone
   (chord-symbol ter-strip) — checklist ini sudah ada di
   `midi-conversion.md` dan WAJIB dijalankan, bukan diasumsikan lolos karena
   file `.mid` ada.
3. **Durasi vs bentuk lagu:** hitung ekspektasi (`bars × beatsPerBar × 60 /
   bpm`) dan bandingkan dengan durasi MIDI/WAV aktual. Selisih besar → bar
   count per section di ABC (atau di drum grid) tidak sesuai rencana —
   kembali ke `jazz-composition`/`abc-notation` (dulu
   `jazz-idea-generator`/`abc-notation-writer`), bukan "lewati".
4. **Densitas per track vs density ceiling genre:** hitung proporsi waktu
   tiap track aktif (bukan rest) per section, bandingkan dengan density
   ceiling genre (lihat `neo-soul-genre.md` — mis. ≤1 foreground voice pada
   satu waktu). Ini menangkap "benar teori tapi penuh" yang tak tertangkap
   validator mekanis — kembali ke Modul 4 Lensa 2/3 kalau gagal.
5. **Tabrakan register lead vs comping:** bandingkan rentang MIDI note lead
   vs comping per section; overlap besar saat keduanya aktif = indikasi
   masking — perbaikan lewat omit-root voicing/register shift (Modul 3).
6. **Kalau hilir = `daw_generative` engine:** server itu sudah menjalankan
   `assertAudible` sendiri saat `POST /api/render` (200 = lolos cek
   silent/durasi minimal server-side). Status 200 dari server **bukan**
   pengganti poin 3-5 di atas — itu cuma memastikan tidak bisu total.

**Yang TIDAK bisa dilakukan agent** (berlaku di paket ini juga, tanpa
kecuali): menilai apakah lagu "enak"/"menyentuh"/"sesuai vibe" secara
subjektif; mendengarkan tanpa bias ekspektasi teori; menangkap elemen yang
"berlebihan/mengganggu" meski lolos semua cek teoretis. Itu wewenang
manusia — konsisten dengan prinsip "Telinga dulu, metrik menyusul" di
`CLAUDE.md` proyek `daw_generative`. Keberadaan file `.mid`/`.wav` **bukan**
bukti sukses, hanya bukti pipeline jalan tanpa crash. Skill ini (dan skill
lain di paket ini) **DILARANG** mengklaim "enak"/"bagus"/"keren" — klaim
maksimal yang boleh: *"lolos teori + metrik terukur sehat, menunggu telinga
manusia."*

## Kaitan dengan file lain di paket ini

- Modul 1-2 dipakai bersamaan dengan `ideation-theory.md` §4b lama (kini
  `skills/arrangement/references/form-and-dramaturgy.md` §11a) saat Step 1-2
  dari `jazz-composition/SKILL.md` (dulu `jazz-idea-generator/SKILL.md`).
- Modul 3-5 dipakai saat Step 3 (generate candidates) dan mengikat bagaimana
  kandidat dibedakan secara struktural, bukan hanya kosmetik.
- Modul 4 dan 6 bersama-sama menjadi isi konkret Step 5 (quality gate) —
  gate itu sudah ada di `SKILL.md`, modul ini memberinya alat yang bisa
  dijalankan secara eksplisit, bukan sekadar "dengar apakah enak".
- Modul 7 relevan lagi setelah `abc-notation` dan `midi-orchestration`
  (dulu `abc-notation-writer`/`abc-to-midi-orchestration`) bekerja —
  dicatat di sini karena kerangka
  pertanyaannya berasal dari proses penalaran yang sama, meski eksekusi
  teknisnya ada di skill selanjutnya.

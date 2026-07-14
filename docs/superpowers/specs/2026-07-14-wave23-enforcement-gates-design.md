# Spec: Wave 2-3 — Enforcement Gates dan Gigi Penilaian

**Tanggal**: 2026-07-14
**Status**: desain final untuk implementasi (Gelombang 2-3 dari rangkaian 3
gelombang); **diamandemen 2026-07-14** menambah Komponen E (export produksi
via engine `daw_generative`) — lihat "Amandemen — Komponen E" setelah D5.

## Latar

Gelombang 1 (protokol kandidat→seleksi Level 1-4, drum engine v2, gate
klaim-vs-notasi — lihat
`docs/superpowers/specs/2026-07-14-wave1-seleksi-drum-claimgate-design.md`)
sudah merge ke `main` dan teruji: run `runs/2026-07-14-dawn-shift-home/`
dijalankan end-to-end memakai skill versi Gelombang 1 dan **lulus L3 telinga
user**. Itu membuktikan akar masalah Gelombang 1 (generate-then-defend, drum
tile identik, klaim teori tak cocok notasi) sudah tertangani, tapi juga
menyisakan dua celah yang tidak disentuh Gelombang 1:

1. **Aturan yang sudah ada di `references/*.md` tapi tak pernah digerbang di
   level.** Beberapa referensi modul (model transisi 4-tahap di
   `instrumental-transitions.md`, kebijakan "satu ide per section" di
   `reasoning-theory.md`) sudah tertulis sejak konsolidasi 2026-07-13, tapi
   file level yang benar-benar dibaca orchestrator (`level-11-*.md`,
   `level-08-bass.md`, dst.) tidak pernah mewajibkan pemakaiannya secara
   eksplisit — device itu ada di kosakata, tapi tidak ada gate yang menolak
   artefak yang mengabaikannya.
2. **Tempo diperlakukan sebagai dekorasi, bukan parameter hilir.** Tak satu
   pun level yang memutuskan materi ritmis (melodi, groove, bass, drum)
   diwajibkan mengecek keputusannya terhadap BPM brief — sebuah motif 16th
   note padat bisa lolos semua rubrik teori sambil tidak bisa dimainkan
   secara wajar pada BPM lambat, atau sebaliknya terdengar encer pada BPM
   cepat.
3. **Penilaian (scorecard) belum "bergigi."** L2 rubrik per-level yang ada
   bisa semuanya skor 2 sambil piece tetap generic — tidak ada kriteria
   blocker yang memaksa revisi, tidak ada uji buta yang memverifikasi arc
   emosional benar-benar terbaca dari notasi (bukan dari membaca brief),
   tidak ada audit originalitas terhadap cliché genre yang terdokumentasi,
   dan tidak ada kewajiban menunjukkan bukti bahwa revisi sungguh terjadi.

Gelombang 2 (komponen C1-C8) mewiring aturan-aturan yang sudah ada tapi belum
digerbang, plus menjadikan tempo parameter hilir yang dicek lintas-level.
Gelombang 3 (komponen D1-D5) memberi "gigi" pada penilaian: kriteria blocker
fail-closed, uji buta emosional, audit cliché, dan syarat bukti revisi.

**Seluruh perubahan Gelombang 2-3 (C1-C8, D1-D5) di spec ini adalah perubahan
DOKUMEN SAJA — nol perubahan kode Python.** Ini keputusan YAGNI yang sadar:
semua komponen di bawah adalah instruksi prosa yang dieksekusi oleh agent LLM
yang mengikuti `SKILL.md`, bukan logika yang perlu diotomasi di script.
Konsekuensi langsung: verifikasi implementasi nanti = **konsistensi teks,
anchor, dan cross-reference** antar file (nama file dirujuk benar-benar ada,
istilah dipakai konsisten, gate bisa diikuti langkah demi langkah oleh
agent) — **bukan** unit test Python. (**Amandemen**: klaim "nol perubahan
Python" ini tetap berlaku persis untuk C1-C8/D1-D5 — Komponen E yang
ditambahkan di bawah, setelah D5, adalah pengecualian **terbatas dan
eksplisit**, bukan pembatalan prinsip ini; lihat "Amandemen — Komponen E".)

## Scope

**In scope:**

- Gelombang 2 — C1 s.d. C8 (lihat "Desain per komponen" di bawah):
  gate transisi 3-fase, dinamika observabel + micro-apex, bass anti-default,
  micro-improvisation map, intro performatif + ending rekontekstualisasi,
  comping cells mengikuti ruang lead, rekonsiliasi kebijakan "1 ide vs 2-3
  gerakan", dan tempo sebagai parameter hilir (5 file).
- Gelombang 3 — D1 s.d. D5: blocker scorecard fail-closed, L2-blind
  (emotional blind test), L2-cliche (originality audit + register cliché),
  bukti revisi, dan L3 wajib per-piece + checklist pra-L3.
- **Amandemen — Komponen E** (baru, requirement product owner 2026-07-14:
  "export harus memakai flow yang ada di `daw_generative`; instrumen
  disesuaikan dengan yang tersedia"): export produksi lewat flow engine yang
  **sudah ada** di repo induk (`POST /api/render`), konverter format drum
  Tool 1 → skema engine, dan penyelarasan instrumentasi ke registry
  instrumen engine yang sungguh tersedia — lihat "Amandemen — Komponen E:
  Export via engine daw_generative" (E1-E4) setelah D5 di bawah. Berbeda
  dari C1-C8/D1-D5, komponen ini **mencakup perubahan kode Python terbatas**
  (lihat catatan out-of-scope tepat di bawah).

**Out of scope (jangan dikerjakan sebagai bagian spec ini):**

- **Untuk C1-C8/D1-D5 (Gelombang 2-3):** perubahan kode Python apa pun
  (`*.py` di `skills/*/scripts/`) — nol perubahan mekanis di dua gelombang
  itu, murni dokumen; ini **tidak berubah** oleh amandemen Komponen E.
- **Komponen E adalah pengecualian terbatas dan eksplisit** atas batas di
  atas — bukan pembatalannya: satu script konverter **baru**
  (`skills/midi-orchestration/scripts/drums_to_engine.py`) + test TDD-nya,
  plus penyelarasan angka pada `PROGRAM` map yang **sudah ada** di
  `skills/midi-orchestration/scripts/abc_to_midi.py` (lihat E2 dan E3 di
  bagian Amandemen). Di luar dua titik itu, tidak ada perubahan Python lain
  yang masuk scope spec ini.
- Audio dalam bentuk apa pun — render tetap eksklusif Tool 2 (`daw_generative`
  engine, `POST /api/render`), tidak disentuh spec ini.
- Renumbering lapisan penilaian L1/L2/L3 — penomoran yang sudah dipakai di
  semua dokumen dan run lama **tidak berubah**. Mekanisme baru (`L2-blind`,
  `L2-cliche`, bukti revisi) masuk sebagai **keluarga L2 tambahan**, bukan
  `L4`/`L5`/`L6` baru.
- Gelombang berikutnya (belum didefinisikan) — spec ini berhenti di D5.

## Konstrain arsitektur

- Paket ini adalah **Tool 1** ("otak") dalam arsitektur 2-tools: outputnya
  notasi ABC, `drums.json`, dan MIDI *validasi* lewat script Python lokal.
  **Tidak ada audio di paket ini** — audio adalah **Tool 2**, dijalankan
  lewat HTTP `POST /api/render` di luar repo ini. Tidak satu pun komponen di
  bawah boleh menambah dependensi audio/DAW, atau menyiratkan bahwa gate baru
  "mendengarkan" apa pun.
- Semua gate baru harus bisa **dieksekusi oleh agent LLM** yang mengikuti
  `SKILL.md` — ditulis sebagai prosedur/prosa yang bisa diikuti langkah demi
  langkah (tabel yang harus diisi, pertanyaan yang harus dijawab tertulis),
  bukan otomasi tersembunyi yang butuh kode baru.
- **Penilaian pendengaran tetap eksklusif L3 manusia.** `L2-blind` dan
  `L2-cliche` (Gelombang 3) dijalankan oleh subagent LLM segar dan menilai
  hal yang bisa diverifikasi dari notasi/teks (arc yang terbaca, kecocokan
  dengan register cliché) — keduanya **bukan** pengganti telinga manusia,
  dan tidak boleh diklaim setara dengannya (lihat Modul 7
  `reasoning-theory.md`: agent dilarang mengklaim "enak"/"bagus"/"keren").
- **Penomoran L1/L2/L3 dikunci.** Mekanisme baru masuk sebagai sub-varian
  L2: `L2-rubrik` (sudah ada, per-level), `L2-blind` (baru), `L2-cliche`
  (baru), plus syarat "bukti revisi" yang menempel ke L2/pra-L3 tanpa
  mendapat label `L`-angka sendiri. Istilah ketiganya dipakai **persis**
  dengan tanda hubung ini di seluruh dokumen yang diubah — jangan
  `L2 blind`/`l2-blind`/`Blind L2` dsb.

## Desain per komponen

### Gelombang 2

#### C1 — Gate transisi 3-fase (Level 11)

**Tujuan.** Model transisi 4-tahap (setup/threshold/arrival/aftercare) sudah
tertulis di `skills/arrangement/references/instrumental-transitions.md` §1
sejak konsolidasi 2026-07-13, tapi `level-11-interlude-shout-transisi.md`
tidak pernah mewajibkan pemakaiannya — artefak Level 11 bisa selesai hanya
dengan menyebut "ada drum fill di sini" tanpa mengikat ke model itu.

**Perubahan konkret.** `level-11-interlude-shout-transisi.md`, bagian
"Output level ini", diganti dari "bagian transisi yang tertulis jelas" jadi
kewajiban tabel **per transisi section** dengan kolom:

| Kolom | Isi |
|---|---|
| Preparation | 1-2 bar sebelum batas — apa yang mulai berubah, instrumen mana |
| Boundary event | kejadian tepat di batas section |
| After-effect | 1-2 bar sesudah batas — apa yang terbawa/tertahan dari sebelum batas |

Tabel ini wajib mengutip dan menautkan eksplisit ke model 4-tahap
setup/threshold/arrival/aftercare di `instrumental-transitions.md` §1 (link
relatif, bukan sekadar menyebut nama) — preparation ≈ setup, boundary event
≈ threshold+arrival, after-effect ≈ aftercare.

**Gate.** Transisi yang hanya berupa kejadian tepat di barline (kolom
preparation dan after-effect kosong/tidak diisi) = **ditolak**, artefak
direvisi sebelum lanjut ke level berikutnya. Ini konsisten dengan
`instrumental-transitions.md` §9 (failure mode "no confirmation after a
dramatic buildup") dan §6 (arrival harus dikonfirmasi ≥2 cue) — gate baru ini
memaksa kedua sisi batas (bukan hanya sisi datang) ditulis eksplisit.

**File yang berubah:**

- `skills/jazz-composition/references/level-11-interlude-shout-transisi.md`
  — ganti "Output level ini" jadi tabel 3-kolom di atas + kutipan/link ke
  `instrumental-transitions.md` §1 + kalimat gate penolakan.

#### C2 — Dinamika observabel + micro-apex wajib (Level 13)

**Tujuan.** Template energy curve persentase (`Intro 20% ... Coda 30%`) di
`level-13-dinamika-dramaturgi.md` tidak bisa diverifikasi dari notasi —
angka persen adalah klaim, bukan fakta yang bisa dicek. Section "restrained"
juga sering jadi alibi untuk section yang sekadar datar tanpa momen berarti.

**Perubahan konkret.** `level-13-dinamika-dramaturgi.md`: ganti template
persentase dengan **tabel per section berisi metrik observabel**:

| Metrik | Sumber |
|---|---|
| Active voices | hitung manual dari partitur/ABC per section |
| Note-attacks per bar | diisi dari output `notation_facts.py` per voice (script sudah ada dari Gelombang 1 — lihat `skills/abc-notation/scripts/notation_facts.py`) |
| Register lead | rendah/tengah/tinggi + rentang aktual |
| Durasi not rata-rata | dari notasi per section |
| Drum hits per bar | dari `drums.json`/roadmap drum |
| Dynamic marks | dari notasi (mf, mp, dst., bila ada) |

Plus field **wajib** baru: **micro-apex** — satu bar spesifik per piece
(atau per bagian besar) yang menjadi momen paling berarti, ditulis sebagai
"bar N: <mekanisme>". Mekanisme harus dari kelas non-volume: register
ekstrem tipis (satu nada tinggi/rendah sesaat), dissonance singkat, drop
groove (instrumen berhenti sesaat), ruang kosong (rest terjadwal), dsb —
**bukan** "volume naik" atau "semua instrumen tutti".

**Gate.** Section yang dilabeli "tidak ada peak"/"restrained" tanpa
micro-apex yang terdefinisi = **ditolak** — restrained tidak sama dengan
datar; artefak harus tetap menunjuk satu momen mekanisme non-volume yang
membuat section itu diingat.

**File yang berubah:**

- `skills/jazz-composition/references/level-13-dinamika-dramaturgi.md` —
  ganti tabel persentase dengan tabel metrik observabel di atas + field
  micro-apex wajib + kalimat gate.

> Catatan scope: `skills/arrangement/SKILL.md` §Level 13 memuat contoh
> energy-curve persentase yang sama secara prosa — spec ini **tidak**
> mengubahnya (tidak diminta di brief desain), lihat laporan akhir untuk
> catatan inkonsistensi minor ini.

#### C3 — Bass anti-default (Level 8)

**Tujuan.** `level-08-bass.md` saat ini hanya punya **satu** contoh konkret
(walking bass, approach-note di beat 4), sehingga chromatic approach jadi
default de-facto meski file yang sama sudah mendaftar enam pendekatan lain
(two-feel, pedal point, ostinato, broken groove, counterline, slash-bass
movement).

**Perubahan konkret.** `level-08-bass.md`: tambah kewajiban **tabel per
transisi chord** (bar N → bar N+1, atau chord A → chord B) berisi kolom
"device dipakai" + "alasan musikal (1 kalimat)". Aturan kuota: **chromatic
approach maksimal ~1/3 dari seluruh transisi chord dalam piece**; sisanya
diambil dari menu: diam/rest, common tone, octave displacement, anticipation,
pedal/held-through (bisa juga two-feel/pedal point/ostinato/counterline/
slash-bass dari daftar "Pilihan pendekatan" yang sudah ada di file). Plus
wajib menyebut **relasi bass-kick per section** (lock point — di beat/step
mana bass dan kick drum bertemu secara sengaja).

Contoh walking-bass approach-note yang sudah ada di file (`D – F – A – Ab |
G`) diberi catatan eksplisit: **"salah satu opsi, bukan default"** — supaya
contoh tunggal yang ada tidak dibaca sebagai satu-satunya cara benar.

**File yang berubah:**

- `skills/jazz-composition/references/level-08-bass.md` — tambah tabel
  device+alasan per transisi chord, aturan kuota chromatic ≤1/3, kewajiban
  relasi bass-kick per section, dan catatan "salah satu opsi, bukan default"
  pada contoh walking-bass yang sudah ada.

#### C4 — Micro-improvisation map (Level 10)

**Tujuan.** `level-10-improvisasi.md` saat ini berasumsi selalu ada solo
section formal (chorus count per solois). Piece tanpa solo section (banyak
brief neo-soul/chill-jazz singkat tidak punya solo formal) selama ini lolos
Level 10 tanpa kewajiban apa pun — seolah "tanpa solo" berarti "nol perilaku
improvisatoris di seluruh piece."

**Perubahan konkret.** `level-10-improvisasi.md`: tambah **subsection baru**
untuk kasus piece **tanpa** solo section — artefak Level 10 tetap wajib
berisi **micro-improvisation map**, berisi:

- bar mana boleh diornamen (pickup bebas, tail ad-lib, ornament lokal);
- nada anchor yang wajib dipertahankan (nada yang tidak boleh diubah performer);
- range maksimum penyimpangan yang diizinkan;
- gesture yang terlarang secara eksplisit;
- tingkat kebebasan ritmis per section (ketat/sedang/longgar).

Kalimat penutup subsection: **"tanpa solo" ≠ "nol perilaku improvisatoris"**
— setiap piece, bersolo atau tidak, punya map ini.

**File yang berubah:**

- `skills/jazz-composition/references/level-10-improvisasi.md` — tambah
  subsection micro-improvisation map untuk piece tanpa solo section, dengan
  lima field di atas.

#### C5 — Intro performatif + ending rekontekstualisasi (Level 12)

**Tujuan.** `level-12-intro-ending.md` mendaftar pilihan intro/ending sebagai
menu datar tanpa gate — intro "pad sempurna sejak beat 1" dan ending "makin
sepi + tonic panjang" keduanya lolos begitu saja meski keduanya adalah pola
yang paling generik/aman.

**Perubahan konkret.** `level-12-intro-ending.md`:

- **(a) Intro performatif wajib.** Intro wajib mengandung **≥1 kejadian
  performatif spesifik** dari menu: incomplete voicing (chord yang sengaja
  belum lengkap), delayed entrance salah satu instrumen, frase yang
  terdengar "mencari" nada (belum landing di target tone), atau ruang/napas
  yang disengaja (rest terjadwal, bukan filler). Pad sempurna sejak beat 1
  = **ditolak tanpa justifikasi tertulis**.
- **(b) Opsi ending baru: rekontekstualisasi.** Ditambahkan ke daftar pilihan
  ending yang sudah ada (tag ending, ritardando, fermata, dst.): nada yang
  sepanjang lagu terasa tegang (mis. muncul berulang sebagai tension/
  outside/dissonant note) **dipertahankan** persis di ending, tapi harmoni
  di bawahnya berubah sehingga nada yang sama kini terasa **diterima**
  (resolved) tanpa nada itu sendiri berubah.
- **(c) Gate ending.** Ending bertipe "makin sepi + tonic panjang" (fade-
  style vamp/pola paling umum) hanya boleh dipilih **setelah** alternatif
  rekontekstualisasi dipertimbangkan tertulis — minimal 1 kalimat kenapa
  rekontekstualisasi tidak dipakai untuk piece ini.

Satu kalimat rujukan ditambahkan ke `skills/arrangement/SKILL.md` §Level 12,
mengarahkan ke gate lengkap di `level-12-intro-ending.md`.

**File yang berubah:**

- `skills/jazz-composition/references/level-12-intro-ending.md` — tambah
  gate intro performatif (a), opsi ending rekontekstualisasi (b), dan gate
  pertimbangan-tertulis (c).
- `skills/arrangement/SKILL.md` §Level 12 — satu kalimat rujukan ke gate di
  atas.

#### C6 — Comping cells mengikuti ruang lead (Level 7)

**Tujuan.** Level 7 sudah mendaftar teknik comping (Charleston rhythm,
anticipatory stab, sustained pad, dst.) tapi tidak pernah mewajibkan
comping benar-benar dipetakan ke napas lead — comping chart yang ada
(`A1: sparse, 2-3 attacks per bar`) adalah deskripsi kepadatan, bukan
pemetaan interaksi.

**Perubahan konkret.** `skills/arrangement/SKILL.md` §Level 7 dan
`skills/jazz-composition/references/level-07-comping-voicing.md`: tambah
deliverable wajib — pilih **≥3 comping cell berbeda** dari vocabulary yang
sudah ada di arrangement SKILL (held / delayed answer / short syncopated
stab, atau turunan dari Charleston rhythm/anticipatory stab/fragmented
chord/dll. yang sudah terdaftar), lalu **petakan ke ruang lead**: bar mana
lead bernapas (rest/held note panjang) → cell comping apa yang mengisi ruang
itu, atau justru diam.

**Gate.** Comping uniform 1 attack/bar sepanjang lagu = **ditolak**, kecuali
dijustifikasi eksplisit terhadap peta napas lead (mis. lead memang tidak
pernah bernapas di section itu, jadi comping sengaja seragam untuk
mendukung, bukan lupa memvariasikan).

**File yang berubah:**

- `skills/arrangement/SKILL.md` §Level 7 — tambah kewajiban ≥3 comping cell
  + pemetaan ke napas lead.
- `skills/jazz-composition/references/level-07-comping-voicing.md` — sama,
  ditambahkan ke bagian "Output level ini" + gate penolakan comping uniform.

#### C7 — Rekonsiliasi kebijakan "1 ide vs 2-3 gerakan"

**Tujuan.** `reasoning-theory.md` Modul 4 Lensa 3 ("Batas ide utama per
section") membatasi ke **satu** ide teori aktif per dimensi, sementara
`skills/RED-FLAGS.md` baris pertama menyatakan "most sections need 2-3
moves, not all of them" — dua kalimat ini terdengar kontradiktif
(satu vs 2-3) meski maksudnya sejalan.

**Perubahan konkret.** Satu paragraf klarifikasi ditambahkan ke Modul 4
Lensa 3 di `skills/vibes-mood/references/reasoning-theory.md`, menegaskan:
**"satu ide UTAMA per dimensi per section, plus hingga 2-3 detail pendukung
yang berkorelasi dengannya."** Detail pendukung bukan ide independen kedua —
ia harus bisa dijelaskan sebagai penjabaran/penguat ide utama yang sama,
bukan tema kedua yang bersaing untuk perhatian. Ini menyelaraskan Lensa 3
dengan RED-FLAGS.md tanpa merombak modul.

**File yang berubah:**

- `skills/vibes-mood/references/reasoning-theory.md` — satu paragraf
  klarifikasi ditambahkan setelah definisi Lensa 3 yang sudah ada, tidak
  mengubah struktur modul lain.

#### C8 — Tempo sebagai parameter hilir (5 file)

**Tujuan.** Tidak ada level manapun yang mengecek keputusan ritmisnya
terhadap BPM brief. Prinsip umum yang berlaku di semua sub-bagian di bawah:
**makin cepat BPM, makin jarang subdivisi rapat dipakai & makin panjang
frase dalam bar** — nilai konkret di tabel boleh disesuaikan penulis plan ke
konvensi genre file lain, tapi arah hubungannya tetap.

**(a) Tabel BPM band di `reasoning-theory.md`.**
`skills/vibes-mood/references/reasoning-theory.md` mendapat tabel baru:

| BPM band | Label | Subdivisi melodi wajar | Napas minimum | Harmonic rhythm wajar | Swing feel |
|---|---|---|---|---|---|
| < 72 | Ballad | 16th aman | ≥2 beat | — | — |
| 72-92 | Medium-slow | 16th selektif | ≥1.5 beat | — | — |
| 92-120 | Medium | 8th dominan, 16th sebagai ornamen | — | — | — |
| > 120 | Up | 8th/quarter, 16th berisiko | — | — | — |

("Napas minimum" = panjang minimum jeda/rest sebelum frase melodi
berikutnya, dalam beat & bisa dikonversi ke detik via `60/BPM × jumlah
beat`; kolom harmonic rhythm dan swing feel dirinci masing-masing di (c) dan
(d) di bawah, bukan diduplikasi di tabel ini.)

**(b) Gate densitas-vs-BPM di melody-design.**
`skills/melody-design/SKILL.md` dan
`skills/melody-design/references/rubric.md`: tambah gate — artefak Level 4
wajib menyebutkan **BPM brief secara eksplisit**; IOI (inter-onset interval)
tercepat yang benar-benar dipakai dan rest ratio melodi dicek terhadap tabel
(a). Kriteria rubrik baru ditambahkan ke `rubric.md`: **"kepadatan ritmis
melodi proporsional dengan tempo brief."** `skills/advanced-melody/SKILL.md`
mendapat satu kalimat pointer ke gate yang sama (chromatic vocabulary tahap
7-8 tunduk pada gate densitas yang sama, bukan gate terpisah).

**(c) Harmonic rhythm vs BPM di harmony.**
`skills/harmony/SKILL.md` mendapat sub-bagian baru di bawah "Langkah 2 —
Tentukan harmonic rhythm": rumuskan sebagai **durasi absolut per chord**:

```
durasi per chord (detik) = bars_per_chord × beats_per_bar × 60 / BPM
```

Target: minimal **±2 detik per chord** agar perubahan harmoni "teraba"
pendengar. Konsekuensi rumus ini (bukan aturan tempo-vs-jumlah-chord yang
berdiri sendiri): pada BPM rendah, satu bar berdurasi lebih panjang secara
absolut, sehingga 2 chord/bar tetap bisa aman asal masih ≥2 detik per chord;
pada BPM tinggi, 2 chord/bar lebih berisiko karena tiap chord kebagian
waktu absolut yang pendek. Rubrik harmony yang sudah menuntut "ritme
harmonik cocok dengan tempo" (lihat rubrik existing) kini punya rumus
konkret untuk mengeceknya, bukan penilaian rasa.

**(d) Breakpoint swing ratio di groove-meter.**
`skills/groove-rhythm/references/groove-meter.md` §3 (Swing feel), yang saat
ini hanya menyatakan prosa "the ratio tends to become more even at faster
tempos" tanpa angka, mendapat breakpoint operasional:

| BPM | Swing ratio |
|---|---|
| < 80 | 2:1 (≈66%) — masih nyaman |
| 80-120 | ≈60-64% |
| > 140 | mendekati even (≈55-57%) |

**(e) Ground rule lintas-level di orchestrator.**
`skills/jazz-composition/SKILL.md`, di dekat ground rules lain ("Aturan
dasar yang berlaku di semua level"): setiap level yang memutuskan materi
ritmis — **Level 4 (melodi), Level 5 (groove), Level 8 (bass), Level 9
(drum)** — wajib menyebut **BPM brief** di artefaknya sendiri dan mengecek
keputusannya terhadap tabel tempo di (a).

**File yang berubah:**

- `skills/vibes-mood/references/reasoning-theory.md` — tabel BPM band (a).
- `skills/melody-design/SKILL.md` — gate BPM eksplisit + cek IOI/rest ratio.
- `skills/melody-design/references/rubric.md` — kriteria baru "kepadatan
  ritmis melodi proporsional dengan tempo brief".
- `skills/advanced-melody/SKILL.md` — satu kalimat pointer ke gate yang
  sama.
- `skills/harmony/SKILL.md` — sub-bagian durasi absolut per chord.
- `skills/groove-rhythm/references/groove-meter.md` — tabel breakpoint
  swing ratio §3.
- `skills/jazz-composition/SKILL.md` — ground rule lintas-level baru
  (Level 4/5/8/9 wajib sebut BPM + cek tabel (a)).

### Gelombang 3

#### D1 — Blocker scorecard + fail-closed

**Tujuan.** Skor L2 rubrik yang tinggi di semua level bisa tetap tidak
menyelamatkan piece yang generic secara keseluruhan — tidak ada kriteria
yang mengikat di level "keseluruhan piece" yang bisa memblokir status
selesai.

**Perubahan konkret.** `skills/jazz-composition/references/scorecard-template.md`
mendapat **bagian baru "L2 global"** (lintas-level, dinilai terhadap
keseluruhan piece — ditempatkan setelah Level 14 dan sebelum `L3 (telinga)`
di struktur scorecard), berisi **4 kriteria BLOCKER**:

| # | Kriteria blocker |
|---|---|
| 1 | Identitas — 4 bar pertama bisa dibedakan dari template genre |
| 2 | Memorability — motif bisa diingat/dinyanyikan setelah sekali baca-dengar |
| 3 | Interaction — instrumen terdengar saling mendengar (ada bukti call-response/ruang) |
| 4 | Emotional specificity — arc terasa dari notasi tanpa membaca brief |

**Semantik fail-closed:** skor **0** pada **salah satu** dari keempat
kriteria ini = run **BELUM SELESAI**, terlepas dari skor kriteria lain —
wajib revisi + re-review sebelum boleh disebut selesai. Skor tinggi di
kriteria lain (L2-rubrik per-level) **tidak menyelamatkan** blocker yang
gagal.

`skills/jazz-composition/SKILL.md` §Penilaian menyatakan aturan fail-closed
ini secara eksplisit, plus merujuk checklist pra-L3 (lihat D5) yang
mengoperasionalkan syarat "semua blocker ≥1" sebagai gerbang sebelum
diserahkan ke telinga manusia.

**File yang berubah:**

- `skills/jazz-composition/references/scorecard-template.md` — bagian baru
  "L2 global" dengan 4 kriteria blocker + semantik fail-closed.
- `skills/jazz-composition/SKILL.md` §Penilaian — pernyataan aturan
  fail-closed + rujukan checklist pra-L3.

#### D2 — L2-blind (emotional blind test)

**Tujuan.** Arc emosional yang diklaim di brief/artefak konsep (`01-brief.md`)
tidak pernah diverifikasi secara independen — tidak ada cek bahwa arc itu
benar-benar terbaca dari notasi akhir, bukan hanya konsisten dengan niat
yang ditulis generator sendiri.

**Perubahan konkret.** Protokol **L2-blind** baru, didokumentasikan di
`scorecard-template.md` (bagian "L2 global") dan prosedurnya di
`skills/jazz-composition/SKILL.md` §Penilaian:

1. Orkestrator menulis **3 opsi arc emosional**: 1 arc yang sebenarnya
   (diambil dari artefak `01-brief.md`) + 2 distractor yang masuk akal,
   ditulis **tanpa membocorkan** mana yang benar (ketiganya ditulis dengan
   detail dan keyakinan setara).
2. Spawn **reviewer segar** (subagent baru, tanpa histori generasi) yang
   diberi **hanya**: `song.abc`, `drums.json`, output `notation_facts.py`,
   dan **3 opsi arc** di atas — **TANPA** brief asli, **TANPA** artefak
   desain lain (form, harmony, dst.), **TANPA** scorecard.
3. Reviewer memilih **1 opsi** + alasan tertulis (harus berbasis apa yang
   benar-benar terdengar/terbaca dari notasi, bukan tebakan buta).
4. **Salah pilih** = otomatis kriteria blocker "emotional specificity" (D1,
   kriteria #4) mendapat skor **0** — terhubung langsung ke fail-closed D1.
5. Hasil (benar/salah + alasan reviewer, apa adanya) dicatat **jujur** di
   `scorecard.md` — termasuk bila hasilnya salah pilih.

**File yang berubah:**

- `skills/jazz-composition/references/scorecard-template.md` — protokol
  L2-blind lengkap di bagian "L2 global".
- `skills/jazz-composition/SKILL.md` §Penilaian — prosedur 5 langkah di
  atas.

#### D3 — L2-cliche (originality audit) + register cliché

**Tujuan.** Tidak ada mekanisme yang mengecek apakah piece jatuh ke pola
neo-soul/AI-jazz generik yang sudah berulang kali muncul di paket ini
(intro pad+preview, ending fade+tonic, dst.) — device semacam ini valid
secara teori (lolos rubrik), tapi kehadirannya tanpa reinterpretasi adalah
sinyal "template di-reskin", bukan komposisi original.

**Perubahan konkret.**

File referensi **baru** `skills/jazz-composition/references/cliche-register.md`
— daftar cliché neo-soul/AI-jazz yang terdokumentasi, isi awal:

| Cliché | Kenapa terasa template | Jalur reinterpretasi |
|---|---|---|
| Intro 2-bar pad + motif preview lalu lead masuk | Pola paling umum di semua contoh genre, nol variasi struktural | lihat gate intro performatif C5(a) |
| Ending fade + held tonic | Sama, default paling aman | lihat opsi rekontekstualisasi C5(b) |
| Chromatic approach di tiap transisi bass | Approach note jadi refleks, bukan pilihan sadar | lihat kuota ≤1/3 C3 |
| Harmonic rhythm seragam 1 chord/bar full-piece dengan semua perpindahan di barline | Tak ada variasi harmonic rhythm sama sekali | variasikan lewat teknik `harmony/SKILL.md` (2 chord/bar terukur via C8c) |
| Rhodes block-chord 1 attack/bar sepanjang lagu | Comping statis, bukan dialog musikal | lihat gate ≥3 comping cell C6 |
| Drum pattern identik section-wide | Melanggar hierarchy drum v2 (Gelombang 1) | lihat aturan hierarchy `level-09-drum.md` |
| Progresi i-bVI-iv-V verbatim tanpa reinterpretasi | Progresi paling dikenal genre dipakai mentah | reharmonize sebagian/ubah voicing/ubah bass motion |
| "Restrained = tanpa momen berarti" | Dalih untuk section datar | lihat gate micro-apex C2 |
| Velocity random sebagai pengganti frase | `humanize_velocity` dipakai sebagai sumber variasi utama, bukan polish | lihat `phrase_velocity` (Gelombang 1, `level-09-drum.md`) |

Tiap entri wajib punya tiga kolom ini (nama, kenapa terasa template, contoh
reinterpretasi yang menyelamatkan) — entri tanpa jalur reinterpretasi tidak
lengkap.

Protokol **L2-cliche** di `scorecard-template.md` (bagian "L2 global") dan
`SKILL.md` §Penilaian: reviewer segar diberi notasi final + register ini →
menandai bagian yang **match** register **tanpa** reinterpretasi yang
terlihat. Composer wajib merespons **tiap temuan** dengan salah satu:

- **revisi** artefak/notasi terkait, atau
- **justifikasi audible spesifik** — mekanisme konkret yang bisa didengar
  kenapa device itu dipertahankan (justifikasi generik seperti "ini
  disengaja" tanpa mekanisme yang bisa didengar = **tidak diterima**; rujuk
  `skills/RED-FLAGS.md`).

**File yang berubah:**

- **File baru** `skills/jazz-composition/references/cliche-register.md` —
  9 entri di atas.
- `skills/jazz-composition/references/scorecard-template.md` — protokol
  L2-cliche di bagian "L2 global".
- `skills/jazz-composition/SKILL.md` §Penilaian — prosedur respons wajib
  (revisi atau justifikasi audible).

#### D4 — Bukti revisi (revision evidence)

**Tujuan.** Tidak ada kewajiban menunjukkan bahwa revisi yang diklaim
(setelah L1/L2/L2-blind/L2-cliche menemukan masalah) benar-benar terjadi —
"first draft dianggap final" adalah pola gagal yang belum tertangkap
eksplisit di `RED-FLAGS.md`.

**Perubahan konkret.** `skills/jazz-composition/SKILL.md` Tahap 15 (Revisi
low level) dan `scorecard-template.md`: sebelum run disebut selesai, wajib
ada bagian **"Bukti revisi"** berisi **≥1 pasangan before/after** untuk 2
masalah terbesar yang ditemukan oleh L1/L2/L2-blind/L2-cliche manapun.
Setiap pasangan wajib:

- kutip notasi/nilai **lama** → **baru** (bukan deskripsi umum "diperbaiki
  voicing-nya");
- 1 kalimat **efek yang diharapkan terdengar** dari perubahan itu.

Run **tanpa** satu pun revisi tercatat = red flag baru **"first draft
dianggap final"**, ditambahkan sebagai baris baru di `skills/RED-FLAGS.md`.

**File yang berubah:**

- `skills/jazz-composition/SKILL.md` Tahap 15 — kewajiban bagian "Bukti
  revisi" sebelum run disebut selesai.
- `skills/jazz-composition/references/scorecard-template.md` — struktur
  bagian "Bukti revisi" (≥1 pasangan before/after, 2 masalah terbesar).
- `skills/RED-FLAGS.md` — baris baru "first draft dianggap final" dengan
  pointer ke syarat bukti revisi.

#### D5 — L3 wajib per-piece + checklist pra-L3

**Tujuan.** `human-ear-protocol.md` saat ini ditulis dalam konteks
**evaluasi skill** ("run this on a small subset... not on every eval run"),
yang bisa disalahbaca sebagai izin melewati L3 untuk piece produksi biasa.
Perlu klarifikasi eksplisit tentang kapan sampling itu berlaku dan kapan
tidak, plus gerbang mekanis sebelum sebuah piece **boleh** diserahkan ke
telinga.

**Perubahan konkret.**

`skills/jazz-composition/references/human-ear-protocol.md`: klarifikasi
eksplisit — sampling ("2 briefs is enough", "not on every eval run") **hanya
berlaku untuk eksperimen evaluasi skill/paket ini sendiri** (mis. eval
before/after seperti `tests/results/2026-07-13-brief-01-02-armA-vs-armB.md`).
Untuk **piece produksi** (composer benar-benar membuat lagu untuk dipakai,
bukan mengevaluasi skill), **L3 wajib per-piece** sebelum piece itu disebut
selesai — tidak ada sampling untuk kasus ini.

`skills/jazz-composition/SKILL.md` §Penilaian: **checklist fail-closed
pra-L3** — semua item berikut harus terpenuhi sebelum sebuah piece
diserahkan ke telinga manusia:

- [ ] L1 (mekanis) — lulus semua level.
- [ ] L2-rubrik — lengkap terisi semua 14 level.
- [ ] 4 kriteria blocker (D1) — semuanya bernilai **≥1** (tidak ada yang 0).
- [ ] L2-blind (D2) — dijalankan, hasilnya **benar**.
- [ ] L2-cliche (D3) — semua temuan sudah direspons (revisi atau
      justifikasi audible).
- [ ] Bukti revisi (D4) — ada, terhubung ke temuan nyata.

Checklist ini adalah operasionalisasi konkret dari fail-closed rule D1 —
"belum boleh disebut selesai" sekarang berarti "checklist ini belum semua
tercentang", bukan penilaian subjektif kapan sebuah piece "cukup matang".

**File yang berubah:**

- `skills/jazz-composition/references/human-ear-protocol.md` — klarifikasi
  sampling-untuk-eval-skill vs. L3-wajib-per-piece-produksi.
- `skills/jazz-composition/SKILL.md` §Penilaian — checklist fail-closed
  pra-L3 (6 item di atas).

## Amandemen — Komponen E: Export via engine daw_generative

**Tanggal amandemen**: 2026-07-14, menyusul requirement baru product owner:
"export harus memakai flow yang ada di `daw_generative`; instrumen
disesuaikan dengan yang tersedia."

**Tujuan.** C1-C8/D1-D5 di atas menutup celah *penilaian* dan *gate teori* di
dalam Tool 1 (paket ini) — tapi berhenti di `output.mid` validasi lokal
(Python), belum pernah benar-benar menempuh jalur produksi (Tool 2, engine
`daw_generative`, `POST /api/render`) yang menghasilkan WAV bertimbre jujur
(soundfont FluidR3_GM asli, bukan preview browser). Komponen E menutup celah
itu: mewajibkan setiap run yang dianggap selesai benar-benar diekspor lewat
flow engine yang **sudah ada** di repo induk (bukan flow baru yang perlu
dibangun), dengan instrumentasi yang diselaraskan ke registry instrumen
engine yang sungguh tersedia — bukan nama instrumen yang hanya masuk akal di
kepala composer.

**Konsekuensi pada batas Gelombang 2-3.** Prinsip "nol perubahan kode
Python" (Latar/Scope) tetap berlaku persis untuk C1-C8/D1-D5 — Komponen E
adalah pengecualian **terbatas dan eksplisit**: satu script konverter baru +
penyelarasan angka di satu script yang sudah ada + test-nya (E2/E3), tidak
lebih. Konstrain arsitektur "tidak ada audio di paket ini" juga tidak
dilanggar: WAV tetap 100% dihasilkan Tool 2 di luar repo ini; paket ini
hanya memicu (trigger) dan mendokumentasikan flow-nya.

Semua fakta engine di bawah diverifikasi langsung dari kode repo induk
`/home/shendi/self-project/daw_generative` (bukan asumsi) — lihat file
sumber yang dikutip di tiap sub-bagian.

### E1. Referensi baru `skills/midi-orchestration/references/engine-export.md`

**Tujuan.** Belum ada dokumentasi tunggal yang menjelaskan flow export
produksi Tool 1 → Tool 2: server dev mana yang harus hidup, kontrak HTTP
persis, skema `drums` yang diterima ENGINE (beda dari skema Tool 1 v1/v2),
dan batasan lingkungan (soundfont/ffmpeg) yang membuat export bisa gagal di
luar kendali composer. Tanpa referensi ini, "cara export" hanya hidup
sebagai pengetahuan tak tertulis.

**Perubahan konkret.** File referensi **baru**
`skills/midi-orchestration/references/engine-export.md`, isi:

- **Prasyarat.**
  - Server dev engine harus hidup: `npm run dev` dijalankan dari **ROOT
    repo induk** `/home/shendi/self-project/daw_generative` (Vite dev
    middleware — `vite-plugin-render.js` via `vite.config.js` — dev-only,
    tidak ada build/production server terpisah untuk endpoint ini).
  - Port default Vite **5173**, TAPI **auto-increment** bila port terpakai
    — komposer **WAJIB membaca port sesungguhnya dari log terminal**
    `npm run dev`, bukan mengasumsikan 5173.
  - Soundfont GM `FluidR3_GM.sf2` **TIDAK auto-download**. Dicek berurutan
    di: env `NEO_SOUL_SOUNDFONT` → cache
    `~/.cache/hermes-neo-soul-soundfonts/fluidr3/usr/share/sounds/sf2/FluidR3_GM.sf2`
    → path sistem `/usr/share/sounds/sf2/FluidR3_GM.sf2`. Cek dulu mana
    yang ada sebelum mencoba render — tak satu pun ada → status export
    **PENDING** (lihat E4), bukan dipaksakan gagal diam-diam.
  - `fluidsynth` **auto-bootstrap** (unduh `.deb` via `apt-get download`)
    bila absen dari PATH/cache — tak perlu instalasi manual di jalur
    happy-path.
  - `ffmpeg` **wajib ada di PATH** bila `mastering` bukan `false` (default
    `mastering` = `'neo-soul'`, jadi ffmpeg wajib di jalur default).

- **Request.** `POST http://127.0.0.1:<port>/api/render`, header
  `content-type: application/json`, body `{abc, drums?, mastering?}`.
  - `mastering`: `'neo-soul'` (default bila field absen), `'legacy'`, atau
    `false` (tanpa mastering). Boolean **`true` DITOLAK** (422) — berbeda
    dari jalur legacy octet-stream (di luar kontrak JSON ini) yang
    menerima `true` → profil `'legacy'`.
  - Body dibatasi **1 MB** — lebih besar → **413**, ditolak begitu
    akumulasi byte melewati cap (tidak menunggu body selesai diterima).

- **Skema `drums` — skema ENGINE, BUKAN skema Tool 1:**

  ```
  {
    steps_per_bar: 8 | 12 | 16,
    gm_map: { voice: <35..81> },
    base_velocity: { voice: <1..127> },
    swing?: <0.5..0.75>,
    sections: [ { bars: <int >= 1>, pattern: { voice: "x.Xg..." } } ]
  }
  ```

  Karakter pola hanya `x` (hit normal), `X` (aksen), `g` (ghost), `.`
  (off). **Semantik velocity engine berbeda dari Tool 1**: engine — `X` =
  base_velocity **+12** (cap 127), `g` = **35 tetap** (nilai absolut,
  bukan relatif ke base_velocity); Tool 1 `grid_to_midi.py` — `X` =
  base_velocity **×1.2**, `g` = base_velocity **×0.45**. Divergensi ini
  **didokumentasikan, bukan disamakan** — WAV hasil engine adalah artefak
  produksi otoritatif untuk timbre/velocity aktual; output MIDI Tool 1
  tetap alat validasi lokal.

  Format Tool 1 **v2** (pattern list per-bar + `phrase_velocity` +
  top-level `timing`) **TIDAK diterima langsung oleh engine** — wajib
  dikonversi dulu lewat E2. `phrase_velocity` dan `timing` **tidak ikut
  terbawa** ke hasil export (keterbatasan skema engine yang tercatat,
  bukan bug tersembunyi); engine punya penggantinya sendiri: swing grid +
  groove profile `%%pocket`.

- **Cross-check bar.** Total bar `drums` (jumlah `sections[].bars`)
  **WAJIB sama** dengan jumlah bar ABC (dihitung dari not terjauh di semua
  track; bar kosong di ekor tidak terhitung) — mismatch → **422** dengan
  body `{error, abcBars, gridBars}`.

- **`%%pocket`.** Hanya id **`neo-soul-core`** yang valid (satu-satunya
  profil terdaftar di engine). Directive ini **tune-level**: harus muncul
  **sebelum voice pertama aktif** di ABC — kemunculan setelah voice aktif
  **diabaikan diam-diam** (bukan error).

- **Respons sukses.** **200**, body **binary WAV** (`content-type:
  audio/wav`), plus header `X-Conformance-Summary` (JSON satu baris
  ringkas: jumlah bar, total not, jumlah track, velocity-std minimum antar
  track melodis, pct-on-grid maksimum, id pocket + status
  konformansinya — **non-gating**, nilai apa pun tetap 200). Simpan body
  ke `runs/<run>/render.wav`; catat isi `X-Conformance-Summary` di
  `scorecard.md`. `render.wav` **tidak dicommit** (lihat E4).

- **Pra-cek murah tanpa render penuh.** `node scripts/conformance-audit.mjs
  <song.abc> [drums-engine.json]` dijalankan dari root repo induk —
  menjalankan pipeline gate yang sama (normalize → gate → import ABC →
  drum-grid → realize → audit) **tanpa** memanggil `toMidi`/FluidSynth/
  ffmpeg, jauh lebih murah untuk memeriksa apakah ABC/drums akan lolos
  sebelum render sungguhan.

- **Error umum.**
  - **422** — ABC gagal gate, `drums` gagal validasi skema engine, bar
    `drums` ≠ bar ABC, atau `mastering` tak dikenal.
  - **413** — body > 1MB.
  - **500** — kegagalan runtime (soundfont tak ketemu, fluidsynth/ffmpeg
    gagal atau timeout — timeout fluidsynth 120 detik, ffmpeg 60 detik —
    atau hasil render silent yang ditangkap pemeriksaan audibilitas).
  - **Batas keras render**: `maxBars` 512, `maxNotes` 50.000, `maxVoices`
    16, BPM 20-400, durasi maksimum 900 detik (15 menit).

**File yang berubah:**

- **File baru** `skills/midi-orchestration/references/engine-export.md` —
  dokumentasi lengkap di atas.

### E2. Konverter `skills/midi-orchestration/scripts/drums_to_engine.py` (+ `test_drums_to_engine.py`, TDD)

**Tujuan.** Format `drums.json` yang selama ini dihasilkan Tool 1 (v1
pattern-dict, atau v2 pattern-list + `phrase_velocity`/`timing`/
`humanize_velocity`/`label` — lihat
`skills/midi-orchestration/assets/drum-grid-template.json`) tidak diterima
mentah oleh engine (skema berbeda, lihat E1). Tanpa konverter, tiap run
harus menerjemahkan manual dan berisiko salah bentuk → 422 yang
membingungkan di titik render, bukan di titik yang lebih murah untuk
didiagnosis.

**Perubahan konkret.** Script baru
`skills/midi-orchestration/scripts/drums_to_engine.py`, ditulis TDD
(`test_drums_to_engine.py` ditulis lebih dulu, mengikuti pola
`test_abc_to_midi_and_grid.py` yang sudah ada di folder yang sama). Input:
`drums.json` Tool 1 (v1 **atau** v2). Output: JSON skema engine murni
(lihat E1) siap dikirim sebagai field `drums` di body `POST /api/render`.

Aturan konversi:

- **(a)** `pattern` berbentuk **dict** (v1) → satu `section {bars,
  pattern}` apa adanya, tanpa pemecahan.
- **(b)** `pattern` berbentuk **list** (v2, satu dict pattern per bar) →
  dipecah per bar dulu, lalu **bar berurutan yang identik digabung** jadi
  satu `section {bars: N}` (mis. 4 bar: 2 identik lalu 2 beda-beda → 3
  section: `{bars:2}, {bars:1}, {bars:1}`).
- **(c)** Field yang tidak dikenal skema engine (`phrase_velocity`,
  `timing`, `humanize_velocity`, `label`, `title`, `tempo_bpm`,
  `beats_per_bar`, `_comment`, dll.) **dibuang**, dengan **WARNING
  eksplisit ke stderr** menyebut nama field yang hilang dan alasannya
  (bukan silent drop).
- **(d)** `steps_per_bar`, `gm_map`, `base_velocity`, `swing`
  **dipertahankan** apa adanya (sudah kompatibel bentuk dengan skema
  engine).
- **(e)** Validasi sebelum dikirim ke engine (fail cepat, bukan 422
  misterius di titik render): `steps_per_bar` ∈ {8,12,16}; nilai `gm_map`
  35-81; nilai `base_velocity` 1-127; karakter pola hanya `x`/`X`/`g`/`.`.
  Pelanggaran → error Python jelas yang menyebut field & nilai yang salah.

**Test wajib** (`test_drums_to_engine.py`):

1. v2 pattern-list 4 bar (2 bar identik berurutan + 2 bar berbeda) →
   `sections` `[{bars:2}, {bars:1}, {bars:1}]`.
2. v1 pattern-dict → passthrough apa adanya sebagai satu section.
3. Field asing (`phrase_velocity`, `timing`, dst.) di input → dibuang dari
   output **dan** warning tercatat (assert pesan menyebut nama field).
4. `steps_per_bar` di luar {8,12,16} → error tervalidasi (assert raise +
   pesan jelas).
5. Output valid untuk contoh
   `skills/midi-orchestration/assets/drum-grid-template.json` **yang ada
   saat ini** (dijalankan sebagai regression fixture, bukan fixture buatan
   sendiri).

**File yang berubah:**

- **File baru** `skills/midi-orchestration/scripts/drums_to_engine.py`.
- **File baru** `skills/midi-orchestration/scripts/test_drums_to_engine.py`.

### E3. Instrumen selaras engine

**Tujuan.** Instrumentasi yang dipilih Level 1
(`level-01-konsep.md`) dan dinotasikan lewat `%%MIDI program` di Level
14/`abc-notation` bisa menyebut instrumen yang tidak dikenal atau salah
nomor GM di registry engine — render lolos secara teori tapi menghasilkan
timbre yang tidak dimaksud composer (mis. maksud Jazz Guitar tapi kena
Clean Electric Guitar karena nomor program keliru).

**Perubahan konkret.**

- Tabel baru di `engine-export.md` (E1) — **registry kurasi engine** (id →
  nama → GM program):

  | id | Nama | GM program |
  |---|---|---|
  | sax | Tenor Sax | 66 |
  | piano | Acoustic Piano | 0 |
  | guitar | Jazz Guitar | 26 |
  | bass | Acoustic Bass | 32 |
  | rhodes | Rhodes E-Piano | 4 |
  | trumpet | Trumpet | 56 |
  | vibraphone | Vibraphone | 11 |
  | guitar-clean | Clean Electric Guitar | 27 |
  | bass-finger | Finger Bass | 33 |
  | synth-bass | Synth Bass | 38 |
  | synth-lead | Soft Synth Lead | 81 |
  | jazz-kit | — (drum kit) | kanal drum GM 10, note number perkusi 35-81 (bukan program) |

  Plus **palet siap pakai** engine (kombinasi id di atas per track):
  `neo-soul-warm`, `jazz-cafe`, `lofi-dusty`, `modern-chill`.

  Render engine sesungguhnya menerima **GM 0-127 penuh** (soundfont
  FluidR3 general-purpose, tidak dibatasi ke 12 id di atas) — registry ini
  adalah **menu default yang direkomendasikan**, bukan pagar keras. GM
  lain di luar tabel boleh dipakai, hanya dengan **justifikasi eksplisit**
  ditulis di artefak `01-brief.md`/Level 1.

- **Gate baru** di `skills/jazz-composition/references/level-01-konsep.md`:
  instrumentasi run **WAJIB** dipilih dari registry engine di atas, atau
  disertai justifikasi eksplisit bila memakai GM lain. ABC final (Level
  14/`abc-notation`) **WAJIB** menulis `%%MIDI program N` eksplisit per
  voice **sesuai nomor di tabel** — jangan mengandalkan name-matching
  otomatis engine (yang hanya menebak dari keyword `sax/bass/guitar/piano`
  dan jatuh ke piano untuk selainnya) sebagai satu-satunya jalur penentuan
  timbre.

- **Selaraskan `PROGRAM` map**
  `skills/midi-orchestration/scripts/abc_to_midi.py` (dipakai Tool 1 untuk
  MIDI validasi lokal) dengan registry engine di atas — prinsip: **keyword
  yang sama menghasilkan nomor program yang sama** dengan registry engine,
  supaya preview MIDI Tool 1 dan hasil WAV engine tidak diam-diam berbeda
  timbre untuk instrumen yang sama. Perubahan konkret pada dict `PROGRAM`
  yang sudah ada:

  | Keyword | Nilai lama | Nilai baru (selaras registry) |
  |---|---|---|
  | `sax` | 65 | **66** |
  | `guitar` | 27 | **26** |
  | `bass` | 33 | **32** |
  | `vibraphone` | *(belum ada)* | **11** (entri baru) |
  | `synth-lead` | *(belum ada)* | **81** (entri baru) |

  `trumpet` (56), `rhodes` (4), `piano` (0) sudah selaras, tidak berubah.
  Keyword lain di `PROGRAM` yang tidak punya padanan langsung di registry
  engine (`horns`:61, `upright`:32, `strings`:48, `pad`:89) **dipertahankan
  apa adanya** — di luar cakupan penyelarasan ini (tidak dikurasi engine,
  bukan berarti salah). Nilai persis final tetap diputuskan penulis plan
  implementasi (bukan dikunci di spec ini); test guard yang sudah ada di
  `test_abc_to_midi_and_grid.py` untuk keyword yang berubah wajib
  diperbarui mengikuti nilai baru, bukan dibiarkan gagal.

**File yang berubah:**

- `skills/midi-orchestration/references/engine-export.md` — tabel registry
  + palet instrumen engine (bagian dari file baru E1).
- `skills/jazz-composition/references/level-01-konsep.md` — gate
  instrumentasi dari registry engine + kewajiban `%%MIDI program`
  eksplisit.
- `skills/midi-orchestration/scripts/abc_to_midi.py` — penyelarasan 3
  nilai + 2 entri baru di `PROGRAM` map.
- `skills/midi-orchestration/scripts/test_abc_to_midi_and_grid.py` — test
  guard diupdate mengikuti nilai baru.

### E4. Wiring export ke workflow

**Tujuan.** Tanpa titik wiring eksplisit di orchestrator, langkah export
(E1-E3) hanya jadi dokumentasi yang bisa dilewatkan — perlu langkah
konkret di alur "piece dianggap selesai" yang sudah ada (Tahap akhir/
`## Penilaian` di `SKILL.md`, Level 14 di referensinya) yang menjalankan
konverter → pra-cek → render sungguhan, dengan jalur keluar jujur
(`PENDING`) saat lingkungan tidak lengkap, alih-alih memaksakan gagal atau
diam-diam dilewati.

**Perubahan konkret.**

- `skills/jazz-composition/SKILL.md`, **section baru di akhir file**
  (setelah `## Sebelum menganggap sebuah piece selesai`, yaitu setelah
  checklist fail-closed pra-L3 dari D5 terpenuhi): **`## Export produksi
  (Tool 2 — engine daw_generative)`**, berisi urutan langkah:
  1. Jalankan `skills/midi-orchestration/scripts/drums_to_engine.py` atas
     `drums.json` run (bila run punya drum) → hasilkan
     `drums-engine.json`.
  2. Bila repo induk `daw_generative` tersedia di mesin: pra-cek murah
     `node scripts/conformance-audit.mjs <song.abc> [drums-engine.json]`
     dari root repo induk.
  3. `POST /api/render` (lihat E1 untuk kontrak lengkap) ke
     `http://127.0.0.1:<port>` — port dibaca dari log `npm run dev`,
     bukan diasumsikan 5173.
  4. Simpan body respons ke `runs/<run>/render.wav`; catat header
     `X-Conformance-Summary` dan profil `mastering` yang dipakai di
     `scorecard.md` (lihat perubahan `scorecard-template.md` di bawah).
  5. Bila server dev/soundfont/fluidsynth/ffmpeg **tidak tersedia** di
     lingkungan yang menjalankan run: status export dicatat **PENDING** +
     alasan konkret (mis. "soundfont tak ditemukan di 3 path yang
     dicek") — **run itu sendiri TIDAK dianggap gagal**; `output.mid`
     (Tool 1) tetap ada dan cukup untuk L3 telinga manusia, tapi WAV hasil
     engine tetap **artefak produksi otoritatif** begitu lingkungan
     tersedia.

  Referensi silang ditambahkan di
  `skills/jazz-composition/references/level-14-detail.md` — **nama file
  ini terverifikasi via `ls` sebelum spec ini ditulis**: file yang
  sebenarnya ada di `skills/jazz-composition/references/` adalah
  `level-14-detail.md`, **bukan** `level-14-review.md`; `14-review.md`
  hanyalah nama **artefak run** (output Tahap 15 di `SKILL.md`), sedangkan
  file **referensi skill** yang dibaca orchestrator untuk Level 14 adalah
  `level-14-detail.md`. Referensi silang ini menunjuk balik ke section
  export produksi di atas sebagai langkah setelah semua gate/checklist
  Level 14 terpenuhi.

- `.gitignore` di root repo ini (`music-composition-skill` — tempat folder
  `runs/` benar-benar hidup dan tercatat git, dicek langsung: `runs/<run>/`
  sudah tracked git saat ini): tambah baris `runs/*/render.wav` — WAV
  tidak dicommit (ukurannya besar, dan merupakan artefak Tool 2, bukan
  sumber kebenaran yang perlu di-diff/di-review lewat git).

- `skills/jazz-composition/references/scorecard-template.md`: tambah
  bagian baru **"Export"** (ditempatkan setelah `Level 14 — Detail Low
  Level`, sebelum `L3 (telinga)` — sejalan dengan penempatan bagian "L2
  global" dari D1-D4 di titik yang sama), berisi field:

  | Field | Isi |
  |---|---|
  | Status | selesai / PENDING + alasan |
  | Path | `runs/<run>/render.wav` (bila ada) |
  | Conformance summary | isi `X-Conformance-Summary` apa adanya |
  | Mastering | profil yang dipakai (`neo-soul` / `legacy` / `false`) |

**File yang berubah:**

- `skills/jazz-composition/SKILL.md` — section baru `## Export produksi
  (Tool 2 — engine daw_generative)`.
- `skills/jazz-composition/references/level-14-detail.md` — referensi
  silang ke section export produksi.
- `skills/jazz-composition/references/scorecard-template.md` — bagian baru
  "Export".
- `.gitignore` (root repo ini) — baris `runs/*/render.wav`.

## Uji penerimaan

1. **Semua anchor/cross-ref valid + istilah konsisten.** Setiap file yang
   dirujuk oleh nama di spec ini benar-benar ada di path yang disebut
   (dicek lewat `ls` sebelum spec ini ditulis — lihat laporan akhir);
   `L2-rubrik`/`L2-blind`/`L2-cliche` dieja persis sama di setiap file yang
   menyebutnya; link antar-file (mis. rujukan `level-11-*.md` ke
   `instrumental-transitions.md` §1) menunjuk ke bagian yang benar-benar
   ada di file target.
2. **Satu run komposisi baru end-to-end**, memakai skill ter-update (brief
   baru — bukan salah satu run lama), menunjukkan semua gate baru bekerja
   di artefak yang dihasilkan:
   - tabel transisi 3-fase (preparation/boundary event/after-effect) di
     artefak Level 11, dengan kutipan model 4-tahap;
   - tabel dinamika observabel (bukan persentase) + field micro-apex terisi
     di artefak Level 13;
   - tabel device bass per transisi chord di artefak Level 8, dengan
     proporsi chromatic approach ≤1/3 dan relasi bass-kick per section
     tercatat;
   - micro-improvisation map di artefak Level 10 (baik piece itu punya solo
     section atau tidak);
   - intro dengan ≥1 kejadian performatif tercatat di artefak Level 12, dan
     pertimbangan tertulis opsi rekontekstualisasi sebelum ending dipilih;
   - ≥3 comping cell terpetakan ke napas lead di artefak Level 7;
   - tabel cek tempo (BPM brief eksplisit + cek terhadap tabel band) muncul
     di artefak Level 4, 5, 8, dan 9;
   - 4 kriteria blocker terisi di scorecard "L2 global";
   - `L2-blind` dijalankan, hasil (benar/salah) dicatat jujur;
   - `L2-cliche` dijalankan, semua temuan mendapat respons (revisi atau
     justifikasi audible);
   - bagian "Bukti revisi" terisi ≥1 pasangan before/after yang terhubung
     ke temuan nyata L1/L2.
   `L3 (telinga)` pada run ini **dibiarkan kosong**, menunggu user — bukan
   diasumsikan lolos karena L1/L2 (termasuk L2-blind/L2-cliche) hijau.
3. **Export produksi nyata via engine, untuk run baru yang sama di atas.**
   Agent menghidupkan `npm run dev` dari root repo induk `daw_generative`,
   membaca port sesungguhnya dari log terminal (bukan mengasumsikan 5173),
   dan mengecek ketersediaan soundfont `FluidR3_GM.sf2` di tiga path yang
   didokumentasikan (E1) **sebelum** mencoba render. Target: **WAV nyata**
   tersimpan di `runs/<run>/render.wav` — usahakan sampai tercapai, bukan
   berhenti di percobaan pertama yang gagal karena hal yang bisa
   diperbaiki (mis. server belum jalan). Bila lingkungan benar-benar tidak
   lengkap (soundfont/fluidsynth/ffmpeg tak tersedia sama sekali di
   mesin), status export **PENDING** dicatat **jujur** di `scorecard.md`
   dengan alasan konkret — bukan diklaim selesai. Kriteria lolos konkret:
   - `render.wav` ada di run folder **dan tidak ke-commit** (cek `git
     status`/`.gitignore` sesuai E4);
   - `X-Conformance-Summary` dan profil `mastering` tercatat di bagian
     "Export" `scorecard.md`;
   - instrumentasi run memakai id dari registry instrumen engine (E3)
     **dan** ABC final menulis `%%MIDI program N` eksplisit per voice
     sesuai tabel registry — bukan mengandalkan name-matching.

## Risiko & tradeoff

| Risiko/tradeoff | Detail | Mitigasi |
|---|---|---|
| Biaya token L2 naik | `L2-blind` dan `L2-cliche` masing-masing butuh minimal 1 subagent reviewer segar tambahan per run, plus authoring 2 distractor arc emosional yang meyakinkan. | Diterima sadar sebagai biaya Gelombang 3 — keduanya menyasar celah spesifik (arc tak terverifikasi, cliché tak terdeteksi) yang Gelombang 1-2 tidak menutup; tidak dijalankan di luar titik pra-L3 (sekali per run, bukan berulang). |
| Distractor `L2-blind` terlalu mudah/susah ditebak | Distractor yang terlalu jauh dari arc asli (mis. beda genre) membuat tebakan trivial; terlalu mirip membuat tebakan jadi lotre murni, bukan sinyal arc benar-benar terbaca. | Aturan authoring distractor: **"berbeda arah arc, bukan berbeda genre"** — ketiga opsi harus masuk akal untuk gaya/instrumentasi yang sama, hanya arah emosionalnya yang berbeda. |
| Register cliché (`cliche-register.md`) jadi checklist mati | Daftar statis berisiko dihafal lalu di-"tick" tanpa dipikirkan, atau jadi larangan absolut yang mematikan device yang sebetulnya sah dipakai sadar. | Tiap entri **wajib** punya kolom jalur reinterpretasi yang menyelamatkan — cliché bukan larangan mutlak, tapi sinyal "pakai sadar dengan reinterpretasi atau revisi", konsisten dengan gate C2/C3/C5/C6 yang jadi jalur reinterpretasinya. |
| "Bukti revisi" dipalsukan sebagai revisi kosmetik | Composer bisa menulis pasangan before/after yang trivial (mis. ganti satu artikulasi tak penting) hanya untuk memenuhi syarat administratif. | Syarat eksplisit: bukti revisi harus **terhubung ke temuan nyata** L1/L2/L2-blind/L2-cliche — bukan revisi berdiri sendiri yang tidak menjawab temuan spesifik mana pun; reviewer L2 berikutnya bisa menolak pasangan before/after yang tidak menjawab temuan yang dicatat. |
| Gate baru menambah panjang setiap artefak level yang tersentuh | 8 dari 14 level (7, 8, 10, 11, 12, 13, plus 4/5/9 untuk tempo) kini punya tabel/field wajib tambahan — risiko artefak jadi lebih berat dibaca/ditulis. | Diterima sadar: seluruh gate ini menutup celah yang sudah terbukti nyata di run lama (device generik lolos tanpa gate) — biaya verbosity dianggap lebih murah daripada biaya rilis piece yang terasa template. |
| Export kehilangan `phrase_velocity`/`timing` per-role | Skema `drums` ENGINE (E1) tidak punya field ini — frase dinamika halus & micro-timing per-role yang dirancang di Tool 1 tidak ikut terbawa ke WAV produksi. | Diterima sadar sebagai keterbatasan format, bukan bug tersembunyi: didokumentasikan eksplisit di E1/E2 (WARNING stderr di titik konversi). Engine punya penggantinya sendiri (swing grid + groove profile `%%pocket neo-soul-core`) yang tidak identik tapi menutup sebagian celah ekspresif yang sama. |
| Dependensi lingkungan (soundfont/ffmpeg/server dev) | Export bisa **PENDING** di mesin yang tidak punya `FluidR3_GM.sf2`/`ffmpeg` terpasang atau repo induk `daw_generative` tak ter-checkout — di luar kendali paket ini (Tool 1). | Fallback eksplisit di E4: status PENDING dicatat jujur + alasan, run tidak dianggap gagal; `output.mid` (Tool 1) tetap cukup untuk L3 telinga sementara menunggu lingkungan lengkap; uji penerimaan (poin 3) tetap mewajibkan **usaha nyata** mencapai WAV, bukan PENDING sebagai jalan pintas default. |
| Dua semantik velocity `X`/`g` berbeda (Tool 1 vs engine) | `grid_to_midi.py` (Tool 1): `X`=×1.2, `g`=×0.45 (relatif base_velocity). Engine: `X`=+12 (absolut, cap 127), `g`=35 tetap (absolut). Preview MIDI lokal dan WAV produksi bisa terdengar berbeda dinamika drum-nya untuk pola yang sama. | Didokumentasikan eksplisit di E1 sebagai divergensi yang diketahui, bukan disamakan paksa (menyamakan berarti mengubah kode engine, di luar wewenang paket ini) — **WAV engine dinyatakan otoritatif** untuk timbre/dinamika aktual; Tool 1 MIDI tetap alat validasi struktural (bar/not/tempo), bukan sumber kebenaran dinamika final. |
| `render.wav` membengkakkan run folder | File audio WAV tak terkompresi bisa puluhan MB per run — berkali lipat lebih besar dari seluruh artefak teks run lainnya digabung. | `.gitignore` (E4) mengecualikan `runs/*/render.wav` dari commit — disk lokal boleh menyimpannya (dibutuhkan untuk didengarkan), tapi repo git tidak ikut membengkak; scorecard tetap mencatat path & conformance summary sebagai jejak tanpa perlu menyimpan biner di git. |

## Ringkasan file yang berubah (rekap lintas komponen)

- `skills/jazz-composition/SKILL.md` — C5 (pointer 12), C8e (ground rule
  tempo), D1 (fail-closed §Penilaian), D2 (prosedur L2-blind), D3 (prosedur
  L2-cliche), D4 (Tahap 15, bukti revisi), D5 (checklist pra-L3), **E4**
  (section baru `## Export produksi (Tool 2 — engine daw_generative)`).
- `skills/jazz-composition/references/level-01-konsep.md` — **E3** (gate
  instrumentasi dari registry engine + `%%MIDI program` eksplisit).
- `skills/jazz-composition/references/level-07-comping-voicing.md` — C6.
- `skills/jazz-composition/references/level-08-bass.md` — C3.
- `skills/jazz-composition/references/level-10-improvisasi.md` — C4.
- `skills/jazz-composition/references/level-11-interlude-shout-transisi.md`
  — C1.
- `skills/jazz-composition/references/level-12-intro-ending.md` — C5.
- `skills/jazz-composition/references/level-13-dinamika-dramaturgi.md` — C2.
- `skills/jazz-composition/references/level-14-detail.md` — **E4**
  (referensi silang ke section export produksi).
- `skills/jazz-composition/references/scorecard-template.md` — D1, D2, D3,
  D4 (bagian "L2 global" baru), **E4** (bagian "Export" baru).
- `skills/jazz-composition/references/human-ear-protocol.md` — D5.
- `skills/jazz-composition/references/cliche-register.md` — **file baru**,
  D3.
- `skills/RED-FLAGS.md` — D4 (baris "first draft dianggap final").
- `skills/arrangement/SKILL.md` — C5 (§Level 12), C6 (§Level 7).
- `skills/vibes-mood/references/reasoning-theory.md` — C7 (Modul 4 Lensa
  3), C8a (tabel BPM band).
- `skills/melody-design/SKILL.md` — C8b (gate BPM eksplisit).
- `skills/melody-design/references/rubric.md` — C8b (kriteria baru).
- `skills/advanced-melody/SKILL.md` — C8b (pointer).
- `skills/harmony/SKILL.md` — C8c (durasi absolut per chord).
- `skills/groove-rhythm/references/groove-meter.md` — C8d (breakpoint
  swing ratio).
- `skills/midi-orchestration/references/engine-export.md` — **file baru**,
  E1 + E3 (tabel registry instrumen + palet engine).
- `skills/midi-orchestration/scripts/drums_to_engine.py` — **file baru**,
  E2 (konverter drums.json Tool 1 → skema engine).
- `skills/midi-orchestration/scripts/test_drums_to_engine.py` — **file
  baru**, E2 (test TDD konverter).
- `skills/midi-orchestration/scripts/abc_to_midi.py` — **E3** (penyelarasan
  `PROGRAM` map: sax/guitar/bass + entri baru vibraphone/synth-lead).
- `skills/midi-orchestration/scripts/test_abc_to_midi_and_grid.py` — **E3**
  (test guard `PROGRAM` map diupdate mengikuti nilai baru).
- `.gitignore` (root repo ini) — **E4** (baris `runs/*/render.wav`).

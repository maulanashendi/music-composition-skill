# Spec: Wave 2-3 — Enforcement Gates dan Gigi Penilaian

**Tanggal**: 2026-07-14
**Status**: desain final untuk implementasi (Gelombang 2-3 dari rangkaian 3 gelombang)

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

**Seluruh perubahan Gelombang 2-3 di spec ini adalah perubahan DOKUMEN
SAJA — nol perubahan kode Python.** Ini keputusan YAGNI yang sadar: semua
komponen di bawah adalah instruksi prosa yang dieksekusi oleh agent LLM yang
mengikuti `SKILL.md`, bukan logika yang perlu diotomasi di script. Konsekuensi
langsung: verifikasi implementasi nanti = **konsistensi teks, anchor, dan
cross-reference** antar file (nama file dirujuk benar-benar ada, istilah
dipakai konsisten, gate bisa diikuti langkah demi langkah oleh agent) —
**bukan** unit test Python.

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

**Out of scope (jangan dikerjakan sebagai bagian spec ini):**

- Perubahan kode Python apa pun (`*.py` di `skills/*/scripts/`) — nol
  perubahan mekanis, murni dokumen.
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

## Risiko & tradeoff

| Risiko/tradeoff | Detail | Mitigasi |
|---|---|---|
| Biaya token L2 naik | `L2-blind` dan `L2-cliche` masing-masing butuh minimal 1 subagent reviewer segar tambahan per run, plus authoring 2 distractor arc emosional yang meyakinkan. | Diterima sadar sebagai biaya Gelombang 3 — keduanya menyasar celah spesifik (arc tak terverifikasi, cliché tak terdeteksi) yang Gelombang 1-2 tidak menutup; tidak dijalankan di luar titik pra-L3 (sekali per run, bukan berulang). |
| Distractor `L2-blind` terlalu mudah/susah ditebak | Distractor yang terlalu jauh dari arc asli (mis. beda genre) membuat tebakan trivial; terlalu mirip membuat tebakan jadi lotre murni, bukan sinyal arc benar-benar terbaca. | Aturan authoring distractor: **"berbeda arah arc, bukan berbeda genre"** — ketiga opsi harus masuk akal untuk gaya/instrumentasi yang sama, hanya arah emosionalnya yang berbeda. |
| Register cliché (`cliche-register.md`) jadi checklist mati | Daftar statis berisiko dihafal lalu di-"tick" tanpa dipikirkan, atau jadi larangan absolut yang mematikan device yang sebetulnya sah dipakai sadar. | Tiap entri **wajib** punya kolom jalur reinterpretasi yang menyelamatkan — cliché bukan larangan mutlak, tapi sinyal "pakai sadar dengan reinterpretasi atau revisi", konsisten dengan gate C2/C3/C5/C6 yang jadi jalur reinterpretasinya. |
| "Bukti revisi" dipalsukan sebagai revisi kosmetik | Composer bisa menulis pasangan before/after yang trivial (mis. ganti satu artikulasi tak penting) hanya untuk memenuhi syarat administratif. | Syarat eksplisit: bukti revisi harus **terhubung ke temuan nyata** L1/L2/L2-blind/L2-cliche — bukan revisi berdiri sendiri yang tidak menjawab temuan spesifik mana pun; reviewer L2 berikutnya bisa menolak pasangan before/after yang tidak menjawab temuan yang dicatat. |
| Gate baru menambah panjang setiap artefak level yang tersentuh | 8 dari 14 level (7, 8, 10, 11, 12, 13, plus 4/5/9 untuk tempo) kini punya tabel/field wajib tambahan — risiko artefak jadi lebih berat dibaca/ditulis. | Diterima sadar: seluruh gate ini menutup celah yang sudah terbukti nyata di run lama (device generik lolos tanpa gate) — biaya verbosity dianggap lebih murah daripada biaya rilis piece yang terasa template. |

## Ringkasan file yang berubah (rekap lintas komponen)

- `skills/jazz-composition/SKILL.md` — C5 (pointer 12), C8e (ground rule
  tempo), D1 (fail-closed §Penilaian), D2 (prosedur L2-blind), D3 (prosedur
  L2-cliche), D4 (Tahap 15, bukti revisi), D5 (checklist pra-L3).
- `skills/jazz-composition/references/level-07-comping-voicing.md` — C6.
- `skills/jazz-composition/references/level-08-bass.md` — C3.
- `skills/jazz-composition/references/level-10-improvisasi.md` — C4.
- `skills/jazz-composition/references/level-11-interlude-shout-transisi.md`
  — C1.
- `skills/jazz-composition/references/level-12-intro-ending.md` — C5.
- `skills/jazz-composition/references/level-13-dinamika-dramaturgi.md` — C2.
- `skills/jazz-composition/references/scorecard-template.md` — D1, D2, D3,
  D4 (bagian "L2 global" baru).
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

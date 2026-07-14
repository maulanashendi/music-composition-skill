# Spec: Wave 1 — Seleksi Kandidat, Drum Engine v2, Gate Klaim-vs-Notasi

**Tanggal**: 2026-07-14
**Status**: desain final untuk implementasi (Gelombang 1 dari rangkaian 3 gelombang)

## Latar

Kritik eksternal atas output run `runs/2026-07-14-doubt-to-acceptance/`
diverifikasi oleh dua audit internal pada 2026-07-14. Tiga akar masalah
terkonfirmasi:

1. **Generate-then-defend, bukan generate-lalu-pilih.** Workflow 14-level di
   `skills/jazz-composition/SKILL.md` bersifat linear: setiap level menulis
   satu artefak dan melanjut. Tidak ada level yang diminta menghasilkan lebih
   dari satu kandidat, sehingga keputusan medioker yang muncul di awal
   diwariskan ke level berikutnya lalu dibela ("self-justification loop")
   alih-alih dibandingkan dengan alternatif. Ironisnya rubrik Level 1 di
   `skills/vibes-mood/references/rubric.md` sudah menuntut "minimal dua
   konsep berbeda secara struktural dipertimbangkan" — tapi tidak ada
   instruksi generasi manapun yang pernah memerintahkan pembuatan dua konsep
   itu, jadi rubriknya menagih sesuatu yang prosesnya sendiri tidak pernah
   menghasilkan.
2. **Drum engine men-tile pola identik.** `skills/midi-orchestration/scripts/grid_to_midi.py`
   melakukan `for _ in range(section["bars"]): ... section["pattern"]` — pola
   1-bar yang sama diulang persis di setiap bar section, dibumbui hanya oleh
   humanize velocity acak per-hit. Ini bertentangan langsung dengan doktrin
   paket sendiri di `skills/groove-rhythm/references/advanced-microtiming.md`
   §1: "Microtiming is ... not indiscriminate randomization." Ini sumber
   utama rasa "generative loop" pada drum.
3. **Klaim teori di artefak tidak cocok notasi aktual.** Berulang kali:
   motif diklaim 4-not padahal secara pitch hanya 3; arpeggio chord-tone
   dilabeli "outside"; `Abmaj7`/`Ebmaj7` yang diatonik di key minor dilabeli
   modal interchange/borrowed; klaim voice-leading top-note tidak cocok
   voicing yang benar-benar tertulis. Ini bottleneck L2 dua run berturut-
   turut: Level 7 (voice-leading) skor 0 dua kali, Level 4 (outside-mislabel)
   dua kali.

Scope spec ini adalah **Gelombang 1 (akar masalah) saja**. Wiring enforcement
level-per-level yang lebih granular (transisi, micro-apex, bass, tempo) adalah
Gelombang 2, dan scorecard blocker + gate Level 4–6 adalah Gelombang 3 —
keduanya spec terpisah, tidak dibahas di sini.

## Scope

**In scope (Gelombang 1):**

- Komponen 1 — mekanisme kandidat→seleksi independen di 4 level ber-leverage
  (Konsep, Arsitektur, Harmoni, Melodi).
- Komponen 2 — drum engine v2: pattern per-bar, phrase velocity, timing
  offset relasional per-role, lint mekanis anti-tile-identik.
- Komponen 3 — script fakta-notasi (`notation_facts.py`) dan gate
  klaim-vs-notasi di DoD Level 3, 4, 7.

**Out of scope (gelombang terpisah, jangan dikerjakan di sini):**

- **Gelombang 2** — wiring enforcement per level yang lebih granular
  (transisi, micro-apex, bass, tempo sebagai gate eksplisit di level lain
  selain 1–4/9).
- **Gelombang 3** — scorecard blocker (skor L2 tertentu memblokir lanjut ke
  level berikutnya) dan gate baru khusus Level 4–6.
- Render audio dalam bentuk apa pun — lihat konstrain arsitektur di bawah.

## Konstrain arsitektur

- Paket ini adalah **Tool 1** ("otak") dalam arsitektur 2-tools: output-nya
  notasi ABC, `drums.json`, dan MIDI *validasi* (via script Python lokal,
  bukan audio). **Tidak ada render audio di paket ini** — audio adalah
  **Tool 2**, dijalankan lewat HTTP `POST /api/render` di luar repo ini.
  Ketiga komponen di bawah tidak boleh menambah dependensi audio/DAW apa pun.
- Semua mekanisme baru harus bisa dijalankan oleh agent LLM yang mengikuti
  `SKILL.md` — instruksinya adalah prosa/prosedur yang dibaca dan dieksekusi
  agent, bukan otomasi tersembunyi. Setiap mekanisme yang berasumsi "spawn
  subagent segar tersedia" (protokol seleksi Komponen 1, reviewer L2) wajib
  punya fallback eksplisit untuk environment yang tidak bisa spawn subagent
  (mis. composer pack di browser AI tanpa Claude Code) — lihat Komponen 1,
  aturan 5.
- Perubahan pada `grid_to_midi.py` harus backward compatible: spec
  `drums.json` v1 (existing, termasuk dua run lama di `runs/`) harus tetap
  ter-render identik bit-untuk-bit pada notes/velocity/timing (kecuali
  warning lint baru yang murni informasional, tidak mengubah output MIDI).

## Desain per komponen

### Komponen 1 — Mekanisme kandidat→seleksi

**Tujuan.** Mengganti generate-then-defend dengan generate-kandidat →
seleksi-independen, **hanya** di 4 level ber-leverage tinggi: Level 1
(konsep), Level 2 (bentuk/arsitektur), Level 3 (harmoni), Level 4
(motif/melodi). Level lain tetap single-shot — menghindari ledakan
paperwork 14 level × 3 kandidat.

**Aturan generasi per level:**

- **Level 1 — Konsep** (`skills/jazz-composition/references/level-01-konsep.md`):
  tambahkan field wajib baru **aesthetic thesis** — 1 kalimat ide musikal
  spesifik yang bisa didengar, bukan daftar atribut genre. Contoh baik:
  "satu nada yang awalnya terasa salah tak pernah dihilangkan; di akhir,
  harmoni di bawahnya berubah sehingga nada yang sama terasa diterima."
  Plus **2 konsep kandidat berbeda struktural** — ini akhirnya memberi
  instruksi generasi untuk tuntutan rubrik `vibes-mood` yang sudah ada
  ("minimal dua konsep berbeda secara struktural").
- **Level 2 — Bentuk** (`skills/jazz-composition/references/level-02-arsitektur.md`):
  **≥2 alternatif bentuk** sebelum memilih (mis. through-composed vs.
  return-with-recontext), masing-masing 2-3 kalimat + risiko statis/simetris.
- **Level 3 — Harmoni** (`skills/jazz-composition/references/level-03-harmoni.md`):
  progresi utama + **1 alternatif lebih sederhana** + **1 alternatif lebih
  berani**, masing-masing dengan exact chord symbols per bar.
- **Level 4 — Melodi** (`skills/jazz-composition/references/level-04-melodi.md`):
  **3 kandidat motif**, masing-masing wajib ditulis sebagai notasi ABC 1-2
  bar + fakta objektif: jumlah pitch aktual (rest bukan pitch), interval
  aktual antar nada berurutan dalam semitone + nama interval, relasi tiap
  nada ke chord (chord-tone / tension / outside).

**Protokol seleksi (anti self-justification)** — didokumentasikan lengkap di
file baru `skills/jazz-composition/references/candidate-selection-protocol.md`,
dirujuk dari keempat file level di atas dan dari `SKILL.md`:

1. Generator menghasilkan kandidat sebagai **material telanjang**: notasi/
   struktur + fakta objektif + maksimal 1 kalimat intent. **Dilarang**
   menulis pembelaan/rasionalisasi per kandidat di tahap ini.
2. Seleksi dilakukan oleh **subagent segar** (selector) yang menerima
   **hanya**: brief, aesthetic thesis, material kandidat, dan fakta objektif.
   Selector **tidak** menerima preferensi/urutan favorit generator — pola
   yang sama dengan aturan reviewer L2 yang sudah ada di `SKILL.md`
   ("Reviewer segar (L2)"), diperluas ke titik seleksi, bukan hanya
   penilaian akhir.
3. Selector memilih 1 pemenang + alasan berbasis **efek yang akan terdengar**
   (bukan nama teori), dan boleh menyarankan **graft** — mengambil elemen
   dari kandidat lain ke pemenang.
4. Hasil seleksi dicatat di run folder:
   - kandidat ditulis ke artefak `NN-<level>-candidates.md` (mis.
     `01-konsep-candidates.md`, `02-arsitektur-candidates.md`,
     `03-harmoni-candidates.md`, `04-melodi-candidates.md`);
   - verdict selector ditulis di **bagian akhir artefak yang sama** (bukan
     file terpisah lagi);
   - artefak utama level tersebut (`01-brief.md`, `02-form.md`,
     `03-harmony.md`, `04-melody.abc`) memakai pemenang seleksi, bukan
     rata-rata atau gabungan tanpa keputusan eksplisit.
5. **Fallback tanpa subagent** (mis. composer pack di browser AI tanpa
   Claude Code): self-selection oleh agent yang sama diizinkan, **tapi**
   wajib pre-mortem — tulis 1 kelemahan konkret tiap kandidat **sebelum**
   memilih, dan kalimat pemilihan pemenang harus secara eksplisit
   mereferensikan kelemahan itu (mis. "dipilih kandidat B meski
   kelemahannya X, karena kelemahan A dan C lebih berat untuk brief ini").

**Kontrak artefak ramping.** Berlaku khusus untuk keempat artefak
`*-candidates.md` di atas — **bukan** kontrak 11-field penuh yang dipakai
artefak level lain:

| Field | Isi |
|---|---|
| Objective | Efek audible yang dikejar (1-2 kalimat) |
| Immutable constraints | Batasan dari brief yang tidak boleh dilanggar kandidat manapun |
| Assumptions | Asumsi yang diambil generator saat brief tidak eksplisit |
| Kandidat | Material telanjang tiap kandidat (lihat aturan per level di atas) |
| Selected + alasan | Pemenang + alasan berbasis efek terdengar (bukan nama teori) |
| Exact artifact | Rujukan ke artefak utama level ini yang memakai pemenang |
| Unresolved/confidence | Hal yang masih terbuka + tingkat keyakinan seleksi |

**File yang berubah:**

- `skills/jazz-composition/SKILL.md` — Tahap 1–4 di "Workflow praktis dari
  nol" ditambah rujukan ke protokol seleksi; bagian "Reviewer segar (L2)"
  ditambah catatan bahwa Level 1–4 kini juga melalui seleksi-terpisah
  sebelum L2 menilai artefak akhirnya.
- **File baru** `skills/jazz-composition/references/candidate-selection-protocol.md`
  — protokol lengkap di atas + format artefak ramping.
- `skills/jazz-composition/references/level-01-konsep.md` — tambah
  requirement aesthetic thesis + 2 konsep kandidat ke bagian "Output level
  ini" dan gate "ask, don't guess".
- `skills/jazz-composition/references/level-02-arsitektur.md` — tambah
  requirement ≥2 alternatif bentuk.
- `skills/jazz-composition/references/level-03-harmoni.md` — tambah
  requirement progresi utama + 2 alternatif (sederhana/berani).
- `skills/jazz-composition/references/level-04-melodi.md` — tambah
  requirement 3 kandidat motif dengan fakta objektif.
- `skills/jazz-composition/references/run-folder-protocol.md` — tambah
  nama artefak `NN-<level>-candidates.md` ke struktur folder dan penjelasan
  kapan artefak ini muncul (hanya Level 1–4).
- `skills/vibes-mood/references/rubric.md` — **tidak berubah**: tuntutan
  "minimal dua konsep" yang sudah ada di sana kini terpenuhi oleh instruksi
  generasi Level 1 di atas.

### Komponen 2 — Drum engine v2

**Format `drums.json` v2 (backward compatible dengan v1).**

`section.pattern` kini boleh berupa dua bentuk:

- **(a) Legacy** — dict tunggal instrumen→string 16-step (bentuk yang
  dipakai `drum-grid-template.json` saat ini). Perilaku tidak berubah:
  di-tile identik ke semua bar section, seperti sekarang.
- **(b) Baru** — `list` of dict, **panjang list harus sama persis dengan
  `section.bars`**, tiap elemen list adalah pattern satu bar (bar 1, bar 2,
  dst., berurutan). Validasi: jika panjang list ≠ `section.bars`, script
  wajib berhenti dengan error yang jelas (bukan silently truncate/pad).

Field opsional baru per section:

- **`phrase_velocity`** — list `float` multiplier per bar, panjang harus
  sama dengan `section.bars`. Dikalikan ke velocity **semua** hit di bar
  itu setelah accent/ghost diterapkan — velocity berbentuk frase (naik-
  turun terarah), bukan jitter acak per-hit. Bila field ini absen di suatu
  section, default `1.0` untuk semua bar (no-op, output identik v1).

Field opsional baru top-level:

- **`timing`** — map `role → offset_ms` (mis.
  `{"rimshot": 25, "chh": -5, "kick": 0}`), diterapkan **deterministik**
  (bukan acak) ke onset MIDI tiap hit role tersebut. Konversi ms→detik
  sebelum ditambahkan ke waktu onset; klem hasil supaya onset tidak pernah
  negatif (`max(0, t)`). Ini merealisasikan timing **relasional per-role**
  (kick sebagai anchor, rimshot laid-back, dst. — lihat tabel profil di
  `skills/groove-rhythm/references/groove-profiles.md`) menggantikan
  ketergantungan penuh pada jitter random. Bila field ini absen, perilaku
  = v1 (tidak ada offset per-role).

`humanize_velocity` **tetap ada**, tapi kini didokumentasikan sebagai jitter
kecil **terakhir** dalam urutan penerapan — setelah accent `X`/ghost `g`
dan setelah `phrase_velocity`. Nilai default yang disarankan di
`drum-grid-template.json` diturunkan (dokumen, bukan pemaksaan mekanis)
karena perannya kini hanya polish akhir, bukan sumber utama variasi.

Urutan penerapan velocity (didokumentasikan eksplisit di
`midi-conversion.md`): **base velocity → accent `X` / ghost `g` →
`phrase_velocity` → `humanize_velocity` kecil**.

**Aturan komposisi drum (dokumen skill, bukan enforced di kode)** — ditulis
di `skills/jazz-composition/references/level-09-drum.md`:

- Untuk section > 2 bar: **hierarchy wajib** — base groove 2-bar (bar ganjil
  dan genap boleh identik satu sama lain dalam pasangannya), variation di
  sekitar bar ke-4, transition variation di bar terakhir section.
- Minimal **satu one-off imperfection** di seluruh lagu — satu kejadian
  sekali-saja yang disengaja (bukan berulang): ghost note tunggal setelah
  frase lead, kick hilang di satu downbeat, open-hat sekali.
- **Dilarang**: section > 2 bar dengan semua bar identik.

**Lint mekanis** — `grid_to_midi.py` (fungsi validasi baru di dalamnya)
memberi **WARNING** (bukan error, demi kompatibilitas legacy) bila
`section["bars"] > 2` dan semua bar pattern-nya identik (berlaku untuk
kedua bentuk pattern: dict legacy yang secara definisi selalu "identik" di-
tile, atau list baru yang isinya semua sama).

**File yang berubah:**

- `skills/midi-orchestration/scripts/grid_to_midi.py` — parsing dua bentuk
  `pattern` (dict legacy vs. list per-bar + validasi panjang), penerapan
  `phrase_velocity`, penerapan `timing` offset per-role, fungsi lint
  identik-section dengan output warning.
- `skills/midi-orchestration/scripts/test_abc_to_midi_and_grid.py` — test
  baru: pattern per-bar list ter-render benar per bar; panjang list ≠
  `bars` → error; `phrase_velocity` mengalikan velocity dengan benar per
  bar; `timing` offset menggeser onset role yang dituju tanpa mengubah role
  lain dan tanpa onset negatif; spec v1 legacy (dict tunggal) tetap
  menghasilkan MIDI identik seperti sebelum perubahan; warning lint muncul
  untuk section > 2 bar semua-identik dan tidak muncul untuk section yang
  bervariasi/section ≤ 2 bar.
- `skills/midi-orchestration/assets/drum-grid-template.json` — perbarui jadi
  contoh v2: minimal satu section > 2 bar memakai pattern list per-bar
  dengan hierarchy (base groove 2-bar, variation bar-4, transition di bar
  terakhir), contoh `phrase_velocity`, dan catatan `_comment` diperbarui
  untuk menjelaskan kedua bentuk pattern + urutan velocity.
- `skills/jazz-composition/references/level-09-drum.md` — tambah aturan
  hierarchy, larangan section identik, dan requirement one-off imperfection
  ke "Komponen utama"/"Output level ini".
- `skills/midi-orchestration/references/midi-conversion.md` — dokumentasi
  format v2 lengkap (dua bentuk pattern, `phrase_velocity`, `timing`) +
  urutan penerapan velocity di atas, di bagian "How the drum converter
  works".
- `skills/groove-rhythm/references/groove-profiles.md` — tambahkan contoh
  nilai `timing` map untuk profil `neo-soul-core` dalam bentuk siap-pakai
  di `drums.json` (mis. `{"kick": 0, "snare": 15, "rimshot": 25, "chh": -3}`
  ms, diturunkan dari tabel tick offset yang sudah ada di file itu), supaya
  composing brain tinggal salin, bukan menurunkan ulang dari tabel tick.

### Komponen 3 — Gate klaim-vs-notasi (notation facts)

**Script baru** `skills/abc-notation/scripts/notation_facts.py`. Input: file
ABC (+ opsi `--voice N`, mengikuti konvensi argparse `validate_abc.py` yang
sudah ada — positional `abc_file: Path`, plus flag opsional). Output: teks/
markdown fakta objektif per voice per bar:

- nada aktual yang berbunyi setelah key signature diterapkan (mis. `K:Cm` →
  huruf tertulis `E` berbunyi `Eb`), berikut oktafnya;
- urutan interval antar nada melodi berurutan (semitone + nama interval,
  mis. `+3 minor 3rd naik`);
- untuk tiap nada: klasifikasi terhadap chord symbol bar itu — chord-tone /
  tension diatonik / outside (parser chord symbol minimal: `maj7`, `m7`,
  `m9`, `7`, `9`, `13`, `7alt`, `7sus`/`7sus4`, `m7b5`, `dim7`, `6`, `m6`,
  `add9`, slash-bass; simbol tak dikenal → ditandai **"unparsed"**, jangan
  crash);
- untuk voicing multi-nada `[..]`: daftar nada bawah→atas + **top note**
  per bar (untuk mengecek klaim voice-leading);
- klasifikasi chord vs. key: diatonik / borrowed / luar-key (untuk mengecek
  label modal-interchange);
- ringkasan per voice: jumlah not, rest ratio, durasi terpendek/terpanjang.

**Prinsip desain**: script ini adalah **generator fakta**, bukan pengecek
klaim — parsing klaim dari prosa artefak terlalu rapuh untuk diotomasi
dengan andal. Gate-nya hidup di instruksi skill, bukan di script:

- Pada DoD **Level 3** (harmoni), **Level 4** (melodi), dan **Level 7**
  (comping/voicing), pembuat artefak **wajib** menjalankan
  `notation_facts.py`, menempelkan output yang relevan ke artefak level
  itu, dan setiap label teori di artefak (interval, "outside",
  "borrowed"/"modal interchange", klaim top-note/voice-leading) harus
  **cocok** dengan fakta script tersebut — ketidakcocokan berarti artefak
  direvisi sebelum lanjut ke level berikutnya.
- Reviewer L2 (lihat "Reviewer segar (L2)" di `SKILL.md`) diberi output
  script yang sama saat menilai Level 3/4/7, supaya penilaian rubrik juga
  bisa memverifikasi klaim, bukan hanya membaca prosa.

**Test baru** `skills/abc-notation/scripts/test_notation_facts.py` — kasus
wajib:

- `K:Cm`, huruf tertulis `E` → dilaporkan berbunyi `Eb`;
- motif `z C E2 A4` → 3 pitch `C, Eb, Ab` (bukan 4 — rest `z` tidak
  dihitung), interval `+3` (minor 3rd naik) lalu `+5` (perfect 4th naik);
- `"Ebmaj7" z e g2 b4` → semua not diklasifikasi chord-tone (bukan
  outside);
- `Abmaj7` dan `Ebmaj7` di dalam `K:Cm` → diklasifikasi diatonik (bukan
  borrowed/modal interchange);
- voicing `[ACEG]` → top note dilaporkan `G`;
- chord symbol tak dikenal → diklasifikasi `"unparsed"` tanpa raise
  exception.

**File yang berubah selain script + test:**

- `skills/jazz-composition/references/level-03-harmoni.md`,
  `level-04-melodi.md`, `level-07-comping-voicing.md` — tambah langkah
  wajib: jalankan `notation_facts.py`, lampirkan output relevan ke artefak,
  cocokkan tiap label teori dengan fakta yang dilaporkan sebelum artefak
  dianggap selesai.
- `skills/jazz-composition/SKILL.md` — bagian "Reviewer segar (L2)":
  tambah catatan bahwa untuk Level 3/4/7, subagent reviewer juga diberi
  output `notation_facts.py` yang sama yang dilampirkan generator, bukan
  hanya artefak + rubric.md.
- `skills/RED-FLAGS.md` — baris baru: "label teori tanpa cek fakta notasi —
  motif '4-not' yang nyatanya 3 pitch", dengan pointer ke
  `notation_facts.py` sebagai tempat cek realitanya.

## Uji penerimaan Gelombang 1

1. **Semua test Python lulus** — test lama (`test_abc_to_midi_and_grid.py`
   existing cases untuk tempo/meter/beats-per-bar/accent-ghost) tetap hijau,
   plus seluruh test baru dari Komponen 2 (`test_abc_to_midi_and_grid.py`)
   dan Komponen 3 (`test_notation_facts.py`).
2. **Regresi nol pada `drums.json` legacy** — kedua run lama di `runs/`
   (format v1, dict tunggal per section) tetap ter-render identik
   not-untuk-not, velocity-untuk-velocity, onset-untuk-onset dibanding
   sebelum perubahan `grid_to_midi.py`, kecuali warning lint baru yang
   murni informasional di stdout (tidak mengubah `.mid` yang dihasilkan).
3. **Satu run komposisi baru end-to-end** memakai skill versi terbaru
   (brief baru, bukan salah satu dari dua brief lama yang sudah dikritik):
   run folder yang dihasilkan berisi
   - artefak `NN-<level>-candidates.md` di Level 1–4 dengan protokol
     seleksi diikuti (material telanjang, verdict selector, atau
     pre-mortem bila fallback dipakai),
   - `drums.json` v2 ber-hierarchy (base groove 2-bar, variation, transition,
     minimal satu one-off imperfection di seluruh lagu),
   - output `notation_facts.py` menempel di artefak Level 3, 4, dan 7 dengan
     label teori yang cocok fakta,
   - review Level 2 (rubrik L2) dilakukan oleh subagent segar sesuai
     protokol existing.
   `output.mid` dari run ini diserahkan ke user untuk pemeriksaan L3
   (telinga) — keputusan melanjutkan ke Gelombang 2/3 menunggu hasil L3 ini,
   bukan diasumsikan otomatis lolos karena L1/L2 hijau.

## Risiko & tradeoff

| Risiko/tradeoff | Detail | Mitigasi |
|---|---|---|
| Biaya token naik di 4 level kandidat | Level 1–4 kini menghasilkan ~1.5–2× konten (kandidat + seleksi) dibanding single-shot sebelumnya. | Sengaja dibatasi ke 4 level ber-leverage tertinggi, bukan semua 14 level (menghindari ledakan 14×3 paperwork yang eksplisit disebut sebagai hal yang dihindari). |
| Breaking change pada `drums.json` | Menambah dua bentuk `pattern` dan dua field opsional baru berisiko mematahkan run lama atau tooling downstream yang mengasumsikan bentuk v1. | Dual-format eksplisit di parser (`grid_to_midi.py` menerima dict lama & list baru), semua field baru opsional dengan default no-op (`phrase_velocity` default 1.0, `timing` default kosong) — v1 tetap valid dan ter-render identik. |
| Analisis simbolik chord tidak sempurna | Parser chord symbol di `notation_facts.py` hanya mendukung daftar tipe chord umum jazz; simbol eksotis/typo tidak akan terklasifikasi. | Unknown chord ditandai eksplisit `"unparsed"` (bukan crash atau tebakan silent) — gate di level skill mewajibkan generator memperhatikan kasus unparsed secara manual alih-alih mempercayai buta hasil script. |
| Protokol seleksi bergantung pada kemampuan spawn subagent | Sebagian environment (composer pack di browser AI tanpa Claude Code) tidak bisa spawn subagent segar untuk selector independen. | Fallback self-selection + pre-mortem wajib (aturan 5, Komponen 1) — lebih lemah dari selector independen sungguhan, tapi tetap memaksa artikulasi kelemahan sebelum memilih, bukan silent self-justification. |
| Lint drum hanya warning, bukan error | Section > 2 bar yang semua bar-nya identik tetap bisa lolos (demi kompatibilitas run lama yang sah memakai pattern legacy tile). | Diterima secara sadar sebagai scope Gelombang 1 — enforcement lebih ketat (mis. jadi blocker) adalah kandidat Gelombang 3, bukan diselesaikan di sini. |

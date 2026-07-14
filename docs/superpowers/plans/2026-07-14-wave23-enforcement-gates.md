# Gelombang 2-3 — Enforcement Gates + Gigi Penilaian + Export Engine — Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Mewiring aturan yang sudah ada di `references/*.md` menjadi gate wajib per level (C1-C8), memberi "gigi" fail-closed pada penilaian (D1-D5), dan menyambungkan export produksi ke engine `daw_generative` via `POST /api/render` (E1-E4) — sesuai spec `docs/superpowers/specs/2026-07-14-wave23-enforcement-gates-design.md`.

**Architecture:** Hampir seluruh perubahan adalah **dokumen prosa/tabel** yang dieksekusi agent LLM pengikut `SKILL.md` — verifikasinya adalah konsistensi teks, anchor, dan cross-reference, bukan unit test. Pengecualian terbatas: Task 7 (Komponen E2/E3) menambah satu script konverter Python baru (`drums_to_engine.py`, TDD) dan menyelaraskan dict `PROGRAM` di `abc_to_midi.py` ke registry instrumen engine.

**Tech Stack:** Markdown (skill docs), Python 3 stdlib (konverter), `uv run` + `unittest` + `importlib` (konvensi test folder `skills/midi-orchestration/scripts/`), music21 + pretty_midi (hanya untuk suite test lama).

## Global Constraints

1. Dokumen skill bahasa Indonesia, istilah musik Inggris dibiarkan.
2. Penomoran L1/L2/L3 lama TIDAK di-renumber; mekanisme baru bernama L2-blind, L2-cliche (ejaan konsisten dengan hubung).
3. Komponen C/D = dokumen saja, kode Python HANYA di Task 7 (drums_to_engine.py baru + PROGRAM map).
4. `drums_to_engine.py` output HARUS valid skema engine `/api/render` (sections[{bars,pattern-dict}], steps_per_bar 8|12|16, gm 35-81, velocity 1-127, chars x/X/g/.).
5. Commit tanpa Co-Authored-By & tanpa footer AI, pesan bahasa Indonesia.
6. Jangan sentuh `runs/` (kecuali TIDAK ADA — .gitignore ada di root, bukan runs/) dan jangan pindah branch.

## Urutan pengerjaan & strategi anchor (WAJIB dibaca sebelum eksekusi)

**Task dikerjakan berurutan 1 → 8.** Empat file diedit oleh lebih dari satu task; anchor tiap edit dipilih supaya unik terhadap kondisi file **saat task itu dieksekusi**:

| File | Diedit oleh | Strategi anchor |
|---|---|---|
| `skills/jazz-composition/SKILL.md` | Task 1 (bullet Aturan dasar), Task 5 (§Penilaian: fail-closed + checklist), Task 6 (§Penilaian: L2-blind/L2-cliche + Tahap 15), Task 8 (section baru di akhir file) | Task 1/5/8 anchor pada teks ASLI yang saling berjauhan (bullet "hilang antar sesi", kalimat "Template lengkap dan aturan pengisiannya", kalimat penutup file). **Task 6 anchor pada heading `### Checklist pra-L3 (fail-closed)` yang BARU dibuat Task 5** — dependency eksplisit, jangan jalankan Task 6 sebelum Task 5. |
| `skills/jazz-composition/references/scorecard-template.md` | Task 2 (baris L1 Level 10), Task 4 (baris L1 Level 13), Task 5 (section L2 global), Task 6 (L2-blind/L2-cliche/Bukti revisi), Task 8 (section Export) | Task 2/4 mengedit baris checkbox L1 yang unik dan terletak SEBELUM titik sisip task lain. Task 5, 6, 8 SEMUA menyisipkan **tepat sebelum heading `## L3 (telinga) — hanya diisi sekali, di akhir`** (unik, tidak pernah berubah) — karena berurutan, hasil akhirnya bertumpuk dalam urutan benar: L2 global → L2-blind → L2-cliche → Bukti revisi → Export → L3. |
| `skills/vibes-mood/references/reasoning-theory.md` | Task 1 (tabel BPM band sebelum Modul 2), Task 4 (paragraf klarifikasi di Modul 4 Lensa 3) | Dua lokasi berjauhan; anchor Task 4 ("...satu section yang sama itu bahaya.") tidak tersentuh Task 1. Independen. |
| `skills/arrangement/SKILL.md` | Task 3 (§Level 12), Task 4 (§Level 7) | Dua lokasi berjauhan, anchor saling tidak tumpang tindih. Independen. |

Semua anchor di plan ini sudah diverifikasi `grep -c` = **tepat 1 kemunculan** terhadap kondisi file saat plan ditulis (kecuali anchor Task 6 di SKILL.md yang sengaja menunjuk teks hasil Task 5, dicatat di tabel di atas).

## Keputusan penulis plan (dari ruang keputusan yang diserahkan spec)

- **PROGRAM map final** (`abc_to_midi.py`): `sax` 65→**66**, `guitar` 27→**26**, `bass` 33→**32**; entri baru `vibraphone` **11**, `synth-lead` **81** (keduanya diwajibkan spec E3), plus `guitar-clean` **27** (keputusan penulis plan — prinsip "keyword sama → GM sama dengan registry"; keyword majemuk ditempatkan SEBELUM keyword substring-nya karena `program_for` mencocokkan substring berurutan). `horns` 61, `upright` 32, `strings` 48, `pad` 89, `trumpet` 56, `rhodes` 4, `piano` 0 dipertahankan. `bass-finger`/`synth-bass` TIDAK ditambahkan (tidak diminta spec/koordinator; nama voice berformat itu jarang, fallback keyword `bass`→32 masih wajar).
- **Test guard PROGRAM**: `test_abc_to_midi_and_grid.py` saat ini TIDAK punya assert nilai program — sesuai daftar file spec E3, test guard **ditambahkan** (bukan diupdate) sebagai kelas test baru.
- **Dua edit konsistensi scorecard di luar daftar file spec, karena kontradiksi langsung** (bukan penambahan fitur): L1 Level 13 ("dengan angka/persentase") kontradiksi frontal dengan C2 yang melarang persentase; L1 Level 10 ("jumlah chorus per solois") mustahil dipenuhi piece tanpa solo yang justru diwajibkan C4. Keduanya diperbaiki di Task 4 dan Task 2. Inkonsistensi minor yang **dibiarkan sesuai catatan scope spec**: contoh energy-curve persentase di `skills/arrangement/SKILL.md` §Level 13.
- `skills/jazz-composition/references/level-04-melodi.md` **tidak diubah** — spec C8b menempatkan gate tempo di modul `melody-design`/`advanced-melody` + ground rule orchestrator, bukan di file level-04.
- **Konversi drums lintas batas section input TIDAK digabung** — merging bar identik (aturan E2-b) hanya berlaku di dalam satu section input; batas section adalah keputusan musikal yang dipertahankan.
- Bahasa tambahan pada file asal-JCD yang berbahasa Inggris (`groove-meter.md`, `human-ear-protocol.md`, `RED-FLAGS.md`): prosa baru ditulis bahasa Indonesia — mengikuti Global Constraint 1 dan preseden baris terakhir `RED-FLAGS.md` yang sudah berbahasa Indonesia.

**Konvensi test terverifikasi** (dijalankan saat plan ditulis, dari `skills/midi-orchestration/scripts/`):

- Suite lama: `uv run --with music21 --with pretty_midi python -m unittest test_abc_to_midi_and_grid -v` → `Ran 14 tests ... OK`.
- Test baru (stdlib murni, TANPA `--with`): `uv run python -m unittest test_drums_to_engine -v`.

---

### Task 1: C8 — Tempo sebagai parameter hilir (6 file)

**Files:**
- Modify: `skills/vibes-mood/references/reasoning-theory.md` (tabel BPM band, sebelum Modul 2)
- Modify: `skills/melody-design/SKILL.md` (gate densitas-vs-BPM)
- Modify: `skills/melody-design/references/rubric.md` (kriteria baru)
- Modify: `skills/advanced-melody/SKILL.md` (pointer 1 kalimat)
- Modify: `skills/harmony/SKILL.md` (sub-bagian durasi absolut per chord)
- Modify: `skills/groove-rhythm/references/groove-meter.md` (breakpoint swing §3)
- Modify: `skills/jazz-composition/SKILL.md` (ground rule lintas-level)

**Interfaces:**
- Produces: istilah **"tabel BPM band"** di `skills/vibes-mood/references/reasoning-theory.md` — dirujuk oleh melody-design/advanced-melody/harmony/groove-meter/jazz-composition (task ini) dan tidak oleh task lain.

- [ ] **Step 1: Tambah tabel BPM band ke `reasoning-theory.md`**

Edit `skills/vibes-mood/references/reasoning-theory.md`. old_string:

```
## Modul 2 — Deklarasi hierarki teori (gate)
```

new_string (section baru + heading lama):

```
## Tabel BPM band — tempo sebagai parameter hilir

Dipakai lintas-level oleh orchestrator `jazz-composition` (Level 4 melodi,
Level 5 groove, Level 8 bass, Level 9 drum — lihat ground rule tempo di
`../../jazz-composition/SKILL.md`): setiap keputusan materi ritmis dicek
terhadap band BPM brief, bukan diputuskan seolah tempo hanya dekorasi.
Prinsip arah: **makin cepat BPM, makin jarang subdivisi rapat dipakai dan
makin panjang frase dalam bar.**

| BPM band | Label | Subdivisi melodi wajar | Napas minimum | Harmonic rhythm wajar | Swing feel |
|---|---|---|---|---|---|
| < 72 | Ballad | 16th aman | ≥2 beat | 2 chord/bar masih bisa aman (cek rumus durasi absolut) | ≈2:1 (66%) |
| 72-92 | Medium-slow | 16th selektif | ≥1.5 beat | 1-2 chord/bar (cek rumus durasi absolut) | ≈60-66% |
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
```

- [ ] **Step 2: Tambah gate densitas-vs-BPM ke `melody-design/SKILL.md`**

Edit `skills/melody-design/SKILL.md`. old_string:

```
## Output level ini
```

new_string (section gate baru + heading lama):

```
## Gate tempo — densitas ritmis vs BPM (wajib)

Artefak Level 4 wajib:

1. Menyebut **BPM brief secara eksplisit** (angka, bukan "sedang").
2. Menyatakan **IOI (inter-onset interval) tercepat** yang benar-benar
   dipakai melodi (subdivisi terkecil antar onset, mis. 16th) dan **rest
   ratio** melodi (proporsi waktu rest per section).
3. Mengecek keduanya terhadap tabel BPM band di
   `../vibes-mood/references/reasoning-theory.md` (kolom "Subdivisi melodi
   wajar" + "Napas minimum" untuk band BPM brief).

Melodi yang memakai subdivisi lebih rapat dari kolom "Subdivisi melodi
wajar" band-nya, atau napas lebih pendek dari "Napas minimum", **direvisi
atau diberi justifikasi eksplisit tertulis** — bukan dilewatkan diam-diam.
Motif 16th padat yang lolos semua rubrik teori tetap ditolak di sini bila
tidak bisa dimainkan wajar pada BPM brief.

## Output level ini
```

- [ ] **Step 3: Tambah kriteria rubrik baru ke `melody-design/references/rubric.md`**

Edit `skills/melody-design/references/rubric.md`. old_string:

```
| Klimaks tidak dilemahkan oleh titik tinggi yang sudah berulang sebelumnya; head tetap memorable setelah nada dekoratif dihapus | | |
```

new_string:

```
| Klimaks tidak dilemahkan oleh titik tinggi yang sudah berulang sebelumnya; head tetap memorable setelah nada dekoratif dihapus | | |
| Kepadatan ritmis melodi proporsional dengan tempo brief (BPM disebut eksplisit; IOI tercepat dan rest ratio cocok dengan tabel BPM band `vibes-mood/references/reasoning-theory.md`) | | |
```

- [ ] **Step 4: Tambah pointer gate tempo ke `advanced-melody/SKILL.md`**

Edit `skills/advanced-melody/SKILL.md`. old_string:

```
Jika salah satu dari keempat syarat ini tidak terpenuhi, jangan pakai
outside pada bar tersebut — kembalikan ke vocabulary `melody-design` biasa.
```

new_string:

```
Jika salah satu dari keempat syarat ini tidak terpenuhi, jangan pakai
outside pada bar tersebut — kembalikan ke vocabulary `melody-design` biasa.

Chromatic vocabulary tahap 7–8 juga tunduk pada **gate tempo
densitas-vs-BPM yang sama** di `../melody-design/SKILL.md` (BPM brief
eksplisit + cek IOI/napas terhadap tabel BPM band
`../vibes-mood/references/reasoning-theory.md`) — bukan gate terpisah.
```

- [ ] **Step 5: Tambah sub-bagian durasi absolut per chord ke `harmony/SKILL.md`**

Edit `skills/harmony/SKILL.md`. old_string:

```
Harmonic rhythm adalah seberapa sering chord berubah — 1 chord per bar,
2 chord per bar, 1 chord setiap 2 bar, atau kombinasi. Harmonic rhythm lambat
memberi ruang modal; harmonic rhythm cepat memberi kesan bebop atau
functional jazz.
```

new_string:

````
Harmonic rhythm adalah seberapa sering chord berubah — 1 chord per bar,
2 chord per bar, 1 chord setiap 2 bar, atau kombinasi. Harmonic rhythm lambat
memberi ruang modal; harmonic rhythm cepat memberi kesan bebop atau
functional jazz.

### Durasi absolut per chord — cek terhadap BPM (wajib)

Rumuskan harmonic rhythm sebagai **durasi absolut**, bukan hanya "N chord
per bar":

```
durasi per chord (detik) = bars_per_chord × beats_per_bar × 60 / BPM
```

Target: minimal **±2 detik per chord** agar perubahan harmoni "teraba"
pendengar. Konsekuensi rumus ini (bukan aturan tempo-vs-jumlah-chord yang
berdiri sendiri): pada BPM rendah satu bar berdurasi lebih panjang secara
absolut, sehingga 2 chord/bar tetap bisa aman asal masih ≥2 detik per
chord; pada BPM tinggi 2 chord/bar lebih berisiko karena tiap chord
kebagian waktu absolut yang pendek. Kriteria rubrik `references/rubric.md`
"ritme harmonik cocok dengan tempo dan groove" kini dicek dengan rumus
ini, bukan penilaian rasa; ringkasan band per BPM ada di tabel BPM band
`../vibes-mood/references/reasoning-theory.md`.
````

- [ ] **Step 6: Tambah breakpoint swing ratio ke `groove-meter.md` §3**

Edit `skills/groove-rhythm/references/groove-meter.md`. old_string:

```
The ratio tends to become more even at faster tempos and may vary by era and player. In ABC, normally notate equal eighths and mark swing as a performance direction.
```

new_string:

```
The ratio tends to become more even at faster tempos and may vary by era and player. In ABC, normally notate equal eighths and mark swing as a performance direction.

Breakpoint operasional untuk prosa di atas (cek terhadap BPM brief —
lihat juga tabel BPM band `../../vibes-mood/references/reasoning-theory.md`):

| BPM | Swing ratio |
|---|---|
| < 80 | 2:1 (≈66%) — masih nyaman |
| 80-120 | ≈60-64% |
| > 140 | mendekati even (≈55-57%) |

Di antara 120-140, interpolasikan (≈57-60%) — arah hubungannya tetap:
makin cepat, makin even.
```

- [ ] **Step 7: Tambah ground rule tempo lintas-level ke `jazz-composition/SKILL.md`**

Edit `skills/jazz-composition/SKILL.md` (bagian "Aturan dasar yang berlaku di semua level"). old_string:

```
- Setiap generate menulis artefak bernomor ke run folder — lihat
  `## Run folder` di bawah — bukan output sekali-pakai yang hilang antar
  sesi.
```

new_string:

```
- Setiap generate menulis artefak bernomor ke run folder — lihat
  `## Run folder` di bawah — bukan output sekali-pakai yang hilang antar
  sesi.
- **Tempo adalah parameter hilir, bukan dekorasi.** Setiap level yang
  memutuskan materi ritmis — Level 4 (melodi), Level 5 (groove), Level 8
  (bass), Level 9 (drum) — wajib menyebut **BPM brief** secara eksplisit
  di artefaknya sendiri dan mengecek keputusan
  subdivisi/napas/harmonic-rhythm/swing-nya terhadap tabel BPM band di
  `../vibes-mood/references/reasoning-theory.md`.
```

- [ ] **Step 8: Verifikasi cross-reference**

Run:
```bash
cd /home/shendi/self-project/daw_generative/music-composition-skill && \
grep -c "Tabel BPM band" skills/vibes-mood/references/reasoning-theory.md && \
grep -l "tabel BPM band" skills/melody-design/SKILL.md skills/melody-design/references/rubric.md skills/advanced-melody/SKILL.md skills/harmony/SKILL.md skills/groove-rhythm/references/groove-meter.md skills/jazz-composition/SKILL.md
```
Expected: angka `1` lalu keenam path file tercetak (semua merujuk tabel yang sama).

- [ ] **Step 9: Commit**

```bash
cd /home/shendi/self-project/daw_generative/music-composition-skill && \
git add skills/vibes-mood/references/reasoning-theory.md skills/melody-design/SKILL.md skills/melody-design/references/rubric.md skills/advanced-melody/SKILL.md skills/harmony/SKILL.md skills/groove-rhythm/references/groove-meter.md skills/jazz-composition/SKILL.md && \
git commit -m "feat(skills): tempo jadi parameter hilir (C8) — tabel BPM band + gate densitas/harmonic-rhythm/swing lintas-level"
```

---

### Task 2: C3 — Bass anti-default + C4 — Micro-improvisation map

**Files:**
- Modify: `skills/jazz-composition/references/level-08-bass.md` (tabel device per transisi, kuota chromatic ≤1/3, relasi bass-kick, catatan contoh walking)
- Modify: `skills/jazz-composition/references/level-10-improvisasi.md` (subsection micro-improvisation map)
- Modify: `skills/jazz-composition/references/scorecard-template.md` (baris L1 Level 10 — konsekuensi wajib C4, lihat "Keputusan penulis plan")

**Interfaces:**
- Produces: istilah **"micro-improvisation map"** (dirujuk baris L1 scorecard Level 10) dan **"tabel device per transisi chord"** + kuota ≤1/3 (dirujuk entri register cliché di Task 6).

- [ ] **Step 1: Beri catatan "salah satu opsi, bukan default" pada contoh walking bass**

Edit `skills/jazz-composition/references/level-08-bass.md`. old_string:

```
Contoh Dm7 menuju G7:

D – F – A – Ab | G
```

new_string:

```
Contoh Dm7 menuju G7:

D – F – A – Ab | G

Catatan: contoh di atas adalah **salah satu opsi, bukan default** —
chromatic approach di beat 4 hanyalah satu dari banyak device transisi.
Lihat tabel device per transisi chord + kuota chromatic ≤1/3 di "Output
level ini" di bawah.
```

- [ ] **Step 2: Ganti output Level 8 — tabel device + kuota + relasi bass-kick**

Edit `skills/jazz-composition/references/level-08-bass.md`. old_string:

```
Output level ini
Bass concept untuk setiap section.
```

new_string:

```
Output level ini
Bass concept untuk setiap section, PLUS dua kewajiban berikut.

### Tabel device per transisi chord (wajib)

Satu baris untuk **setiap transisi chord** dalam piece (bar N → bar N+1,
atau chord A → chord B di dalam bar):

| Transisi (bar/chord) | Device dipakai | Alasan musikal (1 kalimat) |
|---|---|---|

**Kuota**: chromatic approach maksimal **~1/3 dari seluruh transisi chord
dalam piece**. Sisanya diambil dari menu: diam/rest, common tone, octave
displacement, anticipation, pedal/held-through — atau pendekatan dari
daftar "Pilihan pendekatan" di atas (two-feel, pedal point, ostinato,
counterline, slash-bass movement). Tabel dengan chromatic approach di
lebih dari ~1/3 baris = **revisi dulu**, jangan lanjut ke level
berikutnya.

### Relasi bass-kick per section (wajib)

Sebut **lock point** per section: di beat/step mana bass dan kick drum
bertemu secara sengaja (mis. "beat 1 dan and-of-3 dikunci bersama kick;
beat 2-4 bebas"). Bass line yang ditulis tanpa menyebut relasinya ke kick
belum selesai di level ini.
```

- [ ] **Step 3: Tambah subsection micro-improvisation map ke Level 10**

Edit `skills/jazz-composition/references/level-10-improvisasi.md`. old_string:

```
## Gate — ask, don't guess
```

new_string (subsection baru + heading lama):

```
## Micro-improvisation map — wajib untuk piece TANPA solo section

Piece tanpa solo section formal (umum di brief neo-soul/chill-jazz
pendek) TIDAK lolos Level 10 tanpa artefak apa pun. Artefak Level 10
untuk kasus ini adalah **micro-improvisation map** berisi lima field:

1. **Bar yang boleh diornamen** — pickup bebas, tail ad-lib, ornament
   lokal (sebut nomor bar).
2. **Nada anchor yang wajib dipertahankan** — nada yang tidak boleh
   diubah performer.
3. **Range maksimum penyimpangan** yang diizinkan (interval/oktaf).
4. **Gesture yang terlarang secara eksplisit** (mis. run 16th penuh,
   register ekstrem).
5. **Tingkat kebebasan ritmis per section** — ketat / sedang / longgar.

**"Tanpa solo" ≠ "nol perilaku improvisatoris"** — setiap piece, bersolo
atau tidak, punya map ini.

## Gate — ask, don't guess
```

- [ ] **Step 4: Selaraskan baris L1 Level 10 di scorecard-template**

Konsekuensi wajib C4 (tanpa ini, L1 Level 10 mustahil dipenuhi piece tanpa solo). Edit `skills/jazz-composition/references/scorecard-template.md`. old_string:

```
- [ ] Solo map mencantumkan jumlah chorus per solois
```

new_string:

```
- [ ] Solo map mencantumkan jumlah chorus per solois — atau, untuk piece
      tanpa solo section: micro-improvisation map terisi lengkap (5 field,
      lihat `level-10-improvisasi.md`)
```

- [ ] **Step 5: Verifikasi**

Run:
```bash
cd /home/shendi/self-project/daw_generative/music-composition-skill && \
grep -c "salah satu opsi, bukan default" skills/jazz-composition/references/level-08-bass.md && \
grep -c "lock point" skills/jazz-composition/references/level-08-bass.md && \
grep -ci "micro-improvisation map" skills/jazz-composition/references/level-10-improvisasi.md skills/jazz-composition/references/scorecard-template.md
```
Expected: `1`, `1`, lalu `level-10-improvisasi.md:2` (heading kapital + isi) dan `scorecard-template.md:1` (`-i` karena heading memakai kapital "Micro-improvisation").

- [ ] **Step 6: Commit**

```bash
cd /home/shendi/self-project/daw_generative/music-composition-skill && \
git add skills/jazz-composition/references/level-08-bass.md skills/jazz-composition/references/level-10-improvisasi.md skills/jazz-composition/references/scorecard-template.md && \
git commit -m "feat(skills): bass anti-default (C3) + micro-improvisation map utk piece tanpa solo (C4)"
```

---

### Task 3: C1 — Gate transisi 3-fase + C5 — Intro performatif & ending rekontekstualisasi

**Files:**
- Modify: `skills/jazz-composition/references/level-11-interlude-shout-transisi.md` (tabel 3-fase + kutipan model 4-tahap + gate)
- Modify: `skills/jazz-composition/references/level-12-intro-ending.md` (gate intro performatif, opsi rekontekstualisasi, gate ending)
- Modify: `skills/arrangement/SKILL.md` §Level 12 (1 kalimat rujukan)

**Interfaces:**
- Consumes: `skills/arrangement/references/instrumental-transitions.md` §1 (model setup/threshold/arrival/aftercare), §6 (arrival ≥2 cue), §9 (failure modes) — sudah ada, tidak diubah.
- Produces: istilah **"gate intro performatif"** dan **"rekontekstualisasi"** (dirujuk register cliché Task 6).

- [ ] **Step 1: Ganti output Level 11 dengan tabel transisi 3-fase**

Edit `skills/jazz-composition/references/level-11-interlude-shout-transisi.md`. old_string:

```
Output level ini
Bagian transisi yang tertulis jelas.
```

new_string:

```
Output level ini
Tabel transisi 3-fase — satu baris per **transisi section**:

| Transisi (dari → ke) | Preparation (1-2 bar sebelum batas) | Boundary event (tepat di batas) | After-effect (1-2 bar sesudah batas) |
|---|---|---|---|

- **Preparation** — apa yang mulai berubah menjelang batas, instrumen
  mana.
- **Boundary event** — kejadian tepat di batas section.
- **After-effect** — apa yang terbawa/tertahan dari sebelum batas.

Tabel ini wajib mengutip dan menautkan eksplisit model transisi 4-tahap
**setup / threshold / arrival / aftercare** di
[`../../arrangement/references/instrumental-transitions.md`](../../arrangement/references/instrumental-transitions.md)
§1 (Transition model). Pemetaan: preparation ≈ setup; boundary event ≈
threshold + arrival; after-effect ≈ aftercare.

**Gate**: transisi yang hanya berupa kejadian tepat di barline — kolom
preparation dan after-effect kosong/tidak diisi — = **ditolak**; artefak
direvisi sebelum lanjut ke level berikutnya. Konsisten dengan
`instrumental-transitions.md` §9 (failure mode "no confirmation after a
dramatic buildup") dan §6 (arrival dikonfirmasi ≥2 cue): kedua sisi
batas — bukan hanya sisi datang — harus tertulis eksplisit.
```

- [ ] **Step 2: Tambah gate intro performatif ke Level 12**

Edit `skills/jazz-composition/references/level-12-intro-ending.md`. old_string:

```
4 bar piano rubato
4 bar bass pedal
masuk head
```

new_string:

```
4 bar piano rubato
4 bar bass pedal
masuk head

### Gate intro performatif (wajib)

Intro wajib mengandung **≥1 kejadian performatif spesifik** dari menu:

* incomplete voicing — chord yang sengaja belum lengkap;
* delayed entrance salah satu instrumen;
* frase yang terdengar "mencari" nada (belum landing di target tone);
* ruang/napas yang disengaja (rest terjadwal, bukan filler).

Intro "pad sempurna sejak beat 1" = **ditolak tanpa justifikasi
tertulis**.
```

- [ ] **Step 3: Tambah opsi ending rekontekstualisasi**

Edit `skills/jazz-composition/references/level-12-intro-ending.md`. old_string:

```
* fade-style vamp
```

new_string:

```
* fade-style vamp
* rekontekstualisasi — nada yang sepanjang lagu terasa tegang (muncul
  berulang sebagai tension/outside/dissonant note) **dipertahankan**
  persis di ending, tapi harmoni di bawahnya berubah sehingga nada yang
  sama kini terasa **diterima** (resolved) tanpa nada itu sendiri berubah
```

- [ ] **Step 4: Tambah gate ending**

Edit `skills/jazz-composition/references/level-12-intro-ending.md`. old_string:

```
Ending sebaiknya berhubungan dengan motif utama.
```

new_string:

```
Ending sebaiknya berhubungan dengan motif utama.

### Gate ending (wajib)

Ending bertipe "makin sepi + tonic panjang" (fade-style vamp — pola
paling umum) hanya boleh dipilih **setelah** alternatif rekontekstualisasi
dipertimbangkan tertulis — minimal 1 kalimat kenapa rekontekstualisasi
tidak dipakai untuk piece ini.
```

- [ ] **Step 5: Tambah rujukan gate di `arrangement/SKILL.md` §Level 12**

Edit `skills/arrangement/SKILL.md`. old_string:

```
Output level ini: intro dan coda yang punya identitas, bukan sekadar
tambahan.
```

new_string:

```
Output level ini: intro dan coda yang punya identitas, bukan sekadar
tambahan. Sebelum memilih, jalankan gate wajib di
`../jazz-composition/references/level-12-intro-ending.md` — intro
performatif (≥1 kejadian performatif spesifik) dan pertimbangan tertulis
opsi rekontekstualisasi sebelum ending "makin sepi + tonic panjang"
dipilih.
```

- [ ] **Step 6: Verifikasi**

Run:
```bash
cd /home/shendi/self-project/daw_generative/music-composition-skill && \
grep -c "setup / threshold / arrival / aftercare" skills/jazz-composition/references/level-11-interlude-shout-transisi.md && \
grep -c "Gate intro performatif" skills/jazz-composition/references/level-12-intro-ending.md && \
grep -c "rekontekstualisasi" skills/jazz-composition/references/level-12-intro-ending.md && \
grep -c "level-12-intro-ending.md" skills/arrangement/SKILL.md && \
grep -c "1. Transition model" skills/arrangement/references/instrumental-transitions.md
```
Expected: `1`, `1`, `≥3`, `1`, `2` (daftar isi + heading §1 — target link benar-benar ada).

- [ ] **Step 7: Commit**

```bash
cd /home/shendi/self-project/daw_generative/music-composition-skill && \
git add skills/jazz-composition/references/level-11-interlude-shout-transisi.md skills/jazz-composition/references/level-12-intro-ending.md skills/arrangement/SKILL.md && \
git commit -m "feat(skills): gate transisi 3-fase (C1) + intro performatif & ending rekontekstualisasi (C5)"
```

---

### Task 4: C2 — Dinamika observabel + micro-apex, C6 — Comping cells, C7 — Rekonsiliasi 1-ide

**Files:**
- Modify: `skills/jazz-composition/references/level-13-dinamika-dramaturgi.md` (ganti template %, tabel metrik, micro-apex + gate)
- Modify: `skills/jazz-composition/references/scorecard-template.md` (baris L1 Level 13 — konsekuensi wajib C2, lihat "Keputusan penulis plan")
- Modify: `skills/jazz-composition/references/level-07-comping-voicing.md` (comping cells + gate)
- Modify: `skills/arrangement/SKILL.md` §Level 7 (kewajiban yang sama)
- Modify: `skills/vibes-mood/references/reasoning-theory.md` Modul 4 Lensa 3 (paragraf klarifikasi)

**Interfaces:**
- Consumes: `skills/abc-notation/scripts/notation_facts.py` (sudah ada dari Gelombang 1, tidak diubah).
- Produces: istilah **"micro-apex"** dan **"≥3 comping cell"** (dirujuk register cliché Task 6).

- [ ] **Step 1: Ganti template persentase Level 13 dengan tabel metrik observabel + micro-apex**

Edit `skills/jazz-composition/references/level-13-dinamika-dramaturgi.md`. old_string (perhatikan: semua nilai `%` rata di kolom yang sama — salin persis):

```
Buat energy curve
Contoh:

Intro        20%
A1           35%
A2           45%
Bridge       60%
A3           50%
Solo 1       55–70%
Solo 2       65–85%
Shout chorus 100%
Head out     70%
Coda         30%
```

new_string:

```
Buat peta dinamika observabel
Angka persentase (mis. "Intro 20%") adalah klaim yang tak bisa
diverifikasi dari notasi — jangan dipakai. Ganti dengan **tabel per
section berisi metrik observabel**:

| Metrik | Sumber |
|---|---|
| Active voices | hitung manual dari partitur/ABC per section |
| Note-attacks per bar | output `notation_facts.py` per voice (`../../abc-notation/scripts/notation_facts.py`, sudah ada dari Gelombang 1) |
| Register lead | rendah/tengah/tinggi + rentang aktual |
| Durasi not rata-rata | dari notasi per section |
| Drum hits per bar | dari `drums.json`/roadmap drum |
| Dynamic marks | dari notasi (mf, mp, dst., bila ada) |

Micro-apex (field wajib)
Satu bar spesifik per piece (atau per bagian besar) yang menjadi momen
paling berarti, ditulis sebagai **"bar N: <mekanisme>"**. Mekanisme harus
dari kelas **non-volume**: register ekstrem tipis (satu nada
tinggi/rendah sesaat), dissonance singkat, drop groove (instrumen
berhenti sesaat), ruang kosong (rest terjadwal), dsb — **bukan** "volume
naik" atau "semua instrumen tutti".

**Gate**: section yang dilabeli "tidak ada peak"/"restrained" tanpa
micro-apex yang terdefinisi = **ditolak** — restrained tidak sama dengan
datar; artefak tetap menunjuk satu momen mekanisme non-volume yang
membuat section itu diingat.
```

- [ ] **Step 2: Selaraskan baris output Level 13**

Edit `skills/jazz-composition/references/level-13-dinamika-dramaturgi.md`. old_string:

```
Output level ini
Peta energi per section.
```

new_string:

```
Output level ini
Tabel metrik observabel per section + field micro-apex.
```

- [ ] **Step 3: Selaraskan baris L1 Level 13 di scorecard-template**

Konsekuensi wajib C2 (baris lama menuntut persentase yang justru dilarang C2). Edit `skills/jazz-composition/references/scorecard-template.md`. old_string:

```
- [ ] Energy curve tercantum per section dengan angka/persentase
```

new_string:

```
- [ ] Peta dinamika observabel tercantum per section (tabel metrik +
      micro-apex terisi) — bukan persentase (lihat
      `level-13-dinamika-dramaturgi.md`)
```

- [ ] **Step 4: Tambah kewajiban comping cells ke Level 7**

Edit `skills/jazz-composition/references/level-07-comping-voicing.md`. old_string:

```
A1: sparse, 2–3 attacks per bar
A2: syncopated responses
Bridge: denser voicing
Solo: interactive comping
Head out: simplified voicing
```

new_string:

```
A1: sparse, 2–3 attacks per bar
A2: syncopated responses
Bridge: denser voicing
Solo: interactive comping
Head out: simplified voicing

### Comping cells mengikuti ruang lead (wajib)

Deskripsi kepadatan seperti chart di atas belum cukup — itu deskripsi
density, bukan pemetaan interaksi. Deliverable tambahan:

1. Pilih **≥3 comping cell berbeda** dari vocabulary yang sudah ada —
   held / delayed answer / short syncopated stab, atau turunan dari
   teknik comping di atas (Charleston rhythm, anticipatory stab,
   fragmented chord, dll.).
2. **Petakan ke ruang lead**: bar mana lead bernapas (rest/held note
   panjang) → cell comping apa yang mengisi ruang itu, atau justru diam.

**Gate**: comping uniform 1 attack/bar sepanjang lagu = **ditolak**,
kecuali dijustifikasi eksplisit terhadap peta napas lead (mis. lead
memang tidak pernah bernapas di section itu, sehingga comping sengaja
seragam untuk mendukung — bukan lupa memvariasikan).
```

- [ ] **Step 5: Tambah kewajiban yang sama ke `arrangement/SKILL.md` §Level 7**

Edit `skills/arrangement/SKILL.md`. old_string — DUA baris: baris teks `Head out: simplified voicing` diikuti baris penutup code-fence tiga-backtick (di file ini chart berada dalam code fence; string dua-baris ini muncul tepat sekali di file ini):

````
Head out: simplified voicing
```
````

new_string:

````
Head out: simplified voicing
```

Deliverable wajib (selaras gate di
`../jazz-composition/references/level-07-comping-voicing.md`): pilih
**≥3 comping cell berbeda** (held / delayed answer / short syncopated
stab, atau turunan teknik comping di atas), lalu **petakan ke ruang
lead** — bar mana lead bernapas (rest/held note panjang) → cell apa yang
mengisi ruang itu, atau justru diam. Comping uniform 1 attack/bar
sepanjang lagu ditolak tanpa justifikasi eksplisit terhadap peta napas
lead.
````

- [ ] **Step 6: Tambah paragraf rekonsiliasi C7 ke Modul 4 Lensa 3**

Edit `skills/vibes-mood/references/reasoning-theory.md`. old_string:

```
identitas — pendengar tak bisa menangkap "section ini tentang apa". Variasi
*antar*-section itu sehat (lihat variation budget di `neo-soul-genre.md`);
variasi *di dalam* satu section yang sama itu bahaya.
```

new_string:

```
identitas — pendengar tak bisa menangkap "section ini tentang apa". Variasi
*antar*-section itu sehat (lihat variation budget di `neo-soul-genre.md`);
variasi *di dalam* satu section yang sama itu bahaya.

Klarifikasi (rekonsiliasi dengan `../../RED-FLAGS.md` baris "most
sections need 2-3 moves"): **satu ide UTAMA per dimensi per section, plus
hingga 2-3 detail pendukung yang berkorelasi dengannya.** Detail
pendukung bukan ide independen kedua — ia harus bisa dijelaskan sebagai
penjabaran/penguat ide utama yang sama, bukan tema kedua yang bersaing
untuk perhatian. "2-3 moves" di RED-FLAGS.md = ide utama + detail
pendukungnya; Lensa 3 membatasi jumlah ide UTAMA, bukan jumlah move —
kedua kalimat itu sejalan, bukan kontradiksi.
```

- [ ] **Step 7: Verifikasi**

Run:
```bash
cd /home/shendi/self-project/daw_generative/music-composition-skill && \
grep -ci "micro-apex" skills/jazz-composition/references/level-13-dinamika-dramaturgi.md && \
grep -c "20%" skills/jazz-composition/references/level-13-dinamika-dramaturgi.md ; \
grep -c "comping cell" skills/jazz-composition/references/level-07-comping-voicing.md skills/arrangement/SKILL.md && \
grep -c "ide UTAMA per dimensi" skills/vibes-mood/references/reasoning-theory.md && \
ls skills/abc-notation/scripts/notation_facts.py
```
Expected: micro-apex `3` (case-insensitive: heading "Micro-apex" + gate + baris output); `20%` menghasilkan `0` (grep exit 1 — persentase hilang, karena itu dipisah `;` bukan `&&`); comping cell ≥1 di kedua file; `1`; path notation_facts.py tercetak.

- [ ] **Step 8: Commit**

```bash
cd /home/shendi/self-project/daw_generative/music-composition-skill && \
git add skills/jazz-composition/references/level-13-dinamika-dramaturgi.md skills/jazz-composition/references/scorecard-template.md skills/jazz-composition/references/level-07-comping-voicing.md skills/arrangement/SKILL.md skills/vibes-mood/references/reasoning-theory.md && \
git commit -m "feat(skills): dinamika observabel + micro-apex (C2), comping cells ikut napas lead (C6), rekonsiliasi 1-ide vs 2-3 moves (C7)"
```

---

### Task 5: D1 — Blocker L2 global fail-closed + D5 — L3 wajib per-piece & checklist pra-L3

**Files:**
- Modify: `skills/jazz-composition/references/scorecard-template.md` (bagian baru "L2 global" dengan 4 blocker + semantik fail-closed)
- Modify: `skills/jazz-composition/SKILL.md` §Penilaian (aturan fail-closed + checklist pra-L3)
- Modify: `skills/jazz-composition/references/human-ear-protocol.md` (klarifikasi sampling vs L3 wajib per-piece)

**Interfaces:**
- Produces: heading **`### Checklist pra-L3 (fail-closed)`** di `skills/jazz-composition/SKILL.md` — **anchor sisip Task 6**; heading **`## L2 global — kriteria blocker lintas-level (fail-closed)`** di scorecard-template (tempat Task 6 menambahkan subsection L2-blind/L2-cliche). Istilah dipakai persis: `L2-rubrik`, `L2-blind`, `L2-cliche`.

- [ ] **Step 1: Tambah bagian "L2 global" ke scorecard-template**

Edit `skills/jazz-composition/references/scorecard-template.md` — sisip tepat SEBELUM heading L3 (di dalam blok template markdown). old_string:

```
## L3 (telinga) — hanya diisi sekali, di akhir
```

new_string (bagian baru + heading lama):

```
## L2 global — kriteria blocker lintas-level (fail-closed)

Dinilai terhadap **keseluruhan piece** (bukan per level), oleh reviewer
segar, setelah Level 14 selesai. Empat kriteria di bawah adalah
**BLOCKER**:

| # | Kriteria blocker | Skor (0-2) | Bukti dari notasi (bar spesifik) |
|---|---|---|---|
| 1 | Identitas — 4 bar pertama bisa dibedakan dari template genre | | |
| 2 | Memorability — motif bisa diingat/dinyanyikan setelah sekali baca-dengar | | |
| 3 | Interaction — instrumen terdengar saling mendengar (ada bukti call-response/ruang) | | |
| 4 | Emotional specificity — arc terasa dari notasi tanpa membaca brief | | |

**Semantik fail-closed**: skor **0** pada **salah satu** dari keempat
kriteria ini = run **BELUM SELESAI**, terlepas dari skor kriteria lain —
wajib revisi + re-review sebelum boleh disebut selesai. Skor tinggi di
L2-rubrik per-level **tidak menyelamatkan** blocker yang gagal.

## L3 (telinga) — hanya diisi sekali, di akhir
```

- [ ] **Step 2: Tambah aturan fail-closed + checklist pra-L3 ke `SKILL.md` §Penilaian**

Edit `skills/jazz-composition/SKILL.md`. old_string:

```
Setiap run folder punya satu `scorecard.md` berisi penilaian tiga lapis
(L1 mekanis, L2 rubrik oleh reviewer segar, L3 telinga manusia di akhir).
Template lengkap dan aturan pengisiannya ada di
`references/scorecard-template.md`.
```

new_string:

```
Setiap run folder punya satu `scorecard.md` berisi penilaian tiga lapis
(L1 mekanis, L2 rubrik oleh reviewer segar, L3 telinga manusia di akhir).
Template lengkap dan aturan pengisiannya ada di
`references/scorecard-template.md`.

### Aturan fail-closed — 4 blocker L2 global

Selain L2-rubrik per level, scorecard punya bagian **"L2 global"** (lihat
`references/scorecard-template.md`) berisi 4 kriteria **blocker**:
identitas, memorability, interaction, emotional specificity. Skor **0**
pada salah satu = run **BELUM SELESAI**, terlepas dari skor kriteria
lain — wajib revisi + re-review sebelum boleh disebut selesai. Skor
tinggi di L2-rubrik per-level **tidak menyelamatkan** blocker yang gagal.

### Checklist pra-L3 (fail-closed)

Operasionalisasi konkret aturan fail-closed di atas: sebuah piece **boleh
diserahkan ke telinga manusia (L3)** hanya bila SEMUA item berikut
terpenuhi — "belum boleh disebut selesai" berarti "checklist ini belum
semua tercentang", bukan penilaian subjektif kapan piece "cukup matang":

- [ ] L1 (mekanis) — lulus semua level.
- [ ] L2-rubrik — lengkap terisi semua 14 level.
- [ ] 4 kriteria blocker (L2 global) — semuanya bernilai **≥1** (tidak
      ada yang 0).
- [ ] L2-blind — dijalankan, hasilnya **benar** (lihat prosedur L2-blind
      di bagian Penilaian ini).
- [ ] L2-cliche — semua temuan sudah direspons: revisi atau justifikasi
      audible (lihat prosedur L2-cliche di bagian Penilaian ini).
- [ ] Bukti revisi — ada, terhubung ke temuan nyata (lihat Tahap 15).
```

Catatan implementasi: item L2-blind/L2-cliche/Bukti revisi menunjuk prosedur yang baru ditambahkan **Task 6** — antara Task 5 dan Task 6 rujukan itu menggantung sebentar; itu disengaja dan selesai begitu Task 6 rampung (urutan task wajib).

- [ ] **Step 3: Klarifikasi cakupan sampling di `human-ear-protocol.md`**

Edit `skills/jazz-composition/references/human-ear-protocol.md`. old_string:

```
Run this on a small subset (2 briefs is enough) before a release that
changes composition craft, not on every eval run — it's the expensive
layer, spend it deliberately.
```

new_string:

```
Run this on a small subset (2 briefs is enough) before a release that
changes composition craft, not on every eval run — it's the expensive
layer, spend it deliberately.

**Klarifikasi cakupan (penting):** aturan sampling di atas ("2 briefs is
enough", "not on every eval run") **hanya berlaku untuk eksperimen
evaluasi skill/paket ini sendiri** (mis. eval before/after seperti
`tests/results/2026-07-13-brief-01-02-armA-vs-armB.md`). Untuk **piece
produksi** — composer benar-benar membuat lagu untuk dipakai, bukan
mengevaluasi skill — **L3 wajib per-piece** sebelum piece itu disebut
selesai; tidak ada sampling untuk kasus ini. Gerbang mekanis sebelum L3
boleh dijalankan: checklist pra-L3 (fail-closed) di `../SKILL.md`
§Penilaian.
```

- [ ] **Step 4: Verifikasi**

Run:
```bash
cd /home/shendi/self-project/daw_generative/music-composition-skill && \
grep -c "L2 global" skills/jazz-composition/references/scorecard-template.md && \
grep -c "Checklist pra-L3 (fail-closed)" skills/jazz-composition/SKILL.md && \
grep -c "L3 wajib per-piece" skills/jazz-composition/references/human-ear-protocol.md && \
grep -n "Semantik fail-closed" skills/jazz-composition/references/scorecard-template.md
```
Expected: `≥1`, `1`, `1`, satu baris nomor. Lalu cek urutan: `grep -n "^## " skills/jazz-composition/references/scorecard-template.md | tail -4` harus menunjukkan `Level 14` → `L2 global` → `L3 (telinga)` berurutan.

- [ ] **Step 5: Commit**

```bash
cd /home/shendi/self-project/daw_generative/music-composition-skill && \
git add skills/jazz-composition/references/scorecard-template.md skills/jazz-composition/SKILL.md skills/jazz-composition/references/human-ear-protocol.md && \
git commit -m "feat(penilaian): 4 blocker L2 global fail-closed (D1) + L3 wajib per-piece produksi & checklist pra-L3 (D5)"
```

---

### Task 6: D2 — L2-blind, D3 — L2-cliche + register cliché, D4 — Bukti revisi

> **Dependency**: WAJIB dikerjakan SETELAH Task 5 — dua anchor di task ini
> menunjuk teks yang dibuat Task 5 (heading `### Checklist pra-L3
> (fail-closed)` di SKILL.md, dan heading `## L3 (telinga)` yang kini
> berada setelah bagian "L2 global" di scorecard-template).

**Files:**
- Create: `skills/jazz-composition/references/cliche-register.md` (9 entri)
- Modify: `skills/jazz-composition/SKILL.md` §Penilaian (prosedur L2-blind 5 langkah + prosedur respons L2-cliche) dan Tahap 15 (bukti revisi)
- Modify: `skills/jazz-composition/references/scorecard-template.md` (protokol L2-blind, L2-cliche, bagian Bukti revisi)
- Modify: `skills/RED-FLAGS.md` (2 baris baru)

**Interfaces:**
- Consumes: heading `### Checklist pra-L3 (fail-closed)` (Task 5, SKILL.md) sebagai titik sisip; bagian "L2 global" scorecard (Task 5).
- Produces: file `references/cliche-register.md` (dirujuk prosedur L2-cliche); istilah `L2-blind`/`L2-cliche` persis dengan tanda hubung.

- [ ] **Step 1: Buat file baru `skills/jazz-composition/references/cliche-register.md`**

Isi lengkap:

```markdown
# Register cliché — neo-soul/AI-jazz

Daftar pola yang berulang kali muncul di output paket ini dan terasa
"template di-reskin". Dipakai oleh protokol **L2-cliche** (lihat
`scorecard-template.md` bagian "L2 global" dan `../SKILL.md` §Penilaian):
reviewer segar menandai bagian notasi final yang **match** entri di bawah
**tanpa reinterpretasi yang terlihat**; composer wajib merespons tiap
temuan dengan **revisi** atau **justifikasi audible spesifik**.

Cliché **bukan larangan mutlak** — semua device di bawah valid secara
teori dan lolos rubrik. Kehadirannya tanpa reinterpretasi adalah sinyal
"template di-reskin", bukan komposisi original. Karena itu tiap entri
wajib punya tiga kolom: nama, kenapa terasa template, dan jalur
reinterpretasi yang menyelamatkan — **entri tanpa jalur reinterpretasi
tidak lengkap.**

| Cliché | Kenapa terasa template | Jalur reinterpretasi |
|---|---|---|
| Intro 2-bar pad + motif preview lalu lead masuk | Pola paling umum di semua contoh genre, nol variasi struktural | Gate intro performatif di `level-12-intro-ending.md` (incomplete voicing / delayed entrance / frase "mencari" / ruang disengaja) |
| Ending fade + held tonic | Sama, default paling aman | Opsi rekontekstualisasi di `level-12-intro-ending.md` (nada tegang dipertahankan, harmoni di bawahnya berubah hingga nada itu terasa diterima) |
| Chromatic approach di tiap transisi bass | Approach note jadi refleks, bukan pilihan sadar | Kuota chromatic ≤1/3 + tabel device per transisi chord di `level-08-bass.md` |
| Harmonic rhythm seragam 1 chord/bar full-piece dengan semua perpindahan di barline | Tak ada variasi harmonic rhythm sama sekali | Variasikan lewat teknik `../../harmony/SKILL.md` — 2 chord/bar terukur via rumus durasi absolut per chord (≥2 detik per chord) |
| Rhodes block-chord 1 attack/bar sepanjang lagu | Comping statis, bukan dialog musikal | Gate ≥3 comping cell + pemetaan ke napas lead di `level-07-comping-voicing.md` |
| Drum pattern identik section-wide | Melanggar hierarchy drum v2 dari Gelombang 1 (base 2-bar + variation + transition) | Aturan hierarchy di `level-09-drum.md` |
| Progresi i-bVI-iv-V verbatim tanpa reinterpretasi | Progresi paling dikenal genre dipakai mentah | Reharmonize sebagian / ubah voicing / ubah bass motion |
| "Restrained = tanpa momen berarti" | Dalih untuk section datar | Gate micro-apex di `level-13-dinamika-dramaturgi.md` (satu bar mekanisme non-volume) |
| Velocity random sebagai pengganti frase | `humanize_velocity` dipakai sebagai sumber variasi utama, bukan polish terakhir | `phrase_velocity` per bar (Gelombang 1 — lihat `level-09-drum.md` dan `grid_to_midi.py`) |
```

- [ ] **Step 2: Tambah prosedur L2-blind + L2-cliche ke `SKILL.md` §Penilaian**

Edit `skills/jazz-composition/SKILL.md` — sisip SEBELUM heading checklist buatan Task 5. old_string:

```
### Checklist pra-L3 (fail-closed)
```

new_string (dua subsection baru + heading lama):

```
### L2-blind — uji buta arc emosional

Verifikasi independen bahwa arc emosional benar-benar **terbaca dari
notasi**, bukan hanya konsisten dengan niat yang ditulis generator
sendiri. Prosedur:

1. Orkestrator menulis **3 opsi arc emosional**: 1 arc yang sebenarnya
   (diambil dari artefak `01-brief.md`) + 2 distractor yang masuk akal,
   ditulis **tanpa membocorkan** mana yang benar — ketiganya dengan
   detail dan keyakinan setara. Aturan authoring distractor: **berbeda
   arah arc, bukan berbeda genre** — ketiga opsi harus masuk akal untuk
   gaya/instrumentasi yang sama, hanya arah emosionalnya yang berbeda.
2. Spawn **reviewer segar** (subagent baru, tanpa histori generasi) yang
   diberi **hanya**: `song.abc`, `drums.json`, output
   `notation_facts.py`, dan 3 opsi arc di atas — **TANPA** brief asli,
   **TANPA** artefak desain lain (form, harmony, dst.), **TANPA**
   scorecard.
3. Reviewer memilih **1 opsi** + alasan tertulis — harus berbasis apa
   yang benar-benar terbaca dari notasi, bukan tebakan buta.
4. **Salah pilih** = kriteria blocker "emotional specificity" (L2 global
   #4) otomatis mendapat skor **0** — terhubung langsung ke aturan
   fail-closed di atas.
5. Hasil (benar/salah + alasan reviewer, apa adanya) dicatat **jujur** di
   `scorecard.md` — termasuk bila hasilnya salah pilih.

L2-blind (dan L2-cliche di bawah) dijalankan subagent LLM dan menilai apa
yang bisa diverifikasi dari notasi/teks — keduanya **bukan** pengganti
telinga manusia dan tidak boleh diklaim setara dengannya (lihat Modul 7
`../vibes-mood/references/reasoning-theory.md`).

### L2-cliche — audit originalitas

Reviewer segar (subagent baru) diberi **notasi final + register cliché**
(`references/cliche-register.md`) → menandai bagian yang **match**
register **tanpa reinterpretasi yang terlihat**. Composer wajib merespons
**tiap temuan** dengan salah satu:

- **revisi** artefak/notasi terkait, atau
- **justifikasi audible spesifik** — mekanisme konkret yang bisa didengar
  kenapa device itu dipertahankan. Justifikasi generik ("ini disengaja")
  tanpa mekanisme yang bisa didengar = **tidak diterima**; lihat
  `../RED-FLAGS.md`.

Temuan + respons dicatat di bagian L2-cliche `scorecard.md`.

### Checklist pra-L3 (fail-closed)
```

- [ ] **Step 3: Tambah kewajiban Bukti revisi ke Tahap 15 `SKILL.md`**

Edit `skills/jazz-composition/SKILL.md`. old_string:

```
**Tahap 15 — Revisi low level** → artefak `14-review.md`
Perbaiki:

* voice leading
* interval
* phrasing
* density
* voicing
* bass line
* drum setup
* articulation
```

new_string:

```
**Tahap 15 — Revisi low level** → artefak `14-review.md`
Perbaiki:

* voice leading
* interval
* phrasing
* density
* voicing
* bass line
* drum setup
* articulation

**Bukti revisi (wajib sebelum run disebut selesai):** `14-review.md` dan
bagian "Bukti revisi" di `scorecard.md` memuat **≥1 pasangan
before/after** untuk **2 masalah terbesar** yang ditemukan
L1/L2-rubrik/L2-blind/L2-cliche manapun. Setiap pasangan wajib: (a)
kutip notasi/nilai **lama → baru** (bukan deskripsi umum "diperbaiki
voicing-nya"); (b) 1 kalimat **efek yang diharapkan terdengar** dari
perubahan itu. Pasangan harus **terhubung ke temuan nyata** yang
tercatat — bukan revisi kosmetik berdiri sendiri; reviewer L2 berikutnya
boleh menolak pasangan yang tidak menjawab temuan mana pun. Run tanpa
satu pun revisi tercatat = red flag "first draft dianggap final" (lihat
`../RED-FLAGS.md`).
```

- [ ] **Step 4: Tambah protokol L2-blind + L2-cliche + Bukti revisi ke scorecard-template**

Edit `skills/jazz-composition/references/scorecard-template.md` — sisip SEBELUM heading L3 (setelah Task 5, sisipan ini otomatis jatuh setelah bagian "L2 global"). old_string:

```
## L3 (telinga) — hanya diisi sekali, di akhir
```

new_string:

```
### L2-blind — uji buta arc emosional

Prosedur lengkap di `SKILL.md` §Penilaian (3 opsi arc → reviewer segar
dengan diet informasi ketat → pilih 1 + alasan). Catat di sini, jujur:

| Field | Isi |
|---|---|
| 3 opsi arc (verbatim, tanpa menandai yang benar) | |
| Opsi yang dipilih reviewer segar | |
| Arc sebenarnya (dari `01-brief.md`) | |
| Hasil | benar / salah |
| Alasan reviewer (apa adanya) | |

**Salah pilih** = kriteria blocker #4 (emotional specificity) otomatis
**0** — fail-closed, run belum selesai.

### L2-cliche — audit originalitas

Reviewer segar menandai match terhadap `cliche-register.md`; composer
merespons tiap temuan (prosedur di `SKILL.md` §Penilaian):

| Temuan (entri register + lokasi bar) | Respons (revisi / justifikasi audible) | Detail respons |
|---|---|---|

Temuan tanpa respons = run belum selesai. Justifikasi generik ("ini
disengaja") tanpa mekanisme yang bisa didengar = tidak diterima.

## Bukti revisi (wajib sebelum run disebut selesai)

≥1 pasangan before/after untuk 2 masalah terbesar yang ditemukan
L1/L2-rubrik/L2-blind/L2-cliche (lihat `SKILL.md` Tahap 15):

| Temuan (sumber: L1/L2-rubrik/L2-blind/L2-cliche) | Before (kutipan notasi/nilai lama) | After (kutipan baru) | Efek yang diharapkan terdengar (1 kalimat) |
|---|---|---|---|

Run tanpa satu pun revisi tercatat = red flag "first draft dianggap
final" (`RED-FLAGS.md`).

## L3 (telinga) — hanya diisi sekali, di akhir
```

- [ ] **Step 5: Tambah 2 baris baru ke `skills/RED-FLAGS.md`**

Edit `skills/RED-FLAGS.md`. old_string (baris terakhir tabel saat ini):

```
| "Motif ini 4-not, arpeggio-nya outside, chord-nya borrowed — sesuai yang kutulis." | Label teori di prosa sering tak cocok notasi aktual: motif "4-not" yang nyatanya 3 pitch (rest bukan pitch), arpeggio chord-tone yang dilabeli "outside", chord diatonik yang disebut "borrowed", klaim top-note yang beda dari voicing tertulis. Jangan percaya label sebelum dicek terhadap fakta notasi yang sebenarnya berbunyi. | skills/abc-notation/scripts/notation_facts.py (jalankan pada ABC-nya; gate wajib di DoD Level 3/4/7) |
```

new_string:

```
| "Motif ini 4-not, arpeggio-nya outside, chord-nya borrowed — sesuai yang kutulis." | Label teori di prosa sering tak cocok notasi aktual: motif "4-not" yang nyatanya 3 pitch (rest bukan pitch), arpeggio chord-tone yang dilabeli "outside", chord diatonik yang disebut "borrowed", klaim top-note yang beda dari voicing tertulis. Jangan percaya label sebelum dicek terhadap fakta notasi yang sebenarnya berbunyi. | skills/abc-notation/scripts/notation_facts.py (jalankan pada ABC-nya; gate wajib di DoD Level 3/4/7) |
| "First draft-nya sudah solid — tidak ada yang perlu direvisi." | Run tanpa satu pun revisi tercatat berarti temuan L1/L2-rubrik/L2-blind/L2-cliche tidak pernah benar-benar dijawab — "first draft dianggap final" adalah pola gagal, bukan bukti kualitas. Sebelum run disebut selesai wajib ada bagian "Bukti revisi": ≥1 pasangan before/after untuk 2 masalah terbesar, terhubung ke temuan nyata. | skills/jazz-composition/SKILL.md Tahap 15; skills/jazz-composition/references/scorecard-template.md bagian "Bukti revisi" |
| "Device ini memang disengaja — sudah kubilang begitu." | Justifikasi tanpa mekanisme audible yang konkret bukan justifikasi — itu pembelaan. Temuan L2-cliche hanya boleh dijawab dengan revisi ATAU justifikasi audible spesifik (mekanisme yang bisa didengar kenapa device dipertahankan); "ini disengaja" polos tidak diterima. | skills/jazz-composition/references/cliche-register.md; scorecard-template.md bagian L2-cliche |
```

- [ ] **Step 6: Verifikasi ejaan istilah + struktur**

Run:
```bash
cd /home/shendi/self-project/daw_generative/music-composition-skill && \
grep -rn "L2 blind\|l2-blind\|Blind L2\|L2 cliche\|L2-cliché\|l2-cliche" skills/ ; echo "exit=$?" && \
grep -c "^| " skills/jazz-composition/references/cliche-register.md && \
grep -n "^## \|^### " skills/jazz-composition/references/scorecard-template.md | tail -8
```
Expected: grep ejaan salah TIDAK menemukan apa pun (`exit=1`); tabel cliché punya `10` baris berawalan `| ` (1 header + 9 entri; baris separator berawalan `|-` tidak terhitung); 8 heading terakhir scorecard menunjukkan urutan relatif `## Level 14` (beserta `### L1`/`### L2`-nya) → `## L2 global` → `### L2-blind` → `### L2-cliche` → `## Bukti revisi` → `## L3 (telinga)`.

- [ ] **Step 7: Commit**

```bash
cd /home/shendi/self-project/daw_generative/music-composition-skill && \
git add skills/jazz-composition/references/cliche-register.md skills/jazz-composition/SKILL.md skills/jazz-composition/references/scorecard-template.md skills/RED-FLAGS.md && \
git commit -m "feat(penilaian): L2-blind uji buta arc (D2), L2-cliche + register cliché (D3), bukti revisi wajib (D4)"
```

---

### Task 7: E2 — Konverter `drums_to_engine.py` (TDD) + E3 — Penyelarasan `PROGRAM` map

**Files:**
- Create: `skills/midi-orchestration/scripts/test_drums_to_engine.py`
- Create: `skills/midi-orchestration/scripts/drums_to_engine.py`
- Modify: `skills/midi-orchestration/scripts/test_abc_to_midi_and_grid.py` (test guard PROGRAM baru)
- Modify: `skills/midi-orchestration/scripts/abc_to_midi.py` (dict `PROGRAM`)
- Test fixture (dibaca, tidak diubah): `skills/midi-orchestration/assets/drum-grid-template.json`

**Interfaces:**
- Produces: `drums_to_engine.convert(spec: dict) -> dict` — input dict `drums.json` Tool 1 (v1/v2), output dict skema engine `/api/render` murni; WARNING field yang dibuang dicetak ke **stderr**; `ValueError` untuk nilai yang pasti ditolak engine. CLI: `python drums_to_engine.py <drums.json> [drums-engine.json]` (tanpa arg kedua → cetak JSON ke stdout). Dirujuk Task 8 (engine-export.md + langkah 1 section Export produksi).
- Produces: `PROGRAM` di `abc_to_midi.py` selaras registry engine: `sax` **66**, `guitar` **26**, `bass` **32**, entri baru `vibraphone` **11**, `synth-lead` **81**, `guitar-clean` **27**; `horns` 61/`upright` 32/`strings` 48/`pad` 89/`trumpet` 56/`rhodes` 4/`piano` 0 tetap.

- [ ] **Step 1: Tulis test yang gagal — `skills/midi-orchestration/scripts/test_drums_to_engine.py`**

Konten lengkap (pure stdlib — pola `importlib` mengikuti `test_abc_to_midi_and_grid.py`):

```python
from __future__ import annotations

import contextlib
import importlib.util
import io
import json
import sys
import unittest
from pathlib import Path

SCRIPTS_DIR = Path(__file__).resolve().parents[0]
TEMPLATE_PATH = SCRIPTS_DIR.parent / "assets" / "drum-grid-template.json"


def _load(module_name: str, filename: str):
    module_path = SCRIPTS_DIR / filename
    spec = importlib.util.spec_from_file_location(module_name, module_path)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


drums_to_engine = _load("jazz_drums_to_engine", "drums_to_engine.py")

BAR_A = {"kick": "x.......", "chh": "x.x.x.x."}
BAR_B = {"kick": "x...x...", "chh": "x.x.x.x."}
BAR_C = {"kick": "....x...", "snare": "....x..."}


def make_spec(sections) -> dict:
    return {
        "steps_per_bar": 8,
        "gm_map": {"kick": 36, "snare": 38, "chh": 42},
        "base_velocity": {"kick": 96, "snare": 82, "chh": 58},
        "swing": 0.56,
        "sections": sections,
    }


def convert_quiet(spec):
    """Jalankan convert() sambil menangkap stderr (warning) untuk di-assert."""
    stderr = io.StringIO()
    with contextlib.redirect_stderr(stderr):
        engine = drums_to_engine.convert(spec)
    return engine, stderr.getvalue()


class V2MergeTests(unittest.TestCase):
    def test_v2_four_bars_two_identical_then_two_distinct_gives_three_sections(self):
        # Test wajib spec E2 #1: 4 bar (2 identik berurutan + 2 beda)
        # -> sections [{bars:2}, {bars:1}, {bars:1}]
        spec = make_spec([{"bars": 4, "pattern": [BAR_A, BAR_A, BAR_B, BAR_C]}])
        engine, _ = convert_quiet(spec)
        self.assertEqual([s["bars"] for s in engine["sections"]], [2, 1, 1])
        self.assertEqual(engine["sections"][0]["pattern"], BAR_A)
        self.assertEqual(engine["sections"][1]["pattern"], BAR_B)
        self.assertEqual(engine["sections"][2]["pattern"], BAR_C)


class V1PassthroughTests(unittest.TestCase):
    def test_v1_dict_pattern_passes_through_as_single_section(self):
        # Test wajib spec E2 #2: v1 pattern-dict -> passthrough satu section.
        spec = make_spec([{"bars": 4, "pattern": BAR_A}])
        engine, _ = convert_quiet(spec)
        self.assertEqual(engine["sections"], [{"bars": 4, "pattern": BAR_A}])
        self.assertEqual(engine["steps_per_bar"], 8)
        self.assertEqual(engine["swing"], 0.56)
        self.assertEqual(
            set(engine),
            {"steps_per_bar", "gm_map", "base_velocity", "swing", "sections"},
        )


class ForeignFieldTests(unittest.TestCase):
    def test_foreign_fields_dropped_and_warned_by_name(self):
        # Test wajib spec E2 #3: field asing dibuang + warning menyebut namanya.
        spec = make_spec(
            [{"bars": 1, "pattern": BAR_A, "label": "Intro",
              "phrase_velocity": [1.0]}])
        spec["tempo_bpm"] = 90
        spec["beats_per_bar"] = 4
        spec["humanize_velocity"] = 6
        spec["timing"] = {"kick": 0}
        spec["title"] = "T"
        spec["_comment"] = "c"
        engine, warnings = convert_quiet(spec)
        for field in ("tempo_bpm", "beats_per_bar", "humanize_velocity",
                      "timing", "title", "_comment"):
            self.assertNotIn(field, engine)
            self.assertIn(field, warnings)
        self.assertEqual(set(engine["sections"][0]), {"bars", "pattern"})
        self.assertIn("phrase_velocity", warnings)
        self.assertIn("label", warnings)
        self.assertIn("WARNING", warnings)


class ValidationTests(unittest.TestCase):
    def test_invalid_steps_per_bar_raises_with_clear_message(self):
        # Test wajib spec E2 #4: steps_per_bar di luar {8,12,16} -> error jelas.
        spec = make_spec([{"bars": 1, "pattern": BAR_A}])
        spec["steps_per_bar"] = 10
        with self.assertRaises(ValueError) as ctx:
            convert_quiet(spec)
        self.assertIn("steps_per_bar", str(ctx.exception))
        self.assertIn("10", str(ctx.exception))

    def test_invalid_pattern_char_raises(self):
        spec = make_spec([{"bars": 1, "pattern": {"kick": "x..?...."}}])
        with self.assertRaises(ValueError) as ctx:
            convert_quiet(spec)
        self.assertIn("kick", str(ctx.exception))

    def test_gm_map_out_of_range_raises(self):
        spec = make_spec([{"bars": 1, "pattern": BAR_A}])
        spec["gm_map"]["kick"] = 90  # > 81
        with self.assertRaises(ValueError) as ctx:
            convert_quiet(spec)
        self.assertIn("gm_map", str(ctx.exception))

    def test_base_velocity_out_of_range_raises(self):
        spec = make_spec([{"bars": 1, "pattern": BAR_A}])
        spec["base_velocity"]["kick"] = 0
        with self.assertRaises(ValueError) as ctx:
            convert_quiet(spec)
        self.assertIn("base_velocity", str(ctx.exception))

    def test_v2_pattern_list_length_mismatch_raises(self):
        spec = make_spec([{"bars": 3, "pattern": [BAR_A]}])
        with self.assertRaises(ValueError):
            convert_quiet(spec)


class TemplateRegressionTests(unittest.TestCase):
    def test_current_template_asset_converts_to_valid_engine_schema(self):
        # Test wajib spec E2 #5: template asset SAAT INI sebagai regression
        # fixture (bukan fixture buatan sendiri).
        spec = json.loads(TEMPLATE_PATH.read_text(encoding="utf-8"))
        engine, _ = convert_quiet(spec)
        self.assertEqual(
            set(engine),
            {"steps_per_bar", "gm_map", "base_velocity", "swing", "sections"},
        )
        self.assertIn(engine["steps_per_bar"], (8, 12, 16))
        for note in engine["gm_map"].values():
            self.assertTrue(35 <= note <= 81)
        for vel in engine["base_velocity"].values():
            self.assertTrue(1 <= vel <= 127)
        # Template: intro 2 bar (dict) + A 4 bar (list, semua bar beda karena
        # rimshot bar-2 beda) + B 4 bar (bar 1-2 identik -> merge) + outro 2
        # bar (dict) = total 12 bar, 9 section engine.
        self.assertEqual(sum(s["bars"] for s in engine["sections"]), 12)
        self.assertEqual(len(engine["sections"]), 9)
        for section in engine["sections"]:
            self.assertEqual(set(section), {"bars", "pattern"})
            self.assertGreaterEqual(section["bars"], 1)
            for row in section["pattern"].values():
                self.assertTrue(set(row) <= set("xXg."))


if __name__ == "__main__":
    unittest.main()
```

- [ ] **Step 2: Jalankan test — pastikan gagal**

Run: `cd /home/shendi/self-project/daw_generative/music-composition-skill/skills/midi-orchestration/scripts && uv run python -m unittest test_drums_to_engine -v`

Expected: GAGAL saat import dengan `FileNotFoundError` (modul `drums_to_engine.py` belum ada — `_load` gagal meng-exec file). Bukan `OK`.

- [ ] **Step 3: Tulis implementasi — `skills/midi-orchestration/scripts/drums_to_engine.py`**

Konten lengkap (pure stdlib, tanpa dependensi):

```python
#!/usr/bin/env python3
"""Convert drums.json Tool 1 (grid v1/v2, lihat grid_to_midi.py) menjadi
skema `drums` engine daw_generative `POST /api/render`.

Skema engine (lihat ../references/engine-export.md):

    {
      "steps_per_bar": 8 | 12 | 16,
      "gm_map": {voice: 35..81},
      "base_velocity": {voice: 1..127},
      "swing": 0.5..0.75 (opsional, diteruskan apa adanya),
      "sections": [{"bars": int >= 1, "pattern": {voice: "x.Xg..."}}]
    }

Aturan konversi (spec E2):
- (a) pattern dict (v1) -> satu section {bars, pattern} apa adanya.
- (b) pattern list (v2, satu dict per bar) -> dipecah per bar, lalu bar
  berurutan yang identik digabung jadi satu section {bars: N}. Merging
  TIDAK melintasi batas section input (batas section = keputusan musikal).
- (c) Field yang tak dikenal skema engine (phrase_velocity, timing,
  humanize_velocity, label, title, tempo_bpm, beats_per_bar, _comment,
  dll.) DIBUANG dengan WARNING eksplisit ke stderr menyebut nama field —
  bukan silent drop. Nuansa phrase_velocity/timing TIDAK terbawa ke WAV;
  pengganti engine: swing grid + groove profile %%pocket.
- (d) steps_per_bar, gm_map, base_velocity, swing dipertahankan apa adanya.
- (e) Validasi fail-fast (bukan 422 misterius di titik render):
  steps_per_bar di {8,12,16}; nilai gm_map 35-81; nilai base_velocity
  1-127; karakter pola hanya x/X/g/. .

Baris pattern berbentuk list per-step (bentuk yang juga diterima
grid_to_midi.py, "" berarti rest) dinormalisasi ke string engine
("" -> "."). Usage:

    python drums_to_engine.py drums.json [drums-engine.json]

Tanpa argumen kedua, JSON skema engine dicetak ke stdout.
"""
import json
import sys

TOP_LEVEL_KEEP = ("steps_per_bar", "gm_map", "base_velocity", "swing")
SECTION_KEEP = ("bars", "pattern")
VALID_STEPS_PER_BAR = (8, 12, 16)
VALID_CHARS = set("xXg.")


def _warn(message):
    print(f"WARNING: {message}", file=sys.stderr)


def _normalize_row(voice, row):
    """Kembalikan bentuk string engine untuk satu baris pattern; validasi karakter."""
    if isinstance(row, list):
        chars = []
        for step in row:
            if step in ("", "."):
                chars.append(".")
            elif step in ("x", "X", "g"):
                chars.append(step)
            else:
                raise ValueError(
                    f"pattern voice {voice!r}: step {step!r} tidak valid — "
                    "hanya 'x'/'X'/'g'/'.'/'' yang dikenal skema engine"
                )
        return "".join(chars)
    if not isinstance(row, str):
        raise ValueError(
            f"pattern voice {voice!r}: harus string atau list, "
            f"dapat {type(row).__name__}"
        )
    bad = set(row) - VALID_CHARS
    if bad:
        raise ValueError(
            f"pattern voice {voice!r}: karakter tidak dikenal {sorted(bad)!r} — "
            "skema engine hanya menerima 'x'/'X'/'g'/'.'"
        )
    return row


def _normalize_pattern(pattern):
    return {voice: _normalize_row(voice, row) for voice, row in pattern.items()}


def _sections_from(section, index):
    """Hasilkan section engine {bars, pattern} dari satu section Tool 1."""
    bars = section["bars"]
    pattern = section["pattern"]
    if isinstance(pattern, dict):  # v1: passthrough tanpa pemecahan
        yield {"bars": bars, "pattern": _normalize_pattern(pattern)}
        return
    if len(pattern) != bars:  # v2 list — cermin validasi grid_to_midi.py
        raise ValueError(
            f"sections[{index}]: pattern list punya {len(pattern)} bar "
            f"tapi section['bars'] = {bars}; harus sama persis"
        )
    per_bar = [_normalize_pattern(p) for p in pattern]
    run_pattern, run_bars = per_bar[0], 1
    for pat in per_bar[1:]:
        if pat == run_pattern:
            run_bars += 1
        else:
            yield {"bars": run_bars, "pattern": run_pattern}
            run_pattern, run_bars = pat, 1
    yield {"bars": run_bars, "pattern": run_pattern}


def convert(spec):
    """Konversi dict drums.json Tool 1 (v1/v2) -> dict `drums` skema engine.

    WARNING ke stderr untuk tiap field yang dibuang; ValueError untuk nilai
    yang pasti ditolak engine (fail cepat di sini, bukan 422 di render).
    """
    dropped = sorted(set(spec) - set(TOP_LEVEL_KEEP) - {"sections"})
    for field in dropped:
        _warn(
            f"field {field!r} dibuang: tidak dikenal skema engine /api/render "
            "(nuansa phrase_velocity/timing tidak terbawa ke WAV; engine "
            "memakai swing grid + %%pocket sebagai gantinya)"
        )

    steps = spec.get("steps_per_bar")
    if steps not in VALID_STEPS_PER_BAR:
        raise ValueError(
            f"steps_per_bar = {steps!r} tidak valid — skema engine hanya "
            f"menerima {list(VALID_STEPS_PER_BAR)}"
        )

    gm_map = spec["gm_map"]
    for voice, note in gm_map.items():
        if not isinstance(note, int) or not 35 <= note <= 81:
            raise ValueError(
                f"gm_map[{voice!r}] = {note!r} di luar rentang note perkusi "
                "GM engine 35-81"
            )

    base_velocity = spec["base_velocity"]
    for voice, vel in base_velocity.items():
        if not isinstance(vel, int) or not 1 <= vel <= 127:
            raise ValueError(
                f"base_velocity[{voice!r}] = {vel!r} di luar rentang 1-127"
            )

    engine = {
        "steps_per_bar": steps,
        "gm_map": gm_map,
        "base_velocity": base_velocity,
    }
    if "swing" in spec:
        engine["swing"] = spec["swing"]

    sections = []
    for index, section in enumerate(spec["sections"]):
        for field in sorted(set(section) - set(SECTION_KEEP)):
            _warn(
                f"sections[{index}] field {field!r} dibuang: tidak dikenal "
                "skema engine /api/render"
            )
        sections.extend(_sections_from(section, index))
    engine["sections"] = sections
    return engine


def main(argv):
    if len(argv) < 2:
        print("usage: drums_to_engine.py <drums.json> [drums-engine.json]",
              file=sys.stderr)
        return 2
    with open(argv[1]) as fh:
        spec = json.load(fh)
    engine = convert(spec)
    out = json.dumps(engine, indent=2)
    if len(argv) > 2:
        with open(argv[2], "w") as fh:
            fh.write(out + "\n")
        total = sum(s["bars"] for s in engine["sections"])
        print(f"wrote {argv[2]}: {len(engine['sections'])} sections, "
              f"{total} bars")
    else:
        print(out)
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
```

- [ ] **Step 4: Jalankan test — pastikan lulus**

Run: `cd /home/shendi/self-project/daw_generative/music-composition-skill/skills/midi-orchestration/scripts && uv run python -m unittest test_drums_to_engine -v`

Expected: `Ran 9 tests ... OK` (konvensi terverifikasi: test ini pure stdlib, TIDAK butuh `--with music21 --with pretty_midi`).

- [ ] **Step 5: Tulis test guard PROGRAM yang gagal — `test_abc_to_midi_and_grid.py`**

Edit `skills/midi-orchestration/scripts/test_abc_to_midi_and_grid.py`. old_string (penutup file):

```python
if __name__ == "__main__":
    unittest.main()
```

new_string:

```python
class ProgramMapEngineRegistryTests(unittest.TestCase):
    """E3: PROGRAM selaras registry engine daw_generative
    (src/instruments/registry.js — lihat
    skills/midi-orchestration/references/engine-export.md)."""

    def test_keywords_shared_with_engine_registry_use_engine_gm_numbers(self):
        expected = {
            "sax": 66, "piano": 0, "guitar": 26, "bass": 32, "rhodes": 4,
            "trumpet": 56, "vibraphone": 11, "guitar-clean": 27,
            "synth-lead": 81,
        }
        for keyword, program in expected.items():
            self.assertEqual(abc_to_midi.PROGRAM[keyword], program, keyword)

    def test_legacy_keywords_preserved(self):
        # Di luar cakupan registry engine — dipertahankan, bukan dihapus.
        legacy = {"horns": 61, "upright": 32, "strings": 48, "pad": 89}
        for keyword, program in legacy.items():
            self.assertEqual(abc_to_midi.PROGRAM[keyword], program, keyword)

    def test_program_for_prefers_compound_keyword_over_substring(self):
        # 'guitar-clean' harus menang atas substring 'guitar' (urutan dict).
        self.assertEqual(abc_to_midi.program_for("Guitar-Clean"), 27)
        self.assertEqual(abc_to_midi.program_for("Jazz Guitar"), 26)
        self.assertEqual(abc_to_midi.program_for("Synth-Lead"), 81)
        self.assertEqual(abc_to_midi.program_for("Vibraphone"), 11)


if __name__ == "__main__":
    unittest.main()
```

- [ ] **Step 6: Jalankan suite — pastikan test baru gagal**

Run: `cd /home/shendi/self-project/daw_generative/music-composition-skill/skills/midi-orchestration/scripts && uv run --with music21 --with pretty_midi python -m unittest test_abc_to_midi_and_grid -v`

Expected: `FAILED` — 2 dari 3 test `ProgramMapEngineRegistryTests` gagal: `test_keywords_shared_with_engine_registry...` (`KeyError: 'vibraphone'` / assert `65 != 66`) dan `test_program_for_prefers_compound_keyword...` (`program_for("Jazz Guitar")` masih 27, bukan 26). `test_legacy_keywords_preserved` LULUS sejak awal (nilai legacy memang tidak berubah — itu guard anti-penghapusan, bukan guard perubahan). 14 test lama tetap lulus.

- [ ] **Step 7: Selaraskan dict `PROGRAM` di `abc_to_midi.py`**

Edit `skills/midi-orchestration/scripts/abc_to_midi.py`. old_string:

```python
PROGRAM = {"sax":65,"horns":61,"trumpet":56,"rhodes":4,"piano":0,"bass":33,
           "upright":32,"strings":48,"pad":89,"guitar":27}
```

new_string:

```python
# Selaras registry instrumen engine daw_generative (src/instruments/
# registry.js — lihat ../references/engine-export.md): keyword yang sama
# menghasilkan nomor GM yang sama supaya preview MIDI Tool 1 dan WAV engine
# tidak diam-diam beda timbre. Keyword majemuk (guitar-clean, synth-lead)
# HARUS di depan keyword substring-nya karena program_for mencocokkan
# substring berurutan. horns/upright/strings/pad tidak dikurasi registry
# engine — dipertahankan dengan nilai lamanya.
PROGRAM = {"guitar-clean":27,"synth-lead":81,"vibraphone":11,
           "sax":66,"horns":61,"trumpet":56,"rhodes":4,"piano":0,"bass":32,
           "upright":32,"strings":48,"pad":89,"guitar":26}
```

- [ ] **Step 8: Jalankan suite penuh — pastikan semua lulus**

Run: `cd /home/shendi/self-project/daw_generative/music-composition-skill/skills/midi-orchestration/scripts && uv run --with music21 --with pretty_midi python -m unittest test_abc_to_midi_and_grid -v`

Expected: `Ran 17 tests ... OK` (14 lama + 3 baru; baseline sebelum task ini: `Ran 14 tests ... OK`, terverifikasi saat plan ditulis).

- [ ] **Step 9: Smoke-test CLI konverter atas template asset**

Run:
```bash
cd /home/shendi/self-project/daw_generative/music-composition-skill/skills/midi-orchestration/scripts && \
uv run python drums_to_engine.py ../assets/drum-grid-template.json 2>/dev/null | \
uv run python -c "import json,sys; d=json.load(sys.stdin); print(sorted(d.keys()), sum(s['bars'] for s in d['sections']))"
```
Expected: `['base_velocity', 'gm_map', 'sections', 'steps_per_bar', 'swing'] 12` (stderr berisi WARNING field yang dibuang — disembunyikan di sini, itu perilaku benar).

- [ ] **Step 10: Commit**

```bash
cd /home/shendi/self-project/daw_generative/music-composition-skill && \
git add skills/midi-orchestration/scripts/drums_to_engine.py skills/midi-orchestration/scripts/test_drums_to_engine.py skills/midi-orchestration/scripts/abc_to_midi.py skills/midi-orchestration/scripts/test_abc_to_midi_and_grid.py && \
git commit -m "feat(midi-orchestration): konverter drums.json Tool 1 -> skema engine (E2) + selaraskan PROGRAM map ke registry engine (E3)"
```

---

### Task 8: E1 — `engine-export.md`, E3 — Gate instrumentasi Level 1, E4 — Wiring export

> **Dependency**: dikerjakan SETELAH Task 7 (merujuk `drums_to_engine.py`
> yang harus sudah ada) dan setelah Task 5-6 (sisipan scorecard jatuh
> setelah bagian L2 global/Bukti revisi; section export SKILL.md merujuk
> checklist pra-L3).

**Files:**
- Create: `skills/midi-orchestration/references/engine-export.md`
- Modify: `skills/jazz-composition/references/level-01-konsep.md` (gate instrumentasi registry)
- Modify: `skills/jazz-composition/SKILL.md` (section baru `## Export produksi (Tool 2 — engine daw_generative)` di akhir file)
- Modify: `skills/jazz-composition/references/level-14-detail.md` (referensi silang)
- Modify: `skills/jazz-composition/references/scorecard-template.md` (bagian "Export")
- Modify: `.gitignore` (baris `runs/*/render.wav`)

**Interfaces:**
- Consumes: `skills/midi-orchestration/scripts/drums_to_engine.py` (Task 7).
- Produces: file `references/engine-export.md` (dirujuk level-01, SKILL.md, abc_to_midi.py, test guard Task 7); section `## Export produksi (Tool 2 — engine daw_generative)` di SKILL.md (dirujuk level-14 dan scorecard).

- [ ] **Step 1: Buat file baru `skills/midi-orchestration/references/engine-export.md`**

Isi lengkap (semua fakta engine diverifikasi dari kode repo induk `/home/shendi/self-project/daw_generative` saat spec & plan ditulis — `vite-plugin-render.js`, `src/instruments/registry.js`, `src/instruments/palettes.js`):

````markdown
# Export produksi via engine daw_generative (Tool 2)

Referensi tunggal untuk flow export Tool 1 → Tool 2: server dev mana yang
harus hidup, kontrak HTTP persis, skema `drums` yang diterima ENGINE
(berbeda dari skema Tool 1 v1/v2 di `../assets/drum-grid-template.json`),
dan batasan lingkungan (soundfont/ffmpeg) yang bisa membuat export gagal
di luar kendali composer.

Paket ini (Tool 1) TIDAK merender audio — WAV 100% dihasilkan Tool 2 di
luar repo ini; file ini hanya mendokumentasikan cara memicunya. Titik
wiring di workflow: `../../jazz-composition/SKILL.md` §"Export produksi
(Tool 2 — engine daw_generative)".

## Prasyarat

- **Server dev engine hidup**: `npm run dev` dijalankan dari **ROOT repo
  induk** `/home/shendi/self-project/daw_generative` (Vite dev
  middleware — `vite-plugin-render.js` via `vite.config.js` — dev-only;
  tidak ada build/production server terpisah untuk endpoint ini).
- **Port**: default Vite **5173**, TAPI **auto-increment** bila port
  terpakai — **WAJIB membaca port sesungguhnya dari log terminal**
  `npm run dev`, bukan mengasumsikan 5173.
- **Soundfont GM `FluidR3_GM.sf2` TIDAK auto-download.** Dicek berurutan:
  1. env `NEO_SOUL_SOUNDFONT`;
  2. cache `~/.cache/hermes-neo-soul-soundfonts/fluidr3/usr/share/sounds/sf2/FluidR3_GM.sf2`;
  3. path sistem `/usr/share/sounds/sf2/FluidR3_GM.sf2`.

  Cek dulu mana yang ada SEBELUM mencoba render — tak satu pun ada →
  status export **PENDING** (lihat langkah 5 section export di
  `../../jazz-composition/SKILL.md`), bukan dipaksakan gagal diam-diam.
- **`fluidsynth` auto-bootstrap** (unduh `.deb` via `apt-get download`)
  bila absen dari PATH/cache — tak perlu instalasi manual di happy-path.
- **`ffmpeg` wajib ada di PATH** bila `mastering` bukan `false` (default
  `mastering` = `'neo-soul'`, jadi ffmpeg wajib di jalur default).

## Request

`POST http://127.0.0.1:<port>/api/render`, header
`content-type: application/json`, body `{abc, drums?, mastering?}`.

- `abc` — string ABC lengkap (multi-voice).
- `drums` — opsional, **skema ENGINE** (lihat di bawah) — hasil konversi
  `../scripts/drums_to_engine.py` dari `drums.json` Tool 1.
- `mastering` — `'neo-soul'` (default bila field absen), `'legacy'`, atau
  `false` (tanpa mastering). Boolean **`true` DITOLAK** (422) — berbeda
  dari jalur legacy octet-stream (di luar kontrak JSON ini) yang menerima
  `true` → profil `'legacy'`.
- Body dibatasi **1 MB** — lebih besar → **413**, ditolak begitu
  akumulasi byte melewati cap (tidak menunggu body selesai diterima).

## Skema `drums` — skema ENGINE, BUKAN skema Tool 1

```
{
  steps_per_bar: 8 | 12 | 16,
  gm_map: { voice: <35..81> },
  base_velocity: { voice: <1..127> },
  swing?: <0.5..0.75>,
  sections: [ { bars: <int >= 1>, pattern: { voice: "x.Xg..." } } ]
}
```

Karakter pola hanya `x` (hit normal), `X` (aksen), `g` (ghost), `.` (off).

**Semantik velocity engine BERBEDA dari Tool 1** — divergensi ini
didokumentasikan, bukan disamakan:

| Karakter | Engine | Tool 1 (`grid_to_midi.py`) |
|---|---|---|
| `X` | base_velocity **+12** (cap 127) | base_velocity **×1.2** |
| `g` | **35 tetap** (nilai absolut) | base_velocity **×0.45** |

WAV hasil engine adalah artefak produksi **otoritatif** untuk
timbre/velocity aktual; output MIDI Tool 1 tetap alat validasi struktural
lokal (bar/not/tempo).

Format Tool 1 **v2** (pattern list per-bar + `phrase_velocity` +
top-level `timing`) **TIDAK diterima langsung oleh engine** — wajib
dikonversi dulu lewat `../scripts/drums_to_engine.py`. `phrase_velocity`
dan `timing` **tidak ikut terbawa** ke hasil export (keterbatasan skema
engine yang tercatat, bukan bug tersembunyi — konverter mencetak WARNING
di titik konversi); engine punya penggantinya sendiri: swing grid +
groove profile `%%pocket`.

## Cross-check bar

Total bar `drums` (jumlah `sections[].bars`) **WAJIB sama** dengan jumlah
bar ABC (dihitung dari not terjauh di semua track; bar kosong di ekor
tidak terhitung) — mismatch → **422** dengan body
`{error, abcBars, gridBars}`.

## `%%pocket`

Hanya id **`neo-soul-core`** yang valid (satu-satunya profil groove
terdaftar di engine). Directive ini **tune-level**: harus muncul
**sebelum voice pertama aktif** di ABC — kemunculan setelah voice aktif
**diabaikan diam-diam** (bukan error).

## Respons sukses

**200**, body **binary WAV** (`content-type: audio/wav`), plus header
`X-Conformance-Summary` — JSON satu baris ringkas: jumlah bar, total not,
jumlah track, velocity-std minimum antar track melodis, pct-on-grid
maksimum, id pocket + status konformansinya. Header ini **non-gating** —
nilai apa pun tetap 200. Simpan body ke `runs/<run>/render.wav`; catat
isi `X-Conformance-Summary` di `scorecard.md` bagian "Export".
`render.wav` **tidak dicommit** (`.gitignore` root repo ini:
`runs/*/render.wav`).

## Pra-cek murah tanpa render penuh

`node scripts/conformance-audit.mjs <song.abc> [drums-engine.json]`
dijalankan dari root repo induk — menjalankan pipeline gate yang sama
(normalize → gate → import ABC → drum-grid → realize → audit) **tanpa**
memanggil `toMidi`/FluidSynth/ffmpeg; jauh lebih murah untuk memeriksa
apakah ABC/drums akan lolos sebelum render sungguhan.

## Error umum & batas keras

- **422** — ABC gagal gate, `drums` gagal validasi skema engine, bar
  `drums` ≠ bar ABC, atau `mastering` tak dikenal.
- **413** — body > 1 MB.
- **500** — kegagalan runtime: soundfont tak ketemu, fluidsynth/ffmpeg
  gagal atau timeout (fluidsynth 120 detik, ffmpeg 60 detik), atau hasil
  render silent yang ditangkap pemeriksaan audibilitas.
- **Batas keras render**: `maxBars` 512, `maxNotes` 50.000, `maxVoices`
  16, BPM 20-400, durasi maksimum 900 detik (15 menit).

## Registry instrumen engine (kurasi)

Sumber: `src/instruments/registry.js` repo induk. Instrumentasi run
dipilih dari menu ini — gate wajibnya ada di
`../../jazz-composition/references/level-01-konsep.md`:

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

Render engine sesungguhnya menerima **GM 0-127 penuh** (soundfont FluidR3
general-purpose, tidak dibatasi ke 12 id di atas) — registry ini adalah
**menu default yang direkomendasikan**, bukan pagar keras. GM lain di
luar tabel boleh dipakai, hanya dengan **justifikasi eksplisit** ditulis
di artefak `01-brief.md`/Level 1.

### Palet siap pakai (kombinasi id per track)

Sumber: `src/instruments/palettes.js` repo induk:

| Palet | piano → | guitar → | bass → |
|---|---|---|---|
| neo-soul-warm | rhodes | guitar-clean | bass-finger |
| jazz-cafe | piano | vibraphone | bass |
| lofi-dusty | rhodes | vibraphone | bass-finger |
| modern-chill | rhodes | synth-lead | synth-bass |

## Gotcha penentuan timbre

- **ABC final WAJIB menulis `%%MIDI program N` eksplisit per voice**
  sesuai tabel registry di atas. Name-matching otomatis engine hanya
  menebak dari keyword `sax`/`bass`/`guitar`/`piano` dan jatuh ke piano
  untuk selainnya — jangan jadikan satu-satunya jalur penentuan timbre.
- **Tool 1 `../scripts/abc_to_midi.py` MENGABAIKAN `%%MIDI program`** —
  MIDI validasi lokal menentukan program dari **keyword pada NAMA voice**
  (dict `PROGRAM`, selaras registry engine). Supaya preview lokal dan WAV
  engine setimbre: beri nama voice yang mengandung id registry (mis.
  `name="Rhodes"`, `name="Guitar-Clean"`, `name="Tenor Sax"`).
````

- [ ] **Step 2: Tambah gate instrumentasi ke `level-01-konsep.md`**

Edit `skills/jazz-composition/references/level-01-konsep.md`. old_string:

```
- Kandidat + verdict selector ditulis ke `01-konsep-candidates.md`; `01-brief.md` memakai pemenang.
```

new_string:

```
- Kandidat + verdict selector ditulis ke `01-konsep-candidates.md`; `01-brief.md` memakai pemenang.

## Gate instrumentasi — registry engine (wajib)

- Instrumentasi run **WAJIB** dipilih dari registry instrumen engine
  `daw_generative` — tabel id → nama → GM program (plus 4 palet siap
  pakai) di `../../midi-orchestration/references/engine-export.md` — ATAU
  disertai justifikasi eksplisit di `01-brief.md` bila memakai GM lain
  (engine menerima GM 0-127 penuh; registry = menu default yang
  direkomendasikan, bukan pagar keras).
- Konsekuensi hilir: ABC final (Level 14 / modul `abc-notation`)
  **WAJIB** menulis `%%MIDI program N` eksplisit per voice sesuai nomor
  tabel registry — jangan mengandalkan name-matching otomatis engine
  (hanya menebak keyword `sax`/`bass`/`guitar`/`piano`, jatuh ke piano
  untuk selainnya) sebagai satu-satunya jalur penentuan timbre.
```

- [ ] **Step 3: Tambah section export produksi di akhir `SKILL.md`**

Edit `skills/jazz-composition/SKILL.md`. old_string (kalimat penutup file saat ini):

```
Baca `../RED-FLAGS.md` — kumpulan pola "alasan yang terdengar masuk
akal, tapi realitanya tidak" yang sudah terbukti muncul berulang di paket
ini (dari section yang di-stack semua device sampai skor rubrik tinggi
yang dikira berarti enak didengar). Skor rubrik tinggi adalah lantai,
bukan langit-langit — L3 (telinga) tetap wajib sebelum menyebut sebuah
piece selesai.
```

new_string:

```
Baca `../RED-FLAGS.md` — kumpulan pola "alasan yang terdengar masuk
akal, tapi realitanya tidak" yang sudah terbukti muncul berulang di paket
ini (dari section yang di-stack semua device sampai skor rubrik tinggi
yang dikira berarti enak didengar). Skor rubrik tinggi adalah lantai,
bukan langit-langit — L3 (telinga) tetap wajib sebelum menyebut sebuah
piece selesai.

## Export produksi (Tool 2 — engine daw_generative)

Dijalankan **setelah** checklist pra-L3 (lihat §Penilaian) terpenuhi —
langkah konkret di alur "piece dianggap selesai" yang menghasilkan WAV
produksi bertimbre jujur (soundfont FluidR3_GM asli, bukan preview
browser). Kontrak lengkap:
`../midi-orchestration/references/engine-export.md`.

1. Bila run punya drum: jalankan konverter
   `../midi-orchestration/scripts/drums_to_engine.py` atas `drums.json`
   run → hasilkan `runs/<run>/drums-engine.json` (format Tool 1 v2 TIDAK
   diterima mentah oleh engine; WARNING konverter mencatat field yang
   tidak terbawa).
2. Bila repo induk `daw_generative` tersedia di mesin: pra-cek murah
   `node scripts/conformance-audit.mjs <song.abc> [drums-engine.json]`
   dari root repo induk — memeriksa ABC/drums lolos gate tanpa render
   penuh.
3. `POST /api/render` ke `http://127.0.0.1:<port>` dengan body
   `{abc, drums?, mastering?}` — **port dibaca dari log `npm run dev`**
   (auto-increment bila 5173 terpakai), bukan diasumsikan. Prasyarat
   lingkungan (soundfont 3 path, fluidsynth, ffmpeg) dan error umum:
   lihat `engine-export.md`.
4. Simpan body respons ke `runs/<run>/render.wav` (ter-ignore git); catat
   header `X-Conformance-Summary` dan profil `mastering` yang dipakai di
   bagian "Export" `scorecard.md`.
5. Bila server dev/soundfont/fluidsynth/ffmpeg **tidak tersedia** di
   lingkungan yang menjalankan run: status export dicatat **PENDING** +
   alasan konkret (mis. "soundfont tak ditemukan di 3 path yang
   dicek") — **run itu sendiri TIDAK dianggap gagal**; `output.mid`
   (Tool 1) tetap ada dan cukup untuk L3 telinga manusia, tapi WAV hasil
   engine tetap **artefak produksi otoritatif** begitu lingkungan
   tersedia.
```

- [ ] **Step 4: Tambah referensi silang di `level-14-detail.md`**

Edit `skills/jazz-composition/references/level-14-detail.md`. old_string:

```
* bagaimana transisi terjadi
```

new_string:

```
* bagaimana transisi terjadi

## Setelah level ini — export produksi

Setelah semua gate/checklist Level 14 terpenuhi (dan checklist pra-L3 di
`../SKILL.md` §Penilaian tercentang semua), jalankan section
`## Export produksi (Tool 2 — engine daw_generative)` di `../SKILL.md`:
konversi drum (`drums_to_engine.py`) → pra-cek `conformance-audit.mjs` →
`POST /api/render` → simpan `runs/<run>/render.wav` + catat
`X-Conformance-Summary` di `scorecard.md` (status **PENDING** yang jujur
bila lingkungan tidak lengkap — run tidak dianggap gagal).
```

- [ ] **Step 5: Tambah bagian "Export" ke scorecard-template**

Edit `skills/jazz-composition/references/scorecard-template.md` — sisip SEBELUM heading L3; setelah Task 5-6, sisipan ini jatuh setelah bagian "Bukti revisi" (urutan akhir: L2 global → L2-blind → L2-cliche → Bukti revisi → Export → L3). old_string:

```
## L3 (telinga) — hanya diisi sekali, di akhir
```

new_string:

```
## Export (Tool 2 — engine daw_generative)

Diisi setelah section `## Export produksi` di `SKILL.md` dijalankan
(kontrak lengkap: `midi-orchestration/references/engine-export.md`):

| Field | Isi |
|---|---|
| Status | <selesai / PENDING + alasan konkret> |
| Path | <`runs/<run>/render.wav` bila ada> |
| Conformance summary | <isi header `X-Conformance-Summary` apa adanya> |
| Mastering | <profil yang dipakai: `neo-soul` / `legacy` / `false`> |

## L3 (telinga) — hanya diisi sekali, di akhir
```

- [ ] **Step 6: Tambah baris `.gitignore`**

Edit `.gitignore` (root repo ini). old_string:

```
.venv-eval/
__pycache__/
```

new_string:

```
.venv-eval/
__pycache__/
runs/*/render.wav
```

- [ ] **Step 7: Verifikasi wiring + gitignore**

Run:
```bash
cd /home/shendi/self-project/daw_generative/music-composition-skill && \
ls skills/midi-orchestration/references/engine-export.md skills/midi-orchestration/scripts/drums_to_engine.py && \
grep -c "engine-export.md" skills/jazz-composition/references/level-01-konsep.md skills/jazz-composition/SKILL.md && \
grep -c "Export produksi (Tool 2 — engine daw_generative)" skills/jazz-composition/SKILL.md skills/jazz-composition/references/level-14-detail.md && \
git check-ignore runs/uji-coba/render.wav && \
grep -n "^## " skills/jazz-composition/references/scorecard-template.md | tail -5
```
Expected: kedua file ada; tiap grep ≥1; `git check-ignore` mencetak `runs/uji-coba/render.wav` (pola aktif); 5 heading terakhir scorecard: `Level 14` → `L2 global` → `Bukti revisi` → `Export` → `L3 (telinga)`.

- [ ] **Step 8: Verifikasi istilah lintas-file (penutup seluruh plan)**

Run:
```bash
cd /home/shendi/self-project/daw_generative/music-composition-skill && \
grep -rn "L2 blind\|l2-blind\|Blind L2\|L2 cliche\|L2-cliché" skills/ ; echo "ejaan-salah-exit=$?" && \
grep -rlni "tabel BPM band" skills/ | sort
```
Expected: pencarian ejaan salah kosong (`ejaan-salah-exit=1`); daftar file yang menyebut tabel BPM band (case-insensitive, termasuk heading kapital di `reasoning-theory.md` sendiri) mencakup ketujuh file Task 1.

- [ ] **Step 9: Commit**

```bash
cd /home/shendi/self-project/daw_generative/music-composition-skill && \
git add skills/midi-orchestration/references/engine-export.md skills/jazz-composition/references/level-01-konsep.md skills/jazz-composition/SKILL.md skills/jazz-composition/references/level-14-detail.md skills/jazz-composition/references/scorecard-template.md .gitignore && \
git commit -m "feat(export): referensi engine-export (E1), gate instrumentasi registry (E3), wiring export produksi + PENDING fallback (E4)"
```

---

## Catatan penutup untuk eksekutor

- **Uji penerimaan spec** (satu run komposisi end-to-end + export WAV
  nyata) BUKAN bagian plan ini — plan ini berhenti di perubahan
  dokumen/kode + test. Run pembuktian dilakukan setelah semua task merge,
  sesuai bagian "Uji penerimaan" spec.
- Setelah Task 8, seluruh file yang tersentuh: **22 file dimodifikasi + 4
  file baru** (`cliche-register.md`, `engine-export.md`,
  `drums_to_engine.py`, `test_drums_to_engine.py`) — cocok dengan
  "Ringkasan file yang berubah" di spec, plus 2 edit konsistensi scorecard
  (L1 Level 10/13) yang dicatat di "Keputusan penulis plan".



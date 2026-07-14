# Spec: Restrukturisasi skill music-composition-skill

**Tanggal**: 2026-07-14
**Status**: desain final, disetujui product owner — dokumen ini merangkum
keputusan untuk implementasi, bukan bahan brainstorming.

## Konteks

Paket ini (Tool 1, "otak" komposisi dalam arsitektur 2-tools) saat ini terdiri
dari 4 skill di root repo:

- `composition-gateway/` — router, entry point tunggal
- `jazz-idea-generator/` — brief → `composition-plan.json` terkunci
- `abc-notation-writer/` — plan → ABC tervalidasi
- `abc-to-midi-orchestration/` — ABC → MIDI multi-track siap-DAW

Empat masalah mendorong redesign:

1. **Skill panjang rawan membuat AI drift/halu.** Instruksi kritis
   tenggelam di tengah dokumen panjang, dan validator yang ada hanya
   memeriksa struktur — eval di `tests/` menemukan file yang lolos
   `validate_abc.py` tapi hasil render 0 not, kejadian ini terjadi **dua
   kali** secara independen (lihat
   `tests/results/2026-07-13-brief-01-02-armA-vs-armB.md`).
2. **Tidak installable rapi di tempat lain.** Struktur saat ini tidak punya
   satu folder `skills/` yang bisa langsung di-copy/symlink ke project lain.
3. **Progress generate tidak persisten.** Kalau sesi mati di tengah
   generate, posisi kerja hilang total — tidak ada catatan level mana yang
   sudah selesai.
4. **Tidak ada cara menilai output per tahap.** Penilaian saat ini hanya di
   akhir (rubrik `/64` di `quality-control.md`), sehingga tidak ketahuan di
   level mana bottleneck atau slop muncul.

## Keputusan desain

Semua poin di bawah sudah final dan disetujui product owner. SOP 14-level
lengkap sudah dipegang product owner dan akan disalin saat implementasi —
spec ini cukup merangkum strukturnya, bukan menuliskannya ulang kata per
kata.

### 1. Struktur folder installable

Semua skill pindah ke `skills/<nama>/SKILL.md`. Install ke project lain =
copy atau symlink folder `skills/` ke `.claude/skills/` project tersebut.
Tidak ada format plugin, tidak ada installer script — instalasi tetap
selevel operasi filesystem.

### 2. Main skill `skills/jazz-composition/`

Satu-satunya orchestrator. `composition-gateway/` **dihapus** — perannya
sebagai router diserap ke sini.

`SKILL.md` berisi:

- **SOP komposisi jazz 14-level**: Konsep artistik → Arsitektur lagu → Peta
  harmoni → Desain melodi → Ritme/groove → Aransemen instrumen →
  Comping/voicing → Bass line → Drum → Improvisasi → Interlude/shout/
  transisi → Intro/ending → Dinamika/dramaturgi → Detail low-level.
- **Workflow praktis 15 tahap** yang memetakan ke 14 level di atas (tahap
  operasional untuk menjalankan level-level tersebut secara berurutan).
- **CHECKLIST FINAL**: Konsep / Form / Harmoni / Melodi / Ritme / Aransemen /
  Improvisasi / Detail.

Detail panjang tiap level dipecah ke `references/level-XX-<nama>.md` dan
**hanya dibaca saat level itu sedang dikerjakan** — progressive disclosure,
supaya instruksi kritis tetap dekat titik eksekusi dan konteks model tidak
kebanjiran informasi yang belum relevan. Gate "ask, don't guess" dan konten
`RED-FLAGS.md` **diulang di titik level yang relevan** di setiap
`references/level-XX-*.md`, bukan hanya disebut sekali di preambul SKILL.md
— supaya tidak tenggelam di tengah dokumen panjang (masalah #1 di atas).

### 3. Modul detailing

Dipanggil oleh main skill per level; perannya pendalaman, bukan pipeline
berurutan seperti tiga skill lama:

| Modul | Cakupan |
|---|---|
| `harmony` | SOP level 3 (peta harmoni) + konten existing harmoni |
| `melody-design` | Level 4, tahap 1–6 (desain melodi dasar) |
| `advanced-melody` | Level 4, tahap 7–8: outside playing, side-slipping, enclosure, chromatic vocabulary |
| `vibes-mood` | Mood → parameter musikal, diadaptasi dari teori `compose-song` lama; menjaga orientasi genre-first neo-soul/chill-jazz |
| `groove-rhythm` | Level 5, 8, 9 (ritme/groove, bass line, drum) |
| `arrangement` | Level 6, 7, 10–13 (aransemen instrumen, comping/voicing, interlude/shout/transisi, intro/ending, dinamika/dramaturgi) |
| `abc-notation` | Eks `abc-notation-writer` — scripts & references dipindah utuh, termasuk `validate_abc.py` dan pelajaran multi-voice `[V:id]` |
| `midi-orchestration` | Eks `abc-to-midi-orchestration` — scripts dipindah utuh, termasuk `abc_to_midi.py` dan aturan "cek MIDI aktual, bukan cuma validator" |

Konten tiga skill lama (`jazz-idea-generator`, `abc-notation-writer`,
`abc-to-midi-orchestration`) dipecah masuk ke modul-modul di atas. Folder
lama **dihapus setelah** mapping eksplisit lama→baru memastikan tidak ada
file referensi yang jadi yatim (lihat bagian Verifikasi).

### 4. Run folder persisten

Setiap generate menghasilkan `runs/<tanggal>-<slug>/` berisi:

- `progress.md` — status per level (`done` / `in-progress` / `blocked`) +
  next action. Ini sumber resume kalau sesi mati di tengah jalan (mengatasi
  masalah #3).
- Artefak DoD per level, bernomor urut: `01-brief.md`, `02-form.md`,
  `03-harmony.md`, `04-melody.abc`, dst.
- Artefak final: `song.abc`, `drums.json`, `output.mid`.
- `scorecard.md` — hasil penilaian 3 lapis (lihat poin 6).

### 5. DoD per modul

Setiap `SKILL.md` modul mendeklarasikan:

- artefak output yang wajib dihasilkan,
- field wajib di artefak tersebut,
- kontrak konsistensi dengan artefak hulu.

Contoh: `03-harmony.md` wajib punya chord per bar untuk **semua** section
yang terdaftar di `02-form.md`, dengan bar count yang sama persis dengan
`02-form.md`.

Level berikutnya **tidak boleh mulai** tanpa artefak hulu yang memenuhi DoD
— ini gerbang anti-halu di titik handoff antar level, memperluas prinsip
"ask, don't guess" ke prinsip "verify artefak hulu sebelum lanjut".

### 6. Penilaian 3 lapis (semua level dinilai)

- **L1 — cek mekanis (script)**: bar count antar-artefak konsisten, MIDI
  notes-per-track > 0 untuk setiap voice, tempo/meter tag di MIDI cocok
  dengan header ABC, semua voice yang dideklarasikan benar-benar terisi.
- **L2 — rubrik per artefak**: 4–6 kriteria skala 0–2 per artefak, dinilai
  oleh **subagent reviewer segar tanpa konteks generasi** (self-grading
  dilarang — subagent yang menggenerate tidak boleh menilai hasilnya
  sendiri). Skor + alasan 1 kalimat, ditulis ke `scorecard.md`. Rubrik
  existing `quality-control.md` (`/64`) **dipecah per level** menjadi
  bagian-bagian rubrik L2 ini, bukan dihapus.
- **L3 — telinga manusia**: via `tests/human-ear-protocol.md`, hanya
  dijalankan di artefak final (`output.mid`), bukan per level.

Format `scorecard.md` seragam lintas run, supaya agregasi lintas-run bisa
menemukan (a) bottleneck — level yang skornya konsisten paling rendah lintas
banyak run, dan (b) rubrik bolong — level dengan skor L2 tinggi tapi
ternyata jelek di pengecekan telinga L3 (mengatasi masalah #4).

## Verifikasi

Implementasi dianggap selesai hanya setelah dua hal berikut terpenuhi:

1. **Mapping file lama→baru lengkap.** Setiap file di
   `jazz-idea-generator/references/`, `abc-notation-writer/references/` +
   `scripts/`, dan `abc-to-midi-orchestration/references/` + `scripts/`
   punya tujuan eksplisit di salah satu modul baru (`harmony`,
   `melody-design`, `advanced-melody`, `vibes-mood`, `groove-rhythm`,
   `arrangement`, `abc-notation`, `midi-orchestration`). Tidak ada file yang
   jadi yatim (tidak direferensikan dari `SKILL.md` manapun) sebelum folder
   lama dihapus.
2. **Dry-run 1 brief** dari `tests/briefs/` dijalankan lewat main skill baru
   (`skills/jazz-composition/`) dengan subagent segar (tanpa konteks
   pengembangan spec ini), dan dikonfirmasi:
   - `runs/<tanggal>-<slug>/` terbentuk,
   - `progress.md` terisi dan mencerminkan status level yang benar,
   - artefak DoD per level ada dan bernomor sesuai urutan,
   - `output.mid` ter-render dengan track count, notes-per-track, dan
     tempo/time-signature yang benar (dicek langsung dari file MIDI, bukan
     hanya exit status validator — sesuai `RED-FLAGS.md`),
   - `scorecard.md` terisi dengan hasil L1 dan L2 untuk setiap level yang
     dilalui.

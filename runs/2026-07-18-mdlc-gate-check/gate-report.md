# Gate Report — Dry-run 3-skill MDLC (Task 8)

Run folder: `runs/2026-07-18-mdlc-gate-check/`. Piece: **"Lampu Basah"**
(brief: hujan baru reda, jalan basah, lampu jalan menyala satu-satu —
tenang tapi tidak sedih, ~1 menit, rhodes+upright bass+brush drum,
tempo lambat).

## 0. Ketersediaan `pyengine`

**Tersedia.** `pyengine/.venv/bin/python -m pyengine --help` exit 0,
subcommands `validate, render, audition, release, gen-context`. Semua
langkah gate di bawah adalah eksekusi sungguhan, bukan simulasi manual.

## 1. Plan valid iterasi pertama?

**TIDAK.** Iterasi 1: 12 error (`chord_unparseable` ×6,
`degree_unavailable` ×6), semua berakar dari 1 root cause: simbol
`Cmaj9`/`Fmaj9` (quality "maj" + ext "9") lolos grammar whitelist
`_CHORD_GRAMMAR_RE` di `validator.py` tapi **ditolak** oleh
`music21.harmony.ChordSymbol` ("Invalid chord abbreviation 'maj9'").
Diperbaiki ke `Cmaj7add9`/`Fmaj7add9` (pitch set identik) → **iterasi 2
lolos, 0 error 0 warning.** Detail verbatim: `verify-log.md`.

Ini BUKAN kesalahan pemodelan musik (progresi/voice-leading tetap
sama) — ini kesalahan notasi yang **diajarkan oleh referensi skill
sendiri** (lihat Temuan #1 di bawah), jadi sinyalnya bukan "composer
perlu belajar teori lebih baik" tapi "knowledge base `jazz-composing`
punya bug faktual di notasi chord maj9".

## 2. Catatan uji dengar terisi?

**Terisi sejauh mungkin tanpa telinga manusia.** WAV render sungguhan
ada dan terverifikasi non-silent (`scorecard.md` §Audition + L2
global). L1 (mekanis) dan L2 (rubrik self-assessment, ditandai
eksplisit bukan reviewer segar) terisi penuh di `scorecard.md`. L3
(telinga manusia, wajib per-piece per `audition-protocol.md`) **belum
dijalankan** — dicatat sebagai status PENDING, bukan skor dikarang.

## 3. Ketiga SKILL.md bisa diikuti tanpa ambiguitas?

**Tidak sepenuhnya** — ditemukan ambiguitas/gap konkret, lihat daftar
Temuan di bawah. Yang **bisa** diikuti tanpa ambiguitas: struktur
Brief→Ideation→Plan (`jazz-composing`), loop validate→fix→re-run
(`plan-verifying`), perintah `pyengine audition` (`rendering-audition`).

## 4. Blocker konkret untuk kriteria yang butuh `pyengine` sungguhan

Tidak ada — `pyengine` tersedia penuh, `validate` dan `audition`
berjalan sungguhan sampai WAV. Satu-satunya kriteria yang benar-benar
tak bisa dipenuhi solo-agent adalah L3 (telinga manusia) dan L2 dgn
reviewer segar terpisah — itu bukan blocker `pyengine`, melainkan
keterbatasan struktural dry-run 1-agent (lihat Temuan #4).

---

## Daftar Temuan Gate

### Temuan #1 — SEVERITY: TINGGI. `harmony.md` mengajarkan notasi chord yang ditolak validator

`skills/jazz-composing/references/harmony.md` baris 61 dan 155 memakai
`Cmaj9`/`Dm11`/`Fmaj9` sebagai **contoh simbol chord yang benar** untuk
ditulis di `plan.json` (baris 155 eksplisit: "simbol chord (`Fmaj9`,
`Dm7b5`, `C7#9`, …)"). Faktanya `Xmaj9` (quality "maj" + ekstensi "9")
**ditolak** oleh `music21.ChordSymbol` yang dipakai validator
(`Invalid chord abbreviation 'maj9'`) — dikonfirmasi langsung lewat
`pyengine/.venv/bin/python -c "from music21 import harmony; harmony.ChordSymbol('Fmaj9')"`.
`plan-verifying/references/common-errors.md` baris 14 memperparah:
baris itu **merekomendasikan** `Fmaj9` sebagai contoh "simbol standar"
untuk memperbaiki error `chord_unparseable` — padahal `Fmaj9` itu
sendiri adalah salah satu penyebab paling umum error itu. Fix yang
benar (dikonfirmasi manual): `Xmaj7add9` (mis. `Cmaj7add9`) — pitch set
identik (root-3-5-7-9), lolos grammar **dan** music21. Rekomendasi:
perbaiki `harmony.md` §contoh simbol dan `common-errors.md` baris 14 di
sesi berikutnya (di luar mandat task ini untuk menambal).

### Temuan #2 — SEVERITY: TINGGI. Grammar whitelist validator lebih ketat dari music21 secara tidak konsisten

`_CHORD_GRAMMAR_RE` di `pyengine/pyengine/validator.py` menerima
`Cmaj9` (yang lalu ditolak music21) TAPI **menolak** `CM9`/`FM9` (yang
justru **diterima** music21 dan menghasilkan pitch set major-9 yang
benar) — karena regex quality group `(?:maj|min|m|dim|aug|sus2|sus4)?`
tidak memasukkan `M` (case-sensitive, huruf besar). Akibatnya **tidak
ada** cara menulis simbol major-9 murni (`XM9`) yang lolos kedua
lapis; satu-satunya jalan lolos adalah bentuk `Xmaj7add9` yang lebih
verbose dan tidak disebut di manapun sebagai konvensi di
`harmony.md`/`contract.md`. Ini bug di `pyengine` sendiri (grammar
vs. parser tidak sinkron), bukan hanya dokumentasi — di luar mandat
task ini untuk ditambal (aturan main: "jangan mengubah skill/engine
apa pun"), tapi harus dilaporkan balik ke pemilik `pyengine`.

### Temuan #3 — SEVERITY: SEDANG. Kontrak "11-field" untuk artefak level utama tidak pernah didefinisikan

`candidate-selection-protocol.md` baris 26 dan `run-folder-protocol.md`
baris 44 sama-sama menyebut "kontrak 11-field penuh" untuk artefak
`02-konsep.md`/`03-bentuk.md`/`04-harmoni.md`/`05-melodi.md` (dibedakan
eksplisit dari kontrak 7-field `*-candidates.md`) — tapi field itu
**tidak didefinisikan di manapun** dalam skill package (dicek:
`candidate-selection-protocol.md`, `run-folder-protocol.md`,
`harmony.md`, `melody.md`, `structure.md`, `arrangement.md` — tidak
ada satu pun tabel 11-field). Fresh agent (saya) harus **mengimprovisasi**
sendiri 11 field (Level, Aesthetic thesis, Immutable constraints,
Assumptions, Decision, Rationale, Alternatives, Interaction with other
levels, Risks, Confidence, Next action) — dicatat eksplisit di tiap
artefak yang memakainya (`02-konsep.md` dst). Rekomendasi: definisikan
kontrak 11-field itu secara eksplisit (atau hapus rujukan "11-field"
kalau memang dimaksud bebas format).

### Temuan #4 — SEVERITY: SEDANG. Protokol L2/L3 mengasumsikan ≥2 agent/manusia, tidak menyediakan fallback solo-agent

`scorecard-template.md` dan `rubric-checklist.md` eksplisit melarang
self-grading ("diisi subagent reviewer segar tanpa konteks generasi")
dan `audition-protocol.md` mewajibkan L3 telinga manusia sungguhan per-
piece — **tidak seperti** Level 1-4 Ideation di `jazz-composing` yang
punya fallback eksplisit ("self-selection diizinkan, wajib pre-mortem",
`candidate-selection-protocol.md` §5), fase Review di
`rendering-audition` **tidak punya fallback** setara untuk kasus solo-
agent (mis. dry-run gate ini, atau composer pack di AI browser tanpa
Claude Code/subagent). Konsekuensi konkret di gate ini: L2-rubrik
terpaksa diisi self-assessment (ditandai jujur di `scorecard.md`),
L2-blind (uji buta arc) di-skip total, L3 pending. Rekomendasi:
`rendering-audition` perlu pola fallback yang sama seperti
`candidate-selection-protocol.md` §5 untuk L2, dan definisi eksplisit
"apa yang boleh diklaim selesai tanpa L3" untuk konteks non-produksi
(dry-run/gate/eksperimen) vs. piece produksi (L3 wajib, tanpa
pengecualian).

### Temuan #5 — SEVERITY: RENDAH. `durationSec` output `pyengine audition` berpotensi disalahartikan

Sudah didokumentasikan dgn benar di `rendering-audition/SKILL.md` dan
`audition-protocol.md` ("durationSec adalah wall-clock waktu render,
bukan durasi lagu") — tapi field JSON bernama `durationSec` tanpa
konteks di sisi output (`{"midi":...,"wav":...,"durationSec":2.34}`)
sangat mengundang salah baca sebagai "lagu ini 2.34 detik" oleh agent
yang tidak membaca dokumentasi teks itu lebih dulu (di gate ini saya
sempat perlu verifikasi silang manual lewat `wave` module Python utk
memastikan durasi lagu sebenarnya 61.78s). Rekomendasi kosmetik:
rename field ke `renderWallClockSec` atau tambahkan field kedua
`songDurationSec` di output CLI.

---

### Temuan #6 — SEVERITY: RENDAH. `.gitignore` repo tidak menutupi path audio baru

`.gitignore` (`music-composition-skill/.gitignore`) hanya punya pola
`runs/*/render.wav` — dari konvensi run folder LAMA (audio ditulis
langsung di root run folder). Konvensi BARU dari `run-folder-protocol.md`
menulis audio ke `<run-folder>/audition/<slug>.wav` +
`<run-folder>/audition/<slug>.mid` (subfolder, nama file dari slug
judul, bukan `render.wav` literal) — pola lama tidak match sama sekali
(`git check-ignore` dikonfirmasi tidak menandai file ini sebagai
ignored). Akibatnya `git add runs/2026-07-18-mdlc-gate-check/` di
commit gate ini menyertakan WAV asli 10.4 MB ke git history (bukan
disengaja dihindari — mengikuti aturan main task ini "kalau WAV/MID
di-ignore jangan paksa commit, kalau tidak, lanjut apa adanya").
Rekomendasi: perbarui `.gitignore` ke pola `runs/*/audition/*.wav` +
`runs/*/audition/*.mid` (dan `runs/*/release/*.wav` bila fase Release
dipakai) supaya konsisten dengan konvensi baru.

## Ringkasan metrik vs. PRD §8

| Metrik | Target | Hasil dry-run ini |
|---|---|---|
| Validitas plan iterasi pertama | ≥80% | **GAGAL** iterasi 1 (n=1, tidak bisa klaim rate statistik dari 1 sample, tapi kegagalan sistemik — lihat Temuan #1/#2) |
| Validitas setelah ≤2 iterasi | ≥95% | **LOLOS** (iterasi ke-2 bersih) |
| Determinisme render | 100% | Tidak diuji di gate ini (butuh 2× render dibandingkan; di luar cakupan Task 8) |
| Uji dengar WAV | lolos 3/4 | **PENDING** — L3 manusia belum dijalankan |

## Kesimpulan

Dry-run mencapai titik akhir yang diminta (Audition + Review
sejauh mungkin tanpa telinga manusia), tanpa blocker `pyengine`. Alur
3-skill **bisa** diikuti end-to-end oleh fresh agent, TAPI dengan 2
temuan tingkat tinggi (notasi chord yang salah diajarkan + inkonsistensi
grammar/parser) yang menyebabkan kegagalan iterasi-pertama yang bukan
kesalahan composer, dan 1 gap struktural (kontrak 11-field hilang) yang
memaksa improvisasi. Rekomendasi ke pemilik repo: **jangan merge sampai
Temuan #1 dan #2 diperbaiki** (risiko tinggi — bug ini akan berulang di
setiap piece yang butuh warna maj9, chord ekstensi paling umum di
neo-soul/ballad), Temuan #3/#4 sebaiknya diperbaiki tapi tidak
memblokir merge.

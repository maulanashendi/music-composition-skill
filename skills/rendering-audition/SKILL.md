---
name: rendering-audition
description: Render a validated plan.json to MIDI+WAV (pyengine audition/release), run the human-ear audition protocol, score it against the rubric checklist, and release/archive the final WAV + plan.json as the song's source code. Use whenever a plan.json has passed plan-verifying and needs to become audible, whenever someone asks to render, audition, listen to, review, or release a composition, or whenever a piece needs archiving after passing ear-check. This is fase Audition, Review, Release, dan Remix dari MDLC — it does not change musical intent or fix validation errors (that's jazz-composing/plan-verifying's job); it turns a decided, valid plan into produced audio and judges whether that audio is actually enjoyable.
---

# Rendering & Audition — fase Audition, Review, Release, Remix

Input skill ini SELALU `plan.json` yang sudah lolos `plan-verifying`
(tanpa error). Kalau `plan.json` belum divalidasi, kembalikan ke
`../plan-verifying/SKILL.md` dulu — skill ini tidak menjalankan
`pyengine validate` sendiri dan tidak memperbaiki isi plan.

## Workflow

### Fase Audition — render draft dan dengarkan

**Kalau `python -m pyengine` ada** (jalur CLI/dev):

```bash
python -m pyengine audition <path/to/plan.json> -o <run-folder>/audition/
```

**Kalau tidak** (jalur chat Studio, container gateway Node-only — lihat
`references/engine-http-alternative.md` Jalur A): panggil `POST
http://backend:8000/compose?audio=true` dan decode base64 `midi`/`wav` ke
file, persis seperti dicontohkan di referensi itu — hasil akhirnya SAMA:
`<slug>.mid` + `<slug>.wav` di `<run-folder>/audition/`.

Kedua cara menghasilkan `<slug>.mid` + `<slug>.wav` sekali jalan (slug dari
`meta.title` tersanitasi `[a-z0-9-]`, fallback `untitled`), plus metadata
`{"midi","wav","durationSec"}` — `durationSec` adalah wall-clock waktu
render, **bukan** durasi lagu. MIDI-nya byte-identik dan diuji sebagai
kontrak (`meta.seed` men-drive humanization, bukan random tiap render);
WAV-nya deterministik **secara musikal** (konten/notasi sama persis) tapi
byte-identik **tidak** dijamin kontrak — `fluidsynth`/`ffmpeg` tidak
menjamin bit-reproducibility lintas environment.

### Fase Import — masukkan ke Studio DAW (hanya jalur chat Studio)

Kalau skill ini dipicu dari chat panel Studio (project name = nama folder
cwd, sama seperti dicek di `jazz-composing` Fase 0), setelah `<slug>.mid`
berhasil ditulis, jalankan:

```bash
daw song import --project "$(basename "$PWD")" --file <run-folder>/audition/<slug>.mid
```

Ini membaca `<slug>.mid` (multi-track SMF, satu track per voice plan),
memetakan tiap track ke instrument preset Studio (via GM program), dan
menambahkannya sebagai track+clip BARU ke `project.json` project ini —
**satu** `PUT` ber-`If-Match` (satu docVersion bump, satu undo-step di
Studio). Studio yang sedang terbuka akan menerima update ini **otomatis**
lewat WebSocket (realtime docVersion sync) tanpa reload — hasil komposisi
langsung terlihat di piano-roll dalam beberapa detik.

Perlakukan **playback di Studio** sebagai bagian dari protokol uji dengar
3 lapis (`references/audition-protocol.md`), bukan cuma file WAV
terpisah: (1) automated gate — sudah diselesaikan `plan-verifying`; (2)
LLM-judge blind pairwise — subagent segar tanpa konteks generasi menilai;
(3) **human ear, blind A/B — wajib per-piece produksi**, bukan sampel,
sebelum piece disebut selesai — user sekarang bisa melakukan ini langsung
dari Studio.

> **Batas yang sudah ada sebelumnya, bukan regresi baru**: playback di
> Studio memakai synth TS in-browser sendiri (`packages/engine/
> renderProject.ts`), BUKAN reproduksi fluidsynth+mastering byte-identik
> dari `.wav` hasil render di atas. Jadi telinga di Studio menilai NOTASI
> (pitch/timing/artikulasi/pemilihan instrument), bukan warna sonic
> finalnya — `.wav` hasil Fase Audition tetap sumber kebenaran untuk itu.
> Ini gap konvergensi playback-vs-render yang sudah tercatat di
> `daw_generative/CLAUDE.md` §2 (north-star), di luar tanggung jawab
> skill ini untuk menutup.
>
> Kalau `daw` tidak reachable (bukan chat Studio, mis. dijalankan CLI
> dev-only tanpa Studio project) — lewati Fase Import ini, `<slug>.mid`/
> `.wav` di run folder tetap artefak yang sah untuk fase Review/Release
> di bawah.

### Fase Review — skor dan revisi

Isi `references/scorecard-template.md` ke `scorecard.md` di run folder:
status validasi (dari `verify-log.md`), skor L2 rubrik (pakai
`references/rubric-checklist.md`), catatan L3 telinga. Kalau ada temuan
yang menuntut revisi niat musikal (bukan sekadar render ulang) — kembali
ke `../jazz-composing/SKILL.md` fase Plan, bukan ditambal di sini.

**Kaidah knowledge base baru HANYA masuk dari temuan di fase ini.** Kalau
uji dengar menemukan pola gagal berulang, tambahkan entri ke
`../jazz-composing/references/cliche-register.md` (kalau soal cliché) atau
`../jazz-composing/references/vibe-technique-map.md` (kalau soal
mood→teknik) — jangan menambah aturan teori generik yang tidak berasal
dari piece nyata yang barusan dinilai.

### Fase Release — render final dan arsipkan

**Kalau `python -m pyengine` ada**:

```bash
python -m pyengine release <path/to/plan.json> -o <run-folder>/release/
```

**Kalau tidak** (jalur chat Studio): `pyengine release` = `pyengine
audition` + salin `plan.json` — tidak ada endpoint HTTP terpisah untuk
ini, jadi lakukan dua langkahnya manual: panggil ulang `POST
http://backend:8000/compose?audio=true` (sama seperti Fase Audition,
decode ke `<run-folder>/release/<slug>.{mid,wav}`), lalu `cp
<path/to/plan.json> <run-folder>/release/plan.json`.

Render final + penamaan + arsip (salinan `plan.json` ikut diarsipkan di
folder yang sama). **`plan.json` adalah source code lagu** — WAV tidak
pernah "hilang" dalam bentuk audio saja; selalu bisa dibangun ulang, diubah
key-nya, diganti soundfont-nya dari `plan.json` yang diarsipkan di run
folder.

### Fase Remix

`plan.json` yang terarsip adalah titik awal fork/variasi — salin run
folder, ubah field niat yang diinginkan (chord, gaya, seed baru),
jalankan ulang lewat `../plan-verifying/` → skill ini.

## Alternatif HTTP

Kalau tidak ada akses CLI `pyengine` (mis. chat-lane Studio), baca
`references/engine-http-alternative.md` — dua jalur HTTP berbeda
(FastAPI `compose`, DEFAULT untuk chat Studio; Vite dev-render, dev lokal
lama) sebagai padanan `pyengine audition`/`pyengine validate`.

## Jalur legacy (ABC)

Kalau artefak di tangan adalah ABC (bukan `plan.json` — mis. dari
`../abc-notation/SKILL.md`, jalur 2 yang masih didukung engine JS lama),
render/audition-nya **tidak** lewat `pyengine`, dan **tidak** lewat
FastAPI `compose` (modul itu cuma menerima `plan.json`) — hanya lewat
Jalur B (Vite dev-render): `POST /api/render` body `{abc, drums?,
mastering?}` (lihat `references/engine-http-alternative.md` Jalur B
§Jalur legacy ABC). Jangan mencampur `plan.json` dan ABC dalam satu run.

## References

- `references/audition-protocol.md` — protokol uji dengar 3 lapis, kriteria kelulusan per vibe, L3 wajib per-piece.
- `references/scorecard-template.md` — template `scorecard.md`, status validasi dari `verify-log.md` + skor L2 + catatan L3.
- `references/rubric-checklist.md` — rubrik kualitatif konsolidasi (voice-leading, interaksi ensemble, dinamika, timbre) — menggantikan 8 `rubric.md` modul lama.
- `references/engine-http-alternative.md` — kontrak HTTP FastAPI `compose` (default chat Studio) dan Vite dev-render sebagai alternatif CLI, plus jalur legacy ABC.
- `../RED-FLAGS.md` — pola kegagalan umum lintas skill.

## Metrik yang relevan (dari `docs/new-prd.md` §8)

- Uji dengar WAV ("terdengar jazz manusiawi, bukan robot") lolos 3 dari 4 render.
- Determinisme render: MIDI byte-identik (plan sama → MIDI sama) 100% —
  dijamin & diuji kontrak; WAV deterministik secara musikal (konten sama)
  tapi byte-identik lintas environment tidak dijamin kontrak.
- Warning linter yang ditindaklanjuti (bukan diabaikan) — mayoritas.

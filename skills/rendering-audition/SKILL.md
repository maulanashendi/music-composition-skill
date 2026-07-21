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

```bash
python -m pyengine audition <path/to/plan.json> -o <run-folder>/audition/
```

Menghasilkan `<slug>.mid` + `<slug>.wav` sekali jalan (slug dari
`meta.title` tersanitasi `[a-z0-9-]`, fallback `untitled`), plus stdout JSON
`{"midi","wav","durationSec"}` — `durationSec` adalah wall-clock waktu
render, **bukan** durasi lagu. `-o <outdir>` **wajib** per kontrak
`pyengine` (argumen required, bukan opsional). MIDI-nya byte-identik dan
diuji sebagai kontrak (`meta.seed` men-drive humanization, bukan random
tiap render); WAV-nya deterministik **secara musikal** (konten/notasi sama
persis) tapi byte-identik **tidak** dijamin kontrak — `fluidsynth`/`ffmpeg`
tidak menjamin bit-reproducibility lintas environment. Jalankan protokol
uji dengar 3 lapis di `references/audition-protocol.md`: (1) automated gate
— sudah diselesaikan `plan-verifying`; (2) LLM-judge blind pairwise —
subagent segar tanpa konteks generasi menilai; (3) **human ear, blind
A/B — wajib per-piece produksi**, bukan sampel, sebelum piece disebut
selesai.

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

```bash
python -m pyengine release <path/to/plan.json> -o <run-folder>/release/
```

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

Kalau agent memakai server `daw_generative` alih-alih CLI `pyengine`
langsung, baca `references/engine-http-alternative.md` — `POST
/api/render` (body `plan.json`) dan `POST /api/validate` sebagai
padanan `pyengine audition`/`pyengine validate` lewat HTTP.

## Jalur legacy (ABC)

Kalau artefak di tangan adalah ABC (bukan `plan.json` — mis. dari
`../abc-notation/SKILL.md`, jalur 2 yang masih didukung engine JS lama),
render/audition-nya **tidak** lewat `pyengine`; ikuti jalur lama:
`POST /api/render` body `{abc, drums?, mastering?}` (lihat
`references/engine-http-alternative.md` §Jalur legacy ABC). Jangan
mencampur `plan.json` dan ABC dalam satu run.

## References

- `references/audition-protocol.md` — protokol uji dengar 3 lapis, kriteria kelulusan per vibe, L3 wajib per-piece.
- `references/scorecard-template.md` — template `scorecard.md`, status validasi dari `verify-log.md` + skor L2 + catatan L3.
- `references/rubric-checklist.md` — rubrik kualitatif konsolidasi (voice-leading, interaksi ensemble, dinamika, timbre) — menggantikan 8 `rubric.md` modul lama.
- `references/engine-http-alternative.md` — kontrak HTTP `POST /api/render`/`POST /api/validate` sebagai alternatif CLI, plus jalur legacy ABC.
- `../RED-FLAGS.md` — pola kegagalan umum lintas skill.

## Metrik yang relevan (dari `docs/new-prd.md` §8)

- Uji dengar WAV ("terdengar jazz manusiawi, bukan robot") lolos 3 dari 4 render.
- Determinisme render: MIDI byte-identik (plan sama → MIDI sama) 100% —
  dijamin & diuji kontrak; WAV deterministik secara musikal (konten sama)
  tapi byte-identik lintas environment tidak dijamin kontrak.
- Warning linter yang ditindaklanjuti (bukan diabaikan) — mayoritas.

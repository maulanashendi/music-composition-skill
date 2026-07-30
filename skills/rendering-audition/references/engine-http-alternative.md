# Alternatif HTTP: dua jalur berbeda, jangan tertukar

Referensi untuk agent yang tidak punya akses shell ke `pyengine` (CLI)
tapi bisa mengirim request HTTP. Ada **dua** server HTTP yang mengekspos
`pyengine` — pilih sesuai environment kamu, jangan asumsikan satu-satunya:

| | **FastAPI `compose`** (jalur chat Studio) | **Vite dev-render** (dev lokal lama) |
|---|---|---|
| Base URL | `http://backend:8000` (nama service Docker Compose) atau `$STUDIO_SERVER_URL` | `http://localhost:<port auto-increment>` dari `npm run dev` di root `daw_generative` |
| Kapan dipakai | Chat panel Studio (container `agent-chat-gateway`, TIDAK punya Python) — lihat `docs/chat-feature-architecture.md` §7 di repo `daw_generative` | Dev manual di luar Docker, jarang dipakai lintas-agent |
| Endpoint validate | `POST /compose/validate` | `POST /api/validate` |
| Endpoint render | `POST /compose` (`?audio=true` utk WAV) | `POST /api/render` |
| Bentuk respons render sukses | JSON: `{"midi":"<base64>","warnings":[...]}`, tambah `"wav":"<base64>","durationSec":<float>` kalau `?audio=true` | Binary `audio/wav` + header `X-Plan-Warnings` |

**Default-kan ke jalur FastAPI `compose`** kalau kamu tidak yakin sedang
di environment mana — itu satu-satunya yang terjamin hidup di topologi
Docker tempat chat-lane jalan. Jalur Vite dev-render di bawah cuma
relevan kalau eksplisit diberitahu sedang jalan di dev lokal non-Docker.

## Jalur A — FastAPI `compose` (chat Studio, DEFAULT)

```bash
# Verify (padanan `pyengine validate`)
curl -sX POST http://backend:8000/compose/validate \
  -H 'Content-Type: application/json' -d @<plan.json>
# -> selalu 200, {"valid": bool, "errors":[...], "warnings":[...]}

# Audition (padanan `pyengine audition`)
curl -sX POST 'http://backend:8000/compose?audio=true' \
  -H 'Content-Type: application/json' -d @<plan.json> > response.json
# -> 200: {"midi":"<base64>","warnings":[...],"wav":"<base64>","durationSec":<float>}
# -> 422 (belum lolos validate): {"error":"komposisi ditolak validasi","errors":[...],"warnings":[...]}
# -> 503: tool audio (fluidsynth/ffmpeg/soundfont) tak tersedia di backend

python3 -c "
import json, base64, sys
r = json.load(open('response.json'))
open('<run-folder>/audition/<slug>.mid', 'wb').write(base64.b64decode(r['midi']))
if 'wav' in r:
    open('<run-folder>/audition/<slug>.wav', 'wb').write(base64.b64decode(r['wav']))
"
```

Kalau `$STUDIO_SERVER_URL` sudah di-set di environment (dipasang lewat
`docker-compose.yml` untuk container gateway), pakai itu alih-alih
hardcode `http://backend:8000`.

## Jalur B — Vite dev-render (dev lokal lama, BUKAN default)

Server dev `daw_generative` (Vite dev middleware —
`vite-plugin-render.js` via `vite.config.js` — dev-only, bukan production
server, dan bukan yang dipakai chat-lane).

**Prasyarat**: `npm run dev` dijalankan dari root repo `daw_generative`.
Port default Vite 5173 tapi **auto-increment** bila terpakai — baca port
sesungguhnya dari log terminal, jangan mengasumsikan 5173.

## Kontrak respons HTTP (Jalur B)

| Endpoint | Kondisi | Status | Body/Header |
|---|---|---|---|
| `POST /api/render` (body `plan.json` schemaVersion 2) | valid | 200 | `audio/wav` + header `X-Plan-Warnings` (JSON array, non-ASCII di-escape `\uXXXX` — parse dengan `JSON.parse`) |
| | invalid | 422 | `{valid:false, errors:[{path,code,message}], warnings:[...]}` apa adanya |
| | `schemaVersion` ada tapi ≠ angka 2 (mis. string `"2"`, angka `3`) | 400 | `{error, message}` — `schemaVersion` harus `number` `2` |
| | error internal engine | 500 | `{ok:false, error}` |
| | body > 1 MB | 413 | `{error, limit}` |
| `POST /api/validate` (body `plan.json`) | valid ATAU invalid | selalu 200 | `{valid, errors, warnings}` (laporan, bukan gate) |

Catatan: `POST /api/validate` **selalu** 200 — ini laporan (padanan `pyengine
validate` fase Verify), bukan gerbang yang menolak request. Yang membedakan
lolos/tidak adalah isi `valid` di body, bukan status HTTP.

## `POST /api/render` — jalur plan.json (utama)

Body = `plan.json` schemaVersion 2 mentah (objek JSON, bukan string ABC),
sama persis dengan file yang dikonsumsi `pyengine audition`. Sukses (200)
mengembalikan **binary WAV** (`content-type: audio/wav`) plus header
`X-Plan-Warnings` — array JSON warning (sama isi dengan field `warnings`
`pyengine validate`), non-ASCII di dalamnya di-escape `\uXXXX` sesuai
serialisasi header HTTP, jadi parse dengan `JSON.parse` setelah didapat,
jangan dibaca sebagai string mentah. Simpan body ke `<run-folder>/audition/`
atau `<run-folder>/release/` sesuai fase yang sedang dijalankan.

`POST /api/validate` menerima body `plan.json` yang sama dan mengembalikan
`{valid, errors, warnings}` tanpa merender apa pun — padanan HTTP untuk
`pyengine validate` di fase Verify, dipakai kalau agent ingin memeriksa
tanpa membakar biaya render.

## Jalur legacy ABC (catatan terpisah, bukan jalur utama)

Kalau artefak di tangan adalah ABC (bukan `plan.json` — dari
`../abc-notation/SKILL.md`, jalur 2 yang masih didukung engine JS lama),
`POST /api/render` juga menerima body **`{abc, drums?, mastering?}`** (bukan
`plan.json`) sebagai jalur kompatibilitas lama:

- `abc` — string ABC lengkap (multi-voice).
- `drums` — opsional, skema step-grid ENGINE: `{steps_per_bar: 8|12|16,
  gm_map: {voice: <35..81>}, base_velocity: {voice: <1..127>}, swing?:
  <0.5..0.75>, sections: [{bars: <int>=1>, pattern: {voice: "x.Xg..."}}]}`.
  Karakter pola: `x` (hit normal), `X` (aksen, base_velocity **+12** cap
  127), `g` (ghost, velocity **35 tetap**), `.` (off).
- `mastering` — `'neo-soul'` (default bila field absen), `'legacy'`, atau
  `false`. Boolean `true` **DITOLAK** (422).
- Total bar `drums` **WAJIB sama** dengan jumlah bar ABC — mismatch → 422
  `{error, abcBars, gridBars}`.
- `%%pocket` — hanya id `neo-soul-core` valid, harus muncul sebelum voice
  pertama aktif di ABC (kemunculan setelah diabaikan diam-diam).
- Sukses: 200, binary WAV + header `X-Conformance-Summary` (ringkasan bar/
  not/track/velocity-std/pct-on-grid/pocket, non-gating — nilai apa pun
  tetap 200).

Jangan mencampur `plan.json` dan ABC dalam satu run — pilih satu jalur
sesuai artefak yang benar-benar dipegang.

## Batasan umum

- Body dibatasi **1 MB** untuk kedua jalur — lebih besar → 413.
- Batas keras render: `maxBars` 512, `maxNotes` 50.000, `maxVoices` 16, BPM
  20-400, durasi maksimum 900 detik (15 menit).
- **Soundfont GM `FluidR3_GM.sf2` tidak auto-download**; dicek berurutan:
  env `NEO_SOUL_SOUNDFONT`, cache
  `~/.cache/hermes-neo-soul-soundfonts/fluidr3/usr/share/sounds/sf2/FluidR3_GM.sf2`,
  path sistem `/usr/share/sounds/sf2/FluidR3_GM.sf2`. Tak satu pun ada →
  status Audition **PENDING**, dicatat di `scorecard.md`, bukan dipaksakan
  gagal diam-diam.
- `fluidsynth` auto-bootstrap (unduh `.deb` via `apt-get download`) bila
  absen dari PATH/cache.
- `ffmpeg` wajib ada di PATH bila `mastering` bukan `false` (default
  `'neo-soul'`, jadi ffmpeg wajib di jalur default).
- 500 pada render biasanya berarti kegagalan runtime (soundfont tak
  ketemu, fluidsynth/ffmpeg gagal/timeout — fluidsynth 120 detik, ffmpeg 60
  detik — atau hasil render silent yang ditangkap pemeriksaan audibilitas).

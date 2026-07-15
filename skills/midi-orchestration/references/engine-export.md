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

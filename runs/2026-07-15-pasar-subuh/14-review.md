# 14-review.md — Level 14: Revisi Low Level

## Verifikasi mekanis (L1)
- `validate_abc.py song.abc` → **OK: 0 errors, 0 warning(s)**.
- `abc_to_midi.py` → 3 track (Tenor Sax 16 notes max-poly **1**, Rhodes 45
  notes max-poly 4, Finger Bass 51 notes max-poly 1) — mono-lead sax
  terkonfirmasi (Fix 2), tidak ada drone (durasi not wajar, tanpa chord
  symbol yang ikut ter-render sebagai not — Fix 1 aktif otomatis di
  `abc_to_midi.py`).
- `grid_to_midi.py 09-drums.json` → 207 hits di 24 bar, **tanpa WARNING**
  anti-tile (hierarchy base+variation+transition per section >2 bar
  terpenuhi).
- Merge `output.mid` (4 track): Sax/Rhodes/Bass berakhir tepat di
  75.789 detik (= 24 bar × 4 beat × 60/76 detik — matematis pas), Drums
  berakhir 72.811 detik (selisih ~3 detik < 1 bar, wajar — bar drum
  terakhir memang meredup ke sunyi, bukan desync). Tempo terbaca **76
  BPM**, time signature **4/4** — cocok `Q:1/4=76` dan `M:4/4` di ABC.

## Bukti revisi (≥1 pasangan before/after, 2 masalah terbesar)

### Revisi 1 — label teori vs fakta notasi (Level 4, ditemukan gate cek-fakta)
**Temuan (sumber: gate cek-fakta Level 4)**: draf awal `04-melody.abc`
mengklaim nada Ab di bar 19 (micro-apex) sebagai **"nada outside (kromatik,
bukan bagian skala D Dorian)"**. Setelah `notation_facts.py` dijalankan
pada fragmen bar 19, script melaporkan Ab sebagai **`chord-tone`** (karena
b9 memang bagian eksplisit simbol chord `G7b9#5` itu sendiri).
- **Before**: "Fakta objektif: Ab (`_A`) adalah nada outside (kromatik,
  bukan bagian skala D Dorian) — b9 dari G7alt."
- **After**: "Ab dilaporkan `chord-tone`, BUKAN 'outside' ... Ketegangan
  bar ini datang dari **level chord** (chord `G7b9#5` dilaporkan
  `chord-vs-key=borrowed`), bukan level nada."
- **Efek yang diharapkan terdengar**: deskripsi yang benar mengarahkan
  performer/pendengar untuk memahami tension bar 19 datang dari *pemilihan
  chord* yang jauh dari tonal center (chromatic departure), bukan dari
  nada yang "salah" di atas chord biasa — micro-apex tetap terdengar sama
  persis, tapi label desain sekarang tidak menyesatkan revisi berikutnya.

### Revisi 2 — voicing comping tidak mencapai top-note yang diklaim (Level 7)
**Temuan (sumber: gate cek-fakta Level 7)**: draf pertama voicing Rhodes
untuk Em7 (bar 18) ditulis `[G,BD]` dengan asumsi top-note = D (mengikuti
urutan ketik G→B→D). `notation_facts.py` melaporkan **top-note = B**, bukan
D — karena D tanpa modifier oktaf jatuh di register yang sama dengan B
(bukan satu oktaf di atas B seperti yang diasumsikan dari urutan
alfabet/ketik).
- **Before**: `"Em7" [G,BD]4` → fakta: top-note **B** (bukan D yang
  dimaksud), sehingga klaim voice-leading "top note bergerak
  A→F→D→E" (rencana awal) **tidak match** fakta script.
- **After**: `"Em7" [G,DB]4` (dan voicing G7/Dm6add9 disusun ulang senada:
  `[G,DB]`/`[FAB]`) → fakta terkonfirmasi top-note **A → B → B → B**
  (bar 16→17→18→24), dengan B(17)↔B(18) common-tone statis (G7 dan Em7
  berbagi G,B,D) dan callback B muncul lagi di chord akhir bar 24.
- **Efek yang diharapkan terdengar**: top-line comping sekarang benar-benar
  diam/stabil tepat di titik call-response (bar 17-18), memberi kesan
  "menahan nada yang sama" yang mendukung dialog sax-Rhodes, dan callback
  B di bar 24 memperkuat rekontekstualisasi secara terdengar di comping,
  bukan hanya di bass/melodi.

Kedua revisi terhubung langsung ke gate cek-fakta Level 4/7 (bukan revisi
kosmetik berdiri sendiri) — memenuhi syarat Tahap 15/`scorecard-template.md`.

### Revisi 3 — nama voice bass tidak match keyword lokal `abc_to_midi.py` (ditemukan reviewer L2 segar Level 14)
**Temuan**: reviewer L2 segar independen menjalankan ulang
`abc_to_midi.py`/`pretty_midi` dan menemukan `output.mid` merender track
bass dengan **GM program 32** (Acoustic Bass), padahal ABC eksplisit
menulis `%%MIDI program 3 33` (Finger Bass, sesuai registry). Akar
masalah: `abc_to_midi.py` **mengabaikan** `%%MIDI program` dan menentukan
program dari keyword substring pada **nama voice** (`PROGRAM` dict) — nama
`"Finger Bass"` tidak mengandung substring `"bass-finger"` (urutan kata
beda, tanpa hyphen), jatuh ke keyword generik `"bass"` (32).
- **Before**: `V:3 name="Finger Bass" clef=bass` → preview lokal `output.mid` program **32**.
- **After**: `V:3 name="Bass-Finger" clef=bass` → preview lokal `output.mid` program **33**, cocok `%%MIDI program 3 33`.
- **Efek yang diharapkan terdengar**: preview MIDI lokal (Tool 1) sekarang
  bertimbre sama dengan WAV render engine (Tool 2) yang membaca
  `%%MIDI program` langsung — menghilangkan potensi diskrepansi timbre
  antara preview dan produksi akhir (`engine-export.md` §"Gotcha penentuan
  timbre").

Diverifikasi ulang setelah perbaikan: `validate_abc.py` tetap `OK: 0
errors, 0 warning(s)`; `output.mid` tetap 4 track (Tenor Sax 16 not,
Rhodes 45 not, Bass-Finger 51 not program **33**, Drums 207 hits program
drum) — tidak ada regresi pada jumlah not/track lain.

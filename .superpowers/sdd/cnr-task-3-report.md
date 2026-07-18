# CnR Task 3 — bukti eksekusi end-to-end

Deliverable: `examples/plan-call-response-8bar.json` — plan schemaVersion 2, 2
section (intro 4 bar tanpa dialog, building 4 bar dengan dialog
melody↔response), total 8 bar, key C major, vibe neo-soul, tempo 84.

Dialog di section "building": 3 siklus call-response (bar 1-3) + 1 exit cue
(bar 4, call diperpanjang jadi whole-note, tanpa response). Siklus 1 = copy
persis (kontur naik D5-F5-A5 → echo A4 staccato oktaf bawah, satu-satunya
copy persis yang diizinkan). Siklus 2 = inversi+fragmentasi (kontur naik
E5-G5-B5 → response 2 not turun B4→G4, masing-masing 0.5 beat, ghost lalu
staccato). Siklus 3 = augmentasi+penyempitan gap (call cuma 2 not E5-G5 →
response 1 not sustain C4 legato mengisi setengah gap, menyisakan bar3
beat4 kosong sebagai gap yang sengaja tak diisi siapa pun). Response
konsisten di oktaf 4 (A4/B4/G4/C4), lead di oktaf 5 — register terpisah.
Semua artic dipakai sesuai fungsi (legato/accent utk call; staccato/ghost/
legato utk response). Tanpa `vel`, tanpa beat off-grid di luar kelipatan
0.5 yang sudah dipakai contoh resep.

## Verifikasi

1. **`python -m pyengine validate examples/plan-call-response-8bar.json`**
   → `{"valid": true, "errors": [], "warnings": []}` — valid, tanpa warning.

2. **`python -m pyengine render examples/plan-call-response-8bar.json -o
   <scratchpad>/plan-call-response-8bar.mid`** → sukses, MIDI 1474 byte
   dihasilkan (dijalankan dari `daw_generative` root dengan venv
   `pyengine/.venv`).

3. **Inspeksi MIDI via `mido`** — 6 track dihasilkan:
   `Dialogue Bridge, drums(104 note_on), bass(10, program 32), comp(42,
   program 4), melody(9 note_on, program 4), response(4 note_on, program
   24 = acoustic guitar nylon)`. Track `response` (guitar) **berisi 4 not
   nyata**, program GM 24 sesuai `acoustic-guitar` — membuktikan jalur
   guitar tidak di-drop diam-diam oleh pyengine.

4. **Cek mekanis non-overlap** (skrip ad-hoc python, interval half-open
   `[abs_beat_start, abs_beat_start+dur)`, `abs_beat = (bar-1)*4 + beat`):
   - melody intervals: `(1,2) (2,3) (3,4) (5,6) (6,7) (7,8) (9,10) (10,11)
     (13,17)`
   - response intervals: `(4,5) (8,8.5) (8.5,9.0) (11,12)`
   - `OVERLAPS = []` — 0 irisan, aturan emas non-overlap terpenuhi
     (termasuk titik singgung tepat di batas siklus, semua legal sesuai
     half-open).

Semua 4 langkah verifikasi sukses tanpa blocker.

## Concerns

- Tidak ada blocker. Satu catatan minor: track index 0 ("Dialogue Bridge")
  adalah meta-track kosong (0 note_on) — normal, itu track judul/tempo,
  bukan voice.

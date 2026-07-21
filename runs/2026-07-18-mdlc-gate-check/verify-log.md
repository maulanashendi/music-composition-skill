# Verify Log — Lampu Basah

`pyengine` **tersedia** di lingkungan eksekusi (`pyengine/.venv/bin/python -m
pyengine --help` sukses, exit 0). Validasi di bawah adalah `pyengine validate`
**sungguhan**, bukan pengecekan manual.

## Iterasi 1 — GAGAL (12 error)

```
python -m pyengine validate plan.json
```

Exit code: 1.

```json
{"valid": false, "errors": [
  {"path": "sections[1].harmony[2]", "code": "chord_unparseable", "message": "simbol chord 'Cmaj9' tak bisa di-parse music21 dan tak ada di CHORD_SYMBOL_OVERRIDES"},
  {"path": "sections[1].harmony[3]", "code": "chord_unparseable", "message": "simbol chord 'Fmaj9' tak bisa di-parse music21 dan tak ada di CHORD_SYMBOL_OVERRIDES"},
  {"path": "sections[1].harmony[6]", "code": "chord_unparseable", "message": "simbol chord 'Cmaj9' tak bisa di-parse music21 dan tak ada di CHORD_SYMBOL_OVERRIDES"},
  {"path": "sections[1].harmony[7]", "code": "chord_unparseable", "message": "simbol chord 'Fmaj9' tak bisa di-parse music21 dan tak ada di CHORD_SYMBOL_OVERRIDES"},
  {"path": "sections[1].voices.bass.notes[4]", "code": "degree_unavailable", "message": "degree 1 tak tersedia di chord 'Cmaj9' pada bar 3 beat 1"},
  {"path": "sections[1].voices.bass.notes[5]", "code": "degree_unavailable", "message": "degree 1 tak tersedia di chord 'Fmaj9' pada bar 4 beat 1"},
  {"path": "sections[1].voices.bass.notes[10]", "code": "degree_unavailable", "message": "degree 1 tak tersedia di chord 'Cmaj9' pada bar 7 beat 1"},
  {"path": "sections[1].voices.bass.notes[11]", "code": "degree_unavailable", "message": "degree 1 tak tersedia di chord 'Fmaj9' pada bar 8 beat 1"},
  {"path": "sections[2].harmony[0]", "code": "chord_unparseable", "message": "simbol chord 'Fmaj9' tak bisa di-parse music21 dan tak ada di CHORD_SYMBOL_OVERRIDES"},
  {"path": "sections[2].harmony[1]", "code": "chord_unparseable", "message": "simbol chord 'Cmaj9' tak bisa di-parse music21 dan tak ada di CHORD_SYMBOL_OVERRIDES"},
  {"path": "sections[2].voices.bass.notes[0]", "code": "degree_unavailable", "message": "degree 1 tak tersedia di chord 'Fmaj9' pada bar 1 beat 1"},
  {"path": "sections[2].voices.bass.notes[1]", "code": "degree_unavailable", "message": "degree 1 tak tersedia di chord 'Cmaj9' pada bar 2 beat 1"}
], "warnings": []}
```

### Root cause (bukan tebakan — diverifikasi langsung ke music21)

`Cmaj9`/`Fmaj9` LOLOS grammar whitelist `_CHORD_GRAMMAR_RE` di
`validator.py` (quality `maj` + ext `9` keduanya ada di alternation
regex), tapi **ditolak music21**:

```
>>> music21.harmony.ChordSymbol("Fmaj9")
Invalid chord abbreviation 'maj9'; see music21.harmony.CHORD_TYPES for
valid abbreviations or specify all alterations.
```

`degree_unavailable` di bass adalah efek samping langsung — chord yang
gagal parse membuat `_active_symbol`/`_chord_stack_len` tak bisa
menghitung stack, jadi `degree 1` (root) pun ditolak, persis pola yang
didokumentasikan `common-errors.md` untuk kode ini ("sering muncul
sebagai efek samping dari chord symbol lain yang salah/gagal parse di
section yang sama").

**Fix di sumbernya (kembali ke keputusan harmoni, bukan tambal
validator):** ganti `Cmaj9`→`Cmaj7add9`, `Fmaj9`→`Fmaj7add9` (pitch
set identik — root,3,5,7,9 — dan **keduanya** lolos grammar **dan**
music21, dikonfirmasi manual). Perubahan diterapkan di `04-harmoni.md`
(retroaktif, lihat catatan Temuan #1 di `gate-report.md`) dan
`plan.json`.

## Iterasi 2 — LOLOS

```
python -m pyengine validate plan.json
```

Exit code: 0.

```json
{"valid": true, "errors": [], "warnings": []}
```

0 error, 0 warning. Tidak ada warning `target_tone_miss` walau bar 3
head sengaja mendarat di 9th (bukan chord-tone triad) di downbeat —
dicek: validator hanya mengecek pitch-class terhadap stack chord aktif
(termasuk ekstensi), bukan hanya triad, jadi 9th dianggap valid target
tone juga (tidak sesempit yang diasumsikan di `05-melodi.md` poin 8).

## Warning review (Step 3)

Tidak ada warning yang perlu ditinjau — 0 warning di iterasi final.

## Ringkasan metrik

- Validitas plan iterasi pertama: **GAGAL** (bukan ≥80% target metrik
  §8 — 1 dari 1 dry-run gagal iterasi pertama; sample size terlalu
  kecil untuk klaim statistik, tapi kegagalannya **sistemik**, bukan
  human error acak — lihat root cause di atas).
- Validitas setelah ≤2 iterasi: **LOLOS** (iterasi ke-2, memenuhi
  target ≥95% "setelah ≤2 iterasi").
- Serahkan `plan.json` (sudah bersih) ke `../rendering-audition/`.

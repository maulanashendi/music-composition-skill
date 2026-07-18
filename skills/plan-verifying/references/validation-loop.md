# Membaca path beralamat dan memetakannya balik

`pyengine validate` melaporkan tiap error/warning dengan `path` bergaya
akses properti (`sections[1].voices.melody.notes[3]`), bukan nomor baris
file mentah. Cara membacanya (dikonfirmasi dari `validator.py`/`linter.py`
nyata, bukan dugaan skema):

- `sections[N]` — section ke-(N+1) (0-indexed) di array `sections` plan.
  Cocokkan ke `name` section di `plan.json` (mis. `sections[1]` = section
  kedua di array, terlepas dari nilai `name`-nya).
- `sections[N].harmony[M]` — event harmoni ke-(M+1) di section itu (array
  `harmony`, urutan sesuai ditulis).
- `sections[N].voices.<nama>` — voice **bernama** `<nama>` di section
  itu. **`voices` adalah objek (dict), bukan array** — path memakai kunci
  string yang persis sama dengan nama voice di `plan.json` (mis. `comp`,
  `bass`, `melody`, `drums`), bukan indeks angka. Jangan salah baca ini
  sebagai `voices[N]`.
- `sections[N].voices.<nama>.notes[M]` — not ke-(M+1) di voice itu (array
  `notes`, urutan sesuai ditulis).
- `meta`, `meta.<field>` (mis. `meta.seed`, `meta.vibe`, `meta.key`) —
  field di objek `meta`.
- `$` — root plan.json itu sendiri; hanya muncul untuk `internal_error`
  (exit 2), berarti crash sebelum sempat memvalidasi field mana pun.

Contoh nyata (dari menjalankan `pyengine validate` atas plan rusak):

```json
{"valid": false, "errors": [
  {"path": "meta", "code": "meta_field_missing", "message": "meta.seed hilang"},
  {"path": "sections[1].harmony[0]", "code": "chord_unparseable", "message": "simbol chord 'ZZbad9' tak bisa di-parse music21 dan tak ada di CHORD_SYMBOL_OVERRIDES"},
  {"path": "sections[1].voices.melody.notes[3]", "code": "dur_invalid", "message": "dur harus > 0, dapat -1"},
  {"path": "sections[1].voices.bass.notes[0]", "code": "degree_unavailable", "message": "degree 1 tak tersedia di chord 'ZZbad9' pada bar 1 beat 1"}
], "warnings": []}
```

## Memetakan balik ke sumber niat

1. Buka `plan.json` di run folder, cari path itu persis — untuk
   `voices.<nama>`, cari kunci itu di objek `voices` section yang
   ditunjuk, bukan menghitung indeks.
2. Identifikasi **fase Ideation** mana yang menghasilkan nilai itu — chord
   symbol salah → kembali ke keputusan harmoni (Fase 2 poin 3 di
   `jazz-composing/SKILL.md`); pitch/durasi/artic melodi salah →
   keputusan melodi (poin 4); nama groove/pattern salah → keputusan
   ritme/groove (poin 5); dsb.
3. Perbaiki di level niat (ubah keputusan chord/melodi/degree), lalu tulis
   ulang field `plan.json` yang sesuai — jangan menambal hanya angka yang
   dilaporkan tanpa mengecek apakah niat di sekitarnya masih konsisten
   (mis. memperbaiki satu chord symbol tapi lupa `degree` bass/melodi di
   section yang sama masih mengasumsikan chord lama — lihat error
   `degree_unavailable` di contoh di atas, yang muncul sebagai efek
   samping dari chord `ZZbad9` yang gagal parse).
4. Catat perbaikan di `verify-log.md`: path, nilai sebelum, nilai sesudah,
   alasan (bukan cuma "fixed").

## Kode error vs warning — cara membedakan tindakan

- `code` yang berarti struktur (mis. `bar_out_of_range`, `beat_out_of_range`,
  `unknown_groove`, `chord_unparseable`, `role_invalid`, referensi section
  tidak ada) SELALU error — wajib diperbaiki sebelum lanjut.
- `code` yang berarti craft (`vibe_tempo_out_of_range`, `target_tone_miss`)
  SELALU warning — boleh diterima sadar dengan alasan tertulis di
  `verify-log.md`.

Kalau ragu suatu `code` masuk kategori mana, percayai field `errors` vs
`warnings` di JSON output — jangan menebak dari nama code saja, karena
daftar code bisa bertambah seiring `pyengine` berkembang (lihat
`contract.md` yang dibaca `jazz-composing` untuk daftar code terkini kalau
`pyengine` menyediakannya di sana; kalau tidak, `code` yang belum dikenal
tetap diperlakukan sesuai kategori `errors`/`warnings` tempat dia muncul).

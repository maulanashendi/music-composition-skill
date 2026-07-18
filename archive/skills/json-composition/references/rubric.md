# Rubrik kualitas — json-composition

Diturunkan dari kontrak §4 (`docs/superpowers/specs/2026-07-16-json-composition-architecture-design.md`,
repo `daw_generative`) dan `baking-feel.md` — bagian dari SOP per modul, sama
seperti rubric `abc-notation`.

Diisi subagent reviewer segar tanpa konteks generasi — skor + alasan 1
kalimat per kriteria.

| Kriteria | Skor (0-2) | Alasan (1 kalimat) |
|---|---|---|
| Schema valid — `validate_composition.py` lulus dengan 0 pelanggaran | | |
| Setiap voice yang dideklarasikan punya isi (`notes` tidak kosong pada section manapun ia dideklarasikan) | | |
| Dinamika tidak datar — `vel` punya sebaran nyata per voice, bukan satu angka diulang | | |
| Feel dibakar eksplisit — ada `beat` off-grid (ghost/lay-back/pickup) di tempat yang dituntut groove, bukan semua nada persis di grid | | |
| Drum ditulis sebagai voice `role:"drums"` dengan nama GM valid (`kick`/`snare`/`hihat`/`ride`), bukan dipaksa jadi pitch biasa | | |

skala 0-2: 0 = tidak ada/kontradiktif, 1 = ada tapi lemah/tidak konsisten,
2 = jelas dan konsisten sepanjang artefak.

Skor rendah pada baris "feel dibakar" atau "dinamika" bukan alasan untuk
melonggarkan baris "schema valid" — keduanya independen: file bisa valid
secara struktur dan tetap terdengar mekanis bila levernya (lihat
`baking-feel.md`) tidak dipakai.

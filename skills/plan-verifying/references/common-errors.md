# Pola error/warning yang sudah ditemukan

Tumbuh dari pengalaman nyata menjalankan `pyengine validate` — tambahkan
entri baru hanya setelah benar-benar ditemukan di sebuah run, bukan
spekulasi "mungkin ini akan terjadi". Kolom `code` memakai nilai persis
yang dicetak `pyengine` (dikonfirmasi dari kode sumber `validator.py`/
`linter.py`, bukan dugaan) — kalau `code` yang kamu lihat tidak ada di
tabel ini, jangan berasumsi maknanya dari nama; lihat kategori
`errors`/`warnings` di JSON output (§"Kode error vs warning" di
`validation-loop.md`).

| `code` | Kategori | Path contoh | Penyebab umum | Cara perbaikan |
|---|---|---|---|---|
| `chord_unparseable` | Error | `sections[N].harmony[M]` | Simbol chord non-standar (mis. singkatan ambigu, typo notasi, tak dikenal `music21`/`CHORD_SYMBOL_OVERRIDES`) | Kembali ke `jazz-composing/references/harmony.md`, tulis simbol standar (mis. `Fmaj9` bukan singkatan ad-hoc yang tidak dikenal parser) |
| `degree_unavailable` | Error | `sections[N].voices.<nama>.notes[M]` | `degree` bass/melodi (mis. `7`, `9`) tidak tersedia di stack chord aktif pada bar/beat itu — sering muncul sebagai *efek samping* dari chord symbol lain yang salah/gagal parse di section yang sama | Cek dulu apakah akar masalahnya `chord_unparseable` di harmony event terkait sebelum mengubah `degree`; kalau chord memang benar tapi stack-nya pendek (mis. triad tanpa 7th), turunkan `degree` ke nilai yang tersedia sesuai niat harmoni |
| `notes_empty` | Error | `sections[N].voices.<nama>` | Voice non-comping/non-drums (`lead`/`bass`/`pad`/`guitar`) dideklarasikan tapi `notes` kosong atau bukan array — hampir selalu bug, bukan silence disengaja | Hapus voice itu dari section (silence disengaja = voice tidak dideklarasikan sama sekali, bukan dideklarasikan dengan `notes: []`) |
| `meta_field_missing` | Error | `meta` | Salah satu dari `title`/`vibe`/`key`/`seed` hilang dari objek `meta` | Kembali ke Fase 1-2 `jazz-composing` untuk keputusan yang belum dikunci; jangan isi placeholder |
| `unknown_vibe` | Error | `meta.vibe` | `meta.vibe` bukan salah satu preset yang dikenal (lihat `VIBE_PRESETS` di `contract.md`) | Pilih preset vibe yang valid, atau tambahkan preset baru di level `pyengine` (keputusan lintas-tools, bukan tambal di plan) |
| `bars_invalid` / `tempo_invalid` / `meter_invalid` | Error | `sections[N]` / `sections[N].tempo` | Nilai `bars`/`tempo`/`meter` di luar rentang atau format yang valid | Perbaiki nilai sesuai kontrak (`bars >= 1` int, `tempo` 20-400, `meter` pola `angka/angka`) |
| `unknown_groove` | Error | `sections[N].groove` | Nama pattern groove tidak ada di `grooves` plan atau `GROOVE_LIBRARY` | Kembali ke `jazz-composing/references/groove-vocabulary.md`, pilih nama groove yang terimplementasi |
| `too_many_sections` / `too_many_bars` / `too_many_voices` / `too_many_notes` / `too_many_harmony` | Error | bervariasi | Plan melebihi LIMITS (32 sections / 512 total bars / 12 voices per section / 4096 notes per voice / 512 harmony per section) | Pecah jadi beberapa run/section lebih ringkas, atau tinjau apakah jumlah itu memang niat musikal (biasanya bukan — indikasi bug generator) |
| `vibe_tempo_out_of_range` | Warning | `sections[N].tempo` | Tempo section di luar `tempoRange` preset vibe di `meta.vibe` | Cek apakah penyimpangan disengaja (catat alasan di `verify-log.md`) atau salah baca preset saat Ideation |
| `target_tone_miss` | Warning | `sections[N].voices.<nama>.notes[M]` (voice `role: lead`) | Not melodi di downbeat (`beat: 1`) bar baru tidak mendarat di chord tone (pitch-nya di luar pitch-class chord aktif) | Kembali ke `jazz-composing/references/melody.md` §target tone, pilih pitch chord-tone (3rd/7th diutamakan) untuk not itu, atau catat alasan sadar kalau efek yang dikejar memang butuh non-chord-tone di titik itu |

Entri baru: tambahkan baris di sini setiap kali sebuah `code` baru
ditemukan di sebuah run yang belum ada jawabannya di tabel ini, setelah
akar masalahnya jelas (bukan sekadar tambalan yang membuat validator
lolos).

# Doktrin: LLM menulis niat, engine menulis not

**Status: doktrin aktif, menggantikan doktrin `json-composition` lama.**
Doktrin lama (skill `json-composition`, kini diarsipkan —
`archive/skills/json-composition/`) menyatakan hal yang sama lewat dua
kalimat sumber berbeda (dikutip verbatim, bukan satu kutipan tunggal):
"The engine does **not** humanize this path" (`skills/json-composition/SKILL.md:57`)
dan "The engine does not humanize the JSON path." (`skills/json-composition/references/baking-feel.md:3`).
Intinya: LLM wajib menulis `vel` per not, `beat` off-grid
per not, dan `artic` per not secara eksplisit, karena tidak ada
humanization di sisi engine untuk jalur JSON.

Doktrin baru membalik ini. `plan.json` (schemaVersion 2) yang ditulis
`jazz-composing` **tidak pernah** berisi angka waktu absolut, velocity
per-not, atau voicing pitch konkret. Yang ditulis LLM hanya niat:

| Elemen | Niat (ditulis LLM) | Not (ditulis `pyengine`) |
|---|---|---|
| Harmoni | Simbol chord per bar/beat (`Fmaj9`, `Dm7b5`) | Voicing pitch konkret + voice-leading |
| Comping | Gaya (`sparse`, `block-chord`, `arpeggiated`) + density (`low`/`med`/`high`) | Not comping aktual, timing, velocity |
| Bass | Scale degree per bar/beat (`1`, `5`, `b7`) | Pitch oktaf konkret, walking-line fill, timing |
| Melodi | Pitch + durasi per not (TANPA velocity, TANPA off-grid) | Velocity, micro-timing/off-grid, artikulasi |
| Drum | Referensi nama pattern dari groove library (mis. `neo-soul-core`) | Grid/hit konkret, swing, humanization |
| Feel/humanization | Tidak ditulis sama sekali — milik engine | Deterministik, ber-`seed` dari `meta.seed` |

Konsekuensi: `plan.json` **tidak boleh** memiliki field `vel`/`velocity`,
`beat` pecahan off-grid (mis. `2.02`), atau daftar pitch literal untuk
voice `chords`/`drums`. Kalau sebuah reference di `jazz-composing/`
mengajarkan menulis nilai seperti itu, itu **bug migrasi** dari doktrin
lama — perbaiki ke level niat, jangan biarkan koeksis.

Alasan flip: doktrin lama terbukti gagal di praktik — lihat entri memori
sesi `ai-hardening-daw-plan-deepdive` dan `gpt56-sela-kota-analysis` di
`daw_generative` (pipeline lama flatten performa: velocity flat, timing
100% grid, artikulasi di-drop — LLM menulis niat presisi yang tidak
pernah benar-benar dipakai downstream). Menaruh presisi di tangan
`pyengine` yang deterministik-ber-seed menghapus kelas kegagalan itu,
sekaligus membebaskan LLM fokus ke keputusan yang memang kuat untuknya:
arc, struktur, pilihan harmoni/melodi tingkat niat.

Deprecation eksplisit: `skills/json-composition/` tidak dihapus dari
sejarah git, hanya dipindah ke `archive/skills/json-composition/`
(Task 6) dengan banner di `SKILL.md`-nya menunjuk balik ke dokumen ini.

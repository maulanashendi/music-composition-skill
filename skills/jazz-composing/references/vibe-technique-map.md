# Vibe → teknik → field skema

Tabel 3 kolom: brief mood mentah → keputusan craft konkret (dari
`mood-to-parameter.md`/`foundation-neo-soul.md`) → field `plan.json` mana
yang diisi (nama field persis ada di `contract.md`, generated — kolom ini
hanya menunjuk *kategori* field, bukan mengulang skema).

| Vibe/mood | Teknik/keputusan craft | Field skema yang diisi |
|---|---|---|
| Tenang, intim | Tempo rendah, harmonic rhythm lambat, comping sparse | `meta.tempo`, harmony event density, comping style/density |
| Urban, malam hari | Neo-soul groove pattern, sinkopasi bass, extended chords (9/11/13) | drum pattern name, bass degree pattern, harmony symbol pool |
| Nostalgia, hangat | Voicing warm register (niat: sebut "warm", bukan pitch), swing ringan | comping style, groove pattern name |
| Tegang, mencari | Tension map naik, outside material (advanced-melody), harmonic rhythm lebih cepat | melody note choice per tension map, harmony symbol density |
| Lega, menerima | Resolusi ke tonic, density turun, ruang (rest) lebih banyak | section-level density/instrumentation niat, ending technique |
| Dialog, saling sahut, berbalas, hidup | Call-and-response lead↔responder, non-overlap, transformasi motif (lihat `call-and-response.md`) | voice kedua `role: "guitar"` (atau `lead` kedua) dengan `notes[]` di gap call |

Baris di atas contoh awal — tambahkan baris baru HANYA dari temuan uji
dengar nyata (lihat `cliche-register.md` untuk pola yang
sudah ditemukan), bukan spekulasi teori.

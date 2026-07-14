# Level 3 — Peta Harmoni

LEVEL 3 — PETA HARMONI
Tujuan
Menentukan bagaimana tension dan resolution bergerak sepanjang lagu.
Harmoni tidak hanya berarti memilih chord. Harmoni adalah desain arah.
Langkah 1: Tentukan tonal center
Contoh:

C major
D minor
F Dorian
G Mixolydian
Multi-tonal
Langkah 2: Tentukan harmonic rhythm
Harmonic rhythm adalah seberapa sering chord berubah.
Contoh:

1 chord per bar
2 chord per bar
1 chord setiap 2 bar
kombinasi
Harmonic rhythm lambat memberi ruang modal.
Harmonic rhythm cepat memberi kesan bebop atau functional jazz.
Langkah 3: Buat harmonic skeleton
Contoh delapan bar:

| Dm7 | G7 | Cmaj7 | Cmaj7 |
| Em7 | A7 | Dm7   | G7    |
Ini baru kerangka fungsi.
Langkah 4: Tentukan fungsi harmonik

Tonic
Predominant
Dominant
Resolution
Temporary tonicization
Modal area
Chromatic departure
Contoh:

Dm7  = predominant
G7   = dominant
Cmaj7 = tonic
A7   = secondary dominant
Langkah 5: Tambahkan warna
Kerangka sederhana:

Dm7 – G7 – Cmaj7
Dapat dikembangkan menjadi:

Dm9 – G13b9 – Cmaj9
Atau:

Dm11 – Db13 – Cmaj9
Langkah 6: Buat tension map
Tandai tingkat tegangan setiap bar.
Contoh:

Bar 1: stabil
Bar 2: mulai bergerak
Bar 3: stabil
Bar 4: terbuka
Bar 5: meningkat
Bar 6: tinggi
Bar 7: dominan kuat
Bar 8: resolusi
Teknik harmonik yang dapat digunakan

* ii–V–I
* secondary dominant
* tritone substitution
* backdoor dominant
* modal interchange
* diminished passing chord
* chromatic mediant
* pedal point
* constant structure
* slash chord
* polychord
* reharmonization
* side-slipping harmony
Output level ini
Lead-sheet harmony tanpa melodi.
Contoh:

A1
| Dm9      | G13b9    | Cmaj9     | A7alt     |
| Dm9      | Db13     | Cmaj9/E   | A7b13     |
A2
| Dm9      | G13      | Cmaj9     | E7alt     |
| Am9      | D7alt    | Dm9 G13   | Cmaj9     |

## Kandidat & seleksi (Level 3)

Level ini memakai protokol kandidat→seleksi (`candidate-selection-protocol.md`):

- Tulis **progresi utama** + **1 alternatif lebih sederhana** + **1 alternatif lebih berani**, masing-masing dengan **exact chord symbols per bar**, sebagai material telanjang.
- Kandidat + verdict selector ditulis ke `03-harmoni-candidates.md`; `03-harmony.md` memakai pemenang.

## Gate — ask, don't guess

- "Chorus tinggal ulang verse aja — kan emang loop, gak masalah." (alasan yang ditolak, lihat RED-FLAGS.md) → Arc dramatis yang tidak pernah berubah bukan arc. Verse dan chorus (atau bagian berulang lain) butuh perkembangan yang bisa didengar — register, density, harmoni, atau interaksi — bukan restatement identik.
- Jika field wajib artefak level ini belum diputuskan brief/level sebelumnya — **tanya, jangan menebak.**

## Cek fakta notasi (wajib sebelum lanjut ke Level 4)

Sebelum artefak `03-harmony.md` dianggap selesai:

1. Tulis progresi terpilih ke satu file ABC kecil (chord symbols per bar di `V:1`), lalu jalankan:
   `cd skills/abc-notation/scripts && uv run --with music21 --with pretty_midi python notation_facts.py <file.abc>`
2. **Lampirkan** output yang relevan (`chord-vs-key` per bar) ke `03-harmony.md`.
3. **Cocokkan tiap label teori** di artefak dengan fakta script — khususnya klaim `modal interchange`/`borrowed`. Contoh nyata dari run lama: `Abmaj7`/`Ebmaj7` dilabeli "borrowed" padahal `notation_facts.py` melaporkannya **`diatonik`** di key minor. Ketidakcocokan = **revisi artefak dulu**, jangan lanjut.
4. Chord yang dilaporkan `unparsed` (simbol tak dikenal script) diperiksa manual — jangan diasumsikan benar hanya karena script tidak bisa menilainya.

## Modul pendalaman

- ../../harmony/SKILL.md

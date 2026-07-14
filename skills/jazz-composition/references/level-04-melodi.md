# Level 4 — Desain Melodi

LEVEL 4 — DESAIN MELODI
Tujuan
Membuat melodi sebagai struktur horizontal, bukan sekadar nada yang ditempelkan pada chord.
Di sinilah interval, broken chord, enclosure, chromaticism, dan outside playing mulai dirancang.
Tahap 1: Tentukan motif inti
Motif dapat berasal dari:

* interval
* ritme
* contour
* repeated note
* arpeggio fragment
* chromatic cell
Contoh motif intervalik:

D – A – F
Struktur interval:

naik perfect fifth
turun major third
Contoh motif ritmis:

pickup – quarter note – two eighth notes – long note
Tahap 2: Tentukan kontur
Contoh:

rendah → naik → puncak → turun
Atau:

angular → stabil → angular → resolusi
Kontur membuat frase terasa memiliki arah.
Tahap 3: Tentukan target tones
Pilih nada utama pada setiap chord.
Contoh:

| Dm7 | G7 | Cmaj7 |
| F   | B  | E     |
Nada target biasanya:

* chord tone
* guide tone
* extension
* alteration yang akan diresolusikan
Tahap 4: Hubungkan target tones
Gunakan:

* stepwise motion
* interval leap
* arpeggio
* chromatic approach
* enclosure
* passing tone
* neighbor tone
Contoh:

F – A – C – B | Bb – B – D – F | E
Tahap 5: Gunakan interval secara sadar
Interval berfungsi membentuk karakter.
Interval kecil
Memberi kesan:

* lyrical
* smooth
* singable
* connected
Interval besar
Memberi kesan:

* angular
* modern
* dramatic
* energetic
Prinsip yang efektif:

leap → recovery
Contoh:

D – Bb – A – G – F
Setelah lompatan besar, melodi kembali dengan gerakan bertahap.
Tahap 6: Gunakan broken chord
Broken chord membuat harmoni terdengar secara linear.
Contoh pada Dm9:

D – F – A – C – E
Jangan selalu berurutan.
Gunakan displacement:

D – A – F – E – C
Atau intervallic arpeggio:

F – C – E – A
Tahap 7: Tambahkan chromatic vocabulary
Gunakan:

* lower approach
* upper approach
* double chromatic approach
* enclosure
* bebop passing tone
Contoh target E:

Eb – E
F – E
F – Eb – E
D – F – E
Tahap 8: Tentukan area outside
Outside playing harus direncanakan berdasarkan tension map.
Outside dapat berupa:

* altered dominant
* side-slipping
* chromatic sequence
* upper-structure triad
* triad pair
* interval displacement
* superimposed harmony
* temporary tonal shift
Contoh:

Inside:
D – F – A – C
Outside:
Eb – Gb – Bb – Db
Resolution:
E – G – C – B
Outside akan terdengar efektif apabila:

* pola ritmenya kuat
* bentuk motifnya jelas
* durasinya terbatas
* resolusinya nyata
Tahap 9: Bedakan tema dan improvisational vocabulary
Tema utama sebaiknya memiliki:

* motif jelas
* interval khas
* ritme mudah dikenali
* ruang
* repetisi
* variasi
Bagian development dapat memuat:

* arpeggio panjang
* side-slipping
* chromatic line
* interval fourth
* outside sequence
* polyrhythm
Jangan memasukkan seluruh vocabulary jazz ke dalam head.
Output level ini
Melodi utama dalam bentuk notasi atau MIDI yang sudah memiliki:

* motif
* kontur
* target tone
* tension
* resolution
* ruang
* identitas ritmis

## Kandidat & seleksi (Level 4)

Level ini memakai protokol kandidat→seleksi (`candidate-selection-protocol.md`):

- Tulis **3 kandidat motif**, masing-masing sebagai **notasi ABC 1-2 bar** + fakta objektif: jumlah pitch aktual (rest **bukan** pitch), interval aktual antar nada berurutan (semitone + nama interval), relasi tiap nada ke chord (chord-tone / tension / outside).
- Fakta objektif itu **wajib** diambil dari `../../abc-notation/scripts/notation_facts.py` pada tiap kandidat (jangan mengklaim dari ingatan) — lihat juga bagian "Cek fakta notasi" di bawah.
- Kandidat + verdict selector ditulis ke `04-melodi-candidates.md`; `04-melody.abc` memakai pemenang.

## Gate — ask, don't guess

- "Chorus tinggal ulang verse aja — kan emang loop, gak masalah." (alasan yang ditolak, lihat RED-FLAGS.md) → Arc dramatis yang tidak pernah berubah bukan arc. Verse dan chorus (atau bagian berulang lain) butuh perkembangan yang bisa didengar — register, density, harmoni, atau interaksi — bukan restatement identik.
- Jika field wajib artefak level ini belum diputuskan brief/level sebelumnya — **tanya, jangan menebak.**

## Cek fakta notasi (wajib sebelum lanjut)

Sebelum artefak `04-melody.abc` (dan tiap kandidat motif di `04-melodi-candidates.md`) dianggap selesai:

1. Jalankan pada notasi motif/melodi:
   `cd skills/abc-notation/scripts && uv run --with music21 --with pretty_midi python notation_facts.py <file.abc> --voice <id>`
2. **Lampirkan** output relevan (jumlah pitch, interval antar nada, klasifikasi chord-tone/tension/outside) ke artefak.
3. **Cocokkan tiap label teori** dengan fakta script. Contoh nyata dari run lama yang harus tertangkap: motif diklaim "4-not" padahal `notation_facts.py` hanya melaporkan **3 pitch** (rest bukan pitch); arpeggio chord-tone dilabeli "outside" padahal script melaporkannya `chord-tone`. Ketidakcocokan = **revisi dulu**, jangan lanjut.
4. Nada yang jatuh di bar dengan chord `unparsed` diperiksa manual.

## Modul pendalaman

- ../../melody-design/SKILL.md
- ../../advanced-melody/SKILL.md (untuk tahap 7-8: chromatic vocabulary & outside playing)

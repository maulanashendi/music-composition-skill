# Level 7 — Desain Comping dan Voicing

LEVEL 7 — DESAIN COMPING DAN VOICING
Tujuan
Menghindari permainan solid chord yang statis.
Comping harus menjadi bagian dari dialog musikal.
Hindari block chord terus-menerus
Sebagai alternatif, gunakan:

* shell voicing
* rootless voicing
* quartal voicing
* spread voicing
* upper structure
* drop voicing
* intervallic voicing
* cluster
* moving inner voice
Contoh rootless voicing
Dm9:

F – C – E – A
G13:

F – B – E – A
Cmaj9:

E – B – D – G
Perhatikan voice leading:

F tetap
C turun ke B
E tetap
A tetap
Gunakan voicing sebagai gerakan
Bukan:

Chord 1 dipukul
Chord 2 dipukul
Chord 3 dipukul
Tetapi:

top note bergerak
inner voice bergerak
bass bergerak
ritme berubah
density berubah
Teknik comping

* Charleston rhythm
* anticipatory stab
* sustained pad
* fragmented chord
* rhythmic answer
* fill
* call and response
* delayed resolution
* pedal voicing
Output level ini
Comping chart per bagian:

A1: sparse, 2–3 attacks per bar
A2: syncopated responses
Bridge: denser voicing
Solo: interactive comping
Head out: simplified voicing

## Gate — ask, don't guess

- Jika field wajib artefak level ini belum diputuskan brief/level sebelumnya — **tanya, jangan menebak.**

## Cek fakta notasi (wajib sebelum lanjut)

Sebelum comping chart / voicing dianggap selesai:

1. Tulis voicing per bar sebagai bracket chord ABC (`[..]`) di voice keys, lalu jalankan:
   `cd skills/abc-notation/scripts && uv run --with music21 --with pretty_midi python notation_facts.py <file.abc> --voice <keys-id>`
2. **Lampirkan** output `top-note` per bar + daftar nada bawah→atas ke artefak.
3. **Cocokkan klaim voice-leading top-note** dengan fakta script. Contoh nyata dari run lama: klaim "top note bergerak G→F→E" padahal voicing yang benar-benar tertulis punya top-note lain. Ketidakcocokan = **revisi voicing dulu**, jangan lanjut. (Ingat: `notation_facts.py` melaporkan **pitch tertinggi** sebagai top note, sesuai oktaf ABC — verifikasi voicing ditulis di oktaf yang dimaksud.)

## Modul pendalaman

- ../../arrangement/SKILL.md

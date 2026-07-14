# Level 13 — Dinamika dan Dramaturgi

LEVEL 13 — DINAMIKA DAN DRAMATURGI
Tujuan
Membuat lagu terasa hidup dari awal sampai akhir.
Buat peta dinamika observabel
Angka persentase (mis. "Intro 20%") adalah klaim yang tak bisa
diverifikasi dari notasi — jangan dipakai. Ganti dengan **tabel per
section berisi metrik observabel**:

| Metrik | Sumber |
|---|---|
| Active voices | hitung manual dari partitur/ABC per section |
| Note-attacks per bar | output `notation_facts.py` per voice (`../../abc-notation/scripts/notation_facts.py`, sudah ada dari Gelombang 1) |
| Register lead | rendah/tengah/tinggi + rentang aktual |
| Durasi not rata-rata | dari notasi per section |
| Drum hits per bar | dari `drums.json`/roadmap drum |
| Dynamic marks | dari notasi (mf, mp, dst., bila ada) |

Micro-apex (field wajib)
Satu bar spesifik per piece (atau per bagian besar) yang menjadi momen
paling berarti, ditulis sebagai **"bar N: <mekanisme>"**. Mekanisme harus
dari kelas **non-volume**: register ekstrem tipis (satu nada
tinggi/rendah sesaat), dissonance singkat, drop groove (instrumen
berhenti sesaat), ruang kosong (rest terjadwal), dsb — **bukan** "volume
naik" atau "semua instrumen tutti".

**Gate**: section yang dilabeli "tidak ada peak"/"restrained" tanpa
micro-apex yang terdefinisi = **ditolak** — restrained tidak sama dengan
datar; artefak tetap menunjuk satu momen mekanisme non-volume yang
membuat section itu diingat.
Parameter dinamika
Bukan hanya volume.
Gunakan:

* register
* density
* articulation
* harmonic tension
* rhythmic activity
* number of instruments
* note duration
* silence
Output level ini
Tabel metrik observabel per section + field micro-apex.

## Gate — ask, don't guess

- Jika field wajib artefak level ini belum diputuskan brief/level sebelumnya — **tanya, jangan menebak.**

## Modul pendalaman

- ../../arrangement/SKILL.md

# Rubrik kualitas — midi-orchestration

Diturunkan dari `quality-control.md` §13 (Production and DAW-first design),
plus subset "DAW plan" dari §14 (Machine-readable plans) yang relevan ke
output MIDI/DAW modul ini — bagian dari SOP lama, kini didistribusikan per
modul. Subset "Composition plan" dari §14 dan format laporan §17/§18 ada
di `skills/jazz-composition/references/scorecard-template.md`.

Diisi subagent reviewer segar tanpa konteks generasi — skor + alasan 1
kalimat per kriteria.

| Kriteria | Skor (0-2) | Alasan (1 kalimat) |
|---|---|---|
| Komposisi kering (tanpa noise/filter/degradasi) sudah berfungsi sebelum efek produksi ditambahkan | | |
| Setiap track/role punya identitas yang jelas dan berbeda; automation punya tujuan musikal | | |
| Event data eksak (pitch, velocity, offset, gate) tersedia untuk motif kritis, bass, voicing, dan groove class — nilai berada dalam rentang valid | | |
| Pitch name dan nilai MIDI konsisten satu sama lain di seluruh track | | |
| Perubahan state produksi (layer masuk/keluar) memperkuat form, bukan menutupi section yang belum siap | | |
| `output.mid`: jumlah track, notes-per-track > 0 untuk semua voice, dan tag tempo/meter cocok — diverifikasi langsung dari file MIDI, bukan hanya exit status validator | | |

skala 0-2: 0 = tidak ada/kontradiktif, 1 = ada tapi lemah/tidak konsisten,
2 = jelas dan konsisten sepanjang artefak.

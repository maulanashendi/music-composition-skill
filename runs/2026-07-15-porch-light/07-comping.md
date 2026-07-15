# 07-comping.md — Level 7: Desain Comping dan Voicing (Porch Light)

## Comping chart per bagian

| Section | Kepadatan | Cell comping |
|---|---|---|
| A1/A2/A3 (bar 1-3, 5-6) | sparse, 1 attack (sustained) | **Sustained pad** — voicing `F-A-C` ditahan penuh 1 bar, tidak diserang ulang |
| A1/A2/A3 (bar 4, **semua repeat**) | 1 attack, tertunda | **Delayed answer** — `z6 [FAC]2`: diam 3 ketuk, baru diserang di ketuk terakhir, persis sesudah lead menyelesaikan target tone (C→A, Level 4) — bukan cuma A2, direvisi Tahap 15 supaya berlaku konsisten di semua repeat A (lihat catatan revisi di bawah) |
| A1/A2/A3 (bar 7) | 1 attack, ditahan masuk | **Held-back entrance** — `z4 [FAC]4`: diam setengah bar (saat lead masih aktif A→G), baru masuk di paruh kedua — bukan "anticipatory stab" (diserang sebelum beat) seperti draft awal, melainkan entrance yang ditahan sampai lead selesai; direvisi Tahap 15 dari draft awal yang ternyata tidak benar-benar tertulis di notasi (lihat `scorecard.md` L2-cliche) |
| A1/A2/A3 (bar 8) | sparse, 1 attack (sustained) | **Sustained pad** (resolusi) — voicing identik ditahan penuh, hanya bass yang bergerak |
| B (bar 9-16) | denser, 1 attack/bar + voice-leading | **Fragmented chord / moving inner voice** — rootless voicing bergerak tiap bar mengikuti perubahan chord (lihat tabel di bawah) |
| Solo chorus | interactive, variatif | **Call-and-response** — LH merespons frasering RH (detail penuh Level 10) |
| Head out | simplified, kembali ke sustained pad | sama seperti A1 bar 1-6 |

## Comping cells mengikuti ruang lead
Lead (Rhodes RH, Level 4) bernapas panjang di bar 2, 4, 5, 7 (partial), 8 — LH mengisi ruang itu dengan **sustained pad** (bar 1,2,3,5,6,8 — diam mengikuti lead di bar-bar yang harmoni memang statis per thesis Level 1), **delayed answer** (bar 4, menjawab tepat sesudah lead selesai), dan **held-back entrance** (bar 7, masuk di paruh kedua saat lead sudah diam). Tiga cell berbeda ini **benar-benar tertulis di notasi** (`song.abc`, diverifikasi `notation_facts.py`) — bukan hanya deskripsi prosa yang tidak terealisasi (lihat catatan revisi Tahap 15 di bawah).

### Revisi Tahap 15 — temuan L2-cliche
Reviewer segar L2-cliche menemukan bahwa draft awal `song.abc` **mengklaim** 3 cell ini di dokumen (`07-comping.md`) tapi **notasi sebenarnya** memakai `[FAC]8` (1 attack/bar tanpa variasi) di SEMUA 8 bar A section, semua 7 kemunculan A (56 dari 80 bar) — klaim vs notasi tidak cocok, persis pola RED-FLAG yang diperingatkan `CLAUDE.md` proyek ("skor rubrik/klaim tinggi tidak berarti notasi benar-benar begitu"). Diperbaiki: bar 4 tiap repeat A diubah ke `z6 [FAC]2`, bar 7 diubah ke `z4 [FAC]4` — sekarang **konsisten di semua 7 repeat A** (bukan cuma A2 seperti draft awal), diverifikasi ulang lewat `notation_facts.py` (chord-tone/diatonik tetap benar, register tetap dalam band comping 46-60 MIDI setelah revisi register Level 14).

## Voicing A section (beku — device inti)
`F-A-C` (rootless — bass instrumen sudah bawa root/pedal terpisah) ditahan **identik** di semua 8 bar A (A1/A2/A3), termasuk bar 7-8 resolusi. Hanya bass yang bergerak; comping tidak berubah sama sekali.

## Voicing B section (bergerak — kontras)
Rootless voicing 4-not (3-5-7-9 style) per bar, mengikuti guide-tone Level 3:

| Bar | Chord | Voicing (bawah→atas, sesuai tertulis) | Top-note (fakta) |
|---|---|---|---|
| 9 | Bbmaj7 | D F A c | **C** |
| 10 | A7b9#5 | C# F G Bb | **Bb** |
| 11 | Gm9 | Bb(oktaf bawah) D F A | **A** |
| 12 | C7b9#5 | E G# Bb Db | **Bb** |
| 13 | FM9 | C E G A | **A** |
| 14 | Ebmaj7 | D F G Bb | **Bb** |
| 15-16 | A7b9#5 | C# F G Bb | **Bb** |

## Cek fakta notasi (`notation_facts.py`, wajib sebelum lanjut)

Dijalankan: `cd skills/abc-notation/scripts && uv run --with music21 --with pretty_midi python notation_facts.py ../../../runs/2026-07-15-porch-light/07-comping-check.abc --voice 2`

- **Bar 1-8 (A section): `top-note=A` di SEMUA 8 bar, tanpa kecuali.** Ini mengonfirmasi klaim inti — voicing benar-benar tidak berubah, termasuk saat harmoni "resolve" di bar 8 (`F/D`). Fakta ini adalah bukti langsung device thesis Level 1 bekerja di level voicing, bukan cuma klaim prosa.
- **Bar 9-16 (B section): top-note bergerak C→Bb→A→Bb→A→Bb→Bb.** **Koreksi dari rencana awal** (rencana informal membayangkan garis turun linear penuh) — fakta menunjukkan top note bergerak dalam **band sempit A-Bb-C (rentang minor third)**, bukan garis lurus turun. Ini tetap merupakan voice-leading yang halus (top note tidak pernah lompat jauh, selalu stepwise/whole-tone di dalam band sempit) — deskripsi direvisi supaya cocok dengan fakta: "moving inner voice dalam register sempit", bukan "garis turun linear".
- Semua chord ter-parse (tidak ada `unparsed`); klasifikasi chord-tone/tension-diatonik/luar-key/borrowed sesuai fungsi yang diklaim di `03-harmony.md`.

## Kandidat & seleksi
Level 7 tidak memakai protokol kandidat→seleksi (single-shot, hanya Level 1-4). Voicing di atas adalah keputusan langsung composer, diverifikasi via `notation_facts.py`.

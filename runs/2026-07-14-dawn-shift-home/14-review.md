# 14 — Review & Detail Low Level

## Artefak final

`song.abc` (3 voice: Lead Trumpet, Rhodes, Bass — chord symbols pada
voice Bass sebagai referensi harmoni tunggal), `drums.json` (=copy dari
`09-drums.json`, format v2), `output.mid` (pitched.mid + drums.mid
di-merge).

## Ekstensi kecil pada tooling (transparan, bukan pengubahan musik)

`skills/midi-orchestration/scripts/abc_to_midi.py`'s `PROGRAM` dict tidak
punya keyword untuk trumpet/flugelhorn (hanya sax/horns/rhodes/piano/
bass/upright/strings/pad/guitar). Sesuai undangan eksplisit di
`midi-orchestration/references/midi-conversion.md` ("Extend the map in
the script for other instruments"), ditambahkan **satu baris**:
`"trumpet":56` (GM Trumpet, konsisten skema 0-indexed yang sudah dipakai
entry lain di dict yang sama). Voice lead diberi nama `"Lead Trumpet"`
supaya (a) trigger deteksi mono-lead yang sudah ada (`"lead" in
name.lower()`) dan (b) match keyword `trumpet` untuk GM program yang
benar — dua kebutuhan sekaligus tanpa mengubah perilaku lookup untuk nama
lain manapun (pure addition, bukan pengubahan entry lama). Test suite
`test_abc_to_midi_and_grid.py` dijalankan ulang sebelum dan sesudah
perubahan: **14 passed, 0 failed** (tidak ada regresi).

## Cek fakta notasi — final (Level 14)

`validate_abc.py song.abc`: **OK, 0 errors, 0 warnings**.

`notation_facts.py --voice {1,2,3}` dijalankan pada `song.abc` utuh untuk
verifikasi MEKANIS (jumlah not/rest per voice, bukan re-verifikasi
chord-vs-key — itu sudah tuntas di gate Level 3/7 lewat file segmented
terpisah, lihat catatan di bawah):

| Voice | Notes | Rests | Cocok dengan desain? |
|---|---|---|---|
| 1 Lead Trumpet | 13 | 18 | Ya — 13 not persis sesuai `04-melody.abc` + echo section 6 (2+1+1+2+2+2+1+1+1=13), 18 rest token persis (12 bar tacet bar1-12 + 6 rest parsial lain) |
| 2 Rhodes | 67 | 5 | Ya — 5 rest = 4 bar tacet awal (1-4) + 1 bar tacet akhir (24), 67 not = akumulasi voicing 3-4 not/bar bar5-23 |
| 3 Bass | 51 | 11 | Ya — cocok tepat dengan tabel bar-per-bar di `08-bassline.md` |

**Catatan penting soal `chord-vs-key` di file gabungan**: `song.abc`
memakai SATU header `K:C` global (F natural, cocok D Dorian, bar1-14),
tapi bar15-24 memakai F# eksplisit (`^F`) untuk D Mixolydian tanpa
inline key change (karena `notation_facts.py` hanya membaca key SIGNATURE
pertama yang ditemukan, inline `[K:...]` tidak akan mengubah analisis
scale-nya — keterbatasan tool, bukan kesalahan musik). Akibatnya kolom
`chord-vs-key` pada run di atas untuk bar16-24 salah menyebut chord itu
"borrowed" padahal terhadap D Mixolydian yang benar semuanya `diatonik`
(sudah diverifikasi benar terpisah dengan file 2-segmen ber-`K:` yang
tepat — lihat `03-harmony.md` dan `07-comping.md`). Verifikasi PITCH per
not (chord-tone, jumlah, interval) di run final ini tetap valid dan
tidak terpengaruh keterbatasan itu, karena chord-tone diperiksa terhadap
chord symbol langsung, bukan terhadap key.

Tidak ada voice yang menghasilkan 0 not (bug "voice marker tak diulang"
dari `RED-FLAGS.md` **tidak terjadi** — diverifikasi lewat jumlah not
mekanis di atas, bukan diasumsikan dari validator saja).

## Verifikasi MIDI mekanis (output.mid, bukan hanya exit status validator)

```
Tracks: 4
Tempo changes: [(0.0, 74.0)]
Time signatures: [(4, 4, 0.0)]
Total end time: 77.84s  (= 24 bar x 4 beat x 60/74 s/beat = 77.84s, PERSIS cocok)

Lead Trumpet   notes=13  max-poly=1  end=77.84s  longest-note=3.24s
Rhodes         notes=67  max-poly=4  end=74.59s  longest-note=3.24s
Bass           notes=51  max-poly=1  end=77.84s  longest-note=3.24s
Drums          notes=126 max-poly=2  end=68.31s  longest-note=0.18s
```

- **Track count**: 4 (Lead, Rhodes, Bass, Drums) — sesuai kuartet.
- **Tempo/meter**: 74 BPM / 4/4, cocok persis `Q:1/4=74` dan `M:4/4` di
  header `song.abc` — diverifikasi dari MIDI langsung, bukan diasumsikan.
- **Mono lead**: Lead Trumpet max-poly=1 — Fix 2 (`midi-conversion.md`)
  bekerja.
- **No drone**: not terpanjang 3.24s (~1 bar, whole-note chord/root-hold)
  — tidak ada not multi-bar; Fix 1 (chord-symbol stripping) bekerja,
  tidak ada drone chord-symbol yang ikut ter-render sebagai not panjang.
- **Sync**: Lead & Bass berakhir tepat di 77.84s (24 bar penuh — keduanya
  menahan not sampai bar 24). Rhodes berakhir 74.59s (1 bar lebih awal =
  PERSIS bar 24, sesuai desain "Rhodes reda diam di bar 24"). Drums
  berakhir 68.31s (PERSIS di titik aksen bar 22, sesuai desain "diam
  total bar 23-24"). Ketiga selisih ini bukan desync — masing-masing
  cocok bar-demi-bar dengan `06-arrangement.md`/`09-drums.json`, bukan
  gap tak terjelaskan.

## Gate check (Level 14)

`validate_abc.py` lulus 0 error. `output.mid` diverifikasi langsung
(track count, notes-per-track, tempo, time signature, sync) — semua
cocok dengan desain, tidak ada voice 0-not. Piece dianggap selesai secara
mekanis (L1); L2 menyusul di `scorecard.md`; L3 (telinga) tetap kosong.

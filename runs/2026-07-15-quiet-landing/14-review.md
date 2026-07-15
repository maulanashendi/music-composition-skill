# Level 14 — Review low level

## L1 hasil aktual
- `validate_abc.py song.abc`: **0 errors, 0 warnings**.
- `drums.json`: valid JSON; 48 bar; `grid_to_midi.py` menghasilkan 426 hits.
- `output.mid`: 4 track musikal (format MIDI 1 menyertakan satu track metadata kosong); masing-masing memiliki notes; tempo 76.0001 BPM; meter 4/4; lead max-polyphony 1.

## Temuan dan revisi
| Temuan | Before | After | Efek terdengar |
|---|---|---|---|
| Arc awal berisiko terlalu tegang bila A7alt muncul berulang | A1/A2 memakai A7alt di semua akhir gesture | A1/A2 awal memakai A7sus4; A7alt hanya phrase-end besar (16/24) | Tarikan dominant menjadi event yang dapat didengar, bukan warna konstan. |
| Ending berisiko menjadi fade-tonic template | Coda hanya Dm9 dengan drum memudar | `E` ditahan di atas Dm6/9 dan D pedal (bar 41–48) | Nada yang sebelumnya menggantung terdengar berubah fungsi menjadi warna hangat. |
| Audit L2 menemukan G# outside tak terdokumentasi dan comping terlambat di bar 28 | A7alt berisi G#; Rhodes menyerang setelah C# masuk | G# dihapus; stab Rhodes dipindah ke akhir bar 27, Rhodes diam di bar 28 | C#→E menjadi satu push kromatik yang fokus dan resolusinya tidak tertutup comping. |

## Risiko terbuka
L2 reviewer segar, audit cliché/blind, dan L3 telinga manusia masih belum selesai; artifact tidak boleh diklaim “enak” sebelum L3.

# Level 3 — Peta Harmoni: Quiet Landing

**Tonal center:** D minor, dengan coda Dm6/9 sebagai minor yang menghangat.

**Harmonic rhythm:** 1 chord/bar = 4×60/76 = **3.16 detik per chord**, melampaui batas ±2 detik; sesuai BPM 72–92.

## Skeleton dan tension map

| Bar | Chord | Fungsi | Tension |
|---:|---|---|---|
| 1–8 | Dm11, A7sus4, Dm9, Gm9, Bbmaj9, A7sus4, Dm9, A7alt | home → suspended departure → phrase pull | 1→3 |
| 9–16 | Dm9, Gm9, Bbmaj9, A7sus4, Dm9, Gm9, Em7b5, A7alt | head; minor ii–V pull | 2→4 |
| 17–24 | Dm9, Bbmaj9, Gm9, A7sus4, Dm9, Gm9, Bbmaj9, A7alt | head return; graft keeps early motion calm | 2→4 |
| 25–32 | Fmaj9, Gm9, C13sus4, A7alt, Bbmaj9, Gm9, Em7b5, A7alt | detour / narrow peak | 3→5 |
| 33–40 | Dm9, C/E, Bbmaj9, Gm9, Fmaj9, Gm9, A7sus4, A7alt | release, E enters bass then opens outward | 2→4 |
| 41–48 | Dm6/9, Bbmaj9/D, Gm9/D, Dm6/9, Dm6/9, Bbmaj9/D, Dm6/9, Dm6/9 | acceptance; D pedal and E as 9th/6-9 color | 1 |

## Cek fakta notasi
`03-harmony-facts.abc` lolos `validate_abc.py` (0 error, 0 warning). `notation_facts.py` mengklasifikasikan Dm11/Dm9/Gm9/A7sus4/Em7b5/C/E sebagai diatonik; A7alt sebagai borrowed (tekanan terarah). Beberapa extension/slash symbol (`Bbmaj9`, `Fmaj9`, `C13sus4`, `Dm6/9`) tidak diparse oleh helper; fungsi dan spellings tersebut diperiksa manual, tanpa mengklaimnya sebagai hasil otomatis.

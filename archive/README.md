# Arsip skill lama

Skill/modul di sini digantikan oleh 3 skill MDLC (`jazz-composing`,
`plan-verifying`, `rendering-audition`) per
`docs/superpowers/plans/2026-07-18-mdlc-skills.md` di `daw_generative`
(repo utama, bukan repo ini). Diarsipkan, bukan dihapus — reversibel via
git kalau ada konten yang perlu ditarik kembali. Setiap subfolder di sini
punya alasan arsip di baris pertama filenya sendiri atau di tabel di
bawah.

| Folder diarsipkan | Diganti oleh | Alasan |
|---|---|---|
| `jazz-composition/` | `skills/jazz-composing/` | Orchestrator SOP 14-level note-level digantikan workflow Brief-Ideation-Plan; level 5-14 (ritme presisi, voicing, drum, detail) kini kerja `pyengine`, bukan LLM. |
| `harmony/`, `melody-design/`, `advanced-melody/`, `vibes-mood/`, `groove-rhythm/`, `arrangement/` | `skills/jazz-composing/references/*` | Isi craft niat-level dimigrasi; isi note-level presisi (voicing exact, tick offset) diarsipkan di sini karena kini domain `pyengine`. |
| `json-composition/` | `contract.md` generated (dibaca `jazz-composing`) + doktrin baru | Doktrin lama dibalik: LLM kini menulis niat, `pyengine` yang humanize. Doktrin lama dinyatakan verbatim di dua tempat berbeda — "The engine does **not** humanize this path" (`skills/json-composition/SKILL.md:57`) dan "The engine does not humanize the JSON path." (`skills/json-composition/references/baking-feel.md:3`). Lihat `docs/DOCTRINE-NIAT-BUKAN-NOT.md`. |
| `midi-orchestration/` (skrip + sebagian reference) | `skills/rendering-audition/` (untuk yang masih relevan) + `pyengine` (untuk konversi) | `abc_to_midi.py`/`grid_to_midi.py`/`drums_to_engine.py` digantikan pipeline `pyengine`; interaction-map/ensemble craft dimigrasi ke `jazz-composing`. |

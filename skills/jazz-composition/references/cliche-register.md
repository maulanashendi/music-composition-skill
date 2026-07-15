# Register cliché — neo-soul/AI-jazz

Daftar pola yang berulang kali muncul di output paket ini dan terasa
"template di-reskin". Dipakai oleh protokol **L2-cliche** (lihat
`scorecard-template.md` bagian "L2 global" dan `../SKILL.md` §Penilaian):
reviewer segar menandai bagian notasi final yang **match** entri di bawah
**tanpa reinterpretasi yang terlihat**; composer wajib merespons tiap
temuan dengan **revisi** atau **justifikasi audible spesifik**.

Cliché **bukan larangan mutlak** — semua device di bawah valid secara
teori dan lolos rubrik. Kehadirannya tanpa reinterpretasi adalah sinyal
"template di-reskin", bukan komposisi original. Karena itu tiap entri
wajib punya tiga kolom: nama, kenapa terasa template, dan jalur
reinterpretasi yang menyelamatkan — **entri tanpa jalur reinterpretasi
tidak lengkap.**

| Cliché | Kenapa terasa template | Jalur reinterpretasi |
|---|---|---|
| Intro 2-bar pad + motif preview lalu lead masuk | Pola paling umum di semua contoh genre, nol variasi struktural | Gate intro performatif di `level-12-intro-ending.md` (incomplete voicing / delayed entrance / frase "mencari" / ruang disengaja) |
| Ending fade + held tonic | Sama, default paling aman | Opsi rekontekstualisasi di `level-12-intro-ending.md` (nada tegang dipertahankan, harmoni di bawahnya berubah hingga nada itu terasa diterima) |
| Chromatic approach di tiap transisi bass | Approach note jadi refleks, bukan pilihan sadar | Kuota chromatic ≤1/3 + tabel device per transisi chord di `level-08-bass.md` |
| Harmonic rhythm seragam 1 chord/bar full-piece dengan semua perpindahan di barline | Tak ada variasi harmonic rhythm sama sekali | Variasikan lewat teknik `../../harmony/SKILL.md` — 2 chord/bar terukur via rumus durasi absolut per chord (≥2 detik per chord) |
| Rhodes block-chord 1 attack/bar sepanjang lagu | Comping statis, bukan dialog musikal | Gate ≥3 comping cell + pemetaan ke napas lead di `level-07-comping-voicing.md` |
| Drum pattern identik section-wide | Melanggar hierarchy drum v2 dari Gelombang 1 (base 2-bar + variation + transition) | Aturan hierarchy di `level-09-drum.md` |
| Progresi i-bVI-iv-V verbatim tanpa reinterpretasi | Progresi paling dikenal genre dipakai mentah | Reharmonize sebagian / ubah voicing / ubah bass motion |
| "Restrained = tanpa momen berarti" | Dalih untuk section datar | Gate micro-apex di `level-13-dinamika-dramaturgi.md` (satu bar mekanisme non-volume) |
| Velocity random sebagai pengganti frase | `humanize_velocity` dipakai sebagai sumber variasi utama, bukan polish terakhir | `phrase_velocity` per bar (Gelombang 1 — lihat `level-09-drum.md` dan `grid_to_midi.py`) |

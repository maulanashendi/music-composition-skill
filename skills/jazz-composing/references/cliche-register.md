# Register cliché — neo-soul/AI-jazz

Daftar pola yang berulang kali muncul di output paket ini dan terasa
"template di-reskin". Dipakai oleh protokol **L2-cliche** (lihat
`../../jazz-composition/references/scorecard-template.md` bagian "L2
global" dan `../../jazz-composition/SKILL.md` §Penilaian): reviewer segar
menandai bagian niat final yang **match** entri di bawah **tanpa
reinterpretasi yang terlihat**; composer wajib merespons tiap temuan
dengan **revisi** atau **justifikasi audible spesifik**.

Cliché **bukan larangan mutlak** — semua device di bawah valid secara
teori dan lolos rubrik. Kehadirannya tanpa reinterpretasi adalah sinyal
"template di-reskin", bukan komposisi original. Karena itu tiap entri
wajib punya tiga kolom: nama, kenapa terasa template, dan jalur
reinterpretasi yang menyelamatkan — **entri tanpa jalur reinterpretasi
tidak lengkap.**

| Cliché | Kenapa terasa template | Jalur reinterpretasi |
|---|---|---|
| Intro 2-bar pad + motif preview lalu lead masuk | Pola paling umum di semua contoh genre, nol variasi struktural | Gate intro performatif di `../../jazz-composition/references/level-12-intro-ending.md` (incomplete voicing / delayed entrance / frase "mencari" / ruang disengaja) |
| Ending fade + held tonic | Sama, default paling aman | Opsi rekontekstualisasi di `../../jazz-composition/references/level-12-intro-ending.md` (nada tegang dipertahankan, harmoni di bawahnya berubah hingga nada itu terasa diterima) |
| Chromatic approach di tiap transisi bass | Approach note jadi refleks, bukan pilihan sadar | Kuota chromatic ≤1/3 + tabel device per transisi chord di `../../jazz-composition/references/level-08-bass.md` |
| Harmonic rhythm seragam 1 chord/bar full-piece dengan semua perpindahan di barline | Tak ada variasi harmonic rhythm sama sekali | Variasikan lewat teknik `../../harmony/SKILL.md` — 2 chord/bar terukur via rumus durasi absolut per chord (≥2 detik per chord) |
| Rhodes block-chord 1 attack/bar sepanjang lagu | Comping statis, bukan dialog musikal | Gate ≥3 comping cell + pemetaan ke napas lead di `../../jazz-composition/references/level-07-comping-voicing.md` |
| Drum pattern identik section-wide | Melanggar hierarchy drum v2 dari Gelombang 1 (base 2-bar + variation + transition) | Aturan hierarchy di `../../jazz-composition/references/level-09-drum.md` |
| Progresi i-bVI-iv-V verbatim tanpa reinterpretasi | Progresi paling dikenal genre dipakai mentah | Reharmonize sebagian / ubah voicing / ubah bass motion |
| "Restrained = tanpa momen berarti" | Dalih untuk section datar | Gate micro-apex di `../../jazz-composition/references/level-13-dinamika-dramaturgi.md` (satu bar mekanisme non-volume) |
| Variasi density seragam per bar sebagai pengganti frase | Density/comping-activity dipakai statis sepanjang lagu, bukan sebagai polish niat terakhir — **bukan lagi soal velocity**: velocity kini murni domain `pyengine` (lihat `../../../docs/DOCTRINE-NIAT-BUKAN-NOT.md`), jadi variasi harus ada di level niat (density per bar, bukan angka velocity) | Variasikan **density** (comping/melody activity) per bar mengikuti napas frase — niat-level, ditulis di `plan.json` sebagai density section/bar, bukan velocity |

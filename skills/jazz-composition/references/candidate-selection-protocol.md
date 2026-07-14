# Protokol kandidat → seleksi (Level 1-4)

Mengganti pola **generate-then-defend** (menulis satu artefak lalu membelanya) dengan **generate-kandidat → seleksi-independen**. Berlaku **hanya** di 4 level ber-leverage tinggi: Level 1 (konsep), Level 2 (bentuk), Level 3 (harmoni), Level 4 (motif/melodi). Level lain tetap single-shot — ini sengaja, untuk menghindari ledakan paperwork 14 level × 3 kandidat.

## Aturan generasi per level

- **Level 1 — Konsep.** Wajib menulis field **aesthetic thesis**: 1 kalimat ide musikal spesifik yang bisa **didengar**, bukan daftar atribut genre. Contoh baik: "satu nada yang awalnya terasa salah tak pernah dihilangkan; di akhir, harmoni di bawahnya berubah sehingga nada yang sama terasa diterima." Plus **2 konsep kandidat berbeda secara struktural** (ini yang akhirnya memenuhi tuntutan rubrik `vibes-mood` "minimal dua konsep berbeda secara struktural").
- **Level 2 — Bentuk.** **≥2 alternatif bentuk** sebelum memilih (mis. through-composed vs. return-with-recontext), masing-masing 2-3 kalimat + risiko statis/simetrisnya.
- **Level 3 — Harmoni.** Progresi utama + **1 alternatif lebih sederhana** + **1 alternatif lebih berani**, masing-masing dengan **exact chord symbols per bar**.
- **Level 4 — Melodi.** **3 kandidat motif**, masing-masing wajib ditulis sebagai **notasi ABC 1-2 bar** + fakta objektif: jumlah pitch aktual (rest **bukan** pitch), interval aktual antar nada berurutan (semitone + nama interval), dan relasi tiap nada ke chord (chord-tone / tension / outside). Jalankan `../../abc-notation/scripts/notation_facts.py` pada tiap kandidat untuk mendapat fakta ini — jangan mengklaim dari ingatan.

## Protokol seleksi (anti self-justification)

1. Generator menghasilkan kandidat sebagai **material telanjang**: notasi/struktur + fakta objektif + **maksimal 1 kalimat intent**. **Dilarang** menulis pembelaan/rasionalisasi per kandidat di tahap ini.
2. Seleksi dilakukan oleh **subagent segar** (selector) yang menerima **hanya**: brief, aesthetic thesis, material kandidat, dan fakta objektif. Selector **tidak** menerima preferensi/urutan favorit generator — pola yang sama dengan "Reviewer segar (L2)" di `../SKILL.md`, diperluas ke titik seleksi (bukan hanya penilaian akhir).
3. Selector memilih **1 pemenang** + alasan berbasis **efek yang akan terdengar** (bukan nama teori), dan boleh menyarankan **graft** — mengambil elemen dari kandidat lain ke pemenang.
4. Hasil seleksi dicatat di run folder:
   - kandidat ditulis ke artefak `NN-<level>-candidates.md` (`01-konsep-candidates.md`, `02-arsitektur-candidates.md`, `03-harmoni-candidates.md`, `04-melodi-candidates.md`);
   - verdict selector ditulis di **bagian akhir artefak yang sama** (bukan file terpisah);
   - artefak utama level itu (`01-brief.md`, `02-form.md`, `03-harmony.md`, `04-melody.abc`) memakai **pemenang seleksi**, bukan rata-rata atau gabungan tanpa keputusan eksplisit.
5. **Fallback tanpa subagent** (mis. composer pack di browser AI tanpa Claude Code): self-selection oleh agent yang sama **diizinkan**, **tapi** wajib **pre-mortem** — tulis 1 kelemahan konkret tiap kandidat **sebelum** memilih, dan kalimat pemilihan pemenang harus **secara eksplisit** mereferensikan kelemahan itu (mis. "dipilih kandidat B meski kelemahannya X, karena kelemahan A dan C lebih berat untuk brief ini").

## Kontrak artefak ramping (`*-candidates.md`)

Khusus keempat artefak `*-candidates.md` — **bukan** kontrak 11-field penuh artefak level lain:

| Field | Isi |
|---|---|
| Objective | Efek audible yang dikejar (1-2 kalimat) |
| Immutable constraints | Batasan dari brief yang tidak boleh dilanggar kandidat manapun |
| Assumptions | Asumsi yang diambil generator saat brief tidak eksplisit |
| Kandidat | Material telanjang tiap kandidat (lihat aturan per level di atas) |
| Selected + alasan | Pemenang + alasan berbasis efek terdengar (bukan nama teori) |
| Exact artifact | Rujukan ke artefak utama level ini yang memakai pemenang |
| Unresolved/confidence | Hal yang masih terbuka + tingkat keyakinan seleksi |

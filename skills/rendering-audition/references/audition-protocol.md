# Human-ear spot-check protocol (layer 3)

Protokol uji dengar skill ini punya tiga lapis:

1. **Automated gate** — sudah diselesaikan fase Verify (`plan-verifying`):
   `python -m pyengine validate` lulus tanpa error. Cheap, catches breakage.
2. **LLM-judge, blind pairwise** — subagent segar tanpa konteks generasi
   menilai dua kandidat terhadap rubrik (`rubric-checklist.md`) tanpa tahu
   mana yang mana. Cheap, scalable, catches theory/craft gaps.
3. **Human ear, blind A/B** — dokumen ini. Butuh orang sungguhan mendengar
   audio sungguhan, yang tak bisa dilakukan atau dipalsukan agent manapun.
   Lapis 1-2 eksplisit **tidak bisa** mensertifikasi "enak didengar"; hanya
   lapis ini yang bisa.

Untuk eksperimen evaluasi skill/paket ini sendiri (before/after, A/B teknik),
jalankan lapis 3 pada subset kecil (2 brief cukup), bukan tiap run eval —
lapis ini mahal, dipakai sengaja.

**Klarifikasi cakupan (penting):** aturan sampling di atas ("2 brief cukup",
"tidak tiap run eval") **hanya berlaku untuk eksperimen evaluasi skill/paket
ini sendiri** (mis. eval before/after teknik komposisi — dicatat sebagai
hasil audition sebelumnya di run folder yang sama). Untuk **piece produksi**
— composer benar-benar membuat lagu untuk dipakai, bukan mengevaluasi skill
— **L3 wajib per-piece** sebelum piece itu disebut selesai; tidak ada
sampling untuk kasus ini. Gerbang mekanis sebelum L3 boleh dijalankan: lapis
1-2 di atas (fail-closed).

## 1. Render kandidat ke audio

```bash
python -m pyengine audition <path/to/plan.json> -o <run-folder>/audition/
```

adalah jalur primer — menghasilkan `<slug>.mid` + `<slug>.wav` sekali jalan
(stdout JSON `{"midi","wav","durationSec"}`; `durationSec` = wall-clock waktu
render, **bukan** durasi lagu). Kalau agent memakai server `daw_generative`
alih-alih CLI `pyengine` langsung, `POST /api/render` (body `plan.json`)
adalah alternatif — lihat `references/engine-http-alternative.md`.

## 2. Anonymize sebelum mendengarkan

Ganti nama file hasil render supaya pendengar tidak bisa menebak kandidat
mana yang mana, mis. `brief-01-recording-1.wav` / `brief-01-recording-2.wav`,
dengan mapping A/B sungguhan ditulis terpisah oleh yang me-render (tidak
dibagikan ke pendengar sampai setelah skor). Acak posisi "Recording 1" per
brief — jangan biarkan kandidat B selalu di slot yang sama, atau pendengar
akan pattern-match, bukan menilai.

## 3. Skor blind

Untuk tiap rekaman, independen (tanpa membandingkan catatan antar rekaman
sampai keduanya selesai dinilai):

- Apakah dia hidup sebagai satu piece musik, terlepas dari "kebenaran teori"?
- Apakah groove terasa fisik/danceable/bernapas, atau mekanis?
- Apakah arc emosional dari brief (mis. "ragu ke penerimaan") benar-benar
  terasa, atau cuma terbaca sebagai gerak harmonik generik?
- Ada satu hal yang merusak pengalaman mendengar (lompatan yang terasa tidak
  playable, desync yang mengganggu, section yang terlalu lama)?

Baru setelah keduanya dinilai independen: mana yang lebih disukai, dan
kenapa — dengan kata sendiri, bukan menurunkan ulang rubrik.

## 4. Catat hasilnya

Tambahkan entri bertanggal ke run folder (mis. `scorecard.md` bagian L3, atau
`tests/results/<date>-human-ear-<brief>.md` untuk eval skill), berisi: brief
mana, label anonim dan mapping A/B sungguhannya, catatan independen per
rekaman, verdict preferensi, siapa yang mendengarkan. Jangan menimpa entri
sebelumnya — ini log berjalan, bukan satu scoreboard.

## Seperti apa "berhasil" dari waktu ke waktu

Lapis 1-2 sudah menunjukkan with-skill menang skor rubrik pada eval historis
tanpa konfirmasi human-ear. Berhasil di lapis ini berarti preferensi itu
bertahan lewat telinga, bukan cuma di atas kertas — kalau spot-check
human-ear mulai konsisten tidak sepakat dengan rubrik, itu sinyal rubriknya
mengukur sesuatu yang tidak melacak "enak", dan rubrik (bukan craft
komposisi) yang perlu ditinjau ulang.

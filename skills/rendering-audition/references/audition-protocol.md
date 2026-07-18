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

## Kriteria kelulusan per vibe

Kriteria berikut diturunkan dari `VIBE_PRESETS` di `pyengine/pyengine/contracts.py`
(rentang tempo/swing per vibe, groove default `neo-soul-core`) + karakter
musikal genre masing-masing. Dipakai di L3 (human ear) sebagai daftar
konkret, bukan pengganti empat pertanyaan umum di §3 — jawab keempatnya
dulu, baru cek kriteria per-vibe di bawah untuk piece dengan `meta.vibe`
yang sesuai.

### `neo-soul` (tempo 70-95 bpm, swing 0.55-0.62, mode dorian/mixolydian/minor)

- **Pocket terasa laid-back**, bukan on-the-grid: onset drum/bass sedikit
  di belakang beat, konsisten sepanjang piece — kalau terasa "buru-buru"
  atau tepat di grid, revisi `swing`/`timeOffsetTicks` di groove profile
  plan (bukan tambah delay effect).
- **Ghost notes terasa** di comping/drum — bukan flat semua di satu
  velocity; kalau comping terdengar rata/robotic, revisi `density`/velocity
  per-hit di `voices.<name>` plan, bukan tambah humanize acak.
- **Ruang antar-frase (rest) ada** — melodi/comping tidak mengisi tiap
  slot 16th; kalau terasa penuh/tak bernapas, revisi phrase length/rest
  ratio di melody plan section terkait.
- Swing terasa halus (bukan shuffle 100% ala medium-swing) — kalau
  terdengar seperti straight-eighth (nyaris tanpa swing), cek `swingRange`
  section itu masih dalam 0.55-0.62.

### `ballad` (tempo 55-75 bpm, swing 0.50-0.55, mode major/minor)

- **Napas antar-frase terasa** lewat tempo per section (bukan rubato
  in-bar — engine tidak punya rubato dalam bar) — kalau frasa terdengar
  terburu tanpa jeda antar kalimat, revisi bar count/panjang section atau
  `tempo` section berikutnya di plan, bukan menambah rest acak.
- **Sustain kerasa** — note length panjang pada pad/lead, bukan staccato
  rata; kalau terdengar terputus-putus, cek `articulation`/`lengthMultiplier`
  di voice lead/pad.
- **Dinamika naik lembut menuju klimaks** — velocity/density section
  klimaks harus lebih tinggi dari section pembuka tapi progresif, bukan
  loncatan tiba-tiba; kalau klimaks terasa flat atau lompat kasar, revisi
  kurva velocity antar-section di arrangement plan.
- Tempo section tetap dalam 55-75 bpm — kalau terasa jauh lebih cepat dari
  itu, piece ini bukan lagi "ballad" secara vibe, cek `meta.vibe`/tempo
  section.

### `medium-swing` (tempo 100-132 bpm, swing 0.62-0.68, mode major/dorian/mixolydian)

- **Swing offbeat konsisten** sepanjang piece — triplet-feel di semua
  layer (bass/comping/melodi) sepakat, bukan sebagian straight sebagian
  swing; kalau ada layer yang terasa lurus di tengah layer lain yang
  swing, cek groove profile dipakai konsisten oleh semua voice section
  itu.
- **Walking bass terasa mengalir** (quarter-note walk yang punya arah,
  bukan lompat interval acak) — kalau bass terasa patah-patah/tidak
  logis, revisi kontur bass line di plan (approach note ke chord tone
  berikutnya).
- **Artikulasi ringan** (comping/melodi tidak overdrive berat, attack
  jelas tapi tidak staccato kasar) — kalau terdengar terlalu berat/keras
  utk swing medium, cek `articulation`/velocity comping tidak melebihi
  karakter "ringan" yang dimaksud.
- Tempo section dalam 100-132 bpm dan swing 0.62-0.68 — kalau terasa
  lebih dekat ke shuffle neo-soul (lebih lambat/laid-back), cek
  `meta.vibe`/`tempoRange` section tidak salah tempel.

## Seperti apa "berhasil" dari waktu ke waktu

Lapis 1-2 sudah menunjukkan with-skill menang skor rubrik pada eval historis
tanpa konfirmasi human-ear. Berhasil di lapis ini berarti preferensi itu
bertahan lewat telinga, bukan cuma di atas kertas — kalau spot-check
human-ear mulai konsisten tidak sepakat dengan rubrik, itu sinyal rubriknya
mengukur sesuatu yang tidak melacak "enak", dan rubrik (bukan craft
komposisi) yang perlu ditinjau ulang.

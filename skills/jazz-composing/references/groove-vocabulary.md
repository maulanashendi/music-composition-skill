# Groove vocabulary — nama pattern, bukan angka

Ideation memilih **nama** pattern dari groove library `pyengine`; angka
tick/swing/gate-ratio di baliknya adalah implementasi engine, bukan
pengetahuan yang perlu ditulis LLM.

**Saat ini `GROOVE_LIBRARY` pyengine hanya berisi SATU entri: `neo-soul-core`.**
Kategori lain di tabel di bawah (straight/four-on-floor, ballad brush,
uptempo swing) **belum terimplementasi** — itu arah pertumbuhan yang
dicatat sebagai gambaran kategori, BUKAN pattern yang bisa dirujuk plan
hari ini. Wajib cek `contract.md` (generated) untuk daftar id groove yang
benar-benar sah saat ini; **dilarang mereferensikan groove id yang tidak
ada di `contract.md`** hanya karena tercantum di tabel kategori berikut.

| Kategori pattern | Status | Kapan dipakai | Field plan.json |
|---|---|---|---|
| Neo-soul core groove (`neo-soul-core`) | Terimplementasi | Default genre-first, backbeat laid-back | pattern reference per section drum |
| Straight/four-on-floor | Belum ada di `GROOVE_LIBRARY` | Vibe lebih tegas/mekanis (jarang di genre ini) | pattern reference |
| Ballad brush | Belum ada di `GROOVE_LIBRARY` | Tempo lambat, dinamika intim | pattern reference |
| Uptempo swing | Belum ada di `GROOVE_LIBRARY` | Bagian solo/energik | pattern reference |

Kalau vibe menuntut pattern yang belum ada di `contract.md`, itu bukan
alasan menebak angka tick sendiri — catat sebagai kebutuhan pattern baru
untuk `pyengine` (di luar cakupan skill ini) dan pilih pattern terdekat
yang tersedia (saat ini itu berarti `neo-soul-core`) sambil menandai
keterbatasannya di run folder.

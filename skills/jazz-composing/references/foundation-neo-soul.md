# Neo-soul / chill-jazz — profil genre

Diadaptasi dari genre file skill Claude Code `compose-song`
(`references/genres/neo-soul.md`, konsolidasi 2026-07-13), yang sendirinya
diadaptasi dari skill Hermes `original-neo-soul-composition` (MIT). Genre ini
dipilih sebagai genre **pertama** yang punya profil konkret di paket ini,
selaras style family `Jazzhop / neo-soul` yang sudah ada di
`style-cheatsheets.md` — file ini memperdalamnya, bukan menggantikannya.
Genre lain (bebop, modal, bossa, dst.) tetap pakai `style-cheatsheets.md`
sebagai starting point; adaptasi prinsip di sini + beri label "default"
eksplisit bila brief minta genre di luar keduanya.

**JANGAN** meniru artis, lagu, atau aransemen berhak cipta secara literal —
terjemahkan referensi jadi atribut musikal (tempo, tekstur, densitas harmoni,
artikulasi, dinamika, emotional arc). Governing principle: *jaga fondasi
cukup predictable untuk fokus, sambil mengembangkan permukaan cukup untuk
memberi reward pada perhatian.* Orisinalitas datang dari **kombinasi** motif
+ voicing + groove + phrasing + palet + arrangement — bukan dari nama chord
yang rumit.

## Musical DNA baku

| Parameter | Nilai default profil |
|---|---|
| Tempo zone | 68-86 BPM (pocket santai; halftime feel untuk tempo lebih cepat) |
| Meter | 4/4, swing ringan / sixteenth ter-humanize |
| Tonal center | Mayor (hangat/terbuka) atau minor-modal (introspektif); borrowed harmony boleh mengaburkan batas |
| Palet (peran→instrumen) | Anchor: Rhodes/Wurlitzer + finger bass + drum lo-fi · Rotation: clean guitar, soft synth, sax, flute, piano · Ear-candy: reverse tail, chord stab, perc fill |
| Density ceiling | ≤ 1 foreground voice pada satu waktu |

Nilai-nilai ini adalah titik mulai, bukan hukum — sesuaikan dengan brief vibe
selama tetap dalam keluarga neo-soul/chill-jazz. Bila hilir akhir adalah
engine `daw_generative` (`POST /api/render`), catat bahwa engine itu saat ini
hanya merealisasi `4/4` — cek dulu sebelum menjanjikan meter lain di plan;
konverter music21 milik paket ini sendiri (modul `midi-orchestration`, dulu
`abc-to-midi-orchestration`) tidak punya batasan itu.

## 1. Vibe map (lensa genre)

Gunakan tujuh dimensi `reasoning-theory.md` Modul 1 sebagai basis. Untuk
neo-soul, kontras yang paling umum berguna: elemen mana yang lebih
terang/tajam/lebar/animated dibanding fondasi yang stabil. Contoh kalimat
intent: *"Track fokus nocturnal hangat — Rhodes, bass, dan drum berdebu
tetap stabil sementara gitar, synth, dan piano bergantian membawa pernyataan
melodi pendek."*

## 2. Model peran (anchor / rotation / ear-candy)

| Layer | Fungsi | Instrumen tipikal |
|---|---|---|
| **Anchor** | Stabilitas & fokus | Rhodes/Wurlitzer, bass, drums |
| **Rotation** | Pengembangan & karakter | Clean guitar, soft synth, sax, flute, piano |
| **Ear candy** | Momen penemuan kecil | Reverse tail, chord stab, perc fill, tape stop, ambience |

Tiap sound punya SATU peran; jangan biarkan semua instrumen berlaku sebagai
lead. Di tiap momen, identifikasi eksplisit siapa foreground/support/
background — ini adalah kasus konkret dari element leadership per section
(`reasoning-theory.md` Modul 4, Lensa 2) diterapkan ke ensemble neo-soul.

## 3. Harmoni fungsional & voice-leading

Urutan pengerjaan (selaras Modul 5 `reasoning-theory.md`, level menengah→kecil):

1. Fungsi tiap area harmoni: home / departure / tension / return.
2. Gerak root/bass sederhana.
3. Tambahkan seventh chord.
4. Tambahkan 9/11/13/sus/altered/borrowed **hanya bila memperbaiki warna atau
   gerak melodi** — cek katalog sebab-akibat (`reasoning-theory.md` Modul 3)
   untuk mengapa tiap device.
5. Voicing dengan inner-voice halus (detail konkret voicing/register/attack
   ada di `skills/harmony/references/voicing-systems.md` — dulu
   `abc-to-midi-orchestration/references/exact-voicing.md` — dikerjakan
   di modul itu — di sini cukup putuskan *warna dan gerak*, bukan pitch
   pastinya).
6. Uji melodi di atas voicing; revisi chord yang melawan motif.

Kosakata warna (detail sebab-akibat di `reasoning-theory.md` Modul 3):
maj7/maj9/6-9 (hangat) · m7/m9/m11 (lembut) · 7sus/9sus/13sus (gerak tanpa
agresi) · secondary dominant (arah) · altered dominant (tensi singkat) ·
borrowed iv/modal interchange (wistful) · slash/inversi (bass melodis) ·
chromatic approach (transisi, hemat).

Voice-leading: prioritaskan common tone + gerak setengah/whole step di inner
voice · bass membawa root sehingga chord instrument boleh **omit root** · top
note tiap voicing = countermelody tersembunyi · jangan taruh semua ekstensi
di semua chord · spread voicing rendah agar tak mud (lihat §9 arah mix).

## 4. Satu motif sebelum menulis solo

Motif 3-7 nada / satu sel ritmis yang tahan ditransformasi: dipindah oktaf,
dimainkan instrumen lain, digeser ritmis, dipendekkan ke 2-3 nada terakhir,
di-reharmonisasi di section B, dikutip bass/Rhodes/outro.

Pengembangan motif (bukan improvisasi acak): **Statement → Answer → Fragment
→ Expansion → Absence.**

- **Statement** — mainkan motif dengan jelas.
- **Answer** — ubah interval/ritme akhirnya.
- **Fragment** — pakai sebagian saja.
- **Expansion** — perpanjang satu not atau tambah ekor.
- **Absence** — beri ruang kosong supaya motif "diingat", bukan diulang.

Motif = identitas; solo/improvisasi = interpretasi identitas itu, bukan hal
terpisah. Ini adalah **hook** dalam istilah `ideation-theory.md` §5 — beri
hook itu bentuk fragmen, lengkap, dan return ter-transformasi, sama seperti
di `composition-plan-template.json`. Selesai bila ≥3 section memakai versi
ter-transformasi dari motif yang sama tanpa menyalin frasa persis.

## 5. Desain pocket (drum + bass)

**Drum:** kick bulat minim click · snare/rimshot/clap dusty · sebagian
backbeat sedikit di belakang grid · variasikan velocity hi-hat + sisakan gap
· ghost note sebagai feel (bukan hiasan) · fill pendek & bermakna (di batas
section, bukan tiap 4 bar).

**Bass:** mulai root + nada panjang · approach note dekat perubahan chord ·
slide/ghost/sinkopasi selektif · sederhana saat lead aktif, lebih melodis
saat lead istirahat · koordinasi dengan kick tanpa mirror tiap hit.

**Pocket rule:** jangan humanize acak tiap nada — tetapkan relasi konsisten.
Angka konkret pocket (offset tick per peran, gate ratio) sudah dibakukan di
`skills/groove-rhythm/references/groove-profiles.md` (dulu
`abc-to-midi-orchestration/references/groove-profiles.md`) sebagai profil
`neo-soul-core` — otak komposisi di sini cukup **memilih profil itu**, bukan
menghitung ulang ticks per not. Selesai bila groove tetap terasa disengaja
saat hanya drum + bass + voicing chord paling sederhana yang terdengar.

**Doktrin drum paket ini (mengikat, tidak bisa disimpangi per-genre):**
drum **SELALU** direpresentasikan sebagai step-grid JSON
(`skills/midi-orchestration/assets/drum-grid-template.json`, dulu
`abc-to-midi-orchestration/assets/drum-grid-template.json`), **TIDAK
PERNAH** sebagai voice ABC `clef=perc`/`%%MIDI drummap`. ABC di paket ini
hanya untuk suara berpitch (lead, keys, bass) — lihat
`skills/abc-notation/references/drums-and-abc.md` (dulu
`abc-notation-writer/references/drums-and-abc.md`). Ini beda dari repo
`compose-song` sumber adaptasi (yang punya opsi ABC `clef=perc` di engine
`daw_generative`-nya sendiri); jangan bawa opsi itu ke paket ini.

## 6. Rotasi lead tanpa kehilangan identitas

Kontras dari **timbre & register**, bukan kekerasan. Pola:

```
Lead 1 states → silence → Lead 2 answers → rhythm section breathes → Lead 3 transforms
```

Tiap lead punya window 2-4 bar; hanya **satu** foreground pada satu waktu;
instrumen yang keluar jadi tekstur/countermelody/silence; kosakata motif
dibagi lintas performer; artikulasi tiap instrumen distinct (gitar bisa
bend/muted attack, synth sustain, piano jawaban ritmis, sax/flute pakai
napas/curve panjang). Selesai bila tiap lead punya alasan masuk, alasan
keluar, dan relasi ke motif pusat. Eksekusi konkretnya (siapa main di bar
mana) adalah interaction map — job modul `midi-orchestration` (dulu
`abc-to-midi-orchestration`) Step 2; di sini cukup rencanakan pola
rotasinya.

## 7. Variasi terkontrol

Repetisi perlu untuk fokus. Cegah bosan dengan mengubah **1-2 dimensi saja**
per interval:

| Interval | Perubahan yang pantas |
|---|---|
| Tiap 4 bar | Fill, ghost, pickup, chord stab, jawaban lead kecil, silence singkat |
| Tiap 8 bar | Voicing, top note, pola hat, ending bass, instrumen motif, chord akhir |
| Tiap 16 bar | Rotasi lead, ganti tekstur, area harmoni baru, breakdown, geser register |
| Tiap 32 bar | Detour struktural, puncak emosi, subtraksi besar, return penuh |

**Variation budget** tiap section baru: pertahankan ≥2 anchor (mis. groove +
warna harmoni) · ubah 1 dimensi primer · opsional 1 detail sekunder ·
**jangan** ubah harmoni + groove + lead + palet + dinamika serentak. Pakai
**subtractive arrangement** sesering additive — menghilangkan kick/hat/bass/
lead sejenak sering lebih efektif daripada menambah instrumen baru. Ini
sumbu B ("massive + original" — lihat `CLAUDE.md` proyek): variation budget
yang sama bisa dipakai berulang untuk batch banyak output tanpa jadi 1
template di-reskin.

## 8. Arsitektur arrangement

Proporsi andal (bukan hukum kaku):

```
Intro 8 · A1 16 · A2 16 · B/detour 8-16 · A3 16 · Breakdown 8 · Final A 16 · Outro 8
```

| Section | Fungsi dramatik |
|---|---|
| Intro | Tetapkan tekstur & fragmen motif; tahan groove penuh |
| A1 | Sajikan harmoni inti, bass, drum, lead pertama |
| A2 | Pertahankan groove, ganti lead/voicing/ending bass |
| B/detour | Kontras harmonik/modal/tekstural/ritmis — tak wajib chord baru; kontras bisa dari pedal bass, hapus drum, geser register, reassign motif |
| A3 | Kembali dengan makna terakumulasi, bukan copy literal |
| Breakdown | Kurangi densitas, reset perhatian |
| Final A | Sajikan motif paling jelas atau ensemble exchange terkontrol |
| Outro | Lepas elemen satu-satu, sisakan bayangan motif |

Selesai bila tiap section beda dari kemunculan sebelumnya di ≥1 dimensi
bermakna (variation budget §7). Arsitektur ini sejalan dengan arc-first di
`ideation-theory.md` §4b — petakan arc dulu (mis. intim→build→puncak→return),
baru pasang proporsi bar di atas arc itu, bukan sebaliknya.

## 9. Arah sound & mix

Compose & arrange **sebelum** mengandalkan efek. Kick/bass hangat & center ·
hindari cluster chord register-rendah bertabrakan dengan bass · saturasi/
tape/vinyl subtil · lead lebih definisi upper-mid · reverb/delay sebagai ekor
frasa, bukan wash konstan · sisakan ≥1 sumber clarity supaya "lo-fi" tak jadi
buram. Hierarki yang harus tetap audible di volume rendah: groove dulu,
atmosfer harmonik kedua, lead rotasi jelas tapi tak dominan seperti vokal
pop.

> **Timbre jujur (prinsip visi proyek):** penilaian akhir "enak" pakai
> sampel/soundfont senyata mungkin ke hasil akhir (mis. lewat konverter
> music21 paket ini ke DAW/BandLab, atau lewat `POST /api/render` bila hilir
> adalah engine `daw_generative`), bukan synth generik atau preview kasar
> sebagai keputusan final.

## Common Pitfalls

| Gejala | Perbaikan |
|---|---|
| Chord rumit tanpa ide memorable | Tulis motif dulu (§4), ekstensi menyusul dengan alasan |
| Semua instrumen bunyi terus | Assign foreground/support/silence eksplisit per section (§2, `reasoning-theory.md` Modul 4 Lensa 2) |
| Variasi terasa acak | Jaga ≥2 anchor, ubah 1 dimensi primer (§7) |
| Loop terasa persis diulang | Variasikan voicing/orkestrasi/ending bass/subtraksi, bukan cuma ulang |
| Terlalu banyak solo | Statement pendek + rest (§6), bukan noodling berkepanjangan |
| "Lo-fi" jadi semua muffled | Sisakan 1-2 elemen jernih (§9) |
| Bass & Rhodes saling masking | Omit-root voicing, pisahkan register (`reasoning-theory.md` Modul 3) |
| Humanize tanpa pocket | Pakai profil `neo-soul-core` yang konsisten (§5), bukan offset acak |
| B section terasa lagu lain | Pertahankan motif/groove fingerprint/warna harmoni inti |
| Meniru referensi terlalu literal | Ekstrak atribut (tempo/tekstur/densitas), cipta ulang harmoni/melodi/ritme sendiri |

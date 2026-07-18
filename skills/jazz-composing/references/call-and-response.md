# Call and response — resep phrase-level antar-voice

> Menutup gap: `arrangement.md` §1 (empat peran) dan §2 "Call and
> response" menyebut dialog lead↔answer secara konseptual, tapi tidak
> punya resep phrase-level yang memetakan ke `plan.json`. File ini
> mengisi gap itu. Dipakai di Fase Ideation poin 4 (Desain Melodi) dan
> poin 6 (Aransemen) dari `../SKILL.md`.

## Kapan dipakai

Call-and-response adalah salah satu **teknik** interaction map
(`arrangement.md` §1), bukan default tiap section. Karena "arc
menentukan density":

- Cocok di section **building** atau **mid** — dialog menambah hidup
  saat density sedang naik.
- **Jangan** di section **quiet/lonely** — section itu butuh space,
  bukan dua voice saling isi.
- **Jangan** di section **peak** — peak adalah tutti, semua voice
  aktif bersama, bukan bergantian.
- Maksimal **satu pasangan dialog aktif** per section. Dua pasangan
  call-response sekaligus di section yang sama menghasilkan
  kepadatan yang bertabrakan dengan sendirinya.
- Tidak setiap section perlu dialog — sebagian besar piece hanya
  butuh 1-2 section dengan call-and-response eksplisit (lihat
  `arrangement.md` §1 "Do not use all of these in one piece").

## Anatomi: caller & responder

- **Caller** = voice melodi utama, `role: "lead"`. Ini yang memulai
  frasa (call).
- **Responder** = voice KEDUA yang membawa `notes[]` eksplisit (pitch
  konkret, bukan gaya). Default: `role: "guitar"`, `instrument:
  "acoustic-guitar"` (lane register niat ~52-88, MIDI E3-E6 —
  menengah, di bawah lead supaya tidak menutupi). Alternatif:
  responder = `role: "lead"` kedua dengan instrument berbeda dari
  caller (mis. caller `rhodes`, responder `alto-sax` register
  ~55-82) bila timbre setara dengan caller diinginkan.
- **`role: "chords"` TIDAK bisa jadi responder frasa konkret.**
  Comping (voice `chords`) hanya membawa `style`+`density` — tidak
  ada `notes[]` pitch eksplisit untuk dibentuk jadi frasa jawaban
  yang presisi. Kalau ingin comp "menjawab", itu adalah density
  comping naik sesaat, bukan dialog call-and-response niat-level di
  file ini.
- **`role: "pad"` bukan responder.** Pad berkarakter statis/sustain,
  bukan pembawa frasa yang punya kontur dan exit.
- Responder harus berada di **lane register berbeda** dari caller —
  jangan sampai responder menutupi register caller (lihat
  `arrangement.md` §"Peran + lane register" dan §2 "Piano or guitar
  comping" → Avoid "covering the soloist's register").

## Lima keputusan wajib sebelum menulis notes

Formalisasi dari `arrangement.md` §2 "Call and response" ("Define:
caller; response length; whether response copies rhythm, contour,
pitch, or energy; number of cycles; exit cue"):

1. **Siapa caller & responder** — voice mana, instrument apa (lihat
   Anatomi di atas).
2. **Panjang call, gap, dan response** dalam bar/beat. Contoh sehat:
   call 2 bar yang menyisakan gap 1-2 beat di akhir bar kedua,
   response mengisi gap itu (mis. 1-1.5 beat) sebelum call berikutnya
   mulai.
3. **Apa yang di-copy response** — ritme, kontur, pitch, atau energi.
   Pilih **1-2 saja**, jangan semua sekaligus (lihat §"Response =
   transformasi motif" di bawah).
4. **Jumlah siklus** — 2-4 pasangan call↔response per section.
   Kurang dari 2 tidak terasa seperti dialog; lebih dari 4 mulai
   terasa mekanis kecuali arc memang minta itu.
5. **Exit cue** — bagaimana dialog ditutup. Contoh: call terakhir
   diperpanjang (augmented) sampai menyentuh kadens, sehingga
   responder tidak lagi punya gap untuk masuk dan dialog berhenti
   secara natural, bukan tiba-tiba dipotong.

## Aturan emas: non-overlap

Response hidup di **GAP** yang ditinggalkan call, titik. Dihitung dari
field grid `plan.json` (`bar`/`beat`/`dur`), bukan timing off-grid
(off-grid milik `pyengine`, lihat `../../../docs/DOCTRINE-NIAT-BUKAN-NOT.md`):

- Not pertama response mulai **pada atau setelah** akhir not terakhir
  frasa call (`bar_call_end.beat + dur_call_end` ≤ `bar_response_start.beat`,
  dihitung dalam grid section yang sama).
- Not terakhir response **selesai sebelum** frasa call berikutnya
  mulai.

Kalau kedua syarat itu tidak bisa dipenuhi dengan bar/beat yang
sedang ditulis, section itu belum siap untuk call-and-response —
perpendek call, atau perpendek response, jangan biarkan overlap.

## Response = transformasi motif call, bukan melodi baru

Teknik dari `melody.md` ("Development > repetition"): echo
tertransposisi, inversi kontur, fragmentasi, augmentasi ritme.
Contoh klasik: call berkontur **naik** (pertanyaan) → response
berkontur **turun** (jawaban) — kontras kontur itu sendiri yang
membuat response terdengar seperti jawaban, bukan gema.

- **Copy persis** (ritme+kontur+pitch identik, hanya berbeda
  instrument) boleh **maksimal 1 kali** dalam satu rangkaian
  call-response — biasanya siklus pertama, untuk mengenalkan
  pasangan dialog ke pendengar.
- Setelah copy persis yang pertama itu, siklus berikutnya **wajib**
  bertransformasi (salah satu: transpose, invert, fragmentasi,
  augment/diminish ritme) — copy persis berulang adalah anti-pattern
  (lihat tabel di bawah).

## Interaksi dengan negative space

Dialog adalah **cara mengelola ruang**, bukan izin mengisi semua
ruang:

- Total kepadatan call+response dalam satu section tidak boleh
  melebihi kepadatan lead solo yang setara di section sejenis lain —
  dua voice bergantian bukan alasan untuk menggandakan not.
- Gap yang ditinggalkan bersama (tidak diisi call maupun response)
  tetap harus ada di section itu, sesuai prinsip "arc menentukan
  density" — call-and-response mengisi sebagian gap, bukan
  seluruhnya.

## Pemetaan ke `plan.json`

Contoh satu section (4 bar, building phase) dengan dua voice: `melody`
(caller, `role: "lead"`, instrument `rhodes`) dan `response`
(responder, `role: "guitar"`, instrument `acoustic-guitar`). Field
persis (`bar`/`beat`/`pitch`/`dur`/`artic`) — cek `contract.md` untuk
bound valid; **tanpa `vel`, tanpa beat pecahan off-grid** di luar grid
yang diizinkan.

```json
"voices": {
  "melody": {
    "role": "lead", "instrument": "rhodes",
    "notes": [
      {"bar": 1, "beat": 1, "pitch": "D5", "dur": 1, "artic": "legato"},
      {"bar": 1, "beat": 2, "pitch": "F5", "dur": 1, "artic": "legato"},
      {"bar": 1, "beat": 3, "pitch": "A5", "dur": 1, "artic": "accent"}
    ]
  },
  "response": {
    "role": "guitar", "instrument": "acoustic-guitar",
    "notes": [
      {"bar": 1, "beat": 4, "pitch": "A4", "dur": 1, "artic": "staccato"}
    ]
  }
}
```

Di sini call (`melody`) menempati beat 1-3 (berakhir tepat sebelum
beat 4), meninggalkan gap 1 beat di beat 4 — `response` mengisi
persis gap itu dan selesai sebelum bar 2 (call berikutnya) mulai.
Contour call naik (D5→F5→A5); response bisa dilanjutkan siklus
berikutnya dengan kontur turun (mis. bar 2 call naik lagi lalu bar 3
response transpose+invert) untuk memenuhi "response = transformasi,
bukan copy persis berulang". Artic valid: `legato`/`staccato`/
`tenuto`/`accent`/`ghost`.

## Anti-pattern

| Anti-pattern | Kenapa gagal |
|---|---|
| Response menabrak call (overlap bar/beat) | Melanggar aturan emas non-overlap — dialog jadi tumpang tindih, bukan bergantian. |
| Copy persis (ritme+kontur+pitch identik) berulang >1x | Jadi gema mekanis, bukan dialog yang berkembang — lihat "Development > repetition" di `melody.md`. |
| Responder mengisi SEMUA gap di section | Menghapus negative space yang justru jadi alasan dialog itu berguna; section jadi penuh terus-menerus. |
| Dialog call-and-response di tiap section | Arc jadi monoton — bukan setiap section perlu dialog; pilih hanya section yang dilayani arc (building/mid). |
| Responder di register sama dengan lead | Menutupi caller alih-alih menjawabnya — lihat "lane register" di `arrangement.md`. |
| Menulis velocity atau beat off-grid untuk "merasakan" dialog lebih hidup | Itu pelanggaran doktrin niat-bukan-not — feel/humanization adalah kerja `pyengine`, bukan skill ini. |

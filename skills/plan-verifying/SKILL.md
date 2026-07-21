---
name: plan-verifying
description: Run the validate loop on a plan.json (schemaVersion 2) written by jazz-composing — call pyengine's validator, read addressed errors and warnings (e.g. sections[1].voices.melody.notes[3]), fix each at its source, and re-run until it passes. Use whenever a plan.json exists and needs checking before rendering, whenever `python -m pyengine validate` reports errors or warnings, or whenever someone asks to validate, lint, or fix a composition plan. This is the fase Verify of MDLC — it does not invent or change musical intent (that's jazz-composing's job); it only makes an already-decided plan structurally valid and flags craft warnings for jazz-composing to address.
---

# Plan Verifying — fase Verify

Satu-satunya skill yang menjalankan `pyengine validate`. Loop-nya selalu
sama: jalankan → baca **semua** error/warning beralamat → perbaiki di
sumbernya → ulangi sampai `"valid": true` dan tidak ada error tersisa.

Skill ini **tidak menebak niat musikal**. Kalau sebuah error berarti
"field wajib kosong" atau "chord symbol tidak bisa di-parse", perbaikan
yang benar adalah **kembali ke `jazz-composing`** untuk keputusan niat
yang hilang — skill ini tidak boleh mengisi nilai musikal sembarang
hanya supaya validator lolos.

## Dua tingkat penjagaan (dari `docs/new-prd.md` §7.4 di repo `daw_generative`)

- **Error (memblokir)** — struktur, rentang, kontiguitas, referensi,
  chord parse-ability. `plan.json` TIDAK boleh dikirim ke
  `rendering-audition` selama ada error.
- **Warning (tidak memblokir)** — vibe conformance (plan menyimpang dari
  preset vibe: tempo di luar rentang), target tones (melodi di downbeat
  bar baru tidak mendarat di chord tone, khususnya 3rd/7th). Warning
  ditinjau, dipertimbangkan untuk diperbaiki, tapi tidak memblokir lanjut
  ke Audition — dicatat di `verify-log.md` sebagai keputusan sadar kalau
  tidak diperbaiki.

## Workflow

### Step 1 — Jalankan validator

```bash
python -m pyengine validate <path/to/plan.json>
```

Baca **seluruh** stdout JSON — jangan berhenti di error pertama. Format:
`{"valid": bool, "errors": [{"path", "code", "message"}], "warnings": [...]}`.
Exit code 0 = valid (`errors: []`, warning boleh ada), 1 = ada error,
2 = crash internal (payload tetap JSON valid di stdout, `errors: [{"path":
"$", "code": "internal_error", "message": ...}]` — biasanya berarti
`plan.json` bahkan tidak well-formed atau ada bug di pyengine sendiri,
bukan pelanggaran skema biasa).

### Step 2 — Perbaiki tiap error di alamatnya

Baca `references/validation-loop.md` untuk cara membaca `path` beralamat
(mis. `sections[1].voices.melody.notes[3]` = not ke-4 di voice bernama
`melody` di section ke-2) dan memetakannya balik ke keputusan niat yang
perlu diperbaiki. Untuk pola error yang sudah pernah ditemukan dan cara
memperbaikinya, baca `references/common-errors.md` sebelum menebak sendiri.

Jangan perbaiki gejala tanpa memperbaiki sumber: error "chord symbol tidak
valid" berarti kembali ke keputusan harmoni di `jazz-composing`, bukan
mengganti ke simbol acak yang kebetulan valid secara skema.

### Step 3 — Tinjau warning

Untuk tiap warning: putuskan perbaiki (kembali ke `jazz-composing` untuk
menyesuaikan niat) atau terima sadar (dengan alasan tertulis — vibe yang
sengaja menyimpang preset, misalnya). Warning yang diterima tanpa alasan
tertulis dianggap belum ditinjau, bukan "aman".

### Step 3b — Audit interplay (manual, hanya bila ada dialog)

**Trigger**: jalankan hanya kalau plan.json memuat ≥2 voice pembawa
`notes[]` melodis yang ditandai sebagai pasangan call-and-response —
oleh run folder (interaction map/artefak ideation) atau penamaan voice
(mis. `response`/`answer`). Tidak ada dialog → lewati step ini tanpa
catatan.

Cek mekanis (bukan penilaian musikal), pakai definisi aturan emas
non-overlap di `../jazz-composing/references/call-and-response.md`
(jangan duplikasi definisinya di sini): untuk tiap pasangan call/response,
hitung interval `[start, start+dur)` tiap not pada sumbu bar+beat dari
field grid. Pelanggaran = ada interval not response yang **beririsan**
dengan interval not call (menyentuh batas tepat = bukan pelanggaran).
Cek kedua: masih ada gap di section dialog yang tidak diisi voice manapun
(responder tidak boleh mengisi semua gap). Boleh dibantu python ad-hoc
(baca JSON, bandingkan interval) untuk hitungan ini — jangan tambahkan
file script permanen ke repo.

Pelanggaran setara WARNING wajib ditinjau (validator pyengine tidak
menegakkan aturan ini): perbaikan = kembali ke `jazz-composing` untuk
menggeser niat frasa (skill ini tidak menggeser not sendiri), atau
diterima sadar dengan alasan tertulis di `verify-log.md` (mis. overlap
1 not disengaja sebagai handoff).

### Step 4 — Ulangi sampai bersih

Jalankan ulang Step 1 setelah tiap perbaikan. Berhenti hanya saat
`"valid": true` DAN tidak ada error tersisa (warning boleh tersisa kalau
sudah ditinjau di Step 3).

### Step 5 — Tulis verify-log.md dan serahkan

Tulis `verify-log.md` ke run folder: jumlah iterasi, error yang
ditemukan+diperbaiki (before/after ringkas), warning yang diterima +
alasannya, dan hasil audit interplay Step 3b (dilewati / bersih /
pelanggaran+resolusi). Serahkan `plan.json` yang sudah bersih ke
`../rendering-audition/SKILL.md` untuk fase Audition.

## Metrik yang relevan (dari `docs/new-prd.md` §8 di repo `daw_generative`)

- Validitas plan iterasi pertama ≥ 80% — kalau jauh di bawah ini secara
  konsisten, itu sinyal `jazz-composing` perlu memperbaiki
  `contract.md`/knowledge base-nya, bukan `plan-verifying` menambah
  toleransi.
- Validitas setelah ≤ 2 iterasi feedback ≥ 95%.

## References

- `references/validation-loop.md` — cara membaca path beralamat, memetakan
  balik ke sumber keputusan niat.
- `references/common-errors.md` — pola error/warning yang sudah ditemukan
  + perbaikannya (tumbuh dari pengalaman nyata, bukan spekulasi).
- `../RED-FLAGS.md` — pola kegagalan umum lintas skill.

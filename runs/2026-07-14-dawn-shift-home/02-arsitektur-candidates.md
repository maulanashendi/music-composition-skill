# 02 — Arsitektur — Kandidat & Seleksi (Level 2)

## Objective

Menentukan bentuk performa 24 bar yang merealisasikan arc "Home by Dawn"
(lihat `01-brief.md`): tenang-sendiri → berkembang → momentum menumpuk →
satu momen paling berarti → konvergensi (graft) → resolusi tenang.

## Immutable constraints

- 24 bar total (dikunci di `01-brief.md`).
- Instrumen masuk bertahap: bass sendirian dulu, lalu Rhodes, lalu drum,
  lalu lead — urutan ini bagian dari konsep pemenang Level 1, tidak boleh
  diubah di level ini.
- Graft dari Level 1: konvergensi unison bass+lead harus muncul sebagai
  gema/penutup, bukan puncak kedua yang bersaing dengan entri lead.

## Assumptions

- "Section" di bawah adalah unit dramaturgis (fungsi + instrumentasi),
  bukan AABA/blues form tradisional — form ini through-composed by nature
  karena konsepnya accretive, jadi pertanyaannya bukan "AABA vs blues" tapi
  "linear murni vs ada elemen return/bookend".

## Kandidat

### Kandidat 1 — "Linear Accretion" (through-composed murni, tanpa return)

Intent: setiap blok menambah satu lapisan baru dan tidak pernah kembali ke
tekstur sebelumnya — garis waktu murni maju, paling literal terhadap
"momentum menumpuk".

| Section | Bar | Isi |
|---|---|---|
| 1 — Alone | 1-4 | Bass solo (walking/pedal hybrid), D Dorian |
| 2 — Comping in | 5-8 | + Rhodes (comping sparse) |
| 3 — Steps gather | 9-14 (6 bar) | + Drum (hi-hat/rimshot saja, membangun) |
| 4 — Light arrives | 15-20 (6 bar) | + Lead (flugelhorn), lompatan interval lebar; mode mulai brighten ke Mixolydian/mayor-ish |
| 5 — Arrival | 21-24 (4 bar) | Full quartet, konvergensi unison bass+lead, resolusi — TANPA tekstur menipis kembali ke solo |

Risiko statis/simetris: **rendah untuk simetri** (tidak ada yang diulang
sama sekali), tapi risiko lain — bentuk yang murni linear tidak pernah
membangun "rumah" untuk ditinggalkan lalu dikembalikan; momen arrival di
akhir bisa terasa seperti puncak baru yang tiba-tiba penuh, bukan "sampai"
yang terasa sebagai penutup alami dari perjalanan section 1.

### Kandidat 2 — "Frame Return" (bookend, ada elemen return eksplisit)

Intent: setelah lead masuk dan momen puncaknya lewat, Rhodes dan drum
menipis (subtractive) sehingga tekstur balik mendekati section 1 (bass +
sedikit lead) sebelum konvergensi unison — "sampai" dibingkai sebagai
kembali ke kesendirian awal, tapi kali ini ditemani.

| Section | Bar | Isi |
|---|---|---|
| 1 — Alone | 1-4 | Bass solo, D Dorian |
| 2 — Comping in | 5-8 | + Rhodes |
| 3 — Steps gather | 9-12 (4 bar) | + Drum |
| 4 — Light arrives | 13-18 (6 bar) | + Lead, lompatan interval lebar; brighten dimulai |
| 5 — Thinning/Return | 19-22 (4 bar) | Rhodes & drum menipis (subtractive) — tekstur kembali dekat section 1, tapi kini + lead & harmoni yang sudah brighten = return terekontekstualisasi |
| 6 — Arrival | 23-24 (2 bar) | Konvergensi unison bass+lead, resolusi |

Risiko statis/simetris: **risiko simetri lebih tinggi** — bentuk naik-lalu-
turun bisa dibaca sebagai "rise and fall" konvensional, bertentangan dengan
instruksi brief "bukan klimaks besar". Juga risiko eksekusi: kalau
penipisan section 5 terjadi terlalu cepat/tiba-tiba setelah momen lead di
section 4, bisa terdengar seperti "kehilangan energi" alih-alih
"menetap/settled".

## Selected + alasan

**Kandidat 2 — "Frame Return".**

Constraint Level 1 eksplisit: konvergensi unison bass+lead harus jadi
gema/penutup, bukan puncak kedua yang bersaing dengan entri lead. Kandidat 1
melompat dari klimaks lead (section 4) langsung ke "full quartet" tanpa
penipisan apa pun di section 5 — secara struktural nyaris pasti terdengar
sebagai puncak kedua berdensitas penuh, persis yang dilarang graft tersebut
(risiko ini bahkan diakui sendiri di deskripsi Kandidat 1). Kandidat 2
menaruh proses subtractive (bar 19-22) *sebelum* konvergensi, sehingga saat
unison terjadi densitas sudah turun mendekati section 1 — unison otomatis
terdengar sebagai gema yang menetap karena tidak ada lagi "ruang naik" untuk
berkompetisi dengan momen lead. "Satu momen paling berarti" pada kedua
kandidat sama-sama jatuh di entri lead (section 4), tapi hanya Kandidat 2
yang memberi momen itu ruang berdiri sendiri sebagai puncak tunggal, karena
sesudahnya tekstur ditenangkan dulu, bukan langsung disusul blok
sama-penuh. Risiko "rise and fall konvensional" yang disebut sendiri oleh
Kandidat 2 valid secara genre-purist, tapi brief minta "bukan klimaks
besar", bukan "tanpa bentuk apapun" — naik-turun terkendali justru
mekanisme paling langsung untuk mencegah puncak kedua.

**Graft dari Kandidat 1:** ambil prinsip "jangan hapus total lapisan yang
sudah dibangun" — saat penipisan section 5, jangan drop Rhodes & drum
sampai nol/kembali sepenuhnya identik ke tekstur section 1; sisakan jejak
tipis (mis. sustain pad Rhodes atau ghost hi-hat) supaya "return" terasa
sebagai rekontekstualisasi bermuatan momentum, bukan kehilangan energi
mendadak — ini langsung menjawab risiko eksekusi yang diakui sendiri oleh
Kandidat 2.

## Exact artifact

`02-form.md` memakai pemenang seleksi di atas.

## Unresolved/confidence

**Confidence: tinggi** — constraint eksplisit dari Level 1 (graft harus
gema, bukan puncak kedua) menghakimi struktur secara langsung, bukan soal
selera prosa.

Risiko yang masih terbuka pada pemenang:

- Pacing eksekusi penipisan section 5 (4 bar) — kalau terlalu cepat/mekanis
  bisa terdengar seperti "kehilangan energi" alih-alih "menetap", persis
  risiko yang sudah diakui sendiri di deskripsi Kandidat 2; butuh kurva
  dinamik/velocity halus, bukan cut tiba-tiba.
- Section "Arrival" hanya 2 bar untuk convergence + resolusi — berisiko
  terasa terburu-buru untuk "resolusi tenang"; kemungkinan butuh 1 bar
  tambahan diambil dari section 5, tapi itu keputusan level arrangement
  detail (Level 3+), bukan bagian dari seleksi bentuk di level ini.
- Belum diverifikasi telinga langsung (belum ada rendering audio) — pilihan
  ini murni dari deskripsi prosa di kandidat; uji telinga sebenarnya baru
  bisa dilakukan begitu ABC/arrangement konkret sudah ditulis.

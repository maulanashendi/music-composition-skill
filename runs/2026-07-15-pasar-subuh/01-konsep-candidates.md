# Level 1 — Konsep Artistik: kandidat & seleksi

## Objective
Musik instrumental neo-soul/chill-jazz kuartet yang menangkap pasar subuh: dari sunyi-gelap, lampu-lampu warung menyala satu-satu, kota bangun bertahap, menuju hangat-hidup — tanpa klimaks besar, tapi ada satu micro-apex yang paling berarti.

## Immutable constraints (dari brief)
- Genre: neo-soul/chill-jazz instrumental.
- Arc: sepi-gelap → aktivitas tumbuh bertahap → hangat-hidup, TANPA klimaks besar, TAPI ada 1 micro-apex.
- Panjang: 20-28 bar.
- Kuartet (4 suara/track).
- Instrumentasi & lead/rhythm section bebas dipilih via protokol kandidat (tidak boleh tanya balik — asumsi dicatat di sini).

## Assumptions
- "Kuartet" dibaca sebagai 1 lead melodi + 3 rhythm section (bukan 4 melodi paralel) — konvensi standar combo jazz kecil yang dipakai contoh SOP (`level-01-konsep.md`).
- Tempo & key belum ditentukan brief — akan dikunci di kandidat sesuai karakter "tenang, penuh harapan kecil, hangat".
- Instrumentasi WAJIB dari registry engine (`engine-export.md`) — kedua kandidat di bawah memakai kombinasi terdaftar, tanpa GM di luar tabel, jadi tidak perlu justifikasi tambahan.

## Kandidat

### Kandidat A — "Ostinato yang menyalakan diri" (through-composed, lead = Tenor Sax)
Intent (≤1 kalimat): Satu figur bass ostinato dua-nada yang mulai sebagai denyut sunyi di gelap, lapis instrumen menyala satu-satu di atasnya, dan di bar terakhir figur yang sama terdengar hangat karena harmoni di atasnya sudah berubah (rekontekstualisasi).
- Instrumentasi: Tenor Sax (lead, `sax`/GM66), Rhodes E-Piano (`rhodes`/GM4), Finger Bass (`bass-finger`/GM33), jazz-kit (drum). Palet dekat `neo-soul-warm` (rhodes+bass-finger), guitar diganti sax sebagai lead melodi.
- Key/mode: D Dorian (minor dengan warna hangat dari nada ke-6 mayor — cocok "gelap tapi penuh harapan").
- Tempo: ~76 BPM (downtempo, ruang bernapas, konsisten "tenang").
- Struktur: through-composed pendek 24 bar, bukan AABA — cocok arc satu-arah yang tumbuh, tanpa restatement identik.
- Aesthetic thesis: "Satu figur bass dua-nada yang mula-mula terasa seperti detak jam sunyi di gelap; setiap kali kembali, satu instrumen baru menyalakan diri di atasnya, sampai figur yang sama, di harmoni baru, terdengar seperti rumah."

### Kandidat B — "Panggilan-sahutan pedagang" (call-response, lead = Clean Electric Guitar)
Intent (≤1 kalimat): Dua motif pendek saling menyahut seperti dua pedagang memanggil dari kios berbeda; makin lama makin banyak "suara" yang menyahut sampai seluruh pasar terdengar bicara bersama.
- Instrumentasi: Clean Electric Guitar (lead, `guitar-clean`/GM27), Rhodes E-Piano (`rhodes`/GM4, sebagai "suara kedua" call-response), Finger Bass (`bass-finger`/GM33), jazz-kit (drum).
- Key/mode: F major dengan tonicization minor sesaat (lebih terang dari Kandidat A sejak awal).
- Tempo: ~82 BPM.
- Struktur: ABAC pendek 24 bar — A memperkenalkan panggilan gitar, B menambah sahutan rhodes, A' menumpuk keduanya, C coda hangat.
- Aesthetic thesis: "Dua frasa pendek yang mula-mula bicara bergantian dalam sunyi, lalu tumpang tindih semakin rapat sampai keduanya terdengar seperti obrolan pasar yang hidup."

## Selected + alasan

**Dipilih: Kandidat A — "Ostinato yang menyalakan diri"** (verdict selector segar, subagent independen tanpa histori generasi):

> The brief's most concrete image — "satu-satu lampu warung menyala" — is a layer-by-layer ignition over something that stays constant while the world around it grows. Candidate A's mechanism *is* that image: a fixed two-note bass figure that a listener's ear will track through the whole piece, with each repetition getting one more voice on top. That gives the arc structural discipline — the "micro-apex, not a big climax" the brief asks for lands naturally in the final bar, where the *same* figure suddenly reads as warm because the harmony underneath it has shifted (recontextualization, not new material). That's a payoff the ear registers as "oh, this was home all along" rather than a volume/density crescendo — which is exactly the restrained, hangat-not-euphoric target.
>
> Candidate B is a fine concept but its growth mechanism — more voices trading and overlapping until "the whole market is talking" — is additive-density shaped almost by definition. That's a natural fit for a big cumulative climax, and the brief explicitly asks to avoid one. It also risks two co-equal lead-ish voices (guitar + rhodes) diffusing the sense of a single through-line the listener can hold onto over only 20-28 bars, and "obrolan pasar yang hidup" skews more animated/social than "tenang, penuh harapan kecil."
>
> **Graft:** borrow B's call-response texture as a *local* event inside A, not as the structural spine — when the 2nd/3rd layer ignites (section before the micro-apex), let sax and Rhodes trade a short 1-2 bar call-response phrase before settling back into the ostinato-driven texture.

## Exact artifact
Pemenang (Kandidat A + graft call-response lokal dari B) dituliskan ke `01-brief.md`.

## Unresolved/confidence
- Panjang pasti (20-28 bar) akan dikunci di Level 2 sesuai kebutuhan arc bertahap — kandidat ini mengasumsikan 24 bar sebagai titik tengah rentang brief.
- Confidence seleksi: tinggi — kedua kandidat berbeda struktural secara jelas (through-composed satu-arah vs. call-response dua-kekuatan), dan pilihan selaras langsung dengan kata-kata eksplisit brief ("bertahap", "satu micro-apex", "tenang").

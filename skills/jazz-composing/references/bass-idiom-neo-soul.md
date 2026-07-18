# Idiom bassline neo-soul — niat konkret

Ditulis setelah uji A/B lagu nyata menunjukkan bass yang dihasilkan
tanpa konteks ini jadi tangga arpeggio 1-3-5-7 naik lurus per beat,
identik bar demi bar, dan register melayang terlalu tinggi
(`upright-bass` jatuh di C4-Bb4 alih-alih register wajarnya). Ini
bukan aturan teori generik — ini niat *bagaimana* bass neo-soul
biasa bergerak, dipetakan ke field `plan.json` yang sudah didukung
`pyengine` (lihat `contract.md`).

Semua poin di bawah tetap niat-level: yang ditulis adalah `degree`/
`pitch`/`beat`/`octave`/`artic` per not, bukan micro-timing atau
velocity numerik — realisasi humanization tetap kerja `pyengine`.

## Anchor di beat 1

Root (`degree: 1`) di beat 1 tiap bar adalah jangkar default — tempat
paling aman untuk telinga menempatkan downbeat. Anchor tak harus
dipertahankan tiap bar (lihat "variasi antar bar"), tapi kalau
groove/harmoni ambigu, kembalikan ke anchor beat 1.

## Sinkopasi & push ke beat 4.5

Sinkopasi bukan hiasan opsional — ini yang membedakan bassline hidup
dari tangga metronomik. Pola yang sering dipakai: not pendek
(`dur < 1` beat) di `beat: 4.5` yang "mencuri start" menuju chord/bar
berikutnya (lihat `contract.md` §Beat desimal & pickup). Jangan taruh
not di setiap beat penuh (1, 2, 3, 4) tanpa variasi — itu ciri
bassline mekanis, bukan groove.

## Ghost note sebagai ornamen, bukan default

`artic: ghost` (velocity multiplier 0.5, lihat `contract.md`) dipakai
sebagai bumbu — mengisi ruang antar not utama, bukan menggantikan not
utama. Hemat pemakaiannya di section ber-`dynamics` rendah (intro/
outro pelan): ghost + pickup yang ditumpuk pada dynamics rendah bisa
membuat not itu tenggelam di bawah ambang berguna sampel (lihat
`contract.md` §Artikulasi bass).

## Octave-pop

Lompatan oktaf sesaat (mis. root oktaf 2 → oktaf 3 lalu kembali) di
akhir frasa atau transisi section menambah energi tanpa mengubah
harmoni. Tulis lewat `pitch` eksplisit (bukan `degree`, karena
`degree` tidak membawa oktaf) atau kombinasi `degree` + `octave`
berbeda dari not sekitarnya.

## Approach kromatik via `pitch`

Not setengah/satu langkah kromatik menuju root chord berikutnya
adalah idiom umum jazz/neo-soul bass — ini BUKAN chord-tone, jadi
harus ditulis via field `pitch` eksplisit (mis. `"F#2"`), bukan
dipaksakan ke `degree` terdekat (lihat `contract.md` §Field `pitch`
vs `degree`).

## Variasi antar bar (wajib)

Pola bar identik berturut-turut lebih dari 2x adalah tanda gagal —
sekalipun tiap bar individual "benar" secara teori. Variasikan
minimal salah satu dari: pilihan chord-tone (`degree`), penempatan
sinkopasi, kepadatan not, atau ada/tidaknya approach tone, setiap
2 bar.

## Register — `octave` wajib

`octave` wajib secara konvensi — validator TIDAK menegakkan ini; tanpa
`octave` eksplisit, oktaf default engine bisa mendarat terlalu
tinggi untuk instrumen bass (lihat `contract.md` §Register & oktaf —
tabel rentang per instrumen). Untuk `upright-bass`: root nyaman di
oktaf **2**, sesekali oktaf **3** untuk not tinggi/approach
tone/octave-pop. Selalu cek rentang instrumen yang dipakai di
`contract.md` sebelum menulis `octave`.

## Space/rest adalah bagian dari pocket

Bass tidak wajib mengisi tiap beat. Rest yang disengaja (tidak
menulis not di beat tertentu) memberi ruang bagi drum/comping dan
adalah bagian dari pocket, bukan kekosongan yang perlu ditambal.

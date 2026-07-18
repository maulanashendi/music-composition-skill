# Harmony — peta harmoni jazz (niat-level)

> Diringkas dari `../../harmony/SKILL.md` (konsolidasi sebelum
> restrukturisasi MDLC). Semua isi di sini beroperasi di level **simbol
> chord** — tonal center, harmonic rhythm, fungsi harmonik, tension map,
> teknik reharmonisasi — jadi tetap niat-level, bukan not. Dipakai di
> Fase Ideation poin 3 (Peta Harmoni) dari `../SKILL.md`.

## Kapan dipakai

Dipanggil dari `jazz-composing` Fase Ideation poin 3 — menentukan tonal
center, harmonic rhythm, fungsi harmonik tiap chord, dan tension map per
bar. Kalau salah satu field ini belum ditentukan di brief (tonal center,
harmonic rhythm, fungsi tiap bar) — **tanya, jangan menebak.**

## Langkah 1 — Tentukan tonal center

Contoh: `C major`, `D minor`, `F Dorian`, `G Mixolydian`, atau multi-tonal.

## Langkah 2 — Tentukan harmonic rhythm

Harmonic rhythm adalah seberapa sering chord berubah — 1 chord per bar,
2 chord per bar, 1 chord setiap 2 bar, atau kombinasi. Harmonic rhythm
lambat memberi ruang modal; harmonic rhythm cepat memberi kesan bebop
atau functional jazz.

### Durasi absolut per chord — cek terhadap BPM (wajib)

Rumuskan harmonic rhythm sebagai **durasi absolut**, bukan hanya "N chord
per bar":

```
durasi per chord (detik) = bars_per_chord × beats_per_bar × 60 / BPM
```

Target: minimal **±2 detik per chord** agar perubahan harmoni "teraba"
pendengar. Konsekuensi rumus ini (bukan aturan tempo-vs-jumlah-chord yang
berdiri sendiri): pada BPM rendah satu bar berdurasi lebih panjang secara
absolut, sehingga 2 chord/bar tetap bisa aman asal masih ≥2 detik per
chord; pada BPM tinggi 2 chord/bar lebih berisiko karena tiap chord
kebagian waktu absolut yang pendek.

## Langkah 3 — Buat harmonic skeleton

Contoh delapan bar (baru kerangka fungsi):

```
| Dm7 | G7 | Cmaj7 | Cmaj7 |
| Em7 | A7 | Dm7   | G7    |
```

## Langkah 4 — Tentukan fungsi harmonik

Tonic, Predominant, Dominant, Resolution, Temporary tonicization, Modal
area, Chromatic departure. Contoh: `Dm7 = predominant`, `G7 = dominant`,
`Cmaj7 = tonic`, `A7 = secondary dominant`.

## Langkah 5 — Tambahkan warna

Kerangka sederhana `Dm7 – G7 – Cmaj7` dapat dikembangkan menjadi
`Dm9 – G13b9 – Cmaj9`, atau `Dm11 – Db13 – Cmaj9`.

## Langkah 6 — Buat tension map

Tandai tingkat tegangan setiap bar, mis.: bar 1 stabil, bar 2 mulai
bergerak, bar 3 stabil, bar 4 terbuka, bar 5 meningkat, bar 6 tinggi,
bar 7 dominan kuat, bar 8 resolusi. Tension map inilah yang dipakai
`../references/advanced-melody.md` untuk memutuskan bar mana boleh
outside.

## Teknik harmonik

- ii–V–I
- secondary dominant
- tritone substitution
- backdoor dominant
- modal interchange
- diminished passing chord
- chromatic mediant
- pedal point
- constant structure
- slash chord
- polychord
- reharmonization
- side-slipping harmony

## Vocabulary kerja

Ringkasan kerja chord quality, chord-progression logic, dan
voice-leading feel:

**Scales dan chord quality** — kualitas inti dan warna/fungsi
defaultnya:

- **maj7 / 6 / 6/9** — stabil, resting (tonic).
- **m7 / m6 / m9** — stabil minor atau supertonic; m6 dan m(maj7)
  condong ke tonic-minor.
- **dom7 (7, 9, 13, alt)** — tidak stabil, ingin resolve turun perfect
  fifth; `alt` (b9#9b13) memaksimalkan tension.
- **m7b5 (half-dim)** — pre-dominant di minor (ii dari minor ii-V-i).
- **dim7** — passing/leading, simetris, menghubungkan chord diatonis
  secara kromatik.

Pasangan scale-chord yang benar-benar dipakai: major/Ionian di atas
maj7, Dorian di atas m7 (warna minor default jazz), Mixolydian di atas
dom7, Lydian di atas maj7#11, altered/diminished di atas dom7alt,
minor-pentatonic/blues di atas hampir semua chord untuk lead yang
rootsy.

Modal writing: pilih satu mode dan *bertahan*, warnai dengan
characteristic note-nya (natural 6 di Dorian, b2 di Phrygian, #4 di
Lydian). Groove modal hidup di satu atau dua chord — gerakan datang
dari bass dan melodi, bukan pergantian chord.

**Chord progression logic**:

- **Functional motion** = tension→resolution via descending fifths
  (ii-V-I, dan bentuk minornya ii(m7b5)-V(alt)-i). Pakai saat butuh
  dorongan ke depan dan arrival yang jelas. Jangan pakai ii-V-I secara
  refleks — hanya saat motion terarah memang melayani mood.
- **Loop-based / static harmony** = sel pendek (biasanya 2 atau 4
  chord) yang berulang; identitas datang dari groove dan melodi. Ini
  tulang punggung lofi/jazzhop. Loop 4-chord yang kuat biasanya
  mencampur satu tonic stabil, satu color chord (maj7 naik minor
  third, atau bIII/bVI), dan satu tension chord ringan.
- **Modal interchange / borrowed chords** (bVImaj7, bVIImaj7, iv, bII)
  menambah kehangatan dan kejutan tanpa keluar dari key center.
- **Harmonic rhythm** = seberapa cepat chord berubah. Lambat (satu
  chord per bar atau lebih lambat) = lapang, groove-forward, lofi.
  Cepat (dua+ per bar) = bebop, sibuk, forward-driving. Memilih
  harmonic rhythm sering jadi keputusan identitas yang lebih besar
  daripada memilih chord itu sendiri.

Contoh loop minor (C minor, lofi): `Cm9 | Abmaj7 | Fm9 | G7alt` —
tonic, warna bVI yang hangat, subdominant minor, tension kembali ke i.
Terasa laid-back karena harmonic rhythm satu chord per bar dan tension
chord resolve dengan lembut.

**Harmony dan voice-leading feel** — di tahap ide belum menulis
voicing persis (itu bukan lagi tanggung jawab knowledge base ini,
lihat bagian di bawah), tapi tentukan *tekstur*-nya lewat field gaya
comping (`../SKILL.md` Fase Ideation poin 6): rootless comping terbaca
modern/jazzy; open/triad terbaca bersih/pop-jazz; quartal/stacked-4th
terbaca modal dan cool. Prinsip voice-leading yang perlu diingat:
common tone ditahan, voice lain bergerak stepwise, memberi perubahan
yang halus; lompatan paralel besar terbaca berani atau naif tergantung
intent — ini konteks buat memilih gaya comping, bukan resep pitch.

## Yang TIDAK ditulis di sini (sudah pindah ke `pyengine`)

Voicing pitch konkret dan voice-leading not-by-not (dulu di
`archive/skills/harmony/references/voicing-systems.md`) bukan lagi
tanggung jawab knowledge base ini — lihat
`../../../docs/DOCTRINE-NIAT-BUKAN-NOT.md`. Yang ditulis ke `plan.json`
untuk setiap chord hanya **simbol chord** (`Fmaj9`, `Dm7b5`, `C7#9`, …)
dan, bila plan menuntut gaya comping tertentu, field gaya+density (lihat
`contract.md` untuk field pastinya) — bukan daftar pitch voicing.
`voicing-systems.md` diarsipkan di
`archive/skills/harmony/references/voicing-systems.md` untuk rujukan
historis, bukan dihapus.

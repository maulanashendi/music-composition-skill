# Melody — motif, kontur, target tone, broken chord (niat-level)

> Setiap contoh melodi di file ini ditulis sebagai **pitch + durasi per
> not saja**. Jangan menambahkan velocity atau posisi off-grid pada
> contoh baru yang kamu tulis mengikuti pola file ini — itu kerja
> `pyengine`, lihat `../../../docs/DOCTRINE-NIAT-BUKAN-NOT.md`.

Diringkas dari `../../melody-design/references/melody-fundamentals.md`
(vocabulary kerja murni melodi — phrasing, motif/hook, guide tones).
Dipakai di Fase Ideation poin 4 (Desain Melodi) dari `../SKILL.md`,
tahap 1-6 (motif/kontur/target-tone/broken-chord). Untuk chromatic
vocabulary/outside playing (tahap 7-8), lihat
`references/advanced-melody.md` — jangan campur di sini.

## Phrasing (interval, kontur, timing)

**Phrasing** is *how the melody is played*, not just which notes — it's
where feeling lives. Decide per section:

- **long vs. short notes** — long notes = weight, stillness; short =
  urgency, playfulness;
- **gaps between phrases** — long gaps = hesitation, space to breathe;
  short gaps = momentum;
- **rising vs. falling contour** — rising = hope/lift; falling =
  settling/release;
- **the peak note** — the single highest, most-exposed note; place it
  at the emotional climax and consider holding it;
- **motif repetition** — repeating a figure (same, or transposed up as
  a sequence) builds recognition and momentum;
- **notes held before resolution** — landing on an unresolved tone and
  holding creates yearning;
- **on the beat vs. slightly behind** — on-beat = confident, tight;
  behind = relaxed, laid-back, aching.

Catatan: "on-beat vs. slightly behind" di sini adalah *niat ekspresif*
yang dipetakan ke pilihan groove/pattern bernama (Fase Ideation poin 5,
lihat `references/groove-vocabulary.md`) — bukan tick offset numerik
yang ditulis langsung ke `plan.json`. Tension-release sebagai
dramaturgi lintas-section (dominant held, bass contrary motion,
instrumen ditambah, dsb.) dibahas di
`../../arrangement/references/form-and-dramaturgy.md` §11a — di sini
fokusnya murni pada bagaimana melodi diucapkan (interval, kontur,
timing).

## Melody, motif, and hook

- **Motif** = a short, memorable rhythmic+intervallic cell. Define it
  by its rhythm, its interval shape (contour), and its target notes —
  *before* filling bars.
- **Hook** = the phrase a listener remembers in the first few seconds.
  In instrumentals it's carried by the lead's rhythm and contour, not
  lyrics. Give it a fragment form, a complete form, and a transformed
  return.
- **Development** > repetition. Transform the motif (transpose, invert,
  augment/diminish rhythm, reharmonize under it) and assign each
  transformation a role (statement, build, climax, resolution).
  Preserve space — don't turn every repeat into a new tune.
  Transformasi motif juga rumah bagi *response* dalam dialog
  antar-instrumen — lihat `call-and-response.md`.
- **Guide tones** (3rds and 7ths of each chord) are the melody's
  landing points; targeting them makes a line "sing" the changes
  without spelling every note.

## Dari niat ke `plan.json`

Saat menulis Fase Plan, tiap not melodi (`voices.melody.notes[]`)
membawa `bar`, `beat` (di grid), `pitch`, `dur`, dan `artic` — lihat
`contract.md` untuk field pastinya. `artic` (mis. `legato`, `accent`,
`tenuto`, `ghost`) tetap niat-level (bagian dari representasi
selengkap-sheet, lihat CLAUDE.md proyek induk `daw_generative`) dan
boleh ditulis; yang **tidak** boleh ditulis adalah `vel`/velocity
numerik atau `beat` pecahan off-grid — itu milik `pyengine`.

# Template registry — Tier 0 index

The thin index the orchestrator reads **first**, at Level 1 (konsep). Match the
brief's vibe to a row, then load only that template's `<id>.json` (Tier 1). If
no row is a good fit, compose without a template and say so — a forced match is
worse than none.

Keep each row to one line: `id` · style · when-to-use. The `when-to-use` text
must match the `when_to_use` field inside the template file.

| id | style | when to use |
|---|---|---|
| `neo-soul-midnight` | neo-soul | late-night neo-soul where guarded phrases slowly become honest, 68-80 BPM, Rhodes-led with elastic pocket and intimate call-and-response |
| `lofi-jazzhop` | lofi jazz / jazzhop | dusty loop-based jazzhop where familiar material reveals a new shade on each return, 75-95 BPM, Rhodes and grounded bass with late-arriving lead |
| `fusion-vamp` | jazz-funk / fusion | riff-driven jazz-funk or fusion where pressure accumulates through layering and releases through a decisive breakdown-and-return, 96-124 BPM |
| `classic-jazz-swing` | classic jazz / swing big band | big-band swing built like a public celebration: a clear head, conversational sections, one exposed solo break, and a shout chorus that earns its arrival, 115-180 BPM |
| `bossa-nova-classic` | bossa nova | intimate bossa nova where a calm surface carries quiet saudade, nylon-guitar batida and straight 16ths supporting a voice that never needs to raise itself, 80-160 BPM |
| `soul-jazz-organ-blues` | soul jazz | Hammond B-3 soul jazz where a communal gospel-blues groove grows from a low simmer into an organ-led testimony, 90-115 BPM |
| `hiphop-jazz-boombap` | hip-hop jazz / jazz rap | golden-era jazz rap where a chopped Rhodes loop feels archival but the drum pocket and muted-horn replies keep rewriting its present meaning, 84-88 BPM |
| `smooth-jazz-radio` | smooth jazz | radio-friendly smooth jazz where polished restraint makes one vocal-like lead melody feel inevitable, with clear verse-to-chorus lift and consonant R&B harmony, 82-98 BPM |
| `noir-jazz-scene` | cinematic noir jazz / dark-jazz scene score | cinematic noir jazz where silence, decay, and one mournful call carry more narrative weight than harmonic motion, muted trumpet over dark piano, 42-50 BPM |
| `cool-modal-quintet` | cool modal jazz | cool or modal jazz where a small motif gains meaning through silence, patient modal color, and restrained horn conversation rather than chord traffic, 100-125 BPM |

<!--
Adding a template? Append one row above AND create templates/<id>.json per
schema.md. Do not inline groove numbers or chord theory here — the row is an
index entry, the recipe lives in the file. See README.md § Governance.
-->

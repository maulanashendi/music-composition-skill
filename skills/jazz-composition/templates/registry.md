# Template registry — Tier 0 index

The thin index the orchestrator reads **first**, at Level 1 (konsep). Match the
brief's vibe to a row, then load only that template's `<id>.json` (Tier 1). If
no row is a good fit, compose without a template and say so — a forced match is
worse than none.

Keep each row to one line: `id` · style · when-to-use. The `when-to-use` text
must match the `when_to_use` field inside the template file.

| id | style | when to use |
|---|---|---|
| `neo-soul-midnight` | neo-soul | late-night, intimate, a doubt->acceptance arc, 68-80 BPM, Rhodes-led |
| `lofi-jazzhop` | lofi jazz / jazzhop | loop-based, dusty and warm, developed by subtraction/addition, 75-95 BPM, Rhodes+fat bass pocket |
| `fusion-vamp` | jazz-funk / fusion | riff-driven jazz-funk/fusion vamp, tight backbeat, builds and breakdowns, urgency->release arc, 96-124 BPM |
| `classic-jazz-swing` | classic jazz / swing big band | big band swing, dancehall energy, head->soli->solo break->shout chorus arc, 115-180 BPM |
| `bossa-nova-classic` | bossa nova | nylon guitar batida, straight 16ths (no swing) with a laid-back lead, saudade-leaning AABA arc, 80-160 BPM |
| `soul-jazz-organ-blues` | soul jazz | Hammond B-3 organ trio/quintet, gospel-blues 12-bar, organ solo with a Leslie/drawbar dynamic arc, 65-145 BPM |
| `hiphop-jazz-boombap` | hip-hop jazz / jazz rap | golden-era boom-bap / jazz rap, sample-chopped Rhodes loop, Dilla push-pull timing, muted horn hook, 75-95 BPM |
| `smooth-jazz-radio` | smooth jazz | radio-friendly smooth jazz, vocal-centric sax/guitar lead, smooth slash chord, full pop-verse-chorus form, 65-115 BPM |
| `noir-jazz-scene` | noir jazz / dark jazz | cinematic noir/dark jazz, muted trumpet over dark piano, extreme rubato drag, ppp-pp dynamics, scene-form arc, 35-65 BPM |

<!--
Adding a template? Append one row above AND create templates/<id>.json per
schema.md. Do not inline groove numbers or chord theory here — the row is an
index entry, the recipe lives in the file. See README.md § Governance.
-->

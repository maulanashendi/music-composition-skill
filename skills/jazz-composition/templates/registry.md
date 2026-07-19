# Template registry — Tier 0 index

The thin index the orchestrator reads **first**, at Level 1 (konsep). Match the
brief's vibe to a row, then load only that template's `<id>.json` (Tier 1). If
no row is a good fit, compose without a template and say so — a forced match is
worse than none.

Keep each row to one line: `id` · style · when-to-use. The `when-to-use` text
must match the `when_to_use` field inside the template file.

| id | style | when to use |
|---|---|---|
| `neo-soul-midnight` | neo-soul | late-night, intimate, a doubt→acceptance arc, 68–80 BPM, Rhodes-led |

<!--
Adding a template? Append one row above AND create templates/<id>.json per
schema.md. Do not inline groove numbers or chord theory here — the row is an
index entry, the recipe lives in the file. See README.md § Governance.
-->

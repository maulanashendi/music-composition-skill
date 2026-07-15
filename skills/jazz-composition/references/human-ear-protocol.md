# Human-ear spot-check protocol (layer 3)

This package's eval methodology has three layers (see
`tests/results/2026-07-13-brief-01-02-armA-vs-armB.md` for layers 1-2
already run):

1. **Automated gate** — `validate_abc.py` + a manual MIDI track/note/tempo
   check. Cheap, catches breakage. Already run.
2. **LLM-judge, blind pairwise** — a fresh subagent scores both versions
   against the /64 rubric without knowing which is which. Cheap, scalable,
   catches theory/craft gaps. Already run.
3. **Human ear, blind A/B** — this document. **Not run yet in this pass** —
   it requires an actual person listening to actual audio, which no agent
   can do or fake. Layers 1-2 explicitly cannot certify "enjoyable to
   listen to"; only this layer can.

Run this on a small subset (2 briefs is enough) before a release that
changes composition craft, not on every eval run — it's the expensive
layer, spend it deliberately.

**Klarifikasi cakupan (penting):** aturan sampling di atas ("2 briefs is
enough", "not on every eval run") **hanya berlaku untuk eksperimen
evaluasi skill/paket ini sendiri** (mis. eval before/after seperti
`tests/results/2026-07-13-brief-01-02-armA-vs-armB.md`). Untuk **piece
produksi** — composer benar-benar membuat lagu untuk dipakai, bukan
mengevaluasi skill — **L3 wajib per-piece** sebelum piece itu disebut
selesai; tidak ada sampling untuk kasus ini. Gerbang mekanis sebelum L3
boleh dijalankan: checklist pra-L3 (fail-closed) di `../SKILL.md`
§Penilaian.

## 1. Render both candidates to audio

This package stops at MIDI; it does not render audio itself (see
`README.md`, "Downstream"). Two ways to get from the `song.mid` files in
`tests/runs/<brief>-arm{A,B}/` to something listenable:

- **Primary — the `daw_generative` engine.** With its dev server running,
  `POST /api/render` with the corresponding ABC (and drum grid, for
  with-skill runs) realizes it via FluidSynth and returns audio. This is
  the package's own stated primary downstream path — use it if the engine
  is available.
- **Alternative — any local MIDI-to-audio path** (a DAW, `fluidsynth` CLI
  with a General MIDI soundfont, or an online converter you trust) if the
  engine isn't running. The point is a listenable audio file per
  candidate, not a specific tool.

## 2. Anonymize before listening

Rename the rendered files so the listener cannot tell which arm/version
produced which, e.g. `brief-01-recording-1.wav` / `brief-01-recording-2.wav`,
with the actual A/B mapping written down separately by whoever did the
rendering (not shared with the listener until after scoring). Randomize
which one is "Recording 1" per brief — don't let Arm B always land in the
same slot, or the listener will pattern-match instead of judging.

## 3. Score blind

For each recording, independently (without comparing notes between
recordings until both are scored):

- Does it hold together as a piece of music, independent of "correctness"?
- Does the groove feel physical/danceable/breathing, or mechanical?
- Does the emotional arc in the brief (e.g. "doubt to acceptance") actually
  land, or does it just read as generic harmonic motion?
- Any single thing that breaks the listening experience (an unplayable-
  sounding leap, a jarring desync, a section that overstays)?

Then, only after both are scored independently: which one do you prefer,
and why — in your own words, not by re-deriving the rubric.

## 4. Record the result

Append a dated entry to `tests/results/`, e.g.
`tests/results/<date>-human-ear-<brief>.md`, with: which brief, the
anonymized labels and their real A/B mapping, the independent notes per
recording, the preference verdict, and who listened. Do not overwrite
previous entries — this is a running log, not a single scoreboard.

## What "success" looks like over time

Layers 1-2 already showed with-skill winning on rubric score both times
this package was evaluated (49 vs 45, 55 vs 49) without human-ear
confirmation. Success at this layer means that preference holds up by ear,
not just on paper — if human-ear spot-checks start disagreeing with the
rubric consistently, that's a signal the rubric is measuring something
that doesn't track "enjoyable," and the rubric (not the composition
craft) is what needs revisiting.

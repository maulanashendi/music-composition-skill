# Arrangement — interaction map, ensemble interaction, transisi

Konsolidasi Task 3 dari tiga file lama `arrangement/references/`
(`interaction-map.md`, `ensemble-interaction.md`,
`instrumental-transitions.md`) — satu tempat ringkas untuk peta interaksi
dasar + kedalaman ensemble/transisi saat dibutuhkan, dipakai di Ideation
poin 6 (`../SKILL.md`).

## §1 — Interaction map dasar

The interaction map answers one question per instrument, per section: **is it leading, supporting, answering, or silent?** Getting this right is what makes an arrangement feel alive instead of a wall of sound. It is not a new creative dimension piled on top of the music — it is the translation of the dramatic arc into "who plays when."

> **Catatan comping.** "Comping" di seluruh file ini berarti **gaya**
> (`sparse`/`block-chord`/`arpeggiated`) + **density**, BUKAN voicing
> pitch konkret — lihat `harmony.md` §"Yang TIDAK ditulis di sini". Kata
> "voicing"/"register" di bawah adalah niat karakter (mis. "voicing
> penuh" vs "voicing sparse"), bukan daftar pitch literal.

### Empat peran

- **Lead** — carries the melody or the main hook. Usually one instrument at a time. Whoever leads owns the listener's attention.
- **Support** — comps, holds harmony, or lays the groove underneath. Rhodes stabs, pad sustains, walking bass. Present but not competing with the lead.
- **Answer** — plays in the *gaps* the lead leaves (call-and-response). The answer instrument is silent while the lead sings, then fills the space after. This dialogue is one of the strongest ways to keep interest without adding density.
- **Silent** — deliberately not playing. Silence is a role, not an absence. Dropping a voice for a section (subtraction) makes its return land hard.

### Arc menentukan density

Read the plan's `arc`. Each phase implies how many voices should be active:

- **quiet/lonely phase** → one or two voices, lots of space, drums near-absent. Do not fill it.
- **building phase** → voices enter one at a time; density climbs gradually.
- **peak phase** → full ensemble together, everyone active, drums full.
- **resolution phase** → voices drop away, density thins, drums fade, space returns.

If a section's density doesn't match its arc phase, the arrangement fights the emotion. A lonely section with everyone playing doesn't feel lonely.

### Teknik, dipakai hanya saat melayani arc

- **Call-and-response** — pair a lead and an answer instrument; they alternate, never overlap. Best in building or mid sections where dialogue adds life.
- **Subtraction** — drop a prominent voice (often the comp) for a section. The re-entry feels full again by contrast. Strongest right before a peak or as a breakdown.
- **Tutti** — everyone hits together, often on-beat. Reserve for the peak; it loses impact if overused.
- **Handoff** — the lead role passes from one instrument to another between sections, keeping the ear fresh.

Do not use all of these in one piece. Pick the few that serve the arc. A map with three purposeful moves beats one with ten.

### Peta konkret, bukan kalimat

Write it as a table: rows = sections (or bars for fine control), columns = instruments, cells = role. Mark the special events (call-response, subtraction, tutti). Example shape:

| Section | Feeling | Lead | Keys | Bass | Drums | Event |
|---|---|---|---|---|---|---|
| Intro | lonely | silent | support (alone) | support | near-silent | bare |
| A1 | lonely | lead (sparse) | support | support | soft | space around lead |
| B | building | lead | answer | support | grows | call-response lead↔keys |
| C | peak | lead | support | support | full | tutti |
| Outro | rest | lead (fading) | support | support | fades | subtraction into silence |

### Gerbang kualitas

- Does each section's density match its arc phase? If the peak isn't fuller than the lonely intro, fix it.
- Is any instrument active only to fill space, not to serve the moment? Silence it.
- Is there at least one subtraction or one call-response, so the arrangement has dialogue and contrast?
- Would a listener feel the journey, or just hear everyone playing throughout?

The gate judges whether it serves the arc, not whether every cell is filled. Empty cells (silence) are often the best choice.

### Peran + lane register (dari `ideation-theory.md` §8 lama)

- Beri tiap instrumen sebuah **peran** dan **lane register** supaya tidak
  bertabrakan: bass (rendah, fondasi), keys (menengah, harmoni/comping),
  lead (menengah-atas, melodi), pad (lebar, perekat), drum (groove).
- **Call and response** antara lead dan comp menciptakan dialog dan
  menjaga ruang tetap hidup.
- **Subtraction** (menghilangkan satu instrumen untuk satu section) adalah
  salah satu gerakan aransemen terkuat — membuat entry kembali terasa kena.
- Density harus mengikuti arc: intro jarang, tengah lebih penuh, ending
  menipis. Putuskan entrance/exit ini di tahap ide supaya plan membawanya.

## §2 — Ensemble interaction lanjutan

> Dipakai saat ensemble/style butuh kedalaman lebih dari peta empat-peran
> di §1 saja (duo/trio/big band conventions, call-and-response, trading,
> cue systems). Reduksi kembali ke format tabel §1 untuk deliverable
> aktual — bagian ini alat berpikir, bukan format output plan.

Jazz interaction is coordinated listening within a shared or deliberately changing framework. Define enough structure for meaningful choice without scripting every response.

### Shared reference layers

An ensemble may share: pulse; meter; subdivision; form; harmony or center; motif; groove; cue system; density curve. Players do not need identical rhythms, notes, or voicings. In open music, some layers may be intentionally removed, but the remaining reference must be clear.

### Interaction levels

- **Supportive** — rhythm section maintains feel and form while making restrained responses.
- **Conversational** — comping, drums, bass, and soloist exchange motifs, accents, and spaces.
- **Transformative** — the ensemble changes texture, subdivision, density, or harmonic implication in response to a player while retaining form or cues.
- **Open collective** — roles and form can shift. Use explicit entry, density, and transition rules.

Choose the level by style, performer experience, and arrangement density.

### Melody instrument or soloist

Responsibilities: state the head clearly enough to establish identity; phrase within or against the groove intentionally; leave space for response; signal structural arrivals; control density and register; hear accompaniment changes; prepare the handoff. A soloist need not dominate every moment. Silence can invite ensemble contribution.

### Piano or guitar comping

Decisions: voicing family (niat, mis. "close"/"open"/"quartal" — bukan pitch); register (niat karakter); rhythmic density; attack and sustain (niat, bukan velocity); harmonic substitutions; response versus support; interaction with bass and drums.

Avoid: covering the soloist's register; repeating one rhythm mechanically; changing harmony so strongly that the bassist and soloist cannot hear the form; filling every rest; using full low-register chords with active bass.

### Bass

Bass can: state roots and form; walk; play two-feel; sustain a pedal; repeat a riff or tumbao; create counterline; drop out for contrast; signal transitions; imply substitutions with approach motion. The bassist may interact melodically while preserving structural targets — ditulis sebagai posisi chord-tone stack (`degree`), lihat `rhythm-groove.md`. In open music, define whether bass controls center, pulse, or neither.

### Drums and percussion

Drums can: establish subdivision and feel; mark form through setups and fills; shape dynamics; respond to motifs; change cymbal or texture; create metric tension; cue transitions; drop time while preserving phrase awareness — semua ini niat karakter groove/pattern (lihat `groove-vocabulary.md`), bukan hit konkret. Avoid constant fills. Reserve strong setups for meaningful arrivals. Percussion in culturally specific grooves needs defined roles; do not stack generic patterns without checking timeline or clave compatibility.

### Horns and written backgrounds

Backgrounds should: be simple enough to repeat; occupy a different register or rhythmic space from the soloist; support the form; enter after the solo has established direction; leave exits and breaths; build or release energy. Possible backgrounds: sustained pads; riff responses; guide-tone punches; counterline; shout-like ensemble figures; call-response with soloist.

### No-chord-instrument ensembles

In sax-bass-drums or trumpet-bass-drums: bass and melody imply harmony; guide tones and roots need strategic placement; ambiguity can be intentional; counterpoint becomes more important; silence creates harmonic openness; soloists should know structural destinations even without comping chords.

### Duo interaction

- **Melody instrument and piano/guitar** — share bass, harmony, and counterline responsibilities. Use register separation and rubato cues.
- **Melody instrument and bass** — harmony is implied through line and double stops. Define pulse and form clearly.
- **Piano and bass** — avoid constant overlap in low register. Exchange lead and support roles.
- **Instrument and drums** — use motif, timbre, and pulse as primary structures. Harmonic center may be implied or open.

### Trio interaction

- **Piano trio** — piano, bass, and drums can distribute melody, harmony, and pulse. Avoid treating bass and drums as fixed accompaniment only.
- **Guitar trio** — account for guitar sustain and register. Bass may state more roots when guitar uses rootless voicings.
- **Chordless trio** — use counterpoint, guide-tone implication, and form cues.

### Call and response

Define: caller; response length; whether response copies rhythm, contour, pitch, or energy; number of cycles; exit cue. Responses can cross instrument roles: soloist to drums, bass to piano, horns to rhythm section.

### Breaks and stop-time

- **Break** — most of the ensemble stops while one player continues. Specify length and reentry.
- **Stop-time** — ensemble punctuates fixed hits while a soloist plays between them. Ensure hits are countable and do not obscure form.

Use breaks to expose time feel, create surprise, or transition sections.

### Trading

Trading can use 2, 4, 8, or irregular bar lengths. Specify: participants; order; whether the form continues; number of cycles; backgrounds or no backgrounds; cue back to head. Trading with drums often retains the song form even when harmony is absent.

### Background buildup

A common sequence: (1) no background during opening solo phrase; (2) sparse two-bar response; (3) repeated riff on next chorus; (4) harmonized or louder version near climax; (5) clear cutoff before handoff. Do not add backgrounds merely because the arrangement has horns.

### Dynamic and textural arc

Plan changes in: volume; density; register; number of active players; cymbal or percussion texture; harmonic complexity; rhythmic subdivision; articulation (niat karakter). A dynamic arc can rise, fall, plateau, or alternate. Match the composition's narrative.

### Cue systems

Possible cues: visual hand cue; repeated musical figure; drum setup; bass pedal; held note; count-off; conductor cue; number of repetitions; lyric or spoken cue. State who initiates and what follows.

### Interaction by architecture

- **Functional changes** — comping and bass clarify arrivals; drums set up cadences; soloist can play through or against changes.
- **Modal** — interaction focuses on motif, texture, register, and density. Bass may pedal or vary the mode.
- **Groove-vamp** — bass and drums maintain pocket; keyboard/guitar interlock; soloist varies rhythm; breakdowns create form.
- **Free/open** — define density, timbre, entry, and transition rules. Silence and listening replace fixed changes as primary coordination.
- **Big band** — much interaction is pre-arranged through backgrounds, ensemble figures, and cues, but rhythm section and soloist still shape phrasing.

### Performance map template

For each section state: leader or cue source; active instruments; fixed material; improvised freedom; groove or pulse status; harmony or center; density target; dynamic target; exit cue; next section.

### Interaction audit

- Does each player know the shared framework?
- Is there space for listening?
- Are backgrounds subordinate to the solo?
- Can the bass and comping coexist?
- Do drum fills mark real structure?
- Are open sections constrained enough to be repeatable?
- Are cues visible or audible?
- Is the return to the head unmistakable?

## §3 — Transisi antar-section

> Dipakai saat batas section butuh lebih dari sekadar cut kosong.
> Section-boundary handling di sini harus konsisten dengan aturan "arc
> decides density" di §1.

### Model transisi

A complete transition has four possible stages: **setup** (create an expectation that the current state will change); **threshold** (the specific event that crosses the boundary); **arrival** (the first event that confirms the new section); **aftercare** (the first one or two bars that stabilize the new state). Not every transition needs all four stages. A hard cut may intentionally omit setup, but the target must still sound deliberate.

### Analisis source-target

Before writing a transition, compare source and target sections across: tonal center or harmonic field; harmonic rhythm; groove and subdivision; meter and tempo; bass behavior; melodic register; texture density; instrumentation; dynamic level; production state; section function. Choose the transition based on the largest perceptual difference. Do not solve a harmonic discontinuity with only a cymbal fill.

### Durasi transisi

- **Zero-bar** — direct cut, stop, or immediate downbeat. Suitable when contrast itself is the effect. Confirm the new section with a strong first event.
- **One-beat to half-bar** — pickup, breath, drum setup, bass anticipation, reverse tail, or ensemble stab. Suitable for closely related sections.
- **One-bar** — fill, turnaround, harmonic pivot, texture subtraction, held chord, or motif lead-in.
- **Two-bar** — composed connector, sequence, bass line, call-response, meter preparation, or harmonic bridge.
- **Four bars or more** — treat as an interlude or developmental section, not merely a transition. Give it motif, phrase direction, and destination.

### Keluarga transisi

- **Rhythmic** — fill derived from the hook rhythm; subdivision change; stop-time break; pickup across the bar line; half-time or double-time setup; accent-cycle convergence; one-bar drum dropout followed by re-entry. Keep at least one pulse reference when the target groove is complex.
- **Harmonic** — dominant or altered dominant preparation; common-tone pivot; chromatic bass connector; pedal that changes interpretation; planed voicing sequence; deceptive arrival followed by correction; sustained upper voice over moving bass; phrase-end reharmonization. Sebutkan **arah/karakter voice-leading** (niat, mis. "turun bertahap ke target"), bukan pitch literal — lihat `harmony.md` §"Yang TIDAK ditulis di sini".
- **Melodic** — hook pickup; motif fragmentation; sequence into target register; held common tone; call from one instrument answered by another; final source note reinterpreted as a target tension; anticipatory target phrase.
- **Bass** — walk-up or walk-down; chromatic approach; octave fall; pedal release; rhythmic anticipation; silence before target root; contrary motion against a held top line (niat karakter, realisasi tetap `degree` + `pyengine`).
- **Textural** — progressive layer subtraction; sudden dry or mono state; register clearing; solo instrument exposure; sustained tail while rhythm stops; foreground-background exchange; orchestral swell or diminuendo.
- **Production** — filter movement tied to phrase direction; resampled tail; reverse element derived from original material; delay throw on the final motif note; room or width change; tape-stop-like event only when stylistically justified; automation that reveals or obscures the downbeat. Production effects must be traceable to musical material or section function; avoid generic risers as default solutions.
- **Negative-space** — rests, cutoffs, empty beats, or tail-only bars. Silence can clarify a new downbeat more effectively than another fill.
- **Metric** — shared-subdivision modulation; additive beat insertion or deletion; repeated cell that becomes the new grouping; gradual accent reinterpretation; countable transition figure. State the equivalence and cue clearly.

### Handoff antar-instrumen

When the lead role changes instruments: identify the final source phrase and first target phrase; decide whether the handoff overlaps, answers, interrupts, or leaves silence; separate registers if both instruments overlap; transfer one motif feature so the handoff feels related; reduce accompaniment during the transfer if clarity is needed; let the receiving instrument establish its role before adding counterlines.

Possible handoff designs: melody note sustained while another instrument completes the phrase; call-response across two bars; unison for one beat, then divergence; source instrument becomes a background figure; target instrument enters with a rhythmic augmentation of the hook; bass or drums announce the new lead through a setup figure.

### Konfirmasi arrival

The target section should confirm itself through at least two cues: new bass behavior; target chord or center; target groove; new register; new texture; complete hook statement; clear dynamic or articulation change. Do not spend the first four bars of a short section continuing to transition unless ambiguity is intentional.

### Masuk dan kembali dari solo

**Entering a solo:** simplify one layer before the soloist enters; state the solo form or vamp clearly; use a pickup or background release; avoid placing a dense transition over the soloist's first phrase; define whether the solo begins on a downbeat, pickup, or open cue.

**Returning from a solo:** bass ostinato recall; drum figure associated with the head; background hook entering in the final solo phrase; target guide tone; density drop; repeated cue phrase; fixed turnaround; conductor or named-player cue. The return must be audible to performers and listeners without prose explanation.

### Alternatif studio dan live

For any transition dependent on automation, edit, reverse audio, resampling, or fade, provide a live alternative such as: cymbal swell; held voicing; written pickup; bass cue; repeated tag; conductor cutoff; countable interlude.

### Mode kegagalan

Drum fill used at every boundary; cymbal crash without sectional change; random chromatic connector unrelated to voice leading; generic riser covering an unprepared target; transition longer than the section it serves; all instruments filling simultaneously; no confirmation after a dramatic buildup; abrupt key change with no common tone, bass logic, motif, or intentional rupture; solo return based only on eye contact in a composition intended for repeatable performance; studio-only ending with no stage solution.

### Output dan audit transisi

For every major boundary, provide:

| From | To | Perceptual gap | Duration | Setup | Threshold | Arrival | Aftercare | Live alternative |
|---|---|---|---|---|---|---|---|---|

Audit: Does the transition solve the largest source-target difference? Is its duration proportional to the structural change? Is at least one element preserved across the boundary? Is the target confirmed immediately enough? Is the handoff orchestrationally clear? Does the transition use material from the composition? Is a live alternative available when needed? Are different transition families used across the piece?

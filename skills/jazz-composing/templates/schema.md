# Style template — field contract

A style template is a composition recipe that seeds `plan.json`. It stores
musical decisions and constraints, not rendered notes or engine timing values.

## Required shape

```json
{
  "id": "neo-soul-midnight",
  "when_to_use": "one line matching registry.md",
  "style": "neo-soul",
  "defaults": {
    "key_options": ["F major", "Eb major"],
    "tempo_range": [68, 80],
    "meter": "4/4",
    "feel": "relaxed swung-sixteenth pocket"
  },
  "groove_profile": "neo-soul-core",
  "template_version": "1.0.0",
  "palette_reference_key": "F major",
  "form_archetype": ["intro", "A1", "A2", "bridge", "peak", "outro"],
  "harmony_palette": {
    "diatonic_core": ["Fmaj9", "Dm9", "Gm11"],
    "signature_moves": ["Bbm7 -> Eb7 -> Fmaj9"],
    "cadence_options": ["Bbmaj7#11 -> Fmaj9"],
    "avoid": ["plain repeated voicings"]
  },
  "hook_archetypes": [
    {
      "name": "rise-and-settle",
      "rhythm": "syncopated pickup into a held target",
      "contour": "rise then settle",
      "first_appears": "intro"
    }
  ],
  "melody_phrasing": {
    "doubt": {
      "note_lengths": "short phrases with long gaps",
      "contour": "gentle rise then fall",
      "placement": "behind the beat"
    }
  },
  "drum_skeleton": {
    "low_energy": "role behavior",
    "mid_energy": "role behavior",
    "high_energy": "role behavior"
  },
  "arrangement_defaults": {
    "entrance_order": ["keys", "bass", "lead", "drums"],
    "layout_rules": "section and interaction rules"
  },
  "anti_boredom_rules": ["variation constraint"],
  "bass_behavior": {
    "role": "musical function",
    "rhythmic_relationship": "relationship to drums and ensemble",
    "density": "sparse, medium, or continuous",
    "articulation": "attack and duration behavior"
  },
  "groove_intent": {
    "feel": "musician-readable pocket description",
    "kick": "kick behavior",
    "snare": "snare behavior",
    "hihat": "hat or subdivision behavior",
    "ensemble_relationship": "how the roles create the pocket"
  },
  "differentiation": {
    "nearest_templates": ["lofi-jazzhop"],
    "distinguishing_traits": [
      "difference one",
      "difference two",
      "difference three"
    ]
  },
  "composition_status": {
    "defined": true,
    "outline_validated": true,
    "desk_reviewed": true,
    "listening_reviewed": false
  },
  "engine_support": {
    "renderable": false,
    "engine_vibe": null,
    "tempo_range_effective": null,
    "blockers": []
  }
}
```

## Composition fields

- `template_version`: semantic version of the composition recipe.
- `palette_reference_key`: canonical key in which chord names are written. It
  must also appear in `defaults.key_options`; the orchestrator transposes the
  palette when another key is selected.
- `form_archetype`: ordered structural intention. It must show development but
  does not lock bar counts.
- `bass_behavior`: direct statement of bass function, rhythm, density, and
  articulation.
- `groove_intent`: musical pocket description. It must remain understandable to
  a musician and must not contain engine tick offsets.
- `differentiation`: explicit boundary against the closest templates. Use at
  least three substantive differences.
- `composition_status`: composition review state. `listening_reviewed` must stay
  false until rendered or human-performed material has been reviewed.

## Existing recipe fields

- `id`: unique kebab-case id matching filename and registry row.
- `when_to_use`: exact copy of the registry description.
- `style`: human-facing style identity.
- `defaults`: candidate keys, tempo range, meter, and feel.
- `groove_profile`: named reference to the groove knowledge layer.
- `harmony_palette`: vocabulary, signature moves, cadences, and avoid rules.
- `hook_archetypes`: reusable hook shapes, not fixed note events.
- `melody_phrasing`: phrase behavior keyed by the template's arc phases.
- `drum_skeleton`: drum behavior at three energy levels.
- `arrangement_defaults`: entrance order and section interaction rules.
- `anti_boredom_rules`: mandatory variation constraints.

## Engine status is separate

`engine_support` records downstream implementation readiness only. It must not
be used as evidence that a composition recipe is musically valid. Conversely,
a template may be composition-valid while `renderable` remains false.

## Canonical outline

Each template must have
`../examples/composition-outlines/<template-id>.md` containing:

- Tempo
- Key
- Form
- Harmony
- Hook
- Bass behavior
- Drum intent
- Arrangement development
- Ending

## Validation

Run:

```bash
python scripts/validate_composition_templates.py \
  --report composition-validation-report.md
```

The validator checks registry consistency, required recipe fields, canonical
outlines, differentiation, and known contradiction regressions. It does not
run an engine or claim listening approval.

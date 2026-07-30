# Composition-level validation

This validation concerns the quality and completeness of the musical recipe. It
does not claim that an engine can render the template or that a listening panel
has approved the resulting audio.

A template is `desk_reviewed` when it satisfies all of the following:

1. Its genre identity is explicit and distinguishable from nearby templates.
2. Its harmonic vocabulary and melodic phrasing fit that identity.
3. Its `form_archetype` creates development rather than a static list of parts.
4. Its `groove_intent` is specific enough for a musician to understand the
   pocket without requiring engine timing numbers.
5. Bass, drums, and arrangement parts describe behavior, not only instrument
   names.
6. Its `differentiation` section records concrete differences from the closest
   templates.
7. Its rules do not contradict its tempo, form, or rhythmic design center.
8. A canonical outline exists in
   `../examples/composition-outlines/<template-id>.md`.

Run the validator from the repository root:

```bash
python scripts/validate_composition_templates.py \
  --report composition-validation-report.md
```

A successful result establishes `composition_status.desk_reviewed: true`. It
must not set `listening_reviewed: true`; that status requires rendered or
human-performed material and a separate listening process.

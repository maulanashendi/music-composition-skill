#!/usr/bin/env python3
"""Convert drums.json Tool 1 (grid v1/v2, lihat grid_to_midi.py) menjadi
skema `drums` engine daw_generative `POST /api/render`.

Skema engine (lihat ../references/engine-export.md):

    {
      "steps_per_bar": 8 | 12 | 16,
      "gm_map": {voice: 35..81},
      "base_velocity": {voice: 1..127},
      "swing": 0.5..0.75 (opsional, diteruskan apa adanya),
      "sections": [{"bars": int >= 1, "pattern": {voice: "x.Xg..."}}]
    }

Aturan konversi (spec E2):
- (a) pattern dict (v1) -> satu section {bars, pattern} apa adanya.
- (b) pattern list (v2, satu dict per bar) -> dipecah per bar, lalu bar
  berurutan yang identik digabung jadi satu section {bars: N}. Merging
  TIDAK melintasi batas section input (batas section = keputusan musikal).
- (c) Field yang tak dikenal skema engine (phrase_velocity, timing,
  humanize_velocity, label, title, tempo_bpm, beats_per_bar, _comment,
  dll.) DIBUANG dengan WARNING eksplisit ke stderr menyebut nama field —
  bukan silent drop. Nuansa phrase_velocity/timing TIDAK terbawa ke WAV;
  pengganti engine: swing grid + groove profile %%pocket.
- (d) steps_per_bar, gm_map, base_velocity, swing dipertahankan apa adanya.
- (e) Validasi fail-fast (bukan 422 misterius di titik render):
  steps_per_bar di {8,12,16}; nilai gm_map 35-81; nilai base_velocity
  1-127; karakter pola hanya x/X/g/. .

Baris pattern berbentuk list per-step (bentuk yang juga diterima
grid_to_midi.py, "" berarti rest) dinormalisasi ke string engine
("" -> "."). Usage:

    python drums_to_engine.py drums.json [drums-engine.json]

Tanpa argumen kedua, JSON skema engine dicetak ke stdout.
"""
import json
import sys

TOP_LEVEL_KEEP = ("steps_per_bar", "gm_map", "base_velocity", "swing")
SECTION_KEEP = ("bars", "pattern")
VALID_STEPS_PER_BAR = (8, 12, 16)
VALID_CHARS = set("xXg.")


def _warn(message):
    print(f"WARNING: {message}", file=sys.stderr)


def _normalize_row(voice, row, steps_per_bar):
    """Kembalikan bentuk string engine untuk satu baris pattern; validasi
    karakter DAN panjang (harus persis steps_per_bar — engine /api/render
    menolak dengan 422 kalau tidak, jadi cek di sini dulu, fail-fast)."""
    if isinstance(row, list):
        chars = []
        for step in row:
            if step in ("", "."):
                chars.append(".")
            elif step in ("x", "X", "g"):
                chars.append(step)
            else:
                raise ValueError(
                    f"pattern voice {voice!r}: step {step!r} tidak valid — "
                    "hanya 'x'/'X'/'g'/'.'/'' yang dikenal skema engine"
                )
        row = "".join(chars)
    elif not isinstance(row, str):
        raise ValueError(
            f"pattern voice {voice!r}: harus string atau list, "
            f"dapat {type(row).__name__}"
        )
    else:
        bad = set(row) - VALID_CHARS
        if bad:
            raise ValueError(
                f"pattern voice {voice!r}: karakter tidak dikenal {sorted(bad)!r} — "
                "skema engine hanya menerima 'x'/'X'/'g'/'.'"
            )
    if len(row) != steps_per_bar:
        raise ValueError(
            f"pattern voice {voice!r}: panjang baris {len(row)} tidak sama "
            f"dengan steps_per_bar = {steps_per_bar} — engine /api/render "
            "akan menolak ini dengan 422"
        )
    return row


def _normalize_pattern(pattern, steps_per_bar):
    return {
        voice: _normalize_row(voice, row, steps_per_bar)
        for voice, row in pattern.items()
    }


def _sections_from(section, index, steps_per_bar):
    """Hasilkan section engine {bars, pattern} dari satu section Tool 1."""
    bars = section["bars"]
    pattern = section["pattern"]
    if isinstance(pattern, dict):  # v1: passthrough tanpa pemecahan
        yield {"bars": bars, "pattern": _normalize_pattern(pattern, steps_per_bar)}
        return
    if len(pattern) != bars:  # v2 list — cermin validasi grid_to_midi.py
        raise ValueError(
            f"sections[{index}]: pattern list punya {len(pattern)} bar "
            f"tapi section['bars'] = {bars}; harus sama persis"
        )
    per_bar = [_normalize_pattern(p, steps_per_bar) for p in pattern]
    run_pattern, run_bars = per_bar[0], 1
    for pat in per_bar[1:]:
        if pat == run_pattern:
            run_bars += 1
        else:
            yield {"bars": run_bars, "pattern": run_pattern}
            run_pattern, run_bars = pat, 1
    yield {"bars": run_bars, "pattern": run_pattern}


def convert(spec):
    """Konversi dict drums.json Tool 1 (v1/v2) -> dict `drums` skema engine.

    WARNING ke stderr untuk tiap field yang dibuang; ValueError untuk nilai
    yang pasti ditolak engine (fail cepat di sini, bukan 422 di render).
    """
    dropped = sorted(set(spec) - set(TOP_LEVEL_KEEP) - {"sections"})
    for field in dropped:
        _warn(
            f"field {field!r} dibuang: tidak dikenal skema engine /api/render "
            "(nuansa phrase_velocity/timing tidak terbawa ke WAV; engine "
            "memakai swing grid + %%pocket sebagai gantinya)"
        )

    steps = spec.get("steps_per_bar")
    if steps not in VALID_STEPS_PER_BAR:
        raise ValueError(
            f"steps_per_bar = {steps!r} tidak valid — skema engine hanya "
            f"menerima {list(VALID_STEPS_PER_BAR)}"
        )

    gm_map = spec["gm_map"]
    for voice, note in gm_map.items():
        if not isinstance(note, int) or isinstance(note, bool) or not 35 <= note <= 81:
            raise ValueError(
                f"gm_map[{voice!r}] = {note!r} di luar rentang note perkusi "
                "GM engine 35-81"
            )

    base_velocity = spec["base_velocity"]
    for voice, vel in base_velocity.items():
        if not isinstance(vel, int) or isinstance(vel, bool) or not 1 <= vel <= 127:
            raise ValueError(
                f"base_velocity[{voice!r}] = {vel!r} di luar rentang 1-127"
            )

    engine = {
        "steps_per_bar": steps,
        "gm_map": gm_map,
        "base_velocity": base_velocity,
    }
    if "swing" in spec:
        engine["swing"] = spec["swing"]

    sections = []
    for index, section in enumerate(spec["sections"]):
        for field in sorted(set(section) - set(SECTION_KEEP)):
            _warn(
                f"sections[{index}] field {field!r} dibuang: tidak dikenal "
                "skema engine /api/render"
            )
        sections.extend(_sections_from(section, index, steps))
    engine["sections"] = sections
    return engine


def main(argv):
    if len(argv) < 2:
        print("usage: drums_to_engine.py <drums.json> [drums-engine.json]",
              file=sys.stderr)
        return 2
    with open(argv[1]) as fh:
        spec = json.load(fh)
    engine = convert(spec)
    out = json.dumps(engine, indent=2)
    if len(argv) > 2:
        with open(argv[2], "w") as fh:
            fh.write(out + "\n")
        total = sum(s["bars"] for s in engine["sections"])
        print(f"wrote {argv[2]}: {len(engine['sections'])} sections, "
              f"{total} bars")
    else:
        print(out)
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))

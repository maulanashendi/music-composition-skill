# Wave 1 — Seleksi Kandidat, Drum Engine v2, Gate Klaim-vs-Notasi — Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Menutup tiga akar masalah run `runs/2026-07-14-doubt-to-acceptance/` — generate-then-defend, drum tile identik, dan klaim teori yang tak cocok notasi — dengan mekanisme kandidat→seleksi (Level 1-4), drum engine v2 (pattern per-bar + phrase velocity + timing per-role + lint), dan script fakta-notasi (`notation_facts.py`) plus gate klaim-vs-notasi di DoD Level 3/4/7.

**Architecture:** Paket ini "Tool 1" (otak) — output-nya notasi ABC, `drums.json`, dan MIDI validasi via script Python lokal; TIDAK ada render audio (itu Tool 2 via HTTP di luar repo). Semua mekanisme baru berupa prosa/prosedur di `SKILL.md` yang dibaca-dieksekusi agent, plus tiga perubahan kode berdampak sempit: `notation_facts.py` (baru), `grid_to_midi.py` v2 (backward compatible), dan refactor minimal `abc_to_midi.py` (ekstraksi `split_voices`). `notation_facts.py` **memakai ulang** parser ABC music21 yang sudah dipakai `abc_to_midi.py` (bukan parser baru); chord symbol diekstrak dari teks ABC mentah lalu diklasifikasi dengan parser chord minimal berbasis `music21.harmony.ChordSymbol`.

**Tech Stack:** Python 3.11 (via `uv`), `music21` + `pretty_midi` (dari cache uv), `unittest`. Dokumen skill = Markdown berbahasa Indonesia (istilah musik Inggris dibiarkan).

## Global Constraints

Setiap task secara implisit tunduk pada seluruh constraint di bawah ini:

1. **Backward compatible:** `drums.json` legacy (dict-pattern per section) harus tetap ter-render **identik bit-untuk-bit** pada notes/velocity/onset dengan sebelum perubahan — hanya boleh **bertambah warning** (murni informasional di stderr, tidak mengubah `.mid`).
2. **`notation_facts.py` reuse parser `abc_to_midi.py`, bukan parser baru** — analisis pitch memakai `music21.converter.parse` (jalur yang sama dipakai `abc_to_midi.py`) dan memanggil `split_voices()` yang di-ekstrak dari `abc_to_midi.py`. Dilarang menulis ulang tokenizer/parser pitch ABC dari nol.
3. **Chord symbol tak dikenal → "unparsed", tidak boleh crash** — `parse_chord_symbol()` menangkap semua exception dan mengembalikan `None`; downstream menandai `"unparsed"` tanpa raise.
4. **Semua commit TANPA baris `Co-Authored-By`** dan **TANPA footer "Generated with Claude Code"**; pesan commit **bahasa Indonesia**, gaya seperti `git log --oneline -10` (mis. `feat: ...`, `fix: ...`, `docs: ...`, `test: ...`).
5. **Dokumen skill berbahasa Indonesia**, istilah musik Inggris (voicing, chord-tone, backbeat, dsb.) dibiarkan.
6. **Jangan menyentuh file di `runs/`** dan **jangan pindah branch** (tetap di `wave1-seleksi-drum-claimgate`).

## Lingkungan & cara menjalankan test (baca sebelum mulai)

- Tidak ada `pyproject.toml`/venv di repo. `music21` dan `pretty_midi` **tidak** terpasang di python sistem; jalankan lewat `uv` yang menyuntik keduanya dari cache. Command test kanonik (dipakai di setiap task, sudah diverifikasi jalan di repo ini):

  ```bash
  # test drum + abc->midi (dari dir scripts midi-orchestration)
  cd skills/midi-orchestration/scripts && uv run --with music21 --with pretty_midi python -m unittest test_abc_to_midi_and_grid -v

  # test notation_facts (dari dir scripts abc-notation)
  cd skills/abc-notation/scripts && uv run --with music21 --with pretty_midi python -m unittest test_notation_facts -v
  ```

  Kedua file test menggunakan `unittest` + loader `importlib.util.spec_from_file_location` (bukan pytest). `test_abc_to_midi_and_grid.py` meng-import `abc_to_midi.py` (butuh music21) dan `grid_to_midi.py` (butuh pretty_midi), jadi **kedua** flag `--with` selalu diperlukan.
- `validate_abc.py` adalah pure-stdlib (tidak relevan untuk task ini selain sebagai referensi konvensi argparse: positional `abc_file: Path` + flag opsional).

## Acceptance DI LUAR plan ini (dieksekusi orkestrator setelah semua task selesai)

Uji penerimaan #3 spec — **satu run komposisi baru end-to-end** (brief baru, bukan dua brief lama yang sudah dikritik), lalu `output.mid`-nya diserahkan ke user untuk L3 (telinga) — **BUKAN task di plan ini**. Orkestrator menjalankannya setelah Task 1-5 hijau. Plan ini hanya bertanggung jawab atas: semua test Python lulus (acceptance #1) dan regresi nol pada `drums.json` legacy (acceptance #2), yang keduanya ditutup oleh Task 1-2.

---

## Task 1: `notation_facts.py` + refactor `split_voices` di `abc_to_midi.py`

**Files:**
- Modify: `skills/midi-orchestration/scripts/abc_to_midi.py` (ekstrak `split_voices` dari `render`)
- Create: `skills/abc-notation/scripts/notation_facts.py`
- Test: `skills/abc-notation/scripts/test_notation_facts.py` (baru)

**Interfaces:**
- Consumes: `abc_to_midi.split_voices(lines: list[str]) -> tuple[list[str], dict[str,str], dict[str,list[str]]]` — mengembalikan `(header_lines, voice_names, body_by_voice)`.
- Produces (dipakai Task 5 sebagai referensi dokumen):
  - `notation_facts.analyze(abc_text: str, voice: str | None = None) -> dict` — per voice: `{"key", "bars":[{"bar","chord","chord_pcs","chord_vs_key","notes":[{"name","octave","midi","cls","in_chord"}],"top_note"}], "intervals":[{"semitones","name","direction"}], "summary":{...}}`.
  - `notation_facts.parse_chord_symbol(sym: str) -> list[str] | None` — daftar nama pitch-class chord, atau `None` bila tak dikenal (unparsed).
  - `notation_facts.format_report(analysis: dict) -> str` — teks/markdown fakta.
  - CLI: `python notation_facts.py <file.abc> [--voice <id>]`.

**Catatan desain (keputusan yang sudah divalidasi terhadap tooling nyata):**
- Reuse parser: `analyze()` membangun stub per-voice (header + `V:id` + body, chord symbol **dibiarkan**) dan mem-parse dengan `music21.converter.parse(stub, format="abc")` — jalur identik yang dipakai `abc_to_midi.render`. Voice-splitting diambil dari `abc_to_midi.split_voices` (di-ekstrak di step 1). music21 otomatis menerapkan key signature (`K:Cm` → `E` berbunyi `E-`/Eb) dan oktaf ABC.
- Chord symbol: music21 **diam-diam membuang** chord symbol yang tak dikenalnya saat parse ABC (mis. `"G7alt"`, `"Wackadoo"`), sehingga sinyal "unparsed" hilang bila kita hanya mengandalkan music21. Karena itu chord symbol **diekstrak dari teks ABC mentah** per bar (regex `"([^"]*)"` yang diawali `A`-`G`) lalu diklasifikasi oleh `parse_chord_symbol()`. Ini bukan "parser ABC baru" — pitch (bagian sulit: key sig, oktaf) tetap dari music21.
- `parse_chord_symbol()` menormalkan simbol gaya ABC ke bentuk yang dipahami `music21.harmony.ChordSymbol`: flat `Xb` → `X-` (root & slash-bass), dan alias `(?:7)?alt` → `7b9#5` (music21 tak mengenali `7alt`; alias ini memberi altered dominant yang wajar). Tipe lain di daftar spec (`maj7,m7,m9,7,9,13,7sus/7sus4,m7b5,dim7,6,m6,add9,slash-bass`) sudah dipahami music21 apa adanya setelah konversi flat.
- **Top note voicing:** spec §Komponen 3 menulis contoh `[ACEG] → top note G`. Di ABC standar (diverifikasi via music21, parser yang direuse) huruf besar `A` = A4 yang **lebih tinggi** dari `G4`, jadi `[ACEG]` sebenarnya ber-top A. Untuk menguji **maksud** kasus itu (voicing yang puncaknya G) sekaligus benar secara notasi, test memakai voicing setara `[A,CEG]` (A satu oktaf di bawah, ditulis `A,`) → nada bawah→atas `A3,C4,E4,G4`, top = `G`. Ini keputusan sadar; `top_note` diimplementasi benar sebagai **pitch MIDI tertinggi** (bukan urutan tulis).

- [ ] **Step 1: Ekstrak `split_voices` dari `abc_to_midi.render` (refactor behavior-preserving)**

Di `skills/midi-orchestration/scripts/abc_to_midi.py`, ganti awal fungsi `render` (blok yang membangun `header`, `vnames`, `body`) dengan pemanggilan fungsi baru `split_voices`.

Ganti blok ini:

```python
def render(abc_path, out_path, mono_lead=True):
    lines=open(abc_path).read().splitlines()
    header=[h for h in lines if re.match(r"^[A-Za-z]:",h) and not h.startswith("V:")]
    vnames={}
    for ln in lines:
        m=re.match(r"^V:\s*(\S+)",ln)
        if m and "name=" in ln:
            nm=re.search(r'name="([^"]+)"',ln)
            vnames[m.group(1)]=nm.group(1) if nm else m.group(1)
    body={}
    for ln in lines:
        bm=re.match(r"^\[V:\s*(\S+)\]\s?(.*)",ln)
        if bm: body.setdefault(bm.group(1),[]).append(bm.group(2))
```

Menjadi:

```python
def split_voices(lines):
    """Split ABC lines into (header_lines, voice_names, body_by_voice).

    Extracted from render() so notation_facts.py can reuse the exact same
    ABC voice-splitting path instead of writing a second parser.
    """
    header=[h for h in lines if re.match(r"^[A-Za-z]:",h) and not h.startswith("V:")]
    vnames={}
    for ln in lines:
        m=re.match(r"^V:\s*(\S+)",ln)
        if m and "name=" in ln:
            nm=re.search(r'name="([^"]+)"',ln)
            vnames[m.group(1)]=nm.group(1) if nm else m.group(1)
    body={}
    for ln in lines:
        bm=re.match(r"^\[V:\s*(\S+)\]\s?(.*)",ln)
        if bm: body.setdefault(bm.group(1),[]).append(bm.group(2))
    return header, vnames, body


def render(abc_path, out_path, mono_lead=True):
    lines=open(abc_path).read().splitlines()
    header, vnames, body = split_voices(lines)
```

Tidak ada baris lain di `render` yang berubah (baris setelahnya, `# Parse real tempo/meter...`, tetap).

- [ ] **Step 2: Jalankan test lama sebagai guard refactor — harus tetap hijau**

Run: `cd skills/midi-orchestration/scripts && uv run --with music21 --with pretty_midi python -m unittest test_abc_to_midi_and_grid -v`
Expected: `Ran 6 tests ... OK` (test `AbcToMidiTempoMeterTests` melatih `render`, jadi memvalidasi `split_voices` tak mengubah perilaku).

- [ ] **Step 3: Tulis test gagal `test_notation_facts.py`**

Buat `skills/abc-notation/scripts/test_notation_facts.py`:

```python
from __future__ import annotations

import importlib.util
import sys
import unittest
from pathlib import Path

SCRIPTS_DIR = Path(__file__).resolve().parents[0]


def _load(module_name: str, filename: str):
    module_path = SCRIPTS_DIR / filename
    spec = importlib.util.spec_from_file_location(module_name, module_path)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


nf = _load("notation_facts", "notation_facts.py")


def _abc(body: str, key: str = "Cm", voice: str = "Lead") -> str:
    return (
        "X:1\nT:t\nM:4/4\nL:1/8\nQ:1/4=120\n"
        f"K:{key}\nV:{voice}\n[V:{voice}] {body} |]\n"
    )


class NotationFactsTests(unittest.TestCase):
    def test_key_signature_makes_written_E_sound_Eb(self):
        data = nf.analyze(_abc("z C E2 A4"))["Lead"]
        names = [(n["name"], n["octave"]) for bar in data["bars"] for n in bar["notes"]]
        # rest z is NOT a pitch; C sounds C4, E sounds Eb (E-4), A sounds Ab (A-4)
        self.assertEqual(names, [("C", 4), ("E-", 4), ("A-", 4)])

    def test_intervals_are_plus3_then_plus5(self):
        data = nf.analyze(_abc("z C E2 A4"))["Lead"]
        semis = [iv["semitones"] for iv in data["intervals"]]
        dirs = [iv["direction"] for iv in data["intervals"]]
        self.assertEqual(semis, [3, 5])          # minor 3rd up, then perfect 4th up
        self.assertEqual(dirs, ["naik", "naik"])
        self.assertIn("Third", data["intervals"][0]["name"])
        self.assertIn("Fourth", data["intervals"][1]["name"])

    def test_ebmaj7_notes_are_all_chord_tones(self):
        # written e/g/b under K:Cm sound Eb/G/Bb -- all chord tones of Ebmaj7
        data = nf.analyze(_abc('"Ebmaj7" z e g2 b4'))["Lead"]
        classes = [n["cls"] for bar in data["bars"] for n in bar["notes"]]
        self.assertTrue(classes)
        self.assertTrue(all(c == "chord-tone" for c in classes), classes)

    def test_abmaj7_and_ebmaj7_are_diatonic_in_Cm(self):
        data = nf.analyze(_abc('"Abmaj7" A,2C2E2G2 | "Ebmaj7" E,2G,2B,2D2', voice="Keys"), voice="Keys")["Keys"]
        verdicts = [bar["chord_vs_key"] for bar in data["bars"] if bar["chord"]]
        self.assertEqual(verdicts, ["diatonik", "diatonik"])

    def test_voicing_top_note_is_G(self):
        # [A,CEG] = A3,C4,E4,G4 -> highest sounding pitch is G (see plan note on [ACEG])
        data = nf.analyze(_abc("[A,CEG]8", key="C", voice="Keys"), voice="Keys")["Keys"]
        self.assertEqual(data["bars"][0]["top_note"], "G")

    def test_unknown_chord_symbol_is_unparsed_no_crash(self):
        self.assertIsNone(nf.parse_chord_symbol("Wackadoo"))
        data = nf.analyze(_abc('"Wackadoo" C2 E2 G2 z2', key="C"))["Lead"]
        self.assertIsNone(data["bars"][0]["chord_pcs"])
        classes = [n["cls"] for bar in data["bars"] for n in bar["notes"]]
        self.assertTrue(all(c == "unparsed" for c in classes), classes)


if __name__ == "__main__":
    unittest.main()
```

- [ ] **Step 4: Jalankan test — harus GAGAL (modul belum ada)**

Run: `cd skills/abc-notation/scripts && uv run --with music21 --with pretty_midi python -m unittest test_notation_facts -v`
Expected: FAIL / ERROR — `ModuleNotFoundError` atau `FileNotFoundError` untuk `notation_facts.py`.

- [ ] **Step 5: Implementasi `notation_facts.py`**

Buat `skills/abc-notation/scripts/notation_facts.py`:

```python
#!/usr/bin/env python3
"""Report objective facts about the pitches actually written in an ABC file.

This is a FACT GENERATOR, not a claim checker: it reports the notes that
actually sound (after the key signature), the intervals between them, how each
note relates to the bar's chord symbol, the top note of each voicing, and how
each chord relates to the key. The skill instructions (Level 3/4/7 DoD) are
what compare these facts against the prose claims in an artifact.

Pitch parsing reuses abc_to_midi.py's music21 path (split_voices +
music21.converter.parse) rather than a second hand-written ABC parser. Chord
symbols are extracted from the raw ABC text (music21 silently drops unknown
symbols on parse) and classified by a minimal chord parser built on
music21.harmony.ChordSymbol.
"""
from __future__ import annotations

import argparse
import importlib.util as _ilu
import re
import sys
from pathlib import Path

from music21 import converter, harmony, note, chord, key, interval

# --- reuse abc_to_midi.py's voice splitting (single ABC parsing path) ---
_ABC_PATH = (
    Path(__file__).resolve().parents[2]
    / "midi-orchestration" / "scripts" / "abc_to_midi.py"
)
_spec = _ilu.spec_from_file_location("abc_to_midi", _ABC_PATH)
abcmod = _ilu.module_from_spec(_spec)
sys.modules["abc_to_midi"] = abcmod
_spec.loader.exec_module(abcmod)

# --- chord-symbol normalization + minimal parser ---
_FLAT_ROOT_RE = re.compile(r"\b([A-G])b")
_FLAT_BASS_RE = re.compile(r"/([A-G])b")
_ALT_RE = re.compile(r"(?:7)?alt")


def normalize_chord_symbol(sym: str) -> str:
    """ABC/pop chord spelling -> music21 ChordSymbol spelling.

    'Eb'/'Ab'/'Bb' (root or slash bass) -> 'E-'/'A-'/'B-'; '7alt'/'alt' ->
    '7b9#5' (music21 has no 'alt' abbreviation).
    """
    sym = _FLAT_ROOT_RE.sub(r"\1-", sym)
    sym = _FLAT_BASS_RE.sub(r"/\1-", sym)
    sym = _ALT_RE.sub("7b9#5", sym)
    return sym


def parse_chord_symbol(sym: str):
    """Return the chord's pitch-class names, or None if the symbol is unknown.

    Never raises: an unrecognized/eXotic/typo'd symbol yields None ('unparsed').
    """
    try:
        cs = harmony.ChordSymbol(normalize_chord_symbol(sym))
        return [p.name for p in cs.pitches]
    except Exception:
        return None


def extract_bar_chords(body: str):
    """Chord-symbol strings per written bar, split on barlines.

    Only quoted tokens starting with A-G are treated as chord symbols;
    text-placement annotations ('^text', etc.) are ignored. Repeats are NOT
    expanded -- these are facts about the written notation.
    """
    bars = []
    for seg in re.split(r"\|", body):
        seg = seg.strip().strip(":").strip("]").strip("[")
        if seg == "":
            continue
        chords = [q for q in re.findall(r'"([^"]*)"', seg) if re.match(r"^[A-G]", q)]
        bars.append(chords)
    return bars


def _scale_pcs(k):
    return set(p.name for p in k.pitches) if k else set()


def classify_note(pc_name, chord_pcs, scale_pcs):
    if chord_pcs is None:
        return "unparsed"
    if pc_name in chord_pcs:
        return "chord-tone"
    if scale_pcs and pc_name in scale_pcs:
        return "tension-diatonik"
    return "outside"


def chord_vs_key(chord_pcs, scale_pcs):
    if chord_pcs is None:
        return "unparsed"
    if not scale_pcs:
        return "unknown-key"
    if all(pc in scale_pcs for pc in chord_pcs):
        return "diatonik"
    if chord_pcs[0] in scale_pcs:
        return "borrowed"
    return "luar-key"


def _interval_fact(p1, p2):
    iv = interval.Interval(noteStart=note.Note(p1), noteEnd=note.Note(p2))
    semi = iv.semitones
    direction = "naik" if semi > 0 else ("turun" if semi < 0 else "unison")
    return {"semitones": semi, "name": iv.niceName, "direction": direction}


def analyze(abc_text: str, voice: str | None = None) -> dict:
    lines = abc_text.splitlines()
    header, _vnames, body = abcmod.split_voices(lines)
    result: dict = {}
    target_voices = [voice] if voice else list(body.keys())
    for vid in target_voices:
        if vid not in body:
            continue
        joined = " ".join(body[vid])
        stub = "\n".join(header) + f"\nV:{vid}\n" + joined
        s = converter.parse(stub, format="abc")

        k = next(iter(s.recurse().getElementsByClass(key.Key)), None)
        scale_pcs = _scale_pcs(k)
        ts = next(iter(s.recurse().getElementsByClass("TimeSignature")), None)
        bar_ql = float(ts.barDuration.quarterLength) if ts else 4.0
        bar_chords = extract_bar_chords(joined)

        elems = [(int(float(el.offset) // bar_ql), el) for el in s.recurse().notesAndRests]
        max_bar = max((b for b, _ in elems), default=-1)

        notes_seq = []      # ordered Pitch objects for melodic intervals
        bars_report = []
        note_count = rest_count = 0
        durations = []
        for b in range(max_bar + 1):
            chords_here = bar_chords[b] if b < len(bar_chords) else []
            sym = chords_here[0] if chords_here else None
            chord_pcs = parse_chord_symbol(sym) if sym else None
            bar_notes = []
            top = None
            for bar_idx, el in elems:
                if bar_idx != b:
                    continue
                if isinstance(el, note.Rest):
                    rest_count += 1
                    durations.append(float(el.quarterLength))
                    continue
                if isinstance(el, harmony.ChordSymbol):
                    continue
                if isinstance(el, chord.Chord):
                    ps = sorted(el.pitches, key=lambda p: p.midi)
                    top = ps[-1].name
                    for p in ps:
                        note_count += 1
                        durations.append(float(el.quarterLength))
                        bar_notes.append({
                            "name": p.name, "octave": p.octave, "midi": p.midi,
                            "cls": classify_note(p.name, chord_pcs, scale_pcs),
                            "in_chord": True,
                        })
                        notes_seq.append(p)
                elif isinstance(el, note.Note):
                    note_count += 1
                    durations.append(float(el.quarterLength))
                    bar_notes.append({
                        "name": el.pitch.name, "octave": el.pitch.octave,
                        "midi": el.pitch.midi,
                        "cls": classify_note(el.pitch.name, chord_pcs, scale_pcs),
                        "in_chord": False,
                    })
                    notes_seq.append(el.pitch)
            bars_report.append({
                "bar": b + 1, "chord": sym, "chord_pcs": chord_pcs,
                "chord_vs_key": chord_vs_key(chord_pcs, scale_pcs) if sym else None,
                "notes": bar_notes, "top_note": top,
            })

        intervals = [
            _interval_fact(notes_seq[i], notes_seq[i + 1])
            for i in range(len(notes_seq) - 1)
        ]
        total = note_count + rest_count
        result[vid] = {
            "key": str(k) if k else None,
            "bars": bars_report,
            "intervals": intervals,
            "summary": {
                "notes": note_count, "rests": rest_count,
                "rest_ratio": round(rest_count / total, 3) if total else 0,
                "shortest_ql": min(durations) if durations else None,
                "longest_ql": max(durations) if durations else None,
            },
        }
    return result


def format_report(analysis: dict) -> str:
    out = []
    for vid, data in analysis.items():
        out.append(f"# Voice: {vid}")
        out.append(f"Key: {data['key']}")
        s = data["summary"]
        out.append(
            f"Notes: {s['notes']}  Rests: {s['rests']}  Rest-ratio: {s['rest_ratio']}  "
            f"Shortest(ql): {s['shortest_ql']}  Longest(ql): {s['longest_ql']}"
        )
        out.append("")
        for bar in data["bars"]:
            out.append(
                f"## Bar {bar['bar']}  chord={bar['chord']}  "
                f"chord-vs-key={bar['chord_vs_key']}  top-note={bar['top_note']}"
            )
            if bar["chord_pcs"]:
                out.append(f"   chord tones: {', '.join(bar['chord_pcs'])}")
            elif bar["chord"]:
                out.append("   chord tones: UNPARSED (simbol tak dikenal)")
            for n in bar["notes"]:
                out.append(f"   {n['name']}{n['octave']} (midi {n['midi']}) -> {n['cls']}")
        out.append("")
        out.append("Intervals (nada melodi berurutan):")
        for iv in data["intervals"]:
            sign = "+" if iv["semitones"] > 0 else ""
            out.append(f"   {sign}{iv['semitones']} {iv['name']} {iv['direction']}")
        out.append("")
    return "\n".join(out)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("abc_file", type=Path)
    parser.add_argument("--voice", default=None, help="voice id to analyze (default: all)")
    args = parser.parse_args()
    text = args.abc_file.read_text(encoding="utf-8")
    print(format_report(analyze(text, args.voice)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
```

- [ ] **Step 6: Jalankan test — harus LULUS**

Run: `cd skills/abc-notation/scripts && uv run --with music21 --with pretty_midi python -m unittest test_notation_facts -v`
Expected: `Ran 6 tests ... OK`.

- [ ] **Step 7: Smoke-test CLI (opsional tapi disarankan) pada satu ABC run lama**

Run: `cd skills/abc-notation/scripts && uv run --with music21 --with pretty_midi python notation_facts.py ../../../runs/2026-07-14-doubt-to-acceptance/song.abc --voice 1`
Expected: teks laporan tercetak (baris `# Voice: ...`, `## Bar ...`, `Intervals ...`) tanpa traceback. (Ini hanya read-only pada `runs/` — tidak menulis; tidak melanggar constraint 6.)

- [ ] **Step 8: Commit**

```bash
git add skills/midi-orchestration/scripts/abc_to_midi.py skills/abc-notation/scripts/notation_facts.py skills/abc-notation/scripts/test_notation_facts.py
git commit -m "feat: notation_facts.py generator fakta-notasi + ekstrak split_voices (TDD)"
```

---

## Task 2: `grid_to_midi.py` v2 — pattern per-bar, phrase_velocity, timing per-role, lint

**Files:**
- Modify: `skills/midi-orchestration/scripts/grid_to_midi.py`
- Test: `skills/midi-orchestration/scripts/test_abc_to_midi_and_grid.py` (tambah test baru)

**Interfaces:**
- Produces:
  - `grid_to_midi.build_drums(spec_path: str, out_path: str, seed: int = 7) -> list[str]` — sekarang mengembalikan daftar warning lint (sebelumnya `None`; perubahan aman, tidak ada pemanggil yang memakai return).
  - `grid_to_midi.lint_sections(spec: dict) -> list[str]` — warning string per section >2 bar yang semua bar-nya identik.
  - `grid_to_midi._resolve_bar_patterns(section: dict) -> list[dict]` — daftar dict pattern per bar (dict legacy → di-tile; list → apa adanya, dengan validasi panjang).

**Format `drums.json` v2 (backward compatible):**
- `section.pattern` boleh **dict** (legacy → di-tile identik ke semua bar) atau **list of dict** (per-bar; panjang list HARUS == `section.bars`, else `ValueError`).
- `section.phrase_velocity` (opsional): list `float` panjang == `section.bars`, dikalikan ke velocity semua hit di bar itu setelah accent/ghost. Absen → 1.0 (no-op).
- top-level `timing` (opsional): map `role → offset_ms`, ditambahkan deterministik ke onset tiap hit role itu (ms→detik), onset di-klem `max(0, t)`. Absen → tanpa offset.
- Urutan velocity: **base → accent `X`/ghost `g` → `phrase_velocity` → `humanize_velocity`**.

- [ ] **Step 1: Tulis test gagal — tambahkan ke `test_abc_to_midi_and_grid.py`**

Tambahkan blok berikut **sebelum** baris `if __name__ == "__main__":` di akhir file `skills/midi-orchestration/scripts/test_abc_to_midi_and_grid.py`:

```python
def make_v2_spec(sections, timing=None, hum=0) -> dict:
    spec = {
        "tempo_bpm": 120,
        "steps_per_bar": 4,
        "swing": 0.5,
        "humanize_velocity": hum,
        "gm_map": {"kick": 36, "snare": 38},
        "base_velocity": {"kick": 100, "snare": 80},
        "sections": sections,
    }
    if timing is not None:
        spec["timing"] = timing
    return spec


class GridToMidiV2Tests(unittest.TestCase):
    def test_per_bar_list_renders_each_bar_independently(self):
        # bar 0 hits kick at step 0; bar 1 hits snare at step 0
        spec = make_v2_spec([{
            "bars": 2,
            "pattern": [
                {"kick": ["x", "", "", ""]},
                {"snare": ["x", "", "", ""]},
            ],
        }])
        pm = build_drums(spec)
        notes = sorted(pm.instruments[0].notes, key=lambda n: n.start)
        self.assertEqual(len(notes), 2)
        self.assertEqual(notes[0].pitch, 36)               # kick, bar 0
        self.assertAlmostEqual(notes[0].start, 0.0, places=3)
        self.assertEqual(notes[1].pitch, 38)               # snare, bar 1
        self.assertAlmostEqual(notes[1].start, 2.0, places=3)  # 120bpm, 4/4 -> 2s/bar

    def test_pattern_list_length_mismatch_raises(self):
        spec = make_v2_spec([{"bars": 3, "pattern": [{"kick": ["x", "", "", ""]}]}])
        with self.assertRaises(ValueError):
            build_drums(spec)

    def test_phrase_velocity_scales_each_bar(self):
        spec = make_v2_spec([{
            "bars": 2,
            "pattern": {"kick": ["x", "", "", ""]},
            "phrase_velocity": [1.0, 0.5],
        }])
        pm = build_drums(spec)
        notes = sorted(pm.instruments[0].notes, key=lambda n: n.start)
        self.assertEqual([n.velocity for n in notes], [100, 50])

    def test_phrase_velocity_length_mismatch_raises(self):
        spec = make_v2_spec([{
            "bars": 2,
            "pattern": {"kick": ["x", "", "", ""]},
            "phrase_velocity": [1.0],
        }])
        with self.assertRaises(ValueError):
            build_drums(spec)

    def test_timing_offsets_target_role_only_and_clamps(self):
        spec = make_v2_spec(
            [{"bars": 1, "pattern": {"kick": ["x", "", "", ""], "snare": ["x", "", "", ""]}}],
            timing={"kick": 100},   # +100 ms on kick only
        )
        pm = build_drums(spec)
        starts = {n.pitch: round(n.start, 3) for n in pm.instruments[0].notes}
        self.assertAlmostEqual(starts[36], 0.1, places=3)   # kick shifted +0.1s
        self.assertAlmostEqual(starts[38], 0.0, places=3)   # snare unchanged

    def test_timing_negative_offset_clamped_to_zero(self):
        spec = make_v2_spec(
            [{"bars": 1, "pattern": {"kick": ["x", "", "", ""]}}],
            timing={"kick": -500},
        )
        pm = build_drums(spec)
        self.assertAlmostEqual(pm.instruments[0].notes[0].start, 0.0, places=3)

    def test_lint_warns_on_identical_multibar_section(self):
        spec = make_v2_spec([{
            "bars": 3,
            "pattern": [{"kick": ["x"]}, {"kick": ["x"]}, {"kick": ["x"]}],
        }])
        self.assertTrue(grid_to_midi.lint_sections(spec))

    def test_lint_silent_on_varied_and_on_short_sections(self):
        varied = make_v2_spec([{
            "bars": 3,
            "pattern": [{"kick": ["x"]}, {"kick": ["g"]}, {"kick": ["x"]}],
        }])
        self.assertEqual(grid_to_midi.lint_sections(varied), [])
        short = make_v2_spec([{"bars": 2, "pattern": {"kick": ["x", "", "", ""]}}])
        self.assertEqual(grid_to_midi.lint_sections(short), [])
```

- [ ] **Step 2: Jalankan test baru — harus GAGAL**

Run: `cd skills/midi-orchestration/scripts && uv run --with music21 --with pretty_midi python -m unittest test_abc_to_midi_and_grid.GridToMidiV2Tests -v`
Expected: FAIL/ERROR — `AttributeError: module ... has no attribute 'lint_sections'` dan/atau assertion gagal (per-bar list belum didukung).

- [ ] **Step 3: Implementasi `grid_to_midi.py` v2 (ganti seluruh isi file)**

Ganti seluruh isi `skills/midi-orchestration/scripts/grid_to_midi.py` dengan:

```python
#!/usr/bin/env python3
"""Convert a drum step-grid JSON into a MIDI drum track (GM channel 10).

Applies swing (delay off-beat 16th steps), per-role phrase velocity, a small
final velocity humanization, and deterministic per-role timing offsets for a
natural lofi/funk feel. Output is a single-track MIDI on the drum channel,
ready to merge with the pitched MIDI rendered from ABC.

Grid v2 (backward compatible with v1):
- section.pattern may be a dict (legacy: tiled identically across every bar of
  the section) or a list of dicts (one pattern per bar; the list length MUST
  equal section["bars"]).
- section.phrase_velocity (optional): list of float multipliers, one per bar
  (length must equal section["bars"]), applied to every hit's velocity in that
  bar after accent/ghost. Absent -> 1.0 for every bar (no-op, identical to v1).
- top-level "timing" (optional): map role -> offset in milliseconds, added
  deterministically to each onset of that role (clamped so onset >= 0). Absent
  -> no per-role offset (identical to v1).

Velocity order: base -> accent X / ghost g -> phrase_velocity -> humanize.
"""
import json
import random
import sys
import pretty_midi


def _resolve_bar_patterns(section):
    """Return a list of per-bar pattern dicts for a section.

    Legacy dict -> tiled identically across all bars. New list -> returned
    as-is, but its length must match section["bars"] exactly (no silent
    truncate/pad).
    """
    pattern = section["pattern"]
    bars = section["bars"]
    if isinstance(pattern, list):
        if len(pattern) != bars:
            raise ValueError(
                f"section pattern list has {len(pattern)} bars but section['bars'] "
                f"is {bars}; per-bar pattern lists must match the bar count exactly"
            )
        return pattern
    return [pattern] * bars


def lint_sections(spec):
    """Warn (not error) when a section > 2 bars has every bar identical.

    Applies to both pattern forms: a legacy dict is identical-by-tiling, and a
    list whose entries are all equal. Purely informational -- does not change
    the rendered MIDI.
    """
    warnings = []
    for idx, section in enumerate(spec["sections"]):
        bars = section["bars"]
        if bars <= 2:
            continue
        patterns = _resolve_bar_patterns(section)
        first = patterns[0]
        if all(p == first for p in patterns):
            label = section.get("label", f"section {idx}")
            warnings.append(
                f"section {idx} ({label!r}) has {bars} bars but every bar is "
                "identical; add a 2-bar base + variation + transition per "
                "level-09-drum.md"
            )
    return warnings


def build_drums(spec_path: str, out_path: str, seed: int = 7):
    random.seed(seed)
    spec = json.load(open(spec_path))

    tempo = spec["tempo_bpm"]
    spb = spec["steps_per_bar"]
    swing = spec.get("swing", 0.5)          # 0.5 = straight; >0.5 pushes off-beats late
    hum = spec.get("humanize_velocity", 0)
    gm = spec["gm_map"]
    basevel = spec["base_velocity"]
    timing = spec.get("timing", {})         # role -> ms offset (deterministic)

    sec_per_beat = 60.0 / tempo
    # Bar length in quarter-note-equivalents: 4 for 4/4, 3.5 for 7/8 (at eighth-
    # note subdivision), 3 for 3/4, etc. -- numerator * 4/denominator. Defaults
    # to 4 so every existing 4/4 spec that doesn't set this field is unaffected.
    beats_per_bar = spec.get("beats_per_bar", 4)
    sec_per_bar = sec_per_beat * beats_per_bar
    sec_per_step = sec_per_bar / spb

    warnings = lint_sections(spec)
    for w in warnings:
        print(f"WARNING: {w}", file=sys.stderr)

    pm = pretty_midi.PrettyMIDI(initial_tempo=tempo)
    drum = pretty_midi.Instrument(program=0, is_drum=True, name="Drums")

    bar_cursor = 0
    for section in spec["sections"]:
        patterns = _resolve_bar_patterns(section)
        phrase = section.get("phrase_velocity")
        if phrase is not None and len(phrase) != section["bars"]:
            raise ValueError(
                f"phrase_velocity has {len(phrase)} entries but section['bars'] "
                f"is {section['bars']}; they must match"
            )
        for bar_index in range(section["bars"]):
            bar_start = bar_cursor * sec_per_bar
            pat = patterns[bar_index]
            pmult = phrase[bar_index] if phrase is not None else 1.0
            for voice, row in pat.items():
                note = gm[voice]
                bv = basevel[voice]
                for i, ch in enumerate(row):
                    if ch == "x":
                        hit_vel = bv
                    elif ch == "X":
                        hit_vel = bv * 1.2  # accent: ~+20% of normal
                    elif ch == "g":
                        hit_vel = bv * 0.45  # ghost: ~45% of normal
                    else:
                        continue
                    hit_vel *= pmult  # phrase-shaped velocity (directional, not jitter)
                    t = bar_start + i * sec_per_step
                    # swing: push the second 16th of each 8th-note pair later
                    if i % 2 == 1:
                        t += (swing - 0.5) * 2 * sec_per_step
                    # deterministic per-role timing offset; clamp onset >= 0
                    t = max(0.0, t + timing.get(voice, 0) / 1000.0)
                    vel = max(1, min(127, round(hit_vel) + random.randint(-hum, hum)))
                    drum.notes.append(pretty_midi.Note(
                        velocity=vel, pitch=note,
                        start=t, end=t + sec_per_step * 0.9))
            bar_cursor += 1

    pm.instruments.append(drum)
    pm.write(out_path)
    total = len(drum.notes)
    print(f"wrote {out_path}: {total} drum hits across {bar_cursor} bars")
    return warnings


if __name__ == "__main__":
    spec = sys.argv[1] if len(sys.argv) > 1 else "backstep_drums.json"
    out = sys.argv[2] if len(sys.argv) > 2 else "backstep_drums.mid"
    build_drums(spec, out)
```

- [ ] **Step 4: Jalankan seluruh test file — harus LULUS (lama + baru)**

Run: `cd skills/midi-orchestration/scripts && uv run --with music21 --with pretty_midi python -m unittest test_abc_to_midi_and_grid -v`
Expected: `Ran 14 tests ... OK` (6 lama + 8 baru).

- [ ] **Step 5: Verifikasi regresi nol bit-untuk-bit pada `drums.json` legacy**

Buat file sementara `/tmp/wave1_regr.py` (di luar repo) berisi:

```python
import importlib.util, sys, hashlib, subprocess, tempfile, os
from pathlib import Path

REPO = Path("skills/midi-orchestration/scripts").resolve()

def load(name, path):
    s = importlib.util.spec_from_file_location(name, path)
    m = importlib.util.module_from_spec(s); sys.modules[name] = m
    s.loader.exec_module(m); return m

v2 = load("g2", REPO / "grid_to_midi.py")

# Render each legacy spec with BOTH the working-tree (v2) grid_to_midi.py and the
# committed HEAD (pre-Task-2) version, then compare .mid bytes. Only the three
# immutable runs/ legacy specs are used -- NOT drum-grid-template.json, because
# Task 3 rewrites that template to v2 (a list-per-bar form the old HEAD code
# cannot render). The runs/ files are never modified, so this stays valid
# regardless of when it runs; still, run it before committing Task 2 so HEAD is
# the pre-change version (else use HEAD~1 below).
specs = [
    "runs/2026-07-14-doubt-to-acceptance/drums.json",
    "runs/2026-07-14-after-rain-still-warm/drums.json",
    "runs/2026-07-14-urgency-to-release/drums.json",
]
# checkout the pre-change grid_to_midi.py into a temp file for comparison
old = subprocess.run(
    ["git", "show", "HEAD:skills/midi-orchestration/scripts/grid_to_midi.py"],
    capture_output=True, text=True).stdout
tmp = tempfile.NamedTemporaryFile("w", suffix=".py", delete=False)
tmp.write(old); tmp.close()
orig = load("g1", tmp.name)

ok = True
for sp in specs:
    orig.build_drums(sp, "/tmp/_o.mid")
    v2.build_drums(sp, "/tmp/_v.mid")
    ho = hashlib.sha256(open("/tmp/_o.mid","rb").read()).hexdigest()
    hv = hashlib.sha256(open("/tmp/_v.mid","rb").read()).hexdigest()
    print(("IDENTICAL" if ho==hv else "DIFFERENT"), sp)
    ok = ok and (ho == hv)
os.unlink(tmp.name)
print("ALL BIT-IDENTICAL" if ok else "MISMATCH")
```

Run (dari root repo, sebelum commit Task 2): `uv run --with pretty_midi python /tmp/wave1_regr.py`

Catatan: script mengambil versi lama via `git show HEAD:...grid_to_midi.py` (working tree = versi v2 baru). Jalankan **sebelum** meng-commit Task 2 supaya HEAD masih versi lama; bila sudah ter-commit, ganti `HEAD` → `HEAD~1` di script. Tidak perlu `git stash` — old dibaca dari git, v2 dibaca dari working tree.
Expected: `IDENTICAL` untuk ketiga spec + `ALL BIT-IDENTICAL`. (Warning lint muncul di stderr untuk section >2 bar identik pada run lama — itu diharapkan dan tidak mengubah `.mid`.)

- [ ] **Step 6: Commit**

```bash
git add skills/midi-orchestration/scripts/grid_to_midi.py skills/midi-orchestration/scripts/test_abc_to_midi_and_grid.py
git commit -m "feat: drum engine v2 -- pattern per-bar, phrase_velocity, timing per-role, lint (TDD)"
```

---

## Task 3: Aset & dokumen drum — template v2, midi-conversion.md, level-09-drum.md, groove-profiles.md

**Files:**
- Modify: `skills/midi-orchestration/assets/drum-grid-template.json`
- Modify: `skills/midi-orchestration/references/midi-conversion.md`
- Modify: `skills/jazz-composition/references/level-09-drum.md`
- Modify: `skills/groove-rhythm/references/groove-profiles.md`

**Interfaces:**
- Consumes: format v2 dari Task 2 (`grid_to_midi.py`).

- [ ] **Step 1: Ganti `drum-grid-template.json` dengan contoh v2 ber-hierarchy**

Ganti seluruh isi `skills/midi-orchestration/assets/drum-grid-template.json` dengan (sudah diverifikasi: render bersih, 0 warning lint, 167 hits/12 bar):

```json
{
  "_comment": "Drum step-grid for grid_to_midi.py. section.pattern boleh (a) DICT tunggal instrumen->string 16-step (LEGACY: di-tile identik ke semua bar section) atau (b) LIST of dict, satu pattern per bar, panjang list HARUS == bars. 'x' = hit, 'X' = accent, 'g' = ghost, '.' = rest; 16 chars = satu bar di 16 steps. Field opsional: 'phrase_velocity' (list float per bar, panjang == bars, dikali ke velocity semua hit bar itu -- bentuk frase, bukan jitter) dan top-level 'timing' (map role->offset_ms, digeser deterministik ke onset). Urutan velocity: base -> accent X/ghost g -> phrase_velocity -> humanize_velocity kecil (polish terakhir, bukan sumber variasi). Untuk section > 2 bar WAJIB hierarchy: base groove 2-bar + variation sekitar bar-4 + transition di bar terakhir; JANGAN semua bar identik (grid_to_midi.py akan warning). tempo_bpm SELALU tempo musikal nyata (match Q: ABC). beats_per_bar = numerator*4/denominator dari M: ABC. Hapus _comment ini di file final.",
  "title": "Untitled drums",
  "tempo_bpm": 90,
  "beats_per_bar": 4,
  "steps_per_bar": 16,
  "swing": 0.57,
  "humanize_velocity": 6,
  "gm_map": { "kick": 36, "snare": 38, "rimshot": 37, "chh": 42, "ohh": 46, "ride": 51 },
  "base_velocity": { "kick": 92, "snare": 80, "rimshot": 60, "chh": 55, "ohh": 62, "ride": 58 },
  "timing": { "kick": 0, "snare": 15, "rimshot": 25, "chh": -3 },
  "sections": [
    {
      "label": "Intro (2 bar, bentuk dict legacy tetap valid)",
      "bars": 2,
      "pattern": {
        "kick": "x.......x.......",
        "chh":  "x...x...x...x..."
      }
    },
    {
      "label": "A building (4 bar, list per-bar + phrase_velocity): base 2-bar (bar 1-2), restate (bar 3), transition (bar 4)",
      "bars": 4,
      "phrase_velocity": [0.95, 1.0, 1.0, 1.08],
      "pattern": [
        { "kick": "x..x....x.x.....", "rimshot": "....x.......x...", "chh": "x.x.x.x.x.x.x.x." },
        { "kick": "x..x....x.x.....", "rimshot": "....x.......x..g", "chh": "x.x.x.x.x.x.x.x." },
        { "kick": "x..x....x.x.....", "rimshot": "....x.......x...", "chh": "x.x.x.x.x.x.x.x." },
        { "kick": "x..x..x.x.x...x.", "snare": "....x.......x.X.", "chh": "x.x.x.x.x.x.x.xX", "ohh": "..............x." }
      ]
    },
    {
      "label": "B peak (4 bar, list per-bar): ONE-OFF imperfection = kick downbeat sengaja hilang sekali di bar 3",
      "bars": 4,
      "pattern": [
        { "kick": "x..x..x.x.x...x.", "snare": "....x...x...x.x.", "chh": "x.x.x.x.x.x.x.x.", "ride": "x...x...x...x..." },
        { "kick": "x..x..x.x.x...x.", "snare": "....x...x...x.x.", "chh": "x.x.x.x.x.x.x.x.", "ride": "x...x...x...x..." },
        { "kick": "...x..x.x.x...x.", "snare": "....x...x...x.x.", "chh": "x.x.x.x.x.x.x.x.", "ride": "x...x...x...x..." },
        { "kick": "x..x..x.x.x..xx.", "snare": "....x...x...x.X.", "chh": "x.x.x.x.x.x.x.x.", "ride": "x...x...x...x..x" }
      ]
    },
    {
      "label": "Outro (2 bar, bentuk dict legacy): fades",
      "bars": 2,
      "pattern": {
        "kick":    "x...............",
        "rimshot": "....x..........."
      }
    }
  ]
}
```

- [ ] **Step 2: Verifikasi template baru me-render tanpa error dan tanpa warning lint palsu**

Run: `cd skills/midi-orchestration/scripts && uv run --with pretty_midi python grid_to_midi.py ../assets/drum-grid-template.json /tmp/tmpl.mid`
Expected: `wrote /tmp/tmpl.mid: 167 drum hits across 12 bars`, **tanpa** baris `WARNING:` di stderr.

- [ ] **Step 3: Perbarui `midi-conversion.md` — format v2 + urutan velocity**

Di `skills/midi-orchestration/references/midi-conversion.md`, ganti seluruh bullet block di bawah heading `## How the drum converter works` (dari baris `` `grid_to_midi.py <grid.json> <out.mid>`: `` sampai bullet `- GM map and base velocities are set in the grid JSON, so you can tune the kit per song.`) dengan:

```markdown
`grid_to_midi.py <grid.json> <out.mid>`:

- Reads a step-grid (rows = drums, `x` = normal hit, `X` = accent, `g` = ghost, `.` = rest) and writes GM percussion on channel 10 (`is_drum=True`).
- **`tempo_bpm`**: the real musical tempo — always match this to the ABC's `Q:` field (quarter-note BPM). Never fudge this to compensate for bar length; use `beats_per_bar` for that instead.
- **`beats_per_bar`**: the bar length in quarter-note-equivalents (`numerator * 4/denominator` from the ABC's `M:` field) — 4 for 4/4, 3 for 3/4, 3.5 for 7/8. Defaults to 4 if omitted, so plain 4/4 grids don't need to set it. Set this explicitly for any non-4/4 meter so `sec_per_bar` comes out correct without touching `tempo_bpm`.
- **`steps_per_bar`**: how many grid columns make up one bar (independent of `beats_per_bar` — e.g. a 7/8 bar at eighth-note subdivision uses `steps_per_bar: 7`).
- **`section.pattern` — two forms (v2, backward compatible):**
  - **(a) Legacy dict** — one dict `role -> "16-step string"`. The pattern is **tiled identically** across every bar of the section. This is the v1 behaviour and renders bit-for-bit as before.
  - **(b) Per-bar list** — a `list` of dicts, one pattern per bar in order (bar 1, bar 2, …). The list length **must equal `section["bars"]`**; a mismatch raises a clear `ValueError` (no silent truncate/pad). Use this for a base groove + variation + transition inside one section.
- **`phrase_velocity`** (optional, per section): a list of float multipliers, one per bar (length must equal `section["bars"]`), multiplied into the velocity of **every** hit in that bar. This shapes velocity as a **phrase** (a directed rise/fall across bars), not per-hit jitter. Absent → `1.0` for every bar (no-op; output identical to v1).
- **`timing`** (optional, top-level): a map `role -> offset_ms` (e.g. `{"kick": 0, "snare": 15, "rimshot": 25, "chh": -3}`), added **deterministically** (not random) to each onset of that role. ms is converted to seconds; the onset is clamped so it never goes negative (`max(0, t)`). This realizes **relational per-role timing** (kick as anchor, snare/rimshot laid-back, hi-hat slightly ahead) — see `../../groove-rhythm/references/groove-profiles.md` for ready-to-paste values per profile. Absent → v1 behaviour (no per-role offset).
- **Swing**: off-beat (odd-index) 16th steps are nudged later by `(swing - 0.5)` of a step, giving the laid-back feel. 0.5 = straight; ~0.56–0.58 = typical lofi/funk swing.
- **Accent/ghost velocity**: `X` (accent) renders at ~1.2x the voice's `base_velocity`; `g` (ghost) renders at ~0.45x.
- **`humanize_velocity`**: a small ±jitter applied **last** — after accent/ghost and after `phrase_velocity`. It is polish, **not** the main source of variation, so keep it small (single digits); variation should come from per-bar patterns and `phrase_velocity`, not from cranking this up.
- **Velocity application order (explicit):** **base velocity → accent `X` / ghost `g` → `phrase_velocity` → small `humanize_velocity` jitter**, then clamped to 1–127.
- **Anti-tile lint**: for any section with `bars > 2` whose every bar is identical (a legacy dict, or a list of equal dicts), `grid_to_midi.py` prints an informational `WARNING:` to stderr. It never changes the rendered MIDI and never fails the run — it flags a section that should carry a base+variation+transition per `../../jazz-composition/references/level-09-drum.md`.
- GM map and base velocities are set in the grid JSON, so you can tune the kit per song.
```

- [ ] **Step 4: Perbarui `level-09-drum.md` — hierarchy wajib, larangan identik, one-off imperfection**

Di `skills/jazz-composition/references/level-09-drum.md`, ganti blok:

```markdown
Output level ini
Drum roadmap, bukan notasi penuh pada tahap awal.
```

menjadi:

```markdown
Output level ini
Drum roadmap, bukan notasi penuh pada tahap awal.

## Aturan komposisi drum (v2 — dibaca oleh pembuat `drums.json`)

Ini aturan doktrin, bukan enforced di kode (kode hanya memberi warning). Melanggarnya adalah salah satu sumber utama rasa "generative loop".

- **Hierarchy wajib untuk section > 2 bar.** Susun dengan `pattern` berupa **list per-bar** (bukan satu dict yang di-tile):
  - **base groove 2-bar** — bar ganjil & genap boleh identik satu sama lain dalam pasangannya (base groove yang bernapas dua bar);
  - **variation** di sekitar bar ke-4 (bukan pengulangan mentah base);
  - **transition variation** di bar terakhir section (fill/lift menuju section berikutnya).
- **Minimal satu one-off imperfection di seluruh lagu** — satu kejadian sekali-saja yang disengaja (bukan berulang): ghost note tunggal setelah frase lead, kick hilang di satu downbeat, atau open-hat sekali. Tandai di `label` bar-nya supaya jelas ini sengaja, bukan error.
- **Dilarang: section > 2 bar dengan semua bar identik.** `grid_to_midi.py` memberi `WARNING` pada kasus ini (lihat `../../midi-orchestration/references/midi-conversion.md`), tapi warning saja tidak cukup — perbaiki jadi base+variation+transition sebelum lanjut.
- **`phrase_velocity`** dipakai untuk membentuk arc dinamika per bar (naik ke transition, turun saat reda) — bukan mengandalkan `humanize_velocity` acak. `humanize_velocity` dijaga kecil (single digit): perannya polish, bukan sumber variasi.
- **`timing`** relasional per-role dipilih dari profil di `../../groove-rhythm/references/groove-profiles.md` (mis. `neo-soul-core`) — salin map-nya, jangan menurunkan angka tick ad hoc.
```

- [ ] **Step 5: Perbarui `groove-profiles.md` — map `timing` neo-soul-core siap-pakai**

Di `skills/groove-rhythm/references/groove-profiles.md`, tepat **setelah** blok tabel "Gate (note-off / sustain ratio ...)" (baris `| Lead | ~0.86–0.96 | ...` yang mengakhiri tabel gate, sebelum heading `## How this maps to this package's artifacts`), sisipkan:

```markdown

**Ready-to-paste `drums.json` `timing` map (ms offsets, derived from the tick table above).** Convert the tick ranges to ms at 96 BPM/960 PPQ and round to a single per-role value the drum grid can use directly (kick as anchor at 0; snare/rimshot laid-back behind the grid; hi-hat a touch ahead). The composing brain copies this block into `drums.json` under top-level `timing` — do not re-derive per song:

```json
"timing": { "kick": 0, "snare": 15, "rimshot": 25, "chh": -3 }
```

`grid_to_midi.py` applies these deterministically per role (see `../../midi-orchestration/references/midi-conversion.md`, `timing` field). Ride/open-hat, if used, sit near the hi-hat/anchor range; add them only when the kit uses them, keeping kick at 0 as the reference.
```

- [ ] **Step 6: Commit**

```bash
git add skills/midi-orchestration/assets/drum-grid-template.json skills/midi-orchestration/references/midi-conversion.md skills/jazz-composition/references/level-09-drum.md skills/groove-rhythm/references/groove-profiles.md
git commit -m "docs: aset & dokumen drum v2 -- template hierarchy, urutan velocity, timing neo-soul-core"
```

---

## Task 4: Protokol kandidat→seleksi (Level 1-4)

**Files:**
- Create: `skills/jazz-composition/references/candidate-selection-protocol.md`
- Modify: `skills/jazz-composition/SKILL.md` (Tahap 1-5 workflow + catatan Reviewer L2)
- Modify: `skills/jazz-composition/references/level-01-konsep.md`
- Modify: `skills/jazz-composition/references/level-02-arsitektur.md`
- Modify: `skills/jazz-composition/references/level-03-harmoni.md`
- Modify: `skills/jazz-composition/references/level-04-melodi.md`
- Modify: `skills/jazz-composition/references/run-folder-protocol.md`

**Interfaces:**
- Consumes: pola "Reviewer segar (L2)" yang sudah ada di `SKILL.md` (diperluas ke titik seleksi).
- Produces: artefak run-folder baru `NN-<level>-candidates.md` untuk Level 1-4 (dirujuk Task 4's run-folder edit).

- [ ] **Step 1: Buat `candidate-selection-protocol.md`**

Buat `skills/jazz-composition/references/candidate-selection-protocol.md`:

```markdown
# Protokol kandidat → seleksi (Level 1-4)

Mengganti pola **generate-then-defend** (menulis satu artefak lalu membelanya) dengan **generate-kandidat → seleksi-independen**. Berlaku **hanya** di 4 level ber-leverage tinggi: Level 1 (konsep), Level 2 (bentuk), Level 3 (harmoni), Level 4 (motif/melodi). Level lain tetap single-shot — ini sengaja, untuk menghindari ledakan paperwork 14 level × 3 kandidat.

## Aturan generasi per level

- **Level 1 — Konsep.** Wajib menulis field **aesthetic thesis**: 1 kalimat ide musikal spesifik yang bisa **didengar**, bukan daftar atribut genre. Contoh baik: "satu nada yang awalnya terasa salah tak pernah dihilangkan; di akhir, harmoni di bawahnya berubah sehingga nada yang sama terasa diterima." Plus **2 konsep kandidat berbeda secara struktural** (ini yang akhirnya memenuhi tuntutan rubrik `vibes-mood` "minimal dua konsep berbeda secara struktural").
- **Level 2 — Bentuk.** **≥2 alternatif bentuk** sebelum memilih (mis. through-composed vs. return-with-recontext), masing-masing 2-3 kalimat + risiko statis/simetrisnya.
- **Level 3 — Harmoni.** Progresi utama + **1 alternatif lebih sederhana** + **1 alternatif lebih berani**, masing-masing dengan **exact chord symbols per bar**.
- **Level 4 — Melodi.** **3 kandidat motif**, masing-masing wajib ditulis sebagai **notasi ABC 1-2 bar** + fakta objektif: jumlah pitch aktual (rest **bukan** pitch), interval aktual antar nada berurutan (semitone + nama interval), dan relasi tiap nada ke chord (chord-tone / tension / outside). Jalankan `../../abc-notation/scripts/notation_facts.py` pada tiap kandidat untuk mendapat fakta ini — jangan mengklaim dari ingatan.

## Protokol seleksi (anti self-justification)

1. Generator menghasilkan kandidat sebagai **material telanjang**: notasi/struktur + fakta objektif + **maksimal 1 kalimat intent**. **Dilarang** menulis pembelaan/rasionalisasi per kandidat di tahap ini.
2. Seleksi dilakukan oleh **subagent segar** (selector) yang menerima **hanya**: brief, aesthetic thesis, material kandidat, dan fakta objektif. Selector **tidak** menerima preferensi/urutan favorit generator — pola yang sama dengan "Reviewer segar (L2)" di `../SKILL.md`, diperluas ke titik seleksi (bukan hanya penilaian akhir).
3. Selector memilih **1 pemenang** + alasan berbasis **efek yang akan terdengar** (bukan nama teori), dan boleh menyarankan **graft** — mengambil elemen dari kandidat lain ke pemenang.
4. Hasil seleksi dicatat di run folder:
   - kandidat ditulis ke artefak `NN-<level>-candidates.md` (`01-konsep-candidates.md`, `02-arsitektur-candidates.md`, `03-harmoni-candidates.md`, `04-melodi-candidates.md`);
   - verdict selector ditulis di **bagian akhir artefak yang sama** (bukan file terpisah);
   - artefak utama level itu (`01-brief.md`, `02-form.md`, `03-harmony.md`, `04-melody.abc`) memakai **pemenang seleksi**, bukan rata-rata atau gabungan tanpa keputusan eksplisit.
5. **Fallback tanpa subagent** (mis. composer pack di browser AI tanpa Claude Code): self-selection oleh agent yang sama **diizinkan**, **tapi** wajib **pre-mortem** — tulis 1 kelemahan konkret tiap kandidat **sebelum** memilih, dan kalimat pemilihan pemenang harus **secara eksplisit** mereferensikan kelemahan itu (mis. "dipilih kandidat B meski kelemahannya X, karena kelemahan A dan C lebih berat untuk brief ini").

## Kontrak artefak ramping (`*-candidates.md`)

Khusus keempat artefak `*-candidates.md` — **bukan** kontrak 11-field penuh artefak level lain:

| Field | Isi |
|---|---|
| Objective | Efek audible yang dikejar (1-2 kalimat) |
| Immutable constraints | Batasan dari brief yang tidak boleh dilanggar kandidat manapun |
| Assumptions | Asumsi yang diambil generator saat brief tidak eksplisit |
| Kandidat | Material telanjang tiap kandidat (lihat aturan per level di atas) |
| Selected + alasan | Pemenang + alasan berbasis efek terdengar (bukan nama teori) |
| Exact artifact | Rujukan ke artefak utama level ini yang memakai pemenang |
| Unresolved/confidence | Hal yang masih terbuka + tingkat keyakinan seleksi |
```

- [ ] **Step 2: `SKILL.md` — sisipkan catatan kandidat→seleksi di workflow (setelah intro Tahap)**

Di `skills/jazz-composition/SKILL.md`, ganti baris:

```markdown
di `references/run-folder-protocol.md`.

**Tahap 1 — Buat brief** → artefak `01-brief.md`
```

menjadi:

```markdown
di `references/run-folder-protocol.md`.

> **Level 1-4 memakai protokol kandidat→seleksi.** Tahap 1 (konsep), 2 (bentuk),
> 3 (harmoni), dan 5 (motif/melodi) **tidak** langsung menulis satu artefak lalu
> membelanya. Masing-masing menghasilkan **beberapa kandidat sebagai material
> telanjang** dulu, lalu **subagent selector segar** memilih pemenang (fallback:
> self-selection + pre-mortem). Kandidat + verdict ditulis ke
> `NN-<level>-candidates.md`; artefak utama (`01-brief.md`, `02-form.md`,
> `03-harmony.md`, `04-melody.abc`) memakai pemenangnya. Prosedur lengkap +
> kontrak artefak ramping: `references/candidate-selection-protocol.md`. Baca itu
> sebelum mengerjakan Tahap 1-5.

**Tahap 1 — Buat brief** → artefak `01-brief.md`
```

- [ ] **Step 3: `SKILL.md` — catatan di "Reviewer segar (L2)" bahwa Level 1-4 lewat seleksi lebih dulu**

Di `skills/jazz-composition/SKILL.md`, ganti:

```markdown
Self-grading oleh agent/percakapan yang sama yang membuat artefak itu
**dilarang**: agent yang baru saja menulis `04-melody.abc` tidak boleh
juga yang mengisi skor rubriknya sendiri.
```

menjadi:

```markdown
Self-grading oleh agent/percakapan yang sama yang membuat artefak itu
**dilarang**: agent yang baru saja menulis `04-melody.abc` tidak boleh
juga yang mengisi skor rubriknya sendiri.

Untuk **Level 1-4**, prinsip "reviewer/selektor segar" ini **sudah dipakai lebih
awal**, di titik seleksi kandidat (lihat
`references/candidate-selection-protocol.md`): sebelum L2 menilai artefak akhir,
pemenang tiap level dipilih oleh subagent selector segar dari beberapa kandidat.
Jadi untuk Level 1-4, L2 menilai artefak yang **sudah** lolos seleksi
independen, bukan artefak single-shot.
```

- [ ] **Step 4: `level-01-konsep.md` — tambah requirement aesthetic thesis + 2 kandidat**

Di `skills/jazz-composition/references/level-01-konsep.md`, ganti:

```markdown
## Gate — ask, don't guess

- Jika field wajib artefak level ini belum diputuskan brief/level sebelumnya — **tanya, jangan menebak.**
```

menjadi:

```markdown
## Kandidat & seleksi (Level 1)

Level ini memakai protokol kandidat→seleksi (`candidate-selection-protocol.md`). Tambahan wajib pada output level ini:

- **Aesthetic thesis** — 1 kalimat ide musikal spesifik yang bisa **didengar** (bukan daftar atribut genre). Contoh: "satu nada yang awalnya terasa salah tak pernah dihilangkan; di akhir, harmoni di bawahnya berubah sehingga nada itu terasa diterima."
- **2 konsep kandidat berbeda secara struktural** ditulis sebagai material telanjang (≤1 kalimat intent per kandidat, tanpa pembelaan). Ini yang memenuhi tuntutan rubrik `vibes-mood` "minimal dua konsep berbeda secara struktural".
- Kandidat + verdict selector ditulis ke `01-konsep-candidates.md`; `01-brief.md` memakai pemenang.

## Gate — ask, don't guess

- Jika field wajib artefak level ini belum diputuskan brief/level sebelumnya — **tanya, jangan menebak.**
```

- [ ] **Step 5: `level-02-arsitektur.md` — tambah requirement ≥2 alternatif bentuk**

Di `skills/jazz-composition/references/level-02-arsitektur.md`, ganti:

```markdown
## Gate — ask, don't guess

- Jika field wajib artefak level ini belum diputuskan brief/level sebelumnya — **tanya, jangan menebak.**
```

menjadi:

```markdown
## Kandidat & seleksi (Level 2)

Level ini memakai protokol kandidat→seleksi (`candidate-selection-protocol.md`):

- Tulis **≥2 alternatif bentuk** sebelum memilih (mis. through-composed vs. return-with-recontext), masing-masing 2-3 kalimat + **risiko statis/simetris**-nya, sebagai material telanjang.
- Kandidat + verdict selector ditulis ke `02-arsitektur-candidates.md`; `02-form.md` memakai pemenang.

## Gate — ask, don't guess

- Jika field wajib artefak level ini belum diputuskan brief/level sebelumnya — **tanya, jangan menebak.**
```

- [ ] **Step 6: `level-03-harmoni.md` — tambah requirement progresi utama + 2 alternatif**

Di `skills/jazz-composition/references/level-03-harmoni.md`, ganti:

```markdown
## Gate — ask, don't guess

- "Chorus tinggal ulang verse aja — kan emang loop, gak masalah." (alasan yang ditolak, lihat RED-FLAGS.md) → Arc dramatis yang tidak pernah berubah bukan arc. Verse dan chorus (atau bagian berulang lain) butuh perkembangan yang bisa didengar — register, density, harmoni, atau interaksi — bukan restatement identik.
- Jika field wajib artefak level ini belum diputuskan brief/level sebelumnya — **tanya, jangan menebak.**
```

menjadi:

```markdown
## Kandidat & seleksi (Level 3)

Level ini memakai protokol kandidat→seleksi (`candidate-selection-protocol.md`):

- Tulis **progresi utama** + **1 alternatif lebih sederhana** + **1 alternatif lebih berani**, masing-masing dengan **exact chord symbols per bar**, sebagai material telanjang.
- Kandidat + verdict selector ditulis ke `03-harmoni-candidates.md`; `03-harmony.md` memakai pemenang.

## Gate — ask, don't guess

- "Chorus tinggal ulang verse aja — kan emang loop, gak masalah." (alasan yang ditolak, lihat RED-FLAGS.md) → Arc dramatis yang tidak pernah berubah bukan arc. Verse dan chorus (atau bagian berulang lain) butuh perkembangan yang bisa didengar — register, density, harmoni, atau interaksi — bukan restatement identik.
- Jika field wajib artefak level ini belum diputuskan brief/level sebelumnya — **tanya, jangan menebak.**
```

- [ ] **Step 7: `level-04-melodi.md` — tambah requirement 3 kandidat motif + fakta objektif**

Di `skills/jazz-composition/references/level-04-melodi.md`, ganti:

```markdown
## Gate — ask, don't guess

- "Chorus tinggal ulang verse aja — kan emang loop, gak masalah." (alasan yang ditolak, lihat RED-FLAGS.md) → Arc dramatis yang tidak pernah berubah bukan arc. Verse dan chorus (atau bagian berulang lain) butuh perkembangan yang bisa didengar — register, density, harmoni, atau interaksi — bukan restatement identik.
- Jika field wajib artefak level ini belum diputuskan brief/level sebelumnya — **tanya, jangan menebak.**
```

menjadi:

```markdown
## Kandidat & seleksi (Level 4)

Level ini memakai protokol kandidat→seleksi (`candidate-selection-protocol.md`):

- Tulis **3 kandidat motif**, masing-masing sebagai **notasi ABC 1-2 bar** + fakta objektif: jumlah pitch aktual (rest **bukan** pitch), interval aktual antar nada berurutan (semitone + nama interval), relasi tiap nada ke chord (chord-tone / tension / outside).
- Fakta objektif itu **wajib** diambil dari `../../abc-notation/scripts/notation_facts.py` pada tiap kandidat (jangan mengklaim dari ingatan) — lihat juga bagian "Cek fakta notasi" di bawah.
- Kandidat + verdict selector ditulis ke `04-melodi-candidates.md`; `04-melody.abc` memakai pemenang.

## Gate — ask, don't guess

- "Chorus tinggal ulang verse aja — kan emang loop, gak masalah." (alasan yang ditolak, lihat RED-FLAGS.md) → Arc dramatis yang tidak pernah berubah bukan arc. Verse dan chorus (atau bagian berulang lain) butuh perkembangan yang bisa didengar — register, density, harmoni, atau interaksi — bukan restatement identik.
- Jika field wajib artefak level ini belum diputuskan brief/level sebelumnya — **tanya, jangan menebak.**
```

- [ ] **Step 8: `run-folder-protocol.md` — tambah artefak `NN-<level>-candidates.md`**

Di `skills/jazz-composition/references/run-folder-protocol.md`, ganti blok pohon folder:

```markdown
├── 01-brief.md
├── 02-form.md
├── 03-harmony.md
├── 04-melody.abc          (catatan desain, lihat catatan di bawah; atau .md untuk artefak non-notasi)
```

menjadi:

```markdown
├── 01-konsep-candidates.md   (hanya Level 1-4: material kandidat + verdict selector)
├── 01-brief.md
├── 02-arsitektur-candidates.md
├── 02-form.md
├── 03-harmoni-candidates.md
├── 03-harmony.md
├── 04-melodi-candidates.md
├── 04-melody.abc          (catatan desain, lihat catatan di bawah; atau .md untuk artefak non-notasi)
```

Lalu, tepat setelah paragraf yang berakhir `...artefak level N selalu ditulis sebelum\nlevel N+1 dimulai.`, sisipkan paragraf baru:

```markdown
### Artefak `NN-<level>-candidates.md` (hanya Level 1-4)

Level 1-4 memakai protokol kandidat→seleksi (`candidate-selection-protocol.md`),
jadi selain artefak utama bernomor, tiap level itu juga menulis satu
`NN-<level>-candidates.md` (`01-konsep-`, `02-arsitektur-`, `03-harmoni-`,
`04-melodi-`). File ini memuat material kandidat telanjang + verdict selector di
bagian akhirnya, mengikuti kontrak artefak ramping (7 field) di
`candidate-selection-protocol.md` — **bukan** kontrak 11-field artefak lain.
Level 5-14 **tidak** punya artefak `-candidates.md` (single-shot).
```

- [ ] **Step 9: Verifikasi konsistensi tautan (tanpa test kode — dokumen)**

Run: `cd skills/jazz-composition && grep -rl "candidate-selection-protocol.md" references/ SKILL.md`
Expected: mencantumkan `SKILL.md`, `references/level-01-konsep.md`, `references/level-02-arsitektur.md`, `references/level-03-harmoni.md`, `references/level-04-melodi.md`, `references/run-folder-protocol.md`, dan file protokol itu sendiri tidak akan muncul (ia bukan yang merujuk). Pastikan file `references/candidate-selection-protocol.md` benar-benar ada:
Run: `ls skills/jazz-composition/references/candidate-selection-protocol.md`
Expected: path tercetak (file ada).

- [ ] **Step 10: Commit**

```bash
git add skills/jazz-composition/references/candidate-selection-protocol.md skills/jazz-composition/SKILL.md skills/jazz-composition/references/level-01-konsep.md skills/jazz-composition/references/level-02-arsitektur.md skills/jazz-composition/references/level-03-harmoni.md skills/jazz-composition/references/level-04-melodi.md skills/jazz-composition/references/run-folder-protocol.md
git commit -m "feat: protokol kandidat->seleksi Level 1-4 + artefak candidates di run folder"
```

---

## Task 5: Wiring gate klaim-vs-notasi (Level 3/4/7 + Reviewer L2 + RED-FLAGS)

**Files:**
- Modify: `skills/jazz-composition/references/level-03-harmoni.md`
- Modify: `skills/jazz-composition/references/level-04-melodi.md`
- Modify: `skills/jazz-composition/references/level-07-comping-voicing.md`
- Modify: `skills/jazz-composition/SKILL.md` (Reviewer L2)
- Modify: `skills/RED-FLAGS.md`

**Interfaces:**
- Consumes: `notation_facts.py` (Task 1) — path `skills/abc-notation/scripts/notation_facts.py`; command via `uv run --with music21 --with pretty_midi python notation_facts.py <file.abc> [--voice <id>]`.

**Catatan urutan:** Task 5 menyisipkan section baru **sebelum** `## Modul pendalaman`, sedangkan Task 4 menyisipkan section-nya **sebelum** `## Gate — ask, don't guess`. Anchor berbeda → tidak bertabrakan meski keduanya menyentuh `level-03` dan `level-04`. Jalankan Task 5 setelah Task 4.

- [ ] **Step 1: `level-03-harmoni.md` — tambah section "Cek fakta notasi" sebelum "## Modul pendalaman"**

Di `skills/jazz-composition/references/level-03-harmoni.md`, ganti:

```markdown
## Modul pendalaman

- ../../harmony/SKILL.md
```

menjadi:

```markdown
## Cek fakta notasi (wajib sebelum lanjut ke Level 4)

Sebelum artefak `03-harmony.md` dianggap selesai:

1. Tulis progresi terpilih ke satu file ABC kecil (chord symbols per bar di `V:1`), lalu jalankan:
   `cd skills/abc-notation/scripts && uv run --with music21 --with pretty_midi python notation_facts.py <file.abc>`
2. **Lampirkan** output yang relevan (`chord-vs-key` per bar) ke `03-harmony.md`.
3. **Cocokkan tiap label teori** di artefak dengan fakta script — khususnya klaim `modal interchange`/`borrowed`. Contoh nyata dari run lama: `Abmaj7`/`Ebmaj7` dilabeli "borrowed" padahal `notation_facts.py` melaporkannya **`diatonik`** di key minor. Ketidakcocokan = **revisi artefak dulu**, jangan lanjut.
4. Chord yang dilaporkan `unparsed` (simbol tak dikenal script) diperiksa manual — jangan diasumsikan benar hanya karena script tidak bisa menilainya.

## Modul pendalaman

- ../../harmony/SKILL.md
```

- [ ] **Step 2: `level-04-melodi.md` — tambah section "Cek fakta notasi" sebelum "## Modul pendalaman"**

Di `skills/jazz-composition/references/level-04-melodi.md`, ganti:

```markdown
## Modul pendalaman

- ../../melody-design/SKILL.md
- ../../advanced-melody/SKILL.md (untuk tahap 7-8: chromatic vocabulary & outside playing)
```

menjadi:

```markdown
## Cek fakta notasi (wajib sebelum lanjut)

Sebelum artefak `04-melody.abc` (dan tiap kandidat motif di `04-melodi-candidates.md`) dianggap selesai:

1. Jalankan pada notasi motif/melodi:
   `cd skills/abc-notation/scripts && uv run --with music21 --with pretty_midi python notation_facts.py <file.abc> --voice <id>`
2. **Lampirkan** output relevan (jumlah pitch, interval antar nada, klasifikasi chord-tone/tension/outside) ke artefak.
3. **Cocokkan tiap label teori** dengan fakta script. Contoh nyata dari run lama yang harus tertangkap: motif diklaim "4-not" padahal `notation_facts.py` hanya melaporkan **3 pitch** (rest bukan pitch); arpeggio chord-tone dilabeli "outside" padahal script melaporkannya `chord-tone`. Ketidakcocokan = **revisi dulu**, jangan lanjut.
4. Nada yang jatuh di bar dengan chord `unparsed` diperiksa manual.

## Modul pendalaman

- ../../melody-design/SKILL.md
- ../../advanced-melody/SKILL.md (untuk tahap 7-8: chromatic vocabulary & outside playing)
```

- [ ] **Step 3: `level-07-comping-voicing.md` — tambah section "Cek fakta notasi" sebelum "## Modul pendalaman"**

Di `skills/jazz-composition/references/level-07-comping-voicing.md`, ganti:

```markdown
## Modul pendalaman

- ../../arrangement/SKILL.md
```

menjadi:

```markdown
## Cek fakta notasi (wajib sebelum lanjut)

Sebelum comping chart / voicing dianggap selesai:

1. Tulis voicing per bar sebagai bracket chord ABC (`[..]`) di voice keys, lalu jalankan:
   `cd skills/abc-notation/scripts && uv run --with music21 --with pretty_midi python notation_facts.py <file.abc> --voice <keys-id>`
2. **Lampirkan** output `top-note` per bar + daftar nada bawah→atas ke artefak.
3. **Cocokkan klaim voice-leading top-note** dengan fakta script. Contoh nyata dari run lama: klaim "top note bergerak G→F→E" padahal voicing yang benar-benar tertulis punya top-note lain. Ketidakcocokan = **revisi voicing dulu**, jangan lanjut. (Ingat: `notation_facts.py` melaporkan **pitch tertinggi** sebagai top note, sesuai oktaf ABC — verifikasi voicing ditulis di oktaf yang dimaksud.)

## Modul pendalaman

- ../../arrangement/SKILL.md
```

- [ ] **Step 4: `SKILL.md` — Reviewer L2 diberi output `notation_facts.py` untuk Level 3/4/7**

Di `skills/jazz-composition/SKILL.md`, ganti:

```markdown
4. Skor rubrik tinggi tetap lantai, bukan langit-langit — lanjut ke
   `RED-FLAGS.md` dan (untuk `output.mid` final) L3 telinga manusia di
   `references/human-ear-protocol.md` sebelum piece dianggap selesai.
```

menjadi:

```markdown
4. Skor rubrik tinggi tetap lantai, bukan langit-langit — lanjut ke
   `RED-FLAGS.md` dan (untuk `output.mid` final) L3 telinga manusia di
   `references/human-ear-protocol.md` sebelum piece dianggap selesai.

Untuk **Level 3, 4, dan 7**, subagent reviewer juga diberi **output
`notation_facts.py` yang sama** yang sudah dilampirkan generator ke artefak
(bukan hanya artefak + `rubric.md`). Ini supaya penilaian rubrik bisa
**memverifikasi klaim teori terhadap fakta notasi** (interval, chord-tone vs.
outside, borrowed vs. diatonik, klaim top-note/voice-leading), bukan sekadar
membaca prosa. Reviewer boleh menjalankan ulang
`skills/abc-notation/scripts/notation_facts.py` pada notasi artefak bila output
yang dilampirkan diragukan.
```

- [ ] **Step 5: `RED-FLAGS.md` — baris baru "label teori tanpa cek fakta notasi"**

Di `skills/RED-FLAGS.md`, ganti baris terakhir tabel:

```markdown
| "The rubric score is high, so the piece must sound good." | The per-module rubrics score craft and theory-consistency from the notation and plan — they cannot hear timbre, groove feel, or mix. A high score is a floor (nothing is broken or thin), not a ceiling (nobody has confirmed it's enjoyable). Ear-check is still required before calling a piece finished. | skills/*/references/rubric.md; skills/jazz-composition/references/scorecard-template.md; skills/jazz-composition/references/human-ear-protocol.md |
```

menjadi (tambah satu baris setelahnya):

```markdown
| "The rubric score is high, so the piece must sound good." | The per-module rubrics score craft and theory-consistency from the notation and plan — they cannot hear timbre, groove feel, or mix. A high score is a floor (nothing is broken or thin), not a ceiling (nobody has confirmed it's enjoyable). Ear-check is still required before calling a piece finished. | skills/*/references/rubric.md; skills/jazz-composition/references/scorecard-template.md; skills/jazz-composition/references/human-ear-protocol.md |
| "Motif ini 4-not, arpeggio-nya outside, chord-nya borrowed — sesuai yang kutulis." | Label teori di prosa sering tak cocok notasi aktual: motif "4-not" yang nyatanya 3 pitch (rest bukan pitch), arpeggio chord-tone yang dilabeli "outside", chord diatonik yang disebut "borrowed", klaim top-note yang beda dari voicing tertulis. Jangan percaya label sebelum dicek terhadap fakta notasi yang sebenarnya berbunyi. | skills/abc-notation/scripts/notation_facts.py (jalankan pada ABC-nya; gate wajib di DoD Level 3/4/7) |
```

- [ ] **Step 6: Verifikasi tautan `notation_facts.py` dirujuk di semua tempat wajib**

Run: `grep -rl "notation_facts.py" skills/jazz-composition/references/level-03-harmoni.md skills/jazz-composition/references/level-04-melodi.md skills/jazz-composition/references/level-07-comping-voicing.md skills/jazz-composition/SKILL.md skills/RED-FLAGS.md`
Expected: kelima path tercetak.

- [ ] **Step 7: Commit**

```bash
git add skills/jazz-composition/references/level-03-harmoni.md skills/jazz-composition/references/level-04-melodi.md skills/jazz-composition/references/level-07-comping-voicing.md skills/jazz-composition/SKILL.md skills/RED-FLAGS.md
git commit -m "feat: gate klaim-vs-notasi di DoD Level 3/4/7 + reviewer L2 + RED-FLAGS"
```

---

## Ringkasan urutan eksekusi & dependensi

1. **Task 1** (notation_facts + split_voices) — mandiri; menghasilkan script yang dirujuk Task 4 & 5.
2. **Task 2** (grid v2) — mandiri; harus lulus regresi bit-identik sebelum commit.
3. **Task 3** (aset & dokumen drum) — bergantung format v2 dari Task 2.
4. **Task 4** (kandidat→seleksi) — mandiri secara kode; menyisipkan section sebelum `## Gate`.
5. **Task 5** (gate klaim-vs-notasi) — jalankan **setelah** Task 1 (butuh script) & Task 4 (anchor `## Modul pendalaman` masih ada; section disisipkan sebelum anchor itu).

Setelah kelima task hijau, orkestrator menjalankan acceptance #3 (run komposisi baru end-to-end + L3 telinga) — **di luar plan ini**.

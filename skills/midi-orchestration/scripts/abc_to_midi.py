#!/usr/bin/env python3
"""Render multi-voice ABC to multi-track MIDI, one track per V: voice.

Fixes: (1) strip ABC chord-SYMBOL annotations ("Bbm9" etc.) so they are NOT
sounded as notes; (2) isolate each voice into its own stub so tracks don't leak.
"""
import re, sys, tempfile
import pretty_midi
from music21 import converter, harmony

# Selaras registry instrumen engine daw_generative (src/instruments/
# registry.js — lihat ../references/engine-export.md): keyword yang sama
# menghasilkan nomor GM yang sama supaya preview MIDI Tool 1 dan WAV engine
# tidak diam-diam beda timbre. Keyword majemuk (guitar-clean, synth-lead)
# HARUS di depan keyword substring-nya karena program_for mencocokkan
# substring berurutan. horns/upright/strings/pad tidak dikurasi registry
# engine — dipertahankan dengan nilai lamanya.
PROGRAM = {"guitar-clean":27,"synth-lead":81,"vibraphone":11,
           "sax":66,"horns":61,"trumpet":56,"rhodes":4,"piano":0,
           "bass-finger":33,"synth-bass":38,"bass":32,
           "upright":32,"strings":48,"pad":89,"guitar":26}

def program_for(name):
    n=name.lower()
    for k,p in PROGRAM.items():
        if k in n: return p
    return 0

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

    # Parse real tempo/meter from the header so the merged MIDI isn't stuck at
    # pretty_midi's default 120bpm/4-4 -- fall back to that default if either
    # header line is missing or doesn't match the expected format.
    quarter_bpm=None
    for h in header:
        qm=re.match(r"^Q:\s*(\d+)/(\d+)=(\d+(?:\.\d+)?)",h)
        if qm:
            num,den,bpm_value=int(qm.group(1)),int(qm.group(2)),float(qm.group(3))
            quarter_bpm=bpm_value*(num/den)*4
            break
    ts_num,ts_den=None,None
    for h in header:
        mm=re.match(r"^M:\s*(\d+)/(\d+)",h)
        if mm:
            ts_num,ts_den=int(mm.group(1)),int(mm.group(2))
            break

    pm=pretty_midi.PrettyMIDI(initial_tempo=quarter_bpm) if quarter_bpm else pretty_midi.PrettyMIDI()
    if ts_num and ts_den:
        pm.time_signature_changes.append(pretty_midi.TimeSignature(ts_num,ts_den,0))
    for vid,bars in body.items():
        name=vnames.get(vid,vid)
        # STRIP chord symbols in quotes so they aren't rendered as notes
        clean_bars=[re.sub(r'"[^"]*"','',b) for b in bars]
        stub="\n".join(header)+f"\nV:{vid}\n"+" ".join(clean_bars)
        s=converter.parse(stub, format="abc")
        # remove any ChordSymbol objects that slipped through
        for cs in list(s.recurse().getElementsByClass(harmony.ChordSymbol)):
            s.remove(cs, recurse=True)
        tmp=tempfile.NamedTemporaryFile(suffix=".mid",delete=False)
        s.write("midi",tmp.name)
        sub=pretty_midi.PrettyMIDI(tmp.name)
        for tr in sub.instruments:
            tr.name=name
            tr.program=program_for(name)
            # Lead should be monophonic: if any chords remain, keep top note only
            if mono_lead and ("sax" in name.lower() or "horn" in name.lower() or "lead" in name.lower()):
                by_start={}
                for n in tr.notes: by_start.setdefault(round(n.start,3),[]).append(n)
                mono=[]
                for st,ns in by_start.items():
                    top=max(ns,key=lambda x:x.pitch)
                    mono.append(top)
                tr.notes=sorted(mono,key=lambda x:x.start)
            pm.instruments.append(tr)
    pm.write(out_path)
    print(f"wrote {out_path}: {len(pm.instruments)} tracks")
    for i in pm.instruments:
        pol=1
        bs={}
        for n in i.notes: bs.setdefault(round(n.start,2),0); bs[round(n.start,2)]+=1
        if bs: pol=max(bs.values())
        print(f"  {i.name:14s} {len(i.notes):3d} notes  max-poly {pol}")

if __name__=="__main__":
    render(sys.argv[1], sys.argv[2])

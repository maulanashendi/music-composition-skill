"""Validator standalone untuk authoring JSON komposisi (kontrak §4).
Mirror engine src/project/composition/schema.js — repo skill tak bisa impor
engine src/, jadi konstanta di-embed di sini; jaga sinkron via corpus fixtures/.
Kumpulkan SEMUA pelanggaran; jangan diam-diam membenarkan."""
import json, re, sys

VALID_INSTRUMENTS = {  # mirror src/instruments/registry.js ids
    'sax','piano','guitar','bass','rhodes','trumpet','vibraphone','jazz-kit',
    'guitar-clean','bass-finger','synth-bass','synth-lead',
}
INSTRUMENT_ALIASES = {  # mirror src/project/composition/instrument-alias.js keys
    'electric-piano','e-piano','ep','keys','acoustic-piano','upright-bass',
    'acoustic-bass','double-bass','contrabass','electric-bass','finger-bass',
    'fingerbass','jazz-guitar','clean-guitar','tenor-sax','saxophone','vibes',
    'vibe','lead-synth','synth','drumkit','drums','kit','drum-kit',
}
ROLES = {'lead','bass','chords','pad','drums'}
ARTICS = {'legato','staccato','accent','normal'}
DRUMS = {'kick','snare','hihat','ride'}
MODES = {'major','minor','ionian','dorian','phrygian','lydian','mixolydian','aeolian','locrian'}

def _beats_per_bar(meter):
    m = re.match(r'^(\d+)/(\d+)$', str(meter).strip())
    if not m: raise ValueError('meter')
    return int(m.group(1)) / (int(m.group(2)) / 4)

def _instrument_known(name, role):
    if role == 'drums': return True
    key = re.sub(r'[\s_]+', '-', str(name or '').lower()).strip()
    return key in VALID_INSTRUMENTS or key in INSTRUMENT_ALIASES

def validate_composition(json_obj):
    v = []
    if not isinstance(json_obj, dict): return ['root bukan objek']
    if json_obj.get('schemaVersion') != 1: v.append('schemaVersion harus 1')
    meta = json_obj.get('meta') or {}
    for f in ('title','key','tempo','meter'):
        if meta.get(f) in (None,): v.append(f'meta.{f} hilang')
    if meta.get('key') is not None:
        km = re.match(r'^([A-G][#b]?)\s+(\w+)$', str(meta['key']).strip())
        if not km or km.group(2).lower() not in MODES: v.append('meta.key tak valid')
    def_meter = meta.get('meter') or '4/4'
    sections = json_obj.get('sections')
    if not isinstance(sections, list) or not sections:
        v.append('sections kosong'); return v
    for si, s in enumerate(sections):
        tag = f"section[{si}]({s.get('name','?')})"
        if not (isinstance(s.get('bars'), (int,float)) and s['bars'] > 0): v.append(f'{tag}: bars harus > 0')
        try: bpb = _beats_per_bar(s.get('meter') or def_meter)
        except Exception: v.append(f'{tag}: meter tak valid'); bpb = 4
        harmony = s.get('harmony')
        if not isinstance(harmony, list) or not harmony: v.append(f'{tag}: harmony kosong')
        else:
            for hi, h in enumerate(harmony):
                if not (1 <= h.get('bar',0) <= s.get('bars',0)): v.append(f'{tag}.harmony[{hi}]: bar di luar')
                if not (h.get('beat',0) >= 1): v.append(f'{tag}.harmony[{hi}]: beat >= 1')
                if not h.get('symbol'): v.append(f'{tag}.harmony[{hi}]: symbol kosong')
        voices = s.get('voices')
        if not isinstance(voices, list): v.append(f'{tag}: voices bukan array'); continue
        for vi, voice in enumerate(voices):
            vtag = f"{tag}.voice[{vi}]({voice.get('role','?')})"
            if voice.get('role') not in ROLES: v.append(f'{vtag}: role tak valid')
            if not _instrument_known(voice.get('instrument'), voice.get('role')):
                v.append(f"{vtag}: instrument \"{voice.get('instrument')}\" tak dikenal")
            notes = voice.get('notes')
            if not isinstance(notes, list): v.append(f'{vtag}: notes bukan array'); continue
            if not notes: v.append(f'{vtag}: notes kosong')
            for ni, n in enumerate(notes):
                ntag = f'{vtag}.note[{ni}]'
                if not (1 <= n.get('bar',0) <= s.get('bars',0)): v.append(f'{ntag}: bar di luar')
                if not (n.get('beat',0) >= 1): v.append(f'{ntag}: beat >= 1')
                if not (n.get('dur',0) > 0): v.append(f'{ntag}: dur > 0')
                if n.get('beat',0) >= 1 and n.get('dur',0) > 0 and (n['beat']-1+n['dur']) > bpb + 1e-9:
                    v.append(f'{ntag}: beat+dur melewati bar')
                if not (1 <= n.get('vel',0) <= 127): v.append(f'{ntag}: vel di luar 1..127')
                if n.get('artic') not in ARTICS: v.append(f'{ntag}: artic tak valid')
                if not n.get('pitch'): v.append(f'{ntag}: pitch kosong')
                if voice.get('role') == 'drums' and n.get('pitch') and n['pitch'] not in DRUMS:
                    v.append(f'{ntag}: nama drum tak valid "{n.get("pitch")}"')
    return v

if __name__ == '__main__':
    if len(sys.argv) != 2: print('usage: validate_composition.py <song.json>'); sys.exit(2)
    with open(sys.argv[1]) as f: obj = json.load(f)
    viol = validate_composition(obj)
    if viol:
        print(f'{len(viol)} pelanggaran:'); [print(' -', x) for x in viol]; sys.exit(1)
    print('valid'); sys.exit(0)

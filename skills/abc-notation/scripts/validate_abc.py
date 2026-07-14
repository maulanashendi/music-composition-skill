#!/usr/bin/env python3
"""Validate lead-sheet-oriented ABC notation.

Supported features include required headers, additive and common meters, note and
rest lengths, pickup bars, ties, slurs, grace notes, common and explicit tuplets,
broken rhythm, bracket chords, repeats/endings, inline fields, multi-measure
rests, and multiple voices. The validator checks structural duration and common
syntax; it is not a complete implementation of every ABC extension.
"""
from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass, field
from fractions import Fraction
from pathlib import Path
from typing import Optional


REQUIRED_FIELDS = ("X", "T", "M", "L", "Q", "K", "V")
FIELD_RE = re.compile(r"^([A-Za-z]):\s*(.*)$")
INLINE_FIELD_RE = re.compile(r"\[([A-Za-z]):([^\]]*)\]")
METER_RE = re.compile(r"^\s*(\d+(?:\+\d+)*)\s*/\s*(\d+)\s*$")
FRACTION_RE = re.compile(r"^\s*(\d+)\s*/\s*(\d+)\s*$")
TUPLET_RE = re.compile(r"\((\d+)(?::(\d*))?(?::(\d*))?")
LENGTH_RE = re.compile(r"(?:(\d+))?(?:(/+)(\d*)?)?")
VOICE_ID_RE = re.compile(r"^\s*([^\s]+)")


@dataclass
class Event:
    duration: Fraction
    line: int
    token: str
    kind: str = "note"


@dataclass
class Bar:
    duration: Fraction
    expected: Optional[Fraction]
    line: int
    event_count: int
    multi_rest: bool = False
    multi_rest_measures: int = 0


@dataclass
class VoiceState:
    name: str
    meter: Optional[Fraction]
    default_length: Fraction
    bars: list[Bar] = field(default_factory=list)
    events: list[Event] = field(default_factory=list)
    duration: Fraction = Fraction(0, 1)
    tuplet_factor: Fraction = Fraction(1, 1)
    tuplet_remaining: int = 0
    broken_next: Optional[Fraction] = None
    current_line: int = 0
    overlay_segments: list[tuple[Fraction, int, int, bool]] = field(default_factory=list)

    def add_event(self, event: Event, errors: list[str]) -> None:
        if self.broken_next is not None:
            event.duration *= self.broken_next
            self.broken_next = None

        if self.tuplet_remaining > 0 and event.kind != "multi_rest":
            event.duration *= self.tuplet_factor
            self.tuplet_remaining -= 1
            if self.tuplet_remaining == 0:
                self.tuplet_factor = Fraction(1, 1)

        self.events.append(event)
        self.duration += event.duration
        self.current_line = event.line

    def apply_broken(self, marks: str, line: int, errors: list[str]) -> None:
        if not self.events:
            errors.append(f"line {line}, voice {self.name}: broken-rhythm marker has no preceding event")
            return
        if self.broken_next is not None:
            errors.append(f"line {line}, voice {self.name}: consecutive broken-rhythm groups without a following event")
            return

        count = len(marks)
        short = Fraction(1, 2**count)
        long = Fraction(2 ** (count + 1) - 1, 2**count)
        if marks[0] == ">":
            previous_factor, next_factor = long, short
        else:
            previous_factor, next_factor = short, long

        previous = self.events[-1]
        self.duration -= previous.duration
        previous.duration *= previous_factor
        self.duration += previous.duration
        self.broken_next = next_factor

    def start_tuplet(
        self,
        p: int,
        q: int,
        r: int,
        line: int,
        errors: list[str],
        warnings: list[str],
    ) -> None:
        if p <= 0 or q <= 0 or r <= 0:
            errors.append(f"line {line}, voice {self.name}: tuplet values must be positive")
            return
        if self.tuplet_remaining > 0:
            warnings.append(f"line {line}, voice {self.name}: nested or overlapping tuplets require manual review")
        self.tuplet_factor = Fraction(q, p)
        self.tuplet_remaining = r

    def start_overlay(self, line: int, errors: list[str]) -> None:
        if not self.events and self.duration == 0:
            errors.append(f"line {line}, voice {self.name}: overlay marker has no preceding layer")
            return
        if self.broken_next is not None:
            errors.append(f"line {line}, voice {self.name}: broken rhythm cannot cross an overlay marker")
            self.broken_next = None
        if self.tuplet_remaining > 0:
            errors.append(f"line {line}, voice {self.name}: tuplet cannot cross an overlay marker")
            self.tuplet_remaining = 0
            self.tuplet_factor = Fraction(1, 1)
        self.overlay_segments.append(
            (
                self.duration,
                len(self.events),
                self.current_line or line,
                any(event.kind == "multi_rest" for event in self.events),
            )
        )
        self.events = []
        self.duration = Fraction(0, 1)
        self.current_line = 0

    def close_bar(self, line: int, errors: list[str], warnings: list[str]) -> None:
        if not self.events and self.duration == 0 and not self.overlay_segments:
            return
        if self.broken_next is not None:
            errors.append(f"line {line}, voice {self.name}: broken-rhythm marker lacks a following event")
            self.broken_next = None

        segments = list(self.overlay_segments)
        if self.events or self.duration:
            segments.append(
                (
                    self.duration,
                    len(self.events),
                    self.current_line or line,
                    any(event.kind == "multi_rest" for event in self.events),
                )
            )
        elif self.overlay_segments:
            errors.append(f"line {line}, voice {self.name}: overlay marker lacks a following layer")

        durations = [segment[0] for segment in segments]
        if len(durations) > 1 and len(set(durations)) > 1:
            warnings.append(
                f"line {segments[0][2]}, voice {self.name}: overlay layers have different durations "
                + ", ".join(str(value) for value in durations)
            )
        duration = max(durations, default=Fraction(0, 1))
        event_count = sum(segment[1] for segment in segments)
        first_line = min((segment[2] for segment in segments if segment[2] > 0), default=line)
        any_multi_rest = any(segment[3] for segment in segments)
        multi_rest = any_multi_rest and len(segments) == 1 and event_count == 1
        if any_multi_rest and not multi_rest:
            errors.append(f"line {line}, voice {self.name}: multi-measure rest cannot be combined with overlay or other events")

        multi_measures = 0
        if multi_rest and self.meter:
            multi_measures = int(duration / self.meter) if duration % self.meter == 0 else 0

        self.bars.append(
            Bar(
                duration=duration,
                expected=self.meter,
                line=first_line,
                event_count=event_count,
                multi_rest=multi_rest,
                multi_rest_measures=multi_measures,
            )
        )
        self.events = []
        self.duration = Fraction(0, 1)
        self.current_line = 0
        self.overlay_segments = []


def parse_fraction(value: str) -> Fraction:
    match = FRACTION_RE.match(value)
    if not match:
        raise ValueError(f"invalid fraction {value!r}")
    numerator = int(match.group(1))
    denominator = int(match.group(2))
    if numerator <= 0 or denominator <= 0:
        raise ValueError(f"fraction values must be positive: {value!r}")
    return Fraction(numerator, denominator)


def parse_meter(value: str) -> Optional[Fraction]:
    cleaned = value.strip()
    if cleaned.lower() in {"none", "free"}:
        return None
    if cleaned == "C":
        return Fraction(4, 4)
    if cleaned == "C|":
        return Fraction(2, 2)
    match = METER_RE.match(cleaned)
    if not match:
        raise ValueError(f"invalid meter {value!r}")
    numerator = sum(int(part) for part in match.group(1).split("+"))
    denominator = int(match.group(2))
    if numerator <= 0 or denominator <= 0:
        raise ValueError(f"meter values must be positive: {value!r}")
    return Fraction(numerator, denominator)


def is_compound_meter(meter: Optional[Fraction]) -> bool:
    if meter is None:
        return False
    numerator = meter.numerator
    denominator = meter.denominator
    return denominator in {8, 16} and numerator > 3 and numerator % 3 == 0


def default_tuplet_q(p: int, meter: Optional[Fraction]) -> int:
    if p in {2, 4, 8}:
        return 3
    if p in {3, 6}:
        return 2
    if p in {5, 7, 9}:
        return 3 if is_compound_meter(meter) else 2
    return max(1, p - 1)


def parse_length_multiplier(text: str, pos: int) -> tuple[Fraction, int, str]:
    match = LENGTH_RE.match(text, pos)
    if not match:
        return Fraction(1, 1), pos, ""
    number, slashes, denominator = match.groups()
    if not any((number, slashes, denominator)):
        return Fraction(1, 1), pos, ""

    multiplier = Fraction(int(number), 1) if number else Fraction(1, 1)
    if slashes:
        if denominator:
            multiplier /= int(denominator)
            if len(slashes) > 1:
                multiplier /= 2 ** (len(slashes) - 1)
        else:
            multiplier /= 2 ** len(slashes)
    return multiplier, match.end(), match.group(0)


def strip_comment(line: str) -> str:
    in_quote = False
    escaped = False
    result: list[str] = []
    for char in line:
        if escaped:
            result.append(char)
            escaped = False
            continue
        if char == "\\":
            result.append(char)
            escaped = True
            continue
        if char == '"':
            in_quote = not in_quote
            result.append(char)
            continue
        if char == "%" and not in_quote:
            break
        result.append(char)
    return "".join(result)


def voice_id(value: str) -> str:
    match = VOICE_ID_RE.match(value)
    return match.group(1) if match else value.strip() or "default"


class ABCValidator:
    def __init__(self, text: str) -> None:
        self.text = text
        self.errors: list[str] = []
        self.warnings: list[str] = []
        self.headers: dict[str, list[str]] = {}
        self.voice_declarations: list[str] = []
        self.voices: dict[str, VoiceState] = {}
        self.current_voice: Optional[str] = None
        self.global_meter: Optional[Fraction] = Fraction(4, 4)
        self.global_default = Fraction(1, 8)
        self.body_started = False
        self.music_seen = False
        self.lyrics_seen = False
        self.overlay_seen = False
        self.unknown_seen: set[str] = set()

    def get_voice(self, name: Optional[str] = None) -> VoiceState:
        voice_name = name or self.current_voice or (self.voice_declarations[0] if self.voice_declarations else "default")
        if voice_name not in self.voices:
            self.voices[voice_name] = VoiceState(
                name=voice_name,
                meter=self.global_meter,
                default_length=self.global_default,
            )
        self.current_voice = voice_name
        return self.voices[voice_name]

    def declare_voice(self, value: str) -> None:
        name = voice_id(value)
        if name not in self.voice_declarations:
            self.voice_declarations.append(name)
        self.get_voice(name)

    def update_meter(self, value: str, line_no: int, inline: bool = False) -> None:
        try:
            meter = parse_meter(value)
        except ValueError as exc:
            self.errors.append(f"line {line_no}: {exc}")
            return

        if inline or self.current_voice:
            state = self.get_voice()
            if state.duration:
                self.errors.append(f"line {line_no}, voice {state.name}: meter change occurs inside an unfinished bar")
            state.meter = meter
        else:
            self.global_meter = meter
            for state in self.voices.values():
                if not state.bars and not state.events:
                    state.meter = meter

        if meter is None:
            self.warnings.append(f"line {line_no}: unmetered music requires manual duration review")

    def update_default_length(self, value: str, line_no: int, inline: bool = False) -> None:
        try:
            default = parse_fraction(value)
        except ValueError as exc:
            self.errors.append(f"line {line_no}: {exc}")
            return

        if inline or self.current_voice:
            state = self.get_voice()
            if state.duration:
                self.errors.append(f"line {line_no}, voice {state.name}: default-length change occurs inside an unfinished bar")
            state.default_length = default
        else:
            self.global_default = default
            for state in self.voices.values():
                if not state.bars and not state.events:
                    state.default_length = default

    def parse_header_or_field(self, line: str, line_no: int) -> bool:
        match = FIELD_RE.match(line)
        if not match:
            return False
        key, value = match.group(1), match.group(2).strip()

        if not self.body_started:
            self.headers.setdefault(key, []).append(value)
            if key == "M":
                try:
                    self.global_meter = parse_meter(value)
                    for state in self.voices.values():
                        if not state.bars and not state.events:
                            state.meter = self.global_meter
                except ValueError as exc:
                    self.errors.append(f"line {line_no}: {exc}")
            elif key == "L":
                try:
                    self.global_default = parse_fraction(value)
                    for state in self.voices.values():
                        if not state.bars and not state.events:
                            state.default_length = self.global_default
                except ValueError as exc:
                    self.errors.append(f"line {line_no}: {exc}")
            elif key == "V":
                self.declare_voice(value)
            elif key == "K":
                self.body_started = True
                if self.current_voice is None and self.voice_declarations:
                    self.current_voice = self.voice_declarations[0]
            return True

        if key == "V":
            self.headers.setdefault("V", []).append(value)
            self.declare_voice(value)
            return True
        if key == "M":
            self.update_meter(value, line_no)
            return True
        if key == "L":
            self.update_default_length(value, line_no)
            return True
        if key in {"K", "Q", "P", "R", "I", "U"}:
            if key == "U":
                self.warnings.append(f"line {line_no}: user-defined ABC symbols require renderer review")
            return True
        if key in {"w", "W"}:
            self.lyrics_seen = True
            return True
        return True

    def parse_inline_field(self, key: str, value: str, line_no: int) -> None:
        key = key.upper()
        value = value.strip()
        if key == "V":
            self.declare_voice(value)
        elif key == "M":
            self.update_meter(value, line_no, inline=True)
        elif key == "L":
            self.update_default_length(value, line_no, inline=True)
        elif key in {"K", "Q", "P"}:
            return
        else:
            self.warnings.append(f"line {line_no}: inline field [{key}:{value}] requires manual review")

    def parse_note_event(self, line: str, pos: int, line_no: int) -> tuple[Optional[Event], int]:
        start = pos
        accidental = ""
        if line.startswith("^^", pos) or line.startswith("__", pos):
            accidental = line[pos : pos + 2]
            pos += 2
        elif pos < len(line) and line[pos] in "^_=":
            accidental = line[pos]
            pos += 1

        if pos >= len(line) or line[pos] not in "ABCDEFGabcdefgzZxX":
            return None, start

        pitch = line[pos]
        pos += 1
        while pos < len(line) and line[pos] in ",'":
            pos += 1

        multiplier, pos_after, length_text = parse_length_multiplier(line, pos)
        pos = pos_after
        token = line[start:pos]

        if pitch in "zZ" and length_text == "5":
            self.errors.append(
                f"line {line_no}: rest token {token!r} is a bare 'z5'/'Z5' -- the abcjs "
                "renderer used by the downstream render engine fails to parse this exact "
                "duration (\"Duration not representable\"); z1-z4, z6-z10, etc. all parse "
                "fine, only the digit 5 triggers it. Split into two rests with the same "
                "total duration instead, e.g. 'z2 z3' or 'z4 z1'."
            )

        if pitch in "ZX":
            if "/" in length_text:
                self.errors.append(f"line {line_no}: multi-measure rest {token!r} must use an integer measure count")
                count = 1
            else:
                count = int(length_text) if length_text.isdigit() else 1
            state = self.get_voice()
            if state.meter is None:
                self.errors.append(f"line {line_no}, voice {state.name}: multi-measure rest requires a meter")
                duration = Fraction(0, 1)
            else:
                duration = state.meter * count
            event = Event(duration=duration, line=line_no, token=token, kind="multi_rest")
        else:
            state = self.get_voice()
            duration = state.default_length * multiplier
            kind = "rest" if pitch in "zx" else "note"
            event = Event(duration=duration, line=line_no, token=accidental + token, kind=kind)

        if pos < len(line) and line[pos] == "-":
            pos += 1
        return event, pos

    def parse_bracket_chord(self, line: str, pos: int, line_no: int) -> tuple[Optional[Event], int]:
        close = line.find("]", pos + 1)
        if close < 0:
            self.errors.append(f"line {line_no}: unclosed bracket chord")
            return None, len(line)
        content = line[pos + 1 : close]
        inner_durations: list[Fraction] = []
        inner_pos = 0
        while inner_pos < len(content):
            char = content[inner_pos]
            if char.isspace() or char in "-()~.!+":
                inner_pos += 1
                continue
            event, next_pos = self.parse_note_event(content, inner_pos, line_no)
            if event is None:
                inner_pos += 1
                continue
            if event.kind == "multi_rest":
                self.errors.append(f"line {line_no}: multi-measure rest is invalid inside a bracket chord")
            else:
                inner_durations.append(event.duration)
            inner_pos = next_pos

        if not inner_durations:
            self.errors.append(f"line {line_no}: bracket chord contains no parseable notes")
            return None, close + 1

        outer_multiplier, next_pos, outer_text = parse_length_multiplier(line, close + 1)
        state = self.get_voice()
        if outer_text:
            duration = state.default_length * outer_multiplier
        else:
            duration = inner_durations[0]
            if len(set(inner_durations)) > 1:
                self.warnings.append(
                    f"line {line_no}: independent lengths inside bracket chord require manual review"
                )
                duration = max(inner_durations)

        if next_pos < len(line) and line[next_pos] == "-":
            next_pos += 1
        token = line[pos:next_pos]
        return Event(duration=duration, line=line_no, token=token, kind="chord"), next_pos

    def close_bar(self, line_no: int) -> None:
        self.get_voice().close_bar(line_no, self.errors, self.warnings)

    def parse_music_line(self, raw_line: str, line_no: int) -> None:
        line = strip_comment(raw_line)
        if not line.strip():
            return
        self.music_seen = True
        pos = 0

        while pos < len(line):
            char = line[pos]

            if char.isspace() or char == "\\":
                pos += 1
                continue

            if char == '"':
                end = pos + 1
                escaped = False
                while end < len(line):
                    if line[end] == '"' and not escaped:
                        break
                    escaped = line[end] == "\\" and not escaped
                    if line[end] != "\\":
                        escaped = False
                    end += 1
                if end >= len(line):
                    self.errors.append(f"line {line_no}: unclosed quoted chord or annotation")
                    return
                pos = end + 1
                continue

            if line.startswith("%%", pos):
                return

            if char == "!":
                end = line.find("!", pos + 1)
                if end < 0:
                    self.errors.append(f"line {line_no}: unclosed !decoration!")
                    return
                pos = end + 1
                continue

            if char == "+":
                end = line.find("+", pos + 1)
                if end < 0:
                    self.errors.append(f"line {line_no}: unclosed +decoration+")
                    return
                pos = end + 1
                continue

            if char == "{":
                end = line.find("}", pos + 1)
                if end < 0:
                    self.errors.append(f"line {line_no}: unclosed grace-note group")
                    return
                pos = end + 1
                continue

            if char == "[":
                inline = INLINE_FIELD_RE.match(line, pos)
                if inline:
                    self.parse_inline_field(inline.group(1), inline.group(2), line_no)
                    pos = inline.end()
                    continue
                ending = re.match(r"\[(\d+)(?:[-,]\d+)*", line[pos:])
                if ending:
                    pos += ending.end()
                    continue
                if line.startswith("[|", pos):
                    self.close_bar(line_no)
                    pos += 2
                    continue
                event, next_pos = self.parse_bracket_chord(line, pos, line_no)
                if event is not None:
                    self.get_voice().add_event(event, self.errors)
                pos = next_pos
                continue

            barline = None
            for candidate in (":|:", "|:", ":|", "||", "|]", "::", "|"):
                if line.startswith(candidate, pos):
                    barline = candidate
                    break
            if barline:
                self.close_bar(line_no)
                pos += len(barline)
                continue

            if char == "(":
                tuplet = TUPLET_RE.match(line, pos)
                if tuplet:
                    p = int(tuplet.group(1))
                    q = int(tuplet.group(2)) if tuplet.group(2) else default_tuplet_q(p, self.get_voice().meter)
                    r = int(tuplet.group(3)) if tuplet.group(3) else p
                    self.get_voice().start_tuplet(p, q, r, line_no, self.errors, self.warnings)
                    pos = tuplet.end()
                    continue
                pos += 1
                continue

            if char == ")":
                pos += 1
                continue

            if char in "><":
                end = pos + 1
                while end < len(line) and line[end] == char:
                    end += 1
                self.get_voice().apply_broken(line[pos:end], line_no, self.errors)
                pos = end
                continue

            if char == "&":
                self.overlay_seen = True
                self.get_voice().start_overlay(line_no, self.errors)
                pos += 1
                continue

            if char in ".~":
                pos += 1
                continue

            event, next_pos = self.parse_note_event(line, pos, line_no)
            if event is not None:
                self.get_voice().add_event(event, self.errors)
                pos = next_pos
                continue

            if char in "HLMOPSTuv":
                pos += 1
                continue

            if char in ":]":
                self.unknown_seen.add(char)
                pos += 1
                continue

            if char not in self.unknown_seen:
                self.warnings.append(f"line {line_no}: unrecognized ABC character {char!r}; manual review required")
                self.unknown_seen.add(char)
            pos += 1

    def validate_bars(self) -> None:
        expanded_counts: dict[str, int] = {}

        for name, state in self.voices.items():
            state.close_bar(len(self.text.splitlines()), self.errors, self.warnings)
            if state.tuplet_remaining > 0:
                self.errors.append(
                    f"voice {name}: tuplet ended with {state.tuplet_remaining} event(s) still expected"
                )

            bars = state.bars
            if not bars:
                self.warnings.append(f"voice {name}: declared but contains no music events")
                continue

            partial_indices: list[int] = []
            for index, bar in enumerate(bars):
                if bar.expected is None:
                    continue
                if bar.multi_rest:
                    if bar.multi_rest_measures <= 0:
                        self.errors.append(
                            f"line {bar.line}, voice {name}, bar {index + 1}: invalid multi-measure rest duration {bar.duration}"
                        )
                    continue
                if bar.duration == bar.expected:
                    continue
                if bar.duration < bar.expected:
                    partial_indices.append(index)
                    continue
                self.errors.append(
                    f"line {bar.line}, voice {name}, bar {index + 1}: duration {bar.duration} exceeds meter duration {bar.expected}"
                )

            pickup_ok: set[int] = set()
            if partial_indices:
                first = partial_indices[0]
                last = partial_indices[-1]
                if (
                    first == 0
                    and len(bars) > 1
                    and last == len(bars) - 1
                    and first != last
                    and bars[first].expected is not None
                    and bars[first].expected == bars[last].expected
                    and bars[first].duration + bars[last].duration == bars[first].expected
                ):
                    pickup_ok = {first, last}
                    self.warnings.append(
                        f"voice {name}: opening pickup and final bar form a complete measure"
                    )
                elif first == 0 and len(bars) > 1 and len(partial_indices) == 1:
                    pickup_ok = {first}
                    self.warnings.append(
                        f"voice {name}: opening pickup accepted without a complementary shortened final bar; verify performed form"
                    )

            for index in partial_indices:
                if index in pickup_ok:
                    continue
                bar = bars[index]
                self.errors.append(
                    f"line {bar.line}, voice {name}, bar {index + 1}: duration {bar.duration} does not equal meter duration {bar.expected}"
                )

            expanded_counts[name] = sum(
                bar.multi_rest_measures if bar.multi_rest and bar.multi_rest_measures > 0 else 1 for bar in bars
            )

        if len(set(expanded_counts.values())) > 1:
            detail = ", ".join(f"{name}={count}" for name, count in sorted(expanded_counts.items()))
            self.warnings.append(f"voices have different expanded bar counts ({detail}); confirm staggered entries or multi-rest use")

    def run(self) -> tuple[list[str], list[str]]:
        lines = self.text.splitlines()
        for line_no, raw in enumerate(lines, 1):
            stripped = strip_comment(raw).strip()
            if not stripped:
                continue
            if stripped.startswith("%%"):
                if "score" in stripped.lower() or "midi" in stripped.lower() or "transpose" in stripped.lower():
                    self.warnings.append(f"line {line_no}: renderer-specific directive requires manual review")
                continue
            if self.parse_header_or_field(stripped, line_no):
                continue
            if not self.body_started:
                self.errors.append(f"line {line_no}: music appears before the K: field that ends the header")
                self.body_started = True
            self.parse_music_line(raw, line_no)

        for field_name in REQUIRED_FIELDS:
            if field_name == "V":
                if not self.voice_declarations and "V" not in self.headers:
                    self.errors.append("missing required header V:")
            elif field_name not in self.headers:
                self.errors.append(f"missing required header {field_name}:")

        quote_count = sum(strip_comment(line).count('\"') for line in lines)
        if quote_count % 2:
            self.errors.append("unbalanced double quotes in chord symbols or annotations")
        if not self.music_seen:
            self.errors.append("no music body found")

        self.validate_bars()

        if self.overlay_seen:
            self.warnings.append("overlay syntax '&' detected; layer durations were checked, but visual rendering still requires review")
        if self.lyrics_seen:
            self.warnings.append("lyrics detected; syllable-to-note alignment is not validated")
        if any(state.meter is None for state in self.voices.values()):
            self.warnings.append("unmetered voice detected; bar-duration validation was skipped for those bars")

        return self.errors, self.warnings


def validate(path: Path) -> tuple[list[str], list[str]]:
    try:
        text = path.read_text(encoding="utf-8")
    except Exception as exc:
        return [f"cannot read ABC file: {exc}"], []
    return ABCValidator(text).run()


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("abc_file", type=Path)
    args = parser.parse_args()

    errors, warnings = validate(args.abc_file)
    for warning in warnings:
        print(f"WARNING: {warning}")
    for error in errors:
        print(f"ERROR: {error}")

    if errors:
        print(f"FAILED: {len(errors)} error(s), {len(warnings)} warning(s)")
        return 1
    print(f"OK: 0 errors, {len(warnings)} warning(s)")
    return 0


if __name__ == "__main__":
    sys.exit(main())

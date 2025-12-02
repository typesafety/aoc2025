from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable, Self
import re


def solve_part1(puzzle_input: str) -> str:
    ranges = parse_ranges(puzzle_input)

    invalids: list[int] = []
    for r in ranges:
        for n in r.nums:
            if not valid(n):
                invalids.append(n)

    return str(sum(invalids))


def solve_part2(puzzle_input: str) -> str:
    return str(puzzle_input)


REGEX = re.compile(r"(?P<start>\d+)-(?P<end>\d+)")


def valid(n: int) -> bool:
    sn = str(n)
    sn_len = len(sn)

    if sn_len % 2 != 0:
        return True

    first = sn[0 : len(sn) // 2]
    second = sn[len(sn) // 2 :]

    return first != second


def parse_ranges(text: str) -> list[Range]:
    ranges = [Range.from_str(r) for r in text.split(",")]
    return ranges


@dataclass
class Range:
    start: int
    end: int

    @property
    def nums(self) -> Iterable[int]:
        return range(self.start, self.end + 1)

    @classmethod
    def from_str(cls, text: str) -> Self:
        if match := REGEX.search(text):
            start = match.group("start")
            end = match.group("end")

            return cls(int(start), int(end))
        else:
            assert False, "fuck"

from __future__ import annotations

from dataclasses import dataclass
from pprint import pprint, pformat  # noqa: F401
from typing import Self


def solve_part1(puzzle_input: str) -> str:
    ranges, ids = parse_input(puzzle_input)

    fresh: set[int] = set()
    for ident in ids:
        if any(r.contains(ident) for r in ranges):
            fresh.add(ident)

    return str(len(fresh))


def solve_part2(puzzle_input: str) -> str:
    return puzzle_input


def parse_input(puzzle_input: str) -> tuple[set[Range], set[int]]:
    [ranges, ids] = puzzle_input.split("\n\n")
    range_lines = ranges.strip().splitlines()
    id_lines = ids.strip().splitlines()

    return {Range.parse(line) for line in range_lines}, {int(ident) for ident in id_lines}


@dataclass(frozen=True)
class Range:
    start: int
    end: int

    @classmethod
    def parse(cls, text: str) -> Self:
        [start, end] = text.split("-")
        return cls(int(start), int(end))

    def contains(self, ident: int) -> bool:
        return ident >= self.start and ident <= self.end

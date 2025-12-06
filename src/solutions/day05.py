from __future__ import annotations

import copy
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
    ranges, _ = parse_input(puzzle_input)
    merged = merge_ranges(ranges)

    return str(sum(1 + r.end - r.start for r in merged))


def merge_ranges(ranges: set[Range]) -> set[Range]:
    new: set[Range] = set()

    for r in ranges:
        new = add_range(r, new)

    return new


def add_range(new_range: Range, ranges: set[Range]) -> set[Range]:
    new = copy.copy(ranges)

    for r in ranges:
        if merged := r.merge(new_range):
            new.remove(r)
            return add_range(merged, new)

    new.add(new_range)
    return new


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

    def intersects(self, r: Range) -> bool:
        return (
            (r.start < self.start and r.end > self.end)
            or self.contains(r.start)
            or self.contains(r.end)
        )

    def merge(self, r: Range) -> Range | None:
        return (
            Range(start=min(self.start, r.start), end=max(self.end, r.end))
            if self.intersects(r)
            else None
        )


def parse_input(puzzle_input: str) -> tuple[set[Range], set[int]]:
    [ranges, ids] = puzzle_input.split("\n\n")
    range_lines = ranges.strip().splitlines()
    id_lines = ids.strip().splitlines()

    return {Range.parse(line) for line in range_lines}, {int(ident) for ident in id_lines}

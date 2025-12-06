from __future__ import annotations

from dataclasses import dataclass
from functools import reduce
from pprint import pprint, pformat
from typing import Any, Callable, TypeVar  # noqa: F401

T = TypeVar("T")


def solve_part1(puzzle_input: str) -> str:
    problems = parse_input(puzzle_input)
    return str(sum(p.solve() for p in problems))


def solve_part2(puzzle_input: str) -> str:
    return puzzle_input


@dataclass(frozen=True)
class Problem:
    numbers: list[int]
    op: Callable[[int, int], int]

    def solve(self) -> int:
        return reduce(self.op, self.numbers)


def parse_input(puzzle_input: str) -> list[Problem]:
    rows = puzzle_input.splitlines()
    num_rows = [parse_number_row(r) for r in rows[:-1]]
    op_row = parse_op_row(rows[len(rows) - 1])

    return [
       Problem(segments[:-1], segments[len(segments) - 1])
       for segments in transpose([*num_rows, op_row])
    ]


def transpose(m: list[list[Any]]) -> list[list[Any]]:
    return [list(tup) for tup in zip(*m, strict=True)]


def parse_number_row(text: str) -> list[int]:
    return [int(s) for s in text.split()]


def parse_op_row(text: str) -> list[Callable[[int, int], int]]:
    def parse_op(s: str) -> Callable[[int, int], int]:
        def mul(x: int, y: int) -> int:
            return x * y

        def add(x: int, y: int) -> int:
            return x + y

        return {"*": mul, "+": add}[s]

    return [parse_op(s) for s in text.split()]

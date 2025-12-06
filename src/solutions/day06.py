from __future__ import annotations

from dataclasses import dataclass
from functools import reduce
from typing import Any, Callable, TypeVar

T = TypeVar("T")


def solve_part1(puzzle_input: str) -> str:
    problems = parse_input(puzzle_input)
    return str(sum(p.solve() for p in problems))


def solve_part2(puzzle_input: str) -> str:
    rows = puzzle_input.splitlines()
    cols: list[list[str]] = transpose(rows)
    problems = parse_cephalopod_problems(cols)

    return str(sum(p.solve() for p in problems))


@dataclass(frozen=True)
class Problem:
    numbers: list[int]
    op: Callable[[int, int], int]

    def solve(self) -> int:
        return reduce(self.op, self.numbers)


def parse_cephalopod_problems(cols: list[list[str]]) -> list[Problem]:
    problems: list[Problem] = []
    while len(cols) > 0:
        problem, new_cols = parse_cephalopod_problem(cols)
        problems.append(problem)
        cols = new_cols

    return problems


def parse_cephalopod_problem(cols: list[list[str]]) -> tuple[Problem, list[list[str]]]:
    nums: list[int] = []
    op = None

    for ix, col in enumerate(cols):
        if len("".join(col).strip()) == 0:
            assert op is not None
            return Problem(nums, op), cols[ix + 1 :]

        num = parse_col(col[:-1])
        nums.append(num)

        if op is None and (parsed_op := parse_op(col[len(col) - 1])):
            op = parsed_op

    assert op is not None
    return Problem(nums, op), []


def parse_col(col: list[str]) -> int:
    return int("".join([c for c in col if c != " "]))


def parse_input(puzzle_input: str) -> list[Problem]:
    rows = puzzle_input.splitlines()
    num_rows = [parse_number_row(r) for r in rows[:-1]]
    op_row = parse_op_row(rows[len(rows) - 1])

    return [
        Problem(segments[:-1], segments[len(segments) - 1])
        for segments in transpose([*num_rows, op_row])
    ]


def transpose(m: list[Any]) -> list[Any]:
    return [list(tup) for tup in zip(*m, strict=True)]


def parse_number_row(text: str) -> list[int]:
    return [int(s) for s in text.split()]


def parse_op_row(text: str) -> list[Callable[[int, int], int]]:
    ops = [parse_op(s) for s in text.split()]
    return [op for op in ops if op is not None]


def parse_op(s: str) -> Callable[[int, int], int] | None:
    def mul(x: int, y: int) -> int:
        return x * y

    def add(x: int, y: int) -> int:
        return x + y

    return {"*": mul, "+": add}.get(s)

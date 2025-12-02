from __future__ import annotations

from dataclasses import dataclass
from enum import Enum, auto
from typing import Self
import re


def solve_part1(puzzle_input: str) -> str:
    rotations = parse_rotations(puzzle_input)

    count = 0
    val = 50
    for r in rotations:
        val += r.val
        if val % 100 == 0:
            count += 1

    return str(count)


def solve_part2(puzzle_input: str) -> str:
    return "TODO"


REGEX = re.compile(r"(?P<dir>L|R)(?P<num>\d+)")


def parse_rotations(text: str) -> list[Rotation]:
    rotations = [Rotation.from_str(line) for line in text.strip().splitlines()]
    return rotations


class Dir(Enum):
    L = auto()
    R = auto()


@dataclass
class Rotation:
    direction: Dir
    amount: int

    @property
    def val(self) -> int:
        match self.direction:
            case Dir.L:
                return -self.amount
            case Dir.R:
                return self.amount

    @classmethod
    def from_str(cls, text: str) -> Self:
        if res := REGEX.search(text):
            direction = res.group("dir")
            print(f"{direction =}")
            amount = res.group("num")

            match direction:
                case "L":
                    return cls(Dir.L, int(amount))
                case "R":
                    return cls(Dir.R, int(amount))
                case _:
                    raise RuntimeError("Fuck")
        else:
            raise RuntimeError(f"Couldn't parse line: {text}")

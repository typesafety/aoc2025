from __future__ import annotations

import time
from argparse import ArgumentParser
from dataclasses import dataclass
from enum import IntEnum, auto
from pathlib import Path
from typing import Callable, TypeVar

from src.solutions import day01, day02, day03, day04, day05, day06

T = TypeVar("T")


@dataclass
class CliArgs:
    day: Day
    part: Part
    input_path: Path


class Day(IntEnum):
    D01 = auto()
    D02 = auto()
    D03 = auto()
    D04 = auto()
    D05 = auto()
    D06 = auto()


class Part(IntEnum):
    P1 = auto()
    P2 = auto()


def select_solver(day: Day, part: Part) -> Callable[[str], str]:
    match (day, part):
        case (Day.D01, Part.P1):
            return day01.solve_part1
        case (Day.D01, Part.P2):
            return day01.solve_part2
        case (Day.D02, Part.P1):
            return day02.solve_part1
        case (Day.D02, Part.P2):
            return day02.solve_part2
        case (Day.D03, Part.P1):
            return day03.solve_part1
        case (Day.D03, Part.P2):
            return day03.solve_part2
        case (Day.D04, Part.P1):
            return day04.solve_part1
        case (Day.D04, Part.P2):
            return day04.solve_part2
        case (Day.D05, Part.P1):
            return day05.solve_part1
        case (Day.D05, Part.P2):
            return day05.solve_part2
        case (Day.D06, Part.P1):
            return day06.solve_part1
        case (Day.D06, Part.P2):
            return day06.solve_part2
        case _:
            raise RuntimeError(f"Solver for day {day} part {part} not implemented")


def make_argparse_parser() -> ArgumentParser:
    parser = ArgumentParser(prog="aoc2025", description="Advent of Code 2025")
    parser.add_argument(
        "-d", "--day", help="Day (1-12)", metavar="[1..12]", required=True, type=int
    )
    parser.add_argument("-p", "--part", type=int, help="Part (1-2)", metavar="{1,2}", required=True)
    parser.add_argument(
        "-i",
        "--input_path",
        help="Path to puzzle input",
        metavar="PUZZLE_INPUT_PATH",
        required=True,
        type=str,
    )

    return parser


def parse_cli_args(day: int, part: int, input_path: str) -> CliArgs:
    days: dict[int, Day] = {1: Day.D01, 2: Day.D02, 3: Day.D03, 4: Day.D04, 5: Day.D05, 6: Day.D06}
    parts: dict[int, Part] = {1: Part.P1, 2: Part.P2}

    if (parsed_day := days.get(day)) is None:
        raise RuntimeError(f"Invalid day: {day}")
    if (parsed_part := parts.get(part)) is None:
        raise RuntimeError(f"Invalid part: {part}")
    if not Path(input_path).is_file():
        raise RuntimeError(f"Puzzle input file does not exist: {input_path}")

    return CliArgs(day=parsed_day, part=parsed_part, input_path=Path(input_path))


def time_function_call(func: Callable[[], T]) -> tuple[T, float]:
    start_s = time.monotonic()
    result = func()
    stop_s = time.monotonic()
    return result, stop_s - start_s


def main() -> None:
    # Parse CLI args
    parser = make_argparse_parser()
    args = parser.parse_args()
    cli_args = parse_cli_args(args.day, args.part, args.input_path)

    # Run solution
    solver = select_solver(cli_args.day, cli_args.part)
    result, elapsed_s = time_function_call(lambda: solver(cli_args.input_path.read_text()))

    print(f"# Elapsed time (s): {elapsed_s:.3f}")
    print("# Result:")
    print(result)


if __name__ == "__main__":
    main()

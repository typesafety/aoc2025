from __future__ import annotations

from dataclasses import dataclass
from pprint import pprint, pformat  # noqa: F401
from typing import Dict, Set


def solve_part1(puzzle_input: str) -> str:
    grid = parse_grid(puzzle_input)
    first = next_down(grid, grid.start)
    assert first is not None
    index: Index = {}
    build_index(first, grid, index)

    return str(len(index))


def solve_part2(puzzle_input: str) -> str:
    return puzzle_input


@dataclass
class Grid:
    start: Coord
    splitters: set[Coord]


@dataclass(frozen=True)
class Coord:
    x: int
    y: int


type Index = Dict[Coord, Set[Coord]]


def next_down(g: Grid, from_coord: Coord) -> Coord | None:
    match sorted(
        [s for s in g.splitters if s.x == from_coord.x and s.y > from_coord.y],
        key=lambda coord: coord.y,
    ):
        case []:
            return None
        case [c, *_rest]:
            return c
        case _:
            assert False


def build_index(coord: Coord, grid: Grid, acc: Index) -> None:
    if coord in acc:
        return

    child_coords = {
        c
        for c in {
            next_down(grid, Coord(child_x, coord.y)) for child_x in (coord.x - 1, coord.x + 1)
        }
        if c is not None
    }
    acc[coord] = child_coords

    for c in child_coords:
        build_index(c, grid, acc)


def parse_grid(puzzle_input: str) -> Grid:
    start: Coord | None = None
    splitters: set[Coord] = set()
    for y, row in enumerate(puzzle_input.splitlines()):
        for x, char in enumerate(row):
            match char:
                case ".":
                    continue
                case "^":
                    splitters.add(Coord(x, y))
                case "S":
                    start = Coord(x, y)
                case _:
                    assert False

    assert start is not None
    return Grid(start=start, splitters=splitters)

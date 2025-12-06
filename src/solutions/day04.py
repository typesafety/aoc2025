from __future__ import annotations

import copy
from dataclasses import dataclass
from pprint import pprint, pformat  # noqa: F401


def solve_part1(puzzle_input: str) -> str:
    grid = make_grid(puzzle_input)
    accessible = {p for p in grid.rolls if grid.accessible(p)}
    return str(len(accessible))


def solve_part2(puzzle_input: str) -> str:
    starting_grid = make_grid(puzzle_input)

    def shave(grid: Grid) -> int:
        accessible = {p for p in grid.rolls if grid.accessible(p)}
        if len(accessible) == 0:
            return 0

        new_grid = copy.copy(grid)
        for p in accessible:
            new_grid.points[p] = "."

        return len(accessible) + shave(new_grid)

    shaved = shave(starting_grid)

    return str(shaved)


def make_grid(puzzle_input: str) -> Grid:
    lines = puzzle_input.splitlines()
    lines = ["." * len(lines)] + lines + ["." * len(lines)]
    lines = [f".{line}." for line in lines]

    points: dict[Point, str] = {}
    for x in range(0, len(lines[0])):
        for y in range(0, len(lines)):
            points[Point(x, y)] = lines[y][x]

    return Grid(points)


def adjacents(p: Point) -> set[Point]:
    return {
        Point(p.x - 1, p.y - 1),
        Point(p.x - 0, p.y - 1),
        Point(p.x + 1, p.y - 1),
        Point(p.x - 1, p.y),
        Point(p.x + 1, p.y),
        Point(p.x - 1, p.y + 1),
        Point(p.x - 0, p.y + 1),
        Point(p.x + 1, p.y + 1),
    }


@dataclass
class Grid:
    points: dict[Point, str]  # True = roll of paper

    @property
    def rolls(self) -> set[Point]:
        return {p for p in self.points if self.points[p] == "@"}

    def accessible(self, p: Point) -> bool:
        occupied_adjacents = {p for p in adjacents(p) if self.points[p] == "@"}
        return len(occupied_adjacents) < 4

@dataclass(frozen=True)
class Point:
    x: int
    y: int

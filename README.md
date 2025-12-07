# aoc2025

Solutions for [Advent of Code 2025](https://adventofcode.com/2025)

Solutions are located in
[src/solutions/](https://github.com/typesafety/aoc2025/tree/main/src/solutions).

## Running

Run with [`uv`](https://github.com/astral-sh/uv):

```shell
$ uv run main.py --help
usage: aoc2025 [-h] -d [1..12] -p {1,2} -i PUZZLE_INPUT_PATH

Advent of Code 2025

options:
  -h, --help            show this help message and exit
  -d [1..12], --day [1..12]
                        Day (1-12)
  -p {1,2}, --part {1,2}
                        Part (1-2)
  -i PUZZLE_INPUT_PATH, --input_path PUZZLE_INPUT_PATH
                        Path to puzzle input
```

Example:

```shell
$ uv run main.py -d 7 -p 2 -i path/to/input.txt
```

from __future__ import annotations


def solve_part1(puzzle_input: str) -> str:
    banks = puzzle_input.strip().splitlines()
    return str(sum(largest_joltage(bank, num_batteries=2) for bank in banks))


def solve_part2(puzzle_input: str) -> str:
    banks = puzzle_input.strip().splitlines()
    return str(sum(largest_joltage(bank, num_batteries=12) for bank in banks))


def largest_joltage(bank: str, num_batteries: int) -> int:
    batteries = [int(d) for d in bank]
    sequence = largest_sequence(batteries, num_batteries - 1)

    return int("".join([str(d) for d in sequence]))


def largest_sequence(bank: list[int], remaining_steps: int) -> list[int]:
    # Ensure we pick only from batteries that leave enough remaining in the rest
    # of the bank.
    match bank[: len(bank) - remaining_steps]:
        case []:
            return []
        case candidates:
            top, top_ix = candidates[0], 0

            for ix, n in enumerate(candidates):
                if n > top:
                    top, top_ix = n, ix

            rest = (
                largest_sequence(bank[top_ix + 1 :], remaining_steps - 1)
                if remaining_steps > 0
                else []
            )
            return [top, *rest]

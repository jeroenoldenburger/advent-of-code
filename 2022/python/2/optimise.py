from collections.abc import Iterator
from enum import Enum


class Move(Enum):
    ROCK = 0
    PAPER = 1
    SCISSORS = 2

# get points for a round
# use opponents move.value as row index
# use my move.value as column index
points = [
    [3 , 6 , 0],
    [0 , 3 , 6],
    [6 , 0 , 3],
]

def iterate_input_lines(case) -> Iterator[str]:
    with open(case) as input_file:
        for line in input_file:
            if not line.startswith("#"):
                yield line.strip()


def parse_line(line) -> (Move, Move):
    def cast_char(char, options):
        if char == options[0]:
            return Move.ROCK
        elif char == options[1]:
            return Move.PAPER
        elif char == options[-1]:
            return Move.SCISSORS
    return cast_char(line[0], "ABC"), cast_char(line[-1], "XYZ")


def solve(case) -> int:
    moves = [ parse_line(line) for line in iterate_input_lines(case) ]
    return sum([points[opponent.value][me.value] + (me.value + 1) for opponent, me in moves])


if __name__ == '__main__':
    print(solve("input.txt"))
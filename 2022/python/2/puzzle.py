from enum import Enum


class HandShape(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3


class OpponentShape(Enum):
    A = HandShape.ROCK
    B = HandShape.PAPER
    C = HandShape.SCISSORS


class MyShape(Enum):
    X = HandShape.ROCK
    Y = HandShape.PAPER
    Z = HandShape.SCISSORS


def score(opponent_shape, my_shape):
    if opponent_shape.value == HandShape.ROCK:
        if my_shape.value == HandShape.ROCK:
            return 3
        elif my_shape.value == HandShape.PAPER:
            return 6
        elif my_shape.value == HandShape.SCISSORS:
            return 0
    elif opponent_shape.value == HandShape.PAPER:
        if my_shape.value == HandShape.ROCK:
            return 0
        elif my_shape.value == HandShape.PAPER:
            return 3
        elif my_shape.value == HandShape.SCISSORS:
            return 6
    elif opponent_shape.value == HandShape.SCISSORS:
        if my_shape.value == HandShape.ROCK:
            return 6
        elif my_shape.value == HandShape.PAPER:
            return 0
        elif my_shape.value == HandShape.SCISSORS:
            return 3


def solve(case):
    lines = open(case).read().splitlines()
    rounds = [line.strip().split(" ") for line in lines if not line.startswith("#")]
    moves = [(OpponentShape[opponent], MyShape[me]) for opponent, me in rounds]
    scores = [score(opponent_shape, my_shape) + my_shape.value.value for opponent_shape, my_shape in moves]
    return sum(scores)


if __name__ == '__main__':
    print(solve("input.txt"))

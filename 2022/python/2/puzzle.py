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


class Outcome(Enum):
    X = 0  # loose
    Y = 3  # draw
    Z = 6  # win


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


def score_part2(opponent_shape, outcome):
    if opponent_shape.value == HandShape.ROCK:
        if outcome == Outcome.X:
            return 0 + HandShape.SCISSORS.value
        elif outcome == Outcome.Y:
            return 3 + HandShape.ROCK.value
        elif outcome == Outcome.Z:
            return 6 + HandShape.PAPER.value
    elif opponent_shape.value == HandShape.PAPER:
        if outcome == Outcome.X:
            return 0 + HandShape.ROCK.value
        elif outcome == Outcome.Y:
            return 3 + HandShape.PAPER.value
        elif outcome == Outcome.Z:
            return 6 + HandShape.SCISSORS.value
    elif opponent_shape.value == HandShape.SCISSORS:
        if outcome == Outcome.X:
            return 0 + HandShape.PAPER.value
        elif outcome == Outcome.Y:
            return 3 + HandShape.SCISSORS.value
        elif outcome == Outcome.Z:
            return 6 + HandShape.ROCK.value


def solve(case):
    lines = open(case).read().splitlines()
    rounds = [line.strip().split(" ") for line in lines if not line.startswith("#")]
    moves = [(OpponentShape[opponent], MyShape[me]) for opponent, me in rounds]
    scores = [score(opponent_shape, my_shape) + my_shape.value.value for opponent_shape, my_shape in moves]
    return sum(scores)


def solve_part2(case):
    lines = open(case).read().splitlines()
    rounds = [line.strip().split(" ") for line in lines if not line.startswith("#")]
    moves = [(OpponentShape[opponent], Outcome[outcome]) for opponent, outcome in rounds]
    scores = [score_part2(opponent_shape, outcome) for opponent_shape, outcome in moves]
    return sum(scores)


if __name__ == '__main__':
    print(solve_part2("input.txt"))

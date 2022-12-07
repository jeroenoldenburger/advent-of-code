from enum import Enum
from common import iterate_input_lines
import networkx as nx

class Move(Enum):
    ROCK = 0
    PAPER = 1
    SCISSORS = 2

game = nx.DiGraph()
game.add_edge(Move.ROCK, Move.PAPER)
game.add_edge(Move.PAPER, Move.SCISSORS)
game.add_edge(Move.SCISSORS, Move.ROCK)

def score(me, opponent):
    paths = nx.shortest_path(game, source=me, target=opponent)
    hops = len(paths)
    my_move_score = 0
    if hops == 1:
        my_move_score = 3
    elif hops == 3:
        my_move_score = 6
    return my_move_score + (me.value + 1)


def parse_line(line) -> (str, str):
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
    return sum( [score(me, opponent) for opponent, me in moves])


if __name__ == '__main__':
    print(solve("input.txt"))
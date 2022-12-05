import re
from collections import namedtuple
Move = namedtuple('Move', ['number', 'from_stack', 'to_stack'])


class Stacks:
    def __init__(self):
        self.stacks = {}

    def add(self, stack, value):
        if value:
            if stack not in self.stacks:
                self.stacks[stack] = [value]
            else:
                self.stacks[stack].append(value)

    def move(self, stack1, stack2):
        self.stacks[stack2].append(self.stacks[stack1].pop())

    def reverse(self):
        for key in self.stacks:
            self.stacks[key].reverse()

    def apply(self, move: Move):
        for _ in range(move.number):
            self.move(move.from_stack, move.to_stack)

    def apply_move9001(self, move: Move):
        self.stacks[move.to_stack] += self.stacks[move.from_stack][-move.number:]
        self.stacks[move.from_stack] = self.stacks[move.from_stack][0:-move.number]

    def __str__(self):
        keys = sorted(self.stacks.keys())
        return "".join([self.stacks[key][-1][1:-1] for key in keys])


def split_in_stacks(line):
    line_length = len(line)
    num_of_stacks = (line_length // 4) + 1
    stack_values = []
    for i in range(num_of_stacks):
        start = i * 4
        stack_values.append(line[start:start+3].strip())
    return stack_values


def split_in_move(line):
    parts = re.findall(r"move (\d+) from (\d+) to (\d+)", line)[0]
    return Move(*[int(x) for x in parts])


def parse_file(case):
    stacks = Stacks()
    moves = []
    lines = open(case).read().splitlines()
    building_stacks = True
    for line in lines:
        if building_stacks:
            stack_values = split_in_stacks(line)
            if stack_values and len(stack_values[0]) == 1:
                building_stacks = False
                stacks.reverse()
            else:
                for i, value in enumerate(stack_values):
                    stacks.add(i+1, value)
        else:
            if line:
                moves.append(split_in_move(line))
    return stacks, moves


def solve(case):
    stacks, moves = parse_file(case)
    for move in moves:
        stacks.apply(move)
    return stacks


def solve_part2(case):
    stacks, moves = parse_file(case)
    for move in moves:
        stacks.apply_move9001(move)
    return stacks


if __name__ == '__main__':
    # print(solve('example.txt'))
    print(solve_part2('input.txt'))

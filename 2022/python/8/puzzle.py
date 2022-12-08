import functools

from common import iterate_input_lines

class Tree:
    height: int
    visible: bool
    sight: [int]

    def __init__(self, height):
        self.height = height
        self.visible = False
        self.sight = []

    def __str__(self):
        return f"{self.height}"

    def scenic_score(self):
        return functools.reduce(lambda a, b: a * b, self.sight)


def parse_input(case):
    return [[Tree(int(char)) for char in line] for line in iterate_input_lines(case)]


def rotate_matrix(matrix):
    return list(zip(*reversed(matrix)))


def mark_visible_trees_from_left(matrix):
    for row in matrix:
        previous_height = -1
        for tree in row:
            if tree.height > previous_height:
                tree.visible = True
                previous_height = tree.height


def from_4_sides(matrix, func):
    for i in range(4):
        func(matrix)
        matrix = rotate_matrix(matrix)
    return matrix


def compute_tree_sight_to_right(matrix):
    for row in matrix:
        for count in range(len(row)):
            partial_row = row[len(row)-1-count:]
            for i, tree in enumerate(partial_row[1:]):
                if tree.height >= partial_row[0].height:
                    partial_row[0].sight.append(i + 1)
                    break
            else:
                partial_row[0].sight.append(len(partial_row)-1)


def solve(case):
    matrix = parse_input(case)
    matrix = from_4_sides(matrix, mark_visible_trees_from_left)
    return sum([1 if tree.visible else 0 for row in matrix for tree in row])


def solve2(case):
    matrix = parse_input(case)
    matrix = from_4_sides(matrix, compute_tree_sight_to_right)
    return max([ tree.scenic_score() for row in matrix for tree in row])


if __name__ == '__main__':
    print(solve2("input.txt"))
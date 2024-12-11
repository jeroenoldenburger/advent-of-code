import functools
from copy import copy

import numpy as np


def part1(input_file_path):
    puzzle_input = np.loadtxt(input_file_path, dtype=int, delimiter=' ')
    times = 25
    for i in range(times):
        puzzle_input = blink(puzzle_input)
        print(f"Num of stones = {puzzle_input.shape[0]}")


def part2(input_file_path):
    puzzle_input = np.loadtxt(input_file_path, dtype=int, delimiter=' ')
    times = 75
    num_of_stones = 0
    for val in puzzle_input:
        puzzle_input_part = np.array([val])
        print(f"Solve puzzle part {puzzle_input_part}")
        for i in range(times):
            puzzle_input_part = blink(puzzle_input_part)
            print(f"Num of stones in part = {puzzle_input_part.shape[0]}")
        num_of_stones += puzzle_input_part.shape[0]
    print(f"Num of stones in total = {num_of_stones}")


@functools.lru_cache(maxsize=None)
def has_even_num_of_digits(value):
    return len(str(value)) % 2 == 0


@functools.lru_cache(maxsize=None)
def split(value):
    str_value = str(value)
    pos = int(len(str_value) / 2)
    return [int(str_value[0:pos]), int(str_value[pos:])]


def blink(line: np.ndarray):
    indexes_with_zero = np.where(line == 0)[0].tolist()
    indexes_with_even_num_of_digits = [i for i, x in enumerate(line) if has_even_num_of_digits(x)]
    other_indexes = np.setdiff1d(
        range(0, line.shape[0]), indexes_with_zero + indexes_with_even_num_of_digits, assume_unique=False
    ).tolist()

    line[indexes_with_zero] = 1
    line[other_indexes] = line[other_indexes] * 2024

    for counter, index in enumerate(indexes_with_even_num_of_digits):
        actual_index = index + counter
        line[actual_index], new_value = split(line[actual_index])
        line = np.insert(line, actual_index + 1, new_value)

    return line


if __name__ == '__main__':
    # part1('input.txt')
    part2('input.txt')
    exit(0)

from itertools import pairwise
from utils import iterate_input_lines


def __is_valid(mylist: list[int]):
    is_incr = all(a < b for a, b in pairwise(mylist))
    if not is_incr:
        is_decl = all(a > b for a, b in pairwise(mylist))
        if not is_decl:
            return False
    return all(abs(a - b) < 4 for a, b in pairwise(mylist))


def part1_pure_python(input_file_path):

    valid_reports = 0
    for line in iterate_input_lines(input_file_path):
        cols = [int(x) for x in line.split(" ")]
        if __is_valid(cols):
            valid_reports += 1
    print(valid_reports)


def part2_pure_python(input_file_path):

    valid_reports = 0
    for line in iterate_input_lines(input_file_path):
        cols = [int(x) for x in line.split(" ")]
        valid = __is_valid(cols)
        if not valid:
            for n in range(len(cols)):
                tmp_report = cols[:n] + cols[n + 1 :]
                tmp_resp = __is_valid(tmp_report)
                valid = True if tmp_resp else valid
        if valid:
            valid_reports += 1

    print(valid_reports)


if __name__ == '__main__':
    part2_pure_python("input.txt")
    exit(0)


def get_range(input):
    first, second = input.split("-")
    return range(int(first), int(second))


def get_assignments(input):
    first, second = input.split(",")
    return get_range(first), get_range(second)


def is_range_in_range(range1, range2):
    return (range1.start in range2 or range1.start == range2.stop) and\
           (range1.stop in range2 or range1.stop == range2.stop)


def ranges_overlap(range1, range2):
    return (range1.start in range2 or range1.start == range2.stop) or\
           (range1.stop in range2 or range1.stop == range2.stop)


def solve(case):
    lines = open(case).read().splitlines()
    assignments = [get_assignments(line) for line in lines]
    overlapping = [assignment
                   for assignment in assignments
                   if is_range_in_range(assignment[0], assignment[1]) or
                   is_range_in_range(assignment[1], assignment[0])]
    return len(overlapping)


def solve_part2(case):
    lines = open(case).read().splitlines()
    assignments = [get_assignments(line) for line in lines]
    overlapping = [assignment
                   for assignment in assignments
                   if ranges_overlap(assignment[0], assignment[1]) or
                   ranges_overlap(assignment[1], assignment[0])]
    return len(overlapping)


if __name__ == '__main__':
    # print(solve("example.txt"))
    # print(solve("input.txt"))
    print(solve_part2("input.txt"))
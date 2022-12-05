import itertools


def get_item_priority(char):
        value = ord(char)
        if 65 <= value <= 90:
            return value - 38
        elif 97 <= value <= 122:
            return value - 96
        else:
            return None


def get_failed_item(line):
    compartment_length = int(len(line) / 2)
    first_compartment = line[0:compartment_length]
    second_compartment = line[compartment_length:]
    for char in first_compartment:
        if char in second_compartment:
            return char


def solve(case):
    lines = open(case).read().splitlines()
    return sum([get_item_priority(get_failed_item(line)) for line in lines])


def by_triples(iterable):
    it = iter(iterable)
    triple = tuple(itertools.islice(it, 3))
    while triple:
        yield triple
        triple = tuple(itertools.islice(it, 3))


def solve_part2(case):
    lines = open(case).read().splitlines()
    result = 0
    for three_lines in by_triples(lines):
        for char in three_lines[0]:
            if char in three_lines[1] and char in three_lines[2]:
                result += get_item_priority(char)
                break

    return result



if __name__ == '__main__':
    # print(solve_part2("example.txt"))
    print(solve_part2("input.txt"))
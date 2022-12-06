def detect_unique_chars(stream, count):
    found_marker = []
    for i, char in enumerate(stream):
        if char in found_marker:
            found_marker = found_marker[found_marker.index(char)+1:]
        found_marker.append(char)
        if len(found_marker) == count:
            break
    return i + 1


def solve(case):
    stream = open(case).read()
    return detect_unique_chars(stream, 4)


def solve_part2(case):
    stream = open(case).read()
    return detect_unique_chars(stream, 14)


if __name__ == '__main__':
    print(solve_part2('input.txt'))
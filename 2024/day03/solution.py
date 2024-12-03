import re

# reading the puzzle, it immediatly showed that was something for regexes. Finding some particular
# substring multiple times, ignoring the rest of a string. Since regex is available in python, no
# need for an external library today


def part1(input_file_path):
    with open(input_file_path) as input_file:
        puzzle_input = input_file.read()
        matches = re.finditer(r"mul\(\d{1,3},\d{1,3}\)", puzzle_input, re.MULTILINE)
        res = 0
        for _, match in enumerate(matches, start=1):
            digit_matches = re.search(r"(\d{1,3}),(\d{1,3})", match.group())
            if digit_matches:
                res += int(digit_matches.group(1)) * int(digit_matches.group(2))
    print(res)


def part2(input_file_path):
    with open(input_file_path) as input_file:
        puzzle_input = input_file.read()
        matches = re.finditer(r"mul\(\d{1,3},\d{1,3}\)|don?'?t?\(\)", puzzle_input, re.MULTILINE)
        res = 0
        enabled = True
        for _, match in enumerate(matches, start=1):
            found = match.group()
            if found.startswith("don"):
                enabled = False
            elif found.startswith("do"):
                enabled = True
            elif enabled:
                digit_matches = re.search(r"(\d{1,3}),(\d{1,3})", match.group())
                if digit_matches:
                    res += int(digit_matches.group(1)) * int(digit_matches.group(2))
    print(res)


if __name__ == '__main__':
    part2('input.txt')
    exit(0)

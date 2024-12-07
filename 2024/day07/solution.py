import itertools
import re
from copy import copy


def part1(input_file_path):
    possible_operators = ["*", "+"]
    total_calibration = 0

    pattern = re.compile("(^\d+|[\\+|\\*]\d+)")

    with open(input_file_path) as input_file:
        for line in input_file:
            # print(line)
            outcome, expression = line.strip().split(":")
            outcome = int(outcome.strip())
            expression = expression.strip()
            num_of_operators = expression.count(" ")
            proposed_solutions = itertools.product(possible_operators, repeat=num_of_operators)
            for proposed_solution in proposed_solutions:
                proposed_expression = copy(expression)
                for operator in proposed_solution:
                    proposed_expression = proposed_expression.replace(" ", str(operator), 1)

                parts = re.findall(pattern, proposed_expression)
                proposed_outcome = 0
                for part in parts:
                    if proposed_outcome == 0:
                        proposed_outcome = int(part)
                    else:
                        proposed_outcome = eval(f"{proposed_outcome}{part}")

                if outcome == proposed_outcome:
                    total_calibration += outcome
                    break
    print(f"Total calibration: {total_calibration}")


def part2(input_file_path):
    possible_operators = ["*", "+", "|"]
    total_calibration = 0

    pattern = re.compile("(^\d+|[\\+|\\*|\\|\\|]\d+)")

    with open(input_file_path) as input_file:
        for line in input_file:
            # print(line)
            outcome, expression = line.strip().split(":")
            outcome = int(outcome.strip())
            expression = expression.strip()
            num_of_operators = expression.count(" ")
            proposed_solutions = itertools.product(possible_operators, repeat=num_of_operators)
            for proposed_solution in proposed_solutions:
                proposed_expression = copy(expression)
                for operator in proposed_solution:
                    proposed_expression = proposed_expression.replace(" ", str(operator), 1)

                parts = re.findall(pattern, proposed_expression)
                proposed_outcome = 0
                for part in parts:
                    if proposed_outcome == 0:
                        proposed_outcome = int(part)
                    else:
                        if part[0] == "|":
                            proposed_outcome = int(f"{proposed_outcome}{part[1:]}")
                        else:
                            proposed_outcome = eval(f"{proposed_outcome}{part}")

                if outcome == proposed_outcome:
                    total_calibration += outcome
                    break
    print(f"Total calibration: {total_calibration}")


if __name__ == '__main__':
    part2("input.txt")
    exit(0)

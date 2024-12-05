import numpy as np


def part1(input_file_path):
    with open(input_file_path) as input_file:
        puzzle_input = input_file.read()
    (ordering_rules_input, updates_input) = puzzle_input.split('\n\n')
    ordering_rules = np.genfromtxt(ordering_rules_input.split('\n'), delimiter='|', dtype=int)
    updates = [[int(page) for page in update_input.split(',')] for update_input in updates_input.split('\n')]
    valid_middle_pages = []
    for update in updates:
        for page in update:
            rules_with_page = np.any(ordering_rules == page, axis=1)
            applicable_rules = ordering_rules[rules_with_page]
            for applicable_rule in applicable_rules:
                if applicable_rule[0] == page:
                    if (applicable_rule[1] in update) and update.index(page) > update.index(applicable_rule[1]):
                        print("invalid update")
                        break
                else:
                    if (applicable_rule[0] in update) and update.index(page) < update.index(applicable_rule[0]):
                        print("invalid update")
                        break
            else:
                # print("valid update for this page")
                continue
            break
        else:
            print("valid update")
            middle_index = int(len(update) / 2)
            valid_middle_pages.append(update[middle_index])
    print(sum(valid_middle_pages))


def part2(input_file_path):
    with open(input_file_path) as input_file:
        puzzle_input = input_file.read()
    (ordering_rules_input, updates_input) = puzzle_input.split('\n\n')
    ordering_rules = np.genfromtxt(ordering_rules_input.split('\n'), delimiter='|', dtype=int)
    updates = [[int(page) for page in update_input.split(',')] for update_input in updates_input.split('\n')]
    invalid_updates = []
    for update in updates:
        for page in update:
            rules_with_page = np.any(ordering_rules == page, axis=1)
            applicable_rules = ordering_rules[rules_with_page]
            for applicable_rule in applicable_rules:
                if applicable_rule[0] == page:
                    if (applicable_rule[1] in update) and update.index(page) > update.index(applicable_rule[1]):
                        print("invalid update")
                        invalid_updates.append(update)
                        break
                else:
                    if (applicable_rule[0] in update) and update.index(page) < update.index(applicable_rule[0]):
                        print("invalid update")
                        invalid_updates.append(update)
                        break
            else:
                # print("valid update for this page")
                continue
            break
        else:
            print("valid update")
    fixed_middle_pages = []
    fixed_updates = []
    for invalid_update in invalid_updates:
        mentions = np.isin(ordering_rules, invalid_update)
        rules_for_update = np.any(mentions, axis=1)
        applicable_rules = ordering_rules[rules_for_update]
        while 1 > 0:
            for applicable_rule in applicable_rules:
                if applicable_rule[0] in invalid_update and applicable_rule[1] in invalid_update:
                    pos_0 = invalid_update.index(applicable_rule[0])
                    pos_1 = invalid_update.index(applicable_rule[1])
                    if pos_1 < pos_0:
                        invalid_update[pos_0] = applicable_rule[1]
                        invalid_update[pos_1] = applicable_rule[0]
                        break
            else:
                break
        print(invalid_update)
        fixed_updates.append(invalid_update)
    for fixed_update in fixed_updates:
        middle_index = int(len(fixed_update) / 2)
        fixed_middle_pages.append(fixed_update[middle_index])
    print(sum(fixed_middle_pages))


if __name__ == '__main__':
    part2('input.txt')
    exit(0)

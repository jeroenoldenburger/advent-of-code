import math
from dataclasses import dataclass
from common import iterate_input_lines

@dataclass
class Monkey:
    items: [int]
    operation: str
    divide_by: int
    monkey_to_throw_to: [str]
    inspect_counter: int

    def __init__(self):
        self.items = list()
        self.monkey_to_throw_to = ["",""]
        self.inspect_counter = 0

    def inspect(self, level):
        self.inspect_counter += 1
        return eval(self.operation, {}, {'old':level})

    def throw_to_monkey(self, level):
        if level % self.divide_by == 0:
            return self.monkey_to_throw_to[0]
        else:
            return self.monkey_to_throw_to[1]

def parse_input_to_monkeys(case) ->  dict[str, Monkey]:
    monkeys = {}
    cur_monkey_key = None
    for line in iterate_input_lines(case):
        line = line.strip()
        if line.startswith("Monkey"):
            monkey_number = line.split()[1].split(":")[0]
            cur_monkey_key = monkey_number
            monkeys[cur_monkey_key] = Monkey()
        elif line.startswith("Starting items"):
            items = line.split(":")[1]
            monkeys[cur_monkey_key].items = [int(item) for item in items.split(",")]
        elif line.startswith("Operation"):
            monkeys[cur_monkey_key].operation = line.split("=")[1]
        elif line.startswith("Test: divisible by"):
            monkeys[cur_monkey_key].divide_by = int(line.split()[-1])
        elif line.startswith("If true: "):
            monkeys[cur_monkey_key].monkey_to_throw_to[0] = line.split()[-1]
        elif line.startswith("If false: "):
            monkeys[cur_monkey_key].monkey_to_throw_to[1] = line.split()[-1]
    return monkeys

def solve(case):
    monkeys = parse_input_to_monkeys(case)
    lcm = math.lcm(*[monkey.divide_by for monkey in monkeys.values()])
    for i in range(10000):
        for monkey_number, monkey in monkeys.items():
            for item in monkey.items:
                new_level = monkey.inspect(item)
                # relieved_level = floor(new_level / 3)
                relieved_level = new_level % lcm
                to_monkey = monkey.throw_to_monkey(relieved_level)
                monkeys[to_monkey].items.append(relieved_level)
            monkey.items = []
    times = [monkey.inspect_counter for monkey in monkeys.values()]
    times.sort(reverse=True)
    print(f"Money business score: {times[0] * times[1]}")


if __name__ == '__main__':
    solve("input.txt")
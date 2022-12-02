class Inventory:
    item_calories: [int]

    def __init__(self, item_calories: [int]):
        self.item_calories = item_calories

    def calorie_sum(self) -> int:
        return sum(x for x in self.item_calories)


class Elf:
    inventory: Inventory

    def __init__(self, inventory: Inventory):
        self.inventory = inventory

    def inventory_calorie_sum(self) -> int:
        return self.inventory.calorie_sum()


def get_elves() -> [Elf]:
    lines = open("input.txt").read().splitlines()
    global elves
    elves = []
    item_calories = []
    for line in lines:
        if not line:
            elves.append(Elf(inventory=Inventory(item_calories=item_calories)))
            item_calories = []
        else:
            item_calories.append(int(line))
    if item_calories:
        elves.append(Elf(inventory=Inventory(item_calories=item_calories)))
    return elves


def solve_part1() -> int:
    elf_with_largest_inventory = max(elves, key=lambda elf: elf.inventory_calorie_sum())
    return elf_with_largest_inventory.inventory_calorie_sum()


def solve_part2() -> int:
    elves.sort(key=lambda elf: elf.inventory_calorie_sum(), reverse=True)
    return sum([elf.inventory_calorie_sum() for elf in elves[0:3]])


if __name__ == '__main__':
    get_elves()
    print(solve_part2())

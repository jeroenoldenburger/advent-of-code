import re
from dataclasses import dataclass
from math import inf

from common import iterate_input_lines

@dataclass
class Blueprint:
    ore_robot_cost: int = inf
    clay_robot_cost: int = inf
    obsidian_robot_cost: (int, int) = (inf, inf)
    geode_robot_cost: (int, int) = (inf, inf)


@dataclass
class Inventory:
    ore: int = 0
    clay: int = 0
    obsidian: int = 0
    geode: int = 0
    ore_robot: int = 0
    clay_robot: int = 0
    obsidian_robot: int = 0
    geode_robot: int = 0

    def produce(self, blueprint: Blueprint):
        production = Inventory()
        production.geode_robot = self.create_robot('obsidian', blueprint.geode_robot_cost)
        production.obsidian_robot = self.create_robot('clay', blueprint.obsidian_robot_cost)
        production.clay_robot = self.create_robot('ore', blueprint.clay_robot_cost)
        production.ore_robot = self.create_robot('ore', blueprint.ore_robot_cost)
        self.geode += self.geode_robot
        if self.geode_robot:
            print(f"{self.geode_robot} geode-collecting robot collects {self.geode_robot} geode; you now have {self.geode} geode.")
        self.obsidian += self.obsidian_robot
        if self.obsidian_robot:
            print(f"{self.obsidian_robot} obsidian-collecting robot collects {self.obsidian_robot} obsidian; you now have {self.obsidian} obsidian.")
        self.clay += self.clay_robot
        if self.clay_robot:
            print(f"{self.clay_robot} clay-collecting robot collects {self.clay_robot} clay; you now have {self.clay} clay.")
        self.ore += self.ore_robot
        if self.ore_robot:
            print(f"{self.ore_robot} ore-collecting robot collects {self.ore_robot} ore; you now have {self.ore} ore.")
        self.geode_robot += production.geode_robot
        self.obsidian_robot += production.obsidian_robot
        self.clay_robot += production.clay_robot
        self.ore_robot += production.ore_robot

    def create_robot(self, material, costs):
        if isinstance(costs, tuple):
            num_of_robots = min(self.__getattribute__(material) // costs[0], self.ore // costs[1])
        else:
            num_of_robots = self.__getattribute__(material) // costs
        if num_of_robots:
            if isinstance(costs, tuple):
                self.__setattr__(material, self.__getattribute__(material) - costs[0] * num_of_robots)
                self.ore -= costs[1] * num_of_robots
                print(f"Build robot with {costs * num_of_robots} {material} and {costs[1] * num_of_robots} ore")
            else:
                self.__setattr__(material, self.__getattribute__(material) - costs * num_of_robots)
                print(f"Build robot with {costs * num_of_robots} {material}")

        return num_of_robots







def solve(case):
    blueprints = []
    for line in iterate_input_lines(case):
        pattern = r'Blueprint (\d+): Each ore robot costs (\d+) ore. Each clay robot costs (\d+) ore. Each obsidian robot costs (\d+) ore and (\d+) clay. Each geode robot costs (\d+) ore and (\d+) obsidian.'
        res = re.search(pattern, line)
        res1 = res.groups()
        blueprints.append(Blueprint(ore_robot_cost=int(res1[1]), clay_robot_cost=int(res1[2]),obsidian_robot_cost=(int(res1[3]),int(res1[4])), geode_robot_cost=(int(res1[5]),int(res1[6]))))

    for idx, blueprint in enumerate(blueprints):
        inventory = Inventory(ore_robot=1)
        for i in range(24):
            print(f"== Minute {i+1} ==")
            inventory.produce(blueprint)
        print(f"Blueprint {idx} collected {inventory.geode} geodes")

    pass



if __name__ == '__main__':
    solve("example.txt")
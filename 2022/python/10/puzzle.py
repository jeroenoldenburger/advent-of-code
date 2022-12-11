from dataclasses import dataclass
from common import iterate_input_lines
from math import floor

@dataclass
class Device:
    cycles: int = 0
    cpu_x: int  = 1
    add_signal_strength_at_cyles = [20, 60, 100, 140, 180, 220]
    sum_signal_strength = 0
    crt = [["_" for col in range(40)] for row in range(6)]

    def cycle(self):
        self.cycles += 1
        if self.cycles in self.add_signal_strength_at_cyles:
            self.sum_signal_strength += self.signal_strength()
        self.draw_pixel()

    def cpu_addx(self, x):
        self.cycle()
        self.cycle()
        self.cpu_x += x

    def cpu_noop(self):
        self.cycle()

    def signal_strength(self):
        return self.cycles * self.cpu_x

    def print_crt(self):
        print("\n".join(["".join(row)for row in self.crt]))

    def draw_pixel(self):
        zero_based_cycles = self.cycles - 1
        row = floor( zero_based_cycles / 40)
        col = zero_based_cycles % 40

        if col in {self.cpu_x - 1, self.cpu_x, self.cpu_x + 1}:
            self.pixels[zero_based_cycles] = "#"
        self.crt[row][col] = "#" if col in [self.cpu_x -1, self.cpu_x, self.cpu_x + 1] else "."


def solve(case):
    instructions = [line.split() for line in iterate_input_lines(case)]
    device = Device()
    for i, instruction in enumerate(instructions):
        if instruction[0] == 'noop':
            device.cpu_noop()
        elif instruction[0] == 'addx':
            device.cpu_addx(int(instruction[1]))
    device.print_crt()
    return device.sum_signal_strength


if __name__ == '__main__':
    print(solve("input.txt"))
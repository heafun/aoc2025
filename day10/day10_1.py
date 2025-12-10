class Machine:
    def __init__(self, diagramm: list[str]) -> None:
        self.target = 0b0
        self.button_schematics = []

        for index, char in enumerate(diagramm[0].strip("[]")):
            if char == "#":
                self.target = set_bit(self.target, index)

        for button in diagramm[1:-1]:
            schematic = 0b0

            for wiring in button.strip("()").split(","):
                schematic = set_bit(schematic, int(wiring))

            self.button_schematics.append(schematic)


def bfs_get_depth(machine: Machine) -> int:
    depth = 0

    if machine.target == 0b0:  # Just to be sure ;)
        return depth

    current_state_layer = [machine.target]

    while True:
        next_state_layer = []
        depth += 1

        for state in set(current_state_layer):
            for schematic in machine.button_schematics:
                if state ^ schematic == 0b0:
                    return depth

                next_state_layer.append(state ^ schematic)

        current_state_layer = next_state_layer.copy()
        next_state_layer.clear()


def set_bit(value: int, bit_index: int) -> int:
    return value | (1 << bit_index)


with open("day10/input1.txt") as file:
    machines = [Machine(line.strip().split()) for line in file]

button_press_sum = 0

for machine in machines:
    button_press_sum += bfs_get_depth(machine)

print(button_press_sum)

with open("day07/input1.txt") as file:
    lines = [x.strip() for x in file]

beams: set[int] = {lines[0].index("S")}

times_split = 0

for line in lines:
    for beam in beams.copy():
        if line[beam] == "^":
            beams.remove(beam)
            beams.add(beam + 1)
            beams.add(beam - 1)

            times_split += 1

print(times_split)

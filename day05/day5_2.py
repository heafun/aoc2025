with open("day05/input1.txt") as file:
    lines = [x.strip() for x in file]

ranges: list[list[int]] = []

for line in lines:
    if len(line) == 0:
        break

    next_range = [int(x) for x in line.split("-")]

    already_included = False

    for id_range in ranges.copy():
        if id_range[0] <= next_range[0] <= next_range[1] <= id_range[1]:
            already_included = True
            break
        elif id_range[0] <= next_range[0] <= id_range[1]:
            ranges.remove(id_range)
            next_range[0] = id_range[0]
        elif id_range[0] <= next_range[1] <= id_range[1]:
            ranges.remove(id_range)
            next_range[1] = id_range[1]
        elif next_range[0] <= id_range[0] <= id_range[1] <= next_range[1]:
            ranges.remove(id_range)

    ranges.sort(key=lambda id_range: id_range[0])

    if not already_included:
        ranges.append(next_range)

count = 0

print(sum([abs(id_range[0] - id_range[1]) + 1 for id_range in ranges]))

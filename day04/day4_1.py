def count_paper_rolls_around(
    paper_roll_map: list[list[str]],
    pos_x: int,
    pos_y: int,
) -> int:
    counter = 0

    for y in range(pos_y - 1, pos_y + 2):
        if y < 0 or y >= len(paper_roll_map):
            continue

        for x in range(pos_x - 1, pos_x + 2):
            if x < 0 or x >= len(paper_roll_map[0]) or (x == pos_x and y == pos_y):
                continue

            counter += 1 if paper_roll_map[y][x] else 0

    return counter


with open("day04/input1.txt") as file:
    lines = [x.strip() for x in file]

paper_roll_map = [[char == "@" for char in line] for line in lines]

accessable_rolls = 0

for y in range(len(paper_roll_map)):
    for x in range(len(paper_roll_map[y])):
        if not paper_roll_map[y][x]:
            continue

        if count_paper_rolls_around(paper_roll_map, x, y) < 4:
            accessable_rolls += 1

print(accessable_rolls)

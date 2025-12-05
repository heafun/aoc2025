with open("day05/input1.txt") as file:
    lines = [x.strip() for x in file]

ranges: list[list[int]] = []
ingredients: list[int] = []
reading_ranges = True

for line in lines:
    if len(line) == 0:
        reading_ranges = False
        continue

    if reading_ranges:
        ranges.append([int(x) for x in line.split("-")])
    else:
        ingredients.append(int(line))

fresh_ingredient_count = 0

for ingredient in ingredients:
    for id_range in ranges:
        if id_range[0] <= ingredient <= id_range[1]:
            fresh_ingredient_count += 1
            break

print(fresh_ingredient_count)

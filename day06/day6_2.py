from functools import reduce

with open("day06/input1.txt") as file:
    lines = [x.strip("\n") for x in file]

grand_total = 0

columns: list[str] = []
for index in range(len(lines[0]) - 1, -1, -1):
    column = "".join([line[index] for line in lines])

    if len(column.strip()) != 0 or index == 0:
        columns.append(column)

        if index != 0:
            continue

    math_sign = columns[-1][-1]
    numbers = [
        int(number.strip()) for number in ["".join(column[:-1]) for column in columns]
    ]

    if math_sign == "+":
        grand_total += sum(numbers)
    else:
        grand_total += reduce(lambda a, b: a * b, numbers, 1)

    columns.clear()

print(grand_total)

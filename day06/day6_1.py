from functools import reduce

with open("day06/input1.txt") as file:
    lines = [line.split() for line in [x.strip() for x in file]]

grand_total = 0

for index in range(len(lines[0])):
    numbers = [int(number) for number in [line[index] for line in lines[:-1]]]

    if lines[-1][index] == "+":
        grand_total += sum(numbers)
    else:
        grand_total += reduce(lambda a, b: a * b, numbers, 1)

print(grand_total)

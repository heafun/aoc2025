with open("day01/input1.txt") as file:
    lines = [x.strip() for x in file]

zero_pos_count = 0
dial_setting = 50

for line in lines:
    rotation_amount = int(line[1:]) * (-1 if line[0] == "L" else 1)
    dial_setting = dial_setting + rotation_amount

    if dial_setting % 100 == 0:
        zero_pos_count += 1

print(zero_pos_count)

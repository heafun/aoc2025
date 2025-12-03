with open("day01/input1.txt") as file:
    lines = [line.strip() for line in file]

zero_pos_count = 0

dial_setting = 50

for line in lines:
    rotation_amount = int(line[1:])
    signed_rotation_amount = rotation_amount * (-1 if line[0] == "L" else 1)

    full_rotation = abs(int(rotation_amount / 100))
    zero_pos_count += full_rotation

    dial_after_rotation = dial_setting + (rotation_amount % 100) * (
        -1 if line[0] == "L" else 1
    )

    if (dial_setting != 0 and dial_after_rotation <= 0) or dial_after_rotation > 99:
        zero_pos_count += 1

    dial_setting = (dial_setting + signed_rotation_amount) % 100

print(zero_pos_count)

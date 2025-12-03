def index_of_biggest_battery(battery_bank: str) -> int:
    max_index = 0
    max_number = int(battery_bank[0])

    for index, char in enumerate(battery_bank):
        if int(char) == 9:
            return index

        if int(char) > max_number:
            max_index = index
            max_number = int(char)

    return max_index


with open("day03/input1.txt") as file:
    banks = [x.strip() for x in file]

jolt_sum = 0

for bank in banks:
    max_index = index_of_biggest_battery(bank[:-1])
    first_battery = bank[max_index]

    right_of_maxindex = bank[max_index + 1 :]

    second_battery = right_of_maxindex[index_of_biggest_battery(right_of_maxindex)]

    jolt_sum += int(first_battery + second_battery)

print(jolt_sum)

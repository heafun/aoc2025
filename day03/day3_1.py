def index_of_biggest_battery(battery_bank: str):
    max_index = 0
    max_number = int(battery_bank[0])
    
    for index, char in enumerate(battery_bank):
        if int(char) == 9:
            return index
        
        if int(char) > max_number:
            max_index = index
            max_number = int(char)
    
    return max_index

file = open("day03/input1.txt")
banks = list(map(lambda x: x.strip(), file.readlines()))
file.close()

jolt_sum = 0

for bank in banks:
    max_index = index_of_biggest_battery(bank[:-1])
    first_battery = bank[max_index]
    
    left_of_maxindex = bank[max_index+1:]
    
    second_battery = left_of_maxindex[index_of_biggest_battery(left_of_maxindex)]
    
    jolt_sum += int(first_battery + second_battery)

print(jolt_sum)

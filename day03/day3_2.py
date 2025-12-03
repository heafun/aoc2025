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

def get_max_jolt(battery_bank: str, batteries: int) -> str:
    max_index = index_of_biggest_battery(battery_bank[:1 - batteries] if batteries > 1 else battery_bank)
    battery = battery_bank[max_index]
    
    if batteries == 1:
        return battery
    else:
        return battery + get_max_jolt(battery_bank[max_index+1:], batteries - 1)    
    

file = open("day03/input1.txt")
banks = list(map(lambda x: x.strip(), file.readlines()))
file.close()

jolt_sum = 0

for bank in banks:
    jolt_sum += int(get_max_jolt(bank, 12))

print(jolt_sum)

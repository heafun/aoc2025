file = open("day02/input1.txt")
id_ranges = [id_range.strip() for id_range in file.readline().split(',')]
file.close()

invalid_id_count = 0

for id_range in id_ranges:
    start, end = (map(lambda x: int(x), id_range.split('-')))
    
    if len(str(start)) == len(str(end)) and len(str(start)) % 2 != 0:
        continue
    
    for id in range(start, end + 1):
        if len(str(id)) % 2 != 0:
            continue
        
        mid_start_index = int(len(str(id)) / 2)
        
        first_half = str(id)[:mid_start_index]
        second_half = str(id)[mid_start_index:]
        
        if first_half == second_half:
            invalid_id_count += id
            
print(invalid_id_count)
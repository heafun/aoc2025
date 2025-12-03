def split_equal(string: str, part_size: int) -> list[str]:
    part_list: list[str] = list()
    
    start = 0
    end = part_size
    
    while end <= len(string):
        part_list.append(string[start:end])
        
        start += part_size
        end += part_size
        
    return part_list
        

file = open("day02/input1.txt")
id_ranges = [id_range.strip() for id_range in file.readline().split(',')]
file.close()

invalid_id_count = 0

for id_range in id_ranges:
    start, end = (map(lambda x: int(x), id_range.split('-')))
    
    for id in range(start, end + 1):        
        max_part_len = int(len(str(id)) / 2)
        
        for part_len in range(1, max_part_len + 1):
            if len(str(id)) % part_len != 0:
                continue
            
            parts = split_equal(str(id), part_len)
            
            if (len(set(parts))) == 1:
                invalid_id_count += id
                break
        
            
print(invalid_id_count)